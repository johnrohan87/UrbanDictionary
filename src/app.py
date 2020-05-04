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

def where_json(file_name):
    return os.path.exists(file_name)

def query_json():
    with open('data.json') as json_file:
        data = json.load(json_file)
        if data == None:
            print("\nData file is empty...\n")
        else:
            print("\nLoading data file...\n")
            print(data)
            return data

def create_file_json():
    with open('data.json', 'w') as outfile:  
        json.dump({}, outfile)

def append_file_json(data_to_append,term):
    file_data = query_json()
    print("\nTerm --> " + str(term) + "\n")
    print("\nData to append--> " + str(data_to_append) + "\n")
    tmpDict = {}
    tmpList = []
    for item in range(len(data_to_append)):
        tmpList.append(data_to_append[item])
    tmpDict[term] = tmpList
    tmpDict.update(file_data)
    with open('data.json', 'w') as outfile:  
        json.dump(tmpDict, outfile)
    

def verify_file():
    if where_json('data.json'):
        print("File Found\n")
        return True
    else:
        print("file not found\n")
        create_file_json()
        print("File Created\n")
        return True

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "e3115142camsh5f670bda2cc09cdp13d620jsn1218432bf1ec"
    }

querry_list = input_term.split (",")
#print(querry_list)
#print(len(querry_list))

# def process_and_display_data(informatoion):
#     body = response.json()
#     dict_layer1 = body["list"]
#     return dict_layer1
    
def Process_user_input_and_server_response(user_input_term):
#    for items in range(len(querry_list)):
        print("Requesting --> " + str(user_input_term))
        query_dict = {}
        query_dict["term"] = str(user_input_term)
        response = None
        response = requests.request("GET", url, headers=headers, params=query_dict)
        body = response.json()
        request_definition = body["list"]
        return_List =[]
        for items in request_definition:
            return_List.append(items["definition"])
        return return_List


if verify_file() == True:
    data = query_json()
    print("\nThis is the data returned form .json file\n" + str(data))
    for term in querry_list:
        if str(term) in data:
            print("\nItem found in file\n")
            #print(str(data[str(term)]))
            # results_from_query = Process_user_input_and_server_response(term)
            # for x in range(len(results_from_query)):
            #     print("\nDefinition -->" + str(results_from_query[x]) + "\n")

            ### display info in json file
            print("\nFinding - " + str(term) + " - in text.json file\n")
            print("Term - " + str(term) + " - data[term] - " + str(data[term]))
        else:
            #add the item & definitions to json file
            print("Term to be added --> " + str(term))
            results_from_query = Process_user_input_and_server_response(term)
            
            #temp_dict = {str(term):str(list(results_from_query))}

            #request data and append new info
            append_file_json(results_from_query,term)

            pass

# if len(querry_list) <= 1:
#     if verify_file() == True:
        
#         #check here if word is in the data file
#         data = query_json()
#         print("\nThis is the data returned form .json file\n" + str(data))

#         #check if term is in text.json file
#         if str(input_term) in data:
#             print("\nItem found in file\n")
#             print(str(data[str(input_term)]))

#             query_dict = {"term":input_term}
#             response = requests.request("GET", url, headers=headers, params=query_dict)
#             request_definition = process_and_display_data(response)
#             #print(list(request_definition))
#             for items in request_definition:
#                 print(items["definition"] + "\n")
#         else:
#             print("\nItem NOT found in file\n")

# else:
#     if verify_file() == True:
#         for x in range(len(querry_list)):
#             #print(x)
#             #print(querry_list[x])
#             query_dict = {}
#             query_dict["term"] = querry_list[x]
#             response = None
#             response = requests.request("GET", url, headers=headers, params=query_dict)
#             request_definition = process_and_display_data(response)
#             for items in request_definition:
#                 print(items["definition"] + "\n")