fibonacciNumbers = [1, 2];

fibonacciFlag = int(input("Insert the fibonacci number: "));

for i in range(fibonacciFlag):
    if fibonacciFlag <= len(fibonacciNumbers):
        break;
    if i >= 1:
        newFibonacci=fibonacciNumbers[i]+fibonacciNumbers[i-1];

        fibonacciNumbers.append(newFibonacci);


print("Fibonaccis: {}".format(fibonacciNumbers));
