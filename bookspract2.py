#The three biggest are:

#.dict() function is now renamed to .model_dump()

#schema_extra function within a Config class is now renamed to json_schema_extra

#Optional variables need a =None example: id: Optional[int] = None




from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book:
    id: int
    title: str
    author: str
    categoria: str
    precio: int

    def __init__(self, id, title, author, categoria, precio):
        self.id = id
        self.title = title
        self.author = author
        self.categoria = categoria
        self.precio = precio
        

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    categoria: str = Field(min_length=3)
    precio: int = Field(gt=0)

    class Config:
        json_schema_extra = {
            'example': {
                'title': 'A new book',
                'author': 'codingwithroby',
                'categoria': 'A new description of a book',
                'precio': 5
            }
        }




BOOKS=[
    Book(1, 'Prosa completa', 'Alejandra Pizarnik', 'poesia', 1500),
    Book(2, 'Quien no', 'Claudia Piñeiro', 'novela', 524142),
    Book(3, 'Muerte en la vicaria', 'Agatha Christie', 'novela', 421425),
    Book(4, 'Novelas breves', 'Elena Garro', 'novela', 5322),
    Book(5, 'Prostitucion/Trabajo Sexual', 'Diana Maffia', 'ensayo', 3535),
    Book(6, 'Invenciones del Recuerdo', 'Silvina Ocampo', 'biografias', 1455),
    Book(7, 'Antologias', 'Silvina Ocampo', 'ficcion', 152578)
]


@app.get("/books")
async def read_books():
    return BOOKS


@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book=Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))

def find_book_id(book:Book):
    if len(BOOKS)>0:
        book.id=BOOKS[-1].id+1 
    else  :
        book.id=1
    return book
