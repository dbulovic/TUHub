from pyspark import SparkContext


def executeQ12RDD():
    sc1 = SparkContext("local", "q12")
    
    authpapers = sc1.textFile("data/AuthPapers.csv")
    papers = sc1.textFile("data/Papers.csv")
    persons = sc1.textFile("data/Persons.csv")


def executeQ13RDD():
    sc2 = SparkContext("local", "q13")

    authpapers = sc2.textFile("data/AuthPapers.csv")
    papers = sc2.textFile("data/Papers.csv")
    persons = sc2.textFile("data/Persons.csv")
    journals = sc2.textFile("data/Journals.csv")
    conferences = sc2.textFile("data/Conferences.csv")
