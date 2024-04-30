import xmlrpc.client
import base64

API_KEY = 'aa459463d1c6400ed7b7419647362dfcb2c6bfee'
URL = 'https://www.biomederp.com'
USERNAME = 'yousuf@biomed.com.hk'
PASSWORD =  'apple123@biomed'
DB_NAME = 'biomed-technology-holdings-limited1'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(URL))
print(common.version())

uid = common.authenticate(DB_NAME, USERNAME, PASSWORD, {})

if uid:
    print("authentication successful")
else:
    print("failed to authenticate")


models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(URL))


