#! /usr/bin/env python3

#installing all used packages
    #source: https://stackoverflow.com/questions/17271444/how-to-install-a-missing-python-package-from-inside-the-script-that-needs-it

import sys, csv, psycopg2


db_host = sys.argv[-5]
db_port = sys.argv[-4]
db_name = sys.argv[-3]
db_user = sys.argv[-2]
db_password = sys.argv[-1]

#names of the csv files which contain the data
confs_csv_name = sys.argv[1]#'confs.csv'
journals_csv_name = sys.argv[2]#'journals.csv'
persons_csv_name = sys.argv[3]#'persons.csv'
pubs_csv_name = sys.argv[4]#'pubs.csv'
theses_csv_name = sys.argv[5]#'theses.csv'

#------------------------------------------------------------------------------------------------------------------------------------------

#HELP:
'''
---Insertion to database:
   cur.execute('INSERT INTO Table1 (col1, col2) VALUES('%s', '%s')', (value1, value2))

---Fetching from database:-----------------------------------------------------------------------------------------------------------------
   cur.execute(query)
   resultSet = cur.fetchall() - to fetch the whole result set
   reultSet = cur.fetchone() - to fetch a single row(does not mean only the first row, it means one row at a time)
-------------------------------------------------------------------------------------------------------------------------------------------
'''


def csv_to_list(csv_name):
#gets data from the csv file and puts it into a list of lists
#for accessing the data: data_list[row_number][column_number]
    data_list = []
    with open(csv_name, 'r', encoding='utf-8') as csvfile:
      data_squads = csv.reader(csvfile)
      
      for row in data_squads:
        #to remove all the ', to have no collisions in the code later on
        new_row = []
        for element in row:
          if isinstance(element, str):
            element = element.replace("'", "`")
          new_row.append(element)
        #print(new_row)
            
        data_list.append(new_row)
      #deletes the fist row, which contains the table heads
      #optional:uncomment if this makes working with the data easier for you
      del data_list[0]
    return data_list

def semicolon_string_to_list(string):
#interprets all ; of the given string as separator of elements
#returns a list of strings
    return string.split(';')

#------------------------------------------------------------------------------------------------------------------------------------------

#Lists from csvs
confs_list = csv_to_list(confs_csv_name)
journals_list = csv_to_list(journals_csv_name)
persons_list = csv_to_list(persons_csv_name)
pubs_list = csv_to_list(pubs_csv_name)
theses_list = csv_to_list(theses_csv_name)



#SQL connection
sql_con = psycopg2.connect(host = db_host, port = db_port, database = db_name, user = db_user, password = db_password)
#cursor, for DB operations
cur = sql_con.cursor()

# adding Countries
for conf in confs_list:
  if conf[4] != "":
    cur.execute("SELECT CoKey FROM Countries WHERE Countries.Name = '%s'" %(conf[4]))
    if cur.fetchone() is None:
      cur.execute("INSERT INTO Countries (Name) VALUES ('%s')"%(conf[4]))

for person in persons_list:
  if person[4] != "":
    cur.execute("SELECT Countries.Name FROM Countries WHERE Countries.Name = '%s'"%(person[4]))
    if cur.fetchone() is None:
      cur.execute("INSERT INTO Countries (Name) VALUES ('%s')"%(person[4]))

for thesis in theses_list:
  if thesis[6] != "":
    cur.execute("SELECT Countries.Name FROM Countries WHERE Countries.Name = '%s'"%(thesis[6]))
    if cur.fetchone() is None:
      cur.execute("INSERT INTO Countries (Name) VALUES ('%s')"%(thesis[6]))


# adding Institutions
for person in persons_list:
  if person[3] != "":
    cur.execute("SELECT Institutions.Name FROM Institutions WHERE Institutions.Name = '%s'"%(person[3]))
    if cur.fetchone() is None:
      if person[4] != "":
        cur.execute("SELECT CoKey FROM Countries WHERE Countries.Name = '%s'" %(person[4]))
        tmp_CoKey = cur.fetchone()
        cur.execute("INSERT INTO Institutions (Name, CoKey) VALUES ('%s', %s)"%(person[3], tmp_CoKey[0]))
      else:
        cur.execute("INSERT INTO Institutions (Name) VALUES ('%s')"%(person[3]))
    else:
      cur.execute("SELECT CoKey FROM Institutions WHERE Institutions.Name = '%s'"%(person[3]))
      tmp_CoKey_list = cur.fetchall()
      cur.execute("SELECT CoKey FROM Countries WHERE Countries.Name = '%s'"%(person[4]))
      tmp_CoKey = cur.fetchone()
      if tmp_CoKey is None:
        cur.execute("SELECT * FROM Institutions WHERE Institutions.Name = '%s' AND Institutions.CoKey IS NULL"%(person[3]))
        if cur.fetchone() is None:
          cur.execute("INSERT INTO Institutions (Name) VALUES ('%s')"%(person[3]))
        continue
      tmp_test = True
      for result in tmp_CoKey_list:
        if tmp_CoKey[0] in result:
          tmp_test = False
      if tmp_test == True:
        cur.execute("INSERT INTO Institutions (Name, CoKey) VALUES ('%s', %s)"%(person[3], tmp_CoKey[0]))

