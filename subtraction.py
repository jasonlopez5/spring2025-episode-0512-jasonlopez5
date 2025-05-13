def subtract(subtracts: list[float]) -> float:
    if not subtracts:
        return 0

    difference = subtracts[0]
    for number in subtracts[1:]:
        difference = difference - number

    return difference

def describe_subtract() -> str:
    return 'Returns the sum of all of the numbers passed to it.'


if __name__ == '__main__':
    import sys

    print(describe_subtract())

    if len(sys.argv) > 1:
        subtracts = [float(arg) for arg in sys.argv[1:]]
        print(subtract(subtracts))