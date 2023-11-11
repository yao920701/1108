print("----------------------------")
print("        員工薪資輸入        ")
print("   若姓名處未輸入則代表結束   ")
print("----------------------------")

employee_records = []

while True:
    eName = input("請輸入姓名:")
    if not eName:
        break
    
    eSalary = int(input("請輸入薪資:"))
    print(" ")
    
    record = {"eName": eName, "eSalary": eSalary}
    employee_records.append(record)

total_salary = sum(record["eSalary"] for record in employee_records)
average_salary = total_salary / len(employee_records) if len(employee_records) > 0 else 0

print("----------------------------")
if len(employee_records) > 0:
    for record in employee_records:
        print(f'員工{record["eName"]} 的薪資為 {record["eSalary"]:,.0f}')
else:
    print(" ")

print("----------------------------")
print(f"合計薪資：{total_salary:>13,}")
print(f'平均薪資：{average_salary:>13.2f}')
print("============================")
