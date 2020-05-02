import requests, os

# Retrieve your API credentials from the .env file
if os.getenv("API_KEY") is None or os.getenv("API_KEY") == "":
    print("ERROR! Make sure you have created your .env file with your API credentials (look for the .evn.example as an example and replace it with your own API credentials that you got from RapidAPI)")
    exit(1)

# Get credentials from the .env file
API_HOST = os.getenv("API_HOST")
API_KEY = os.getenv("API_KEY")

# continue with your application here
#print(API_HOST)
#print(API_KEY)

input_term = input("What term do you want to look for? You can make multiple requests by seperating your input with commas.")

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "e3115142camsh5f670bda2cc09cdp13d620jsn1218432bf1ec"
    }

querystring = {"term":input_term}
#print(querystring)

response = requests.request("GET", url, headers=headers, params=querystring)

body = response.json()
dict_layer1 = body["list"]
for items in dict_layer1:
    print(items["definition"])
#print(dict_layer1)