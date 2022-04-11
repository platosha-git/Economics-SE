import numpy as np
from matplotlib import pyplot as plt
from parameters import *

#Обычный вариант
def PM(C1, p1, EAF, SIZE):
    return C1 * EAF * (SIZE ** p1)

def TM(C2, p2, PM):
    return C2 * (PM ** p2)

def calc_EAF(params: list):
    return np.prod(params)


def plot_bar(table):
    y = []
    for i in range(5):
        t = round(float(table.item(i, 1).text()))
        for j in range(t):
            y.append(round(round(float(table.item(i, 0).text())) / t))

    x = [i + 1 for i in range(len(y))]

    plt.bar(x, y)
    plt.show()


def plot(t, MODP, TOOL):
    y_modp_pm = []
    y_modp_tm = []

    y_tool_pm = []
    y_tool_tm = []

    y_sced_pm = []
    y_sced_tm = []

    x = [1, 2, 3]

    for i in range(1, 4):
        y_modp_pm.append(PM(TYPE['C1'][t], TYPE['p1'][t], calc_EAF([
            ATTRIBUTES['MODP'][i]
        ]), 50))
        y_modp_tm.append(TM(TYPE['C2'][t], TYPE['p2'][t], y_modp_pm[-1]))

        y_tool_pm.append(PM(TYPE['C1'][t], TYPE['p1'][t], calc_EAF([
            ATTRIBUTES['TOOL'][i]
        ]), 50))
        y_tool_tm.append(TM(TYPE['C2'][t], TYPE['p2'][t], y_tool_pm[-1]))

        y_sced_pm.append(PM(TYPE['C1'][t], TYPE['p1'][t], calc_EAF([
            ATTRIBUTES['SCED'][i]
        ]), 50))
        y_sced_tm.append(TM(TYPE['C2'][t], TYPE['p2'][t], y_sced_pm[-1]))

    plt.suptitle(f'Режим проекта: {t}')

    plt.subplot(121)
    plt.title('Трудоемкость')
    line1, = plt.plot(x, y_modp_pm, 'r', label='MODP')
    line2, = plt.plot(x, y_tool_pm, 'b', label='TOOL')
    line3, = plt.plot(x, y_sced_pm, 'g', label='SCED')
    plt.legend(handles=[line1, line2, line3])

    plt.subplot(122)
    plt.title('Время разработки')
    line4, = plt.plot(x, y_modp_tm, 'r', label='MODP')
    line5, = plt.plot(x, y_tool_tm, 'b', label='TOOL')
    line6, = plt.plot(x, y_sced_tm, 'g', label='SCED')
    plt.legend(handles=[line4, line5, line6])

    plt.show()
