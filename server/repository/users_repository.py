from sqlalchemy.exc import IntegrityError

from server.database import db_connection
from server.database.models import UserModel
from server.exceptions import UniqFieldException


class UsersRepository:
    def __init__(self):
        self.db = db_connection.session

    def create(self, new_user_dict: dict) -> dict:
        new_user = UserModel(**new_user_dict)
        self.db.add(new_user)
        try:
            self.db.commit()
        except IntegrityError as ie:
            self.db.rollback()
            raise UniqFieldException(ie.args)
        self.db.refresh(new_user)
        return new_user.to_dict()

    def get_list(self, limit: int, offset: int) -> list[dict]:
        users = self.db.query(UserModel).order_by('id').limit(limit).offset(offset).all()
        return [user.to_dict() for user in users]

    def get_by_id(self, user_id: int) -> dict | None:
        user = self.__get_one(user_id)
        if user is None:
            return
        return user.to_dict()
    
    def get_by_username(self, username: str) -> dict | None:
        return self.db.query(UserModel).filter_by(username=username).first()

    def update(self, id: int, new_data: dict) -> dict | None:
        user = self.__get_one(id)
        if user is None:
            return
        for field in new_data.keys():
            setattr(user, field, new_data[field])
        self.db.commit()
        self.db.refresh(user)
        return user.to_dict()

    def delete(self, id: int) -> bool:
        user = self.__get_one(id)
        if user is None:
            return False
        self.db.delete(user)
        self.db.commit()
        return True
    
    def check_password(self, user_id: int, password: str) -> False:
        user = self.__get_one(user_id)
        if user is None: return False
        return user.check_password(password)


    def __get_one(self, user_id: int) -> UserModel | None:
        return self.db.query(UserModel).filter_by(id=user_id).first()
