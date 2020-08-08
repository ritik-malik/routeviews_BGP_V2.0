### Datasets for major telecom providers in India
AIRTEL_IPs_INDIA_AS24560<br>
AIRTEL_IPs_INDIA_AS45609<br>
AIRTEL_IPs_INDIA_AS9498<br>
IDEA_IPs_INDIA_AS45271<br>
JIO_IPs_INDIA_AS55836<br>
TATA_IPs_INDIA_AS4755 <br>
VODA-IDEA_IPs_INDIA_AS55410<br>
VODAFONE_IPs_INDIA_AS38266<br>
Source - [IPinfo.io](https://ipinfo.io/)

### Created using scrap_IP_info.py
Uses [IPinfo API](https://github.com/ipinfo/python) to scrap the details<br>
PS : in case it gives error 429, use VPN for same access token, (preferrably [ovpn](https://openvpn.net/))

### Sorting the subnets
Sort the obtained subnets using sort_IP.py<br>
It confirms the details.region from the API on 7 different IPs from same subnet and saves it in a file<br>
<br>
verified_IP_UP is the output of the above process
