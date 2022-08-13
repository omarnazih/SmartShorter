from app import app, db
from flask import jsonify, request


@app.route('/')
def index():    
    return {'status': 'OK',
            f'{request.url}shortlinks': 'Show all shortned links',
            f'{request.url}createshortlink': 'Create new shortlink',
            f'{request.url}shortlinks/<slug>': 'Update shortlink <slug>'}

@app.route('/shortlinks', methods=['GET'])
def shortLinks():
    return 'shortlinks'

@app.route('/createshortlink', methods=['POST'])
def createShortLink():
    # db.test.insert_one({'slug': 's5G1f3', 'link': "https://jsfiddle.net/8vb2pqtm/"})
    return 'createshortlink'

@app.route('/shortlinks/<slug>', methods=['PUT'])
def updateShortLink(slug):
    return f'updateShortLink {slug}'

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response    
