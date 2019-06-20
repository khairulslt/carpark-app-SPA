from flask import Flask, render_template, request
from flask import jsonify
import requests
import json
app = Flask(__name__)

@app.route('/',methods = ['GET'])
def index_page():
	return render_template("index.html")

@app.route('/carparks',methods = ['POST'])
def carparks():
	search = request.get_json()

	cp_service = new Carpark_service()
	cp_info1, cp_info2 = cp_service.search(search["text"])

	cp_numbers = fetch_cp_numbers_from(cp_info1, cp_info2)

	cp_avail = new Carpark_availability_service()
	cp_availability_data = cp_avail.search(cp_numbers)

	return jsonify(cp_info1, cp_info2, cp_availability_data)

if __name__ == '__main__':
    app.run(debug=True)

class Carpark_service
	def search(self, keyword):
		response = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=139a3035-e624-4f56-b63f-89ae28d4ae4c&q=" + search["text"])
		r = response.json()
		cp_info1 = r['result']['records']

		response = requests.get("https://data.gov.sg/api/action/datastore_search?resource_id=5a8f7572-0d46-4ce5-be71-a7081d2c42b0&q=" + search["text"])
		j = response.json()
		cp_info2 = j['result']['records']

		return cp_info1, cp_info2

class Carpark_availability_service
	def search(self, cp_numbers):
		all_cp_avail = self.__fetch_results()

		result = ... # from cp_data - for every carpark_number, extract the info for matching cp_numbers
		return result

	def __fetch_results(self)
		cache_for(30 seconds)
			carpark_api = requests.get("https://api.data.gov.sg/v1/transport/carpark-availability")
			carpark_json = carpark_api.json()
			return carpark_json['items'][0]["carpark_data"]