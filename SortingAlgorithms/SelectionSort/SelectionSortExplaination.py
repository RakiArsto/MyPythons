n = len(arr)
- Dòng này gán độ dài của danh sách arr vào biến n,
để biết được số lượng phần tử trong danh sách.

for i in range(n):
- Vòng lặp bên ngoài này duyệt qua từng phần tử của danh sách, từ phần tử đầu tiên đến phần tử cuối cùng.

min_index = i
- Biến min_index được sử dụng để lưu vị trí của phần tử nhỏ nhất trong đoạn chưa được sắp xếp, bắt đầu từ vị trí i.

for j in range(i + 1, n):
- Vòng lặp bên trong duyệt qua các phần tử từ phần tử kế tiếp của i đến phần tử cuối cùng của danh sách.

if arr[j] < arr[min_index]:
- Điều kiện này so sánh giá trị của phần tử hiện tại arr[j] với giá trị của phần tử nhỏ nhất đang được lưu 
trữ tại min_index.

min_index = j
- Nếu phần tử hiện tại nhỏ hơn phần tử nhỏ nhất, thì min_index sẽ được cập nhật để lưu vào vị trí của phần tử hiện tại.

arr[i], arr[min_index] = arr[min_index], arr[i]
- Sau khi duyệt qua tất cả các phần tử trong đoạn chưa được sắp xếp, phần tử nhỏ nhất sẽ được hoán đổi với 
phần tử ở vị trí i, đảm bảo rằng phần tử nhỏ nhất đã được đưa vào đúng vị trí của nó trong danh sách 
(để ngoài vòng lặp bên trong).