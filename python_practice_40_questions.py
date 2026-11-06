"""
Python Practice Set - 40 Questions
Each question is a separate function: q1(), q2(), ... q40()
Run this file, then enter a question number (1-40) to run it.
Enter 0 to run nothing / 'q' to quit.
"""

import os
import random
import string
from datetime import datetime


# ---------------------------------------------------------------
# Helper functions for safe input
# ---------------------------------------------------------------
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter an integer.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid input. Please enter a number.")


# ===============================================================
# 1. DATA TYPES
# ===============================================================
def q1():
    """Find the data type of every value in a mixed list."""
    data = [10, 3.14, "hello", True, None, [1, 2], (3, 4), {5, 6}, {"a": 1}, 2 + 3j]
    for item in data:
        print(f"{item!r:15} -> {type(item).__name__}")


def q2():
    """Convert a nested list into a tuple of tuples."""
    def to_tuple(obj):
        if isinstance(obj, list):
            return tuple(to_tuple(x) for x in obj)
        return obj

    nested = [[1, 2, 3], [4, 5], [6, [7, 8]]]
    print("Nested list   :", nested)
    print("Tuple of tuple:", to_tuple(nested))


def q3():
    """Remove duplicates from a mixed list while preserving order."""
    data = [1, "a", 2, "a", 1, 3.5, 3.5, True, "b", 2, (1, 2), (1, 2), [1], [1]]
    result = []
    for x in data:
        # compare value AND type so that 1 and True are treated as different
        if not any(x == y and type(x) is type(y) for y in result):
            result.append(x)
    print("Original :", data)
    print("Unique   :", result)


# ===============================================================
# 2. OPERATORS
# ===============================================================
def q4():
    """Check whether a number is a power of 2 using operators."""
    n = get_int("Enter a number: ")
    if n > 0 and (n & (n - 1)) == 0:
        print(f"{n} is a power of 2")
    else:
        print(f"{n} is NOT a power of 2")


def q5():
    """Swap two numbers using bitwise XOR."""
    a = get_int("Enter first number : ")
    b = get_int("Enter second number: ")
    print(f"Before swap: a = {a}, b = {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After swap : a = {a}, b = {b}")


def q6():
    """Check whether a number is divisible by both 4 and 6."""
    n = get_int("Enter a number: ")
    if n % 4 == 0 and n % 6 == 0:
        print(f"{n} is divisible by both 4 and 6")
    else:
        print(f"{n} is NOT divisible by both 4 and 6")


def q7():
    """Calculate total electricity bill using different unit rates."""
    units = get_float("Enter units consumed: ")
    # Slabs: first 100 @ 5, next 100 @ 7, next 100 @ 10, above 300 @ 12
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100 * 5 + (units - 100) * 7
    elif units <= 300:
        bill = 100 * 5 + 100 * 7 + (units - 200) * 10
    else:
        bill = 100 * 5 + 100 * 7 + 100 * 10 + (units - 300) * 12
    print(f"Total electricity bill for {units} units = Rs. {bill:.2f}")


# ===============================================================
# 3. CONDITIONAL STATEMENTS
# ===============================================================
def q8():
    """Check whether three sides can form a triangle."""
    a = get_float("Side 1: ")
    b = get_float("Side 2: ")
    c = get_float("Side 3: ")
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        print("Valid triangle")
    else:
        print("Not a valid triangle")


def q9():
    """Determine the type of triangle."""
    a = get_float("Side 1: ")
    b = get_float("Side 2: ")
    c = get_float("Side 3: ")
    if not (a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a):
        print("Not a valid triangle")
    elif a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")


def q10():
    """Simple ATM menu (Withdraw, Deposit, Balance)."""
    balance = 10000.0
    while True:
        print("\n----- ATM MENU -----")
        print("1. Withdraw")
        print("2. Deposit")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            amt = get_float("Amount to withdraw: ")
            if amt <= 0:
                print("Invalid amount.")
            elif amt > balance:
                print("Insufficient balance.")
            else:
                balance -= amt
                print(f"Please collect your cash. Remaining balance: {balance:.2f}")
        elif choice == "2":
            amt = get_float("Amount to deposit: ")
            if amt <= 0:
                print("Invalid amount.")
            else:
                balance += amt
                print(f"Deposited. New balance: {balance:.2f}")
        elif choice == "3":
            print(f"Current balance: {balance:.2f}")
        elif choice == "4":
            print("Thank you for using the ATM.")
            break
        else:
            print("Invalid choice.")


