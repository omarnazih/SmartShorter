from app import app, db
from flask import request, json, jsonify
from flask_cors import CORS
from app.models import Url

# Allow access for all domains in development env
# if app.config['ENV'] == 'development':
# !remove on prodcution
CORS(app)

@app.route('/')
def index():        
    return {'status': 'OK',
            f'{request.url}shortlinks': 'Show all shortned links',
            f'{request.url}createshortlink': 'Create new shortlink',
            f'{request.url}shortlinks/<slug>': 'Update shortlink slug'}, 200


@app.route('/createshortlink', methods=['POST'])
def createShortLink():            
    return Url().insert()     

@app.route('/shortlinks', methods=['GET'])
def shortLinks():                
    return Url().retreive_all()    

@app.route('/shortlinks/<slug>', methods=['GET', 'PUT'])
def updateShortLink(slug):  
    if request.method == 'GET':
        return Url().get(slug) 

    return Url().update(slug)                

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response    