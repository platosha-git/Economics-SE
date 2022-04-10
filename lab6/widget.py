import sys, os
from plots import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QHeaderView, QTableWidgetItem


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi('widget.ui', self)

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
        
        self.size: QLineEdit = self.ui.sizeEdit
        self.type: QComboBox = self.ui.comboBox_16

        self.ui.wbsTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.classicTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


    def fill_table(self, pm, tm, pm_clean, tm_clean):
        for i in range(8):
            self.ui.wbsTable.setItem(i, 1, QTableWidgetItem(
                str(round(pm * int(self.ui.wbsTable.item(i, 0).text()) / 100.0, 2))))
        self.ui.wbsTable.setItem(8, 1, QTableWidgetItem(str(pm)))

        self.ui.classicTable.setItem(0, 0, QTableWidgetItem(str(round(pm_clean * PERCENTAGE['PM'][0], 2))))
        self.ui.classicTable.setItem(1, 0, QTableWidgetItem(str(round(pm_clean * PERCENTAGE['PM'][1], 2))))
        self.ui.classicTable.setItem(2, 0, QTableWidgetItem(str(round(pm_clean * PERCENTAGE['PM'][2], 2))))
        self.ui.classicTable.setItem(3, 0, QTableWidgetItem(str(round(pm_clean * PERCENTAGE['PM'][3], 2))))
        self.ui.classicTable.setItem(4, 0, QTableWidgetItem(str(round(pm_clean * PERCENTAGE['PM'][4], 2))))
        self.ui.classicTable.setItem(5, 0, QTableWidgetItem(str(round(pm_clean, 2))))
        self.ui.classicTable.setItem(6, 0, QTableWidgetItem(str(round(pm, 2))))
        self.ui.classicTable.setItem(0, 1, QTableWidgetItem(str(round(tm_clean * PERCENTAGE['TM'][0], 2))))
        self.ui.classicTable.setItem(1, 1, QTableWidgetItem(str(round(tm_clean * PERCENTAGE['TM'][1], 2))))
        self.ui.classicTable.setItem(2, 1, QTableWidgetItem(str(round(tm_clean * PERCENTAGE['TM'][2], 2))))
        self.ui.classicTable.setItem(3, 1, QTableWidgetItem(str(round(tm_clean * PERCENTAGE['TM'][3], 2))))
        self.ui.classicTable.setItem(4, 1, QTableWidgetItem(str(round(tm_clean * PERCENTAGE['TM'][4], 2))))
        self.ui.classicTable.setItem(5, 1, QTableWidgetItem(str(round(tm_clean, 2))))
        self.ui.classicTable.setItem(6, 1, QTableWidgetItem(str(round(tm, 2))))


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


    
    @pyqtSlot(name="on_calculateButton_clicked")
    def calculate_project(self):
        pm, tm, pm_clean, tm_clean = self.calculate()

        self.ui.pmLine.setText(str(pm))
        self.ui.tmLine.setText(str(tm))
        self.fill_table(pm, tm, pm_clean, tm_clean)

        plot(0)
        #plot(2)
        #plot(4)


    def calculate(self):
        try:
            mode = self.type.currentIndex()
            size = float(self.size.text())
        except:
            return

        PM = TYPE['C1'][mode] * self.eaf() * (size ** TYPE['p1'][mode])
        TM = TYPE['C2'][mode] * (PM ** TYPE['p2'][mode])

        pm_clean = round(PM, 2)
        tm_clean = round(TM, 2)
        pm = round(pm_clean * 1.08, 2)
        tm = round(tm_clean * 1.36, 2)

        return pm, tm, pm_clean, tm_clean


    @pyqtSlot(name="on_barButton_clicked")
    def bar_clicked(self):
        plot_bar(self.ui.classicTable)    
