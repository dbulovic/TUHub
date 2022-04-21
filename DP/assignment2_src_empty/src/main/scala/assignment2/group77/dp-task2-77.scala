// Abgabe Deklarative Programmierung, Aufgabenblatt 2 im SS 2022

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

package assignment2.group77

// Implementieren Sie die folgende Klasse nach den Vorgaben aus dem
// Aufgabenblatt (siehe TeachCenter).

object DpTask2 {

  // EvenElements
  def evenElements(as: List[Int]) : List[Int] = {
    def addIfEven(x: Int, ls: List[Int]) : List[Int] =
    {
      if (x % 2 == 0) x::ls
      else ls
    }
    as.foldRight(List[Int]())(addIfEven)
  }

  // all
  def all(as : List[Int], predicate : Int => Boolean): Boolean = {
    as.foldRight(true)((predicate(_) && _))
  }

  // interleave
  def interleave(as : List[Int], separator : Int) : List[Int] = {
    as.foldRight(List[Int](separator))((x : Int, l : List[Int]) => (separator +: (x +: l)))
  }

  // toInteger
  // Do NOT modify this!
  def integerPow(base: Int, exponent: Int): Int = {
    Math.pow(base, exponent).toInt
  }

  def toInteger(as: List[Int]) : Int = { 
    def fn(xp: (Int, Int), s: Int): Int = xp match
    {
      case (x, p) => integerPow(2,p)*x + s
    }
    as.foldLeft(List[Int]())((l: List[Int], x: Int) => x::l).zipWithIndex.foldRight(0)(fn)
  }

  // scalarMultiplication
  def scalarMultiplication(as: List[Int], s: Int) : List[Int] = {
    as.foldRight(List[Int]())((x: Int, l: List[Int]) => (x*s)::l)
  }

  // firstIndex 
  def firstIndex(as: List[Int], s: Int) : Int = {
    def f(x: Int, y: Int): Int = 
    {
      if (x == s) 0
      else y + 1
    }
    
    val res = as.foldRight(0)(f)
    if (res == as.length) -1
    else res
  }


  // Baum Beispiel
  sealed trait BTree[T]
  case class Leaf[T]() extends BTree[T]
  case class Node[T](left: BTree[T], e: T, right: BTree[T]) extends BTree[T]

  // invertTree
  def invertTree(tree: BTree[Int]): BTree[Int] = {
    tree match
    {
      case Leaf() => Leaf[Int]()
      case Node(left, e, right) => Node[Int](invertTree(right), e, invertTree(left))
    }
  }

  // treeToSortedList
  def searchTreeToSortedList(tree: BTree[Int]) : List[Int] = {
    tree match
    {
      case Leaf() => List[Int]()
      case Node(left, e, right) => searchTreeToSortedList(left) ::: e::searchTreeToSortedList(right)      
    }
  }

  // test code
  def main(args: Array[String]) 
  {
    val leaf = Leaf[Int]()
    val ll = Node[Int](leaf, 2, leaf)
    val r = Node[Int](leaf, 7, leaf)
    val l = Node[Int](ll, 4, leaf)
    val root = Node[Int](l, 5, r)
    println(searchTreeToSortedList(root))
  }

}
