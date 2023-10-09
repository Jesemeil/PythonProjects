def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


def main():
    try:
        num1 = int(input("Enter the first positive integer: "))
        num2 = int(input("Enter the second positive integer: "))

        if num1 > 0 and num2 > 0:
            result = lcm(num1, num2)
            print("The least common multiple of", num1, "and", num2, "is:", result)
        else:
            print("Both numbers should be positive integers.")
    except ValueError:
        print("Invalid input. Please enter positive integers.")


if __name__ == "__main__":
    main()
