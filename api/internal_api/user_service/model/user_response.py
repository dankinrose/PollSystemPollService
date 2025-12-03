from pydantic import BaseModel


class UserResponse(BaseModel):
    id: int
    is_registered: bool
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None