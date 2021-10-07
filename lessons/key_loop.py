"""In class lesson on dict"""

schools = {}
print(schools)

schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)

for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")