import time

# set count-down time in second
count_down = 10
for i in range(count_down, 0, -1):
    msg = u"\rThe system will exit in " + str(i) + " second(s)."
    print(msg, end="")
    time.sleep(1)

# to cover everything displaying in last step
end_msg = "End." + "  "*(len(msg)-len("End."))

print(u"\r"+end_msg)
