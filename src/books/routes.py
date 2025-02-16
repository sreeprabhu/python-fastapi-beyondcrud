from fastapi import APIRouter, HTTPException, status
from typing import List
from src.books.schemas import BookModel, BookUpdateModel
from src.books.book_data import books

book_router = APIRouter()
@book_router.get('/', response_model=List[BookModel])
async def get_all_books():
    return books

@book_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_book(book_data: BookModel) -> dict:
    new_book: BookModel = book_data.model_dump()
    books.append(new_book)
    return new_book

@book_router.get('/{book_id}', status_code=status.HTTP_200_OK)
async def get_book(book_id: int) -> dict:
    for book in books:
        if book['id'] == book_id:
            return book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found!")


@book_router.put('/{book_id}', status_code=status.HTTP_201_CREATED)
async def update_books(book_id: int, book_update_data: BookUpdateModel) -> dict:
    for book in books:
        if book['id'] == book_id:
            book['title'] = book_update_data.title
            book['publisher'] = book_update_data.publisher
            book['page_count'] = book_update_data.page_count
            book['language'] = book_update_data.language

            return book
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found!")

@book_router.delete('/{book_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_id: int) -> None:
    for book in books:
        if book['id'] == book_id:
            books.remove(book)

            return {}
        
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book Not Found!")