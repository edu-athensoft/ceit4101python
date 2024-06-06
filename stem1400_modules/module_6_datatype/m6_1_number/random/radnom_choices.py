"""
usage of random.choices()

random.choices(population, weights=None, cum_weights=None, k=1)
"""
import random

k = 100
normal_chance = 0.638 * k
magic_chance = 0.25 * k
rare_chance = 0.10 * k
leg_chance = 0.01 * k
aleg_chance = 0.002 * k

list_rarity = ["normal", "magic", "rare", "legendary", "ANCIENT LEGENDARY!"]
list_chance = [normal_chance, magic_chance, rare_chance, leg_chance, aleg_chance]

results = random.choices(list_rarity, list_chance, k=k)
# test by results
print(results)
