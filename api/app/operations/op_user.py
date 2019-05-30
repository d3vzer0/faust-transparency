from app.models import Users
from app.utils import Random
import mongoengine
import hashlib


class User:
    def __init__(self, username):
        self.username = username

    def create(self, password):
        try:
            salt = Random(32).create()
            password_hash = hashlib.sha512()
            password_string = salt + password
            password_hash.update(password_string.encode('utf-8'))
            password_hash = str(password_hash.hexdigest())

            user = Users(username=self.username, salt=salt,
                password=password_hash).save()

            result = {'result': 'created', 'message': 'Succesfully created user'}

        except mongoengine.errors.NotUniqueError:
            result = {'result': 'failed', 'message': 'User already exists'}

        except Exception as err:
            result = {'result': 'failed', 'message': 'Failed to create user'}

        return result

    def delete(self):
        try:
            user_object = Users.objects.get(username=self.username).delete()
            result = {'result': 'deleted', 'message': 'Deleted user from DB'}

        except mongoengine.errors.DoesNotExist:
            result = {'result': 'failed', 'message': 'User does not exist'}

        except Exception as err:
            result = {'result': 'failed', 'message': 'Failed to delete user from DB'}

        return result
