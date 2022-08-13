from app import app

@app.route('/')
def index():
    return 'Hi Mom'

@app.route('/shortlinks', methods=['GET'])
def shortLinks():
    return 'shortlinks'

@app.route('/createshortlink', methods=['POST'])
def createShortLink():
    return 'createshortlink'

@app.route('/shortlinks/<slug>', methods=['PUT'])
def updateShortLink(slug):
    return f'updateShortLink {slug}'
