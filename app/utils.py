from app.database import book

def find_index(id: int):
    for i, p in enumerate(book):
        if p['id'] == id:
            return i
    return None  
