print("===================================")
print("      EMPLOYEE PAYROLL SYSTEM      ")
print("===================================")

employees = []   # list to store employee data

def calculate_salary(basic_salary):
    hra = 0.20 * basic_salary
    da = 0.10 * basic_salary
    pf = 0.12 * basic_salary
    tax = 0.05 * (basic_salary + hra + da)
    net_salary = basic_salary + hra + da - pf - tax
    return net_salary

while True:
    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Generate Payroll")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        designation = input("Enter Designation: ")
        basic_salary = float(input("Enter Basic Salary: "))

        employee = {
            "id": emp_id,
            "name": name,
            "designation": designation,
            "basic": basic_salary
        }

        employees.append(employee)
        print("✅ Employee added successfully")

    elif choice == "2":
        print("\n--- Employee List ---")
        for emp in employees:
            print(emp)

    elif choice == "3":
        emp_id = input("Enter Employee ID to generate payroll: ")
        found = False

        for emp in employees:
            if emp["id"] == emp_id:
                net_salary = calculate_salary(emp["basic"])
                print("\n--- Salary Slip ---")
                print("Name:", emp["name"])
                print("Designation:", emp["designation"])
                print("Net Salary:", net_salary)
                found = True
                break

        if not found:
            print("❌ Employee not found")

    elif choice == "4":
        print("Exiting Payroll System...")
        break

    else:
        print("❌ Invalid choice. Try again.")
