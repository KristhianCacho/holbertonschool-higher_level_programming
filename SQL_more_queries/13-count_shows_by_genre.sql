-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 12-no_genre.sql)
-- Write a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Dont display a genre that doesnt have any shows linked
-- Results must be sorted in descending order by the number of shows linked
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_genres.name AS "genre", COUNT(tv_genres.id) AS "number_of_shows" FROM tv_genres JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY name ORDER BY number_of_shows DESC;