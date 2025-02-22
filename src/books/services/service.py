from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.schemas import BookCreateModel, BookUpdateModel
from src.books.models.models import BookModel
from sqlmodel import select, desc

from .base_service import BaseService


class BookService():
    # def __init__(self, session):
    #     super().__init__(session)

    async def get_all_books(self, session:AsyncSession):
        statement = select(BookModel).order_by(desc(BookModel.created_at))
        result = await session.exec(statement)

        return result.all()

    async def get_book(self, book_uuid: str, session:AsyncSession):
        statement = select(BookModel).where(BookModel.uid == book_uuid)
        result = await session.exec(statement)
        book = result.first()

        return book if not None else None

    async def create_book(self, book_data: BookCreateModel, session:AsyncSession):
        # to get the book data as a dictionary, use model_dump()
        book_data_dict = book_data.model_dump()

        # unpack all keys and values from book_data_dict into new_book object
        new_book = BookModel(
            **book_data_dict
        )

        session.add(new_book)
        await session.commit()

        return new_book

    async def update_book(self, book_uuid: str, update_data: BookUpdateModel, session:AsyncSession):
        book_to_update = self.get_book(book_uuid, session)

        if book_to_update is not None:
            update_data_dict = update_data.model_dump()

            for k, v in update_data_dict.items():
                setattr(book_to_update, k, v)

            await session.commit()

            return book_to_update
        else:
            return None

    async def delete_book(self, book_uuid: str, session:AsyncSession):
        book_to_delete = self.get_book(book_uuid, session)

        if book_to_delete is not None:
            await session.delete(book_to_delete)

            await session.commit()

        else:
            return None