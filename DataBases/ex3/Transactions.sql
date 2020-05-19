-- (a)
BEGIN TRANSACTION;

CREATE TABLE R (a INT, b INT);
CREATE TABLE S (a INT, b INT);

INSERT INTO R VALUES (2, 4), (3, 5), (6, 8), (7, 9);
INSERT INTO S VALUES (4, 20), (5, 21), (6, 80);

COMMIT;

-- (b)
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
SELECT AVG(a) INTO aver1 FROM R;
-- other transaction executed here
SELECT AVG(a) INTO aver2 FROM R;
COMMIT;

BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;
INSERT INTO R VALUES (6, 9);
COMMIT;
-- If the second transaction was executed between the two SELECTs of the first transaction would usually result in a phantom read.
-- However, since isolation level is set to seralizable, it is prevented and we get the following message: 
-- "ERROR:  current transaction is aborted, commands ignored until end of transaction block"
-- This is because, with this isolation level transactions are executed serially one after the other, and cannot be concurrent.



BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SELECT AVG(a) INTO aver1 FROM R;
-- other transaction executed here
SELECT AVG(a) INTO aver2 FROM R;
COMMIT;

BEGIN TRANSACTION ISOLATION LEVEL REPEATABLE READ;
INSERT INTO R VALUES (6, 9);
COMMIT;
-- Here isolation level is set to the less strict Repetable Read. Therefore phantom read is possible.
-- If the second transaction was executed between the two SELECTs of the first transaction, the results in aver1 and aver2 tables would be different.
