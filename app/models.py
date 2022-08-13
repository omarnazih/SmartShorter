from flask import Flask, jsonify, request, redirect
from datetime import datetime 
from random import choice
from app import db
import string
import uuid

class Url:
  
  def insert(self):

    if not request.is_json:
      return jsonify({"msg":"Missing JSON in request"}), 400

    req = request.get_json()
    url = {
      "_id": uuid.uuid4().hex,
      "slug": uuid.uuid4().hex,
      "primary": req['primary'],
      "fallback": req['fallback'],
      "time": datetime.now()
    }

    new_url = request.url.replace('createshortlink', 'shortlinks')
    shortend_url = f"{new_url}/{url['slug']}"

    if db.test.insert_one(url):      
      return jsonify(shortend_url), 200
    
    return jsonify({"msg": "Insertion Failed"}), 400       

  def retreive_all(self):
    
    shortlinks = db.test.find({})

    # If empty list return
    if not shortlinks:
        return jsonify({"msg":"No Data found"}), 400    
    
    shortlinks_list = []
    for entry in shortlinks:             
      row = {
          'slug': entry['slug'],
      }
      shortlinks_list.append(row)
        
    return jsonify(data=shortlinks_list), 200        

  def get(self, slug):

    response = db.test.find_one_or_404({"slug": slug})    

    return redirect(response['primary'], code=302)

  def update(self, slug):

    if db.test.find_one_or_404({"slug": slug}):
      return "Found"
    
    return redirect(response['primary'], code=302)    