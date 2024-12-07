# База данных пользователей
import logging

logger = logging.getLogger(__name__)


class UserAlreadyExistError(Exception):
    ...


users = {
    1: {"name": "Alice", "email": "alice@example.com", "age": 25},
    2: {"name": "Bob", "email": "bob@example.com", "age": 30},
}


def add_user(user_id, name, email, age):
    """
    Добавляет нового пользователя в базу данных.
    Если пользователь с таким user_id уже существует, возвращает ошибку.
    """
    if user_id in users:
        raise UserAlreadyExistError(f'User with id {user_id} already exist')
    else:
        users[user_id] = {"name": name, "email": email, "age": age}
        logger.info(f"Пользователь с ID {user_id} успешно добавлен.")

def get_user_by_id(user_id):
    """
    Возвращает информацию о пользователе по его user_id.
    Если пользователь не найден, возвращает None.
    """
    return users.get(user_id)
