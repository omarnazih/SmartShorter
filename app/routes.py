from app import app, db
from flask import request, json, jsonify


@app.route('/')
def index():    
    return {'status': 'OK',
            f'{request.url}shortlinks': 'Show all shortned links',
            f'{request.url}createshortlink': 'Create new shortlink',
            f'{request.url}shortlinks/<slug>': 'Update shortlink <slug>'}, 200


@app.route('/shortlinks', methods=['GET'])
def shortLinks():    
    shortlinks_db_list = []

    # Return all shortlinks from mongodb
    shortlinks = db.test.find({})
    for entry in shortlinks:        
        row = {
            'slug': entry['slug'],
            'link': entry['link'],
        }
        shortlinks_db_list.append(row)
    
    response = {
        'data':shortlinks_db_list
    }    
        
    return jsonify(response), 200
    


@app.route('/createshortlink', methods=['POST'])
def createShortLink():            
    if not request.is_json:
        return jsonify({"msg":"Missing JSON in request", "status":400}), 400
        
    req_data = request.get_json()
    print(req_data)

    return req_dat


@app.route('/shortlinks', defaults={'slug':None}, methods=['PUT'])
@app.route('/shortlinks/<slug>', methods=['PUT'])
def updateShortLink(slug):    
    # !NOTE Slug stays as it is
    return f'update shortlink for this slug {slug}'


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'message': 'Resource Not Found ' + request.url,
        'status': 404
    }
    response = jsonify(message)
    response.status_code = 404
    return response    

@app.errorhandler(500)
def not_found(error=None):
    message = {
        'message': 'Internal Server Error ' + request.url,
        'status': 500
    }
    response = jsonify(message)
    response.status_code = 500
    return response    
