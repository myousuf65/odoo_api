import pandas as pd
import xmlrpc.client
import base64
import time

API_KEY = ''
URL = '' # database url
USERNAME = '' # email
PASSWORD =  '' 
DB_NAME = ''


# authentication
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
print(common.version())
uid = common.authenticate(DB_NAME, USERNAME, PASSWORD, {})
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))

if uid:
    print("authentication successful")
else:
    print("failed to authenticate")


#read data from a file using pandas
df = pd.read_excel('', sheet_name='')

# convery data frame to an array
arr = df['Account'].tolist()
print(arr)


# update the person in charge and salesperson to be the value you want
for item in arr: 
    query = models.execute_kw(DB_NAME, uid , PASSWORD,  'res.partner', 'search', [[['display_name', '=', item ]]])

    retrievedRecord = models.execute_kw(DB_NAME, uid , PASSWORD,  'res.partner', 'read', [query], {'fields' : ['x_salesperson', 'x_personincharge']} )

    for record in retrievedRecord:
        if record.get('x_salesperson') != 'Gorden Wong' or record.get('x_personincharge') != 'Gorden Wong':

            update = models.execute_kw(DB_NAME, uid, PASSWORD, 'res.partner', 'write', [[record['id']], {'x_salesperson': 'Jeo Chan' , 'x_personincharge' : 'Joe Chan'}])
            
            if update:
                print(item, "Record updated for 'x_salesperson'")
            else:
                print(item , "Failed to update x_salesperson")
        else:
            print(item, "Didnt do anything")
         
