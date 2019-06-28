import pyowm

owm = pyowm.OWM('acc29a593594a342c670e4255fff5cdc')

place = input("Какой город?")

observation = owm.weather_at_place(place)
w = observation.get_weather()

print(w)                      