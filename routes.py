from flask import Blueprint, json, request
from app import extensions
webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/receiver', methods=["POST"])
def receiver():
    if request.headers['content-type'] == 'application/json':
        return json.dumps(request.json)
    return {}, 200
