"""School"""
from decimal import Decimal, ROUND_HALF_UP

def main():
    """School"""
    member = input()
    n = int(input())
    price = Decimal("0")
    for _ in range(n):
        price += Decimal(input())

    if member == "Y":
        price *= Decimal("0.95")
    elif member == "N":
        if price >= 500:
            price *= Decimal("0.97")

    price = price.quantize(
    Decimal("0.01"),
    rounding=ROUND_HALF_UP
)
    print(price)
main()