from random import randint, choice
from vectortools import *
from foodclasses import *


class Diet:

  def __init__(self, calories, totalFat, saturatedFat, carbohydrates, protein):
    self.calories = int(calories)
    self.vector = [float(totalFat), float(saturatedFat), float(carbohydrates), float(protein)]


class DietGen:

  def __init__(self, foods, targetDiet, populationSize):
    self.foods = foods
    self.genes = foods.getItemSymbols()
    self.target = targetDiet.vector
    self.cals = targetDiet.calories
    self.popSize = populationSize
    self.generation = 1
    self.population = self.randomPopulation()
    
  def randomPopulation(self):
    pop = []
    n = len(self.genes) - 1
    for i in range(self.popSize):
      g = ""
      for j in range(self.cals):
        g += choice(self.genes)
      pop.append(g)
    return pop
    
  def evaluate(self, genome):
    coefficients = [genome.count(g) for g in self.genes] # get food item coefficients
    vectors = [self.foods.getItemBySymbol(s).getUnit() for s in self.genes] # get food item unit vectors
    vectors = [scale(vectors[i], coefficients[i]) for i in range(len(self.genes))] # scale up vectors with coefficients
    result = vectorSum(vectors)
    return cosine(result, self.target)
    
  # sort population by fitness in descending order
  def rankFitness(self):
    lookup = {}
    for g in self.population: # build a dictionary to associate a genome with its fitness
      lookup[self.evaluate(g)] = g 
    sortedKeys = sorted(list(lookup.getKeys()))
    self.population = [lookup[g] for g in sortedKeys][::-1]
    
  def mutate(self, gene):
    p = randint(0, self.cals - 1)
    s = choice(self.genes)
    return gene[:p] + s + gene[p + 1]
    
  def crossover(self, a, b):
    c = self.cals / 20
    p = randint(c, c * 19)
    c = a[:p] + b[p:]
    d = b[:p] + a[p:]
    return [c, d]

  def mate(self, a, b, crossovers, mutations):
    for i in range(crossovers):
      a, b = self.crossover(a, b)
    for i in range(mutations):
      a = self.mutate(a)
      b = self.mutate(b)
    return [a, b]
    
  def evolve(self, crossovers, mutations, nGenerations=1):
    # get top genes
    self.rankFitness()
    topgenes = int(sqrt(self.popSize)) + 1
    # kill off weak genes
    self.population = self.population[:topgenes]
    # repopulate
    for i in range(1, topgenes - 1):
      for j in range(i, topgenes):
        self.population += mate(self.population[i], self.population[j], crossovers, mutations)
    # trim down population
    self.population = self.population[:self.popSize]
    self.generation += 1
    
  def printBest(self):
    pass

    
    
    
    
    
    
    
    