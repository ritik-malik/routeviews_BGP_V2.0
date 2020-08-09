import matplotlib.pyplot as plt 
import os

csv_file = 'nohup.out'

G_type = input("Make overlapping graph? y/n : ")

if G_type == 'n':
    os.system('mkdir non-overlap-graphs')
    temp = 'cp '+csv_file+' non-overlap-graphs'
    os.system(temp)
    os.chdir('non-overlap-graphs')
elif G_type == 'y':
    os.system('mkdir overlap-graphs')
    temp = 'cp '+csv_file+' overlap-graphs'
    os.system(temp)
    os.chdir('overlap-graphs')
else:
    print('wrong input!')
    exit(0)


with open(csv_file) as f:
    content = f.readlines()
content = [x.strip() for x in content]

os.remove(csv_file)

dates = [1 , 2 , 3 , 4,  5,  6,  7,  8,  9,  10 , 11,  12,  13,  14 , 15 , 16 , 17 , 18 , 19,  20,  21,  22,  23,  24,  25,  26,  27,  28,  29,  30]
count = 1

for i in content:
    temp = i.split(',')
    temp = list(map(int, temp))
    
    plt.plot(dates, temp)
    plt.xlabel('dates')
    plt.ylabel('frequency')
    
    head = 'Verified IP number - '+str(count)
    plt.title(head)
    
    
    if G_type == 'n':
        head = 'non-overlap-graph_'+str(count)+'.png'
        plt.savefig(head)
        plt.clf()
    else:
        head = 'overlap-graph_'+str(count)+'.png'
        plt.savefig(head)
    
    count+=1

    # plt.show()
