from app import app, api
from app.operations import Regex, Fuzzy, Whitelist
from app.utils import Streaming
from flask import Flask, request, g
from flask_restful import Api, Resource, reqparse
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity, get_jwt_claims
)

from bson.json_util import dumps as loadbson
import json
import asyncio


class APIWhitelists(Resource):
    decorators = []

    def __init__(self):
        self.args = reqparse.RequestParser()
        if request.method == "POST":
            self.args.add_argument('value', location='json', required=True, help='Value', type=str)

        if request.method == "GET":
            self.args.add_argument('skip', location='args', help='Start', required=False, type=int)
            self.args.add_argument('limit', location='args', required=False, type=int)
            self.args.add_argument('value', required=False, default='', type=str)


    def get(self):
        args = self.args.parse_args()
        result = Whitelist(args.value).get()
        return result

    def post(self):
        args = self.args.parse_args()
        result = Whitelist(args.value).create()
        asyncio.run(Streaming('whitelist').refresh())
        return result

api.add_resource(APIWhitelists, '/api/v1/whitelist')


class APIWhitelist(Resource):
    decorators = []

    def delete(self, whitelist_name):
        result = Whitelist(whitelist_name).delete()
        asyncio.run(Streaming('whitelist').refresh())
        return result

api.add_resource(APIWhitelist, '/api/v1/whitelist/<string:whitelist_name>')


class APIRegex(Resource):
    decorators = []

    def __init__(self):
        self.args = reqparse.RequestParser()
        if request.method == "POST":
            self.args.add_argument('value', location='json', required=True, help='Value', type=str)
            self.args.add_argument('score', location='json', required=False, default=80, type=int)

        if request.method == "GET":
            self.args.add_argument('start', location='args', help='Start', required=False, type=int)
            self.args.add_argument('limit', location='args', required=False, type=int)
            self.args.add_argument('value', required=False, default='', type=str)


    def post(self):
        args = self.args.parse_args()
        result = Regex(args.value).create(args.score)
        asyncio.run(Streaming('regex').refresh())
        return result

    def get(self):
        args = self.args.parse_args()
        result = Regex(args.value).get()
        return result

api.add_resource(APIRegex, '/api/v1/filters/regex')


class APIFuzzy(Resource):
    decorators = []

    def __init__(self):
        self.args = reqparse.RequestParser()
        if request.method == "POST":
            self.args.add_argument('value', location='json', required=True, help='Value', type=str)
            self.args.add_argument('likelihood', location='json', required=True, help='Likelihood', default=None, type=int)
            self.args.add_argument('score', location='json', required=False, default=80, type=int)


        if request.method == "GET":
            self.args.add_argument('start', location='args', help='Start', required=False, type=int)
            self.args.add_argument('limit', location='args', required=False, type=int)
            self.args.add_argument('value', required=False, default='', type=str)

    def post(self):
        args = self.args.parse_args()
        result = Fuzzy(args.value).create(args.likelihood, args.score)
        asyncio.run(Streaming('fuzzy').refresh())
        return result

    def get(self):
        args = self.args.parse_args()
        result = Fuzzy(args.value).get()
        return result

api.add_resource(APIFuzzy, '/api/v1/filters/fuzzy')


class APIFilter(Resource):
    decorators = []

    def delete(self, filter_type, filter_name):
        if filter_type == 'fuzzy':
            result = Fuzzy(filter_name).delete()
            asyncio.run(Streaming('fuzzy').refresh())

        elif filter_type == 'regex':
            result = Regex(filter_name).delete()
            asyncio.run(Streaming('regex').refresh())
        else:
            result = {'result':'failed', 'data':'Invalid filter type '}

        return result


api.add_resource(APIFilter, '/api/v1/filter/<string:filter_type>/<string:filter_name>')
