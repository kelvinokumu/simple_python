import statistics

dataset = [25, 28, 30, 22, 26]
mean_abs_dev = statistics.mean([abs(x - statistics.mean(dataset)) for x in dataset])
print("Mean Absolute Deviation:", mean_abs_dev)

