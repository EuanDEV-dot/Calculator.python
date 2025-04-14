continue_calculating = True

while continue_calculating:
  number1 = input('Whats the first number?')
  number2 = input('Whats the second number?')
  signthingy = input('Do you want to add (+), subtract (-), multiply (*) or divide (/)?')
  if(signthingy == '+'):
    solution_add = int(number1) + int(number2)
    print(solution_add)
  if(signthingy == '-'):
    solution_sub = int(number1) - int(number2)
    print(solution_sub)
  if(signthingy == '*'):
    solution_mul = int(number1) * int(number2)
    print(solution_mul)
  if(signthingy == '/'):
    solution_div = int(number1) / int(number2)
    print(solution_div)
  question = input('Do you want to calculate something else? (y/n) ')
  if question.lower() != 'y' and question.lower() != 'yes':
    print('Ok bye!')
    break