for thesis in theses_list:
  if thesis[5] != "":
    cur.execute("SELECT Institutions.Name FROM Institutions WHERE Institutions.Name = '%s'"% (thesis[5]))
    if cur.fetchone() is None:
      if thesis[6] != "":
        cur.execute("SELECT CoKey FROM Countries WHERE Countries.Name = '%s'" %(thesis[6]))
        tmp_CoKey = cur.fetchone()
        cur.execute("INSERT INTO Institutions (Name, CoKey) VALUES ('%s', %s)"%(thesis[5], tmp_CoKey[0]))
      else:
        cur.execute("INSERT INTO Institutions (Name) VALUES ('%s')"%(thesis[5]))
    else:
      cur.execute("SELECT CoKey FROM Institutions WHERE Institutions.Name = '%s'"% (thesis[5]))
      tmp_CoKey_list = cur.fetchall()
      cur.execute("SELECT CoKey FROM Countries WHERE Countries.Name = '%s'" %(thesis[6]))
      tmp_CoKey = cur.fetchone()
      if tmp_CoKey is None:
        cur.execute("SELECT * FROM Institutions WHERE Institutions.Name = '%s' AND Institutions.CoKey IS NULL"%(thesis[5]))
        if cur.fetchone() is None:
          cur.execute("INSERT INTO Institutions (Name) VALUES ('%s')"%(thesis[5]))
        continue
      tmp_test = True
      for result in tmp_CoKey_list:
        if tmp_CoKey[0] in result:
          tmp_test = False
      if tmp_test == True:
        cur.execute("INSERT INTO Institutions (Name, CoKey) VALUES ('%s', %s)"%(thesis[5], tmp_CoKey[0]))



# adding Conferences
for conf in confs_list:
  cur.execute("SELECT CoKey FROM Countries WHERE Countries.Name = '%s'"% (conf[4]))
  tmp_CoKey = cur.fetchone()
  cur.execute("INSERT INTO Conferences VALUES(%s, '%s', '%s', '%s', %s, %s, '%s')" %(conf[0][1:], conf[1], conf[2], conf[3], tmp_CoKey[0], conf[6], conf[7]))
  
# adding Journals
for journal in journals_list:
  if journal[4] != "":
    cur.execute("INSERT INTO Journals VALUES(%s, '%s', '%s', %s, %s, %s)"%(journal[0][1:], journal[1], journal[2], journal[3], journal[4], journal[5]))
  else:
    cur.execute("INSERT INTO Journals (JKey, SName, Title, Volume, Year) VALUES(%s, '%s', '%s', %s, %s)"%(journal[0][1:], journal[1], journal[2], journal[3], journal[5]))


# adding Persons
for person in persons_list:
  if person[3] != "":
    cur.execute("SELECT IKey FROM Institutions WHERE Institutions.Name = '%s'"% (person[3]))
    tmp_IKey = cur.fetchone()
    cur.execute("INSERT INTO Persons VALUES(%s, '%s', '%s', %s)" %(person[0][1:], person[1], person[5], tmp_IKey[0]))
  else:
    cur.execute("INSERT INTO Persons (AKey, Name, Website) VALUES(%s, '%s', '%s')" %(person[0][1:], person[1], person[5]))

# adding Papers
for paper in pubs_list:
  if (paper[4][0] == "C"):
    cur.execute("INSERT INTO Papers (PKey, Title, Pages, CKey) VALUES(%s, '%s', '%s', %s)"% (paper[0][1:], paper[2], paper[3], paper[4][1:]))
  elif (paper[4][0] == "J"):
    cur.execute("INSERT INTO Papers (PKey, Title, Pages, JKey) VALUES(%s, '%s', '%s', %s)" %(paper[0][1:], paper[2], paper[3], paper[4][1:]))

# adding Theses
for thesis in theses_list:
  cur.execute("SELECT IKey FROM Institutions WHERE Institutions.Name = '%s'" %(thesis[5]))
  tmp_IKey = cur.fetchone()
  if thesis[7] != "" and thesis[5] != "":
    cur.execute("INSERT INTO Theses VALUES(%s, '%s', %s, %s, '%s', '%s', %s, %s)"% (thesis[0][1:], thesis[2], thesis[3], thesis[7], thesis[4], thesis[8], thesis[1][1:], tmp_IKey[0]))
  elif thesis[7] != "":
    cur.execute("INSERT INTO Theses (TKey, Title, Year, NPages, Type, ISBN, AKey) VALUES(%s, '%s', %s, %s, '%s', '%s', %s)"% (thesis[0][1:], thesis[2], thesis[3], thesis[7], thesis[4], thesis[8], thesis[1][1:]))
  elif thesis[5] != "":
    cur.execute("INSERT INTO Theses (TKey, Title, Year, Type, ISBN, AKey, IKey) VALUES(%s, '%s', %s,'%s', '%s', %s, %s)"% (thesis[0][1:], thesis[2], thesis[3], thesis[4], thesis[8], thesis[1][1:], tmp_IKey[0]))
  else:
    cur.execute("INSERT INTO Theses (TKey, Title, Year, Type, ISBN, AKey) VALUES(%s, '%s', %s, '%s', '%s', %s)"% (thesis[0][1:], thesis[2], thesis[3], thesis[4], thesis[8], thesis[1][1:]))
 

#commit the changes, this makes the database persistent
sql_con.commit()

#close connections
cur.close()
sql_con.close()