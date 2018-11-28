print("     ",end="")
for colidx in range(16):
    if colidx > 0:
        print("%5d|"%colidx,end="")

print()
print("------"*17)
for rowidx in range(16):
    if rowidx > 0:
        print("%5d|"%rowidx,end="")
        for colidx in range(16):
            if colidx > 0:
                print("%5d|"%(rowidx*colidx),end = "")
        print()