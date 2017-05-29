import random
def generarkSat(nv = 5, nc=5, DNF = False, k=3, car='x', path='problem.txt'):
    scl = []
    rv = getrandomvariable(nv, car)
    if DNF:        
        dnfpt = listwithclauseofonevarible(nv, nc, k, car, rv)
        dnfpt.insert(0, 'DNF')
        dnfpf = listofonevariableallclauses(nv, nc, k, car, rv)
        dnfpf.insert(0, 'DNF')
        dnfpr = listofclauses(nv, nc, k, car)
        dnfpr.insert(0, 'DNF')
        dnfa = listassignment(nv, car, rv)
        #pasar a archivo
        tofile('dnft.txt', dnfpt)
        tofile('dnff.txt', dnfpf)
        tofile('dnfr.txt', dnfpr)
        tofile('dnfa.txt', dnfa)        
    else:#CNF
        cnfpt = listofonevariableallclauses(nv, nc, k, car, rv)
        cnfpt.insert(0, 'CNF')
        cnfpf = listwithclauseofonevarible(nv, nc, k, car, rv)
        cnfpf.insert(0, 'CNF')
        cnfpr = listofclauses(nv, nc, k, car)
        cnfpr.insert(0, 'CNF')
        cnfa = listassignment(nv,car,rv)
        #pasar a archivo
        tofile('cnft.txt', cnfpt)
        tofile('cnff.txt', cnfpf)
        tofile('cnfr.txt', cnfpr)
        tofile('cnfa.txt', cnfa)    
def tofile(path, data):
    file = open(path,'w')
    print('tofile: ', path)
    if type(data) is list:
        data = '\n'.join(str(x) for x in data)
    file.write(data)
    file.close()
    print('done: ', path)

def getrandomnegation():
    return '!' if random.randint(0,1) else ''

def getrandomvariable(nv, car):
    return str(car) + str(random.randint(1,nv+1))

def clausewithonevariable(nv, k, rv, car):
    result = ''
    if not rv:
        rv = getrandomvariable(nv, car)
    result = " ".join(str(rv) for x in range(k))
    return result

def listwithclauseofonevarible(nv, nc, k, car, rv):
    scl = []
    if not rv:
        rv = getrandomvariable(nv, car)
    ct = clausewithonevariable(nv, k, rv, car)
    cf = clausewithonevariable(nv, k,'!' + rv, car)
    scl.append(ct)
    scl.append(cf)
    for c in range(nc-2):
        claus = []
        for v in range(k):
            lv = getrandomvariable(nv,car)
            n = getrandomnegation()
            claus.append(str(n) + str(lv))
        claus = " ".join(str(x) for x in claus)
        scl.append(claus)
    random.shuffle(scl)
    return scl

def listofonevariableallclauses(nv, nc, k, car, rv):
    scl = []
    if not rv:
        rv = getrandomvariable(nv, car)
        rv = getrandomnegation() + rv
    for c in range(nc):
        cl = []
        cl.append(rv)
        for v in range(k - 1):
            lv = getrandomvariable(nv,car)
            lv = getrandomnegation() + lv
            cl.append(lv)
        random.shuffle(cl)        
        claus  = " ".join(str(x) for x in cl)
        scl.append(claus)
    random.shuffle(scl)    
    return scl

def listofclauses(nv, nc, k, car):
    scl = []
    for c in range(nc):
        cl = []
        for v in range(k):
            lv = getrandomvariable(nv,car)
            lv = getrandomnegation() + lv
            cl.append(lv)
        claus  = " ".join(str(x) for x in cl)
        scl.append(claus)
    random.shuffle(scl)
    return scl

def listassignment(nv, car, rv):
    a = 'True' if random.randint(0,1) else 'False'
    ll = [a]
    mv = random.randint(1, nv+1)
    if rv:
        if (a == 'True' and not rv[0] == '!') or (a == 'False' and rv == '!') :
            ll.append(rv)
            mv -= 1
    for i  in range(mv):
        rl = getrandomvariable(nv,car)
        if rl not in ll:
            ll.append(rl)
    return ll