def q11():
    """Calculate income tax based on slabs (illustrative slabs)."""
    income = get_float("Enter annual income: ")
    # Illustrative slabs (not official advice):
    # up to 3L: 0%, 3-7L: 5%, 7-10L: 10%, 10-12L: 15%, 12-15L: 20%, above 15L: 30%
    if income <= 300000:
        tax = 0
    elif income <= 700000:
        tax = (income - 300000) * 0.05
    elif income <= 1000000:
        tax = 400000 * 0.05 + (income - 700000) * 0.10
    elif income <= 1200000:
        tax = 400000 * 0.05 + 300000 * 0.10 + (income - 1000000) * 0.15
    elif income <= 1500000:
        tax = 400000 * 0.05 + 300000 * 0.10 + 200000 * 0.15 + (income - 1200000) * 0.20
    else:
        tax = (400000 * 0.05 + 300000 * 0.10 + 200000 * 0.15
               + 300000 * 0.20 + (income - 1500000) * 0.30)
    print(f"Income: Rs. {income:.2f}  ->  Tax: Rs. {tax:.2f}")


def q12():
    """Menu-driven calculator using if-elif."""
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Power")
    choice = input("Enter choice (1-6): ")
    a = get_float("First number : ")
    b = get_float("Second number: ")
    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        print("Result:", a / b if b != 0 else "Cannot divide by zero")
    elif choice == "5":
        print("Result:", a % b if b != 0 else "Cannot take modulus by zero")
    elif choice == "6":
        print("Result:", a ** b)
    else:
        print("Invalid choice")


# ===============================================================
# 4. LOOPS
# ===============================================================
def q13():
    """Print all prime numbers between 1 and n."""
    n = get_int("Enter n: ")
    primes = []
    for num in range(2, n + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print(f"Primes between 1 and {n}:", primes)


def q14():
    """Factorial of a number using a loop."""
    n = get_int("Enter a number: ")
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"Factorial of {n} = {fact}")


def q15():
    """Print Fibonacci series up to n terms."""
    n = get_int("Enter number of terms: ")
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    print("Fibonacci series:", series)


def q16():
    """Check whether a number is an Armstrong number."""
    n = get_int("Enter a number: ")
    digits = str(abs(n))
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    if total == abs(n):
        print(f"{n} is an Armstrong number")
    else:
        print(f"{n} is NOT an Armstrong number")


def q17():
    """Reverse a number and check if it is a palindrome."""
    n = get_int("Enter a number: ")
    original = n
    rev = 0
    temp = abs(n)
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    print("Reversed number:", rev)
    if original >= 0 and rev == original:
        print(f"{original} is a palindrome")
    else:
        print(f"{original} is NOT a palindrome")


def q18():
    """Greatest Common Divisor (GCD) of two numbers."""
    a = get_int("Enter first number : ")
    b = get_int("Enter second number: ")
    x, y = abs(a), abs(b)
    while y != 0:
        x, y = y, x % y
    print(f"GCD of {a} and {b} = {x}")


# ===============================================================
# 5. FUNCTIONS
# ===============================================================
def is_palindrome(s):
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]


def q19():
    """Function to check if a string is a palindrome."""
    s = input("Enter a string: ")
    if is_palindrome(s):
        print(f'"{s}" is a palindrome')
    else:
        print(f'"{s}" is NOT a palindrome')


def count_vowels_consonants(s):
    vowels = consonants = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


def q20():
    """Function to count vowels and consonants in a string."""
    s = input("Enter a string: ")
    v, c = count_vowels_consonants(s)
    print(f"Vowels: {v}, Consonants: {c}")


def calculate_interest(principal, rate, time, n=1):
    simple = (principal * rate * time) / 100
    compound = principal * (1 + rate / (100 * n)) ** (n * time) - principal
    return simple, compound


def q21():
    """Function to calculate simple and compound interest."""
    p = get_float("Principal amount: ")
    r = get_float("Rate of interest (% per year): ")
    t = get_float("Time (years): ")
    si, ci = calculate_interest(p, r, t)
    print(f"Simple Interest   = {si:.2f}")
    print(f"Compound Interest = {ci:.2f} (compounded annually)")


def get_factors(n):
    return [i for i in range(1, n + 1) if n % i == 0]


def q22():
    """Function to return all factors of a number."""
    n = get_int("Enter a positive number: ")
    if n <= 0:
        print("Please enter a positive number.")
        return
    print(f"Factors of {n}:", get_factors(n))


def second_largest(lst):
    unique = sorted(set(lst))
    if len(unique) < 2:
        return None
    return unique[-2]


