# 1. LEEMOS EL COSTO DE CADA ARCO
import numpy as np
import pandas as pd
ar = pd.read_csv("ruta.csv", sep = ';')

cost = ar.to_numpy()
n_cities = len(distances)


class tsp:
  def __init__ (self, n_cities, cost):
    self.tam = n_cities
    self.distance = cost
    self.pob = []
    self.npob = 0

  def generaPoblacion(self, npob):
    ar = [int(i) for i in range(self.tam)]
    ar = np.array(ar)
    self.npob = npob
    for _ in range(self.npob):
      np.random.shuffle(ar)
      shu = [int(x) for x in ar]
      self.pob.append(shu)

  def evaluar (self, individuo):
    suma = 0
    ini = individuo[0]
    for i in range (1, self.tam):
      fin = individuo[i]
      suma += self.distance[ini][fin]
      ini = fin
    # print(individuo, suma)
    return suma
  
  def get_costos(self):
    costos = []
    for x in self.pob:
      costos.append(self.evaluar(x))
    return costos

  def seleccion(self):
    costos = self.get_costos()    

    for i in range(self.npob):
      for j in range(i+1, self.npob):
        if (costos[i] > costos[j]):
          tmp = self.pob[i]
          self.pob[i] = self.pob[j]
          self.pob[j] = tmp

          tmp2 = costos[i]
          costos[i] = costos[j]
          costos[j] = tmp2
    

  def mutacion(self):
    len2 = len(self.pob[0])
    l = random.randint(0, len2-1)
    r = random.randint(0, len2-1)

    # print(l, r)

    # print(self.pob)
    for individuo in self.pob:
      aux = individuo[l]
      individuo[l] = individuo[r]
      individuo[r] = aux
    # print(self.pob)

# https://www.hindawi.com/journals/cin/2017/7430125/
# order crossover operator
  def cruce2 (self, a, b):
    tam2 = len(a)
    l = 1
    r = 2
    mod = tam2

    noponer = []
    for i in range(l, r+1):
      noponer.append(a[i])

    # print(noponer)

    seq = []
    pos = (r+1) % mod
    for i in range(tam2):
      if (not b[pos] in noponer):
        seq.append(b[pos])
      pos = (pos + 1) % mod

    # print(seq)

    ans = [int(x) for x in a]
    pos = 0
    j = (r+1)%mod
    for _ in range(tam2):
      if (j < l or j > r):
        ans[j] = seq[pos]
        pos = pos + 1
      j = (j + 1) % mod
    
    return ans
    # print(a)
    # print(ans)

  def cruce(self):
    nuevo = []
    for i in range(self.npob-1):
      a = self.pob[i]
      b = self.pob[i+1]
      nuevo.append(self.cruce2(a,b))
      nuevo.append(self.cruce2(b,a))
      
      if (len(nuevo) > 200):
        break

    self.pob = nuevo
    self.npob = len(self.pob)

  def ejecucion(self, ngeneraciones):
    for i in range(ngeneraciones):
      self.seleccion()
      self.cruce()
      self.mutacion()

    self.seleccion()
    best = self.pob[0]
    print(best)
    print(self.evaluar(best))



x = tsp(n_cities, cost)
x.generaPoblacion(200)
x.ejecucion(100)