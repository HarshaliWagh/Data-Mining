def candidate(freqitem, count):
    combination = []
    item = []
    for a in freqitem.keys():
        item.append(a)
    for i in range(0, len(freqitem)- 1, 1):
        for j in range(i+1, len(freqitem)):
            comb = []
            comb.append(item[i])
            comb.append(item[j])
            combination.append(comb)
    #print("Combinationsss")
    #print(combination)
    candi = []
    for i in range(len(combination)):
        p = []
        a = combination[i]
        b = ','.join(a)
        cand = b.split(',')
        for a in range(0, len(cand)):
            p.append(cand[a])
        candi.append(p)
    #print("candiiii")
    duplicatecand = []
    prunedcandi = []
    dell = []
    for i in range(0, len(candi)):
        p = set(candi[i])
        q = list(p)
        duplicatecand.append(q)
        if (len(duplicatecand[i]) == count):
           prunedcandi.append(duplicatecand[i])
        else:
            dell.append(duplicatecand[i])
    #print("extra freqitemset")
    #print(dell)
    #print("removeeeed dupiii")
    #print(prunedcandi)
    return(prunedcandi)

def support(can, data):
    supo = []
    w = []
    n = []
    for p in range(0, len(can)):
        a = set(can[p])
        z = set(a)
        w.append(z)
    #print(w)
    for q in range(0, len(data)):
        b = set(data[q])
        o = set(b)
        n.append(o)
    for i in range(0, len(can)):
        counter = 0
        j=0
        for j in range(0, len(data)):
            if((w[i]).issubset(n[j])):
                counter = counter + 1
            j = j + 1
        supo.append(counter)
    #print("supo countttt")
    #print(supo)
    return(supo)

def freqitemset(candidateg, sup, minsup):
    freq = {}
    for i in range(0, len(candidateg)):       
        a = candidateg[i]
        b = ','.join(a)
        if(sup[i] >= minsup):
            freq[b] = sup[i]
    #print("frwqqqqqqq")
    #print(freq)
    return(freq)

def freqlist(freqitemsetg, count):
    n = count - 1
    freqnew = []
    for x in freqitemsetg:
        a = x.split(',')
        freqnew.append(a)
    #print(freqnew)
    while(n !=0):
        for i in range(0, len(freqnew)):
            glue = []
            aso = association(freqnew[i], glue, n)
            print(aso)
            for j in range(0, len(aso)):
                dumpy = []
                for k in range(0, len(freqnew[i])):
                    if (freqnew[j][k] not in aso[j]):
                        dumpy.append(freqnew[i][k])
                        print(str(dumpy)+"--------->"+str(aso[j]))         
        n = n - 1
    '''apriori = []
    supportx = []
    supportxy = []
    for trans in dataset:
        if set(dumpy[0]).issubset(set(trans)):
            supportx = supportx + 1
        if set(dumpy[0] + dumpy[i]).issubset(set(trans)):
            supportxy - supportxy + 1
        confidence = (supportxy / supportx) * 100
        if confidence >= minconf:
            print(confidence)'''

def association(freq, glue, n):
    if len(freq) == n:
        if glue.count(freq) == 0:
            glue.append(freq)
            #print(glue)
        return glue
    elif len(freq)!= n:
        for i in range(0,len(freq)):
            nextfreq = freq[i+1:] + freq[:i]
            glue = association(nextfreq, glue, n)
            #print(glue)
        return glue
         

# Take values from user - Main
dataset = []
print("Select the dataset:")
print("1 grocery")
print("2 clothing")
print("3 electronics")
print("4 utensils")
print("5 furniture")
finput = input("Enter number ")
minsup = int(input('Enter minimum Support: '))
minconf = int(input('Enter minimum Confidence: '))
fopen = ""

if finput == '1':
    fopen = "db1.txt"
elif finput == '2':
    fopen = "db2.txt"
elif finput == '3':
    fopen = "db3.txt"
elif finput == '4':
    fopen = "db4.txt"
else:
    fopen = "db5.txt"

#Reading the data

fp = open(fopen, 'r')
while True:
    line = fp.readline()
    if not line :
        break;
    line = line.rstrip()
    dataset.append(line.split(", "))
#print(dataset)

#To create C1

itemdict = {}
for data in dataset:
    for item in data:
        if item in itemdict:
            itemdict[item] = itemdict[item] + 1
        else:
            itemdict[item] = 1
#print(" Its C1")
#print(itemdict)

#To create L1
freq = {}
for i in range(0, len(itemdict)):       
    for item, count in itemdict.items():
        if(count >= minsup):
            freq[item] = count
#print(" Its L1")
#print(freq)

# To create C2, calculate support, L2
count = 2
candidateg = candidate(freq, count)
sup = support(candidateg, dataset)
freqitemsetg = freqitemset(candidateg, sup, minsup)
freqitemlist = freqlist(freqitemsetg, count)

# To create C3, L3 and all furthur sets 
temp = 0
count = 3
#print(count)
while(temp == 0):
    candidateg = candidate(freqitemsetg, count)
    #print("candidateg")
    #print(candidateg)
    
    sup = support(candidateg, dataset)
    #print("supppppppooooort")
    #print(sup)
    
    freqitemsetg = freqitemset(candidateg, sup, minsup)
    #print("frequent itemset are")
    #print(freqitemsetg)

    freqitemlist = freqlist(freqitemsetg, count)
    #print("Frequent itemset list")
    #print(freqitemlist)

    count = count + 1

    for i in range(0, len(sup)):
        if(sup[i] >= minsup):
            temp = 0
            break
        else:
            temp = 1
            break    
