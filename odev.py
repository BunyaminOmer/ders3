import requests

class Il:
    url = "https://api.weatherapi.com/v1/forecast.json?"
    key = "b41d9679c49249c8806123829230110"

    def get_weather_il(self, il, day):
        u = f"{self.url}key={self.key}&q={il}&days={day}&lang=tr"
        a = requests.get(u)
        return a.json()

il = Il()
print(il.get_weather_il("Bursa",1))

class Ilce:
    url = "https://api.weatherapi.com/v1/forecast.json?"
    key = "b41d9679c49249c8806123829230110"

    def get_weather_ilce(self, ilce, day):
        ur = f"{self.url}key={self.key}&q={ilce}&days={day}&lang=tr"
        b = requests.get(ur)
        return b.json()


    def parse_data(self):
      ilce_data = self.get_weather_ilce("Rize", 1)
      sicaklik = ilce_data["location"]["lat"]
      lo = ilce_data["location"]["lon"]
      print(sicaklik)
      print(lo)

ilce = Ilce()
print(ilce.get_weather_ilce("Ergani",1))
print(ilce.parse_data())