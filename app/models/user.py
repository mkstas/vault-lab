from datetime import datetime

from sqlalchemy import Boolean, DateTime, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class User(Base):
    __tablename__ = "users"

    id:            Mapped[int]      = mapped_column(Integer, primary_key=True)
    email:         Mapped[str]      = mapped_column(String, unique=True, index=True)
    password_hash: Mapped[str]      = mapped_column(String)
    is_active:     Mapped[bool]     = mapped_column(Boolean)
    is_admin:      Mapped[bool]     = mapped_column(Boolean)
    created_at:    Mapped[datetime] = mapped_column(DateTime)

    __table_args__ = (Index("ix_users_email", "email"),)
