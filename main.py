from fastapi import FastAPI, Depends
from pydantic import BaseModel
from shemas import STaskAdd,STask
from typing import Optional,Annotated


from contextlib import asynccontextmanager

from database import delete_tables,create_tables

from router import router as task_router





@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print ("clean")
    await create_tables() 
    print ("starting")
    
    yield

    print ("shutdown")

app = FastAPI(lifespan=lifespan)

app.include_router(task_router)








tasks = []



