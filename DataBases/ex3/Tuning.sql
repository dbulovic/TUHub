-- (a)
-- Q09:
-- old:
-- SELECT I.Name FROM Institutions I WHERE I.CoKey IN(
-- SELECT CoKey FROM Countries C WHERE C.Name = 'Germany' OR C.Name = 'Austria');
-- new:
SELECT I.Name FROM Institutions I, Countries C 
WHERE I.CoKey = C.CoKey AND (C.Name = 'Germany' OR C.Name = 'Austria');


--  Hash Join  (cost=2.04..34.42 rows=45 width=25)
--    Hash Cond: (i.cokey = c.cokey)
--    ->  Seq Scan on institutions i  (cost=0.00..28.16 rows=1516 width=29)
--    ->  Hash  (cost=2.02..2.02 rows=2 width=4)
--          ->  Seq Scan on countries c  (cost=0.00..2.02 rows=2 width=4)
--                Filter: (((name)::text = 'Germany'::text) OR ((name)::text = 'Austria'::text))

--  Hash Join  (cost=2.04..34.42 rows=45 width=25)
--    Hash Cond: (i.cokey = c.cokey)
--    ->  Seq Scan on institutions i  (cost=0.00..28.16 rows=1516 width=29)
--    ->  Hash  (cost=2.02..2.02 rows=2 width=4)
--          ->  Seq Scan on countries c  (cost=0.00..2.02 rows=2 width=4)
--                Filter: (((name)::text = 'Germany'::text) OR ((name)::text = 'Austria'::text))

-- As we can see, even though the query is unnested, the plans are the same.



-- (b)
-- Q10:
-- old
-- (SELECT P.Name FROM Persons P, Theses T
-- WHERE P.Akey = T.Akey AND T.Year < 2020)
-- INTERSECT
-- (SELECT P.Name FROM Persons P, Theses T
-- WHERE P.Akey = T.Akey AND T.Year >= 2018);
-- new:
SELECT P.Name FROM Persons P, Theses T
WHERE P.Akey = T.Akey AND T.Year < 2020 AND T.Year >= 2018;


--  HashSetOp Intersect  (cost=61.12..1804.81 rows=322 width=278)
--    ->  Append  (cost=61.12..1799.20 rows=2242 width=278)
--          ->  Subquery Scan on "*SELECT* 2"  (cost=61.12..868.03 rows=322 width=18)
--                ->  Hash Join  (cost=61.12..864.81 rows=322 width=14)
--                      Hash Cond: (p.akey = t.akey)
--                      ->  Seq Scan on persons p  (cost=0.00..622.31 rows=35631 width=18)
--                      ->  Hash  (cost=57.10..57.10 rows=322 width=4)
--                            ->  Seq Scan on theses t  (cost=0.00..57.10 rows=322 width=4)
--                                  Filter: (year >= 2018)
--          ->  Subquery Scan on "*SELECT* 1"  (cost=81.10..919.97 rows=1920 width=18)
--                ->  Hash Join  (cost=81.10..900.76 rows=1920 width=14)
--                      Hash Cond: (p_1.akey = t_1.akey)
--                      ->  Seq Scan on persons p_1  (cost=0.00..622.31 rows=35631 width=18)
--                      ->  Hash  (cost=57.10..57.10 rows=1920 width=4)
--                            ->  Seq Scan on theses t_1  (cost=0.00..57.10 rows=1920 width=4)
--                                  Filter: (year < 2020)

--  Hash Join  (cost=65.84..869.45 rows=314 width=14)
--    Hash Cond: (p.akey = t.akey)
--    ->  Seq Scan on persons p  (cost=0.00..622.31 rows=35631 width=18)
--    ->  Hash  (cost=61.92..61.92 rows=314 width=4)
--          ->  Seq Scan on theses t  (cost=0.00..61.92 rows=314 width=4)
--                Filter: ((year < 2020) AND (year >= 2018))


-- The plan for the rewritten query is much shorter. This is because it only performs SELECT once, as opposed to the original query.
-- There is much less work to do (e.g. fewer searches), which makes it much faster.


-- (c)
-- create index
CREATE INDEX idx_thesis_year
ON Theses (Year);

--  Hash Join  (cost=65.84..869.45 rows=314 width=14)
--    Hash Cond: (p.akey = t.akey)
--    ->  Seq Scan on persons p  (cost=0.00..622.31 rows=35631 width=18)
--    ->  Hash  (cost=61.92..61.92 rows=314 width=4)
--          ->  Seq Scan on theses t  (cost=0.00..61.92 rows=314 width=4)
--                Filter: ((year < 2020) AND (year >= 2018))


--  Hash Join  (cost=53.13..856.74 rows=314 width=14)
--    Hash Cond: (p.akey = t.akey)
--    ->  Seq Scan on persons p  (cost=0.00..622.31 rows=35631 width=18)
--    ->  Hash  (cost=49.21..49.21 rows=314 width=4)
--          ->  Bitmap Heap Scan on theses t  (cost=11.50..49.21 rows=314 width=4)
--                Recheck Cond: ((year < 2020) AND (year >= 2018))
--                ->  Bitmap Index Scan on idx_thesis_year  (cost=0.00..11.42 rows=314 width=0)
--                      Index Cond: ((year < 2020) AND (year >= 2018))


-- As opposed to a seq scan on thesis we have a bitmap heap scan.