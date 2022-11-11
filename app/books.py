from fastapi import FastAPI, Query
from pydantic import BaseModel

tags_metadata = [
    {
        "name": "book",
        "description": "Operations with books. You can list them or add books."
    }
]

app = FastAPI(
    openapi_tags=tags_metadata,
    title="Book API",
    description="An API to keep track of your books.",
    contact={
        "name": "Caro Daems",
        "email": "r0889345@student.thomasmore.be"
    }
)


class Book(BaseModel):
    title: str
    author: str
    page_count: int
    publisher: str
    format: str


book_start = {
    "title": "Tower of Dawn",
    "author": "Sarah J Maas",
    "page_count": 644,
    "publisher": "Bloomsbury",
    "format": "hardback"
}

books = {0: book_start}


@app.get("/books", tags=["book"])
async def get_books():
    return books


@app.get("/book/{id}", tags=["book"])
async def get_book(book_id: int | None = Query(
    description="The id of the book you would like to display information for."
)):
    if book_id in books:
        return books[book_id]
    else:
        return {"error": "This book was not found."}


@app.post("/books", response_model=Book, tags=["book"])
async def create_book(book: Book):
    key = max(books, key=books.get) + 1
    books[key] = book
    return books[key]
