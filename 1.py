# 步驟 a: 建立一個 10x10 的二維整數陣列 map，每個元素初始為 0
map: list[list[int]] = [[0 for _ in range(10)] for _ in range(10)]

# 步驟 b: 建立一個大小為 10 的一維整數陣列 rowMap
# 用來表示地雷位置
rowMap = []
#for b in range(10):
    #boom = int(input("輸入10次炸彈位置:"))
    #rowMap.append(boom)
rowMap: list[int] = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]

# 步驟 c: 根據 rowMap 裡的索引值在 map 中標記地雷

for index in rowMap:
    row = index // 10  # 使用索引計算對應的行
    col = index % 10   # 使用索引計算對應的列
    map[row][col] = '*'  # 在地雷位置標記為 '*'

# 步驟 d: 計算並標記每個位置周圍的地雷數量
for i in range(10):
    for j in range(10):
        # 只對非地雷位置進行地雷數量的計算
        if map[i][j] != '*':
            # 計算以 map[i][j] 為中心的 3x3 區域中的地雷數量
            bomb_count = 0
            for x in range(max(0, i - 1), min(10, i + 2)):
                for y in range(max(0, j - 1), min(10, j + 2)):
                    if map[x][y] == '*':
                        bomb_count += 1
            # 如果附近有地雷，記錄地雷數量，否則顯示為空白
            map[i][j] = bomb_count if bomb_count > 0 else ' '

# 步驟 e: 印出含有地雷和地雷數量的二維陣列
for row in map:
    print(' '.join(str(cell) for cell in row))