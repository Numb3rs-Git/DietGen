from math import sqrt
from random import randint, shuffle

# vectors are [grams of food, calories, total fat, badFat, carbohydrates, protein]
CHICKEN       = [100.0, 120.0, 2.00, 1.00, 0.00, 23.0]
OATS          = [35.00, 130.0, 3.50, 0.50, 22.0, 5.00]
PEANUT_BUTTER = [15.00, 90.00, 7.00, 1.00, 3.00, 4.00]
CHEESE        = [30.00, 110.0, 9.00, 0.90, 1.00, 8.00]
POWDER        = [32.00, 120.0, 1.50, 1.00, 3.00, 24.0]
SWEET_POTATO  = [100.0, 86.00, 0.10, 0.00, 20.0, 1.60]
BROCCOLI      = [85.00, 25.00, 0.00, 0.00, 5.00, 3.00]
EGG           = [53.00, 70.00, 5.00, 1.50, 1.00, 6.00]
FOOD_ITEMS = {"K" : CHICKEN, "O" : OATS, "B" : PEANUT_BUTTER, "C" : CHEESE, "P" : POWDER, "S" : SWEET_POTATO}


# convert vectors to values per calorie (and remove calorie column)
for i in "KOBCPS":
  temp = []
  for j in FOOD_ITEMS[i]:
    temp.append(j / FOOD_ITEMS[i][1]))
  FOOD_ITEMS[i] = temp[:1] + temp[2:]
 
  
TARGET_CALORIES = 1600
TARGET_DIET   = [52.0000, 5.00000, 190.000, 120.000]
      
      
def getFitness(genome):
  diet = [0, 0, 0, 0]
  for i in genome:
    diet = add(diet, FOOD_ITEMS[i][1:])
  return cosine(diet, TARGET_DIET)    
      
      
def randomNucleotide():
  return "KOBCPS"[randint(0, 5)]


def randomGenome(length):
  return "".join([randomNucleotide() for i in range(length)])
  
  
def mutate(genome, nMutations):
  locations = []
  newGene = genome[:]
  for i in range(nMutations):
    loc = randint(0, len(genome) - 1)
    if loc not in locations:
      locations.append(loc)
      newGene = newGene[:loc] + randomNucleotide() + newGene[loc + 1:]
  return newGene
  
  
def crossover(a, b):
  if len(a) != len(b):
    return None
  else:
    crossPoint = randint(0, len(a) - 1)
    newGene = a[:crossPoint] + b[crossPoint:]
    return newGene