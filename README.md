# Bookstore API

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x
- Django Rest Framework 3.x

### Installation

1. Clone the repository
2. Create a virtual environment
3. Install the dependencies
4. Create the database
5. Run the server

```bash
git clone https://github.com/yeboahd24/django-facade.git
cd bookstore-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Usage

### Create a book

```bash
curl -X POST \
  http://localhost:8000/api/books/ \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "price": 12.99
  }'
```

### Get all books

```bash
curl -X GET http://localhost:8000/api/books/
```

### Get a book

```bash
curl -X GET http://localhost:8000/api/books/1/
```

### Update a book

```bash
curl -X PUT \
  http://localhost:8000/api/books/1/ \
  -H 'Content-Type: application/json' \
  -d '{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "price": 12.99
  }'
```

### Delete a book

```bash
curl -X DELETE http://localhost:8000/api/books/1/
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

