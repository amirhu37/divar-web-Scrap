genrelist={'Horror':0, 'Romance':0, 'Comedy':0, 'History':0, 'Adventure':0, 'Action':0}
x = int(input())
i = 0
ara =[]
for i in range(x):
    name , g1 , g2 , g3 = input().split(' ')
    ara.append(g1)
    ara.append(g2)
    ara.append(g3)
for e in range(len(ara)):
    if ara[e] =='Horror':
        genrelist['Horror'] +=1
    elif ara[e] =='Romance':
        genrelist['Romance'] +=1
    elif ara[e] =='Comedy':
        genrelist['Comedy'] +=1
    elif ara[e] =='History':
        genrelist['History'] +=1
    elif ara[e] =='Adventure':
        genrelist['Adventure'] +=1
    elif ara[e] =='Action':
        genrelist['Action'] +=1

genrelist1 = dict(sorted(genrelist.items(), key = lambda kv:(kv[1]  , kv[0]) , reverse = True))
genrelist2 = dict(sorted(genrelist.items(), key = lambda kv:(kv[1]  , kv[0]) , reverse = True))


for keys,values in genrelist.items():
    if        
    print(keys , end= ' : ')
    print(values)