def salary(i):
    if len(buka[i]) == 0:
        return 1
    else:
        staff_list = buka[i]
        salary_list = []
        for staff in staff_list:
            salary_list.append(salary(staff))

        return max(salary_list) + min(salary_list) + 1


n = int(input())
buka = [[] for _ in range(n)]
for i in range(n - 1):
    boss = int(input()) - 1
    staff = i + 1
    buka[boss].append(staff)

print(salary(0))