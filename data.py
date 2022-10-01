##############################################################
# Imports
##############################################################

import csv
import requests
# from main import *

##############################################################
# Main
##############################################################

url = 'https://raw.githubusercontent.com/xivapi/ffxiv-datamining/master/csv/World.csv'

id = 8 #Crystal Datacenter

servers = {
    "id": [],
    "internalName": [],
    "name": [],
    "region": [],
    "userType": [],
    "dataCenter": [],
    "isPublic": []
}

def datacenter():
    print("DCID: " + str(id))
    # fetch file
    response = requests.get(url, allow_redirects=True)
    if response.status_code == 200:
        with requests.Session() as s:
            download = s.get(url)
            decoded_content = download.content.decode('utf-8')
            cr = csv.reader(decoded_content.splitlines(), delimiter=',')
            full_list = list(cr)
            col = full_list[1].index('DataCenter')
            # filter results for requested datacenter
            for row in full_list:
                if row[col] == str(id):
                    # print(row)
                    servers["id"].append(row[0])
                    servers["internalName"].append(row[1])
                    servers["name"].append(row[2])
                    servers["region"].append(row[3])
                    servers["userType"].append(row[4])
                    servers["dataCenter"].append(row[5])
                    servers["isPublic"].append(row[6])
    else:
        print("failed")
        # return "failed"
    print(servers)

datacenter()