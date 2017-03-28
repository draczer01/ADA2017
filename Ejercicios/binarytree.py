class node:
    def __init__(self,val):
        self.value = val
        self.count =1
        self.left = None
        self.right = None
    def add(self,new):
        if new  < self.value:
            #ver si hay nodo hijo
            if self.left is None:
                self.left = node(new)
            else:
                self.left.add(new)
        elif new > self.value:
            if self.right is None:
                self.right = node(new)
            else:
                self.right.add(new)
        else:
            self.count += 1
            
    def search(self,i):
        if self.value == i:
            return self
        elif self.value > i:
            if self.left is None:
                return False
            return self.left.search(i)
        else:
            if self.right is None:
                return False
            return self.right.search(i)

    def __str__(self):
        s = ''
        if self.left is not None:
            s += str(self.left)
        s += str(self.value) + " "
        if self.right is not None:
            s += self.right.__str__()
        return s

    def delete(self, i):
        if i < self.value:                    
            if self.left is not None and self.left.value == i:
                self.left =  None
                return True
            elif self.left is not None:
                self.left.delete(i)
            else:
                #i no está en el arbol izq y es menor que self
                return False
        elif i > self.value:
            if self.right is not None and self.right.value == i:
                self.right = None
                return True
            elif self.right is not None:
                self.right.delete(i)
            else:
                #i no esta en el arbol der y es mayor que self
                return False
        else:
            #i es igual a self
            return False
        
            
raiz = node(13)
raiz.add(16)
raiz.add(23)
raiz.add(4)
print(raiz.search(8))
#print(raiz.search(23).count)
raiz.add(23)
#print(raiz.search(23).count)

print(raiz)

print(raiz.delete(4))
print(raiz)
print(raiz.delete(13))
print(raiz)
