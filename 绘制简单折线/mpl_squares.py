import matplotlib.pyplot as plt

def main():
    # 使用内置样式
    plt.style.use('seaborn-v0_8')

    # 数据准备
    x_values = [1, 2, 3, 4, 5]
    y_values = [x**2 for x in x_values]  # 计算y值为x的平方

    # 创建图表和一个子图
    fig, ax = plt.subplots()

    # 绘制数据
    ax.plot(x_values, y_values, linewidth=2)  # 绘制线图
    ax.scatter(x_values, y_values, color='red', s=100)  # 在相同位置上绘制红色散点图

    # 设置图表标题和标签
    ax.set_title("Simple Plot & Scatter", fontsize=24)
    ax.set_xlabel("X Label", fontsize=14)
    ax.set_ylabel("Y Label", fontsize=14)

    # 设置刻度标记的大小
    ax.tick_params(axis='both', labelsize=14)

    # 显示网格
    ax.grid(True)

    # 显示图表
    plt.show()

if __name__ == '__main__':
    main()