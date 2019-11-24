#
# import pyowm
#
# owm = pyowm.OWM('db7cff7b3e0764f72a48ef53be5f99a4')  # You MUST provide a valid API key
#
# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')
#
# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_coords(55.47,49.7)
# w = observation.get_location()
# print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>
#
# # Weather details
# print(w.get_name())  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
#
# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)