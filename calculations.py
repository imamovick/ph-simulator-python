# Import necessary modules
import math
from constants import *

# Function to calculate pH from [H+]
# used for acid, bases, salts, and water
def get_pH(hplus_conc):
    return -math.log10(hplus_conc)

# Function to calculate pH from concs
# used for buffers
def get_pH_buffer(pKa, base_conc, acid_conc):
    return pKa+math.log10(base_conc/acid_conc)

# Function to calculate [H+] from pH
#currently unused
def get_hplus_conc_from_ph(ph):
    return 10 ** (-ph)

# Function to calculate pH for an acid solution
def get_ph_acid_solution(Ka, conc):
    # Assuming the acid dissociates completely and gives one H+ ion per molecule
    hplus_conc = math.sqrt(Ka * conc)
    return get_pH(hplus_conc)

# Function to calculate pH for a base solution using Kb and conc
def get_ph_base_solution(Kb, conc):
    # Calculate [OH-] conc from Kb and conc, then find [H+]
    oh_conc = math.sqrt(Kb * conc)
    hplus_conc = Kw / oh_conc
    return get_pH(hplus_conc)

# Function to calculate pKa from Ka
def get_pKa(Ka):
    return -math.log10(Ka)

# Function to calculate pKb from Kb
def get_pKb(Kb):
    return -math.log10(Kb)

# Barium Hydroxide, strong base
def get_Ba_OH_2(conc):
    return Kw / (2*conc)

# Calcium Hydroxide, strong base
def get_CA_OH_2(conc):
    return Kw / (2*conc)

# Sodium Hydroxide, strong base
def get_Na_OH(conc):
    return Kw / conc

# Ammonium Hydroxide
def get_NH4OH(conc):
    return Kw/math.sqrt(Kb_ammonia*conc)

# Hydrochloric Acid, strong acid
def get_HCl(conc):
    return conc

# Nitric Acid, strong acid
def get_HNO3(conc):
    return conc

# Acetic Acid, weak acid
def get_HC2H3O2(conc):
    return math.sqrt(Ka_acetic_acid*conc)

# Carbonic Acid, weak acid
def get_H2CO3(conc):
    return math.sqrt(Ka_carbonic_acid*conc)

# Sodium Chloride, neutral salt
def get_NaCl(conc):
    return 7

# Ammonium Chloride, acidic salt of NH3
def get_NH4Cl(conc):
    return math.sqrt((Kw / Kb_ammonia) * conc)

# Sodium Acetate, basic salt of HC2H3O2
def get_NaC2H3O2(conc):
    return Kw / math.sqrt((Kw / Ka_acetic_acid) * conc)

# Sodium Bicarbonate, basic salt H2CO3
def get_NaHCO3(conc):
    return Kw / math.sqrt((Ka_carbonic_acid) * conc)

# Sodium Carbonate, basic salt of HCO3
def get_Na2CO3(conc):
    return Kw / math.sqrt((Kw / Ka_bicarbonate) * conc)

# Sodium Bisulfate, acidic salt of H2SO4
def get_NaHSO4(conc):
    return math.sqrt(Ka_hydrogen_sulfate * conc)