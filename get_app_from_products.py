import requests
import json
import csv
import os


productName = ""
BasicAuth = ""
organization = ""
apigeeDomain = ""
version = ""
output_csv_file = ""

getAppurl = "http://"+apigeeDomain+"/"+version+"/o/"+organization+"/apiproducts/"+productName+"?query=list&entity=apps"

headers = {
  'Authorization': 'Basic '+BasicAuth,
  'Content-Type': 'application/json'
}

def get_apps_under_api_products():
    response = requests.get(getAppurl, headers=headers).json()
 
    for i in response:
        url = 'http://'+apigeeDomain+'/'+version+'/o/'+organization+'/apps/'+i
        appDetails = requests.get(url, headers=headers).json()
    
        with open(output_csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([appDetails["name"] if appDetails["name"] else "-", appDetails["status"]])
    print("file is located in " + os.path.dirname(os.path.abspath(__file__))+"/"+output_csv_file)
        

if __name__ == "__main__":
    get_apps_under_api_products()