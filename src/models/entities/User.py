from werkzeug.security import check_password_hash
from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id, username, password, name="") -> None:
        self.id = id
        self.username = username
        self.password = password
        self.name = name

    @classmethod
    def check_password(self, hashed_password, password):
        return check_password_hash(hashed_password, password)

#Para hashear password:
#en el import: generate_password_hash
#print(generate_password_hash("gisela123456"))
#print(generate_password_hash("gabriel123456"))
