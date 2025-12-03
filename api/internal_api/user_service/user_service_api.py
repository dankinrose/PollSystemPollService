from typing import Optional

import httpx

from config.config import Config
from api.internal_api.user_service.model.user_response import UserResponse

config = Config()


async def get_user_by_id(user_id: int) -> Optional[UserResponse]:
    url = f"{config.USER_SERVICE_BASE_URL}/user/{user_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            if response.status_code == 404:
                return None

            response.raise_for_status()
            data = response.json()
            return UserResponse(**data)

        except Exception as exc:
            print(f"Error getting user {user_id} from User Service: {exc}")
            return None
