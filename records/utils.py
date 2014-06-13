#coding=utf-8

def payoff(s_answer, u_answer, s=1):
    length = len(s_answer)
    msg = ''
    if not u_answer:
        msg = 'Answer from user is missing'
    if length % s != 0:
        msg = 'Parameter is supposed to divide '+ len(s_answer)
    c = length / s
    correct_count = 0
    print "c is ",c
    for i in range(c):#
        if s_answer[i*s:(i+1)*s] == u_answer[i*s:(i+1)*s]:
            
            correct_count += 1
    return s * correct_count        


if __name__ == "__main__":
    print payoff('1'*12,'111111011110',12)