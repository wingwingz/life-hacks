def mod7(arr: list[int], checkDigit: int):
    x = int("".join(arr))
    return x % 7 == checkDigit

def mod10(
        arr: list[int], checkDigit: int,
        evensMultiplier: int, oddsMultiplier: int):
    total = sum(
        idx % 2 == 0 and evensMultiplier * val or oddsMultiplier * val
        for idx, val in enumerate(arr))
    x = total % 10
    if x != 0:
        x = 10 - x
    
    return x == checkDigit

def s10(seq1: list[int], checkDigit: int):
    weightings = [8,6,4,2,3,5,9,7]
    x = sum(x * y for x, y in zip(seq1, weightings))
    r = x % 11
    if (r == 1):
        r = 0
    elif (r == 0):
        r = 5
    else:
        r = 11 - r

    return r == checkDigit

def sumProductWithWeightingsAndModulo(
        seq1: list[int], checkDigit: int, weightings: list[int],
        modulo1: int, modulo2: int):
    x = sum(x * y for x, y in zip(seq1, weightings))
    return x % modulo1 % modulo2 == checkDigit


def serial_number(chars: str, is_ups: bool) -> int:
    if is_ups:
        return [int(ch) if ch.isdigit() else (ord(ch) - 3) % 10 for ch in chars]
    else:
        return [int(ch) for ch in chars]