import pandas as pd

# 读取数据
data = pd.read_csv('.../HonorOfKings-Data-Analysis/data/clean_heros.csv')

# 主要定位分类
roles = {
    role_loc: role
    for role_loc, role in data.groupby('主要定位')
}

# 保存csv文件
def save_csv():
    for role_loc in roles:
        roles[role_loc].to_csv(
            f'.../HonorOfKings-Data-Analysis/role/{role_loc}.csv',
            index=False
        )

# 单个定位的属性
def analyze_role(role_loc, role):
    print(f"========== {role_loc} ==========")

    columns = [
        '初始生命',
        '初始法力',
        '初始物防',
        '初始物攻'
    ]

    for col in columns:
        role_max = role[col].idxmax()
        role_min = role[col].idxmin()
        role_avg = role[col].mean()
        role_mid = role[col].median()
        role_std = role[col].std()

        print(
            f"--------------------\n"
            f"MAX({col})："
            f"{role.loc[role_max, '英雄']} "
            f"{role.loc[role_max, col]}"
        )

        print(
            f"MIN({col})："
            f"{role.loc[role_min, '英雄']} "
            f"{role.loc[role_min, col]}"
        )

        print(f"AVG({col})：{role_avg:.2f}")

        print(f"MED({col})：{role_mid:.2f}")

        print(f"STD({col})：{role_std:.2f}")

# 英雄定位统计
def role_count():
    print("========== 英雄定位统计 ==========")

    print(data['主要定位'].value_counts())

# 初始生命、初始物攻top10
def top10(col):
    print(f"========== {col}top10 ==========")

    print(
        data.nlargest(
            10,
            col
        )[['英雄', col]].reset_index(drop=True)
    )

def main():
    save_csv()

    for role_loc in roles:
        role = roles[role_loc]
        analyze_role(role_loc, role)
        print("\n")

    role_count()
    print("\n")

    top10('初始生命')
    print("\n")

    top10('初始物攻')
    print("\n")

if __name__ == '__main__':
    main()
