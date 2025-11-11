import json
from typing import Union
from fastapi.responses import JSONResponse
from fastapi import Request, status
from app.schemas.item_schema import ItemSchema
from app.services.item_service import create_and_update_in_one_transaction, delete_item, get_all_items, get_item_by_id, create_item, get_items_by_price_filter, update_item
from app.api.routes import api_router
from .decorators import x_api_key_required

@api_router.get("/items/filter")
@x_api_key_required()
def read_item_with_filter(request: Request, price_min: Union[int, None] = None, price_max: Union[int, None] = None):
    if price_min is None and price_max is None:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "At least one filter parameter (price_min or price_max) must be provided"})
    
    items = get_items_by_price_filter(price_min, price_max)

    if not items:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "Item not found with the given filters"})

    return items

@api_router.get("/items/{item_id}")
@api_router.get("/items")
@x_api_key_required()
def read_item(request: Request, item_id: int = None, q: Union[str, None] = None):
    if not item_id:
        return get_all_items()
    
    item = get_item_by_id(item_id)

    if not item:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "Item not found"})

    return item


@api_router.post("/items", status_code=status.HTTP_201_CREATED, response_model=ItemSchema)
@x_api_key_required()
def create_item_resource(request: Request, item: ItemSchema):
    item = create_item(**item.model_dump())
    if not item:
        return JSONResponse(status_code=400, content={"error": "Item with the same name already exists"})
    
    return item

@api_router.post("/items/create_v2", response_model=ItemSchema, status_code=status.HTTP_201_CREATED)
@x_api_key_required()
def create_item_resource_v2(request: Request, item: ItemSchema):
    item = create_and_update_in_one_transaction(**item.model_dump())
    if not item:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"error": "Item with the same name already exists"})
    
    return item

@api_router.put("/items/{item_id}", status_code=status.HTTP_200_OK)
@api_router.patch("/items/{item_id}", status_code=status.HTTP_200_OK)
@x_api_key_required()
def update_item_resource(request: Request, item_id: int, data: dict):
    updated_item = update_item(item_id, **data)

    if not updated_item:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "Item not found"})
    
    return updated_item


@api_router.delete("/items/{item_id}", status_code=status.HTTP_200_OK)
@x_api_key_required()
def delete_item_resource(request: Request, item_id: int):
    success = delete_item(item_id)
    if not success:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"error": "Item not found"})
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Item deleted successfully"})

