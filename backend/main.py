from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from database import SessionLocal ,engine
from pydantic import BaseModel 
from models import Todo,Base


Base.metadata.create_all(bind=engine)  # butun tabloları veri tabanını getirr

app= FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )


def get_db():
    db=SessionLocal()
    try:
        yield db 
    finally:
        db.close()

# ornek appim 
@app.get("/")
def root():
    return{"message":" hello world"}

@app.get("/hi")
def root():
    return{"message":"hi"} 

@app.get("/todos")   # butun todoları getiren 
def read_todos(db=Depends(get_db)): 
    todos=db.query(Todo).all()
    return todos

class TodoCreate(BaseModel):
    title: str

@app.post("/todos")   # ve yeni todo ekleyen fonksiyonlarım 
def create_todo( new_todo: TodoCreate, db=Depends(get_db)):
    db_todo=Todo(title=new_todo.title)
    db.add(db_todo)
    db.commit() # yansıt
    return {"message": "successfuly added"}
