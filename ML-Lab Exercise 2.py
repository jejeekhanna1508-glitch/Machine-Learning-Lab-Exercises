
import csv
import os
from itertools import product

# Create the CSV file automatically
folder = r"E:\SIMATS PROJECTS"
os.makedirs(folder, exist_ok=True)
file_path = os.path.join(folder, "training.csv")

sample_data = [
    ["Sky", "Temperature", "Humidity", "Wind", "EnjoySport"],
    ["Sunny", "Warm", "Normal", "Strong", "Yes"],
    ["Sunny", "Warm", "High", "Strong", "Yes"],
    ["Rainy", "Cold", "High", "Strong", "No"],
    ["Sunny", "Warm", "High", "Weak", "Yes"]
]

with open(file_path, "w", newline="") as file:
    csv.writer(file).writerows(sample_data)

print("CSV file created successfully!")

# Read CSV data
with open(file_path, "r", newline="") as file:
    data = list(csv.reader(file))

attributes = data[0][:-1]
examples = data[1:]

domains = [
    sorted(set(row[i] for row in examples))
    for i in range(len(attributes))
]

# Generate all hypotheses
all_hypotheses = product(
    *[[*domain, "?"] for domain in domains]
)

# Find all hypotheses consistent with the data
version_space = []

for h in all_hypotheses:
    valid = True

    for row in examples:
        x = row[:-1]
        target = row[-1]
        prediction = all(
            h[i] == "?" or h[i] == x[i]
            for i in range(len(h))
        )

        if (target == "Yes" and not prediction) or \
           (target == "No" and prediction):
            valid = False
            break

    if valid:
        version_space.append(h)

# Display consistent hypotheses
print("\nAll Consistent Hypotheses:")
for h in version_space:
    print(list(h))

print("\nTotal Consistent Hypotheses:", len(version_space))
