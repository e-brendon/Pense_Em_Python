
def print_n(s, n):
    if n <=0:
        return
    print(f"Exec {n} string {s}")
    print_n(s, n-1)
print_n("teste", 5)