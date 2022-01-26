class Divider:

    def __init__(self):
      pass

    def divide_two_numbers(self, numberOne, numberTwo):

        try:
            print(numberOne/numberTwo)
        except ZeroDivisionError:
            print("You cant divide by 0 dummy!")
        except:
            print("Something went wrong!")
        else:
            print("The division was successful!")
            return numberOne / numberTwo
        finally:
            print("I will always run at the end no matter what!")

        if(numberOne is None or numberTwo is None):
            print("You must enter 2 numbers!")

# TODO: Write 4 Tests for divider section
    # Input two numbers
    # Divide by 0 SHOULD NOT WORK
    # 2 / "2" SHOULD NOT WORK
    # 2 / NONE SHUOLD NOT WORK