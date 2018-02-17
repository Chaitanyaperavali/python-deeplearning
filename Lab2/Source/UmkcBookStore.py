def booksInRange(books,low,high):
    resultBooks = set()
    for book in books:
        if low <= books[book] <= high :
            resultBooks.add(book)
    return resultBooks

# function to add books to the bookstore
def setBooks():
    com = str(input("'q' for quit\nEnter book name and value seperated by space\n"))
    books={}
    # adds books to the list untill quit
    while(com != "q"):
        com_temp = com.split(" ")
        if com_temp.__len__()>0:
            books[com_temp[0]] = int(com_temp[1])
        com = str(input())

    range = str(input("Enter range low <space> high: \n"))
    range_temp = range.split(" ")

    # calling function by passing list of books, low and high in a range
    result = booksInRange(books,int(range_temp[0]),int(range_temp[1]))
    if result.__len__()>0:
        print("You can purchase books:\n"+str(result))
    else:
        print("No books available in given range")

setBooks()