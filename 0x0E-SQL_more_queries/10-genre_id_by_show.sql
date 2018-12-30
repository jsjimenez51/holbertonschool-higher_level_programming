-- imports a database dump to a MySQL server
SELECT 	tv_shows.title, tv_show_genres.genre_id
From tv_show_genres
INNER JOIN tv_shows ON tv_show_genres.show_id=tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
