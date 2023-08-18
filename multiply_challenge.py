import random

def generate_random_number():
    return random.randint(1, 9)

def multiply_numbers(a, b):
    return a * b

def print_result(a, c):
    print(f"Randomly generated A: {a}")
    print(f"A multiplied by B: {c}")

def main():
    print("Welcome to the Multiply Challenge!")
    
    while True:
        A = generate_random_number()
        B = generate_random_number()
        C = multiply_numbers(A, B)
        
        print("\nGenerating a new challenge...")
        print_result(A, C)
        
        if C == 4:
            print("\nChallenge completed!")
            print(f"Success! A: {A}, B: {B}")
            break

if __name__ == "__main__":
    main()
