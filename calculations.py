# Import necessary modules
import math
from constants import *


# READ ME
# Calling variables as arguments is likely redundant as they are global variables
# Keeping them just to be safe tho
#
# Function to calculate pH from [H+]
# used for acid, bases, salts, and water
def get_pH():
    return -math.log10(Hplus)

# Function to calculate pH from concs
# used for buffers
def get_pH_buffer(pKa, base_conc, acid_conc):
    return pKa+math.log10(base_conc/acid_conc)


# Function to calculate [H+] from pH
# currently unused
# def get_hplus_conc_from_ph(ph):
#     return 10 ** (-ph)
#
#
# # Function to calculate pH for an acid solution
# def get_ph_acid_solution(Ka):
#     # Assuming the acid dissociates completely and gives one H+ ion per molecule
#     hplus_conc = math.sqrt(Ka * acid_conc)
#     return get_pH(hplus_conc)

# Function to calculate pH for a base solution using Kb and conc
#  def get_ph_base_solution(Kb):
#     # Calculate [OH-] conc from Kb and conc, then find [H+]
#     oh_conc = math.sqrt(Kb * base_conc)
#     hplus_conc = Kw / oh_conc
#     return get_pH(hplus_conc)


# Function to calculate pKa from Ka
def get_pKa(Ka):
    return -math.log10(Ka)


# Function to calculate pKb from Kb
def get_pKb(Kb):
    return -math.log10(Kb)

# Barium Hydroxide, strong base
def get_Ba_OH_2(Ba_OH_2_conc):
    return Kw / (2*Ba_OH_2_conc)

# Calcium Hydroxide, strong base
def get_CA_OH_2(CA_OH_2_conc):
    return Kw / (2*CA_OH_2_conc)

# Sodium Hydroxide, strong base
def get_NaOH(NaOH_conc):
    return Kw / NaOH_conc

# Ammonium Hydroxide, weak base
def get_NH4OH(NH4OH_conc):
    return Kw/math.sqrt(Kb_ammonia*NH4OH_conc)

# Hydrochloric Acid, strong acid
def get_HCl(HCl_conc):
    return HCl_conc

# Nitric Acid, strong acid
def get_HNO3(HNO3_conc):
    return HNO3_conc

# Acetic Acid, weak acid
def get_HC2H3O2(HC2H3O2_conc):
    return math.sqrt(Ka_acetic_acid*HC2H3O2_conc)

# Carbonic Acid, weak acid
def get_H2CO3(H2CO3_conc):
    return math.sqrt(Ka_carbonic_acid*H2CO3_conc)

# Sodium Chloride, neutral salt
def get_NaCl():
    return 7

# Ammonium Chloride, acidic salt of NH3
def get_NH4Cl(NH4Cl_conc):
    return math.sqrt((Kw / Kb_ammonia) * NH4Cl_conc)

# Sodium Acetate, basic salt of HC2H3O2
def get_NaC2H3O2(NaC2H3O2_conc):
    return Kw / math.sqrt((Kw / Ka_acetic_acid) * NaC2H3O2_conc)

# Sodium Bicarbonate, basic salt H2CO3
def get_NaHCO3(NaHCO3_conc):
    return Kw / math.sqrt(Ka_carbonic_acid * NaHCO3_conc)

# Sodium Carbonate, basic salt of HCO3
def get_Na2CO3(Na2CO3_conc):
    return Kw / math.sqrt((Kw / Ka_bicarbonate) * Na2CO3_conc)

# Sodium Bisulfate, acidic salt of H2SO4
def get_NaHSO4(NaHSO4_conc):
    return math.sqrt(Ka_hydrogen_sulfate * NaHSO4_conc)

def get_volume_added(drops):
    return drop_volume * drops

def get_total_volume(drops):
    return 10 + get_volume_added(drops)

def get_HCl_H(M_HCl, drops):
    return ((M_HCl * get_volume_added(drops)) / get_total_volume(drops)) + 1e-7
def get_NaOH_H(M_NaOH, drops):
    return Kw / get_HCl_H(M_NaOH, drops)

'''
For Hc2H3O2 (Acetic Acid) / NaC2H3O2 (Sodium Acetate) Buffer System
'''
# REWORK!!
# seeing as though it requires acetic acid and sodium acetate which can be calculated in two diff ways
def get_ace_buffer_system(NaC2H3O2_conc, HC2H3O2_conc):
    return pKa_acetic_acid + math.log10(get_NaC2H3O2(NaC2H3O2_conc)/get_HC2H3O2(HC2H3O2_conc))

# Adding drops of .1 or .01 M HCl
def get_HCl_HC2H3O2(HC2H3O2_conc, M_HCl, drops):
    return ((10* HC2H3O2_conc) + (drop_volume * drops * M_HCl)) / get_volume_added(drops)

