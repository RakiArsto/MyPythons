import random
import locale


def main():
    tai_khoang_nguoi_choi = 10000000
    locale.setlocale(locale.LC_ALL, 'vi_VN.UTF-8')

    while True:
        print("-----------* MỜI BẠN LỰA CHỌN *-----------")
        print("Chọn (1) để tiếp tục chơi.")
        print("Chọn (phím bất kỳ) để thoát.")
        lua_chon = int(input())
        if lua_chon == 1:
            print("**** BẮT ĐẦU CHƠI: ")

            # Đặt cược
            print("******** TÀI KHOẢN CỦA BẠN:", locale.currency(tai_khoang_nguoi_choi, grouping=True),
                  ", BẠN MUỐN CƯỢC BAO NHIÊU? ")
            dat_cuoc = 0
            while True:
                try:
                    dat_cuoc = float(input("******** Đặt cược (0 < số tiền cược <= {}): ".format(
                        locale.currency(tai_khoang_nguoi_choi, grouping=True))))
                    if 0 < dat_cuoc <= tai_khoang_nguoi_choi:
                        break
                    else:
                        print("Số tiền cược không hợp lệ. Vui lòng nhập lại!")
                except ValueError:
                    print("Số tiền cược không hợp lệ. Vui lòng nhập lại!")

            # Chọn tài xỉu
            while True:
                lua_chon_tai_xiu = int(input("******** Chọn: 1 <-> Tài hoặc 2 <-> Xỉu: "))
                if lua_chon_tai_xiu in [1, 2]:
                    break
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập lại!")

            # Tung xúc xắc
            gia_tri1 = random.randint(1, 6)
            gia_tri2 = random.randint(1, 6)
            gia_tri3 = random.randint(1, 6)
            tong = gia_tri1 + gia_tri2 + gia_tri3

            # Tính toán kết quả
            print("******** Kết quả:", gia_tri1, "-", gia_tri2, "-", gia_tri3)
            if tong == 3 or tong == 18:
                tai_khoang_nguoi_choi -= dat_cuoc
                print("******** Tổng là:", tong, "=> Nhà cái ăn hết, bạn đã thua!")
                print("******** Tài khoản của bạn là:", locale.currency(tai_khoang_nguoi_choi, grouping=True))
            elif 4 <= tong <= 10:
                print("******** Tổng là:", tong, "=> Xỉu")
                if lua_chon_tai_xiu == 2:
                    print("******** BẠN ĐÃ THẮNG CƯỢC!")
                    tai_khoang_nguoi_choi += dat_cuoc
                    print("******** Tài khoản của bạn là:", locale.currency(tai_khoang_nguoi_choi, grouping=True))
                else:
                    print("******** BẠN ĐÃ THUA CƯỢC!")
                    tai_khoang_nguoi_choi -= dat_cuoc
                    print("******** Tài khoản của bạn là:", locale.currency(tai_khoang_nguoi_choi, grouping=True))
            else:
                print("******** Tổng là:", tong, "=> Tài")
                if lua_chon_tai_xiu == 1:
                    print("******** BẠN ĐÃ THẮNG CƯỢC!")
                    tai_khoang_nguoi_choi += dat_cuoc
                    print("******** Tài khoản của bạn là:", locale.currency(tai_khoang_nguoi_choi, grouping=True))
                else:
                    print("******** BẠN ĐÃ THUA CƯỢC!")
                    tai_khoang_nguoi_choi -= dat_cuoc
                    print("******** Tài khoản của bạn là:", locale.currency(tai_khoang_nguoi_choi, grouping=True))
        else:
            break


if __name__ == "__main__":
    main()