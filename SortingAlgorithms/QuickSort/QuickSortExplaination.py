Hàm Partition(arr, left, right)

pivot = arr[right]
- pivot là phần tử chốt được chọn để phân chia mảng. Trong trường hợp này, chọn phần tử pivot từ mảng, 
thường là phần tử cuối cùng của mảng.

i = left - 1
- i là biến đếm cho các phần tử nhỏ hơn pivot. Khởi tạo chỉ số i trỏ vào phần tử trước vị trí bắt đầu 
của mảng (left).

for j in range(left, right):
- Duyệt qua các phần tử từ left đến right - 1 (không bao gồm phần tử cuối cùng) của mảng.

if arr[j] < pivot:
- Kiểm tra nếu phần tử hiện tại nhỏ hơn phần tử pivot.

i += 1
- Tăng chỉ số i lên 1.

arr[i], arr[j] = arr[j], arr[i]
- Hoán đổi giá trị của arr[i] và arr[j].

arr[i + 1], arr[right] = arr[right], arr[i + 1]
- (Ở ngoài vòng lặp for)
- Sau khi duyệt qua tất cả các phần tử, hoán đổi giá trị của pivot với phần tử tại i + 1. Điều này đặt 
pivot vào vị trí đúng trong mảng đã được sắp xếp.

return i + 1
- Trả về chỉ số của pivot.

Hàm QuickSort(arr, left, right)

if left < right:
- Kiểm tra điều kiện dừng của đệ quy, đảm bảo rằng vẫn còn ít nhất hai phần tử trong đoạn cần sắp xếp.

pi = Partition(arr, left, right)
- Gọi hàm Partition để chia mảng thành hai phần và lây chỉ số pivot(pi).

QuickSort(arr, left, pi - 1)
- Đệ quy sắp xếp các phần tử nhỏ hơn pivot ở bên trái của pivot.

QuickSort(arr, pi + 1, right)
- Đệ quy sắp xếp các phần tử lớn hơn pivot ở bên phải của pivot.