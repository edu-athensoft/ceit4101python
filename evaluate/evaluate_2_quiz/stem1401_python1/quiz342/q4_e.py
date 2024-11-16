days_amount = 10
start = 1
peaches_per_day = 1.5

while start < days_amount+1:
    peaches_total = peaches_per_day * start
    start += 1

print(f"The monkey picked {peaches_total:0.0f} peaches.")