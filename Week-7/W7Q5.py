def read_employees(file_path):
    employees = []
    with open(file_path, 'r') as file:
        next(file)  # Skip header
        for line in file:
            name, eid, salary, did = line.strip().split(',')
            employees.append({
                'Name': name,
                'EId': int(eid),
                'Salary': float(salary),
                'DID': int(did)
            })
    return employees

def read_departments(file_path):
    departments = {}
    with open(file_path, 'r') as file:
        next(file)  # Skip header
        for line in file:
            did, dname, dlocation = line.strip().split(',')
            departments[int(did)] = {
                'DName': dname,
                'DLocation': dlocation
            }
    return departments

def calculate_average_salary(employees):
    salary_sum = {}
    employee_count = {}
    
    for emp in employees:
        did = emp['DID']
        salary = emp['Salary']
        
        if did not in salary_sum:
            salary_sum[did] = 0
            employee_count[did] = 0
            
        salary_sum[did] += salary
        employee_count[did] += 1
        
    average_salaries = {}
    for did in salary_sum:
        average_salaries[did] = salary_sum[did] / employee_count[did]
    
    return average_salaries

def main():
    employees = read_employees('employees.txt')
    departments = read_departments('departments.txt')
    
    average_salaries = calculate_average_salary(employees)

    for did, avg_salary in average_salaries.items():
        if did in departments:
            print(f"Department: {departments[did]['DName']}, Average Salary: RS -{avg_salary:.2f}")

if __name__ == "__main__":
    main()
