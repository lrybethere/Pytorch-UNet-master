with open('HEDiou.txt', 'r') as f:
    lines = f.readlines()
    acc_list = [float(line.strip()) for line in lines]

avg_acc = sum(acc_list) / len(acc_list)
print("Average Accuracy:", avg_acc)
