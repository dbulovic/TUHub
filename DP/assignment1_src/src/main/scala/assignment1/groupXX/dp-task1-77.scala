// Abgabe Deklarative Programmierung, Aufgabenblatt 1 im SS 2022

// Bitten fügen Sie folgend die Namen der Gruppenpartner ein:

// Gruppensprecher: Max Mustermann, 12345678
// Mitglied 2: 
// Mitglied 3: 

// Benennen Sie die Datei mit Ihrer vollständigen Gruppennummer (siehe TeachCenter) !

// z.b. Gruppe 1 = dp-task1-01.scala
//      Gruppe 10 = dp-task1-10.scala

// Benennen Sie das Paket (package) mit Ihrer vollständigen Gruppennummer (siehe TeachCenter) !

// z.b. Gruppe 1 = assignment1.group01
//      Gruppe 10 = assignment1.group10

package assignment1.group77

import scala.annotation.tailrec

// Implementieren Sie die folgende Klasse nach den Vorgaben aus dem
// Aufgabenblatt (siehe TeachCenter).


object DpTask1 {


  // 1.a
  def multPos(ls: List[Int]): Int = ls match
  {
    case Nil => 1
    case x::tail if x >= 0 => x * multPos(tail)
    case x::tail if x < 0 => multPos(tail)
  }



  // 1.b

  def multPos2(ls: List[Int]): Int = 
  {
    @tailrec
    def multPos_(ls: List[Int], mult: Int): Int = ls match
    {
      case Nil => mult
      case x::tail if x >= 0 => multPos_(tail, x * mult)
      case x::tail if x < 0 => multPos_(tail, mult)
    }

    multPos_(ls, 1)
  }



  // 2

  def indexOf(ls: List[Int], value: Int): Int = ls match
  {
    case Nil => 1
    case x::tail if x == value => 0
    case x::tail => 1 + indexOf(tail, value)
  }



  // 3.a

  def memberDouble(n: Int, l: List[Int]): Boolean = 
  l match
  {
    case Nil => false
    case x::tail if x == 2*n => true
    case x::tail => false || memberDouble(n, tail)
  }



  // 3.b

  def memberDouble2(n: Int, l: List[Int]): Boolean = 
  {
    @tailrec
    def memberDouble_(n: Int, l: List[Int], b: Boolean): Boolean = l match
    {
      case Nil => b
      case x::tail if x == 2*n => true
      case x::tail => memberDouble_(n, tail, b)
    }

    memberDouble_(n, l, false)
  }



  // 4

  def dropWhile[T](l: List[T], f: T => Boolean): List[T] = ???



  // 5

  def dropN[T](l: List[T], n: Int): List[T] = ???



  // 6

  def addCorrespondingElems(l1: List[Int], l2: List[Int]): List[Int] = 
  {
    if (l1.length < l2.length)
    {
      l1 match
      {
        case Nil => List[Int]()
        case _ => (l1.head + l2.head) +: addCorrespondingElems(l1.tail, l2.tail)
      }
    }
    else 
    {
      l2 match
      {
        case Nil => List[Int]()
        case _ => (l1.head + l2.head) +: addCorrespondingElems(l1.tail, l2.tail)
      }
    }
  }



  // 7.a

  def gcdList(n: Int, m: Int): List[Int] = ???



  // 7.b

  def gcdList2(n: Int, m: Int): List[Int] = ???



  // 8.a

  def oddsLessThanEqual2(n: Int): List[Int] = ???



  // 8.b

  def l1Norm2(elems: List[Int]): Int = ???



  // 9

  def checkEvenEven(l: List[Int]): Boolean = ???



  // 10

  // Do not modify this!
  def mergeSort(ls: List[Int]): List[Int] = {
    def split(ls: List[Int]): (List[Int], List[Int]) = {
      ls match {
        case Nil => (Nil, Nil)
        case l@List(v) => (Nil, l)
        case v1 :: v2 :: t =>
          val (l1, l2) = split(t)
          (v1 :: l1, v2 :: l2)
      }
    }

    ls match {
      case Nil => Nil
      case l@List(v) => l
      case l =>
        val (left, right) = split(l)
        merge(mergeSort(left), mergeSort(right))
    }
  }


  def merge(left: List[Int], right: List[Int]): List[Int] = ???



  // 11

  def isPrime(value: Int): Boolean = ???


  def removePrimes(xs: List[Int], isPrime: Int => Boolean): List[Int] = ???



  // 12

  def greaterThan(xs: List[Int], ys: List[Int]): Boolean = ???



  // 13

  def compareGeneral(xs: List[Int], ys: List[Int], op: (Int, Int) => Boolean): Boolean = ???



  // 14

  def sameElements(xs: List[Int], ys: List[Int]): Boolean = ???

  // Driver Code
  def main(args: Array[String]) 
  {
    println(addCorrespondingElems(List(7, 3, 9, 1, 11, 10 ), List(2, 2, 2 )))
  }

}




