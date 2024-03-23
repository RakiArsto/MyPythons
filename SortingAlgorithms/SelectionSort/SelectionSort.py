import random


def selection_sort(arr):
    # Dòng này gán độ dài của danh sách arr vào biến n,
    # để biết được số lượng phần tử trong danh sách.
    n = len(arr)
    # Vòng lặp bên ngoài này duyệt qua từng phần tử của danh sách,
    # từ phần tử đầu tiên đến phần tử cuối cùng.
    for i in range(n):
        # Biến min_index được sử dụng để lưu vị trí của phần tử nhỏ
        # nhất trong đoạn chưa được sắp xếp, bắt đầu từ vị trí i.
        min_index = i
        # Vòng lặp bên trong duyệt qua các phần tử từ phần tử kế
        # tiếp của i đến phần tử cuối cùng của danh sách.
        for j in range(i + 1, n):
            # Điều kiện này so sánh giá trị của phần tử hiện tại arr[j]
            # với giá trị của phần tử nhỏ nhất đang được lưu trữ tại
            # min_index.
            if arr[j] < arr[min_index]:
                # Nếu phần tử hiện tại nhỏ hơn phần tử nhỏ nhất, thì min_index
                # sẽ được cập nhật để lưu vị trí của phần tử hiện tại.
                min_index = j
        # Sau khi duyệt qua tất cả các phần tử trong đoạn chưa được sắp xếp,
        # phần tử nhỏ nhất sẽ được hoán đổi với phần tử ở vị trí i, đảm bảo
        # rằng phần tử nhỏ nhất đã được đưa vào đúng vị trí của nó trong danh sách.
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Nhập số lượng phần tử từ người dùng
n = int(input("Nhập số lượng phần tử trong danh sách: "))

# Tạo danh sách chứa các ố ngẫu nhiên không trùng lặp
my_list = random.sample(range(1, 101), n)

print(f"Danh sách trước khi sắp xếp là: {my_list}")

# Sắp xếp danh sách bằng Selection Sort
selection_sort(my_list)

print(f"Danh sách sau khi sắp xếp là: {my_list}")
