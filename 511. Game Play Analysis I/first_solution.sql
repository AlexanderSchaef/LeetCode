/*
Find earliest event_date for each player
*/
SELECT a1.player_id, a1.event_date first_login 
FROM Activity a1
WHERE (SELECT MIN(event_date) 
        FROM ACTIVITY a2 
        WHERE a2.player_id=a1.player_id) = a1.event_date
