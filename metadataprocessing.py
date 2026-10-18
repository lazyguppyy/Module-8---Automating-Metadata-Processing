#MODULE 8: Automating Metadata Processing
#author: Logan Grisby
#assignment: develop a python script that automates a LIS workflow, such as metadata cleaning, batch processing, or file organization

#1) creating a list of book records (title, author, year, genre, isbn)

##dystopian books
book1 = {'title': 'lord of the flies', 'author': 'william golding', 'year': '1954', 'genre': 'dystopian', 'isbn': '978-0399501487'}
book2 = {"title": "The Handmaid's Tale", 'author': 'Margaret Atwood', 'year': '1985', 'genre': 'dystopian', 'isbn': '978-054734566'}

##memoirs
book3 = {'title': 'crying in h mart', 'author': 'Michelle Zauner', 'year': '2021', 'genre': 'memoir', 'isbn': '978-1984898951'}

##mystery books
book4 = {'title': 'The Secret History', 'author': 'donna tartt', 'year': '1992', 'genre': 'mystery', 'isbn': '978-1400031702'}

##science fiction books
book5 = {'title': 'the martian', 'author': 'andy weir', 'year': '2014', 'genre': 'science fiction', 'isbn': '978-0553418026'}

##fantasy books
book6 = {'title': 'twilight', 'author': 'stephanie myer', 'year': '2005', 'genre': 'fantasy', 'isbn': '978-0316327336'}
book7 = {'title': 'coraline', 'author': 'neil gaiman', 'year': '2002', 'genre': 'fantasy', 'isbn': '978-0380807345'}

##fiction books
book8 = {'title': 'a little life', 'author': 'hanya yanagihara', 'year': '2016', 'genre': 'fiction', 'isbn': '978-0804172707'}

##romance books
book9 = {'title': 'sense and sensibility', 'author': 'jane austen', 'year': '1811', 'genre': 'romance', 'isbn': '978-8172344511'}

##poetry books
book10 = {'title': 'pillow thoughts', 'author': 'courtney peppernell', 'year': '2017', 'genre': 'poetry', 'isbn': '978-1449490010'}

#storing all books into a list catalogue
book_catalogue = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]

#2) cleaning book titles
def clean_title(title="Unknown Title"):
  return title.strip().title()

#3) organizing books...
## ...by year
def year_category(year):
  if int(year) < 1900:
    return "Historical Text"
  elif 1900 <= int(year) < 2000:
    return "20th Century Book"
  elif 2000 <= int(year) < 2010:
    return "Early 2000's book"
  else:
    return "Modern Book"

## ...by genre
def genre_category(genre):
  if genre in ["dystopian"]:
    return "Dystopian"
  elif genre in ["memoires"]:
    return "Memoir"
  elif genre in ["mystery"]:
    return "Mystery"
  elif genre in ["science fiction"]:
    return "Science Fiction"
  elif genre in ["fantasy"]:
    return "Fantasy"
  elif genre in ["fiction"]:
    return "Fiction"
  elif genre in ["romance"]:
    return "Romance"
  else:
    return "Poetry"

#4) write a loop that prints each book and categorizes it
processed_books = []

for book in book_catalogue:
  #clean title
  title = clean_title(book["title"])

  author = book["author"]

  category = year_category(book["year"])

  genre = genre_category(book["genre"])

  line = f"{title} by {author.title()} was published in {book['year']}, making it a {category}. The book belongs in the {book['genre'].title()} category.\n"

  processed_books.append(line)

#5) write the cleaned metadata to a file (output.txt)
try:
  with open("output.txt", "w") as file:
    for line in processed_books:
      file.write(line + "\n")

  print()
  print("[OK] Wrote output.txt\n")

#6) exception handling
except FileNotFoundError:
  print("Error: Could not find the file location.")