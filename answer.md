# 期中考
>
>學號：112111205
><br />
>姓名：鄭宇辰
><br />
>作業撰寫時間：180 (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2024/11/4
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容

## 說明程式與內容

開始寫說明，該說明需說明想法，
並於之後再對上述想法的每一部分將程式進一步進行展現，
若需引用程式區則使用下面方法，
若為.cs檔內程式除了於敘述中需註明檔案名稱外，
還需使用語法` ```語言種類 程式碼 ``` `，其中語言種類若是要用python則使用py，java則使用java，C/C++則使用cpp，
下段程式碼為語言種類選擇csharp使用後結果：

```csharp
public void mt_getResult(){
    ...
}
```

若要於內文中標示部分網頁檔，則使用以下標籤` ```html 程式碼 ``` `，
下段程式碼則為使用後結果：

```html
<%@ Page Language="C#" AutoEventWireup="true" ...>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" ...>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
    </form>
</body>
</html>
```
更多markdown方法可參閱[https://ithelp.ithome.com.tw/articles/10203758](https://ithelp.ithome.com.tw/articles/10203758)

a. 小題

Ans
```py
map: list[list[int]] = [[0 for _ in range(10)] for _ in range(10)]
```

b. 小題

Ans
```py
# 步驟 b: 建立一個大小為 10 的一維整數陣列 rowMap
# 用來表示地雷位置
rowMap = []
rowMap: list[int] = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]
#for b in range(10): #可以手動輸入地雷位置
    #boom = int(input("輸入10次炸彈位置:"))
    #rowMap.append(boom)
```

c. 小題

Ans
```py
#步驟 c: 根據 rowMap 裡的索引值在 map 中標記地雷
for index in rowMap:
    row = index // 10  # 使用索引計算對應的行
    col = index % 10   # 使用索引計算對應的列
    map[row][col] = '*'  # 在地雷位置標記為 '*'
```


d. 小題

Ans
```py
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
```


e. 小題

Ans
```py
# 步驟 e: 印出含有地雷和地雷數量的二維陣列
for row in map:
    print(' '.join(str(cell) for cell in row))
```
