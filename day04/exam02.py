training_data = [['연두', 3, '사과'],
                 ['노랑', 3, '사과'],
                 ['빨강', 2, '포도'],
                 ['빨강', 1, '포도'],
                 ['노랑', 3, '레몬']]


def fruit_counts(data):
    fruit_dic = {}
    for i in data:
        label = i[-1]
        if label not in fruit_dic:
            fruit_dic[label] = 0
        fruit_dic[label] += 1
    return fruit_dic


def fruit_color(data):
    color_dic = {}
    for i in data:
        label = i[0]
        if label not in color_dic:
            color_dic[label] = 0
        color_dic[label] += 1
    return color_dic


result = fruit_counts(training_data)
print(result)

colorCnt = fruit_color(training_data)
print(colorCnt)
