import requests

class TargetSite:
   def __init__(self, url):
    self.url = url

   @property
   def url_bilgisi(self):
    return self.url
   
class RequestService:
    def __init__(self, urller):
      self.urller = urller

    def bilgileri_goster(self):
      for s in self.urller:
        response = requests.get(s.url)
        print(response)

url_1 = TargetSite("https://udemy.com")
url_2 = TargetSite("https://facebook.com")
url_3 = TargetSite("https://w3schools.com")

urller = [url_1, url_2, url_3]
istek_at = RequestService(urller)
istek_at.bilgileri_goster()