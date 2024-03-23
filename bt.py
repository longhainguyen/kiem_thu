def tinh_tien_tro_so_nguoi(so_nguoi):
    if so_nguoi == 1:
        return 1700000
    elif so_nguoi == 2:
        return 2100000
    elif so_nguoi == 3:
        return 2500000
    else:
        return 0


def tinh_tien_dien(kwh):
    if kwh <= 50:
        return kwh * 1806
    elif kwh <= 100:
        return 50 * 1806 + (kwh - 50) * 1866
    else:
        return 50 * 1806 + 50 * 1866 + (kwh - 100) * 2167


def tong_tien_thang(so_nguoi, kwh):
    tien_dien = 0
    tien_tro = 0
    if so_nguoi < 1 or so_nguoi > 3 or kwh <= 0:
        return 0
    tien_tro = tinh_tien_tro_so_nguoi(so_nguoi)
    tien_dien = tinh_tien_dien(kwh)
    return tien_tro + tien_dien
