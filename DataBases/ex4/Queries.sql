-- Q12
SELECT a1.name, a2.name, COUNT(*)
FROM papers, authpapers ap1
JOIN persons a1 ON a1.akey = ap1.akey,
authpapers ap2
JOIN persons a2 ON a2.akey = ap2.akey
WHERE a1.akey > a2.akey AND papers.pkey = ap1.pkey AND papers.pkey = ap2.pkey 
GROUP BY a1.name, a2.name
ORDER BY COUNT(*) DESC
LIMIT 5;


-- Q13
SELECT subq.name, COUNT(*) FROM(
    SELECT persons.name, papers.title FROM authpapers
    JOIN persons ON persons.akey = authpapers.akey
    JOIN papers ON papers.pkey = authpapers.pkey
    JOIN journals ON papers.jkey = journals.jkey
    where journals.sname = 'PVLDB' AND journals.year > 2014 AND journals.year < 2020
    UNION
    SELECT persons.name, papers.title FROM authpapers
    JOIN persons ON persons.akey = authpapers.akey
    JOIN papers ON papers.pkey = authpapers.pkey
    JOIN conferences ON papers.ckey = conferences.ckey
    WHERE conferences.sname = 'SIGMOD' AND conferences.year > 2014 AND conferences.year < 2020) AS subq
GROUP BY subq.name
HAVING COUNT(*) > 20
ORDER BY COUNT(*) DESC;