from flask import jsonify, abort
import uuid

from app.models import ShortLink


ShortLink = ShortLink()

def generate_slug():
  return uuid.uuid4().hex  

def get_all_links():
  return jsonify(ShortLink.fetch_all()) 

def get_link(slug):
  link = ShortLink.fetch_one(slug)
  if not link:
    abort(404)

  return jsonify(link)

def create_link(request):
  if 'slug' in request and request['slug'] != "":
    slug = request['slug']

    if ShortLink.fetch_one(slug) :
      message = {
        "status": "failed",
        "message": f"Duplicate Entry, Slug [{slug}] already exists"
      }
      response = jsonify(message)
      response.status_code = 400
      return response
  else:
    slug = generate_slug()    

  new_link = {
    "slug":slug,
    "android":{
      "primary": request['android']['primary'],
      "fallback": request['android']['fallback'],
    },
    "ios":{
      "primary": request['ios']['primary'],
      "fallback": request['ios']['fallback'],
    },
    "web":request['web']
  } 
  ShortLink.insert(new_link) 

  message = {
    "status": "successful",
    "slug": slug,
    "message": "created successfully"
  }
  reponse = jsonify(message), 201

  return reponse

def update_link(slug, request):
  link = ShortLink.fetch_one(slug, show_id=True)

  if not link:
    abort(404)

  # Check Key Values exist to update in db
  if 'android' in request:
    if 'primary' in request['android']:
      link['android']['primary'] = request['android']['primary']
    if 'fallback' in request['android']:
      link['android']['fallback'] = request['android']['fallback']

  if 'ios' in request:
    if 'primary' in request['ios']:
      link['ios']['primary'] = request['ios']['primary']
    if 'fallback' in request['ios']:
      link['ios']['fallback'] = request['ios']['fallback']   

  if 'web' in request:
    link['web'] = request['web']

  # Update
  ShortLink.update(link)

  # Prepare Response
  message = {
    "status": "successful",
    "message": "updated successfully"
  }
  response = jsonify(message)
  response.status_code = 201

  return response


