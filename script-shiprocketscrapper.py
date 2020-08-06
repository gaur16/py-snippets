import pandas as pd
import requests
URL = "https://apiv2.shiprocket.in/v1/external/orders"
class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r
order_id = '1016769'
PARAMS = {"filter_by":"channel_order_id","filter":order_id}
head = {"Authorization": "Bearer <token-here>"}
r = requests.get(url = URL, params = PARAMS, headers=head)
print(r)
x=r.json()
y = x['data'][0]['status']
print (y)
px_h = pd.read_csv("h_list.csv")
h_orders = px_h['OrderId'].tolist()
lx=[]
count=0
for each in h_orders:
    PARAMS['filter']=each
    r = requests.get(url = URL, params = PARAMS, headers=head)
    try:
	x=r.json()
        y=x['data'][0]['status']
        temp=[each,y]
        lx.append(temp)
        count=count+1
        print(count)
    except:
        print("error: ")

