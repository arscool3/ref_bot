from datetime import datetime

import sqlalchemy as sa
import sqlalchemy_utils as su
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from typing_extensions import Annotated

from src.types import Role

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    telegram_user_id: Mapped[str] = mapped_column(sa.String)
    name: Mapped[str]
    description: Mapped[str]
    role: Mapped[Annotated[Role, mapped_column(su.ChoiceType(Role, impl=sa.Text()))]]
    cv_url: Mapped[Annotated[str, mapped_column(sa.String, default="")]]
    current_company: Mapped[str]
    yoe: Mapped[int]


class Refer(Base):
    __tablename__ = "refers"

    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    candidate_id: Mapped[Annotated[int, mapped_column(sa.ForeignKey(User.id))]]
    refer_id: Mapped[Annotated[int, mapped_column(sa.ForeignKey(User.id), nullable=True)]]
    created_at: Mapped[Annotated[datetime, mapped_column(sa.DateTime(timezone=True), server_default=func.now())]]

