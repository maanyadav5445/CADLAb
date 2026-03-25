library = {}
issued = {}

def add_book():
    book = input()
    count = int(input())
    library[book] = count

def issue_book():
    user = input()
    book = input()
    if book in library and library[book] > 0:
        library[book] -= 1
        issued.setdefault(user, []).append(book)

def return_book():
    user = input()
    book = input()
    if user in issued and book in issued[user]:
        issued[user].remove(book)
        library[book] += 1

def show_books():
    print(library)

def show_issued():
    print(issued)

while True:
    choice = input()
    if choice == "1":
        add_book()
    elif choice == "2":
        issue_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        show_books()
    elif choice == "5":
        show_issued()
    elif choice == "6":
        break
    