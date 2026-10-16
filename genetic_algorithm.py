import random

from flower import Flower

def generate_population():
    population = []

    for i in range(8):
        dna = [random.randint(20,30),
               random.randint(0,255),
               random.randint(0,255),
               random.randint(0,255),
               random.randint(0,255),
               random.randint(0,255),
               random.randint(0,255),
               random.randint(0,7),
        ]

        flower = Flower(dna)
        population.append(flower)

    return population

def selection(population):
    total = 0
    for flower in population:
        total += flower.fitness()

    x = random.uniform(0,total)
    running_total = 0

    for flower in population:
        running_total += flower.fitness() 
        if running_total > x :
            return flower
    return population[-1]

def crossover(f1 , f2):
    dna1 = f1.dna
    dna2 = f2.dna
    point = random.randint(1,7)
    child1_dna = dna1[:point]+dna2[point:]
    child2_dna = dna2[:point]+dna1[point:]

    child1 = Flower(child1_dna)
    child2 = Flower(child2_dna)
    return child1, child2

def mutate(flower):
    dna = flower.dna
    point = random.randint(0,7)
    if point == 0:
        dna[point] = random.randint(20,30)
    elif point == 7:
        dna[point] = random.randint(0,7)
    else:
        dna[point] = random.randint(0,255)

    return Flower(dna)

def create_new_population(population):
    new_population = []
    for i in range(4):
        f1 = selection(population)
        f2 = selection(population)
        child1, child2 = crossover(f1,f2)
        result1 = mutate(child1)
        result2 = mutate(child2)
        new_population.append(result1)
        new_population.append(result2)

    return new_population
