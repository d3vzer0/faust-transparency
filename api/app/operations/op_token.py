from app.models import RevokedTokens
import mongoengine


class Token:
    def __init__(self, token):
        self.token = token

    def blacklist(self):
        try:
            profile = RevokedTokens(token=self.token).save()
            result = {'result': 'success', 'message': 'Succesfully added token to  blacklist'}

        except mongoengine.errors.NotUniqueError:
            result = {'result': 'failed', 'message': 'Token already exist in blacklist'}

        except Exception as err:
            result = {'result': 'failed', 'message': 'Unable to add token in blacklist'}

        return result

