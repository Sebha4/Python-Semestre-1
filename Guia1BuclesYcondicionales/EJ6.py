s=0
m=0
h=0

while h < 24:
    while m < 60:
        while s < 60:
            print(f"{h}:{m}:{s}")
            s += 1
        s = 0
        m += 1
    m = 0
    h += 1