import bcrypt

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String

from .base_model import BaseModel


class UserModel(BaseModel):
    __tablename__ = 'users'

    username: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(String(20), nullable=False)
    encrypted_password: Mapped[str] = mapped_column(String(100), nullable=False)

    projects = relationship('ProjectModel', back_populates='owner')

    @property
    def password(self) -> str:
        return self.encrypted_password

    @password.setter
    def password(self, plain_password: str) -> None:
        hashed_pass = bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())
        self.encrypted_password = hashed_pass.decode('utf-8')

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
