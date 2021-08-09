in_list = list()
listt = list()
n = int(input())
x=0
for i in range(n):
    in1 = input().lower()
    in_list.append(list(in1.split('.')))



listt = list(map(lambda x:(x[1].capitalize()),in_list))

for item in range(len(in_list)):
    in_list[item][1] = listt[item]
    

for i in in_list():
    
