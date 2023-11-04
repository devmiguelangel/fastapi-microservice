from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI, HTTPException
from models.users  import Gender, Role, User, UserEdit

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender=Gender.male,
        roles=[Role.admin, Role.user],
    ),
    User(
        id=uuid4(),
        first_name="Jamila",
        last_name="Ahmed",
        gender=Gender.female,
        roles=[Role.student],
    ),
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/users")
async def get_users():
    return db

@app.post("/api/v1/users")
async def create_user(user: User):
    db.append(user)
    return user

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for index, user in enumerate(db):
        if user.id == user_id:
            db.pop(index)
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User with id: {0} not found".format(user_id))

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user: UserEdit):
    for index, user_item in enumerate(db):
        if user_item.id == user_id:
            if user.first_name is not None:
                db[index].first_name = user.first_name
            if user.last_name is not None:
                db[index].last_name = user.last_name
            if user.middle_name is not None:
                db[index].middle_name = user.middle_name
            if user.roles is not None:
                db[index].roles = user.roles
            return {"message": "User updated successfully"}

    raise HTTPException(status_code=404, detail="User with id: {0} not found".format(user_id))
