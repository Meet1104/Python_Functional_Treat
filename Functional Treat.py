class Analyzer:
    def __init__(self):
        self.array = []

    def create_1d_array(self):
        self.array = list(map(int, input(
            "Enter data for a 1D array (separated by spaces): ").split()))
        print("Data inserted successfully!")

    def display_data(self):
        if not self.array:
            print("Array is empty! Please input data first.")
            return

        total_elements = len(self.array)
        minimum = min(self.array)
        maximum = max(self.array)
        total_sum = sum(self.array)
        avg = total_sum / total_elements

        print("\n📊 Data Summary:")
        print("Total elements:", total_elements)
        print("Minimum value:", minimum)
        print("Maximum value:", maximum)
        print("Sum of all values:", total_sum)
        print("Average value:", avg)

    def factorial(self):
        if not self.array:
            print("Array is empty! Please input data first.")
            return

        n = int(input("Enter a number from the array to calculate factorial: "))

        if n not in self.array:
            print("Number not found in array!")
            return

        if n < 1:
            print("Factorial is defined only for positive numbers!")
            return

        def factorial(n):
            if n == 1:
                return 1
            return n * factorial(n - 1)

        print(f"Factorial of {n} is: {factorial(n)}")

    def filter_by_threshold(self):
        if not self.array:
            print("Array is empty! Please input data first.")
            return

        threshold = int(input("Enter threshold value: "))

        filtered = list(filter(lambda x: x > threshold, self.array))

        print("Filtered values (greater than threshold):", filtered)

    def sort_data(self):
        if not self.array:
            print("Array is empty! Please input data first.")
            return

        print("\nSort Options:")
        print("1. Ascending Order")
        print("2. Descending Order")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.array.sort()
            print("Array sorted in ascending order:", self.array)

        elif choice == 2:
            self.array.sort(reverse=True)
            print("Array sorted in descending order:", self.array)

        else:
            print("Invalid sorting choice!")


print("Welcome to the Data Analyzer and Transformer Program\n")

obj = Analyzer()

while True:
    print("\nMain Menu:")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial (Recursion)")
    print("4. Filter Data by Threshold (Lambda Function)")
    print("5. Sort Data")
    print("6. Exit program\n")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number!")
        continue

    match choice:
        case 1:
            obj.create_1d_array()

        case 2:
            obj.display_data()

        case 3:
            obj.factorial()

        case 4:
            obj.filter_by_threshold()

        case 5:
            obj.sort_data()

        case 6:
            print("\nThank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break

        case _:
            print("\nEnter a valid choice")
