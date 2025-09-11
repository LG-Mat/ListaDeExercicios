import requests
#response = requests.get("https://randomuser.me/api/" )
#print(response.text)

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Replace DEMO_KEY below with your own key if you generated one.
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)
photo = response.json()["photos"]
photo = photo[4]["camera"]["name"]
print(type(photo))
photo = response.json()["photos"]
photo = photo[4]["img_src"]
print(type(photo))

# Resposta: ambas são do tipo string, a primeira retorna 'RHAZ' e a segunda o link para a acessar a imagem