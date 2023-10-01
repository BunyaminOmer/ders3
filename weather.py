import requests

# https://api.weatherapi.com/v1/forecast.json?key=bf62b422e0f74797a55193719232408&q=pazar,rize&days=7&lang=tr

class WeatherService:
   url = "https://api.weatherapi.com/v1/forecast.json?"
   key = "b41d9679c49249c8806123829230110"

   def get_weather(self , city, day):
      urll = f"{self.url}key={self.key}&q={city}&days={day}&lang=tr"
      a = requests.get(urll)
      return a.json()

   def veri(self):
      b = self.get_weather("Rize",1)
      sicaklik = b["location"]["lat"]
      lo = b["location"]["lon"]
      print(sicaklik)
      print(lo)

n = WeatherService()
n.get_weather("Rize",1)
n.veri()
# n.get_weather("Sincan", "Ankara",1)

# sehirler = ["Ankara","Bursa","İstanbul","Diyarbakır","İzmir",""]

# for s in sehirler:
#    n.get_weather(s, 1)