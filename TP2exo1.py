from time import sleep
import time

class ArbreBinaire:

   def __init__(self, valeur):
      self.valeur = valeur
      self.enfant_gauche = None
      self.enfant_droit = None

   def __str__(self):
        return str(self.valeur)

   def suppression(self, valeur):
        if valeur < self.valeur and self.enfant_gauche is not None:
            self.enfant_gauche = self.enfant_gauche.suppression(valeur)
        elif valeur > self.valeur and self.enfant_droit is not None:
            self.enfant_droit = self.enfant_droit.suppression(valeur)
        elif self.valeur == valeur:
            if self.enfant_gauche is None:
                return self.enfant_droit
            elif self.enfant_droit is None:
                return self.enfant_gauche
            else:
                successeur = self.enfant_droit
                while successeur.enfant_gauche is not None:
                    successeur = successeur.enfant_gauche
                self.valeur = successeur.valeur
                self.enfant_droit = self.enfant_droit.suppression(successeur.valeur)
        return self

   def recherche(self, valeur):
        if self.valeur == valeur:
            return True
        elif valeur < self.valeur and self.enfant_gauche is not None:
            return self.enfant_gauche.recherche(valeur)
        elif valeur > self.valeur and self.enfant_droit is not None:
            return self.enfant_droit.recherche(valeur)
        else:
            return False

   def insert_gauche(self, valeur):
      if self.enfant_gauche == None:
         self.enfant_gauche = ArbreBinaire(valeur)
      else:
         new_node = ArbreBinaire(valeur)
         new_node.enfant_gauche = self.enfant_gauche
         self.enfant_gauche = new_node

   def insert_droit(self, valeur):
      if self.enfant_droit == None:
         self.enfant_droit = ArbreBinaire(valeur)
      else:
         new_node = ArbreBinaire(valeur)
         new_node.enfant_droit = self.enfant_droit
         self.enfant_droit = new_node

   def get_valeur(self):
      return self.valeur

   def get_gauche(self):
      return self.enfant_gauche

   def get_droit(self):
      return self.enfant_droit


   def insert(self,valeur):
    if valeur < self.valeur:
        if self.enfant_gauche is None:
            self.enfant_gauche = ArbreBinaire(valeur)
        else:
            self.enfant_gauche.insert(valeur)
    elif valeur > self.valeur:
        if self.enfant_droit is None:
            self.enfant_droit = ArbreBinaire(valeur)
        else:
            self.enfant_droit.insert(valeur)

#######fin de la classe########
### CreerABRComplet Tableau#####
def creer_abr_complet(p):
    T=[0]
    for i in range(1,2**(p+1)):
        T.append(0)
    T[1]= 2**p
    k=2

    for i in range (p-1,-1,-1):
        T[k]=2**i
        k=k+1
        for j in range (1,2**(p-i)):
            T[k]=T[k-1]+2**(i+1)
            k=k+1
    return T
### CreerABRfiliforme Tableau#####


def creer_abr_filiforme(p):
    compteur = 1
    T=[0]
    for i in range(1,2**(p+1)):
        T.append(0)

    for i in range(1,2**(p+1)):
        T[i]= compteur
        compteur = compteur +1
    return T



################################# On a rencontrer un probleme d'impossibilité d'effectuer beaucoup de récursion (contrainte Python), car l'arbre filiforme utilise beaucoup de récursion on va donc utiliser un delay pour celui (artificialise)
delay = 0.1

T2= creer_abr_filiforme(1)
#print (T2)
#print(len(T2))
l=len(T2)
i=1
##Start Timer T2 Filiforme
start1 = time.time()
racine2 = ArbreBinaire(T2[i])
for i in range(2,l):
    #sleep(delay)
    racine2.insert(T2[i])
print("Algo insertion filiforme : ",time.time() - start1,"seconde(s)")
##End Timer T2 Filiforme


T=creer_abr_complet(3)
print(T)
#print(len(T))
l=len(T)


i=1
##Start Timer T Complet
start2 = time.time()
racine = ArbreBinaire(T[i])
for i in range(2,l):
   racine.insert(T[i])
print("Algo insertion ABR : ",time.time() - start2,"seconde(s)")

##End Timer T Complet


racine = racine.suppression(15)

######début de la construction de l'arbre binaire###########

#racine = ArbreBinaire('8')
#racine.insert('4')
#racine.insert('12')
#racine.insert('2')
#racine.insert('6')
#racine.insert('10')
#racine.insert('14')
#racine.insert('1')
#racine.insert('3')
#racine.insert('5')
#racine.insert('7')
#racine.insert('9')
#racine.insert('11')
#racine.insert('13')
#racine.insert('15')


######fin de la construction de l'arbre binaire###########
def Manipuler_ABR_complet(racine,T):
    print(affiche(racine))
    p = len(T)-1
    for i in range(2**p, 0, -1):
        racine = racine.suppression(i)
        racine = racine.insert(i+1)
    return racine



def affiche(T):
   if T != None:
      return (T.get_valeur(),affiche(T.get_gauche()),affiche(T.get_droit()))
print(affiche(racine))
#print(affiche(racine2))
#print(pprint(racine))

if racine.recherche(3):
    print("La valeur est présente dans l'arbre")
else:
    print("La valeur n'est pas présente dans l'arbre")

#arbre_modifie = Manipuler_ABR_complet(racine,T)
#print(affiche(arbre_modifie))
#print(len(T))
