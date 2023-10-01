import requests

class TargetSite:
   def __init__(self, url):
    self.url = url

   def bilgileri_goster(self):
    response = requests.get(self.url)
    print(response)

url_1 = TargetSite("https://udemy.com")
url_2 = TargetSite("https://facebook.com")
url_3 = TargetSite("https://w3schools.com")

url_1.bilgileri_goster()
url_2.bilgileri_goster()
url_3.bilgileri_goster()