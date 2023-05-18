-- list all genres not linked to the show Dexter
SELECT DISTINCT tg.name
FROM tv_genres tg
WHERE tg.id NOT IN (SELECT tg.genre_id FROM tv_shows ts LEFT JOIN tv_show_genres tg ON tg.show_id = ts.id WHERE ts.title = "Dexter")
ORDER BY tg.name;
