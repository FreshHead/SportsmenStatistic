from operator import itemgetter
sportsmen = [["Баландин", "С", 123.7, 2],
             ["Шишков", "Ш", 79.98, 3],
             ["Кравченко", "Д", 134.8, 1]]

sportsmen.sort(key=itemgetter(3))

for i in range(0, len(sportsmen)):
    sportsmen[i].__setitem__(3, i+1)
