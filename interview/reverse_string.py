# Q6
# reverse string
# using negative index

# -1,-2,...-len()
src_str= "athens"

# negative_index = [-(i+1) for i in range(0,len(src_str))]
# print(negative_index)

result = ""
for i in range(1, len(src_str)+1):
    # print(src_str[-i])
    result+=src_str[-i]

print(result)