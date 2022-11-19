import random
from random import randint
import requests
import json

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


tags_metadata = [
    {
        "name": "book",
        "description": "Operations with books. You can list them or add books."
    },
    {
        "name": "random book",
        "description": "Request a random book to read."
    },
    {
        "name": "display",
        "description": "Retrieval of information used for display purposes. This makes use of an external Google Books API"
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

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://127.0.0.1:5500",
    "https://carodaems.github.io",
    "http://carodaems.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Book(BaseModel):
    title: str
    author: str
    page_count: int
    publisher: str
    format: str
    ISBN: str


books = {
    0: {
        "title": "Tower of Dawn",
        "author": "Sarah J Maas",
        "page_count": 644,
        "publisher": "Bloomsbury",
        "format": "hardback",
        "ISBN": "1681195771"
    },
    1: {
        "title": "Empire of Storms",
        "author": "Sarah J Maas",
        "page_count": 704,
        "publisher": "Bloomsbury",
        "format": "hardback",
        "ISBN": "1619636093"
    }
}

#books = {0: book_start}

# get a list of all the books


@app.get("/books", tags=["book"])
async def get_books():
    return books


# return a specific book from the list
@app.get("/book/{book_id}", tags=["book"])
async def get_book(book_id: int | None = Query(
    default=None,
    description="The id of the book you would like to display information for.",
)):
    if book_id in books:
        return books[book_id]
    else:
        return {"error": "This book was not found."}


# pick a random book from the list
@app.get("/randombook", tags=["random book"])
async def get_random_book():
    choice = random.choice(list(books.keys()))
    return books[choice]


# get the cover from an ISBN
@app.get("/{ISBN}", tags=["display"])
async def get_cover(ISBN: str | None = Query(
    default=None,
    description="The ISBN of the book a cover needs to be retreived for.",
)):
    URL = "https://www.googleapis.com/books/v1/volumes?q=isbn:{0}".format(ISBN)
    response = requests.get(URL)
    obj = json.loads(response.text)
    cover_link = obj['items'][0]['volumeInfo']['imageLinks']['thumbnail']
    return cover_link


# add a book to the list
@app.post("/books", response_model=Book, tags=["book"])
async def create_book(book: Book):
    key = max(books, key=books.get) + 1
    books[key] = book
    return books[key]
