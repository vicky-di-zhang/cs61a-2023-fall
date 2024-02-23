CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;


-- All dogs with parents ordered by decreasing height of their parent
CREATE TABLE by_parent_height AS
  SELECT a.child from parents as a, dogs as b 
  where b.name = a.parent 
  order by b.height DESC;


-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT d.name,s.size from sizes as s, dogs as d 
  where d.height > s.min AND d.height <= s.max;


-- Filling out this helper table is optional
CREATE TABLE siblings AS
  SELECT s1.name as name1, s2.name as name2, s2.size as size from size_of_dogs as s1, size_of_dogs as s2
  where s1.name != s2.name AND s1.size = s2.size;

-- Sentences about siblings that are the same size
CREATE TABLE sentences AS
  SELECT "The two siblings,"|| name1 ||"and"|| name2 ||", have the same size: "|| size
  from siblings;


-- Height range for each fur type where all of the heights differ by no more than 30% from the average height

CREATE TABLE low_variance AS
  SELECT fur, MAX(height) - MIN(height) AS height_range
  FROM dogs
  GROUP BY fur
  HAVING 
    MIN(height) >= AVG(height) * 0.7 AND
    MAX(height) <= AVG(height) * 1.3;

