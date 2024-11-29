import matplotlib.pyplot as plt

def main():
    # 使用内置样式
    plt.style.use('seaborn-v0_8')

    # 定义数据
    x_values = list(range(1, 1001))
    y_values = [x**2 for x in x_values]

    # 创建图表
    fig, ax = plt.subplots()

    # 绘制一系列点
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=10)

    # 设置图题并给坐标轴加上标签
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    # 设置刻度标记的样式
    ax.tick_params(axis='both', which='major', labelsize=14)

    # 设置每个坐标轴的取值范围
    ax.axis([0, 1100, 0, 1100000])

    # 使用常规表示法（避免科学计数法）
    ax.ticklabel_format(style='plain')

    # 保存图表
    plt.savefig('squares_plot.png', bbox_inches='tight')

    # 显示图表
    plt.show()

if __name__ == '__main__':
    main()