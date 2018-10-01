import tn_header_files
numbers = []
targets = []
number = int
target = int
i = int
j = int
result = ""
numbers = [2, 7, 11, 15]
print("***Numbers:***")
for i, number in enumerate(numbers):
    print("[{}] = {}\n".format(i, number))
targets = [9, 13, 17, 18, 22, 26]
target = tn_header_files.random.choice(targets)
print("***Target:***")
print(target, "\n")
result = tn_header_files.total(numbers, target)
print(result)
