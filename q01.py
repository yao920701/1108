def triangle_zhonxin(a, b, c):
    
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    x = (x1 + x2 + x3) / 3
    y = (y1 + y2 + y3) / 3

    return round(x), round(y)

if __name__ == "__main__":
    print("請輸入三角形的 3 個頂點坐標")
    print("------------------------------")
    a = tuple(map(int, input("請輸入頂點 a 的坐標：").split(',')) )
    b = tuple(map(int, input("請輸入頂點 b 的坐標：").split(',')) )
    c = tuple(map(int, input("請輸入頂點 c 的坐標：").split(',')) )
    print("------------------------------")

    centroid = triangle_zhonxin(a, b, c)

    print(f"此三角形的重心為：{centroid}")
