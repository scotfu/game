#coding=utf-8
import random
from numpy.random import uniform
import pprint


n = 16
block_size = 4


def payoff(s_answer, u_answer, s=1):
    length = len(s_answer)
    msg = ''
    if not u_answer:
        msg = 'Answer from user is missing'
    if length % s != 0:
        msg = 'Parameter is supposed to divide '+ len(s_answer)
    c = length / s
    correct_count = 0
    for i in range(c):#
        if s_answer[i*s:(i+1)*s] == u_answer[i*s:(i+1)*s]:
            
            correct_count += 1
    return s * correct_count        


# block size is unknown
def construction():

    a = [[]] * n
    for temp in range(n):
        a[temp] = [0]*n

    
    start = 0
    stop = start + block_size
    for i in range(n):
        for j in range(start,stop):
#            print "i is ",i,"j is ",j
            if i != j:
                a[i][j] = 1
        if (i % block_size) == (block_size - 1):
            start = start + block_size
            stop  = start + block_size

    return a        

            
def connect(a):
    for i in range(n):
        if (i % block_size) == 0:
            connect_index = (n + i - 1) % n
            a[i][connect_index] = 1
            a[connect_index][i] = 1
    return a        


def rewire(a,p):
    base = 0
    for i in range(n):
        start = i + 1
        stop = start + (block_size - 1) / 2
        for j in range(start,stop):
            if ((i + 1) % block_size != 0 ) or ((j % block_size) != 0):
                if uniform() < p:
                    #uniform() will return a float number between 0 and 1 from uniform distribution 
                    if (j - base) > (block_size - 1):
                        disconnect_index = j - block_size
                    else:
                        disconnect_index = j
                    a[i][disconnect_index] = 0;
                    a[disconnect_index][i] = 0;

                    ran_node = random.randrange(n)
                    while ran_node == i:
                        ran_node = random.randrange(n)
                    a[i][ran_node] = 1;
                    a[ran_node][j] = 1;
        if (i + 1) % block_size == 0:
            base = base + block_size
    return a        
    
    
    

    
if __name__ == "__main__":
#    print payoff('1'*12,'111111011110',12)

    a = construction()
    print "<<< Result of construction:>>>"
    pprint.pprint(a)
    print "<<< Result of connection:>>>"
    pprint.pprint(connect(a))
    print "<<< Result of rewire:>>>"
    pprint.pprint(rewire(a, 0.3))