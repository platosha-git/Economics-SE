from functools import reduce
from base import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QComboBox, QLabel

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = uic.loadUi("widget.ui", self)

        self.tab1 = self.ui.tabWidget.widget(0)
        self.tab2 = self.ui.tabWidget.widget(1)

        self.get_func_params()

        self.sysParams = []
        for i in range(1, 15):
            self.sysParams.append(self.tab1.findChild(QComboBox, 'comboBox_' + str(i)))

        self.get_lang_params()

        self.VAFRes: QLineEdit = self.tab1.findChild(QLineEdit, 'VAFLabel')
        self.NormFPRes: QLineEdit = self.tab1.findChild(QLineEdit, 'NormFPLabel')
        self.FPRes: QLineEdit = self.tab1.findChild(QLineEdit, 'FPLabel')
        self.LOCRes: QLineEdit = self.tab1.findChild(QLineEdit, 'LOCLabel')

        self.PREC: QComboBox = self.tab2.findChild(QComboBox, 'powComboBox_1')
        self.FLEX: QComboBox = self.tab2.findChild(QComboBox, 'powComboBox_2')
        self.RESL: QComboBox = self.tab2.findChild(QComboBox, 'powComboBox_3')
        self.TEAM: QComboBox = self.tab2.findChild(QComboBox, 'powComboBox_4')
        self.PMAT: QComboBox = self.tab2.findChild(QComboBox, 'powComboBox_5')

        self.Power: QLabel = self.tab2.findChild(QLineEdit, 'PLabel')

        self.arch: [QComboBox] = [
            self.tab2.findChild(QComboBox, 'archComboBox_1'),
            self.tab2.findChild(QComboBox, 'archComboBox_2'),
            self.tab2.findChild(QComboBox, 'archComboBox_3'),
            self.tab2.findChild(QComboBox, 'archComboBox_4'),
            self.tab2.findChild(QComboBox, 'archComboBox_5'),
            self.tab2.findChild(QComboBox, 'archComboBox_6'),
            self.tab2.findChild(QComboBox, 'archComboBox_7'),
        ]

        self.archLab: QLabel = self.tab2.findChild(QLineEdit, 'archLabLabel')
        self.archTime: QLabel = self.tab2.findChild(QLineEdit, 'archTimeLabel')
        self.archBudget: QLabel = self.tab2.findChild(QLineEdit, 'archBudgetLabel')

        self.screenQty = [
            self.tab2.findChild(QLineEdit, 'screenSimpleEdit'),
            self.tab2.findChild(QLineEdit, 'screenMediumEdit'),
            self.tab2.findChild(QLineEdit, 'screenDifficultEdit'),
        ]

        self.reportQty = [
            self.tab2.findChild(QLineEdit, 'reportSimpleEdit'),
            self.tab2.findChild(QLineEdit, 'reportMediumEdit'),
            self.tab2.findChild(QLineEdit, 'reportDifficultEdit'),
        ]

        self.gen3Qty: QLineEdit = self.tab2.findChild(QLineEdit, 'gen3Edit')
        self.RUSE: QLineEdit = self.tab2.findChild(QLineEdit, 'RUSEEdit')
        self.EXP: QComboBox = self.tab2.findChild(QComboBox, 'expComboBox')

        self.compLab: QLineEdit = self.tab2.findChild(QLineEdit, 'compLabLabel')
        self.compTime: QLineEdit = self.tab2.findChild(QLineEdit, 'compTimeLabel')
        self.compBudget: QLineEdit = self.tab2.findChild(QLineEdit, 'compBudgetLabel')
        self.avgSalary: QLineEdit = self.tab2.findChild(QLineEdit, 'avgSalaryEdit')

        self.LOC = 0
        self.calculate_LOC()
        self.p = 0
        self.SALARY = SALARY


    def get_func_params(self):
        self.EIQty: QLineEdit = self.tab1.findChild(QLineEdit, 'EIEdit')
        self.EOQty: QLineEdit = self.tab1.findChild(QLineEdit, 'EOEdit')
        self.EQQty: QLineEdit = self.tab1.findChild(QLineEdit, 'EQEdit')
        self.ILFQty: QLineEdit = self.tab1.findChild(QLineEdit, 'ILFEdit')
        self.EIFQty: QLineEdit = self.tab1.findChild(QLineEdit, 'EIFEdit')

        self.EIDif: QComboBox = self.tab1.findChild(QComboBox, 'comboBox_16')
        self.EODif: QComboBox = self.tab1.findChild(QComboBox, 'comboBox_17')
        self.EQDif: QComboBox = self.tab1.findChild(QComboBox, 'comboBox_18')
        self.ILFDif: QComboBox = self.tab1.findChild(QComboBox, 'comboBox_19')
        self.EIFDif: QComboBox = self.tab1.findChild(QComboBox, 'comboBox_20')

        self.EIRes: QLabel = self.tab1.findChild(QLabel, 'EILabel')
        self.EORes: QLabel = self.tab1.findChild(QLabel, 'EOLabel')
        self.EQRes: QLabel = self.tab1.findChild(QLabel, 'EQLabel')
        self.ILFRes: QLabel = self.tab1.findChild(QLabel, 'ILFLabel')
        self.EIFRes: QLabel = self.tab1.findChild(QLabel, 'EIFLabel')
        self.TFPRes: QLabel = self.tab1.findChild(QLabel, 'ResLabel')


    def get_lang_params(self):
        self.ASMPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'ASMEdit')
        self.CPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'CEdit')
        self.CobolPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'CobolEdit')
        self.FortranPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'FortranEdit')
        self.PascalPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'PascalEdit')
        self.CPPPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'CPPEdit')
        self.JavaPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'JavaEdit')
        self.CSharpPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'CSharpEdit')
        self.AdaPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'AdaEdit')
        self.SQLPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'SQLEdit')
        self.VCPPPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'VCPPEdit')
        self.DelphiPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'DelphiEdit')
        self.PerlPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'PerlEdit')
        self.PrologPercent: QLineEdit = self.tab1.findChild(QLineEdit, 'PrologEdit')


    def get_sys_params(self):
        return list(map(lambda sb: sb.currentIndex(), self.sysParams))

    def get_lang_percentages(self):
        return {
            'ASM': float(self.ASMPercent.text()),
            'C': float(self.CPercent.text()),
            'Cobol': float(self.CobolPercent.text()),
            'Fortran': float(self.FortranPercent.text()),
            'Pascal': float(self.PascalPercent.text()),
            'CPP': float(self.CPPPercent.text()),
            'Java': float(self.JavaPercent.text()),
            'CSharp': float(self.CSharpPercent.text()),
            'Ada': float(self.AdaPercent.text()),
            'SQL': float(self.SQLPercent.text()),
            'VCPP': float(self.VCPPPercent.text()),
            'Delphi': float(self.DelphiPercent.text()),
            'Perl': float(self.PerlPercent.text()),
            'Prolog': float(self.PrologPercent.text()),
        }

    def get_fp_qty(self):
        return {
            'EI': float(self.EIQty.text()),
            'EO': float(self.EOQty.text()),
            'EQ': float(self.EQQty.text()),
            'ILF': float(self.ILFQty.text()),
            'EIF': float(self.EIFQty.text()),
        }

    def get_fp_levels(self):
        return {
            'EI': self.EIDif.currentIndex(),
            'EO': self.EODif.currentIndex(),
            'EQ': self.EQDif.currentIndex(),
            'ILF': self.ILFDif.currentIndex(),
            'EIF': self.EIFDif.currentIndex(),
        }

    def set_fp_results(self, EI, EO, EQ, ILF, EIF, RES):
        self.EIRes.setText(str(EI))
        self.EORes.setText(str(EO))
        self.EQRes.setText(str(EQ))
        self.ILFRes.setText(str(ILF))
        self.EIFRes.setText(str(EIF))
        self.TFPRes.setText(str(RES))

    def set_calculate_fp_results(self, VAF, NormFP, FP, LOC):
        self.VAFRes.setText(str(VAF))
        self.NormFPRes.setText(str(NormFP))
        self.FPRes.setText(str(FP))
        self.LOCRes.setText(str(LOC))

    def get_screen_qty(self):
        return list(map(lambda le: float(le.text()), self.screenQty))

    def get_report_qty(self):
        return list(map(lambda le: float(le.text()), self.reportQty))

    def calculate_LOC(self):
        fp_levels = self.get_fp_levels()
        fp_qty = self.get_fp_qty()
        sys_params = self.get_sys_params()
        languages = self.get_lang_percentages()

        EILevel = params_level_table['EI'][fp_levels['EI']]
        EOLevel = params_level_table['EO'][fp_levels['EO']]
        EQLevel = params_level_table['EQ'][fp_levels['EQ']]
        ILFLevel = params_level_table['ILF'][fp_levels['ILF']]
        EIFLevel = params_level_table['EIF'][fp_levels['EIF']]

        EIResult = int(fp_qty['EI']) * EILevel
        EOResult = int(fp_qty['EO']) * EOLevel
        EQResult = int(fp_qty['EQ']) * EQLevel
        ILFResult = int(fp_qty['ILF']) * ILFLevel
        EIFResult = int(fp_qty['EIF']) * EIFLevel
        UFPC = EIResult + EOResult + EQResult + ILFResult + EIFResult

        VAF = 0.65 + 0.01 * sum(sys_params)
        AFPC = UFPC * VAF

        for lang in ['ASM', 'C', 'Cobol', 'Fortran', 'Pascal', 'CPP', 'Java', 'CSharp', 'Ada', 'SQL', 'VCPP', 'Delphi',
            'Perl', 'Prolog']:
            self.LOC += AFPC * (float(languages[lang]) / 100.0) * LANGUAGE_FP[lang]


