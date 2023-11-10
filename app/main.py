# Code to demonstrate Synchronous REST Api - with the data stored in JSON file
# Demonstrated for GET, GET ID, POST, PUT AND DELETE HTTP Methods
# URL to run -> http://localhost:8001/docs which opens the Swagger API documentation
# Run Uvicorn - uvicorn main:app --reload --port=8002

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .services import service

app = FastAPI()

class Product(BaseModel):
    item: str
    description: str
    quantity: int
    image: str
    price: int
    

@app.get('/')
def getAllProducts():
    data = service.get_all_product()
    print(data)
    return data


@app.get('/products/{id}', status_code=200)
def get_product(id: int):
    try:
        data = service.get_product(id)
        return data
    except:
        return HTTPException(status_code=404, detail=f"Failed to fetch product with id {id}")



@app.post('/products', status_code=201)
def new_product(productObj: Product):
    try:
        new_product = {
            'item': productObj.item,
            'description': productObj.description,
            'quantity': productObj.quantity,
            'image': productObj.image,
            'price': productObj.price,
        }
        data = service.create_product(new_product)
        return data
    except:
        return HTTPException(status_code=404, detail=f"Product creation failed")


@app.delete('/products/{id}',status_code=200)
def delete_product(id: int):
    try:
        data = service.delete_product(id);
        return {'message': f"Successfully Deleted product with id {data}"}
    except:
        raise HTTPException(status_code=404, detail=f"There is no Product with id as {id}")

@app.put('/products/{id}', status_code=200)
def change_product(id: int, productObj: Product):
    try:
        update_product = {
            'item': productObj.item,
            'description': productObj.description,
            'quantity': productObj.quantity,
            'image': productObj.image,
            'price': productObj.price,
        }
        data = service.update_product(id, update_product)
        return data
    except:
        return HTTPException(status_code=404, detail=f"Product with id {id} does not exist")
