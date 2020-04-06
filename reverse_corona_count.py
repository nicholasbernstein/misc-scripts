#!/usr/bin/env python 
doublingInDays = 3
mortalityRate = .027
deathCount = 7020
lag = 20

count = int(deathCount / mortalityRate)
iterations = (lag/doublingInDays)
print("Infected Now:", count, "Dead: ", deathCount)
for x in range(1, int(iterations)):
   count=(count*2)
   projected_deaths=int(count*mortalityRate)
   print("Infected ", lag-(x*3), "days ago:", count, "( deaths in ", x*3, "days: ", projected_deaths, ")" )

