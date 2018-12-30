from flask import Flask, render_template, request
from flask import jsonify
import requests
import json
app = Flask(__name__)

@app.route('/',methods = ['POST', 'GET'])
def index_page():
	if request.method == 'POST':
		search = request.get_json()
		response = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c&q=" + search["text"])
		r = response.json()
		cp_info = r['result']['records']

		carpark_api = requests.get("https://api.data.gov.sg/v1/transport/carpark-availability")
		carpark_json = carpark_api.json()
		cp_data = carpark_json['items'][0]["carpark_data"]

		return jsonify(cp_info, cp_data)
	return render_template("index.html")
		
if __name__ == '__main__':
    app.run(debug=True)