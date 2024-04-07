n = len(arr)
- Dòng này gán độ dài của danh sách arr vào biến n, để biết được số lượng phần tử trong danh sách.

for i in range(n):
- Vòng lặp bên ngoài này điều chỉnh số lần lặp, chạy qua từng phần tử của danh sách. Với mỗi vòng lặp, 
phần tử lớn nhất sẽ được đưa vào đúng vị trí cuối cùng của danh sách.

for j in range(0, n - i - 1):
- Vòng lặp bên trong điều chỉnh việc so sánh và hoán đổi giữa các phần tử. Ở mỗi lần lặp, nó sẽ so sánh 
phần tử thứ j và phần tử tiếp theo (j+1).

if arr[j] > arr[j + 1]:
- Điều kiện này kiểm tra xem phần tử hiện tại arr[j] có lớn hơn phần tử tiếp theo arr[j+1] không. Nếu có, 
nó sẽ hoán đổi hai phần tử này để đảm bảo phần tử lớn hơn nằm ở phía sau.

arr[j], arr[j + 1] = arr[j + 1], arr[j]
- Đây là cách Python thực hiện việc hoán đổi giữa hai phần tử. Nó sẽ hoán đổi giá trị của arr[j] và arr[j+1] 
mà không cần sử dụng một biến tạm.