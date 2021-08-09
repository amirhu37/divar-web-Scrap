#klass koli(parent)
class student():
    a_list = list() 
    w_list = list()
    h_list = list()
    def __init__(self):
        self.a_list = list() 
        self.w_list = list()
        self.h_list = list()
    def gt_ag(self, ags):
       student.a_list.append(ags)
       return ags 
    def gt_wg(self, wgs):
        self.w_list.append(wgs)
    def gt_hg(self , hgs):
        self.h_list.append(hgs)
#klass dansh amozan grouh A
class klass_a(student):
    a_list = list() 
    w_list = list()
    h_list = list()
    def avg_ag(self):
        res = float(sum(klass_a.a_list[0]) / (len(klass_a.a_list[0])-1))
        return res
    def avg_wg(self):
        res = float(sum(klass_a.w_list[0]) / (len(klass_a.w_list[0])-1))
        return res
    def avg_hg(self):
        res = float(sum(klass_a.h_list[0]) / (len(klass_a.h_list[0])-1))
        return res
#klass dansh amozan grouh B
class klass_b(student):
    a_list = list() 
    w_list = list()
    h_list = list()
    def avg_ag(self):
        res = float(sum(klass_b.a_list[0]) / (len(klass_b.a_list[0])-1))
        return res
    def avg_wg(self):
        res = float(sum(klass_b.w_list[0]) / (len(klass_b.w_list[0])-1))
        return res
    def avg_hg(self):
        res = float(sum(klass_b.h_list[0]) / (len(klass_b.h_list[0])-1))
        return res
            
#mohasebe ye sen vazn va qad grouh A
n = int(input())
klass_a.a_list = [(*map(int, input().split()), i) for i in range(n-(n-1))]
klass_a.w_list = [(*map(int, input().split()), i) for i in range(n-(n-1))]
klass_a.h_list = [(*map(int, input().split()), i) for i in range(n-(n-1))]
#mohasebe ye sen vazn va qad grouh B
n = int(input())
klass_b.a_list = [(*map(int, input().split()), i) for i in range(n-(n-1))]
klass_b.w_list = [(*map(int, input().split()), i) for i in range(n-(n-1))]
klass_b.h_list = [(*map(int, input().split()), i) for i in range(n-(n-1))]
#seri aval khoroji ha
print(klass_a().avg_ag())
print(klass_a().avg_wg())
print(klass_a().avg_hg())
print(klass_b().avg_ag())
print(klass_b().avg_wg())
print(klass_b().avg_hg())
#seri dovom khoroji ha
if klass_a().avg_hg() > klass_b().avg_hg():
    print('A')
elif klass_a().avg_hg() == klass_b().avg_hg():
    if klass_a().avg_wg() < klass_b().avg_wg():
        print('A')
    elif klass_a().avg_wg() > klass_b().avg_wg():
        print('B')
    elif klass_a().avg_wg() == klass_b().avg_wg():
        print('Same')
elif klass_a().avg_hg() < klass_b().avg_hg():
    print('B')
