from flask import jsonify, abort, redirect
import uuid

from app.models import ShortLink


ShortLink = ShortLink()

def generate_slug():
  return uuid.uuid4().hex  

def get_platform(user_agent):
  if "Android" in user_agent:
    return "android"

  if "Windows" in user_agent:
    return "web"

  if "Mac OS" in user_agent:
    return "ios"

  return None  

def get_platform_link(link, platform):

  if not platform or platform == 'web':
    return link['web']

  if link[platform]['primary']:
    return link[platform]['primary']

  if link[platform]['fallback']:
    return link[platform]['fallback']
  
def get_all_links():
  return jsonify(ShortLink.fetch_all()) 

def get_link(slug, request):
  link = ShortLink.fetch_one(slug)
  if not link:
    abort(404)
  
  platform = get_platform(request.headers.get('User-Agent'))
  location = get_platform_link(link, platform) 

  return redirect(location, 302)

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
    "web": check_key_exist('web', request),
    "android":{
      "primary":  check_2keys_exist('android', 'primary', request),
      "fallback": check_2keys_exist('android', 'fallback', request),
    },
    "ios":{
      "primary": check_2keys_exist('ios', 'primary', request),
      "fallback": check_2keys_exist('ios', 'fallback', request),
    }    
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


# Helpers
def check_key_exist(key, request):
  if key in request:
    return request[key]
  return      

def check_2keys_exist(key1, key2, request):
  if key1 in request:
    if key2 in request[key1]:
      return request[key1][key2]
  return    
