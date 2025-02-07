def divisibility(a,b):
    try:
        print(f"{a} divided by {b}: {a/b}")
    except Exception as e:
        print(e)
    else:
        print("Program successfully executed")
    finally:
        print("----------END----------")

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
divisibility(a,b)