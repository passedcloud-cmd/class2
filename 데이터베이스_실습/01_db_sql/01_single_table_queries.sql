-- Active: 1793582255406@@127.0.0.1@3306
-- 01. Querying data

SELECT
  LastName
FROM
  employees;


SELECT
  FirstName
FROM
  employees;

SELECT
  *
FROM
  employees;

SELECT
  FirstName as '이름', LastName as '성'
FROM
  employees;


SELECT
  Name,
  Milliseconds / 60000 as '재생 시간(분)'
FROM
  tracks;


-- 02. Sorting data
SELECT
  FirstName
FROM
  employees
ORDER BY
  FirstName DESC;


SELECT
  Country, City
FROM
  customers
ORDER BY
  Country DESC,
  City;

SELECT
  Name,
  Milliseconds / 60000 as "재생 시간(분)"
From
  tracks
ORDER BY Milliseconds DESC;


SELECT
  ReportsTo
FROM
  employees
ORDER BY
  ReportsTo;

SELECT DISTINCT
  Country
FROM
  customers
ORDER BY
  Country;


SELECT
  LastName, FirstName, City
FROM
  customers
WHERE
  -- City = 'Prague'
  City = 'Prague';


SELECT
  Company, Country
FROM
  customers
WHERE
  Company IS NULL
  AND Country = 'USA';

SELECT
  Name, Bytes
FROM
  tracks
WHERE
  Bytes BETWEEN 100000 AND 500000
ORDER BY
  Bytes;

SELECT
  Company, Country
FROM
  customers
WHERE
  Country IN ('Canada', 'Germany', 'France');


SELECT
  LastName, FirstName
FROM
  customers
WHERE
  LastName Like 'Peter%'


SELECT
  TrackId, Name, Bytes
FROM
  tracks
ORDER BY Bytes DESC
LIMIT 4 OFFSET 3;


SELECT
  Country, COUNT(*)
FROM 
  customers
GROUP BY
  Country;

SELECT
  Composer,
  AVG(Milliseconds / 60000) as avgOFFMinute
FROM
  tracks
GROUP BY
  Composer
ORDER BY
  AVG(Milliseconds / 60000);


SELECT
  Composer,
  AVG(Milliseconds / 60000) as avgOFFMinute
FROM
  tracks
GROUP BY
  Composer
HAVING
  AVG(Milliseconds / 60000) < 10 ;