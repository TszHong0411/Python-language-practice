# def for define "定義"

kg = input("Please enter weight (kg): ")

if kg.isdigit():
    kg = int(kg)
    def converter(weight):
        ponds = weight / 0.45
        print(ponds)
    converter(kg)
else:
    print("Please enter number.")