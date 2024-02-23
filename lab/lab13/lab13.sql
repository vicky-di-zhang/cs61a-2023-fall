.read data.sql


CREATE TABLE bluedog AS
  SELECT color,pet from students where color=='blue' AND pet=='dog';

CREATE TABLE bluedog_songs AS
  SELECT color,pet,song FROM students WHERE color=='blue' AND pet=='dog';



CREATE TABLE smallest_int_having AS
  SELECT time, smallest
  FROM (
    SELECT time, smallest,COUNT(smallest) AS count_smallest
    FROM students
    GROUP BY smallest
    HAVING count_smallest = 1
  );



CREATE TABLE matchmaker AS
  SELECT a.pet, a.song, a.color, b.color 
  from students as a join students as b 
  where a.pet == b.pet and a.song == b.song and a.time <> b.time;


CREATE TABLE sevens AS
  SELECT s.seven from students as s join numbers as n where n.time = s.time and n.'7' == 'True' and s.smallest <= 7;

