def la_so_nguyen_to(n):
    # Kiểm tra điều kiện ban đầu
    # Nếu n nhỏ hơn hoặc bằng 1, hàm trả về False vì số
    # 1 và các số âm không phải là số nguyên tố.
    if n <= 1:
        return False
    # Kiểm tra từ 2 đến căn bậc hai của n
    # Hàm duyệt qua các số từ 2 đến căn bậc hai của n (được làm tròn lên).
    # Nếu n chia hết cho một số trong khoảng này (tức là n % i == 0),
    # hàm trả về False vì n không phải là số nguyên tố.
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    # Trả về kết quả
    # Nếu không tìm thấy số nào chia hết cho n, hàm trả về True, tức là n là số nguyên tố.
    return True


# Gọi hàm để kiểm tra một số ví dụ
so_kiem_tra = int(input("Nhập số nguyên bất kỳ: "))
if la_so_nguyen_to(so_kiem_tra):
    print(f"{so_kiem_tra} là số nguyên tố.")
else:
    print(f"{so_kiem_tra} không là số nguyên tố.")
