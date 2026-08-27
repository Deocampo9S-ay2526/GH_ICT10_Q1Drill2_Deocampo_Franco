# Drill 2
from pyscript import display, document

# This will add!
def addition(e):
    document.getElementById('result').innerHTML = " "
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    sum = first_number + second_number

    display(f'the sum of {first_number} and {second_number} is {sum}', target='result')

# This will subtract!
def subtraction(e):
    document.getElementById('result').innerHTML = " "
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    difference = first_number - second_number

    display(f'the difference of {first_number} and {second_number} is {difference}', target = 'result')


# This will multiply!
def multiplication(e):
    document.getElementById('result').innerHTML = " "
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    product = first_number - second_number

    display(f'the product of {first_number} and {second_number} is {product}', target = 'result')

# This will divide!
def division(e):
    document.getElementById('result').innerHTML = " "
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    quotient = first_number - second_number

    display(f'the quotient of {first_number} and {second_number} is {quotient}', target = 'result')

# This will modulus!
def modulus(e): 
    document.getElementById('result').innerHTML = " "
    first_number = float(document.getElementById('num1').value)
    second_number = float(document.getElementById('num2').value)
    remainder = first_number - second_number

    display(f'the remainder of {first_number} and {second_number} is {remainder}', target='result')

