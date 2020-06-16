from pyspark.sql import SparkSession


def executeQ12Dataset():
   sc1 = SparkSession \
      .builder \
      .appName("query 12 datasets") \
      .getOrCreate()
      

   authpapers = sc1.read.csv("data/AuthPapers.csv", header=True)
   papers = sc1.read.csv("data/Papers.csv", header=True)
   persons = sc1.read.csv("data/Persons.csv", header=True)

   authpapers.createOrReplaceTempView("authpapers")
   papers.createOrReplaceTempView("papers")
   persons.createOrReplaceTempView("persons")

   query12 = sc1.sql("SELECT a1.name, a2.name, COUNT(*) FROM papers, authpapers ap1 "+
   "JOIN persons a1 ON a1.akey = ap1.akey, authpapers ap2 "+
   "JOIN persons a2 ON a2.akey = ap2.akey "+
   "WHERE a1.akey > a2.akey AND papers.pkey = ap1.pkey AND papers.pkey = ap2.pkey "+
   "GROUP BY a1.name, a2.name "+
   "ORDER BY COUNT(*) DESC "+
   "LIMIT 5")

   newHeaders = ['name1','name2', 'count']
   query12 = query12.toDF(*newHeaders)
   
   #query12.show()
   query12.write.parquet("out12.parquet")

def executeQ13Dataset():
   sc2 = SparkSession \
      .builder \
      .appName("query 13 datasets") \
      .getOrCreate()
      

   authpapers = sc2.read.csv("data/AuthPapers.csv", header=True)
   papers = sc2.read.csv("data/Papers.csv", header=True)
   persons = sc2.read.csv("data/Persons.csv", header=True)
   journals = sc2.read.csv("data/Journals.csv", header=True)
   conferences = sc2.read.csv("data/Conferences.csv", header=True)

   authpapers.createOrReplaceTempView("authpapers")
   papers.createOrReplaceTempView("papers")
   persons.createOrReplaceTempView("persons")
   journals.createOrReplaceTempView("journals")
   conferences.createOrReplaceTempView("conferences")

   query13 = sc2.sql("SELECT subq.name, COUNT(*) AS cnt FROM( " +
    "SELECT persons.name, papers.title FROM authpapers " +
    "JOIN persons ON persons.akey = authpapers.akey " +
    "JOIN papers ON papers.pkey = authpapers.pkey " +
    "JOIN journals ON papers.jkey = journals.jkey " +
    "where journals.sname = 'PVLDB' AND journals.year > 2014 AND journals.year < 2020 " +
    "UNION " +
    "SELECT persons.name, papers.title FROM authpapers " +
    "JOIN persons ON persons.akey = authpapers.akey " +
    "JOIN papers ON papers.pkey = authpapers.pkey " +
    "JOIN conferences ON papers.ckey = conferences.ckey " +
    "WHERE conferences.sname = 'SIGMOD' AND conferences.year > 2014 AND conferences.year < 2020) AS subq " +
    "GROUP BY subq.name " +
    "HAVING cnt > 20 " +
    "ORDER BY cnt DESC")
   
   #query13.show()
   query13.write.parquet("out13.parquet")

executeQ12Dataset()
executeQ13Dataset()