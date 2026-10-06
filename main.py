"""flash"""

def main():
    """flash"""
    route = input().split()
    weight = float(input())

    start = route[0]
    destination = route[1]

    if start == "BKK" and destination == "CNX":
        bath = 10 + weight * 30
    elif start == "CNX" and destination == "UBP":
        bath = 15 + weight * 40
    elif start == "UBP" and destination == "BKK":
        bath = 20 + weight * 40
    elif start == "BKK" and destination == "PKT":
        bath = 25 + weight * 50
    elif start == "PKT" and destination == "CNX":
        bath = 30 + weight * 60
    elif start == "UBP" and destination == "PKT":
        bath = 40 + weight * 70
    else:
        print("Error")
        return

    print(f"{bath:.2f}")
main()