mydict = { 1: "London", 2: "Tokoy", 3: "Bankok" }

mydict = { "L": "London", "B": "Bankok", "T": "Tokoy" }

print(mydict)

print("mydict[L] = ", mydict['L']);


mydict = { 1: "London", "B": "Bankok", 3: "Tokoy" }

print(mydict['B'])


ka = 1
kb = 2
kc = 3

mydict = { ka: "London", kb: "Bankok", kc: "Tokoy" }

print(mydict[ka])
print(mydict[kb])
print(mydict[kc])



ka = 1
kb = 2
kc = 3

va = "London"
vb = "Bankok"
vc = "Tokoy"

mydict = { ka: va, kb: vb, kc: vc }

print(mydict[ka])
print(mydict[kb])
print(mydict[kc])

mydict = {(ka,va), (kb,vb), (kc,vc)}
print(mydict)
print(type(mydict))
print(type((ka,va)))
