# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:11:37 2018

@author: gabmv
"""

class grafo(object):
    def setValores(self,l):
        self.vertice=0
        self.arestas=0
        self.adj=list(range(l))
        
def zerarMatrixAdj(matriz):	
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            matriz[i][j]=-1
    return matriz;	

# Cria um grafo G como matriz
# V : Quantidade de vértices do grafo
def criarGrafo(quantidade):
    g = object.__new__(grafo)
    g.setValores(quantidade)
    for i in range(0,len(g.adj)):
        g.adj[i]=list(range(quantidade))
    g.vertice=quantidade
    print(g.adj)
    g.adj = zerarMatrixAdj(g.adj)
    return g

#Insere a aresta a_ij num grafo 
#G : Ponteiro para grafo simples
#i, j : Vértices extremidades da aresta (i,j) ~ (j,i)
def inserirAresta(grafo,i,j):
    if(i !=j and grafo.adj[i][j] == 0):
        grafo.adj[i][j] = grafo.adj[j][i] = 1
        grafo.aresta+=1
    return grafo

#Remove a aresta a_ij do grafo
#G : Ponteiro para grafo
#i,j : Vértices extremidades da aresta a ser deletada
def removeAresta(grafo,i,j):
    if(i!=j and grafo.adj[i][j] == 1):
        grafo.adj[i][j] = grafo.adj[j][i] = 1
        grafo.aresta-=1
    return grafo

#Exibe na tela o grafo G como matriz de adjacências
#G : Ponteiro para o grafo a ser exibido
def imprimeGrafo(grafo):
    for i in range(0,grafo.vertice):
        print(i)
        for j in range(0,grafo.vertice):
            print(j)
#Retorna 1 se os vértices v e w são adjacentes e 0 caso contrário
#G : Ponteiro para o grafo 
#v, w : Vértices a serem analisados
def verticesADJ(grafo,v,w):
    return grafo.adj[v][w]   

#Calcula e retorna o grau de um vértice
#G : Ponteiro para o grafo
#v : Vértice cujo grau deseja-se saber
def grauVertice(grafo,v):
    q = grafo.vertice
    grau = 0
    q-=1
    while(q>=0):
        grau+= grafo.adj[v][q]
        q-=1
    return grau

#Exibe todos os vértices adjacentes a um vertice
#G : Ponteiro para o grafo
#v : Vértice analisado
def exibeVerticesADJ(grafo,vertice):
    for j in range(0,grafo.vertice):
        if(j != vertice and grafo.adj[vertice][j] ==1):
            print(j)
        
        
        
def main():
    escolha=-1
    G = criarGrafo(1)
    while(escolha!=0):
        escolha = int(input("\n 1-Construir Grafo \n 2 - Verificar adjacencias \n 3 - Exibir adjacencias \n 4 - Exibir Grau \n"))
        if(escolha==1):    
            v = int(input("manda o numero de vertices ai fion "))
            e = int(input("manda o numero de arestas ai man "))
            G = criarGrafo(v)
            for q in range(0,e):
                i = int(input("vai inserindo arestas ai fion "))
                j = int(input("vai inserindo arestas ai fion "))
                G = inserirAresta(G,i,j)
            escolha=-1
        elif (escolha == 2):
            imprimeGrafo(G)
        elif (escolha == 3):
            exibeVerticesADJ(G)
    
        
main()
"""

	imprimirGrafo( G );
	printf(" (0,1) São vertices adjacentes? %d\n", vertivesAdjacentes(G, 0, 1) );
	printf("Grau do vertice 0 : %d\n", grauVertice(G, 0) ) ;
	printf("Exibir vertices adjacentes a 0: \n");
	exibirVerticesAdjacentes(G, 0);
}
        """
        
