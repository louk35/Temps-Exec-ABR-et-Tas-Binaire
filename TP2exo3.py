#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Power Media
#
# Created:     29/03/2023
# Copyright:   (c) Power Media 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import random
import math
from time import sleep
import time


class MaxBinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, item):
        self.heap_list.append(item)
        self.current_size += 1
        self.sift_up(self.current_size)

    def sift_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] > self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            i //= 2
    def find(self, value):
        for i in range(1, self.current_size + 1):
            if self.heap_list[i] == value:
                return i
        return None

#------Tableau aléatoire

def tableau_aleatoire(p):
    n = 2**(p+1) - 1
    T = list(range(1, n+1))
    random.shuffle(T)
    return T

CoutMieuxCreation = 500
CoutPireCreation = 0
CoutMieuxRecherche = 500
CoutPireRecherche = 0

for y in range(0,50):       #Boucle qui essaye plusieurs fois pour en tiré cout pire/mieux
    T = tableau_aleatoire(2)
    #print('Tableau aléatoire : ',T)

    #Création Max Tas Binaire------
    start1 = time.time()
    heap = MaxBinaryHeap()
    values = T

    for value in values:
        heap.insert(value)
    #print('Max tas binaire :',heap.heap_list)
    TempsCreation = time.time() - start1
    #print("Algo création Max Tas Binaire : ",time.time() - start1,"seconde(s)")

    if TempsCreation > CoutPireCreation :           #Cout Mieux/Pire de la creation
        CoutPireCreation = TempsCreation
    if TempsCreation < CoutMieuxCreation :
        CoutMieuxCreation = TempsCreation

    #Recherche ----------

    start2 = time.time()    #Start Timer de la recherche
    index = heap.find(1)
    TempsRecherche = time.time() - start2       # Fin du Timer de la recherche

    #Affichage temps de recherche élément 1
    #print("Temps de recherche élément 1 : ",time.time() - start2,"seconde(s)")
    #if index is not None:
    #    print("L'élément 1 est à la position", index)
    #else:
    #    print("L'élément 1 n'est pas présent dans le tas binaire")


    if TempsRecherche > CoutPireRecherche :     #Cout Mieux/Pire de la recherche
        CoutPireRecherche = TempsRecherche
    if TempsRecherche < CoutMieuxRecherche :
        CoutMieuxRecherche = TempsRecherche

print("Cout au pire creation :",CoutPireCreation)       #Affichage Cout mieux/pire création
print("Cout au mieux creation : ",CoutMieuxCreation)

print("Cout au pire recherche :",CoutPireRecherche)     #Affichage Cout mieux/pire recherche
print("Cout au mieux recherche : ",CoutMieuxRecherche)
