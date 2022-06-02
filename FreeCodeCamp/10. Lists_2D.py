# 2 Dimensional List

full_age_dataset = [
    ["Amy", 23],
    ["John", 17],
    ["Lily", 15],
    ["Ben", 21],
    ["Sam", 16],
    ["Jim", 18]
]

underage_count = 0
underage_name = []

for age_dataset in full_age_dataset:

    if(age_dataset[1] < 18):
        underage_count += 1
        underage_name.append(age_dataset[0])
    else:
        continue

print("There are %d underage people. They are:" % underage_count)   # There are 3 underage people. They are:
print(underage_name)                                                # ['John', 'Lily', 'Sam']

