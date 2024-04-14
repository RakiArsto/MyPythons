Hàm Merge(left, right)

result = []
- Khởi tạo một danh sách rỗng để lưu trữ kết quả của việc hợp nhất (merge) các phần tử từ hai mảng.

left_idx = 0
- Khởi tạo một biến chỉ mục để theo dõi vị trí hiện tại trong mảng bên trái (left).

right_idx = 0
- Khởi tạo một biến chỉ mục để theo dõi vị trí hiện tại trong mảng bên phải (right).

while left_idx < len(left) and right_idx < len(right):
- Đây là một vòng lặp while kiểm tra điều kiện. Nó sẽ tiếp tục chạy miễn là cả left_idx và 
right_idx đều nhỏ hơn độ dài tương ứng của mảng left và right. Điều này đảm bảo rằng chúng 
ta vẫn còn các phần tử chưa được xử lý trong cả hai mảng.

if left[left_idx] < right[right_idx]:
- Đây là một câu lệnh điều kiện, kiểm tra xem phần tử tại chỉ mục left_idx của mảng left 
có nhỏ hơn phần tử tại chỉ mục right_idx của mảng right hay không.

result.append(left[left_idx])
- Nếu phần tử tại left[left_idx] nhỏ hơn phần tử tương ứng tại right[right_idx], thì phần 
tử đó của mảng left được thêm vào danh sách kết quả result.

left_idx += 1
- Sau khi thêm phần tử từ mảng left vào danh sách kết quả, chỉ mục của mảng left (left_idx) 
được tăng lên 1 đơn vị để chúng ta có thể tiếp tục kiểm tra và thêm các phần tử tiếp theo 
từ mảng left.

else:
result.append(right[right_idx])
- Trong trường hợp phần tử từ mảng right nhỏ hơn hoặc bằng phần tử từ mảng left, chúng ta 
thêm phần tử từ mảng right vào danh sách kết quả result.

right_idx += 1
- Sau khi thêm phần tử từ mảng right vào danh sách kết quả, chỉ mục của mảng right (right_idx) 
được tăng lên 1 đơn vị để chúng ta có thể tiếp tục kiểm tra và thêm các phần tử tiếp theo 
từ mảng right.

while left_idx < len(left):
- Đây là một vòng lặp while kiểm tra điều kiện. Nó sẽ tiếp tục chạy miễn là chỉ mục left_idx 
nhỏ hơn độ dài của mảng left. Điều này đảm bảo rằng chúng ta vẫn còn các phần tử chưa được 
xử lý trong mảng left.

result.append(left[left_idx])
- Trong mỗi vòng lặp, phần tử tại vị trí left[left_idx] của mảng left được thêm vào danh sách 
kết quả result.

left_idx += 1
- Sau khi thêm phần tử từ mảng left vào danh sách kết quả, chỉ mục của mảng left (left_idx) 
được tăng lên 1 đơn vị để chúng ta có thể tiếp tục thêm các phần tử tiếp theo từ mảng left.

while right_idx < len(right):
- Đây là một vòng lặp while khác kiểm tra điều kiện. Nó sẽ tiếp tục chạy miễn là chỉ mục 
right_idx nhỏ hơn độ dài của mảng right. Điều này đảm bảo rằng chúng ta vẫn còn các phần 
tử chưa được xử lý trong mảng right.

result.append(right[right_idx])
- Trong mỗi vòng lặp, phần tử tại vị trí right[right_idx] của mảng right được thêm vào danh 
sách kết quả result.

right_idx += 1
- Sau khi thêm phần tử từ mảng right vào danh sách kết quả, chỉ mục của mảng right (right_idx) 
được tăng lên 1 đơn vị để chúng ta có thể tiếp tục thêm các phần tử tiếp theo từ mảng right.

return result
- Câu lệnh return result được sử dụng để trả về kết quả cuối cùng của quá trình hợp nhất hai 
mảng con đã sắp xếp thành một mảng con duy nhất đã sắp xếp.
- Việc trả về mảng result là cách để truyền kết quả của quá trình hợp nhất này từ hàm Merge 
ra bên ngoài, để sau đó nó có thể được sử dụng trong quá trình sắp xếp toàn bộ mảng trong 
hàm MergeSort.

Hàm MergeSort(arr)

if len(arr) <= 1:
- Dòng này kiểm tra nếu độ dài của mảng arr nhỏ hơn hoặc bằng 1, tức là mảng chỉ có một phần tử 
hoặc không có phần tử nào.

return arr
- Trả về mảng đó mà không cần sắp xếp (vì mảng đã sắp xếp khi chỉ có một phần tử hoặc 
không có phần tử nào).

mid = len(arr) // 2
- Dòng này tính chỉ số của phần tử ở giữa của mảng arr, sẽ được sử dụng để chia mảng thành hai nửa.

left_half = arr[:mid]
- Dòng này tạo ra một mảng mới chứa các phần tử từ đầu của mảng arr cho đến chỉ số mid, tạo thành 
nửa đầu của mảng.

right_half = arr[mid:]
- Dòng này tạo ra một mảng mới chứa các phần tử từ chỉ số mid đến cuối của mảng arr, tạo thành 
nửa sau của mảng.

left_half = MergeSort(left_half)
- Dòng này là việc gọi đệ quy của hàm MergeSort trên nửa đầu của mảng arr. Điều này sẽ sắp xếp 
nửa đầu của mảng.

right_half = MergeSort(right_half)
- Tương tự như trên, dòng này gọi đệ quy của hàm MergeSort trên nửa sau của mảng arr, sắp xếp 
nửa sau của mảng.

return Merge(left_half, right_half)
- Dòng này kết hợp hai nửa đã được sắp xếp lại bằng cách gọi hàm Merge với hai mảng đã được sắp 
xếp này làm đối số. Điều này sẽ trả về một mảng đã được sắp xếp hoàn chỉnh.