

pets = {"oscar":"dog",
        "Niko":"cat",
        "Coe":"fish"}

class Pet(object):
    def __init__(self):
        self.name = 'trixy'

    species = 'dog'
    breed = 'mutt'
    name = 'scruffy'
    def print_pet(self):
        print(self.name)
        print(self.species)
        print(self.breed)


dog = Pet()
dog.print_pet()


class Book(object):
    def __init__(self):
        self.author = "Tony"
        self.title = "Darkest"

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        template ="{title} by {author}"
        return template.format(title=self.title, author=self.author)

    def __eq__(self, other):
        if self.title == other.title and self.author == other.author:
            return True
        else:
            return False
    title = ''
    author = ''


myBook = Book(title = "Snow Crash", author="stephenson")
jimBook = Book(title="Storm Front", author="Butcher")
tonyBook = Book(title="Storm Front", author="Butcher")
yosBook = Book(title="Storm Front", author="Wheaton")

print(myBook.title)

books = [myBook, jimBook]

def print_books(books):
    for book in books:
        print(book)

print_books(books)

print(myBook == jimBook)
print(jimBook == tonyBook)
print(tonyBook == yosBook)