######################
# Функциональные точки
######################
    @pyqtSlot(name='on_calculateButton_clicked')
    def calculate_fp(self):
        self.LOC = 0
        fp_levels = self.get_fp_levels()
        fp_qty = self.get_fp_qty()
        sys_params = self.get_sys_params()
        languages = self.get_lang_percentages()

        EILevel = params_level_table['EI'][fp_levels['EI']]
        EOLevel = params_level_table['EO'][fp_levels['EO']]
        EQLevel = params_level_table['EQ'][fp_levels['EQ']]
        ILFLevel = params_level_table['ILF'][fp_levels['ILF']]
        EIFLevel = params_level_table['EIF'][fp_levels['EIF']]

        EIResult = int(fp_qty['EI']) * EILevel
        EOResult = int(fp_qty['EO']) * EOLevel
        EQResult = int(fp_qty['EQ']) * EQLevel
        ILFResult = int(fp_qty['ILF']) * ILFLevel
        EIFResult = int(fp_qty['EIF']) * EIFLevel
        UFPC = EIResult + EOResult + EQResult + ILFResult + EIFResult

        VAF = calculate_VAF(sys_params)
        AFPC = calculate_AFPC(VAF, UFPC)
        self.LOC += calculate_LOC(AFPC, languages)

        self.set_fp_results(EIResult, EOResult, EQResult, ILFResult, EIFResult, UFPC)
        self.set_calculate_fp_results(VAF, round(AFPC, 2), UFPC, int(self.LOC))

    def get_power_params(self):
        return {
            'PREC': self.PREC.currentIndex(),
            'FLEX': self.FLEX.currentIndex(),
            'RESL': self.RESL.currentIndex(),
            'TEAM': self.TEAM.currentIndex(),
            'PMAT': self.PMAT.currentIndex(),
        }

    @pyqtSlot(name='on_pCalculateButton_clicked')
    def calculate_p(self):
        power_params = self.get_power_params()

        PREC = DEGREE_FACTOR['PREC'][power_params['PREC']]
        FLEX = DEGREE_FACTOR['FLEX'][power_params['FLEX']]
        RESL = DEGREE_FACTOR['RESL'][power_params['RESL']]
        TEAM = DEGREE_FACTOR['TEAM'][power_params['TEAM']]
        PMAT = DEGREE_FACTOR['PMAT'][power_params['PMAT']]

        result = PREC + FLEX + RESL + TEAM + PMAT
        self.p = result / 100 + 1.01
        
        self.Power.setText(str(self.p))


