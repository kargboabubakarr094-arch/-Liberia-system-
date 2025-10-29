books = {}
members = []
genres = ('Fiction', 'Non-Fiction', 'Sci-Fi')

def add_book(ISBN, title, author, genre, total_copies):
    if not all([ISBN, title, author, genre]) or total_copies < 1:
        return "All fields required, total copies at least 1!"
    if ISBN in books:
        return "ISBN already exists!"
    if genre not in genres:
        return "Genre must be Fiction, Non-Fiction, or Sci-Fi!"
    books[ISBN] = {'title': title, 'author': author, 'genre': genre, 'total_copies': total_copies}
    return "Book added successfully!"

def add_member(member_id, name, email):
    if not name or not email:
        return "Name and email required!"
    for member in members:
        if member['member_id'] == member_id:
            return "Member ID already exists!"
    members.append({'member_id': member_id, 'name': name, 'email': email, 'borrowed_books': []})
    return "Member added successfully!"

def search_book(keyword):
    if not keyword:
        return "Keyword required!"
    results = []
    for ISBN, details in books.items():
        if keyword.lower() in details['title'].lower() or keyword.lower() in details['author'].lower():
            results.append({'ISBN': ISBN, 'title': details['title'], 'author': details['author'], 'genre': details['genre'], 'total_copies': details['total_copies']})
    return results if results else "No books found!"

def update_book(ISBN, **details):
    if ISBN not in books:
        return "ISBN not found!"
    if 'genre' in details and details['genre'] not in genres:
        return "Invalid genre!"
    if 'total_copies' in details and details['total_copies'] < 0:
        return "Total copies cannot be negative!"
    books[ISBN].update(details)
    return "Book updated successfully!"

def delete_book(ISBN):
    if ISBN not in books:
        return "ISBN not found!"
    for member in members:
        if ISBN in member['borrowed_books']:
            return "Cannot delete borrowed book!"
    del books[ISBN]
    return "Book deleted successfully!"

def borrow_book(ISBN, member_id):
    if ISBN not in books:
        return "ISBN not found!"
    if books[ISBN]['total_copies'] < 1:
        return "No copies available!"
    member = next((m for m in members if m['member_id'] == member_id), None)
    if not member:
        return "Member not found!"
    if len(member['borrowed_books']) >= 3:
        return "Borrowing limit (3 books) reached!"
    member['borrowed_books'].append(ISBN)
    books[ISBN]['total_copies'] -= 1
    return "Book borrowed successfully!"

def return_book(ISBN, member_id):
    if ISBN not in books:
        return "ISBN not found!"
    member = next((m for m in members if m['member_id'] == member_id), None)
    if not member:
        return "Member not found!"
    if ISBN not in member['borrowed_books']:
        return "Book not borrowed by member!"
    member['borrowed_books'].remove(ISBN)
    books[ISBN]['total_copies'] += 1
    return "Book returned successfully!"