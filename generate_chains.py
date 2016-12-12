import pickle
import pygraphml
import sys
from pygraphml import Graph
from pygraphml import GraphMLParser

def generate_chain(screen_name, store_graph):

    fh = open("downloaded/%s/tweets.txt" % screen_name, "r")
     
    chain = {}
     
    g = Graph()
    nodes = {}

    def generate_trigram(words):
        if len(words) < 3:
            return
        for i in range(len(words) - 2):
            yield (words[i], words[i+1], words[i+2])
            
            if((words[i], words[i+1]) in nodes):
                if((words[i+2]) in nodes):
                    g.add_edge(nodes[(words[i], words[i+1])], nodes[(words[i+2])])
                else:
                    nodes[(words[i+2])] = g.add_node(words[i+2])
                    g.add_edge(nodes[(words[i], words[i+1])], nodes[(words[i+2])])
            else:
                nodes[(words[i], words[i+1])] = g.add_node(words[i] + words[i+1])
                if((words[i+2]) in nodes):
                    g.add_edge(nodes[(words[i], words[i+1])], nodes[(words[i+2])])
                else:
                    nodes[(words[i+2])] = g.add_node(words[i+2])
                    g.add_edge(nodes[(words[i], words[i+1])], nodes[(words[i+2])])
     
    for line in fh.readlines():
        words = line.split()
        for word1, word2, word3 in generate_trigram(words):
            key = (word1, word2)
            if key in chain:
                chain[key].append(word3)
            else:
                chain[key] = [word3]

    if(store_graph):
        parser = GraphMLParser()
        parser.write(g, "downloaded/%s/graph.graphml" % screen_name)
     
    pickle.dump(chain, open("downloaded/%s/chain.p" % screen_name, "wb" ))

if __name__ == '__main__':
    generate_chain(sys.argv[1], True)
