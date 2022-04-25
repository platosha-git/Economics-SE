import math
from parameters import *

def calculate_budget(salary, labor):
    budget = salary * labor
    return budget

#Метод функциональных точек
def calculate_LOC(AFPC, languages):
    LOC = 0
    for lang in ['ASM', 'C', 'Cobol', 'Fortran', 'Pascal', 'CPP', 'Java',
                'CSharp', 'Ada', 'SQL', 'VCPP', 'Delphi','Perl', 'Prolog']:
        LOC += AFPC * (float(languages[lang]) / 100.0) * LANGUAGE_FP[lang]

    return LOC

def calculate_VAF(params):
    VAF = 0.65 + 0.01 * sum(params)
    return VAF

def calculate_AFPC(VAF, UFPC):
    AFPC = UFPC * VAF
    return AFPC


#Модель композиции приложения
def calculate_NOP(forms, reports, modules):
    NOP = forms[0] + forms[1] * 2 + forms[2] * 3 + \
        reports[0] * 2 + reports[1] * 5 + reports[2] * 8 + \
        modules * 10
    return NOP

def calculate_compLABOR(NOP, RUSE, PROD):
    labor = round((NOP * (100 - RUSE) / 100) / PROD)
    return labor

def calculate_compTIME(labor, p):
    time = round(3 * math.pow(labor, 0.33 + 0.2 * (p - 1.01)))
    return time


#Модель ранней архитектуры приложения
def calculate_archLABOR(eArch, size, p):
    labor = round(2.45 * eArch * math.pow(size, p))
    return labor

def calculate_archTIME(labor, p):
    time = round(3 * math.pow(labor, 0.33 + 0.2 * (p - 1.01)))
    return time
