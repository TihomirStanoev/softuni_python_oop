class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        username_length = len(value)
        if username_length < 5 or username_length > 15 :
            raise ValueError('The username must be between 5 and 15 characters.')
        self.__username = value

    @property
    def password(self):
        return '*' * len(self.__password)

    @password.setter
    def password(self, value):
        if not Profile._is_valid(value):
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

        self.__password = value


    @staticmethod
    def _is_valid(value):
        is_long = len(value) >= 8
        has_uppercase = any(el for el in value if el.isupper())
        has_digit = any(el for el in value if el.isdigit())

        return is_long and has_uppercase and has_digit


    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {self.password}'



correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
