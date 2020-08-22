# routeviews_BGP_V2.0
Backup of the routeviews scripts and utilities

### Aim
Automation to download desired datasets from a particular range of dates, from [routeviews](http://archive.routeviews.org/)<br>
Then sort them according to the given set of IPs or AS

#### Task
1. Sort the required IP from Indian telecom dataset<br>
2. Verify them using sort_ip.py<br>
3. Run routeview on selected dates<br>
4. Make the required graph<br>
<br>

#### To do
UPDATE output folder \[Done]<br>
Script for graph<br>
Release V3.0<br>
Improve the flow

#### Still in testing...
##### Tree

┌─[michael@VSauce]─[routeviews_BGP_V2.0]<br>
└──╼ $tree<br>
.<br>
├── Datasets<br>
│   ├── master.sh<br>
│   ├── nohup.out<br>
│   ├── readme.MD<br>
│   ├── scrap_routeviews.py<br>
│   ├── search_routeviews.sh<br>
│   ├── verified_IP_UP<br>
│   └── zebra-dump-parser<br>
│       ├── aggregate-by-asn.pl<br>
│       ├── aslookup.pl<br>
│       ├── drop-stats<br>
│       │   ├── doit<br>
│       │   ├── drop-stats<br>
│       │   └── info.txt<br>
│       ├── get-asn-names.pl<br>
│       ├── README<br>
│       ├── zebra.conf<br>
│       └── zebra-dump-parser.pl<br>
├── IPs<br>
│   ├── AIRTEL_IPs_INDIA_AS24560<br>
│   ├── AIRTEL_IPs_INDIA_AS45609<br>
│   ├── AIRTEL_IPs_INDIA_AS9498<br>
│   ├── IDEA_IPs_INDIA_AS45271<br>
│   ├── JIO_IPs_INDIA_AS55836<br>
│   ├── README.md<br>
│   ├── scrap_IP_info.py<br>
│   ├── sort_IP.py<br>
│   ├── TATA_IPs_INDIA_AS4755<br>
│   ├── verified_IP_UP<br>
│   ├── VODAFONE_IPs_INDIA_AS38266<br>
│   └── VODA-IDEA_IPs_INDIA_AS55410<br>
├── LICENSE<br>
├── Output<br>
│   ├── GRAPHS<br>
│   │   ├── graph.py<br>
│   │   ├── nohup.out<br>
│   │   ├── non-overlap-graphs<br>
│   │   │   ├── non-overlap-graph_10.png<br>
│   │   │   ├── non-overlap-graph_11.png<br>
│   │   │   ├── non-overlap-graph_12.png<br>
│   │   │   ├── non-overlap-graph_13.png<br>
│   │   │   ├── non-overlap-graph_14.png<br>
│   │   │   ├── non-overlap-graph_15.png<br>
│   │   │   ├── non-overlap-graph_16.png<br>
│   │   │   ├── non-overlap-graph_17.png<br>
│   │   │   ├── non-overlap-graph_18.png<br>
│   │   │   ├── non-overlap-graph_19.png<br>
│   │   │   ├── non-overlap-graph_1.png<br>
│   │   │   ├── non-overlap-graph_20.png<br>
│   │   │   ├── non-overlap-graph_21.png<br>
│   │   │   ├── non-overlap-graph_22.png<br>
│   │   │   ├── non-overlap-graph_23.png<br>
│   │   │   ├── non-overlap-graph_24.png<br>
│   │   │   ├── non-overlap-graph_25.png<br>
│   │   │   ├── non-overlap-graph_26.png<br>
│   │   │   ├── non-overlap-graph_27.png<br>
│   │   │   ├── non-overlap-graph_28.png<br>
│   │   │   ├── non-overlap-graph_29.png<br>
│   │   │   ├── non-overlap-graph_2.png<br>
│   │   │   ├── non-overlap-graph_30.png<br>
│   │   │   ├── non-overlap-graph_31.png<br>
│   │   │   ├── non-overlap-graph_3.png<br>
│   │   │   ├── non-overlap-graph_4.png<br>
│   │   │   ├── non-overlap-graph_5.png<br>
│   │   │   ├── non-overlap-graph_6.png<br>
│   │   │   ├── non-overlap-graph_7.png<br>
│   │   │   ├── non-overlap-graph_8.png<br>
│   │   │   └── non-overlap-graph_9.png<br>
│   │   └── overlap-graphs<br>
│   │       ├── overlap-graph_10.png<br>
│   │       ├── overlap-graph_11.png<br>
│   │       ├── overlap-graph_12.png<br>
│   │       ├── overlap-graph_13.png<br>
│   │       ├── overlap-graph_14.png<br>
│   │       ├── overlap-graph_15.png<br>
│   │       ├── overlap-graph_16.png<br>
│   │       ├── overlap-graph_17.png<br>
│   │       ├── overlap-graph_18.png<br>
│   │       ├── overlap-graph_19.png<br>
│   │       ├── overlap-graph_1.png<br>
│   │       ├── overlap-graph_20.png<br>
│   │       ├── overlap-graph_21.png<br>
│   │       ├── overlap-graph_22.png<br>
│   │       ├── overlap-graph_23.png<br>
│   │       ├── overlap-graph_24.png<br>
│   │       ├── overlap-graph_25.png<br>
│   │       ├── overlap-graph_26.png<br>
│   │       ├── overlap-graph_27.png<br>
│   │       ├── overlap-graph_28.png<br>
│   │       ├── overlap-graph_29.png<br>
│   │       ├── overlap-graph_2.png<br>
│   │       ├── overlap-graph_30.png<br>
│   │       ├── overlap-graph_31.png<br>
│   │       ├── overlap-graph_3.png<br>
│   │       ├── overlap-graph_4.png<br>
│   │       ├── overlap-graph_5.png<br>
│   │       ├── overlap-graph_6.png<br>
│   │       ├── overlap-graph_7.png<br>
│   │       ├── overlap-graph_8.png<br>
│   │       └── overlap-graph_9.png<br>
│   ├── randomIP_1.png<br>
│   ├── randomIP_2.png<br>
│   ├── randomIP_3.png<br>
│   ├── randomIP_4.pdf<br>
│   └── results.csv<br>
└── README.md<br>
<br>
8 directories, 98 files<br>

