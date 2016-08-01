class ident(object):
    def __init__(self,identificador):
	self.identificador=identificador
class relacion(object):
    def __init__(self,source,target):
	self.source=source
	self.target=target
class graph(object):
    def __init__(self,nodes,edges):
	self.nodes=nodes
	self.edges=edges

import json
def jdefault(o):
    if isinstance(o, set):
        return list(o)
    return o.__dict__

def write_json(fileName, grafo):
    f = open(fileName, mode='w')
    tex =json.dumps(grafo, default=jdefault)
    json.dump(tex,f)
    f.close()

def make_structure(texto):
    lista =texto.split(" ")
    lisnodos=[]
    lisres=[]
    anterior=""
    for i in lista:
        a=ident(i)
        lisnodos.insert(len(lisnodos),a)
        if anterior != "":
            c=relacion(anterior,i)
            lisres.insert(len(lisres),c)
        anterior=i
    grafo=graph(lisnodos,lisres)
    return grafo

def function_make_graph():
    texto=raw_input()
    direccion=raw_input()
    grafo=make_structure(texto)
    write_json(direccion, grafo)


#En funtion_make_graph()
# texto= "Cusco grande paraiso"
# direccion= "prueba.json"
#
#
