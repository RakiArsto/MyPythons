import math


# Định nghĩa hàm giải phương trình bậc hai ax^2 + bx + c = 0
def giai_ptb2(a, b, c):
    # Tính delta
    delta = b ** 2 - 4 * a * c

    # Kiểm tra giá trị của delta
    if delta > 0:
        # Hai nghiệm thực phân biệt
        nghiem1 = (-b + math.sqrt(delta)) / (2 * a)
        nghiem2 = (-b - math.sqrt(delta)) / (2 * a)
        return nghiem1, nghiem2
    elif delta == 0:
        # Một nghiệm thực
        nghiem = -b / (2 * a)
        return (nghiem,)
    else:
        # Không có nghiệm thực
        return ()


# Hàm main để kiểm tra hàm giai_ptb2
def main():
    # Các hệ số của phương trình bậc hai
    a = float(input("Nhập giá trị a: "))
    b = float(input("Nhập giá trị b: "))
    c = float(input("Nhập giá trị c: "))

    # Giải phương trình bậc hai
    nghiem = giai_ptb2(a, b, c)

    # In kết quả
    if len(nghiem) == 2:
        print(f"Phương trình có hai nghiệm phân biệt: \n"
              f"{nghiem[0]} và {nghiem[1]}")
    elif len(nghiem) == 1:
        print(f"Phương trình có nghiệm kép: \n{nghiem[0]}")
    else:
        print("Phương trình vô nghiệm")


# Gọi hàm main
if __name__ == "__main__":
    main()