def q23():
    """Function to find the second-largest number in a list."""
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    result = second_largest(nums)
    if result is None:
        print("Not enough distinct elements.")
    else:
        print("Second largest:", result)


# ===============================================================
# 6. LISTS
# ===============================================================
def q24():
    """Merge two lists without duplicates."""
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 5, 6, 7, 8]
    merged = l1 + [x for x in l2 if x not in l1]
    print("List 1:", l1)
    print("List 2:", l2)
    print("Merged (no duplicates):", merged)


def q25():
    """Find second-largest and second-smallest elements."""
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    unique = sorted(set(nums))
    if len(unique) < 2:
        print("Need at least two distinct numbers.")
        return
    print("Second smallest:", unique[1])
    print("Second largest :", unique[-2])


def q26():
    """Rotate a list to the left by k positions."""
    lst = list(map(int, input("Enter list elements separated by space: ").split()))
    k = get_int("Enter k: ")
    if not lst:
        print("List is empty.")
        return
    k = k % len(lst)
    rotated = lst[k:] + lst[:k]
    print("Original:", lst)
    print(f"Rotated left by {k}:", rotated)


def q27():
    """Separate even and odd numbers into two lists."""
    nums = list(map(int, input("Enter numbers separated by space: ").split()))
    evens = [x for x in nums if x % 2 == 0]
    odds = [x for x in nums if x % 2 != 0]
    print("Even numbers:", evens)
    print("Odd numbers :", odds)


def q28():
    """Find common elements between two lists."""
    l1 = list(map(int, input("Enter first list : ").split()))
    l2 = list(map(int, input("Enter second list: ").split()))
    common = []
    for x in l1:
        if x in l2 and x not in common:
            common.append(x)
    print("Common elements:", common)


# ===============================================================
# 7. TUPLES & SETS
# ===============================================================
def q29():
    """Count the frequency of each element in a tuple."""
    t = (1, 2, 2, 3, 3, 3, 4, "a", "a")
    freq = {}
    for item in t:
        freq[item] = freq.get(item, 0) + 1
    print("Tuple:", t)
    for k, v in freq.items():
        print(f"{k!r} -> {v}")


def q30():
    """Union, intersection and difference of two sets."""
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}
    print("Set A:", a)
    print("Set B:", b)
    print("Union (A | B)        :", a | b)
    print("Intersection (A & B) :", a & b)
    print("Difference (A - B)   :", a - b)
    print("Difference (B - A)   :", b - a)


def q31():
    """Check whether one set is a subset of another."""
    a = set(map(int, input("Enter elements of set A: ").split()))
    b = set(map(int, input("Enter elements of set B: ").split()))
    print("A is a subset of B" if a.issubset(b) else "A is NOT a subset of B")
    print("B is a subset of A" if b.issubset(a) else "B is NOT a subset of A")


# ===============================================================
# 8. DICTIONARIES
# ===============================================================
def q32():
    """Count the frequency of words in a sentence."""
    sentence = input("Enter a sentence: ").lower()
    freq = {}
    for word in sentence.split():
        word = word.strip(".,!?;:\"'")
        if word:
            freq[word] = freq.get(word, 0) + 1
    for w, c in freq.items():
        print(f"{w} : {c}")


def q33():
    """Create a dictionary from two lists (keys and values)."""
    keys = ["name", "age", "city"]
    values = ["Amit", 21, "Pune"]
    d = dict(zip(keys, values))
    print("Keys  :", keys)
    print("Values:", values)
    print("Dictionary:", d)


def q34():
    """Sort a dictionary by its values."""
    d = {"apple": 50, "banana": 20, "cherry": 35, "date": 10}
    asc = dict(sorted(d.items(), key=lambda item: item[1]))
    desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
    print("Original  :", d)
    print("Ascending :", asc)
    print("Descending:", desc)


# ===============================================================
# 9. FILE HANDLING
# ===============================================================
SAMPLE_FILE = "sample.txt"


def create_sample_file():
    """Creates a sample text file if it doesn't exist."""
    if not os.path.exists(SAMPLE_FILE):
        with open(SAMPLE_FILE, "w") as f:
            f.write("This is line 1\n")
            f.write("Python is fun\n")
            f.write("File handling is easy\n")
            f.write("This is line 4\n")
            f.write("Last line here\n")
        print(f"(Created sample file: {SAMPLE_FILE})")


def q35():
    """Read a text file and count lines, words and characters."""
    create_sample_file()
    lines = words = chars = 0
    with open(SAMPLE_FILE, "r") as f:
        for line in f:
            lines += 1
            words += len(line.split())
            chars += len(line)
    print(f"Lines     : {lines}")
    print(f"Words     : {words}")
    print(f"Characters: {chars}")


