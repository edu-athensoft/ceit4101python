def find_total_peaches():
    day = 10  # Start from day 10 when there's only 1 peach left
    peaches = 1  # On the 10th day, 1 peach remains

    while day > 1:
        peaches = (peaches + 1) * 2  # Reverse the process to find the peaches on the previous day
        day -= 1  # Move to the previous day

    return peaches

# Output the result
total_peaches = find_total_peaches()
print(f"The total number of peaches on the first day was: {total_peaches}")