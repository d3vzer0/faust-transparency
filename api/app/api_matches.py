
from app import app, api
from flask import Flask, request, g
from flask_restful import Api, Resource, reqparse
from app.models import Matches

class APIMatches(Resource):
    decorators = []

    def __init__(self):
        self.args = reqparse.RequestParser()
        if request.method == "GET":
            self.args.add_argument('skip', location='args', required=True, help='Start', type=int)
            self.args.add_argument('limit', location='args', required=True, help='Length', type=int)
            self.args.add_argument('search', location='args', required=False, help='Search', type=str, default="")

    def get(self):
        args = self.args.parse_args()
        matches_object = Matches.objects(target__contains=args['search']).order_by('-timestamp')
        matches_count = targets_object.count()
        get_matches = matches_object.skip(args.skip).limit(args.limit)
        all_hits = json.loads(get_matches.to_json())
        results = {'count':matches_count, 'results':all_hits}
        return results


api.add_resource(APIMatches, '/api/v1/matches')
