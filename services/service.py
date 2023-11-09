from db import db
import boto3
from boto3.dynamodb.conditions import Key

cur = db.table

def get_all_product():
    response = cur.scan()

    if 'Items' not in response:
        return []

    return response['Items']

def get_product(id):
    if id :
        item_key = {"id":f"{id}"}
        res = cur.get_item(Key = item_key)
        if 'Item' not in res:
            return {}
        return res['Item']
    else:
        return {}
    

def create_product(product):
    response = cur.scan()
    len1 = len(response['Items']) + 1
    product["id"] = f"{len1}"

    created = cur.put_item(
        Item=product
    )

    if 'Item' not in created:
        return product
    return created['Item']


def update_product(id, product):
    item_key = {"id":f"{id}"}
    print(product);
    print(product['item'])
    response = cur.update_item(
        Key=item_key,
        UpdateExpression='SET #item = :item, #description = :description, #price = :price, #quantity = :quantity, #image = :image',
        ExpressionAttributeNames={
            "#item": "item",
            "#description" :"description", 
            "#price":"price", 
            "#quantity":"quantity", 
            "#image":"image"
        },
        ExpressionAttributeValues={
            ':item': product['item'],
            ':description': product['description'],
            ':price': product['price'],
            ':quantity': product['quantity'],
            ':image': product['image'],
        },
        ReturnValues="UPDATED_NEW",
    )
    return response['Attributes']

def delete_product(id):
    item_key = {"id":f"{id}"}
    response = cur.delete_item(
        Key=item_key
    )
    return id