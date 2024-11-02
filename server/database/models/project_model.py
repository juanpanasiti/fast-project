from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from .base_model import BaseModel


class ProjectModel(BaseModel):
    __tablename__ = 'projects'

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)
    priority: Mapped[str] = mapped_column(String(20), default='low', nullable=False)
