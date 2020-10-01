def find_lucky(lst):
    out = []
    d = {x: lst.count(x) for x in lst}
    a, b = list(d.keys()), list(d.values())
    print(a, b)
    for i in range(0, len(a)):
        if a[i] == b[i]:
            out.append(a[i])
    return max(out)

print(find_lucky(lst=[1,2,2,3,3,3,4,4,4,4]))