
number1 = float(input("Enter first number: "))
operator = input("Enter operator")
number2 = float(input("Enter second number: "))


if operator == '+':
  result = number1 + number2
  print(operator)
elif operator == '-':
  result = number1 - number2
  print(operator)
elif operator == '/':
  result = number1 / number2
  print(operator)
elif operator == '%':
  result = number1 % number2
  print(operator)
elif operator == '*':
  result = number1 * number2
  print(operator)
