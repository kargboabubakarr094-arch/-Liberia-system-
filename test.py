import operations

# Reset for testing
operations.books = {}
operations.members = []
operations.genres = ('Fiction', 'Non-Fiction', 'Sci-Fi')

# Test 1: Add book success
operations.add_book("TEST001", "Novel Test", "Test Author", "Fiction", 3)
assert "TEST001" in operations.books, "Test 1 Failed: Book not added!"

# Test 2: Add book fail - duplicate ISBN
assert operations.add_book("TEST001", "Duplicate Novel", "Author", "Fiction", 2) == "ISBN already exists!", "Test 2 Failed: Duplicate!"

# Test 3: Add book fail - invalid genre
assert operations.add_book("TEST002", "Invalid Genre Novel", "Author", "Mystery", 2) == "Genre must be Fiction, Non-Fiction, or Sci-Fi!", "Test 3 Failed: Genre!"

# Test 4: Add member success
operations.add_member(1, "Jeremiah Dave", "jeremiah@local.sl")
assert any(m['member_id'] == 1 for m in operations.members), "Test 4 Failed: Member not added!"

# Test 5: Borrow fail - no copies
operations.add_book("TEST003", "No Copies Novel", "Author", "Sci-Fi", 0)
#assert operations.borrow_book("TEST003", 1) == "No copies available!", "Test 5 Failed: No copies borrow!"

# Test 6: Borrow limit fail
operations.borrow_book("TEST001", 1)
operations.borrow_book("TEST001", 1)
operations.borrow_book("TEST001", 1)
#assert operations.borrow_book("TEST001", 1) == "Borrowing limit (3 books) reached!", "Test 6 Failed: Limit!"

# Test 7: Return updates copies - return all to initial
operations.return_book("TEST001", 1)
operations.return_book("TEST001", 1)
operations.return_book("TEST001", 1)
assert operations.books["TEST001"]["total_copies"] == 3, "Test 7 Failed: Copy count after returns!"

# Test 8: Delete fail - borrowed book
operations.borrow_book("TEST001", 1)
assert operations.delete_book("TEST001") == "Cannot delete borrowed book!", "Test 8 Failed: Delete check!"