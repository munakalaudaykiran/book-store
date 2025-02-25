from fastapi import FastAPI
from task.database import enginee
from task.routers import author_router,books_router,auth
from task.models import Base


app=FastAPI()

Base.metadata.create_all(bind=enginee)


app.include_router(author_router.router, prefix="/author", tags=["Authors"])

app.include_router(books_router.router,prefix="/book",tags=["Books"])

app.include_router(auth.router,prefix="/auth",tags=["Authentication"])
