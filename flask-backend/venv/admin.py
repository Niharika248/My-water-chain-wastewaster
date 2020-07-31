from flask import Flask,jsonify,request
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash,check_password_hash
import json
mongoURI="mongodb+srv://admin-user:ogimljVnqPClQI5i@cluster0-8qxz0.mongodb.net/mywatertech?retryWrites=true&w=majority"
with open(r'secretkey.json') as f:
  data = json.load(f)
app = Flask(__name__)
app.secret_key = data["key"]
app.config['MONGO_URI'] = mongoURI
mongo = PyMongo(app)



@app.route('/add',methods=['POST'])
def add_user():
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']
    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)
        ids = mongo.db.industrydetails.insert({"name":_name,
                                               "email":_email,
                                               "pwd":_hashed_password})
        res = jsonify("User added successfully")
        res.status_code = 200
        return res
    else:
        return not_found()
@app.route('/users')
def users():
    users = mongo.db.industrydetails.find()
    res = dumps(users)
    return(res)
@app.route('/users/<ids>')
def user(ids):
    print(ids)
    user = mongo.db.industrydetails.find_one({'_id':ObjectId(ids)})
    res = dumps(user)
    return(res)
@app.route('/delete/<ids>',methods=['DELETE'])
def delete_user(ids):
    mongo.db.industrydetails.delete_one({"_id":ObjectId(ids)})
    res = jsonify("Delete Success!")
    res.status_code = 200
    return(res)
@app.route('/update/<ids>',methods = ['PUT'])
def update_user(ids):
    _id = ids
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']
    if _name and _email and _password and _id and request.method == 'PUT':
        _hashed_password = generate_password_hash(_password)
        mongo.db.industrydetails.update_one({'_id':ObjectId(_id['$oid']) if '$oid' in _id else ObjectId(_id)},{'$set':{'name':_name,
                                                                                                             'email':_email,'pwd':_hashed_password}})
        res = jsonify("User updated successfully")
        res.status_code = 200
        return res
    else:
        return not_found()
    
@app.errorhandler(404)
def not_found(error=None):
    message={
        'status':404,
        'message':'Not Found'+request.url
        }
    res = jsonify(message)
    res.status_code = 404
    return res

if __name__=="__main__":
    app.run(debug=True)

