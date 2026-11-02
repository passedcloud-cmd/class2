SELECT
  *
FROM
  tracks
WHERE
  Name LIKE '%love%';



SELECT
  *
FROM
  tracks
WHERE
  Genreid = 1
  AND Milliseconds >= 300000
ORDER BY
  UnitPrice DESC;



SELECT
  Genreid, count(*) as TotalTracks
FROM
  tracks
GROUP BY
  GenreID;



SELECT
  Genreid,
  SUM(UnitPrice) as TotalPrice
FROM
  tracks
GROUP BY
  GenreId
HAVING
  SUM(UnitPrice) >= 100;
