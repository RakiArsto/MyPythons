n = len(arr)
- Đây là cách để lấy độ dài của mảng arr và lưu vào biến n. Độ dài này sẽ được sử dụng để xác định 
số lần lặp qua mảng.

for i in range(1, n):
- Vòng lặp này duyệt qua mảng arr bắt đầu từ chỉ số thứ 1 cho đến n - 1, bởi vì ta sẽ so sánh mỗi 
phần tử với các phần tử trước nó.

temp = arr[i]
- Gán giá trị của phần tử hiện tại đang xét arr[i] vào biến tạm thời temp.

j = i - 1
- Khởi tạo biến j là chỉ số của phần tử trước đó trong mảng. Trong quá trình lặp, j sẽ giảm dần 
từ vị trí hiện tại của i xuống 0.

while j >= 0 and temp < arr[j]
- Điều kiện của vòng lặp while, nó sẽ tiếp tục lặp cho đến khi j vẫn lớn hơn hoặc bằng 0 và giá 
trị của temp nhỏ hơn giá trị của phần tử tại vị trí arr[j].

arr[j + 1] = arr[j]
- Di chuyển các phần tử lớn hơn temp sang phải một vị trí. Cụ thể là gán giá trị của phần tử 
tại vị trí arr[j] vào vị trí kế tiếp, tức là arr[j + 1]

j -= 1
- Giảm giá trị của j đi 1 để kiểm tra phần tử tiếp theo bên trái của temp.

arr[j + 1] = temp
- Gán giá trị của temp vào vị trí đúng của nó trong mảng đã sắp xếp. Vị trí này là j + 1 bởi vì 
sau khi vòng lặp while kết thúc, j đã giảm đi một lần nữa. 