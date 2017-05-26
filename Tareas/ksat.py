class SatProblem:
    def __init__(self, path = None, dnf = False, problem = None):
        if path is not None:
            l = open(path,'r').readlines()
            print(l)
            p = l[0][-1]
            self._dnf = (p == 'False' or p =='DNF' or p == 'dnf')
            self._problem = [(x.replace("\n", "").split(' ')) for x in l[1:]]
        else:
            self._dnf = dnf
            self._problem = problem

    @property
    def problem(self):
        return self._problem
    
    @property
    def dnf(self):
        return self._dnf
            
    def evaluate(self, assignation, value = True):
        valid = 0
        result = True
        #print(self._dnf)
        for clause_tuple in self._problem:
            clause = True if self._dnf else False
            for lit in clause_tuple:
                n = lit[0] == '!'
                val = lit if not n else lit[1:]
                var_res = (val in assignation and not n ) or (val not in assignation and n)
                var_res = not var_res if not value else var_res
                clause = (clause and var_res) if self._dnf else (var_res or clause)
                #print(clause_tuple,lit, var_res,clause)
            result = (result or clause) if self._dnf else (result and clause)
            valid += 1 if clause else 0
        return 1 if result == 1 else (valid / len(self._problem))

    def countapperance(self, assignation, literal, value = True):
        result = 0        
        for clause in self._problem:
            for lit in clause:                
                n = lit[0] == '!'
                val = lit if not n else lit[1:]
                if value:
                    if lit in assignation:
                        if n:
                            continue
                        else:       
                            break                                                     
                    else:
                        if n:
                            if lit == literal:
                                result +=1
                            else:
                                break
                        else:
                            if lit == literal:
                                result +=1
                            else:
                                continue
                else:                        
                    if lit in assignation:
                        if n:
                            break                                    
                        else:       
                            continue
                                                     
                    else:
                        if n:
                            if lit == literal:
                                result +=1
                            else:
                               continue                      
                        else:
                            if lit == literal:
                                result +=1
                            else:
                                break    
                                
        return result
    
    def costFunction(self, assignation, literal,value=True): 
        return self.countapperance(assignation, literal, value)

    def literalrange(self):
        literal = set()
        for clause in self._problem:
            for lit in clause:
                n = lit[0] == '!'
                val = lit if not n else lit[1:]
                literal.add(val)
        return list(literal)        
        
            

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

