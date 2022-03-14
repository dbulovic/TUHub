package assignment1.groupXX

import org.scalatest.funsuite.AnyFunSuite

class DpTask1Test extends AnyFunSuite {
  test("multPos: two positive values and one negative value") {
    assert(DpTask1.multPos(List(2,-3,4)) == 8)
    assert(DpTask1.multPos2(List(2,-3,4)) == 8)
  }
}
