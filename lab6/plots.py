import numpy as np
from matplotlib import pyplot as plt
from parameters import *

#Обычный вариант
def PM(C1, p1, EAF, SIZE):
    return 3.2 * EAF * (SIZE ** 1.05)

def TM(C2, p2, PM):
    return 2.5 * (PM ** 0.38)

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


def plot(cplx):
    for t in range(3):
        y_acap_pm = []
        y_aexp_pm = []
        y_pcap_pm = []
        y_lexp_pm = []
        y_acap_tm = []
        y_aexp_tm = []
        y_pcap_tm = []
        y_lexp_tm = []

        x = [1, 2, 3]

        for i in range(1, 4):
            y_acap_pm.append(PM(TYPE['C1'][t], TYPE['p1'][t], calc_EAF([
                ATTRIBUTES['ACAP'][i],
                ATTRIBUTES['CPLX'][cplx]
            ]), 100))
            y_acap_tm.append(TM(TYPE['C2'][t], TYPE['p2'][t], y_acap_pm[-1]))

            y_aexp_pm.append(PM(TYPE['C1'][t], TYPE['p1'][t], calc_EAF([
                ATTRIBUTES['AEXP'][i],
                ATTRIBUTES['CPLX'][cplx]
            ]), 100))
            y_aexp_tm.append(TM(TYPE['C2'][t], TYPE['p2'][t], y_aexp_pm[-1]))

            y_pcap_pm.append(PM(TYPE['C1'][t], TYPE['p1'][t], calc_EAF([
                ATTRIBUTES['PCAP'][i],
                ATTRIBUTES['CPLX'][cplx]
            ]), 100))
            y_pcap_tm.append(TM(TYPE['C2'][t], TYPE['p2'][t], y_pcap_pm[-1]))

            y_lexp_pm.append(PM(TYPE['C1'][t], TYPE['p1'][t], calc_EAF([
                ATTRIBUTES['LEXP'][i],
                ATTRIBUTES['CPLX'][cplx]
            ]), 100))
            y_lexp_tm.append(TM(TYPE['C2'][t], TYPE['p2'][t], y_lexp_pm[-1]))

        plt.suptitle(f'PM, TM; mode={t}, CPLX={cplx}')
        plt.subplot(121)
        line1, = plt.plot(x, y_acap_pm, 'r', label='ACAP')
        line2, = plt.plot(x, y_aexp_pm, 'g', label='AEXP')
        line3, = plt.plot(x, y_pcap_pm, 'b', label='PCAP')
        line4, = plt.plot(x, y_lexp_pm, 'y', label='LEXP')
        plt.subplot(122)
        plt.plot(x, y_acap_tm, 'r', x, y_aexp_tm, 'g', x, y_pcap_tm, 'b', x, y_lexp_tm, 'y')
        plt.legend(handles=[line1, line2, line3, line4])
        plt.show()