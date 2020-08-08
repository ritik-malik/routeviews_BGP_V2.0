# use opvn to bypass ipinfo.exceptions.RequestQuotaExceededError

import ipinfo
access_token = '7338dsa1e6a21'
handler = ipinfo.getHandler(access_token)
handler = ipinfo.getHandler(request_options={'timeout': 100})

IP = [
"118.185.237",
"118.185.239",
"118.185.46",
"118.185.88",
"118.185.93",
"118.185.95",
"122.15.128",
"122.15.13",
"122.15.133",
"122.15.134",
"122.15.135",
"122.15.138",
"122.15.143",
"122.15.225",
"122.15.23",
"122.15.31",
"122.15.36",
"122.15.40",
"122.15.93",
"123.63.100",
"123.63.106",
"123.63.160",
"123.63.162",
"123.63.191",
"123.63.193",
"123.63.3",
"123.63.5",
"123.63.78",
"123.63.90",
"123.63.91",
"182.19.4",
"182.19.73",
"182.19.85",
"182.19.90",
"182.19.91",
"182.19.94",
"42.104.110"]

f1 = open("verified_IP_UP","a")

for i in IP:
    a = handler.getDetails(i+'.1').region
    b = handler.getDetails(i+'.10').region
    c = handler.getDetails(i+'.90').region
    d = handler.getDetails(i+'.120').region
    e = handler.getDetails(i+'.150').region
    f = handler.getDetails(i+'.200').region
    g = handler.getDetails(i+'.230').region
    
    print(a,b,c,d,e,f,g,i)
    
    if(a == b == c == d == e == e == f == g == 'Uttar Pradesh'):
        f1.write(i)
        f1.write("\n")
        print('yes')

f1.close()


