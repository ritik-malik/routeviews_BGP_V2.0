import ipinfo
import json
access_token = 'ad23hjwe4543543hb'
handler = ipinfo.getHandler(access_token)
handler = ipinfo.getHandler(request_options={'timeout': 20})


IPv4 = [
"103.224.191.0",
"103.29.44.0",
"123.63.57.0",
"123.63.59.0",
"123.63.60.0",
"123.63.6.0",
"123.63.61.0",
"123.63.63.0",
"42.104.88.0",
"42.104.89.0",
"42.104.91.0",
"42.104.93.0",
"42.104.94.0",
"42.104.96.0",
"42.104.96.0",
"42.104.97.0",
"42.104.99.0",
"43.245.88.0"]


for i in IPv4:
    ip_address = i
    details = handler.getDetails(ip_address)
    # pprint.pprint(details.all)
    data = details.all
    print(data,'\n')

    with open('VODA-IDEA_IPs_INDIA_AS55410', 'a') as f:
        print(data, file=f)
        print('\n', file=f)
        
