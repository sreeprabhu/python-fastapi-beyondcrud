from typing import List
from src.books.schemas import BookModel
from datetime import datetime

current_date_time: str = datetime.now()

books: List[BookModel] = [
    {"id": 1,"title": "Python", "author": "John", "publisher": "Sreeprabhu", "published_date": current_date_time, "page_count":123, "language": 'English'},
    {"id": 2,"title": "Python", "author": "John", "publisher": "Sreeprabhu", "published_date": current_date_time, "page_count":123, "language": 'English'},
    {"id": 3,"title": "Python", "author": "John", "publisher": "Sreeprabhu", "published_date": current_date_time, "page_count":123, "language": 'English'}
]