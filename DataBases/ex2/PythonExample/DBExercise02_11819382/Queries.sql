-- Q01
SELECT Conferences.City, Countries.Name
FROM Conferences, Countries
WHERE Conferences.SName = 'SIGMOD' AND Conferences.Year = 2019 AND Conferences.CoKey = Countries.CoKey;
-- result:
--    city    |      name       
-- -----------+-----------------
--  Amsterdam | The Netherlands

-- Q02
SELECT Persons.Name, Persons.Website
FROM Persons, Institutions
WHERE Persons.IKey = Institutions.IKey AND Institutions.Name = 'Graz University of Technology'
ORDER BY Persons.Name;
-- result:
--         name         |                website                
-- ---------------------+---------------------------------------
--  Alexander Felfernig | http://www.ist.tugraz.at/felfernig/
--  Bernhard C. Geiger  | https://orcid.org/0000-0003-3257-743X
--  Denis Helic         | https://orcid.org/0000-0003-0725-7450
--  Hermann A. Maurer   | http://www.iicm.edu/Hmaurer
--  Martin Trapp 0001   | https://martint.blog/
--  Matthias Boehm 0001 | http://matthiasboehm.org/

-- Q03
SELECT Year, COUNT(*) AS Total 
FROM Theses 
GROUP BY Year ORDER BY Year;
-- result:
--  year | total 
-- ------+-------
--  2011 |   187
--  2012 |   218
--  2013 |   243
--  2014 |   259
--  2015 |   250
--  2016 |   225
--  2017 |   224
--  2018 |   207
--  2019 |   107
--  2020 |     8

-- Q04
SELECT Journals.Title, Journals.Volume, Journals.Issue, Journals.Year
FROM Journals, Papers
WHERE Journals.JKey = Papers.JKey
GROUP BY Journals.Title, Journals.Volume, Journals.Issue, Journals.Year
HAVING COUNT(*) > 70
ORDER BY Journals.Year DESC, Journals.Issue DESC
-- result:
--  title | volume | issue | year 
-- -------+--------+-------+------
--  PVLDB |     12 |    12 | 2019
--  PVLDB |     11 |    12 | 2018
--  PVLDB |      8 |    12 | 2015
--  PVLDB |      7 |    13 | 2014

-- Q05
SELECT Conferences.City, Countries.Name, COUNT(*) AS Count
FROM Conferences, Countries
WHERE Conferences.CoKey = Countries.CoKey
GROUP BY Conferences.City, Countries.Name
HAVING COUNT(*) > 1
ORDER BY Count DESC;
-- result:
--      city      |      name       | count 
-- ---------------+-----------------+-------
--  San Francisco | USA             |     6
--  Chicago       | USA             |     6
--  New York      | USA             |     4
--  Melbourne     | Australia       |     4
--  Athens        | Greece          |     4
--  Asilomar      | USA             |     4
--  Brussels      | Belgium         |     4
--  Beijing       | China           |     4
--  Hong Kong     | China           |     3
--  Houston       | USA             |     3
--  Amsterdam     | The Netherlands |     3
--  Vienna        | Austria         |     3
--  Lisbon        | Portugal        |     2
--  Scottsdale    | USA             |     2
--  Snowbird      | USA             |     2
--  Lyon          | France          |     2
--  Dublin        | Ireland         |     2
--  Genoa         | Italy           |     2
--  Vancouver     | Canada          |     2
--  San Diego     | USA             |     2
--  Shanghai      | China           |     2
--  Bordeaux      | France          |     2
--  Portland      | USA             |     2
--  Florence      | Italy           |     2
--  Venice        | Italy           |     2
--  Berlin        | Germany         |     2
--  Paris         | France          |     2
--  Uppsala       | Sweden          |     2
--  Seoul         | South Korea     |     2
--  Singapore     | Singapore       |     2