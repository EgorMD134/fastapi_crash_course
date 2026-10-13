from fastapi import APIRouter,Depends
from typing import Optional,Annotated
from shemas import STaskAdd,STask,STaskId 
from repositoriy import TaskRepository

router = APIRouter(
    prefix = "/tasks",
    tags= ["tasks"]


)

@router.post("")
async def add_task(
    task: Annotated [STaskAdd,Depends()]

)-> STaskId:
    
    task_id = await TaskRepository.add_one(task)

    return {"ok":True , "task_id":task_id}


@router.get("/task")
async def get_task() -> list[STask]:

    tasks = await TaskRepository.find_all()
    

    return tasks