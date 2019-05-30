from app.models import Users
import hashlib

class Authentication:
    def login(username, password):
        try:
            userobject = Users.objects.get(username=username)
            salt = userobject.salt
            passhash = hashlib.sha512()
            passwordhash = salt + password
            passhash.update(passwordhash.encode('utf-8'))
            passhash = str(passhash.hexdigest())

            if passhash == userobject.password:
                result = {'result': 'success', 'message': 'Succesfull login','data': userobject}

            else:
                result = {'result': 'failed', 'message': 'Wrong username and/or password'}

        except mongoengine.errors.DoesNotExist:
            result = {"result":"failed", "message":"Wrong username and/or password"}

        return result

    def blacklist(token):
        try:
            profile = RevokedTokens.objects.get(token=token)
            result = True

        except mongoengine.errors.DoesNotExist:
            result = False

        except Exception as err:
            result = False
            
        return result