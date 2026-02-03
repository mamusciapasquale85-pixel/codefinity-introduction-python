meat = ["Ham", 3.99, 50, "Sliced"]
cheese = ["Cheddar", 5.49, 100, "Sharp"]
deli_dept = [meat, cheese]
print("Initial Deli list:", deli_dept)
if meat[2] < 100 :
    meat[2]=100
deli_dept.sort()
print("Updated Deli List: <deli_dept>")