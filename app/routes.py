from flask import request, json, jsonify
from flask_cors import CORS

from app import app, db
from app.controller import *

# remove on prodcution
# Allow access for all domains while in development env
# if app.config['ENV'] == 'development':
CORS(app)

@app.route('/')
def index():        
    return {'status': 'OK',
            f'{request.url}shortlinks - GET': 'Fetch all shortlinks',
            f'{request.url}shortlinks - POST': 'Create new shortlink',
            f'{request.url}shortlinks/<slug>': 'Update shortlink slug'}, 200

@app.route('/<slug>')
def short_link(slug):        
    return  get_link(slug)

@app.route('/shortlinks', methods=['GET', 'POST'])
def short_links():       
    if request.method == 'GET':        
        return get_all_links()
        
    return create_link(request.json)


@app.route('/shortlinks/<slug>', methods=['PUT'])
def update_short_link(slug):      
    return update_link(slug, request.json)    

# Error Handlres
@app.errorhandler(400)
def bad_request(error):
    message = {
        'status': 'failed',
        'message': 'Bad Request'
    }
    response = jsonify(message)
    response.status_code = 400
    return response   

@app.errorhandler(404)
def not_found(error):
    message = {
        'status': 'failed',
        'message': 'not found'
    }
    response = jsonify(message)
    response.status_code = 404
    return response    

@app.errorhandler(500)
def internal_error(error):
    return {}, 500    