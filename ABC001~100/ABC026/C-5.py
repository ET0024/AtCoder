def salary(n):
    # return salary of person(n)
    if len(staffs[n]) == 0:
        return 1
    else:
        staffs_salary = []
        for staff in staffs[n]:
            staffs_salary.append(salary(staff))
        return max(staffs_salary) + min(staffs_salary) + 1


n = int(input())
staffs = [[] for _ in range(n)]
for idx in range(n - 1):
    boss = int(input()) - 1
    staff = idx + 1
    staffs[boss].append(staff)

print(salary(0))