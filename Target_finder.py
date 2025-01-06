def search(target, size_hex):
    q = target / size_hex 
    q = float( '0.' + str(q).split('.')[1])
    return(q)

n = []
max_list = []
x = 128
f = 1024
below = 0.0001
bit_range = 0xFFFFFFFFFF 
target = 0xe02b35a358f 

while f < 256000:
    n.append(f)
    f += 2

for i in range(len(n)):
    grid = n[i] * x
    size_hex = bit_range / grid
    size_hex = round(size_hex)
    cmax = search(target, size_hex)
    max_list.append(cmax)
    if cmax <= below:
        print(f"Below {below} {n[i]}\t Biggest = {cmax}\n")

print(f"Time to Find")
print(f"Smallest: {min(max_list)}")
print(f"Avg: {sum(max_list) / len(max_list)}")
