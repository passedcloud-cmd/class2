    ##############################
    # 알고리즘 메인 부분 구현 시작
    ##############################
    # [붙여넣는 곳]
    #   while 반복문 안의 "알고리즘 메인 부분 구현 시작" ~ "끝" 사이에 있던 코드를
    #   전부 지우고, 이 내용을 통째로 붙여넣기 (앞에 띄어쓰기 4칸 유지!)

    # 1) 서버가 보낸 데이터 읽기
    grid, normal, mega, x_hp, codes = read_game(game_data)

    # 2) 지난 턴에 암호를 풀었다면, 메가 포탄이 늘었는지 보고 성공/실패 확인
    if tried_decode:
        if mega > mega_before:
            print('[암호] 해독 성공! 간격 =', SHIFT)
        else:
            SHIFT = (SHIFT + 1) % 26             # 틀렸으면 다음 간격으로 바꿔서 다시 시도
            print('[암호] 해독 실패... 다음엔 간격', SHIFT, '로 해볼게')
    tried_decode = False

    # 3) 이번 턴에 할 명령 정하기 (혹시 오류가 나도 프로그램이 죽지 않게 try로 감싸기)
    try:
        output = decide(grid, normal, mega, x_hp, codes)
    except Exception as e:
        print('[오류]', e)
        output = 'S'

    if output.startswith('G'):                   # 암호 해독을 시도하는 턴이면 기록해 두기
        tried_decode = True
        mega_before = mega

    print(f'[내 탱크] 일반 포탄 {normal}, 메가 포탄 {mega}, 포탑 체력 {x_hp} → 명령: {output}')

    # 4) 명령을 보내고 다음 턴 데이터 받기
    game_data = submit(output)

    ##############################
    # 알고리즘 메인 부분 구현 끝
    ##############################
