import pandas as pd

# 注意：不要加 header=3，直接默认读取第1行作为表头
df = pd.read_excel("shiyan.xlsx", sheet_name="Sheet1", usecols="A")
print(df.head())
print(f"一共读到了 {len(df)} 行数据")