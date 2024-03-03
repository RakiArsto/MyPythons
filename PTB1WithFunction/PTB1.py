def ptb1(a, b):
    if a == 0:
        if b == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -b / a
        print(f"Phương trình có nghiệm là: {x}")


a = float(input("Nhập số nguyên a: "))
b = float(input("Nhập số nguyên b: "))
ptb1(a, b)
