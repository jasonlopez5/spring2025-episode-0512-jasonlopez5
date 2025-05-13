def multiply(factors: list[float]) -> float:
    product = 0
    for factor in factors:
        product = product * factor

    return product

def describe_multiply() -> str:
    return 'Returns the product of all of the numbers passed to it.'

if __name__ == '__main__':
    import sys

    print(describe_multiply())

    if len(sys.argv) > 1:
        factors = [float(arg) for arg in sys.argv[1:]]
        print(multiply(factors))