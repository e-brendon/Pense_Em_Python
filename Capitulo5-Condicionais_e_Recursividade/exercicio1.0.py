def print_n (v, c):
    if c <= 0:
        return
    print(v)
    print_n(v, c-1)

s
print_n("Ola mundo",3)
