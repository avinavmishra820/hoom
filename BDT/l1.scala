import scala.io.StdIn

object BubbleSort extends App {
  def bubbleSort(arr: Array[Int]): Array[Int] = {
    var swapped = true
    while (swapped) {
      swapped = false
      for (i <- 0 until arr.length - 1) {
        if (arr(i) > arr(i + 1)) {
          val temp = arr(i)
          arr(i) = arr(i + 1)
          arr(i + 1) = temp
          swapped = true
        }
      }
    }
    arr
  }

  println("Enter the size of the array:")
  try {
    val size = StdIn.readInt()
    if (size <= 0) println("Array size must be positive.")
    else {
      val arr = Array.fill(size)(StdIn.readInt())
      println(s"Array: ${arr.mkString(", ")}")
      println(s"Sorted: ${bubbleSort(arr).mkString(", ")}")
    }
  } catch {
    case _: Exception => println("Invalid input.")
  }
}

