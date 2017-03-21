import generadorksat

def heristicgrasp(probm, iters, alpha):
    bs = None
    be = None
    for i in range(iters):
        cs = greedyconstructive(alpha)
        ls = localsearch(cs)
        ae = probm.evaluate(ls)
        if be < ae:
            bs = ls
            be = ae
    return bs

def greedyconstructive(alpha):
    
