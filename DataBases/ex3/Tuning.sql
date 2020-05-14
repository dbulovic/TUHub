-- Q09:
-- old: SELECT I.Name FROM Institutions I WHERE I.CoKey IN(
--         SELECT CoKey FROM Countries C WHERE C.Name = 'Germany' OR C.Name = 'Austria');

SELECT I.Name FROM Institutions I, Countries C 
WHERE I.CoKey = C.CoKey AND (C.Name = 'Germany' OR C.Name = 'Austria');

-- Q10:
-- (SELECT P.Name FROM Persons P, Theses T
-- WHERE P.Akey = T.Akey AND T.Year < 2020)
-- INTERSECT
-- (SELECT P.Name FROM Persons P, Theses T
-- WHERE P.Akey = T.Akey AND T.Year >= 2018);

SELECT P.Name FROM Persons P, Theses T
WHERE P.Akey = T.Akey AND T.Year < 2020 AND T.Year >= 2018 ORDER BY 1;