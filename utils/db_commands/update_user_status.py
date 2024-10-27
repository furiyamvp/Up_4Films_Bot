from sqlalchemy.exc import SQLAlchemyError

from main.database import database
from main.models import users


async def admin_update_user_status(user_id: int, new_value):
    try:
        query = users.update().where(users.c.id == user_id).values(status=new_value)
        await database.execute(query=query)
        return True
    except SQLAlchemyError as e:
        error_text = f"Error updating user's status with ID {user_id}: {e}"
        print(error_text)
        return {"error": error_text}
