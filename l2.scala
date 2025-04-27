import scala.io.StdIn._

object LongestWordFinder extends App {
  def findLongestWord(words: Array[String]) = words.map(w => (w, w.length)).maxBy(_._2)

  println("Enter words separated by spaces:")
  val input = readLine().split("\\s+")
  if (input.nonEmpty) {
    val (word, length) = findLongestWord(input)
    println(s"The longest word is: '$word' with length $length")
  } else println("No words were entered.")
}

