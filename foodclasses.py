from copy import deepcopy


class FoodItem:

  def __init__(self, name, grams, calories, totalFat, saturatedFat, carbohydrates, protein):
    
    assert isinstance(name, str)
    self.name = name
    cals = float(calories)
    self.vector = [float(totalFat), float(saturatedFat), float(carbohydrates), float(protein)]
    self.gramsPerCalorie = float(grams) / cals
    
    # convert values to per calorie
    for i in range(4):
      self.vector[i] /= cals
      
  # returns one calorie worth of macronutrients as a vector
  def getUnit(self):
    return self.vector
    
  # returns the mass of the specified number of calories for this food item
  def getMass(self, calories):
    return self.gramsPerCalorie * calories


class FoodLibrary:

  def __init__(self):
    self.list = {}
    self.symbolLookup = {}
    
  # adds an item to the library
  # returns true if added, false otherwise
  def add(self, item):
    
    if self.count() >= 100 or not isinstance(item, FoodItem):
      return False
      
    if not isinstance(item.name, str) or item.name.lower() in self.symbolLookup:
      return False
    
    nextKey = chr(len(self.list) + 32) # generate next key
    self.symbolLookup[item.name.lower()] = nextKey
    self.list[nextKey] = deepcopy(item)
    return True

  # removes an item from the list by symbol
  # returns true if item existed, false otherwise
  def removeBySymbol(self, symbol):  
    if symbol in self.list:
      name = self.list[symbol].name
      del self.list[symbol]
      del self.symbolLookup[name]
      return True
    else:
      return False
    
  # removes an item from the list by name
  # returns true if item existed, false otherwise
  def removeByName(self, name):  
    if name.lower() in self.symbolLookup:
      del self.list[self.symbolLookup[name.lower()]]
      del self.symbolLookup[name]
      return True
    else:
      return False
    
  def getItemSymbols(self):
    return "".join(list(self.list.keys()))
    
  def getItemNames(self):
    return list(self.symbolLookup.keys())
    
  def getItemBySymbol(self, code):
    if code in self.list:
      return deepcopy(self.list[code])
    else:
      return None
    
  def getItemByName(self, name):
    if name.lower() in self.symbolLookup:
      return deepcopy(self.list[self.symbolLookup[name.lower()]])
    else:
      return None
    
  def count(self):
    return len(self.list)