def q36():
    """Copy only the even-numbered lines from one file to another."""
    create_sample_file()
    out_file = "even_lines.txt"
    with open(SAMPLE_FILE, "r") as src, open(out_file, "w") as dest:
        for line_no, line in enumerate(src, start=1):
            if line_no % 2 == 0:
                dest.write(line)
    print(f"Even-numbered lines copied to '{out_file}':")
    with open(out_file, "r") as f:
        print(f.read())


# ===============================================================
# 10. EXCEPTION HANDLING
# ===============================================================
def q37():
    """Handle invalid integer input using try-except."""
    while True:
        try:
            n = int(input("Enter an integer: "))
            print(f"You entered: {n}")
            break
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def q38():
    """Handle file-not-found errors while reading a file."""
    filename = input("Enter file name to read (try a wrong name too): ")
    try:
        with open(filename, "r") as f:
            print("File contents:\n")
            print(f.read())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")


# ===============================================================
# 11. MODULES
# ===============================================================
def q39():
    """Random password generator using random and string modules."""
    length = get_int("Enter password length (min 4): ")
    if length < 4:
        print("Password length should be at least 4.")
        return
    # guarantee at least one of each type
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    print("Generated password:", "".join(password))


def q40():
    """Number of days between two dates using datetime."""
    fmt = "%Y-%m-%d"
    try:
        d1 = datetime.strptime(input("Enter first date  (YYYY-MM-DD): "), fmt)
        d2 = datetime.strptime(input("Enter second date (YYYY-MM-DD): "), fmt)
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return
    print("Number of days between dates:", abs((d2 - d1).days))


# ===============================================================
# MAIN MENU
# ===============================================================
QUESTIONS = {
    1: ("Find data type of every value in a mixed list", q1),
    2: ("Nested list -> tuple of tuples", q2),
    3: ("Remove duplicates from mixed list (keep order)", q3),
    4: ("Check power of 2 using operators", q4),
    5: ("Swap two numbers using XOR", q5),
    6: ("Divisible by both 4 and 6", q6),
    7: ("Electricity bill with unit rates", q7),
    8: ("Can three sides form a triangle?", q8),
    9: ("Type of triangle", q9),
    10: ("ATM menu", q10),
    11: ("Income tax using slabs", q11),
    12: ("Menu-driven calculator", q12),
    13: ("Prime numbers between 1 and n", q13),
    14: ("Factorial using loop", q14),
    15: ("Fibonacci series up to n terms", q15),
    16: ("Armstrong number", q16),
    17: ("Reverse number & palindrome check", q17),
    18: ("GCD of two numbers", q18),
    19: ("String palindrome function", q19),
    20: ("Count vowels and consonants", q20),
    21: ("Simple and compound interest", q21),
    22: ("All factors of a number", q22),
    23: ("Second-largest number in a list", q23),
    24: ("Merge two lists without duplicates", q24),
    25: ("Second-largest & second-smallest", q25),
    26: ("Rotate list left by k", q26),
    27: ("Separate even and odd numbers", q27),
    28: ("Common elements between two lists", q28),
    29: ("Frequency of elements in a tuple", q29),
    30: ("Union, intersection, difference of sets", q30),
    31: ("Subset check", q31),
    32: ("Word frequency in a sentence", q32),
    33: ("Dictionary from two lists", q33),
    34: ("Sort dictionary by values", q34),
    35: ("Count lines, words, characters in a file", q35),
    36: ("Copy even-numbered lines to another file", q36),
    37: ("Handle invalid integer input", q37),
    38: ("Handle file-not-found error", q38),
    39: ("Random password generator", q39),
    40: ("Days between two dates", q40),
}


def main():
    while True:
        print("\n" + "=" * 55)
        print("          PYTHON PRACTICE SET - 40 QUESTIONS")
        print("=" * 55)
        for num, (title, _) in QUESTIONS.items():
            print(f"{num:>2}. {title}")
        print(" q. Quit")
        choice = input("\nEnter question number to run: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break
        if choice.isdigit() and int(choice) in QUESTIONS:
            num = int(choice)
            print(f"\n--- Question {num}: {QUESTIONS[num][0]} ---\n")
            QUESTIONS[num][1]()
            input("\nPress Enter to return to the menu...")
        else:
            print("Invalid choice. Enter a number from 1 to 40, or 'q' to quit.")


if __name__ == "__main__":
    main()
