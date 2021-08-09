# B group worldCup
iplus=[]
splus=[]
pplus=[]
mplus=[]
ineg=[]
sneg =[]
pneg =[]
mneg =[]
Spain ={'wins':0 , 'loses':0 , 'draws':0 , 'goal difference':0 , 'points':0 }
Iran ={'wins':0 , 'loses':0 , 'draws':0 , 'goal difference':0 , 'points':0 }
Portugal ={'wins':0 , 'loses':0 , 'draws':0 , 'goal difference':0 , 'points':0 }
Morocco ={'wins':0 , 'loses':0 , 'draws':0 , 'goal difference':0 , 'points':0 }
c=0
for index in range(1,7):
    x,y = input().split('-')
    c +=1
    if c == 1 : #iran-spain
        iplus.append(int(x))
        splus.append(int(y))
        sneg.append(int(x))
        ineg.append(int(y))
        if x > y:
            Iran['wins'] += 1
            Iran['points'] +=3
            Spain['loses'] += 1
        elif x==y:
            Spain['draws'] += 1
            Iran['draws'] += 1
            Iran['points'] +=1
            Spain['points'] +=1
        elif x < y:
            Spain['wins'] += 1
            Iran['loses'] += 1
            Spain['points'] +=3
    elif c == 2: #IRAN-POr
        iplus.append(int(x))
        pplus.append(int(y))
        pneg.append(int(x))
        ineg.append(int(y))
        if x > y:
            Iran['wins'] += 1
            Portugal['loses'] += 1
            Iran['points'] +=3
        elif x==y:
            Portugal['draws'] += 1
            Iran['draws'] += 1
            Portugal['points'] +=1
            Iran['points'] +=1
        elif x < y:
            Portugal['wins'] += 1
            Iran['loses'] += 1
            Portugal['points'] +=3
    elif c == 3:#irna- moroccow
        iplus.append(int(x))
        mplus.append(int(y))
        mneg.append(int(x))
        ineg.append(int(y))
        if x > y:
            Iran['wins'] += 1
            Morocco['loses'] += 1
            Iran['points'] +=3
        elif x==y:
            Morocco['draws'] += 1
            Iran['draws'] += 1
            Iran['points'] +=1
            Morocco['points'] +=1
        elif x < y:
            Morocco['wins'] += 1
            Iran['loses'] += 1
            Morocco['points'] +=3
    elif c == 4:#spain-por
        splus.append(int(x))
        pplus.append(int(y))
        pneg.append(int(x))
        sneg.append(int(y))
        if x > y:
            Spain['wins'] += 1
            Portugal['loses'] += 1
            Spain['points'] +=3
        elif x==y:
            Spain['draws'] += 1
            Portugal['draws'] += 1
            Spain['points'] +=1
            Portugal['points'] +=1
        elif x < y:
            Portugal['wins'] += 1
            Spain['loses'] += 1
            Portugal['points'] +=3
    elif c == 5:#spain-mor
        splus.append(int(x))
        mplus.append(int(y))
        mneg.append(int(x))
        sneg.append(int(y))
        if x > y:
            Spain['wins'] += 1
            Morocco['loses'] += 1
            Spain['points'] +=3
        elif x==y:
            Spain['draws'] += 1
            Morocco['draws'] += 1
            Spain['points'] +=1
            Morocco['points'] +=1
        elif x < y:
            Morocco['wins'] += 1
            Spain['loses'] += 1
            Morocco['points'] +=3
    elif c == 6:#por- mor
        pplus.append(int(x))
        mplus.append(int(y))
        mneg.append(int(x))
        pneg.append(int(y))
        if x > y:
            Portugal['wins'] += 1
            Morocco['loses'] += 1
            Portugal['points'] +=3
        elif x==y:
            Portugal['draws'] += 1
            Morocco['draws'] += 1
            Portugal['points'] +=1
            Morocco['points'] +=1
        elif x < y:
            Portugal['loses'] += 1
            Morocco['wins'] += 1
            Portugal['points'] +=1
            Morocco['points'] +=1

i_goal_s = sum(iplus)
s_goal_s = sum(splus)
p_goal_s = sum(pplus)
m_goal_s = sum(mplus)
i_goal_n = sum(ineg)
s_goal_n = sum(sneg)
p_goal_n = sum(pneg)
m_goal_n = sum(mneg)
Spain['goal difference'] = s_goal_s - s_goal_n
Iran['goal difference'] = i_goal_s - i_goal_n
Morocco['goal difference'] = m_goal_s - m_goal_n
Portugal['goal difference'] = p_goal_s - p_goal_n

print('Spain ', 'wins:{0}'.format(Spain['wins']),',', 'loses:{0}'.format(Spain['loses']) ,',','draws:{0}'.format(Spain['draws']) ,',','goal difference:{0}'.format(Spain['goal difference']),',','points:{0}'.format(Spain['points']))


print('Iran ', 'wins:{0}'.format(Iran['wins']),',', 'loses:{0}'.format(Iran['loses']),' , ','draws:{0}'.format(Iran['draws']) ,',','goal difference:{0}'.format(Iran['goal difference']),',','points:{0}'.format(Iran['points']))


print('Portugal ', 'wins:{0}'.format(Portugal['wins']),',', 'loses:{0}'.format(Portugal['loses']) ,' , ','draws:{0}'.format(Portugal['draws']) ,',','goal difference:{0}'.format(Portugal['goal difference']) ,',','points:{0}'.format(Portugal['points']) )


print('Morocco ', 'wins:{0}'.format(Morocco['wins']) ,',', 'loses:{0}'.format(Morocco['loses'] ),' , ','draws:{0}'.format(Morocco['draws']) ,',','goal difference:{0}'.format(Morocco['goal difference']) ,',','points:{0}'.format(Morocco['points']))
