from app.models.item_models import Item
from app.db.connections import db
from sqlalchemy.exc import SQLAlchemyError

def get_item_by_id(item_id: int) -> Item:
    # Logic to retrieve an item by its ID from the database
    return db.query(Item).filter(Item.id == item_id).first()
    
def get_items_by_price_filter(price_min: int = None, price_max: int = None) -> list[Item]:
    query = db.query(Item)
    if price_min is not None:
        query = query.filter(Item.price >= price_min)
    if price_max is not None:
        query = query.filter(Item.price <= price_max)

    return query.all()

def create_item(name: str, description: str, price: int, **kwargs) -> Item:
    # Logic to create a new item in the database
    existing_item = db.query(Item).filter(Item.name == name).first()
    if existing_item:
        return None  # Item with the same name already exists
    
    new_item = Item(name=name, description=description, price=price)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


def create_and_update_in_one_transaction(db, new_item_data, update_item_id):
    try:
        with db.begin():
            new_item = Item(**new_item_data)
            db.add(new_item)

            db.query(Item).filter(Item.id == update_item_id).update({"price": 500})

        return {"message": "Transaction successful"}

    except SQLAlchemyError as e:
        return {"error": f"Transaction failed: {str(e)}"}


def update_item(item_id: int, **kwargs) -> Item:
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        return None

    updates = {k: v for k, v in kwargs.items() if v is not None}

    for key, value in updates.items():
        setattr(item, key, value)

    db.commit()
    db.refresh(item)
    return item


def get_all_items() -> list[Item]:
    print("Fetching all items from the database")
    return db.query(Item).all()


def delete_item(item_id: int) -> bool:
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        return False

    db.delete(item)
    db.commit()
    return True