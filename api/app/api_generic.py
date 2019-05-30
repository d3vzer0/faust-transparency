from app import app, api, jwt
from app.models import Users
from app.operations import User, Token
from app.validators import Authentication
from flask import Flask, request, g, redirect
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims,
    create_refresh_token, jwt_refresh_token_required,
    get_raw_jwt
)


@jwt.user_claims_loader
def add_claims_to_access_token(user):
    result = {'role':user.role}
    return result


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.username


@jwt.expired_token_loader
def expired_token_callback():
    result = {'status':401, 'sub_status':42, 'data':'Token expired'}
    return json.dumps(result), 401


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    is_revoked = Authentication.blacklist(jti)
    return is_revoked


class APIUsers(Resource):
    decorators = []

    def __init__(self):
        self.args = reqparse.RequestParser()
        if request.method == "POST":
            self.args.add_argument('username', location='json',required=True, help='Username')
            self.args.add_argument('password', location='json', required=True, help='Password')
            self.args.add_argument('email', location='json', required=True, help='Username')

    def post(self):
        args = self.args.parse_args()
        operation = User().create(args['username'], args['password'], args['email'])
        return operation

    def get(self):
        users_objects = Users.objects().to_json()
        result = json.loads(user_object)
        return result

api.add_resource(APIUsers, '/api/v1/users')


class APIUser(Resource):
    decorators = []

    def delete(self, user_id=None):
        if user_id == None:
            result = {"result":"failed", "message":"Requires user ID"}
        else:
            current_user = str(g.currentUser.id)
            if user_id == current_user:
                result = {"result":"failed", "message":"Can't delete own user"}
            else:
                result = User().delete(user_id)

        return result

api.add_resource(APIUser, '/api/v1/user/<string:user_id>')


class APILogin(Resource):
    def __init__(self):
        self.args = reqparse.RequestParser()
        self.username = self.args.add_argument('username', location='json', required=True, help='Username')
        self.password = self.args.add_argument('password', location='json', required=True, help='Password')

    def post(self):
        args = self.args.parse_args()
        validate = Authentication.login(args['username'], args['password'])
        if validate['result'] == 'success':
            access_token = create_access_token(identity=validate['data'])
            refresh_token = create_refresh_token(identity=validate['data'])
            result = {"access_token":access_token, 'refresh_token':refresh_token}
            return result

        else:
            return validate, 401


api.add_resource(APILogin, '/api/v1/login')


class APIRefresh(Resource):
    decorators = [jwt_refresh_token_required]

    def get(self):
        user_object = Users.objects.get(username=get_jwt_identity())
        access_token = create_access_token(identity=user_object)
        result = {"access_token":access_token}
        return result

api.add_resource(APIRefresh, '/api/v1/refresh') 


class APILogoutRefresh(Resource):
    decorators = [jwt_refresh_token_required]

    def get(self):
        jti = get_raw_jwt()['jti']
        revoke_token = RevokeToken.create(jti)
        return revoke_token

api.add_resource(APILogoutRefresh, '/api/v1/logout/refresh')


class APILogout(Resource):
    decorators = [jwt_required]

    def get(self):
        jti = get_raw_jwt()['jti']
        revoke_token = RevokeToken.create(jti)
        return revoke_token

api.add_resource(APILogout, '/api/v1/logout/token')

