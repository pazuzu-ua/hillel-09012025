-- **************** SELECT
SELECT i_author,
       name,
       birth_year AS year      -- alias
  FROM Authors;

--
SELECT i_book,
       title,
       publication_year,
       pages
  FROM Books
 WHERE ( publication_year > 1900 ) AND ( publication_year < 1950 )

--
SELECT i_book,
       title,
       publication_year,
       pages
  FROM Books
 WHERE title LIKE 'the%'
 -- % будь-яку кількість будь-яких символів
 -- _ один будь-який символ
;

--
SELECT i_book,
       title,
       publication_year,
       pages
  FROM Books
 ORDER BY publication_year DESC
;

--
SELECT i_book,
       title,
       publication_year,
       pages
  FROM Books
 LIMIT 5 OFFSET 10
 -- OFFSET N, почни ПІСЛЯ N
;

--
SELECT B.title,
       A.name,
       G.genre_name
  FROM Books B
  JOIN Authors A ON B.i_author = A.i_author
  JOIN Genres G ON B.i_genre = G.i_genre
;

--
SELECT B.title,
       A.name,
       B.publication_year,
       G.genre_name
  FROM Books B
  JOIN Authors A ON B.i_author = A.i_author
  JOIN Genres G ON B.i_genre = G.i_genre
 WHERE G.i_genre == 1
 ORDER BY publication_year
;

--
SELECT COUNT(1)
  FROM Books
;

--
SELECT COUNT(i_book)
  FROM Books
  -- СПОЧАТКУ ВИКОНАЄТЬСЯ ФІЛЬТРАЦІЯ
 WHERE ( publication_year > 1900 ) AND ( publication_year < 1950 )
 ;

--
-- Спочатку виконуються умови в WHERE
-- в результаті: отримуємо список
-- далі, цей список групується за GROUP BY
-- в кінці, ми фільтруємо все через HAVING
SELECT A.name,
       COUNT(B.title) -- 4: агрегації
  FROM Books B
  JOIN Authors A ON B.i_author = A.i_author -- 1: поєднай таблиці
  WHERE A.name LIKE 'J%' -- 2: фільтруємо
  GROUP BY B.i_author -- 3: ГРУПУЄМО УСІ ДАНІ
  HAVING COUNT(B.title) > 1 -- 5: фільтруємо агреговані дані
;
