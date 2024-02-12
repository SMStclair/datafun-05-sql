-- count all rows
SELECT COUNT(*) FROM authors;

-- get average year published
SELECT AVG(year_published) FROM books;

--get sum of years published
SELECT SUM(year_published) FROM books;