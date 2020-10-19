grafo= {'a':{'b':2,'f':1},
        'b':{'a':2,'c':2,'d':2,'e':4},
        'c':{'b':2,'e':3,'z':1},
        'd':{'b':2,'e':4,'f':3},
        'e':{'b':4,'c':3,'d':4,'g':7},
        'f':{'a':1,'d':3,'g':5},
        'g':{'e':7,'f':5,'z':6},
        'z':{'c':1,'g':6},
        }

def algoritmoPrim(raiz,grafo):
    listaBusqueda=[raiz]
    iteraciones=[]

    while( len(listaBusqueda) != len(grafo)  ):
        valorminimo=1000
        nodoHijo=None
        nodoPadre=None
        for x in listaBusqueda:
            for row in grafo[x]:
                if  row not in listaBusqueda and grafo[x][row]<valorminimo:
                    nodoHijo=row
                    nodoPadre=x
                    valorminimo=grafo[x][row]
                   
        listaBusqueda.append(nodoHijo)
        iteraciones.append((nodoPadre,nodoHijo))
    
    return iteraciones,listaBusqueda

raiz=input("Digite el valor inicial: ")
iteraciones,T=algoritmoPrim(raiz,grafo)
print("iteraciones ",iteraciones, "\n",T)