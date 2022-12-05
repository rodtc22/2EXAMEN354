# 1. LOAD LIBRARIES
import random
import numpy as np

from deap import algorithms
from deap import base 
from deap import creator
from deap import tools

# 2. LEEMOS EL COSTO DE CADA ARCO
import pandas as pd
ar = pd.read_csv("ruta.csv", sep = ';')

distances = ar.to_numpy()
NUMBER_OF_CITIES = len(distances)


# 3. SETUP THE GENETIC ALGORITHM
creator.create("FitnessMin", base.Fitness, weights=(-1.0, ))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()

toolbox.register ("indices", random.sample, range(NUMBER_OF_CITIES), NUMBER_OF_CITIES) ## permutation setup for indiviual
toolbox.register ("individual", tools.initIterate, creator.Individual, toolbox.indices)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# 4. FITNESS, MATE, MUTATE METHODS
def EVALUATE (individual):
  summation = 0
  start = individual[0]
  for i in range (1, len(individual)):
    end = individual[i]
    summation += distances[start][end]
    start = end
  return summation,
  
toolbox.register("evaluate", EVALUATE)
toolbox.register("mate", tools.cxOrdered ) #cxOrdered es otra forma o cxPartialyMatched
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.02)
toolbox.register("select", tools.selTournament, tournsize=3)


def main (seed = 0):
  random.seed(seed)
  pop = toolbox.population(n=200)
  hof = tools.HallOfFame(1)
  stats = tools.Statistics(lambda ind: ind.fitness.values)
  stats.register("Avg", np.mean)
  # stats.register("Std", np.std)
  stats.register("Min", np.min)
  stats.register("Max", np.max)

  algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.5, ngen=10, stats=stats, halloffame=hof,verbose=True)
  
  return pop, stats, hof

def calculateCost (ar):
  ans = 0
  for i in range(NUMBER_OF_CITIES-1):
    a = ar[i]
    b = ar[(i+1)%NUMBER_OF_CITIES]
    print(a+1,b+1,distances[a][b])
    ans += (distances[a][b])
  return ans

if __name__ == "__main__":
  # distances[4][2] = distances[2][4] = 100000
  pop, stats, hof = main()
  # print(pop)
  # print(hof)
  print(hof[0])
  print("min cost: ",calculateCost(hof[0]))
  print(distances)