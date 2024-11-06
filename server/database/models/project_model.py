from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from .base_model import BaseModel


class ProjectModel(BaseModel):
    __tablename__ = 'projects'

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)
    priority: Mapped[str] = mapped_column(String(20), default='low', nullable=False)

    # Foreign Key
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))

    owner = relationship('UserModel', back_populates='projects')

    def to_dict(self):
        response = super().to_dict()
        if self.owner:
            response['owner'] = self.owner.to_dict()
        return response