car_type = input("Nhap vao loai xe 4 cho hoac 7 cho ")
dist = float(input("Nhap vao so km (so duong): "))
waiting_time = int(input("Nhap vao thoi gian cho theo don vi phut"))
waiting_money = (waiting_time - 5)*750
if (car_type == 4):
    open_door_money = 11000
    if (dist <= 0.8):
        moving_fee = open_door_money + waiting_money
        print(f"Tien phi cho la: {waiting_money}")
        print(f"Tien phi di chuyen la: {open_door_money}")
        print(f"Tong chi phi la: {moving_fee}")
    elif ((dist > 0.8) and (dist <= 30)):
        moving_fee = open_door_money + (30-0.8) * 15300
        final_fee = waiting_money + moving_fee
        print(f"Tien phi cho la: {waiting_money}")
        print(f"Tien phi di chuyen la: {moving_fee}")
        print(f"Tong tien cuoc can thanh toan la: {final_fee}")
    else:
        moving_fee = open_door_money + (30-0.8) * 15300 + (dist - 30 - 0.8)* 12100
        final_fee = waiting_money + moving_fee
        print(f"Tien phi cho la: {waiting_money}")
        print(f"Tien phi di chuyen la: {moving_fee}")
        print(f"Tong tien cuoc can thanh toan la: {final_fee}") 

elif (car_type == 7):
    open_door_money = 12000
    if (dist <= 0.8):
        moving_fee = open_door_money + waiting_money
        print(f"Tien phi cho la: {waiting_money}")
        print(f"Tien phi di chuyen la: {open_door_money}")
        print(f"Tong chi phi la: {moving_fee}")
    elif ((dist > 0.8) and (dist <= 30)):
        moving_fee = open_door_money + (30-0.8) * 16100
        final_fee = waiting_money + moving_fee
        print(f"Tien phi cho la: {waiting_money}")
        print(f"Tien phi di chuyen la: {moving_fee}")
        print(f"Tong tien cuoc can thanh toan la: {final_fee}")
    else:
        moving_fee = open_door_money + (30-0.8) * 16100 + (dist - 30 - 0.8)* 13800
        final_fee = waiting_money + moving_fee
        print(f"Tien phi cho la: {waiting_money}")
        print(f"Tien phi di chuyen la: {moving_fee}")
        print(f"Tong tien cuoc can thanh toan la: {final_fee}") 

