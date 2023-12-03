from functools import reduce

x=[1,2,3]
y=[4,5,6]
def pirsonCorelation(listx,listy):
    if listx and listy:
        m_x=sum(x)/len(x)
        m_y=sum(y)/len(y)

        listx=list(map(lambda x: x-m_x, listx))
        listy = list(map(lambda y: y - m_y, listy))
        multyply_lists=[x*y for x, y in zip(listx,listy)]
        sum_up=reduce(lambda x,y: x+y, multyply_lists)
        print(sum_up)

        listx=list(map(lambda x:(x-m_x)**2, listx))
        listy = list(map(lambda y: (y - m_y)**2, listy))
        sum_x=reduce(lambda x,y: x+y, listx)
        sum_y=reduce(lambda x,y: x+y, listy)
        sum_down=(sum_x*sum_y)**0.5
        print(sum_down)

        if sum_down!=0:
            return  sum_up/sum_down
    return -1

print(pirsonCorelation(x,y))