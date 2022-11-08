from flask import Flask, render_template
import requests
import json
from flask_googlemaps import GoogleMaps
app = Flask(__name__)
app.config['GOOGLEMAPS_KEY'] = 'AIzaSyAC8upaQp2nxzBhCCa1QkqoussL9z03hfA'
GoogleMaps(app)
@app.route('/map',methods=["GET"])
def map():
    req = requests.get("https://api.npoint.io/f26432e9e880999eeb1b")
    data = json.loads(req.content)
    feature=data['features']
    k=data.keys()
    print (k)
    print(type(feature))


    return render_template('maps.html',data=feature)
if __name__=='__main__':
    app.run(debug=True)
