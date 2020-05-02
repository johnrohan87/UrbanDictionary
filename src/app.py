import requests, os, json

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

input_term = input("What term do you want to look for? \nYou can make multiple requests by seperating your input with commas.\n")

with open('data.txt') as json_file:
    data = json.load(json_file)
if data == None:
    print("\nData file is empty...\n")
else:
    print("\nLoading data file...\n")

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "e3115142camsh5f670bda2cc09cdp13d620jsn1218432bf1ec"
    }

querry_list = input_term.split (",")
#print(querry_list)
#print(len(querry_list))

def process_and_display_data(informatoion):
    body = response.json()
    dict_layer1 = body["list"]
    for items in dict_layer1:
        print(items["definition"])

if len(querry_list) <= 1:
    query_dict = {"term":input_term}
    response = requests.request("GET", url, headers=headers, params=query_dict)
    process_and_display_data(response)
else:
    for x in range(len(querry_list)):
        #print(x)
        #print(querry_list[x])
        query_dict = {}
        query_dict["term"] = querry_list[x]
        response = None
        response = requests.request("GET", url, headers=headers, params=query_dict)
        process_and_display_data(response)