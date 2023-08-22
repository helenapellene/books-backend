# #The three biggest are:

# #.dict() function is now renamed to .model_dump()

# #schema_extra function within a Config class is now renamed to json_schema_extra

# #Optional variables need a =None example: id: Optional[int] = None




# from typing import Optional
# from fastapi import FastAPI, Path, Query, HTTPException
# from pydantic import BaseModel, Field
# from starlette import status

# app = FastAPI()

# class Book:
#     id: int
#     title: str
#     author: str
#     categoria: str
#     descrip: str
#     precio: int
#     fechapublic:int

#     def __init__(self, id, title, author, categoria, descrip, precio,fechapublic):
#         self.id = id
#         self.title = title
#         self.author = author
#         self.categoria = categoria
#         self.descrip=descrip
#         self.precio = precio
#         self.fechapublic=fechapublic
        

# class BookRequest(BaseModel):
#     id: Optional[int] = None
#     title: str = Field(min_length=3)
#     author: str = Field(min_length=1)
#     categoria: str = Field(min_length=3)
#     descrip: str = Field(min_length=5)
#     precio: int = Field(gt=0)
#     fechapublic: int = Field(gt=1990, lt=2023)

#     class Config:
#         json_schema_extra = {
#             'example': {
#                 'title': 'A new book',
#                 'author': 'codingwithroby',
#                 'categoria': 'poesia',
#                 'descrip':'Un libro sobre amor',
#                 'precio': 5,
#                 'fechapublic':1995
#             }
#         }




# BOOKS=[
#     Book(1, 'Prosa completa', 'Alejandra Pizarnik', 'poesia','Un libro sobre fasfsa', 1500,2019),
#     Book(2, 'Quien no', 'Claudia Piñeiro', 'novela','Un libro sobre afsafsamor', 524142,2014),
#     Book(3, 'Muerte en la vicaria', 'Agatha Christie', 'novela','Un libro sobre fasfs', 421425,2011),
#     Book(4, 'Novelas breves', 'Elena Garro', 'novela','Un libro sobre afahgmor', 5322,2017),
#     Book(5, 'Prostitucion/Trabajo Sexual', 'Diana Maffia', 'ensayo','Un libro sobre amjgdor', 3535,2010),
#     Book(6, 'Invenciones del Recuerdo', 'Silvina Ocampo', 'biografias','Un libro sobre jdf', 1455,2019),
#     Book(7, 'Antologias', 'Silvina Ocampo', 'ficcion','Un libro sobre agdsmor', 152578,2019)
# ]


# @app.get("/books", status_code=status.HTTP_200_OK)
# async def read_all_books():
#     return BOOKS



# @app.get("/books/{book_id}",status_code=status.HTTP_200_OK)
# async def read_book(book_id:int = Path(gt=0)):
#     for book in BOOKS:
#         if book.id==book_id:
#             return book
#     raise HTTPException(status_code=404, detail="Item not found")

# @app.get("/books/publish/",status_code=status.HTTP_200_OK)
# async def buscar_fecha(book_fecha:int = Query(gt=1990, lt=2023)):
#     books_to_return=[]
#     for book in BOOKS:
#         if book.fechapublic==book_fecha:
#             books_to_return.append(book)
#     return books_to_return
    




# @app.post("/create-book",status_code=status.HTTP_201_CREATED)
# async def create_book(book_request: BookRequest):
#     new_book=Book(**book_request.model_dump())
#     BOOKS.append(find_book_id(new_book))

# def find_book_id(book:Book):
#     if len(BOOKS)>0:
#         book.id=BOOKS[-1].id+1 
#     else  :
#         book.id=1
#     return book


# @app.put("/books/update_book",status_code=status.HTTP_204_NO_CONTENT)
# async def update_book(book: BookRequest):
#     book_changed = False
#     for i in range (len(BOOKS)):
#         if BOOKS[i].id==book.id:
#             BOOKS[i]=book
#             book_changed = True
#     if not book_changed:
#         raise HTTPException(status_code=404, detail="Item not found")





# @app.delete("/books/{book_id}",status_code=status.HTTP_204_NO_CONTENT)
# async def delete_book(book_id:int = Path(gt=0)):
#     book_changed = False
#     for i in range (len(BOOKS)):
#         if BOOKS[i].id==book_id:
#             BOOKS.pop(i)
#             book_changed = True

#             break
#     if not book_changed:
#         raise HTTPException(status_code=404, detail="Item not found")
