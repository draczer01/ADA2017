def tsat(dirprob, dirass):
    filea = open(dirass, 'r')
    val = filea.readline()[:-1]== 'False'
    ass = []
    a = filea.readline()[:-1]
    while a:
        ass.append(a)
        a =filea.readline()[:-1]
    print(ass)
    filep = open(dirprob, 'r')
    p = filep.readline()[:-1]
    dnf = (p == 'False' or p =='DNF' or p == 'dnf')
    if dnf:
        print('DNF')
        p = filep.readline()[:-1]
        r = False
        while p:
            varbs = p.split(' ')
            rc, rv = True, True
            print(varbs)
            for var in varbs:
                va = ''
                neg = False
                if(var[0]== '!'):
                  va = var[1:]
                  neg = True
                else:
                    va = var
                print(var, va)
                rv = (va in ass and not neg) or (va not in ass and neg)
                rc = rc and rv
                if not rv:
                    break
                print('rc: ', rc, ' rv: ', rv)
            r = r or rc
            p = filep.readline()[:-1]
    else:
        print('CNF')
        r = True,
        p = filep.readline()[:-1]
        while p:
            varbs = p.split(' ')
            rc, rv = False, True
            print(varbs)
            for var in varbs:
                va = ''
                neg = False
                if(var[0]== '!'):
                  va = var[1:]
                  neg = True
                else:
                    va = var
                rv = (va in ass and not neg) or (va not in ass and neg)
                rc = rc or rv
                print('rc: ', rc, ' rv: ', rv)
            r = r and rc
            if not rc:
                break
            else:
                p = filep.readline()[:-1]        
    return r     
    
                
#print(tsat('ptsat.py', 'atsat.py'))

