def main():

  firstNumber = input("Enter the first number: ")
  secondNumber = input("Enter the second number: ")
  operation = input("Choose one of the operations (*, /, +, -) ")
  if firstNumber.isdigit() and secondNumber.isdigit():
    firstNumber = int(firstNumber)
    secondNumber = int(secondNumber)
    if operation == "*":
        print("The answer is {}".format(firstNumber * secondNumber))
    elif operation == "/":
        print("The answer is {}".format(firstNumber / secondNumber))
    elif operation == "+":
        print("The answer is {}".format(firstNumber + secondNumber))
    elif operation == "-":
        print("The answer is {}".format(firstNumber - secondNumber))
    else:
        print("Invalid Operation!")
  else:
    print("Invalid Numbers!")

if __name__ == '__main__':
	main()
