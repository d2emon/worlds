import uuid


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    },
]


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


def add_book(data):
    BOOKS.append({
        'id': uuid.uuid4().hex,
        'title': data.get('title'),
        'author': data.get('author'),
        'read': data.get('read')
    })
    return True


def edit_book(book_id, data):
    remove_book(book_id)
    BOOKS.append({
        'id': uuid.uuid4().hex,
        'title': data.get('title'),
        'author': data.get('author'),
        'read': data.get('read')
    })
    return True
