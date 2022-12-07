import my_module
import calculator
# Import the module `calculator` here

my_module.hello_world("John")


calc = calculator.Calculator() #'Create a new instance of Calculator class defined in calculator'
for i in range(100):
    # Use Calculator method `add` to add `i` to the current value.
    calc.add(i)

print(calc.get_current())




