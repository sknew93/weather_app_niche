import json
from flask import Flask, render_template, request, flash
import requests
import pdb

app = Flask(__name__)
app.secret_key = "manbearpig_MUDMAN888"

@app.route("/")
def index():
	flash("Give us your latitude's and longitude's!")
	return render_template("index.html")

@app.route("/greet", methods=['POST', 'GET'])
def greeter():
	temp_data = getAPIData(str(request.form['name_input']))
	flash(str(temp_data))
	return render_template("index.html")

def getAPIData(data):
	data = data.strip()
	# 38.2527 N, 85.7585 W 39.7456,-97.0892
	split1 = data.split(',')
	first_half_sign = split1[0].split(' ')[0]
	first_half = split1[0].split(' ')[1]
	second_half_sign = split1[1].strip().split(' ')[0]
	second_half = split1[1].strip().split(' ')[1]
	# https://api.weather.gov/points/39.7456,-97.0892
	html_part_one = ifPositiveOrNegative(first_half) + first_half_sign+','
	html_part_two = ifPositiveOrNegative(second_half) + second_half_sign
	final_link = html_part_one + html_part_two
	r1 = requests.get(f'https://api.weather.gov/points/{final_link}')
	# pdb.set_trace()
	reqData1 = r1.json()['properties']['forecast']
	r2 = requests.get(reqData1)
	reqData2 = r2.json()['properties']['periods']
	temp = ''
	for data in reqData2:
		if(data['name']=='Tonight'):
			temp = data['temperature']
			break
	if(temp < 68):
		return f"Gonna be a little chilly at {temp}'F. Take your coats !"
	elif(68 < temp < 82.4):
		return f"Woohoo, you're having a pleasant night at {temp}'F."
	else:
		return f"Uff! Looks like you have a hot night ahead of you at {temp}`F."

def ifPositiveOrNegative(letter):
	if(letter == 'N' or letter == 'E'):
		return ''
	else:
		return '-'