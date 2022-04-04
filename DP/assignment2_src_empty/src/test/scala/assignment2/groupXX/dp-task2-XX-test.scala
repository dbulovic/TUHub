package assignment2.groupXX

import assignment2.groupXX.DpTask2.{Leaf, Node}
import org.scalatest.funsuite.AnyFunSuite

class DpTask2Test extends AnyFunSuite {

  test("interleave"){
    assert(DpTask2.interleave(List(1,2,3),0) ==  List(0,1,0,2,0,3,0))
  }


  test("invertTree"){
    val leaf = Leaf[Int]()
    val node1 = Node[Int](leaf, 5, leaf)
    val node2 = Node[Int](leaf, 7, leaf)
    val node3 = Node[Int](node1, 6, node2)
    val node4 = Node[Int](leaf, 13, leaf)
    val root = Node[Int](node3, 10, node4)

    assert(DpTask2.searchTreeToSortedList(root) == List(5,6,7,10,13))
    assert(DpTask2.invertTree(leaf) == leaf)
    assert(DpTask2.invertTree(node1) == node1)
    assert(DpTask2.invertTree(node2) == node2)
    assert(DpTask2.invertTree(node4) == node4)
    assert(DpTask2.invertTree(node3) == Node(node2, 6, node1))
    assert(DpTask2.invertTree(root) == Node(node4, 10, Node(node2,6,node1)))
  }
}
