import requests, os, json, sys

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



def where_json(file_name):
    return os.path.exists(file_name)

def query_json():
    with open('data.json') as json_file:
        data = json.load(json_file)
        if data == None:
            print("\nData file is empty...\n")
        else:
            print("\nLoading data file...")
            #print(data)
            return data

def create_file_json():
    with open('data.json', 'w') as outfile:  
        json.dump({}, outfile)

def append_file_json(data_to_append,term):
    file_data = query_json()
    #print("\nTerm --> " + str(term) + "\n")
    #print("\nData to append--> " + str(data_to_append) + "\n")
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
        #print("File Found\n")
        return True
    else:
        #print("file not found\n")
        create_file_json()
        #print("File Created\n")
        return True


    
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

url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

headers = {
    'x-rapidapi-host': str(API_HOST),
    'x-rapidapi-key': str(API_KEY)
    }

if len(sys.argv) > 1:
    print(str(sys.argv))
    for x in range(len(sys.argv)):
        #print(" X = " + str(x) + " sys.argv = " + str(sys.argv[int(x)]) + "\n")
        if int(x) > 0:
            #print(x)


            querry_list = sys.argv[1:]
            print(querry_list)

            if verify_file() == True:
                data = query_json()
                for term in querry_list:
                    if str(term) in data:
                        print("\nItem found in file")

                        ### display info in json file
                        print("\nFinding - " + str(term) + " - in text.json file\n")

                        #print("Term - " + str(term) + " - data[term] - " + str(data[term]) + "\n")
                        for item in data[term]:
                            print("Definition found \n --->" + str(item) + "\n")
                        pass
                    else:
                        #add the item & definitions to json file
                        print("Term to be added --> " + str(term) + "\n")
                        results_from_query = Process_user_input_and_server_response(term)

                        #request data and append new info
                        append_file_json(results_from_query,term)
                        for item in results_from_query:
                            print("Definition found \n --->" + str(item) + "\n")
                        pass
else:
    #no cmd request
    input_term = input("What term do you want to look for? \nYou can make multiple requests by seperating your input with commas.\n")

    querry_list = input_term.split (",")

    if verify_file() == True:
        data = query_json()
        #print("\nThis is the data returned form .json file\n" + str(data))
        for term in querry_list:
            if str(term) in data:
                print("\nItem found in file")

                ### display info in json file
                print("\nFinding - " + str(term) + " - in text.json file\n")

                #print("Term - " + str(term) + " - data[term] - " + str(data[term]) + "\n")
                for item in data[term]:
                    print("Definition found \n --->" + str(item) + "\n")
                pass
            else:
                #add the item & definitions to json file
                print("Term to be added --> " + str(term) + "\n")
                results_from_query = Process_user_input_and_server_response(term)

                #request data and append new info
                append_file_json(results_from_query,term)
                for item in results_from_query:
                    print("Definition found \n --->" + str(item) + "\n")
                pass