from app import db

class ShortLink:

  def __init__(self):
    # Collection - test
    self.db = db.shortlinks

  def insert(self, shortlink):
    self.db.insert_one(shortlink)
    
  def fetch_one(self, slug, show_id=False):
    if show_id:
      return self.db.find_one({'slug': slug})    
    return self.db.find_one({'slug': slug}, {'_id': False})  

  def fetch_all(self):    
    return [dict(link) for link in self.db.find({}, {'_id': False})]    
      
  def update(self, link):
    self.db.update_one({"slug": link['slug']}, {"$set": link})
