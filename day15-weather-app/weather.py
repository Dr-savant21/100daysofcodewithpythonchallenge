# import requests
# import json
# from dotenv import load_dotenv
# import dotenv
# import os

# load_dotenv()
# api_key = os.getenv('API_KEY')

# try:
#     result = dotenv.load_dotenv()
#     print("Dotenv file loaded successfully.")
# except Exception as e:
#     print("Error loading dotenv file:", str(e))
#     # Optionally, you can raise the exception to stop the program execution
#     # raise e

# # Continue with the rest of your code
# print(os.environ)


# # def get_lat_lon(city_name, state_code, country_code, API_KEY):
# #     url = f'http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&key={API_KEY}'
# #     headers = {'Content-Type': 'application/json'}
# #     resp = requests.get(url, headers=headers)
# #     print(resp.status_code)
# #     print(resp)

# # get_lat_lon('Toronto', 'ON', 'Canada', api_key)
# # https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}

# def get_lat_lon(lat, lon, API_key):
#     url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
#     headers = {'Content-Type': 'application/json'}
#     resp = requests.get(url, headers=headers)
#     print(resp.status_code)
#     print(resp)

# get_lat_lon('6.6342', '5.9304', api_key)
