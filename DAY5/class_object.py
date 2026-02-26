class StudentData:
    def __init__(self):
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.roll_no = int(input("Enter roll number: "))

    def display(self):
        print("\n--- Student Details ---")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Thanks for submitting your data,", self.name)

# Create object
hariharan = StudentData()
deepak = StudentData()

# Call method
hariharan.display()
deepak.display()