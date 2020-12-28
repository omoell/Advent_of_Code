with open('1a-input.txt', 'r') as f:
    expenses = f.readlines()
    expenses = [int(x.replace('\n', '')) for x in expenses]

# print(file)

# expenses = [1721
#            , 979
#            , 366
#            , 299
#            , 675
#            , 1456
#           ]

expenses_dict = {}

for expense in expenses:
    if expense in expenses_dict:
        relevant_expense = expense
        break
    else:
        residual = 2020 - expense
        expenses_dict[residual] = expense

print(f'Expense A: {relevant_expense}')
print(f'Expense B: {expenses_dict[relevant_expense]}')
print(f'Result: {relevant_expense * expenses_dict[relevant_expense]}')
