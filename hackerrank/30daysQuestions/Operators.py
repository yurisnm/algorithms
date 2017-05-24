
mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

print(int(round(mealCost+(mealCost*tipPercent/100.0)+(mealCost*taxPercent/100.0))))