#############################
# Метод композиции приложения
#############################
    def get_forms(self):
        easy_forms = self.get_screen_qty()[0]
        medium_forms = self.get_screen_qty()[1]
        hard_forms = self.get_screen_qty()[2]
        return [easy_forms, medium_forms, hard_forms]

    def get_reports(self):
        easy_report = self.get_report_qty()[0]
        medium_report = self.get_report_qty()[1]
        hard_report = self.get_report_qty()[2]
        return [easy_report, medium_report, hard_report]

    def set_comp_results(self, labor, time, budget):
        self.compLab.setText(str(labor))
        self.compTime.setText(str(time))
        self.compBudget.setText(str(budget))

    @pyqtSlot(name='on_compCalculateButton_clicked')
    def calculate_comp(self):
        RUSE = float(self.RUSE.text())
        PROD = experience_level[self.EXP.currentIndex()]
        
        forms = self.get_forms()
        reports = self.get_reports()
        modules = float(self.gen3Qty.text())

        NOP = calculate_NOP(forms, reports, modules)
        labor = calculate_compLABOR(NOP, RUSE, PROD)
        time = calculate_compTIME(labor, self.p)
        budget = calculate_budget(self.SALARY, labor)

        self.set_comp_results(labor, time, budget)


#############################
# Метод ранней архитектуры
#############################
    def get_arch_params(self):
        return list(map(lambda sb: sb.currentIndex(), self.arch))
    
    def set_arch_results(self, labor, time, budget):
        self.archLab.setText(str(labor))
        self.archTime.setText(str(time))
        self.archBudget.setText(str(budget))

    @pyqtSlot(name='on_archCalculateButton_clicked')
    def calculate_arch(self):
        arch_params = self.get_arch_params()
        
        arch_params_values = []
        arch_params_values.append(LABOR_FACTOR['PERS'][arch_params[0]])
        arch_params_values.append(LABOR_FACTOR['RCPX'][arch_params[1]])
        arch_params_values.append(LABOR_FACTOR['RUSE'][arch_params[2]])
        arch_params_values.append(LABOR_FACTOR['PDIF'][arch_params[3]])
        arch_params_values.append(LABOR_FACTOR['PREX'][arch_params[4]])
        arch_params_values.append(LABOR_FACTOR['FCIL'][arch_params[5]])
        arch_params_values.append(LABOR_FACTOR['SCED'][arch_params[6]])

        labor = calculate_archLABOR(reduce(lambda x, y: x * y, arch_params_values), 
                                    self.LOC / 1000.0, self.p)
        time = calculate_archTIME(labor, self.p)
        budget = calculate_budget(self.SALARY, labor)

        self.set_arch_results(labor, time, budget)
