def convert_decimal(num):
    binary = bin(num)
    octal = oct(num)
    hexadecimal = hex(num)

    print(f"Decimal : {num}")
    print(f"Binary : {binary}")
    print(f"Octal : {octal}")
    print(f"Hexadecimal : {hexadecimal}")

decimal_num= int(input("Enter a decimal Number : "))
convert_decimal(decimal_num)

