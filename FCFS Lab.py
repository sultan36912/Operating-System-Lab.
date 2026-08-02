processes = [
    ["P0", 3, 1],
    ["P1", 5, 3],
    ["P2", 2, 2],
    ["P3", 1, 2],
    ["P4", 6, 3]
]

processes.sort(key=lambda x: x[1])

time = 0
result = []

print("Gantt Chart:")

for p in processes:
    pid, at, bt = p

    if time < at:
        print(f"| Idle ({time}-{at}) ", end="")
        time = at

    start = time
    ct = start + bt
    tat = ct - at
    wt = tat - bt

    result.append([pid, at, bt, ct, tat, wt])

    print(f"| {pid} ({start}-{ct}) ", end="")
    time = ct

print("|")

print("\nProcess\tAT\tBT\tCT\tTAT\tWT")

total_tat = 0
total_wt = 0

for r in result:
    print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]}")
    total_tat += r[4]
    total_wt += r[5]

n = len(result)

print("\nAverage Turnaround Time =", total_tat / n)
print("Average Waiting Time =", total_wt / n)
