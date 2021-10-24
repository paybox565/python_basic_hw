from schemas import UserOut, UserIn, User


USER_ID_TO_USER: dict = {}
USER_TOKEN_TO_USER: dict = {}


def create_user(user_in: UserIn) -> User:
    user = User(id=len(USER_ID_TO_USER) + 2,**user_in.dict())
    USER_ID_TO_USER[user.id] = user
    USER_TOKEN_TO_USER[user.token] = user
    return user


def users_list() -> list:
    return list(USER_ID_TO_USER.values())
