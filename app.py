from fastapi import FastAPI  
from pydantic import BaseModel, Field

app = FastAPI()


class Product(BaseModel):
    name : str = Field(ge=2, le=100)
    price : float = Field(ge=0)
    category: str 
    description : str = Field(max_length=100)


@app.post("/create")
async def create_product(Product):
    return {
        "successfully created"
    }