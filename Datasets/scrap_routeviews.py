import os
import sys  

def get_data(x, URL, mirrors):
        
    for i in mirrors:
        
        # final URL = http://archive.routeviews.org/route-views.chicago/bgpdata/2020.02/RIBS/rib.20200201.1200.bz2
        temp='wget '+URL+i+'/bgpdata/'+x[:4]+'.'+x[4:6]+'/RIBS/rib.'+x+'.bz2'
        os.system(temp)

        print('decompressing the archive...')
        path='rib.'+x+'.bz2'                     # path = rib.20200215.1200.bz2
        temp = 'bzip2 -d '+path
        os.system(temp)             # decompress
        
        print('running zebra-dump parser...')
        temp = 'cat '+path[:-4]+' | '+'perl zebra-dump-parser/zebra-dump-parser.pl >'+path[:-4]+i+' 2>dump_errors'
        os.system(temp)
        temp = 'rm '+path[:-4]                                              # remove original file
        os.system(temp)


#######################################################################


URL = 'http://archive.routeviews.org/route-views.'
mirrors = ['chicago','chile',]#'eqix','flix','gorex','isc','kixp','jinx','linx','napafrica','nwax','phoix','telxatl','wide','sydney','saopaulo','sg','perth','sfmix','soxrs','mwix','rio','fortaleza','gixa']

# wget format = 'http://archive.routeviews.org/route-views.chicago/bgpdata/2020.02/RIBS/rib.20200201.1200.bz2'

print('MRT format RIBs and UPDATEs will be downloaded from -')
print('1  - Chicago     \t   2  - Chile      ')
print('3  - Equinix     \t   4  - FL-IX      ')
print('5  - Gorex       \t   6  - PAIX       ')
print('7  - KIXP        \t   8  - JINX       ')
print('9  - LINX        \t   10 - NAPAfrica ')
print('11 - NWAX        \t   12 - PhOpenIX  ')
print('13 - TELXATL     \t   14 - DIXIE     ')
print('15 - SYDNEY      \t   16 - SAOPAULO  ')
print('17 - SAOPAULO_2  \t   18 - SINGAPORE ')
print('19 - PERTH       \t   20 - SFMIX     ')
print('21 - Serbia      \t   22 - MWIX      ')
print('23 - RIO         \t   24 - FORTALEZA ')
print('25 - GIXA \n')

# x = input('Syntax -> "YYYYMMDD.time AS" : ').split()
# get_data(x, URL, mirrors)

# 20200220.1200 134023
x = sys.argv[1]


#x = '20180710.1000'
# x = '20180710.1200'
# x = '20180710.1400'
# x = '20180710.1600'

get_data(x, URL, mirrors)





