"""User Model."""
from masoniteorm.models import Model
from masoniteorm.scopes import SoftDeletesMixin
from masonite.authentication import Authenticates
import bcrypt
from masonite.facades import Dump


class User(Model, SoftDeletesMixin, Authenticates):
    """User Model."""

    __fillable__ = ["name", "email", "password"]
    __hidden__ = ["password"]
    __auth__ = "email"

    def get_firstname_attribute(self):
        return self.name.split(" ")[0]

    def get_lastname_attribute(self):
        return self.name.split(" ")[1]

    def update_profile(self, data):
        # Dump.dd(data)
        self.name = data["first_name"]+" "+data["last_name"]
        self.email = data["email"]
        self.phone = data["phone"] if 'phone' in data else ""
        if 'current_password' in data and data["current_password"] :
            if bcrypt.checkpw(bytes(data["current_password"], 'utf-8'), bytes(self.password, 'utf-8')):
                self.password= bcrypt.hashpw(bytes(data["new_password"], 'utf-8'), bcrypt.gensalt()).decode()
        self.save()            