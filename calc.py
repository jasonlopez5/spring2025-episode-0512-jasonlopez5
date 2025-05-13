from add import add, describe_add

"""
This dictionary serves as the central “registry” for the calc program. This
allows the program to be expanded in a highly modular manner. To expand calc,
do the following:

1. Implement the operator and describer functions in its own file
   (see _add.py_ as an example)

2. You can test and debug the file independently before making it available
   to calc (again see how _add.py_ is implemented)

3. When the new module is ready, “register” it with this dictionary

4. calc should now be able to use that operator!
"""
CALC_MODULES = {
    'add': {
        'operator': add,
        'describer': describe_add
    }
}


def calc(operator: str, operands: list[float]) -> float:
    operator_entry = CALC_MODULES[operator]
    operator = operator_entry['operator']
    return operator(operands)


def print_available_operators():
    print('Available operators:')

    for key in CALC_MODULES:
        description = CALC_MODULES[key]['describer']()
        print(f'• {key}: {description}')


if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print('Usage: calc.py <operator> <operands (depending on operator)>')
        print()
        print_available_operators()
    else:
        operator = sys.argv[1]
        operands = [float(arg) for arg in sys.argv[2:]]

        try:
            answer = calc(operator, operands)
            print(f'The answer is {answer}.')
        except KeyError:
            print(f'Sorry, but we do not know how to do the {operator} operation 😕')
            print()
            print_available_operators()
