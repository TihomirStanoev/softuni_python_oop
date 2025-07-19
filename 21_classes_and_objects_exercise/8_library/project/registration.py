from project.user import User
from project.library import Library

class Registration:
    @staticmethod
    def _is_registered(user, library):
        return next((u for u in library.user_records if u.user_id == user.user_id),None)

    @staticmethod
    def add_user(user:User, library: Library):
        if not Registration._is_registered(user, library):
            library.user_records.append(user)
            return None
        return f'User with id = {user.user_id} already registered in the library!'

    @staticmethod
    def remove_user(user:User, library:Library):
        if not Registration._is_registered(user, library):
            return 'We could not find such user to remove!'
        library.user_records.remove(user)

    @staticmethod
    def change_username(user_id: int, new_username: str, library: Library):
        user = next((u for u in library.user_records if u.user_id == user_id), None)

        if not user:
            return f'There is no user with id = {user_id}!'
        if user.username == new_username:
            return 'Please check again the provided username - it should be different than the username used so far!'

        user.username = new_username
        return f'Username successfully changed to: {new_username} for user id: {user_id}'