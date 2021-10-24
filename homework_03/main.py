from fastapi import FastAPI, Body

import crud
from schemas import UserIn, UserOut


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/{user_id}/friends/")
def get_friends(user_id: int):
    return {
        "id": user_id,
        "friends":[
            {"id": 123, "bd": None, "close_friend": False}
        ]
    }


@app.get("/users/", response_model=list)
def get_users():
    users = crud.users_list()
    return users


@app.get("/ping/")
def homework_mock():
    mock_response = {"message": "pong"}
    return mock_response


@app.post("/item/")
def create_item(data: dict = Body(...)):
    """
    # Header
    ## HEader 2
    ### Header 3
     - Creates new item
    """
    return {
        "item": data,
    }


@app.post("/users/", response_model=UserOut)
def create_user(user_in: UserIn):
    user = crud.create_user(user_in)
    return user