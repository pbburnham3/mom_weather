from flask_app import app
from flask import render_template, redirect, session, request
import requests

@app.route("/")
def index():
    r = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Seattle&appid=e2be89402f5f6c85a28246d6097c70b4')
    json_object_seattle = r.json()

    r2 = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Denver&appid=e2be89402f5f6c85a28246d6097c70b4')
    json_object_denver = r2.json()

    r3 = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Chatham&appid=e2be89402f5f6c85a28246d6097c70b4')
    json_object_chatham = r3.json()

    r4 = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Sisters&appid=e2be89402f5f6c85a28246d6097c70b4')
    json_object_sisters = r4.json()
    
    r5 = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Nanaimo&appid=e2be89402f5f6c85a28246d6097c70b4')
    json_object_nanaimo = r5.json()

    temp_k = float(json_object_seattle['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    temp_round = round(temp_f, 1)

    condition = json_object_seattle['weather'][0]['description']

    icon = json_object_seattle['weather'][0]['icon']

    wind_speed_raw = float(json_object_seattle['wind']['speed'])
    wind_speed_round = round(wind_speed_raw)

    humidity_raw = float(json_object_seattle['main']['humidity'])
    humidity_round = round(humidity_raw)

#=================================================================================================================

    temp_k_denver = float(json_object_denver['main']['temp'])
    temp_f_denver = (temp_k_denver - 273.15) * 1.8 + 32
    temp_round_denver = round(temp_f_denver, 1)

    condition_denver = json_object_denver['weather'][0]['description']
    
    icon_denver = json_object_denver['weather'][0]['icon']

    wind_speed_raw_denver = float(json_object_denver['wind']['speed'])
    wind_speed_round_denver = round(wind_speed_raw_denver)

    humidity_raw_denver = float(json_object_denver['main']['humidity'])
    humidity_round_denver = round(humidity_raw_denver)

#==================================================================================================================

    temp_k_chatham = float(json_object_chatham['main']['temp'])
    temp_f_chatham = (temp_k_chatham - 273.15) * 1.8 + 32
    temp_round_chatham = round(temp_f_chatham, 1)

    condition_chatham = json_object_chatham['weather'][0]['description']
    
    icon_chatham = json_object_chatham['weather'][0]['icon']

    wind_speed_raw_chatham = float(json_object_chatham['wind']['speed'])
    wind_speed_round_chatham = round(wind_speed_raw_chatham)

    humidity_raw_chatham = float(json_object_chatham['main']['humidity'])
    humidity_round_chatham = round(humidity_raw_chatham)

#==================================================================================================================

    temp_k_sisters = float(json_object_sisters['main']['temp'])
    temp_f_sisters = (temp_k_sisters - 273.15) * 1.8 + 32
    temp_round_sisters = round(temp_f_sisters, 1)

    condition_sisters = json_object_sisters['weather'][0]['description']
    
    icon_sisters = json_object_sisters['weather'][0]['icon']

    wind_speed_raw_sisters = float(json_object_sisters['wind']['speed'])
    wind_speed_round_sisters = round(wind_speed_raw_sisters)

    humidity_raw_sisters = float(json_object_sisters['main']['humidity'])
    humidity_round_sisters = round(humidity_raw_sisters)

#==================================================================================================================

    temp_k_nanaimo = float(json_object_nanaimo['main']['temp'])
    temp_f_nanaimo = (temp_k_nanaimo - 273.15) * 1.8 + 32
    temp_round_nanaimo = round(temp_f_nanaimo, 1)

    condition_nanaimo = json_object_nanaimo['weather'][0]['description']
    
    icon_nanaimo = json_object_nanaimo['weather'][0]['icon']

    wind_speed_raw_nanaimo = float(json_object_nanaimo['wind']['speed'])
    wind_speed_round_nanaimo = round(wind_speed_raw_nanaimo)

    humidity_raw_nanaimo = float(json_object_nanaimo['main']['humidity'])
    humidity_round_nanaimo = round(humidity_raw_nanaimo)

#==================================================================================================================
    
    return render_template("index.html", temp=temp_round, wind_speed = wind_speed_round, humidity = humidity_round, temp_denver = temp_round_denver, wind_speed_denver = wind_speed_round_denver, humidity_denver = humidity_round_denver, condition = condition, condition_denver = condition_denver, icon = icon, icon_denver = icon_denver, temp_chatham = temp_round_chatham, condition_chatham = condition_chatham, icon_chatham = icon_chatham, wind_speed_chatham = wind_speed_round_chatham, humidity_chatham = humidity_round_chatham, temp_sisters = temp_round_sisters, condition_sisters = condition_sisters, icon_sisters = icon_sisters, wind_speed_sisters = wind_speed_round_sisters, humidity_sisters = humidity_round_sisters, temp_nanaimo = temp_round_nanaimo, condition_nanaimo = condition_nanaimo, icon_nanaimo = icon_nanaimo, wind_speed_nanaimo = wind_speed_round_nanaimo, humidity_nanaimo = humidity_round_nanaimo)