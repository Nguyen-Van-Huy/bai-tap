def tinhgiaithua(n):
    giai_thua = 1;
    if (n == 0 or n == 1):
        return giai_thua;
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i;
        return giai_thua;
    n = int(input("Nhap mot so n = ")):
print("Giai thua cua", n);
© 2020 GitHub, Inc.
