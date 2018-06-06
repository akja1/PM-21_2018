# Perseus, Pegasus und Andromeda: eine Variante des Ziegenproblems
#
# siehe Seite 7 in:
# www.school-scout.de/vorschau/62770/mathematische-spiele-und-strategien-22012.pdf

import random

def choices(seq, k):
    result = []
    for n in range(k):
        result.append(random.choice(seq))
    return result

# set up the three caves
caves = [1,2,3]
# initialize counters for the two possible outcomes
counter_andromeda_in_original_cave = 0
counter_andromeda_in_third_cave = 0

trials = 10000

for trial in range(trials):
    cave = set(caves)
    andromeda_cave = random.choice(list(cave))
    
    perseus_first_choice = random.choice(list(cave))
    
    cave.discard(andromeda_cave)
    cave.discard(perseus_first_choice)
    pegasus_comment = random.choice(list(cave))

    if perseus_first_choice == andromeda_cave:
        counter_andromeda_in_original_cave += 1
    else:
        counter_andromeda_in_third_cave += 1

# report results of simulation
print(
    'Reconsidering his original choice would have been good for Perseus in '
    '{0} out of {1} cases.'
    .format(counter_andromeda_in_third_cave, trials)
    )
