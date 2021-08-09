from datetime import date

def ask_for_date(name):
    data = input(name).split('/')
    try:
        return  date(int(data[0]),int(data[1]),int(data[2]))
    except:
        print('WRONG')
        
    ask_for_date(name)
    


def calculate_age():
    born = ask_for_date('')
    today = date.today()
    extra_year = 1 if ((today.month, today.day) < (born.month, born.day)) else 0
    return today.year - born.year - extra_year

print(calculate_age())
#1995/10/23
input('any ey to exit')