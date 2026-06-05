import pandas as pd

# 读取数据
data = pd.read_csv('.../HonorOfKings-Data-Analysis/data/raw_heros.csv')
print(data)

# 检查缺失值
def check_missing():
    print(f"缺失值数量：\n{data.isna().sum()}")

# 检查重复值
def check_duplicates():
    print(f"重复值数量：{data.duplicated().sum()}")

# 删除一些不要的列
def drop_columns():
    drop_col = ['最大生命',
                '生命成长',
                '最大法力',
                '法力成长',
                '最高物攻',
                '物攻成长',
                '最大物防',
                '物防成长',
                '最大每5秒回血',
                '每5秒回血成长',
                '最大每5秒回蓝',
                '每5秒回蓝成长',
                '最大攻速',
                '次要定位']

    data.drop(columns=drop_col, inplace=True)

# 导出处理后的数据
def export_csv():
    data.to_csv(
        '.../HonorOfKings-Data-Analysis/data/clean_heros.csv',
        index=False
    )

def main():
    check_missing()
    check_duplicates()

    drop_columns()

    export_csv()

if __name__ == '__main__':
    main()
