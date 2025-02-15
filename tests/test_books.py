from tests import client


def test_get_all_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert len(response.json()) == 3


def test_get_single_book():
    response = client.get("/books/1")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"


def test_create_book():
    new_book = {
        "id": 4,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "publication_year": 1997,
        "genre": "Fantasy",
    }
    response = client.post("/books/", json=new_book)
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 4
    assert data["title"] == "Harry Potter and the Sorcerer's Stone"


def test_update_book():
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put("/books/1", json=updated_book)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit: An Unexpected Journey"


def test_delete_book():
    response = client.delete("/books/3")
    assert response.status_code == 204

    response = client.get("/books/3")
    assert response.status_code == 404


def test_get_book_success():
    response = client.get("/books/1")
    assert response.status_code == 200
    assert response.json()["title"] == "The Hobbit: An Unexpected Journey"

# Test to get a single book by ID (not found case)
# This test will fail because the book with ID 999 does not exist


def test_get_book_not_found():
    response = client.get("/books/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}

# Test to get a single book by invalid ID format


def test_get_book_invalid_id():
    response = client.get("/books/12invalid")
    assert response.status_code == 404
    assert response.json() == {"detail": "Book not found"}
