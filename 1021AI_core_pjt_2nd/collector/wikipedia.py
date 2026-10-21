"""
collector/wikipedia.py — 한국어 위키백과 API와 통신하는 도구
==============================================================
이 파일은 "화가"를 모른다. 검색어를 받으면 문서를 찾고, 제목을 받으면 본문을 가져올 뿐이다.
(다른 도메인에서도 그대로 쓸 수 있게 분리 — NF2005)

위키미디어 규칙 (NF2006):
  - User-Agent에 연락처를 넣는다
  - 요청 사이에 쉬는 시간을 둔다
  - 실패하면 잠깐 기다렸다 다시 시도한다
"""

import time

import requests

import config

_last_request_time = 0.0


def _get(params: dict) -> dict:
    """위키백과 API에 GET 요청을 보내고 JSON을 돌려준다. (호출 간격·재시도 포함)"""
    global _last_request_time
    params = {"format": "json", "formatversion": 2, **params}
    headers = {"User-Agent": config.WIKI_USER_AGENT}

    for attempt in range(1, config.WIKI_MAX_RETRIES + 1):
        # 직전 요청과의 간격을 지킨다
        wait = config.WIKI_REQUEST_INTERVAL - (time.time() - _last_request_time)
        if wait > 0:
            time.sleep(wait)
        _last_request_time = time.time()

        try:
            response = requests.get(config.WIKI_API_URL, params=params, headers=headers, timeout=30)
            if response.status_code == 429 or response.status_code >= 500:
                raise requests.HTTPError(f"HTTP {response.status_code}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            if attempt == config.WIKI_MAX_RETRIES:
                raise
            print(f"  ⚠️ 위키백과 요청 실패({error}). {5 * attempt}초 후 다시 시도할게요.")
            time.sleep(5 * attempt)
    return {}


def search(query: str, limit: int) -> list[dict]:
    """
    검색어로 문서를 찾아 [{page_id, title, summary}, ...] 를 돌려준다.
    summary는 문서 첫머리 일부분이다. (본문 전체는 아직 받지 않음 → 프롬프트 2가 고른 뒤에 받음)
    """
    data = _get(
        {
            "action": "query",
            "generator": "search",
            "gsrsearch": query,
            "gsrlimit": limit,
            "gsrnamespace": 0,          # 일반 문서만 (토론·사용자 문서 제외)
            "prop": "extracts",
            "exintro": 1,               # 첫 문단만
            "explaintext": 1,           # HTML 말고 글자만
            "exchars": config.SUMMARY_CHARS,
        }
    )
    pages = data.get("query", {}).get("pages", [])
    pages.sort(key=lambda p: p.get("index", 0))  # 검색 순위대로
    return [
        {"page_id": p["pageid"], "title": p["title"], "summary": (p.get("extract") or "").strip()}
        for p in pages
        if "pageid" in p
    ]


def fetch_page(title: str) -> dict | None:
    """
    제목으로 문서 1개의 본문 전체와 원문 URL을 가져온다.
    넘겨주기(redirect) 문서면 실제 문서를 따라간다. 문서가 없으면 None.
    """
    data = _get(
        {
            "action": "query",
            "titles": title,
            "redirects": 1,
            "prop": "extracts|info",
            "explaintext": 1,
            "inprop": "url",
        }
    )
    pages = data.get("query", {}).get("pages", [])
    if not pages or pages[0].get("missing"):
        return None
    page = pages[0]
    return {
        "page_id": page["pageid"],
        "title": page["title"],
        "url": page.get("fullurl", ""),
        "text": (page.get("extract") or "").strip(),
    }
