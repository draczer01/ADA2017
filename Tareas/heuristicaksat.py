import generadorksat
import ksat
import random

def heuristicgrasp(probpath, iters, alpha):
    bs = None
    be = 0
    sp = ksat.SatProblem(probpath)
    print(sp.problem)
    for i in range(iters):
        so = greedyconstructive(sp, alpha)
        ls = localsearch(sp,so)
        ae = sp.evaluate(ls)
        if be < ae:
            bs = ls
            be = ae
        print(so, ae, ls,be)
    return bs, ae

def greedyconstructive(prob, alpha):
    assign = []
    val = True
    literals = prob.literalrange()
    evl = dict()        
    for l in literals:
        evl[l] = prob.costFunction(assign, val, l)

    mv = max(evl.items(), key=lambda x:x[1])
    ll = len(literals)
    while ll > 0 and mv[1] > 0:
        revl = sorted(evl.items(), key=lambda x:x[1])
        rcl = revl[0:round(alpha*len(evl))]
        ce = random.choice(rcl)
        assign.append(ce[0])
        literals.remove(ce[0])
        for l in literals:
            evl[l] = prob.costFunction(assign, val, l)
        mv = max(evl.items(), key=lambda x:x[1])
        ll = len(literals)
    return assign
    
def localsearch(prob, so):
    literals = prob.literalrange()
    vso = prob.evaluate(so)
    sk = so
    bs = so
    for l in literals:
        if l in sk:
            sk.remove(l)
        else:
            sk.append(l)
        if vso < prob.evaluate(sk):
            bs = localsearch(prob, sk)
            break
    return bs
