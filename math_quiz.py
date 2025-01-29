import random
import time

OPERATORS = ["+", "-", "*", "/"]
MIN_OPERAND = 2
MAX_OPERAND = 15
TOTAL_PROBLEMS = 10

def generate_problem():
    while True: 
        left = random.randint(MIN_OPERAND, MAX_OPERAND)
        right = random.randint(MIN_OPERAND, MAX_OPERAND)
        operator = random.choice(OPERATORS)

        if operator == "/":
            if left % right == 0:
                expr = str(left) + " " + operator + " " + str(right)
                answer = eval(expr)
                return expr, answer
        else:
            expr = str(left) + " " + operator + " " + str(right)
            answer = eval(expr)
            return expr, answer

wrong = 0
input("Press enter to start!")
print('____________')

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Question #" + str(i + 1) + ": " + expr + ' = ')
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("_________")
print("Good job you finished in", total_time, "seconds!")
