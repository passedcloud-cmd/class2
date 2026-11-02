-- Active: 1793596242397@@127.0.0.1@3306
CREATE TABLE examples(
  ExamId INTEGER PRIMARY KEY AUTOINCREMENT,
  LastName VARCHAR(50) NOT NULL,
  FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('examples')

ALTER TABLE
  examples
ADD COLUMN
  Country VARCHAR(100) NOT NULL DEFAULT 'default value';

PRAGMA table_info('examples');



-- sqlite는 단일 문을 사용하여 한번에 여러 열을 추가하는 것을 지원하지 않음
ALTER TABLE examples
ADD COLUMN Age INTEGER NOT NULL DEFAULT 0;

ALTER TABLE examples
ADD COLUMN Address VARCHAR(100) NOT NULL DEFAULT 'default value';

PRAGMA table_info('examples');



ALTER TABLE
  examples
RENAME COLUMN Address TO PostCode;

PRAGMA table_info('examples');

ALTER TABLE
  examples
DROP COLUMN PostCode;

PRAGMA table_info('examples');

ALTER TABLE examples
RENAME to new_examples;

PRAGMA table_info('new_examples');

DROP TABLE new_examples;












CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content VARCHAR(200) NOT NULL,
  createdAt DATE NOT NULL
);

PRAGMA table_info('articles');

INSERT INTO articles (title, content, createdAt)
VALUES ('hello', 'world', '2000-01-01');

SELECT * FROM articles;

INSERT INTO
  articles (title, content, createdAt)
VALUES ('title1', 'content1', '1900-01-01'),
  ('title2', 'content2', '1800-01-01'),
  ('title3', 'content3', '1700-01-01');

SELECT * FROM articles;

INSERT INTO
  articles (title, content, createdAt)
VALUES
  ('title1', 'content1', 'DATA()');


SELECT * FROM articles;

UPDATE articles
SET createdAt = DATE('now')
WHERE id = 5;

SELECT * FROM articles;





-- 2. Update data in table
UPDATE 
  articles
SET
  title = 'update Title'
WHERE
  id = 1;

UPDATE 
  articles
SET
  title = 'update Title',
  content = 'update Content'
WHERE
  id = 2;

SELECT * FROM articles
WHERE
  id = 2;

SELECT * FROM articles;

-- 3. Delete data from table
DELETE FROM 
  articles
WHERE 
  id = 1;

SELECT * FROM articles;





-- 심화
SELECT id FROM articles
ORDER BY createdAt
LIMIT 2;

DELETE FROM 
  articles
WHERE id IN (
  SELECT id FROM articles
  ORDER BY createdAt
  LIMIT 2
);
  
SELECT * FROM articles;





-- 4. 
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;



-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) 
    REFERENCES users(id)
);

PRAGMA table_info('articles');
PRAGMA table_info('users');

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);

SELECT * FROM articles;
SELECT * FROM users;


-- INNER JOIN
SELECT * FROM articles
INNER JOIN users 
  ON users.id = articles.userId;

SELECT articles.title, users.name 
FROM articles
INNER JOIN users 
  ON users.id = articles.userId
WHERE users.id = 1;




-- LEFT JOIN
SELECT * FROM articles
LEFT JOIN users 
  ON users.id = articles.userId;


SELECT users.name, articles.id
FROM users
  LEFT JOIN articles
    ON users.id = articles.userId
WHERE articles.id IS NULL;


SELECT * FROM users
LEFT JOIN articles 
  ON articles.userId = users.id;
-- WHERE articles.userId IS NULL
