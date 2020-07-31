from flask import Flask,jsonify,request
import datetime
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/register', methods=['POST'])
def postTest():
    datapacket = request.get_json()
    print(datapacket)
    #print(datapacket["Device_ID"])
    datadict={"abc":123,"def":345,"fgh":678}
    return datadict

if __name__=="__main__":
    app.run(debug=True)

#Interface this program with MongoDB
#
