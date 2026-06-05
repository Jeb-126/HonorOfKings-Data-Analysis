import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.sans-serif'] = ['SimHei']

data = pd.read_csv('.../HonorOfKings-Data-Analysis/data/clean_heros.csv')

# 英雄主要定位可视化
def visualize_main_role():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))

    # 饼状图(pie)
    ax1.set_title('英雄主要定位分布-饼状图', fontsize=20)
    ax1.pie(
        data['主要定位'].value_counts(),
        labels=data['主要定位'].value_counts().index,
        autopct='%.2f%%',
        startangle=90,
        colors=['cornflowerblue', 'palegreen', 'navajowhite', 'lightcoral', 'hotpink', 'skyblue'],
        shadow=True
    )
    ax1.legend(loc='lower left', fontsize=8)

    # 条形图(bar)
    ax2.set_title('英雄主要定位分布-条形图', fontsize=20)
    ax2.bar(
        data['主要定位'].value_counts().index,
        data['主要定位'].value_counts().values,
        width=0.6,
        color='skyblue'
    )
    ax2.set_xlabel('主要定位', fontsize=12)
    ax2.set_ylabel('英雄数量', fontsize=12)
    ax2.set_yticks(range(0,21,1))
    ax2.grid(axis='y', alpha=0.3, linestyle='--')
    for i, j in zip(data['主要定位'].value_counts().index, data['主要定位'].value_counts().values):
        ax2.text(i, j, j, fontsize=10, ha='center', va='bottom')

    plt.show()

# 各定位4项数据的平均值对比
def visualize_mean_of_data():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12,7))

    plots = [
        ('初始生命', ax1, 'lightcoral'),
        ('初始法力', ax2, 'cornflowerblue'),
        ('初始物攻', ax3, 'navajowhite'),
        ('初始物防', ax4, 'palegreen')
    ]

    for col, ax, color in plots:
        avg = data.groupby('主要定位')[col].mean()

        ax.set_title(f'6种定位的{col}平均值对比', fontsize=15)

        ax.bar(
            avg.index,
            avg.values,
            width=0.5,
            color=color
        )

        ax.set_ylabel(f'{col}平均值', fontsize=10)

        ax.grid(
            axis='y',
            alpha=0.3,
            linestyle='--'
        )

    plt.tight_layout() # 调整子图间距

    plt.show()

# 生命值和物防的离散关系图
def visualize_hp_vs_def():
    plt.figure(figsize=(10,6))
    plt.scatter(
        data['初始生命'],
        data['初始物防'],
        color='blue',
        alpha=0.7,
        s=20
    )

    plt.title('生命值和物防的离散关系图', fontsize=20)
    plt.xlabel('初始生命', fontsize=12)
    plt.ylabel('初始物防', fontsize=12)
    plt.grid(alpha=0.3, linestyle='--')

    # 添加趋势线
    z = np.polyfit(data['初始生命'], data['初始物防'], 1)
    p = np.poly1d(z)
    plt.plot(data['初始生命'], p(data['初始生命']), color='red', linewidth=1.5, linestyle='-')

    plt.show()

    corr = data[['初始生命', '初始物防']].corr().iloc[0, 1]
    print(f'生命值和物防的系数为：{corr:.4f}')

# 6种定位初始生命的箱线图
def visualize_boxplot():
    plt.figure(figsize=(10,6))

    role_hp_data = []
    role_names = []

    for role in data['主要定位'].value_counts().index:
        role_hp_data.append(data[data['主要定位'] == role]['初始生命'])
        role_names.append(role)

    bp = plt.boxplot(role_hp_data,
                tick_labels=role_names,
                patch_artist=True,
                medianprops=dict(linestyle='-', linewidth=1.5, color='red'))

    colors = ['cornflowerblue', 'palegreen', 'navajowhite', 'turquoise', 'gold', 'skyblue']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)

    plt.title('6种定位初始生命的箱线图', fontsize=20)
    plt.xlabel('主要定位', fontsize=12)
    plt.ylabel('初始生命', fontsize=12)
    plt.grid(axis='y', alpha=0.3, linestyle='--')

    plt.show()

def main():
    visualize_main_role()
    visualize_mean_of_data()
    visualize_hp_vs_def()
    visualize_boxplot()

if __name__ == '__main__':
    main()