# Adding drops of .1 or .01 M HCl
def get_HCl_NaC2H3O2(NaC2H3O2_conc, M_HCl, drops):
    return ((10* NaC2H3O2_conc) - (drop_volume * drops * M_HCl)) / get_volume_added(drops)

# NaC2H3O2 (Sodium Acetate) buffer capacity calculations
# Adding drops of .1 or .01 M HCl
def get_NaC2H3O2_buffer_overload():
    print("Buffer Capacity Exceeded!")

def get_NaC2H3O2_init_M(NaC2H3O2_conc):
    return NaC2H3O2_conc * 10.000

def get_M_HCl(drops, M_HCl):
    return 0.36 * drops * M_HCl

def get_excess_H(drops, M_HCl, NaC2H3O2_conc):
    return (get_M_HCl(drops, M_HCl)) - (get_NaC2H3O2_init_M(NaC2H3O2_conc))

# H+ method defined in the NaC2H3O2 buffer capacity, using the excess H+
def get_Hplus_fe(drops, M_HCl, NaC2H3O2_conc):
    Hplus = (get_excess_H(drops, M_HCl, NaC2H3O2_conc)) / (get_total_volume(drops))
    return Hplus

# HC2H3O2 buffer capacity calculations
# Adding drops of .1 or .01 NaOH

def get_NaOH_HC2H3O2(HC2H3O2_conc, M_NaOH, drops):
    return ((10.000 * HC2H3O2_conc) - (drop_volume * drops * M_NaOH)) / get_total_volume(drops)

def get_NaOH_NaC2H3O2(NaC2H3O2_conc, M_NaOH, drops):
    return ((10.000 * NaC2H3O2_conc) + (drop_volume * drops * M_NaOH)) / get_total_volume(drops)

def get_HC2H3O2_buffer_overload():
    print("Buffer Capacity Exceeded!")

def get_HC2H3O2_init_M(HC2H3O2_conc):
    return HC2H3O2_conc*10.000

def get_M_NaOH(drops, M_NaOH):
    return drop_volume * drops * M_NaOH

def get_excess_OH(drops, M_NaOH, HC2H3O2_conc):
    return get_M_NaOH(drops, M_NaOH) - get_HC2H3O2_init_M(HC2H3O2_conc)

def get_OH(drops, M_NaOH, HC2H3O2_conc):
    return get_excess_OH(drops, M_NaOH, HC2H3O2_conc) / get_total_volume(drops)

# H+ method deined in the HC2H3O2 buffer capacity, using excess OH-
def get_Hplus_OH(drops, M_NaOH, HC2H3O2_conc):
    Hplus = Kw / get_OH(drops, M_NaOH, HC2H3O2_conc)
    return Hplus
'''
For General Acid / Base Buffer System
'''

# ask Ron for function purpose
# pKa_acid, acid, and base are placeholders
def get_acid_base_buffer_system(pKa_acid, acid_conc, base_conc, M_HCl, drops):
    return pKa_acid + math.log10(get_HCl_base(base_conc, M_HCl, drops)/get_HCl_acid(acid_conc, M_HCl, drops))

# Adding drops of .1 or .01 M HCl
def get_HCl_acid(acid_conc, M_HCl, drops):
    return ((10* acid_conc) + (drop_volume * drops * M_HCl)) / get_volume_added(drops)

# Adding drops of .1 or .01 M HCl
def get_HCl_base(base_conc, M_HCl, drops):
    return ((10* base_conc) - (drop_volume * drops * M_HCl)) / get_volume_added(drops)

# Base buffer capacity calculations
# Adding drops of .1 or .01 M HCl
def get_Base_buffer_overload():
    print("Buffer Capacity Exceeded!")

def get_base_init_M(base_conc):
    return base_conc * 10.000

def get_excess_base_H(drops, M_HCl):
    return (get_M_HCl(drops, M_HCl)) - (get_base_init_M(base_conc))

# H+ method defined in the Base buffer capacity, using the excess H+
def get_base_Hplus(drops, M_HCl):
    Hplus=(get_excess_base_H(drops, M_HCl)) / (get_total_volume(drops))
    return Hplus

# Acid buffer capacity calculations
# Adding drops of .1 or .01 NaOH

def get_NaOH_acid(H_conc, M_NaOH, drops):
    return ((10.000 * H_conc) - (drop_volume * drops * M_NaOH)) / get_total_volume(drops)

def get_NaOH_base(Na_conc, M_NaOH, drops):
    return ((10.000 * Na_conc) + (drop_volume * drops * M_NaOH)) / get_total_volume(drops)

def get_acid_buffer_overload():
    print("Buffer Capacity Exceeded!")

def get_acid_init_M(acid_conc):
    return acid_conc*10.000

def get_excess_OH(drops, acid_conc):
    return get_M_NaOH(drops, M_NaOH) - get_acid_init_M(acid_conc)

# REWORK BUFFER SYSTEMS TO ALL USE Hplus, excessHplus, OH, AND excessOH
# AS IT STANDS THEY ARE INCONSISTENT
