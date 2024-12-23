import plotly.express as px
from die import Die
# 创建一个 D6
die_1 = Die()
die_2 = Die(10)
# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)

for value in poss_results:
 frequency = results.count(value)
 frequencies.append(frequency)
 print(frequencies) 
fig = px.bar(x=poss_results, y=frequencies)
title = "Results of Rolling TWO D6 Dice 5,0000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()