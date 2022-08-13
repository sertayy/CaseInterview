clocks = []

for i in range(1, 13):
    for j in range(60):
        clocks.append("{0}:{1}\n".format(i, j))

with open("time.csv", "w") as outfile:
    outfile.write("time\n")
    outfile.writelines(clocks)
