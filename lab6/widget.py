import sys, os
import numpy as np
from matplotlib import pyplot as plt
from parameters import TYPE, ATTRIBUTES
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem


#Обычный вариант
def PM(C1, p1, EAF, SIZE):
    return 3.2 * EAF * (SIZE ** 1.05)

def TM(C2, p2, PM):
    return 2.5 * (PM ** 0.38)

def calc_EAF(params: list):
    return np.prod(params)


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi('./lab6.ui', self)

        self.RELY: QComboBox = self.ui.comboBox_1
        self.DATA: QComboBox = self.ui.comboBox_2
        self.CPLX: QComboBox = self.ui.comboBox_3
        self.TIME: QComboBox = self.ui.comboBox_4
        self.STOR: QComboBox = self.ui.comboBox_5
        self.VIRT: QComboBox = self.ui.comboBox_6
        self.TURN: QComboBox = self.ui.comboBox_7
        self.ACAP: QComboBox = self.ui.comboBox_8
        self.AEXP: QComboBox = self.ui.comboBox_9
        self.PCAP: QComboBox = self.ui.comboBox_10
        self.VEXP: QComboBox = self.ui.comboBox_11
        self.LEXP: QComboBox = self.ui.comboBox_12
        self.MODP: QComboBox = self.ui.comboBox_13
        self.TOOL: QComboBox = self.ui.comboBox_14
        self.SCED: QComboBox = self.ui.comboBox_15

        self.RELY.currentIndexChanged.connect(self.calculate_project)
        self.DATA.currentIndexChanged.connect(self.calculate_project)
        self.CPLX.currentIndexChanged.connect(self.calculate_project)
        self.TIME.currentIndexChanged.connect(self.calculate_project)
        self.STOR.currentIndexChanged.connect(self.calculate_project)
        self.VIRT.currentIndexChanged.connect(self.calculate_project)
        self.TURN.currentIndexChanged.connect(self.calculate_project)
        self.ACAP.currentIndexChanged.connect(self.calculate_project)
        self.AEXP.currentIndexChanged.connect(self.calculate_project)
        self.PCAP.currentIndexChanged.connect(self.calculate_project)
        self.VEXP.currentIndexChanged.connect(self.calculate_project)
        self.LEXP.currentIndexChanged.connect(self.calculate_project)
        self.MODP.currentIndexChanged.connect(self.calculate_project)
        self.TOOL.currentIndexChanged.connect(self.calculate_project)
        self.SCED.currentIndexChanged.connect(self.calculate_project)

        self.SIZE: QLineEdit = self.ui.sizeEdit
        self.SIZE.textEdited.connect(self.calculate_project)

        self.project_mode: QComboBox = self.ui.comboBox_16
        self.project_mode.currentIndexChanged.connect(self.calculate_project)

        self.ui.wbsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.classicTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.calculate_project()

    def eaf(self):
        RELY = ATTRIBUTES['RELY'][self.RELY.currentIndex()]
        DATA = ATTRIBUTES['DATA'][self.DATA.currentIndex()]
        CPLX = ATTRIBUTES['CPLX'][self.CPLX.currentIndex()]
        TIME = ATTRIBUTES['TIME'][self.TIME.currentIndex()]
        STOR = ATTRIBUTES['STOR'][self.STOR.currentIndex()]
        VIRT = ATTRIBUTES['VIRT'][self.VIRT.currentIndex()]
        TURN = ATTRIBUTES['TURN'][self.TURN.currentIndex()]
        ACAP = ATTRIBUTES['ACAP'][self.ACAP.currentIndex()]
        AEXP = ATTRIBUTES['AEXP'][self.AEXP.currentIndex()]
        PCAP = ATTRIBUTES['PCAP'][self.PCAP.currentIndex()]
        VEXP = ATTRIBUTES['VEXP'][self.VEXP.currentIndex()]
        LEXP = ATTRIBUTES['LEXP'][self.LEXP.currentIndex()]
        MODP = ATTRIBUTES['MODP'][self.MODP.currentIndex()]
        TOOL = ATTRIBUTES['TOOL'][self.TOOL.currentIndex()]
        SCED = ATTRIBUTES['SCED'][self.SCED.currentIndex()]

        return RELY * DATA * CPLX * TIME * STOR * VIRT * TURN * ACAP * AEXP * PCAP * VEXP * LEXP * MODP * TOOL * SCED

    def PM(self):
        mode = self.project_mode.currentIndex()
        SIZE = float(self.SIZE.text())
        return TYPE['C1'][mode] * self.eaf() * (SIZE ** TYPE['p1'][mode])

    def TM(self):
        mode = self.project_mode.currentIndex()

        return TYPE['C2'][mode] * (self.PM() ** TYPE['p2'][mode])

    def calculate_project(self):
        try:
            float(self.SIZE.text())
        except:
            return

        pm_clean = round(self.PM(), 2)
        tm_clean = round(self.TM(), 2)
        pm = round(pm_clean * 1.08, 2)
        tm = round(tm_clean * 1.36, 2)

        self.ui.pmLabel.setText(f'Трудоемкость: {pm}')
        self.ui.tmLabel.setText(f'Время разработки: {tm}')

        for i in range(8):
            self.ui.wbsTable.setItem(i, 1,
                                     QTableWidgetItem(
                                         str(round(pm * int(self.ui.wbsTable.item(i, 0).text()) / 100.0, 2))))
        self.ui.wbsTable.setItem(8, 1, QTableWidgetItem(str(pm)))

        self.ui.classicTable.setItem(0, 0, QTableWidgetItem(str(round(pm_clean * 0.08, 2))))
        self.ui.classicTable.setItem(1, 0, QTableWidgetItem(str(round(pm_clean * 0.18, 2))))
        self.ui.classicTable.setItem(2, 0, QTableWidgetItem(str(round(pm_clean * 0.25, 2))))
        self.ui.classicTable.setItem(3, 0, QTableWidgetItem(str(round(pm_clean * 0.26, 2))))
        self.ui.classicTable.setItem(4, 0, QTableWidgetItem(str(round(pm_clean * 0.31, 2))))
        self.ui.classicTable.setItem(5, 0, QTableWidgetItem(str(round(pm_clean, 2))))
        self.ui.classicTable.setItem(6, 0, QTableWidgetItem(str(round(pm, 2))))
        self.ui.classicTable.setItem(0, 1, QTableWidgetItem(str(round(tm_clean * 0.36, 2))))
        self.ui.classicTable.setItem(1, 1, QTableWidgetItem(str(round(tm_clean * 0.36, 2))))
        self.ui.classicTable.setItem(2, 1, QTableWidgetItem(str(round(tm_clean * 0.18, 2))))
        self.ui.classicTable.setItem(3, 1, QTableWidgetItem(str(round(tm_clean * 0.18, 2))))
        self.ui.classicTable.setItem(4, 1, QTableWidgetItem(str(round(tm_clean * 0.28, 2))))
        self.ui.classicTable.setItem(5, 1, QTableWidgetItem(str(round(tm_clean, 2))))
        self.ui.classicTable.setItem(6, 1, QTableWidgetItem(str(round(tm, 2))))

        y = []
        for i in range(5):
            t = round(float(self.ui.classicTable.item(i, 1).text()))
            for j in range(t):
                y.append(round(round(float(self.ui.classicTable.item(i, 0).text())) / t))

        x = [i + 1 for i in range(len(y))]

        plt.bar(x, y)
        plt.show()

    @pyqtSlot(name="on_task1Button_clicked")
    def calculate_task1(self):

        for cplx in [0, 2, 4]:
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
