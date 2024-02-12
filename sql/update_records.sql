-- Update the year published of a book
UPDATE books
SET year_published = '2023'
WHERE title = "The Hobbit";

-- Correct the last name of an author
UPDATE authors
SET last_name = 'Upncomer'
WHERE first_name = 'Lee';