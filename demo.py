import operations

# Add novels
print(operations.add_book("NOV001", "The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 5))
print(operations.add_book("NOV002", "Things Fall Apart", "Chinua Achebe", "Fiction", 4))
print(operations.add_book("NOV003", "The Alchemist", "Paulo Coelho", "Fiction", 3))
print(operations.add_book("NOV004", "1984", "George Orwell", "Sci-Fi", 2))
print(operations.add_book("NOV001", "Duplicate", "Author", "Fiction", 1))  # Fail: Duplicate

# Add members with local names
print(operations.add_member(1, "Jeremiah Dave", "jeremiah@local.sl"))
print(operations.add_member(2, "Amadu Coker", "amadu@local.sl"))
print(operations.add_member(3, "Fatima Bangura", "fatima@local.sl"))
print(operations.add_member(4, "Saidu Conteh", "saidu@local.sl"))
print(operations.add_member(5, "Mariama Kamara", "mariama@local.sl"))
print(operations.add_member(1, "Duplicate", "email@local.sl"))  # Fail: Duplicate

# Borrow novels
print(operations.borrow_book("NOV001", 1))  # Success
print(operations.borrow_book("NOV002", 1))  # Success
print(operations.borrow_book("NOV003", 1))  # Success
print(operations.borrow_book("NOV003", 1))  # Fail: Limit
print(operations.borrow_book("NOV005", 1))  # Fail: Not found
operations.update_book("NOV004", total_copies=0)
print(operations.borrow_book("NOV004", 2))  # Fail: No copies

# Search novels
print(operations.search_book("Great"))
print(operations.search_book("Alchemist"))
print(operations.search_book(""))  # Fail: Empty

# Update novel
print(operations.update_book("NOV001", title="The Great Gatsby Updated", total_copies=6))
print(operations.update_book("NOV001", genre="Mystery"))  # Fail: Invalid genre
print(operations.update_book("NOV005", title="Missing"))  # Fail: Not found

# Return novel
print(operations.return_book("NOV001", 1))  # Success
print(operations.return_book("NOV005", 1))  # Fail: Not borrowed

# Delete novel
print(operations.delete_book("NOV001"))  # Success
print(operations.delete_book("NOV002"))  # Fail: Borrowed
print(operations.delete_book("NOV005"))  # Fail: Not found

# Extra borrow with other member
print(operations.borrow_book("NOV004", 3))  # Success for Fatima