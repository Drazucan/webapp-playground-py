from sqlmodel import SQLModel, Field


class PlayAppUser(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str # Not indexing because display names are intended to be changed by users
    password: str
    email: str
    age: int

