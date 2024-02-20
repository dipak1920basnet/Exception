def main():
    taqueria = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }
    def totalval(s):
        return taqueria[s]
    while True:
        try:
            name = str(input("Item: "))
        except ValueError:
            continue
        else:
            print(f"total:{totalval(name)}")
            continue

main()
