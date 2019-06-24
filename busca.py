#!/usr/bin/python
# -*- coding: utf-8 -*-

#Algoritmo de Busca de Custo Uniforme - IA (Cedido pelo prof. Yuri Malheiros)

class State(object):
    def __init__(self, name):
        self.name = name
        self.neighbors = []

    def add_neighbors (self, states):
        for state in states:
            self.neighbors.append({"state": state[0], "cost": state[1]})

    def __str__ (self):
        return self.name
    
    def __repr__ (self):
        return self.name
    

def search (inital_state, goal):
    frontier = [{"state": inital_state, "cost": 0, "parent": None}]
    explored = set()

    while True:
        
        #print(frontier)
        
        if len(frontier) == 0:
            return False
        
        chosen = choose_state(frontier)
        explored.add(chosen["state"])

        if chosen["state"] == goal:
            return chosen
        
        for neighbor in chosen["state"].neighbors:
            
            path_cost = neighbor["cost"]+chosen["cost"]
        
            if neighbor ["state"] in explored:
                continue
            else:                
                flag = False
                
                for node in frontier:
                    if neighbor["state"] == node["state"]:
                        flag = True
                        
                        if node["cost"] > path_cost:
                            frontier.remove(node)
                            frontier.append({"state": neighbor["state"], "cost": path_cost, "parent": chosen})
                if flag == False:
                    frontier.append({"state": neighbor["state"], "cost": path_cost, "parent": chosen})
    
                

def choose_state(frontier):
    lower_cost_node = frontier[0]
    for node in frontier:
        if node["cost"] < lower_cost_node ["cost"]:
            lower_cost_node = node
    frontier.remove(lower_cost_node)
    return lower_cost_node

        
joao_pessoa = State ("João Pessoa")
campina_grande = State ("Campina Grande")
itabaiana = State ("Itabaiana")
santa_rita = State ("Santa Rita")
mamanguape = State ("Mamanguape")
guarabira = State ("Guarabira")
areia = State ("Areia")
picui = State("Picuí")
soledade = State ("Soledade")
coxixola = State ("Coxixola")
patos = State ("Patos")
monteiro = State ("Monteiro")
catole = State ("Catolé")
pombal = State ("Pombal")
itaporanga = State ("Itaporanga")
souza = State ("Souza")
cajazeiras = State ("Cajazeiras")

    

joao_pessoa.add_neighbors([[campina_grande, 125], [itabaiana, 68], [santa_rita, 26]])
campina_grande.add_neighbors([[joao_pessoa, 125], [itabaiana, 65], [areia, 40], [coxixola, 128], [soledade, 58]])
itabaiana.add_neighbors([[joao_pessoa, 68], [campina_grande, 65]])
santa_rita.add_neighbors([[joao_pessoa, 26], [mamanguape, 38]])
mamanguape.add_neighbors([[santa_rita,38], [ guarabira, 42]])
guarabira.add_neighbors([[mamanguape, 42], [areia, 41]])
areia.add_neighbors([[guarabira,41], [campina_grande,40]])
picui.add_neighbors([[soledade,69]])
soledade.add_neighbors([[campina_grande, 58], [patos, 117], [picui, 69]])
coxixola.add_neighbors([[campina_grande, 128], [monteiro, 83]])
patos.add_neighbors([[soledade, 117], [pombal, 71], [itaporanga, 108]])
monteiro.add_neighbors([[coxixola, 83], [itaporanga, 224]])
catole.add_neighbors([[pombal, 57]])
pombal.add_neighbors([[catole, 57], [patos, 71], [souza, 56]])
itaporanga.add_neighbors([[patos, 108], [monteiro, 224], [cajazeiras, 121]])
souza.add_neighbors([[pombal, 56], [cajazeiras, 43]])
cajazeiras.add_neighbors([[souza,43], [itaporanga, 121]])

state = search(joao_pessoa, cajazeiras)

#path = []
while state != None:
    print(state["state"])
    #path.append(state["state"])
    state = state["parent"]
#path.reverse()
#print(path)

#se quiser imprimir na tela em ordem diferente, alterar a posição dos comentários.


