-- Q01
EXPLAIN SELECT Conferences.City, Countries.Name
FROM Conferences, Countries
WHERE Conferences.SName = 'SIGMOD' AND Conferences.Year = 2019 AND Conferences.CoKey = Countries.CoKey;

--                                  QUERY PLAN                                 
-- ----------------------------------------------------------------------------
--  Hash Join  (cost=5.08..6.95 rows=1 width=16)
--    Hash Cond: (countries.cokey = conferences.cokey)
--    ->  Seq Scan on countries  (cost=0.00..1.68 rows=68 width=12)
--    ->  Hash  (cost=5.07..5.07 rows=1 width=12)
--          ->  Seq Scan on conferences  (cost=0.00..5.07 rows=1 width=12)
--                Filter: (((sname)::text = 'SIGMOD'::text) AND (year = 2019))


-- Q02
EXPLAIN SELECT Persons.Name, Persons.Website
FROM Persons, Institutions
WHERE Persons.IKey = Institutions.IKey AND Institutions.Name = 'Graz University of Technology'
ORDER BY Persons.Name;

--                                      QUERY PLAN                                     
-- ------------------------------------------------------------------------------------
--  Sort  (cost=748.40..748.46 rows=24 width=23)
--    Sort Key: persons.name
--    ->  Hash Join  (cost=31.96..747.85 rows=24 width=23)
--          Hash Cond: (persons.ikey = institutions.ikey)
--          ->  Seq Scan on persons  (cost=0.00..622.31 rows=35631 width=27)
--          ->  Hash  (cost=31.95..31.95 rows=1 width=4)
--                ->  Seq Scan on institutions  (cost=0.00..31.95 rows=1 width=4)
--                      Filter: ((name)::text = 'Graz University of Technology'::text)

