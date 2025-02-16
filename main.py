from fastapi import FastAPI, Header, status
from fastapi.exceptions import HTTPException
from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()


@app.get('/')
async def read_root():
    return {"message": "Hello World"}


@app.get('/greet')
async def greet_name(name: Optional[str] = "User", age: int = 0) -> dict:
    return {"message": f"Hello {name}", "age": age}


class BookCreateModel(BaseModel):
    title: str
    author: str


@app.post('/create_book')
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.title,
        "author": book_data.author
    }


@app.get('/get_headers')
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None)
):
    request_headers = {}

    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host

    return request_headers


#Books APIs starts here

class BookModel(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: datetime
    page_count: int
    language: str


class BookUpdateModel(BaseModel):
    title: str
    author: str
    publisher: str
    page_count: int
    language: str

current_date_time: str = datetime.now()

print(f"date: {current_date_time}")

books: List[BookModel] = [
    {"id": 1,"title": "Python", "author": "John", "publisher": "Sreeprabhu", "published_date": current_date_time, "page_count":123, "language": 'English'},
    {"id": 2,"title": "Python", "author": "John", "publisher": "Sreeprabhu", "published_date": current_date_time, "page_count":123, "language": 'English'},
    {"id": 3,"title": "Python", "author": "John", "publisher": "Sreeprabhu", "published_date": current_date_time, "page_count":123, "language": 'English'}
]

@app.get('/books', response_model=List[BookModel])
async def get_all_books():
    return books

@app.post('/books', status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookModel) -> dict:
    new_book: BookModel = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get('/book/{book_id}', status_code=status.HTTP_200_OK)
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found!")


@app.put('/book/{book_id}', status_code=status.HTTP_201_CREATED)
async def update_books(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found!")

@app.delete('/book/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> None:
    for book in books:
        if book['id'] == book_id:
            books.remove(book)

            return {}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found!")