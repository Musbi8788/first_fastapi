from fastapi import FastAPI

app = FastAPI()

task_manager =[
    {
    "id": 1, 
    "title": "Marketing",
    "description": "This is a marketing task for attendancegm",
    "completed": True
},
    {
    "id": 2, 
    "title": "Bill",
    "description": "This is billing task for attendancegm",
    "completed": False
}
] 

next = 1


@app.get("/tasks")
async def get_tasks(completed: bool = None):
    return task_manager

@app.get("/tasks/{task_id}")
async def get_task_by_id(task_id: int):
    item_id = task_id
    data = [item for item in task_manager if item["id"] == item_id ] 

    return data


@app.post("/tasks")
async def create_task(id:int , title:str , description:str,
completed:bool):
        new_task = {f"id": id, "title": title, "description":description, "completed":True}
        task_manager.append(new_task)
        return new_task



@app.put("/tasks/{task_id}")
async def update_task(id: int, title: str, description: str, completed: bool):
    item_id = id
    updated_task = {f"id": id, "title": title, "description":description, "completed": completed}
    for item in task_manager:
        if item["id"] == item_id:
            item.update(updated_task)
            
    return updated_task


@app.delete("/tasks/{task_id}")
async def detele_task(id:int):
    delete_id = id
    recent_task = [ del_task for del_task in task_manager if del_task.get("id") != delete_id]
    return recent_task