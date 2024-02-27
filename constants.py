# Constants
Kw = 1e-14
Ka_acetic_acid = 1.8e-5  # Used for HC2H3O2
Ka_carbonic_acid = 4.3e-7  # Used for H2CO3
Ka_bicarbonate = 5.6e-11  # Used for NaHCO3
Ka_dihydrogen_phosphate = 6.2e-8  # Used for NaH2PO4
Ka_hydrogen_sulfate = 1.2e-2  # Used for NaHSO4
Kb_ammonia = 1.8e-5  # Used for NH3

# pKa values for weak acids and bases
pKa_acetic_acid = 4.745  # Used for HC2H3O2
pKa_ammonium_chloride = 9.255  # Used for NH4Cl
pKa_monohydrogen_phosphate = 7.208  # Used for NaH2PO4
pKa_bicarbonate = 10.252  # Used for HO3 # strange minus mark at the end (ignored)
pKa_carbonic_acid = 6.367  # Used for H2CO3

# other consts
initial_water_pH = 7
drop_volume = 0.036
drops=0;
base_conc=0
acid_conc=0
M_HCl=0
M_NaOH=0;
Hplus=0;
excessHplus=0;
excessOH=0;
OH=0;

# chemical concentrations, safe measure in case multiple chemicals require accessing the same conc variable

Ba_OH_2_conc=0;

# Calcium Hydroxide, strong base
CA_OH_2_conc=0;

# Sodium Hydroxide, strong base
NaOH_conc=0;

# Ammonium Hydroxide, weak base
NH4OH_conc=0;

# Hydrochloric Acid, strong acid
HCl_conc=0;

# Nitric Acid, strong acid
HNO3_conc=0;

# Acetic Acid, weak acid
HC2H3O2_conc=0;

# Carbonic Acid, weak acid
H2CO3_conc=0;

# Sodium Chloride, neutral salt
# NaCl=7;

# Ammonium Chloride, acidic salt of NH3
NH4Cl_conc=0;

# Sodium Acetate, basic salt of HC2H3O2
NaC2H3O2_conc=0;

# Sodium Bicarbonate, basic salt H2CO3
NaHCO3_conc=0;

# Sodium Carbonate, basic salt of HCO3
Na2CO3_conc=0;

# Sodium Bisulfate, acidic salt of H2SO4
NaHSO4_conc=0;

# HOUSEHOLD ITEMS

household_items={
    "Table Salt (Sodium Chloride)": 7.0,
    "Baking Soda (sodium bicarbonate)": 8.3,
    "Hydrogen Peroxide (3% H2O2)": 6.2,
    "Drano (contains Sodium Hydroxide)": 12.0,
    "Liquid Plumber (contains Sulfuric Acid)": 1.0,
    "Soft Drink (contains Citric and Carbonic Acids)": 3.2,
    "Orange Juice (contains Citric and Ascorbic Acids)": 3.9,
    "Milk": 6.8,
    "Dish Soap": 8.7,
    "Blood": 7.40,
    "Battery Acid (contains Sulfuric Acid)": 1.0,
    "Ammonia Cleaner (2% Ammonium Hydroxide)": 11.6,
    "Vinegar (5% Acetic Acid)": 2.4
}