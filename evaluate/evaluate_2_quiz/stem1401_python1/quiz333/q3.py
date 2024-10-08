"""
quiz 333
q3

Average Temperature: 22.2°C
Highest Temperature: 25.0°C
Lowest Temperature: 19.5°C

"""

temperature_data = [22.5, 21.0, 23.5, 25.0, 20.0, 19.5, 24.0]

total_temp = 0
highest_temp = temperature_data[0]
lowest_temp = highest_temp

for temp in temperature_data:
    total_temp += temp
    if temp > highest_temp:
        highest_temp = temp
    if temp < lowest_temp:
        lowest_temp = temp

avg_temp = total_temp/len(temperature_data)
print(f"Average Temperature: {avg_temp:.1f}°C")
print(f"Highest Temperature: {highest_temp:.1f}°C")
print(f"Lowest Temperature: {lowest_temp:.1f}°C")
