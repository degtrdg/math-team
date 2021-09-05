import numpy as np
import queue
 
 
class Problem:
    def __init__(self):
        self.answers = queue.queue()
        # queue for answers with linked list
        # index of problem made in different class not in p1
        # tk gui
 
    def p1(self):
        a = np.random.randint(10, 1000)
        b = np.random.randint(10, 1000)
        c = np.random.randint(10, 1000)
        d = a+b+c
        self.answers.enqueue(d)  # inputting the answer inside of the queue
        return('{0}+{1}+{2}'.format(a, b, c))
 
    def p2(self):
        a = np.random.randint(10, 1000)
        b = np.random.randint(10, 1000)
        c = np.random.randint(10, 1000)
        d = a-b-c
        self.answers.enqueue(d)
        return('{0}-{1}-{2}'.format(a, b, c))
 
    def p3(self):
        n = np.random.randint(2, 3)
        range_start = 10**(n-1)
        range_end = (10**n)-1
        d = np.random.randint(range_start, range_end)*(10**-1)
        self.answers.enqueue(d*2.5)
        return('{0}*2.5'.format(d))
 
    def p4(self):
        a = np.random.randint(1, 25)
        b = np.random.randint(1, 10)
        c = np.random.randint(1, 25)
        d = np.random.randint(1, 10)
        if c/d < a/b:
            e = a/b-c/d
            self.answers.enqueue(e)
            return('{0}/{1}-{2}/{3}'.format(a, b, c, d))
        else:
            e = c/d-a/b
            self.answers.enqueue(e)
            return('{0}/{1}-{2}/{3}'.format(c, d, a, b))
 
    def p5(self):
        a = np.random.randint(1, 99)
        b = np.random.randint(1, 99)
        d = a*b
        self.answers.enqueue(d)
        return('{0}*{1}'.format(a, b))
 
    def p6(self):
        a = np.random.randint(1, 1000)
        b = np.random.randint(1, 10)
        d = a/b
        self.answers.enqueue(d)
        return('{0}/{1}'.format(a, b))

