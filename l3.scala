object BookCountByAuthor extends App {
  val books = Seq(
    ("Dr. Seuss", "How the Grinch Stole Christmas!"),
    ("Jon Stone", "Monsters at the End of This Book"),
    ("Dr. Seuss", "The Lorax"),
    ("Jon Stone", "Big Bird in China"),
    ("Dr. Seuss", "One Fish, Two Fish, Red Fish, Blue Fish")
  )

  // Group the books by author and count them, also include the list of books
  // books.groupBy(_._1).foreach { case (author, booksByAuthor) =>
  books.groupBy(_._1).mapValues(_.size).foreach { case (author, count) =>
    println(s"$author has published $count book(s).")
  }
    // Uncomment below to print the titles of the books as well
  /*
  books.groupBy(_._1).foreach { case (author, booksByAuthor) =>
    println(s"$author has published ${booksByAuthor.size} book(s):")
    booksByAuthor.foreach { case (_, book) =>
      println(s"  - $book")
    }
    println()  // Blank line for better readability
  }
  */
}

