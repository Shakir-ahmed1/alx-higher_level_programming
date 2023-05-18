-- lists all Comedy shows in the database hbtn_0d_tvshows.
select ts.title AS title
FROM tv_shows ts LEFT JOIN tv_show_genres tsg ON ts.id = tsg.show_id
LEFT JOIN tv_genres tg ON tg.id = tsg.genre_id
WHERE tg.name = 'Comedy'
ORDER BY title;
