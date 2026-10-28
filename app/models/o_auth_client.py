from sqlalchemy import Boolean, DateTime, Index, Integer, String, JSON
from sqlalchemy.orm import Mapped, mapped_column

from base import Base


class OAuthClient(Base):
    __tablename__ = "o_auth_clients"

    id:              Mapped[int]       = mapped_column(Integer, primary_key=True)
    client_id:       Mapped[str]       = mapped_column(String, unique=True)
    name:            Mapped[str]       = mapped_column(String)
    is_confidential: Mapped[bool]      = mapped_column(Boolean)
    redirect_uris:   Mapped[list[str]] = mapped_column(JSON)
    created_at:      Mapped[bool]      = mapped_column(DateTime)
