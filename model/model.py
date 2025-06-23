import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()

    def getAnni(self):
        return DAO.getAnni()
    def getSquadreAnno(self, anno):
        return DAO.getSquadreAnno(anno)

    def buildGraph(self, anno):
        listaNodi = DAO.getSquadreAnno(anno)
        self.grafo.add_nodes_from(listaNodi)

        for u in listaNodi:
            for v in listaNodi:
                if u!=v:
                    salariTot = DAO.getSalarioSquadre(u,v,anno)
                    self.grafo.add_edge(u, v, weight = salariTot)

    def getNumeriGrafo(self):
        return self.grafo.number_of_nodes(), self.grafo.number_of_edges()

    def getNodes(self):
        return self.grafo.nodes()

    def getSquadreVicinePesate(self, source):
        listaTuplaVicini = []
        vicini = self.grafo.neighbors(source)
        for vicino in vicini:
            peso = self.grafo[source][vicino]["weight"][0]
            if peso is None:
                peso = 0
            listaTuplaVicini.append((vicino, peso))
        listaTuplaViciniOrdinata = sorted(listaTuplaVicini, key=lambda x: x[1], reverse = True )
        return listaTuplaViciniOrdinata
