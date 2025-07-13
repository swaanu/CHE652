# --- SET DEFINITIONS ---
import gurobipy as gp # access all gurobi functions and classes through a gp. prefix
from gurobipy import GRB
import math
# Countries

A= [
    "UK",
    "USA",
    "Germany",
    "Saudi Arabia",
    "China",
    "Australia",
    "India",
    "Brazil",
    "Kazakhstan",  # Fixed spelling (from Kazakastan)
    "Canada",
    "Chile",
    "Peru",
    "Mexico",     # Fixed spelling (from Maxico)
    "Indonesia",
    "Japan",
    "South Korea"  # Fixed spelling (from South koria)
    ]
#parts =
B= [
    "Shim Coils", "RF Coils", "Gradient Coil", "Patient Table", "PDU",
    "Gradient Amplifier", "RF Amplifier", "RF Receiver Assembly",
    "Image Reconstruction Computer", "Peripheral Devices", "MRI Safety System",
    "RF Shielding"
]
#packaging_types
C= [
    "Fiberboard Boxes", "Plastic Drums", "Steel Drums", "Wooden Crates",
    "Vacuum-Sealed Foil Bags", "Anti-Static Bags", "Polyethylene Bags",
    "Bubble/Foam Wrap", "IBC Totes", "Cardboard Tubes",
    "Shrink-Wrapped Pallets", "Cushioned Metal Boxes", "Thermal Insulated Boxes"
]
D = [
    "Unskilled", "Semi-Skilled", "Skilled", "Highly Skilled"
]
E = [ "Magnets" , "Liquid helium", "Cu", "Al", "Nb", "Ti",  
    "Capacitor", "Fibre Glass", "Epoxy resin", "ABS", "GaAs",  
    "Rn-316", "Deionized water", "Teflon", "Kapton Tape", "Foam Damper",  
    "Plastic", "Polypropylene", "Non Magnetic Motor", "Silicon gel", "Fibre optic wire",  
    "PET", "Anti Bacterial vinyl", "Emi Paint", "LEDs", "Lcds Monitor",  
    "Lion battery", "Brass", "Inductor", "Mosfets", "FGA",  
    "Lc Filters", "LDMOS", "GAN", "SiGe BJTs", "VSWR",  
    "RF Coaxial", "SiGe Trans", "Gold", "Optical isolator", "Rubber",  
    "Galvanized steel"
]


                             #Parameters 
speed_air = 900 
speed_water = 35

Sourcing_cost  = {
    "UK": {
        "Magnets": 65000,
        "Liquid helium": 11.5,
        "Cu": 8.4,
        "Al": 2.4,
        "Nb": 756,
        "Ti": 9,
        "Capacitor": 0.866666667,
        "Fibre Glass": 1.936,
        "Epoxy resin": 6.2,
        "ABS": 0.45,
        "GaAs": 28.8,
        "Rn-316": 3.85,
        "Deionized water": 0.66,
        "Teflon": 1.08,
        "Kapton Tape": 0.42,
        "Foam Damper": 7.333333333,
        "Plastic": 1.672,
        "Polypropylene": 1.513333333,
        "Non Magnetic Motor": 390,
        "Silicon gel": 10.5,
        "Fibre optic wire": 1.8,
        "PET": 6.75,
        "Anti Bacterial vinyl": 3.6,
        "Emi Paint": 22.5,
        "LEDs": 0.38,
        "Lcds Monitor": 320,
        "Lion battery": 48.5,
        "Brass": 7,
        "Inductor": 1,
        "Mosfets": 16,
        "FGA": 175,
        "Lc Filters": 2.5,
        "LDMOS": 210,
        "GAN": 220,
        "SiGe BJTs": 65,
        "VSWR": 48,
        "RF Coaxial": 4.722222222,
        "SiGe Trans": 6.666666667,
        "Gold": 59,
        "Optical isolator": 18,
        "Rubber": 6,
        "Galvanized steel": 1.36
    },
    "USA": {
        "Magnets": 60000,
        "Liquid helium": 12,
        "Cu": 9.1,
        "Al": 2.6,
        "Nb": 774,
        "Ti": 10,
        "Capacitor": 0.933333333,
        "Fibre Glass": 2.024,
        "Epoxy resin": 6.4,
        "ABS": 0.5175,
        "GaAs": 32,
        "Rn-316": 4.083333333,
        "Deionized water": 0.9,
        "Teflon": 1.2,
        "Kapton Tape": 0.465,
        "Foam Damper": 8.533333333,
        "Plastic": 1.824,
        "Polypropylene": 1.713333333,
        "Non Magnetic Motor": 410,
        "Silicon gel": 11.7,
        "Fibre optic wire": 1.9,
        "PET": 7.5,
        "Anti Bacterial vinyl": 4,
        "Emi Paint": 23.75,
        "LEDs": 0.45,
        "Lcds Monitor": 340,
        "Lion battery": 55,
        "Brass": 7.5,
        "Inductor": 1.1,
        "Mosfets": 19,
        "FGA": 200,
        "Lc Filters": 3,
        "LDMOS": 230,
        "GAN": 245,
        "SiGe BJTs": 75,
        "VSWR": 54,
        "RF Coaxial": 5.111111111,
        "SiGe Trans": 7.5,
        "Gold": 65,
        "Optical isolator": 20,
        "Rubber": 7,
        "Galvanized steel": 1.52
    },
    "Germany": {
        "Magnets": 62000,
        "Liquid helium": 11.9,
        "Cu": 9.1,
        "Al": 2.6,
        "Nb": 756,
        "Ti": 10,
        "Capacitor": 0.933333333,
        "Fibre Glass": 2.024,
        "Epoxy resin": 6.4,
        "ABS": 0.50625,
        "GaAs": 32,
        "Rn-316": 4.025,
        "Deionized water": 0.87,
        "Teflon": 1.2,
        "Kapton Tape": 0.465,
        "Foam Damper": 8.4,
        "Plastic": 1.824,
        "Polypropylene": 1.713333333,
        "Non Magnetic Motor": 410,
        "Silicon gel": 11.7,
        "Fibre optic wire": 1.9,
        "PET": 7.5,
        "Anti Bacterial vinyl": 4,
        "Emi Paint": 23.75,
        "LEDs": 0.45,
        "Lcds Monitor": 340,
        "Lion battery": 55,
        "Brass": 7.5,
        "Inductor": 1.1,
        "Mosfets": 19,
        "FGA": 200,
        "Lc Filters": 3,
        "LDMOS": 230,
        "GAN": 245,
        "SiGe BJTs": 75,
        "VSWR": 54,
        "RF Coaxial": 5.111111111,
        "SiGe Trans": 7.5,
        "Gold": 65,
        "Optical isolator": 20,
        "Rubber": 7,
        "Galvanized steel": 1.52
    },
    "Saudi Arabia": {
        "Magnets": 80000,
        "Liquid helium": 12.53333333,
        "Cu": 9.6,
        "Al": 2.771428571,
        "Nb": 90000,
        "Ti": 11,
        "Capacitor": 8,
        "Fibre Glass": 1.584,
        "Epoxy resin": 7.2,
        "ABS": 0.5625,
        "GaAs": 35.2,
        "Rn-316": 4.258333333,
        "Deionized water": 1.08,
        "Teflon": 1.32,
        "Kapton Tape": 0.54,
        "Foam Damper": 9.066666667,
        "Plastic": 2.014,
        "Polypropylene": 1.98,
        "Non Magnetic Motor": 430,
        "Silicon gel": 12.6,
        "Fibre optic wire": 2.1,
        "PET": 8.25,
        "Anti Bacterial vinyl": 4.4,
        "Emi Paint": 26.25,
        "LEDs": 0.5,
        "Lcds Monitor": 360,
        "Lion battery": 59,
        "Brass": 8,
        "Inductor": 1.2,
        "Mosfets": 21,
        "FGA": 225,
        "Lc Filters": 3.5,
        "LDMOS": 250,
        "GAN": 265,
        "SiGe BJTs": 82.5,
        "VSWR": 59,
        "RF Coaxial": 5.5,
        "SiGe Trans": 8.333333333,
        "Gold": 70,
        "Optical isolator": 22,
        "Rubber": 8,
        "Galvanized steel": 1.68
    },
    "China": {
        "Magnets": 42000,
        "Liquid helium": 10.4,
        "Cu": 7.5,
        "Al": 2.057142857,
        "Nb": 720,
        "Ti": 8,
        "Capacitor": 0.466666667,
        "Fibre Glass": 1.188,
        "Epoxy resin": 4.6,
        "ABS": 0.405,
        "GaAs": 25.6,
        "Rn-316": 3.558333333,
        "Deionized water": 0.54,
        "Teflon": 0.96,
        "Kapton Tape": 0.36,
        "Foam Damper": 6,
        "Plastic": 1.32,
        "Polypropylene": 1.26,
        "Non Magnetic Motor": 345,
        "Silicon gel": 9,
        "Fibre optic wire": 1.4,
        "PET": 6,
        "Anti Bacterial vinyl": 3.2,
        "Emi Paint": 21,
        "LEDs": 0.35,
        "Lcds Monitor": 300,
        "Lion battery": 45,
        "Brass": 6.5,
        "Inductor": 0.96,
        "Mosfets": 14,
        "FGA": 165,
        "Lc Filters": 2.3,
        "LDMOS": 190,
        "GAN": 200,
        "SiGe BJTs": 60,
        "VSWR": 42,
        "RF Coaxial": 4,
        "SiGe Trans": 5.833333333,
        "Gold": 52,
        "Optical isolator": 16,
        "Rubber": 5,
        "Galvanized steel": 1.2
    },
    "Australia": {
        "Magnets": 58000,
        "Liquid helium": 11.33333333,
        "Cu": 8.2,
        "Al": 2.457142857,
        "Nb": 800,
        "Ti": 9,
        "Capacitor": 8,
        "Fibre Glass": 1.672,
        "Epoxy resin": 6.8,
        "ABS": 0.48375,
        "GaAs": 30.4,
        "Rn-316": 3.966666667,
        "Deionized water": 0.96,
        "Teflon": 1.14,
        "Kapton Tape": 0.45,
        "Foam Damper": 7.733333333,
        "Plastic": 1.768,
        "Polypropylene": 1.62,
        "Non Magnetic Motor": 395,
        "Silicon gel": 11.1,
        "Fibre optic wire": 1.75,
        "PET": 6.75,
        "Anti Bacterial vinyl": 3.6,
        "Emi Paint": 22.5,
        "LEDs": 0.42,
        "Lcds Monitor": 330,
        "Lion battery": 52.5,
        "Brass": 7.25,
        "Inductor": 1.04,
        "Mosfets": 17.25,
        "FGA": 190,
        "Lc Filters": 2.8,
        "LDMOS": 220,
        "GAN": 230,
        "SiGe BJTs": 70,
        "VSWR": 51,
        "RF Coaxial": 4.777777778,
        "SiGe Trans": 7,
        "Gold": 60,
        "Optical isolator": 19,
        "Rubber": 6.666666667,
        "Galvanized steel": 1.44
    },
    "India": {
        "Magnets": 55000,
        "Liquid helium": 10.8,
        "Cu": 7.8,
        "Al": 2.257142857,
        "Nb": 741,
        "Ti": 8.5,
        "Capacitor": 0.6,
        "Fibre Glass": 1.32,
        "Epoxy resin": 4.8,
        "ABS": 0.4275,
        "GaAs": 27.2,
        "Rn-316": 3.733333333,
        "Deionized water": 0.63,
        "Teflon": 1.02,
        "Kapton Tape": 0.39,
        "Foam Damper": 6.533333333,
        "Plastic": 1.406,
        "Polypropylene": 1.353333333,
        "Non Magnetic Motor": 355,
        "Silicon gel": 9.6,
        "Fibre optic wire": 1.5,
        "PET": 6.25,
        "Anti Bacterial vinyl": 3.4,
        "Emi Paint": 21.5,
        "LEDs": 0.38,
        "Lcds Monitor": 310,
        "Lion battery": 47.5,
        "Brass": 6.75,
        "Inductor": 1,
        "Mosfets": 15,
        "FGA": 175,
        "Lc Filters": 2.5,
        "LDMOS": 200,
        "GAN": 210,
        "SiGe BJTs": 65,
        "VSWR": 45,
        "RF Coaxial": 4.333333333,
        "SiGe Trans": 6.333333333,
        "Gold": 55,
        "Optical isolator": 17,
        "Rubber": 5.666666667,
        "Galvanized steel": 1.28
    },
    "Brazil": {
        "Magnets": 59000,
        "Liquid helium": 12.26666667,
        "Cu": 9.3,
        "Al": 2.657142857,
        "Nb": 800,
        "Ti": 10.33333333,
        "Capacitor": 8,
        "Fibre Glass": 1.496,
        "Epoxy resin": 6.6,
        "ABS": 0.495,
        "GaAs": 32,
        "Rn-316": 4.141666667,
        "Deionized water": 1.02,
        "Teflon": 1.26,
        "Kapton Tape": 0.495,
        "Foam Damper": 8.133333333,
        "Plastic": 1.896,
        "Polypropylene": 1.8,
        "Non Magnetic Motor": 415,
        "Silicon gel": 12,
        "Fibre optic wire": 1.95,
        "PET": 7.5,
        "Anti Bacterial vinyl": 4,
        "Emi Paint": 24,
        "LEDs": 0.46,
        "Lcds Monitor": 350,
        "Lion battery": 57.5,
        "Brass": 7.75,
        "Inductor": 1.16,
        "Mosfets": 19.5,
        "FGA": 210,
        "Lc Filters": 3.2,
        "LDMOS": 240,
        "GAN": 250,
        "SiGe BJTs": 77.5,
        "VSWR": 55,
        "RF Coaxial": 5.222222222,
        "SiGe Trans": 7.833333333,
        "Gold": 67.5,
        "Optical isolator": 21,
        "Rubber": 7.333333333,
        "Galvanized steel": 1.56
    },
    "Kazakhstan": {
        "Magnets": 60000,
        "Liquid helium": 12.4,
        "Cu": 9.4,
        "Al": 2.742857143,
        "Nb": 800,
        "Ti": 10.66666667,
        "Capacitor": 8,
        "Fibre Glass": 1.54,
        "Epoxy resin": 7,
        "ABS": 0.50625,
        "GaAs": 33.6,
        "Rn-316": 4.191666667,
        "Deionized water": 1.05,
        "Teflon": 1.29,
        "Kapton Tape": 0.5025,
        "Foam Damper": 8.533333333,
        "Plastic": 1.938,
        "Polypropylene": 1.873333333,
        "Non Magnetic Motor": 425,
        "Silicon gel": 12.6,
        "Fibre optic wire": 2,
        "PET": 7.75,
        "Anti Bacterial vinyl": 4.1,
        "Emi Paint": 24.5,
        "LEDs": 0.49,
        "Lcds Monitor": 355,
        "Lion battery": 59,
        "Brass": 7.875,
        "Inductor": 1.18,
        "Mosfets": 20.25,
        "FGA": 217.5,
        "Lc Filters": 3.3,
        "LDMOS": 245,
        "GAN": 255,
        "SiGe BJTs": 80,
        "VSWR": 57.5,
        "RF Coaxial": 5.388888889,
        "SiGe Trans": 8.166666667,
        "Gold": 68.75,
        "Optical isolator": 22,
        "Rubber": 7.666666667,
        "Galvanized steel": 1.6
    },
    "Canada": {
        "Magnets": 61000,
        "Liquid helium": 11.6,
        "Cu": 8.6,
        "Al": 2.514285714,
        "Nb": 800,
        "Ti": 9.666666667,
        "Capacitor": 8,
        "Fibre Glass": 1.76,
        "Epoxy resin": 6,
        "ABS": 0.46125,
        "GaAs": 30.4,
        "Rn-316": 3.908333333,
        "Deionized water": 0.84,
        "Teflon": 1.14,
        "Kapton Tape": 0.435,
        "Foam Damper": 7.6,
        "Plastic": 1.748,
        "Polypropylene": 1.66,
        "Non Magnetic Motor": 390,
        "Silicon gel": 10.8,
        "Fibre optic wire": 1.75,
        "PET": 6.5,
        "Anti Bacterial vinyl": 3.45,
        "Emi Paint": 23,
        "LEDs": 0.42,
        "Lcds Monitor": 330,
        "Lion battery": 54,
        "Brass": 7.375,
        "Inductor": 1.06,
        "Mosfets": 18,
        "FGA": 195,
        "Lc Filters": 2.8,
        "LDMOS": 220,
        "GAN": 230,
        "SiGe BJTs": 72.5,
        "VSWR": 52,
        "RF Coaxial": 4.888888889,
        "SiGe Trans": 7.333333333,
        "Gold": 62.5,
        "Optical isolator": 19.5,
        "Rubber": 6.666666667,
        "Galvanized steel": 1.44
    },
    "Chile": {
        "Magnets": 80000,
        "Liquid helium": 11.26666667,
        "Cu": 8.2,
        "Al": 2.4,
        "Nb": 800,
        "Ti": 9.166666667,
        "Capacitor": 8,
        "Fibre Glass": 1.628,
        "Epoxy resin": 5.8,
        "ABS": 0.43875,
        "GaAs": 28.8,
        "Rn-316": 3.791666667,
        "Deionized water": 0.78,
        "Teflon": 1.08,
        "Kapton Tape": 0.405,
        "Foam Damper": 7.066666667,
        "Plastic": 1.634,
        "Polypropylene": 1.546666667,
        "Non Magnetic Motor": 370,
        "Silicon gel": 10.2,
        "Fibre optic wire": 1.65,
        "PET": 6.1,
        "Anti Bacterial vinyl": 3.225,
        "Emi Paint": 22,
        "LEDs": 0.39,
        "Lcds Monitor": 320,
        "Lion battery": 51,
        "Brass": 7,
        "Inductor": 1.02,
        "Mosfets": 17,
        "FGA": 180,
        "Lc Filters": 2.7,
        "LDMOS": 215,
        "GAN": 225,
        "SiGe BJTs": 70,
        "VSWR": 49,
        "RF Coaxial": 4.555555556,
        "SiGe Trans": 7,
        "Gold": 60,
        "Optical isolator": 18.5,
        "Rubber": 6.333333333,
        "Galvanized steel": 1.36
    },
    "Peru": {
        "Magnets": 80000,
        "Liquid helium": 11.26666667,
        "Cu": 8.2,
        "Al": 2.4,
        "Nb": 800,
        "Ti": 9.166666667,
        "Capacitor": 8,
        "Fibre Glass": 1.628,
        "Epoxy resin": 5.8,
        "ABS": 0.43875,
        "GaAs": 28.8,
        "Rn-316": 3.791666667,
        "Deionized water": 0.78,
        "Teflon": 1.08,
        "Kapton Tape": 0.405,
        "Foam Damper": 7.066666667,
        "Plastic": 1.634,
        "Polypropylene": 1.546666667,
        "Non Magnetic Motor": 370,
        "Silicon gel": 10.2,
        "Fibre optic wire": 1.65,
        "PET": 6.1,
        "Anti Bacterial vinyl": 3.225,
        "Emi Paint": 22,
        "LEDs": 0.39,
        "Lcds Monitor": 320,
        "Lion battery": 51,
        "Brass": 7,
        "Inductor": 1.02,
        "Mosfets": 17,
        "FGA": 180,
        "Lc Filters": 2.7,
        "LDMOS": 215,
        "GAN": 225,
        "SiGe BJTs": 70,
        "VSWR": 49,
        "RF Coaxial": 4.555555556,
        "SiGe Trans": 7,
        "Gold": 60,
        "Optical isolator": 18.5,
        "Rubber": 6.333333333,
        "Galvanized steel": 1.36
    },
    "Mexico": {
        "Magnets": 62000,
        "Liquid helium": 11.86666667,
        "Cu": 9.1,
        "Al": 2.6,
        "Nb": 800,
        "Ti": 10,
        "Capacitor": 8,
        "Fibre Glass": 1.672,
        "Epoxy resin": 6.3,
        "ABS": 0.4725,
        "GaAs": 30.4,
        "Rn-316": 3.966666667,
        "Deionized water": 0.9,
        "Teflon": 1.14,
        "Kapton Tape": 0.45,
        "Foam Damper": 7.733333333,
        "Plastic": 1.768,
        "Polypropylene": 1.62,
        "Non Magnetic Motor": 395,
        "Silicon gel": 11.1,
        "Fibre optic wire": 1.75,
        "PET": 6.75,
        "Anti Bacterial vinyl": 3.6,
        "Emi Paint": 22.5,
        "LEDs": 0.43,
        "Lcds Monitor": 340,
        "Lion battery": 55,
        "Brass": 7.5,
        "Inductor": 1.1,
        "Mosfets": 19,
        "FGA": 200,
        "Lc Filters": 3,
        "LDMOS": 230,
        "GAN": 245,
        "SiGe BJTs": 75,
        "VSWR": 54,
        "RF Coaxial": 5.111111111,
        "SiGe Trans": 7.5,
        "Gold": 65,
        "Optical isolator": 20,
        "Rubber": 7,
        "Galvanized steel": 1.52
    },
    "Indonesia": {
        "Magnets": 61000,
        "Liquid helium": 10.93333333,
        "Cu": 8,
        "Al": 2.257142857,
        "Nb": 800,
        "Ti": 8.666666667,
        "Capacitor": 8,
        "Fibre Glass": 1.232,
        "Epoxy resin": 5,
        "ABS": 0.41625,
        "GaAs": 28,
        "Rn-316": 3.641666667,
        "Deionized water": 0.69,
        "Teflon": 1.02,
        "Kapton Tape": 0.375,
        "Foam Damper": 6.533333333,
        "Plastic": 1.444,
        "Polypropylene": 1.393333333,
        "Non Magnetic Motor": 352.5,
        "Silicon gel": 9.9,
        "Fibre optic wire": 1.45,
        "PET": 6,
        "Anti Bacterial vinyl": 3.3,
        "Emi Paint": 21.25,
        "LEDs": 0.37,
        "Lcds Monitor": 310,
        "Lion battery": 50,
        "Brass": 6.875,
        "Inductor": 1,
        "Mosfets": 15.5,
        "FGA": 170,
        "Lc Filters": 2.6,
        "LDMOS": 205,
        "GAN": 215,
        "SiGe BJTs": 67.5,
        "VSWR": 46,
        "RF Coaxial": 4.388888889,
        "SiGe Trans": 6.5,
        "Gold": 56.25,
        "Optical isolator": 17.5,
        "Rubber": 6,
        "Galvanized steel": 1.28
    },
    "Japan": {
        "Magnets": 46000,
        "Liquid helium": 12.26666667,
        "Cu": 9.3,
        "Al": 2.657142857,
        "Nb": 800,
        "Ti": 10.33333333,
        "Capacitor": 8,
        "Fibre Glass": 1.936,
        "Epoxy resin": 6.1,
        "ABS": 0.495,
        "GaAs": 32,
        "Rn-316": 4.083333333,
        "Deionized water": 0.96,
        "Teflon": 1.2,
        "Kapton Tape": 0.465,
        "Foam Damper": 8.133333333,
        "Plastic": 1.896,
        "Polypropylene": 1.8,
        "Non Magnetic Motor": 415,
        "Silicon gel": 12,
        "Fibre optic wire": 1.95,
        "PET": 7.5,
        "Anti Bacterial vinyl": 4,
        "Emi Paint": 24,
        "LEDs": 0.46,
        "Lcds Monitor": 350,
        "Lion battery": 57.5,
        "Brass": 7.75,
        "Inductor": 1.16,
        "Mosfets": 19.5,
        "FGA": 210,
        "Lc Filters": 3.2,
        "LDMOS": 240,
        "GAN": 250,
        "SiGe BJTs": 77.5,
        "VSWR": 55,
        "RF Coaxial": 5.222222222,
        "SiGe Trans": 7.833333333,
        "Gold": 67.5,
        "Optical isolator": 21,
        "Rubber": 7.333333333,
        "Galvanized steel": 1.56
    },
    "South Korea": {
        "Magnets": 50000,
        "Liquid helium": 12,
        "Cu": 9,
        "Al": 2.571428571,
        "Nb": 800,
        "Ti": 10,
        "Capacitor": 8,
        "Fibre Glass": 1.848,
        "Epoxy resin": 5.9,
        "ABS": 0.4725,
        "GaAs": 31.2,
        "Rn-316": 4.025,
        "Deionized water": 0.93,
        "Teflon": 1.17,
        "Kapton Tape": 0.45,
        "Foam Damper": 7.866666667,
        "Plastic": 1.838,
        "Polypropylene": 1.746666667,
        "Non Magnetic Motor": 405,
        "Silicon gel": 11.4,
        "Fibre optic wire": 1.85,
        "PET": 7.1,
        "Anti Bacterial vinyl": 3.85,
        "Emi Paint": 23.5,
        "LEDs": 0.44,
        "Lcds Monitor": 345,
        "Lion battery": 56,
        "Brass": 7.5,
        "Inductor": 1.14,
        "Mosfets": 18.75,
        "FGA": 205,
        "Lc Filters": 3.1,
        "LDMOS": 235,
        "GAN": 245,
        "SiGe BJTs": 75,
        "VSWR": 53.5,
        "RF Coaxial": 5.055555556,
        "SiGe Trans": 7.5,
        "Gold": 65,
        "Optical isolator": 20.5,
        "Rubber": 7,
        "Galvanized steel": 1.52
    }
}
insurance_data = {
    "UK": 0.40,
    "USA": 0.35,
    "Germany": 0.40,
    "Saudi Arabia": 0.55,
    "China": 0.30,
    "Australia": 0.35,
    "India": 0.60,
    "Brazil": 0.65,
    "Kazakhstan": 0.75,
    "Canada": 0.30,
    "Chile": 0.55,
    "Peru": 0.65,
    "Mexico": 0.40,
    "Indonesia": 0.65,
    "Japan": 0.30,
    "South Korea": 0.40
}
setup_cost_data = {
    "UK": 2.5,
    "USA": 3.0,
    "Germany": 2.8,
    "Saudi Arabia": 3.2,
    "China": 2.0,
    "Australia": 2.6,
    "India": 2.4,
    "Brazil": 3.0,
    "Kazakhstan": 3.1,
    "Canada": 2.7,
    "Chile": 2.5,
    "Peru": 2.5,
    "Mexico": 2.9,
    "Indonesia": 2.3,
    "Japan": 3.0,
    "South Korea": 2.8
}
combined_logistics_labour = {
    "UK": 1.8,
    "USA": 2.4,
    "Germany": 2.6,
    "Saudi Arabia": 2.8,
    "China": 1.5,
    "Australia": 1.9,
    "India": 1.7,
    "Brazil": 2.5,
    "Kazakhstan": 2.6,
    "Canada": 2.0,
    "Chile": 1.8,
    "Peru": 1.8,
    "Mexico": 2.3,
    "Indonesia": 1.6,
    "Japan": 2.5,
    "South Korea": 2.2
}
uplift_data = {
    "UK": 1.1695,
    "USA": 1.2486,
    "Germany": 1.0904,
    "Saudi Arabia": 1.2034,
    "China": 1.3051,
    "Australia": 1.1356,
    "India": 1.0000,
    "Brazil": 1.3955,
    "Kazakhstan": 1.3390,
    "Canada": 1.1582,
    "Chile": 1.2938,
    "Peru": 1.2260,
    "Mexico": 1.2712,
    "Indonesia": 1.1808,
    "Japan": 1.0678,
    "South Korea": 1.1130
}
import_cost = {
    "UK": 20.0,
    "USA": 0.0,
    "Germany": 19.0,
    "Saudi Arabia": 20.75,
    "China": 13.0,
    "Australia": 10.0,
    "India": 26.85,
    "Brazil": 33.38,
    "Kazakhstan": 17.60,
    "Canada": 5.00,
    "Chile": 26.14,
    "Peru": 18.00,
    "Mexico": 16.00,
    "Indonesia": 11.00,
    "Japan": 10.00,
    "South Korea": 10.00
}
component_usage = {
    "Shim Coils": {
        "Liquid helium": 0, "Cu": 15, "Al": 0, "Nb": 2.5, "Ti": 1.5,
        "Capacitor": 0, "Fibre Glass": 0, "Epoxy resin": 4, "ABS": 2, "GaAs": 0,
        "Rn-316": 0, "Deionized water": 0, "Teflon": 0, "Kapton Tape": 0, "Foam Damper": 0,
        "Plastic": 0, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 0,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 0, "Lcds Monitor": 0,
        "Lion battery": 0, "Brass": 0, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "RF Coils": {
        "Liquid helium": 0, "Cu": 10, "Al": 1, "Nb": 0.8, "Ti": 0,
        "Capacitor": 2, "Fibre Glass": 5, "Epoxy resin": 3, "ABS": 2, "GaAs": 0.5,
        "Rn-316": 0.2, "Deionized water": 0, "Teflon": 0, "Kapton Tape": 0, "Foam Damper": 0,
        "Plastic": 0, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 0,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 0, "Lcds Monitor": 0,
        "Lion battery": 0, "Brass": 0, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "Gradient Coil": {
        "Liquid helium": 0, "Cu": 50, "Al": 0, "Nb": 0, "Ti": 0,
        "Capacitor": 0, "Fibre Glass": 0, "Epoxy resin": 3, "ABS": 0, "GaAs": 0,
        "Rn-316": 2, "Deionized water": 20, "Teflon": 0, "Kapton Tape": 0, "Foam Damper": 0,
        "Plastic": 0, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 0,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 0, "Lcds Monitor": 0,
        "Lion battery": 0, "Brass": 0, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "Patient Table": {
        "Liquid helium": 0, "Cu": 0, "Al": 2, "Nb": 0, "Ti": 3,
        "Capacitor": 0, "Fibre Glass": 0, "Epoxy resin": 0, "ABS": 0, "GaAs": 0,
        "Rn-316": 0, "Deionized water": 0, "Teflon": 0, "Kapton Tape": 0, "Foam Damper": 0,
        "Plastic": 1, "Polypropylene": 10, "Non Magnetic Motor": 1, "Silicon gel": 2, "Fibre optic wire": 1,
        "PET": 2, "Anti Bacterial vinyl": 1, "Emi Paint": 0, "LEDs": 0, "Lcds Monitor": 0,
        "Lion battery": 0, "Brass": 0, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "Operation Console": {
        "Liquid helium": 0, "Cu": 5, "Al": 0, "Nb": 0, "Ti": 0,
        "Capacitor": 0, "Fibre Glass": 0, "Epoxy resin": 0, "ABS": 0, "GaAs": 0,
        "Rn-316": 8, "Deionized water": 0, "Teflon": 0, "Kapton Tape": 0, "Foam Damper": 0,
        "Plastic": 0, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 0.3,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 1, "LEDs": 0.5, "Lcds Monitor": 2,
        "Lion battery": 1, "Brass": 0, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "PDU": {
        "Liquid helium": 0, "Cu": 3, "Al": 2, "Nb": 0, "Ti": 0,
        "Capacitor": 2, "Fibre Glass": 0, "Epoxy resin": 0, "ABS": 0, "GaAs": 0,
        "Rn-316": 0, "Deionized water": 0, "Teflon": 1, "Kapton Tape": 0.5, "Foam Damper": 0,
        "Plastic": 1, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 0,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 0, "Lcds Monitor": 0,
        "Lion battery": 2, "Brass": 1, "Inductor": 2, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "Gradient Amplifier": {
        "Liquid helium": 0, "Cu": 2, "Al": 2, "Nb": 0, "Ti": 0,
        "Capacitor": 0, "Fibre Glass": 0, "Epoxy resin": 0, "ABS": 0, "GaAs": 0,
        "Rn-316": 2, "Deionized water": 0, "Teflon": 0, "Kapton Tape": 0, "Foam Damper": 0,
        "Plastic": 0, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 0,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 0, "Lcds Monitor": 0,
        "Lion battery": 0, "Brass": 0, "Inductor": 0, "Mosfets": 6, "FGA": 1,
        "Lc Filters": 1, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "RF Amplifier": {
        "Liquid helium": 0, "Cu": 2, "Al": 1.5, "Nb": 0, "Ti": 0,
        "Capacitor": 0, "Fibre Glass": 0, "Epoxy resin": 0, "ABS": 0, "GaAs": 0,
        "Rn-316": 0, "Deionized water": 0, "Teflon": 0, "Kapton Tape": 0, "Foam Damper": 0,
        "Plastic": 0, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 0,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 0, "Lcds Monitor": 0,
        "Lion battery": 0, "Brass": 0, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 3, "GAN": 2, "SiGe BJTs": 1, "VSWR": 1,
        "RF Coaxial": 8, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "RF Receiver Assembly": {
        "Liquid helium": 0, "Cu": 8, "Al": 4, "Nb": 0, "Ti": 0,
        "Capacitor": 0, "Fibre Glass": 0, "Epoxy resin": 1, "ABS": 2, "GaAs": 0,
        "Rn-316": 0, "Deionized water": 0, "Teflon": 3, "Kapton Tape": 20, "Foam Damper": 0,
        "Plastic": 0, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 10,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 0, "Lcds Monitor": 0,
        "Lion battery": 0, "Brass": 0, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 8, "Gold": 0, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "Image Reconstruction Computer": {
        "Liquid helium": 0, "Cu": 5, "Al": 6, "Nb": 0, "Ti": 0,
        "Capacitor": 20, "Fibre Glass": 0, "Epoxy resin": 1, "ABS": 2, "GaAs": 0,
        "Rn-316": 0, "Deionized water": 0, "Teflon": 0, "Kapton Tape": 10, "Foam Damper": 0,
        "Plastic": 0, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0.12, "Fibre optic wire": 5,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 0, "Lcds Monitor": 0,
        "Lion battery": 0, "Brass": 0, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 6, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "Peripheral Devices": {
        "Liquid helium": 0, "Cu": 4, "Al": 2, "Nb": 0, "Ti": 0,
        "Capacitor": 0, "Fibre Glass": 0, "Epoxy resin": 0, "ABS": 4, "GaAs": 0,
        "Rn-316": 0, "Deionized water": 0, "Teflon": 0, "Kapton Tape": 0, "Foam Damper": 0,
        "Plastic": 0, "Polypropylene": 2, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 0,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 1, "Lcds Monitor": 3,
        "Lion battery": 0, "Brass": 0, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 1, "Rubber": 0,
        "Galvanized steel": 0
    },
    "MRI Safety System": {
        "Liquid helium": 0, "Cu": 5, "Al": 4, "Nb": 0, "Ti": 0,
        "Capacitor": 0, "Fibre Glass": 0, "Epoxy resin": 0, "ABS": 2, "GaAs": 0,
        "Rn-316": 6, "Deionized water": 0, "Teflon": 0, "Kapton Tape": 2, "Foam Damper": 0,
        "Plastic": 0, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 0,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 2, "Lcds Monitor": 0,
        "Lion battery": 0, "Brass": 3, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 0, "Rubber": 0,
        "Galvanized steel": 0
    },
    "RF Shielding": {
        "Liquid helium": 0, "Cu": 7, "Al": 4, "Nb": 0, "Ti": 0,
        "Capacitor": 0, "Fibre Glass": 0, "Epoxy resin": 0, "ABS": 0, "GaAs": 0,
        "Rn-316": 5, "Deionized water": 0, "Teflon": 0, "Kapton Tape": 0, "Foam Damper": 0,
        "Plastic": 3, "Polypropylene": 0, "Non Magnetic Motor": 0, "Silicon gel": 0, "Fibre optic wire": 0,
        "PET": 0, "Anti Bacterial vinyl": 0, "Emi Paint": 0, "LEDs": 0, "Lcds Monitor": 0,
        "Lion battery": 0, "Brass": 3, "Inductor": 0, "Mosfets": 0, "FGA": 0,
        "Lc Filters": 0, "LDMOS": 0, "GAN": 0, "SiGe BJTs": 0, "VSWR": 0,
        "RF Coaxial": 0, "SiGe Trans": 0, "Gold": 0, "Optical isolator": 0, "Rubber": 6,
        "Galvanized steel": 6
    },
    "System Assembly" :  {"Magnets": 1, "Liquid helium": 200
}


}
air_freight_costs = {
    "UK": {
        "UK": 0, "USA": 6900, "Germany": 650, "Saudi Arabia": 5000, "China": 9200,
        "Australia": 17000, "India": 7900, "Brazil": 9400, "Kazakhstan": 5600, "Canada": 5700,
        "Chile": 11600, "Peru": 10300, "Mexico": 8800, "Indonesia": 11700, "Japan": 9600,
        "South Korea": 8900
    },
    "USA": {
        "UK": 6900, "USA": 0, "Germany": 7300, "Saudi Arabia": 11200, "China": 11600,
        "Australia": 14500, "India": 13400, "Brazil": 7800, "Kazakhstan": 11100, "Canada": 1300,
        "Chile": 8200, "Peru": 5900, "Mexico": 1800, "Indonesia": 15600, "Japan": 10600,
        "South Korea": 10700
    },
    "Germany": {
        "UK": 650, "USA": 7300, "Germany": 0, "Saudi Arabia": 4400, "China": 8700,
        "Australia": 16200, "India": 7200, "Brazil": 9900, "Kazakhstan": 4500, "Canada": 6400,
        "Chile": 12000, "Peru": 10800, "Mexico": 9400, "Indonesia": 11300, "Japan": 9200,
        "South Korea": 8600
    },
    "Saudi Arabia": {
        "UK": 5000, "USA": 11200, "Germany": 4400, "Saudi Arabia": 0, "China": 7300,
        "Australia": 12200, "India": 4300, "Brazil": 12000, "Kazakhstan": 3500, "Canada": 11300,
        "Chile": 14000, "Peru": 13300, "Mexico": 14000, "Indonesia": 8100, "Japan": 8500,
        "South Korea": 7700
    },
    "China": {
        "UK": 9200, "USA": 11600, "Germany": 8700, "Saudi Arabia": 7300, "China": 0,
        "Australia": 8000, "India": 2300, "Brazil": 17800, "Kazakhstan": 4300, "Canada": 10200,
        "Chile": 19100, "Peru": 18000, "Mexico": 14300, "Indonesia": 4500, "Japan": 1800,
        "South Korea": 850
    },
    "Australia": {
        "UK": 17000, "USA": 14500, "Germany": 16200, "Saudi Arabia": 12200, "China": 8000,
        "Australia": 0, "India": 7900, "Brazil": 13400, "Kazakhstan": 10600, "Canada": 15500,
        "Chile": 11200, "Peru": 12600, "Mexico": 13200, "Indonesia": 5500, "Japan": 7100,
        "South Korea": 8100
    },
    "India": {
        "UK": 7900, "USA": 13400, "Germany": 7200, "Saudi Arabia": 4300, "China": 2300,
        "Australia": 7900, "India": 0, "Brazil": 15400, "Kazakhstan": 2600, "Canada": 12300,
        "Chile": 17000, "Peru": 17000, "Mexico": 14500, "Indonesia": 2300, "Japan": 5300,
        "South Korea": 4200
    },
    "Brazil": {
        "UK": 9400, "USA": 7800, "Germany": 9900, "Saudi Arabia": 12000, "China": 17800,
        "Australia": 13400, "India": 15400, "Brazil": 0, "Kazakhstan": 15000, "Canada": 8100,
        "Chile": 2600, "Peru": 3100, "Mexico": 7600, "Indonesia": 16200, "Japan": 18600,
        "South Korea": 18200
    },
    "Kazakhstan": {
        "UK": 5600, "USA": 11100, "Germany": 4500, "Saudi Arabia": 3500, "China": 4300,
        "Australia": 10600, "India": 2600, "Brazil": 15000, "Kazakhstan": 0, "Canada": 10000,
        "Chile": 17200, "Peru": 17100, "Mexico": 14100, "Indonesia": 5200, "Japan": 5700,
        "South Korea": 5100
    },
    "Canada": {
        "UK": 5700, "USA": 1300, "Germany": 6400, "Saudi Arabia": 11300, "China": 10200,
        "Australia": 15500, "India": 12300, "Brazil": 8100, "Kazakhstan": 10000, "Canada": 0,
        "Chile": 9500, "Peru": 7000, "Mexico": 3600, "Indonesia": 14700, "Japan": 10100,
        "South Korea": 10000
    },
    "Chile": {
        "UK": 11600, "USA": 8200, "Germany": 12000, "Saudi Arabia": 14000, "China": 19100,
        "Australia": 11200, "India": 17000, "Brazil": 2600, "Kazakhstan": 17200, "Canada": 9500,
        "Chile": 0, "Peru": 2500, "Mexico": 6700, "Indonesia": 16300, "Japan": 18300,
        "South Korea": 18600
    },
    "Peru": {
        "UK": 10300, "USA": 5900, "Germany": 10800, "Saudi Arabia": 13300, "China": 18000,
        "Australia": 12600, "India": 17000, "Brazil": 3100, "Kazakhstan": 17100, "Canada": 7000,
        "Chile": 2500, "Peru": 0, "Mexico": 5200, "Indonesia": 16400, "Japan": 17600,
        "South Korea": 18000
    },
    "Mexico": {
        "UK": 8800, "USA": 1800, "Germany": 9400, "Saudi Arabia": 14000, "China": 14300,
        "Australia": 13200, "India": 14500, "Brazil": 7600, "Kazakhstan": 14100, "Canada": 3600,
        "Chile": 6700, "Peru": 5200, "Mexico": 0, "Indonesia": 16600, "Japan": 12200,
        "South Korea": 12600
    },
    "Indonesia": {
        "UK": 11700, "USA": 15600, "Germany": 11300, "Saudi Arabia": 8100, "China": 4500,
        "Australia": 5500, "India": 2300, "Brazil": 16200, "Kazakhstan": 5200, "Canada": 14700,
        "Chile": 16300, "Peru": 16400, "Mexico": 16600, "Indonesia": 0, "Japan": 5900,
        "South Korea": 4500
    },
    "Japan": {
        "UK": 9600, "USA": 10600, "Germany": 9200, "Saudi Arabia": 8500, "China": 1800,
        "Australia": 7100, "India": 5300, "Brazil": 18600, "Kazakhstan": 5700, "Canada": 10100,
        "Chile": 18300, "Peru": 17600, "Mexico": 12200, "Indonesia": 5900, "Japan": 0,
        "South Korea": 1200
    },
    "South Korea": {
        "UK": 8900, "USA": 10700, "Germany": 8600, "Saudi Arabia": 7700, "China": 850,
        "Australia": 8100, "India": 4200, "Brazil": 18200, "Kazakhstan": 5100, "Canada": 10000,
        "Chile": 18600, "Peru": 18000, "Mexico": 12600, "Indonesia": 4500, "Japan": 1200,
        "South Korea": 0
    }
}
shipping_distances = {
    "UK": {
        "UK": 0, "USA": 5900, "Germany": 850, "Saudi Arabia": 6200, "China": 19000,
        "Australia": 23000, "India": 16100, "Brazil": 9600, "Kazakhstan": 7900, "Canada": 17200,
        "Chile": 12900, "Peru": 13300, "Mexico": 13600, "Indonesia": 17500, "Japan": 20000,
        "South Korea": 19600
    },
    "USA": {
        "UK": 5900, "USA": 0, "Germany": 6400, "Saudi Arabia": 11600, "China": 20200,
        "Australia": 24000, "India": 21300, "Brazil": 7400, "Kazakhstan": 13600, "Canada": 8300,
        "Chile": 9200, "Peru": 7700, "Mexico": 4600, "Indonesia": 20600, "Japan": 22000,
        "South Korea": 21400
    },
    "Germany": {
        "UK": 850, "USA": 6400, "Germany": 0, "Saudi Arabia": 5600, "China": 18400,
        "Australia": 22500, "India": 15400, "Brazil": 10300, "Kazakhstan": 7400, "Canada": 17000,
        "Chile": 13600, "Peru": 14000, "Mexico": 13900, "Indonesia": 17200, "Japan": 19400,
        "South Korea": 19000
    },
    "Saudi Arabia": {
        "UK": 6200, "USA": 11600, "Germany": 5600, "Saudi Arabia": 0, "China": 12600,
        "Australia": 17500, "India": 5700, "Brazil": 14400, "Kazakhstan": 4000, "Canada": 19800,
        "Chile": 17200, "Peru": 16800, "Mexico": 17600, "Indonesia": 10700, "Japan": 13000,
        "South Korea": 12700
    },
    "China": {
        "UK": 19000, "USA": 20200, "Germany": 18400, "Saudi Arabia": 12600, "China": 0,
        "Australia": 7000, "India": 5600, "Brazil": 23800, "Kazakhstan": 9200, "Canada": 9600,
        "Chile": 18700, "Peru": 18400, "Mexico": 17000, "Indonesia": 3100, "Japan": 1900,
        "South Korea": 1600
    },
    "Australia": {
        "UK": 23000, "USA": 24000, "Germany": 22500, "Saudi Arabia": 17500, "China": 7000,
        "Australia": 0, "India": 8300, "Brazil": 19000, "Kazakhstan": 13700, "Canada": 13600,
        "Chile": 11100, "Peru": 13100, "Mexico": 14900, "Indonesia": 5500, "Japan": 7300,
        "South Korea": 8000
    },
    "India": {
        "UK": 16100, "USA": 21300, "Germany": 15400, "Saudi Arabia": 5700, "China": 5600,
        "Australia": 8300, "India": 0, "Brazil": 21800, "Kazakhstan": 4000, "Canada": 18900,
        "Chile": 20700, "Peru": 20400, "Mexico": 20400, "Indonesia": 3150, "Japan": 6480,
        "South Korea": 6110
    },
    "Brazil": {
        "UK": 9600, "USA": 7400, "Germany": 10300, "Saudi Arabia": 14400, "China": 23800,
        "Australia": 19000, "India": 21800, "Brazil": 0, "Kazakhstan": 17300, "Canada": 15800,
        "Chile": 3400, "Peru": 4400, "Mexico": 6200, "Indonesia": 23500, "Japan": 24800,
        "South Korea": 24500
    },
    "Kazakhstan": {
        "UK": 7900, "USA": 13600, "Germany": 7400, "Saudi Arabia": 4000, "China": 9200,
        "Australia": 13700, "India": 4000, "Brazil": 17300, "Kazakhstan": 0, "Canada": 15300,
        "Chile": 18900, "Peru": 18600, "Mexico": 17600, "Indonesia": 10200, "Japan": 11600,
        "South Korea": 11100
    },
    "Canada": {
        "UK": 17200, "USA": 8300, "Germany": 17000, "Saudi Arabia": 19800, "China": 9600,
        "Australia": 13600, "India": 18900, "Brazil": 15800, "Kazakhstan": 15300, "Canada": 0,
        "Chile": 14000, "Peru": 13800, "Mexico": 8200, "Indonesia": 14300, "Japan": 11400,
        "South Korea": 11600
    },
    "Chile": {
        "UK": 12900, "USA": 9200, "Germany": 13600, "Saudi Arabia": 17200, "China": 18700,
        "Australia": 11100, "India": 20700, "Brazil": 3400, "Kazakhstan": 18900, "Canada": 14000,
        "Chile": 0, "Peru": 1500, "Mexico": 6300, "Indonesia": 17800, "Japan": 19800,
        "South Korea": 19500
    },
    "Peru": {
        "UK": 13300, "USA": 7700, "Germany": 14000, "Saudi Arabia": 16800, "China": 18400,
        "Australia": 13100, "India": 20400, "Brazil": 4400, "Kazakhstan": 18600, "Canada": 13800,
        "Chile": 1500, "Peru": 0, "Mexico": 5800, "Indonesia": 18300, "Japan": 19300,
        "South Korea": 19200
    },
    "Mexico": {
        "UK": 13600, "USA": 4600, "Germany": 13900, "Saudi Arabia": 17600, "China": 17000,
        "Australia": 14900, "India": 20400, "Brazil": 6200, "Kazakhstan": 17600, "Canada": 8200,
        "Chile": 6300, "Peru": 5800, "Mexico": 0, "Indonesia": 17200, "Japan": 18400,
        "South Korea": 18600
    },
    "Indonesia": {
        "UK": 17500, "USA": 20600, "Germany": 17200, "Saudi Arabia": 10700, "China": 3100,
        "Australia": 5500, "India": 3150, "Brazil": 23500, "Kazakhstan": 10200, "Canada": 14300,
        "Chile": 17800, "Peru": 18300, "Mexico": 17200, "Indonesia": 0, "Japan": 5500,
        "South Korea": 5200
    },
    "Japan": {
        "UK": 20000, "USA": 22000, "Germany": 19400, "Saudi Arabia": 13000, "China": 1900,
        "Australia": 7300, "India": 6480, "Brazil": 24800, "Kazakhstan": 11600, "Canada": 11400,
        "Chile": 19800, "Peru": 19300, "Mexico": 18400, "Indonesia": 5500, "Japan": 0,
        "South Korea": 1400
    },
    "South Korea": {
        "UK": 19600, "USA": 21400, "Germany": 19000, "Saudi Arabia": 12700, "China": 1600,
        "Australia": 8000, "India": 6110, "Brazil": 24500, "Kazakhstan": 11100, "Canada": 11600,
        "Chile": 19500, "Peru": 19200, "Mexico": 18600, "Indonesia": 5200, "Japan": 1400,
        "South Korea": 0
    }
}
labour_data = {
    'UK': {'Unskilled': 12.2, 'Semi-Skilled': 15, 'Skilled': 22.5, 'Highly Skilled': 40},
    'USA': {'Unskilled': 10.5, 'Semi-Skilled': 15, 'Skilled': 22.5, 'Highly Skilled': 40},
    'Germany': {'Unskilled': 12.8, 'Semi-Skilled': 17, 'Skilled': 26, 'Highly Skilled': 45},
    'Saudi Arabia': {'Unskilled': 4.5, 'Semi-Skilled': 6.5, 'Skilled': 11, 'Highly Skilled': 21.5},
    'China': {'Unskilled': 3, 'Semi-Skilled': 5, 'Skilled': 10, 'Highly Skilled': 17.5},
    'Australia': {'Unskilled': 15, 'Semi-Skilled': 19, 'Skilled': 26, 'Highly Skilled': 40},
    'India': {'Unskilled': 0.8, 'Semi-Skilled': 1.75, 'Skilled': 4.25, 'Highly Skilled': 10},
    'Brazil': {'Unskilled': 2.5, 'Semi-Skilled': 4.25, 'Skilled': 7, 'Highly Skilled': 13.5},
    'Kazakhstan': {'Unskilled': 1.5, 'Semi-Skilled': 3, 'Skilled': 5, 'Highly Skilled': 10},
    'Canada': {'Unskilled': 14, 'Semi-Skilled': 18, 'Skilled': 24, 'Highly Skilled': 40},
    'Chile': {'Unskilled': 4, 'Semi-Skilled': 5.5, 'Skilled': 9, 'Highly Skilled': 13.5},
    'Peru': {'Unskilled': 2.5, 'Semi-Skilled': 3.5, 'Skilled': 6, 'Highly Skilled': 10},
    'Mexico': {'Unskilled': 4, 'Semi-Skilled': 5, 'Skilled': 8.5, 'Highly Skilled': 14},
    'Indonesia': {'Unskilled': 1.5, 'Semi-Skilled': 2, 'Skilled': 4, 'Highly Skilled': 8},
    'Japan': {'Unskilled': 10, 'Semi-Skilled': 12, 'Skilled': 16.5, 'Highly Skilled': 30},
    'South Korea': {'Unskilled': 7.2, 'Semi-Skilled': 9, 'Skilled': 13.5, 'Highly Skilled': 25}
}
assembly_cost = {
    'UK': 21120.0, 
    'USA': 16000.0,
    'Germany': 20240.0,
    'Saudi Arabia': 22880.0,
    'China': 10560.0,
    'Australia': 22000.0,
    'India': 7040.0,
    'Brazil': 12320.0,
    'Kazakhstan': 11440.0,
    'Canada': 17600.0,
    'Chile': 13200.0,
    'Peru': 9680.0,
    'Mexico': 14080.0,
    'Indonesia': 7920.0,
    'Japan': 18480.0,
    'South Korea': 16720.0
}
overtime_data = {
    'UK': {'Unskilled': 18.3, 'Semi-Skilled': 22.5, 'Skilled': 33.8, 'Highly Skilled': 60},
    'USA': {'Unskilled': 15.8, 'Semi-Skilled': 22.5, 'Skilled': 33.8, 'Highly Skilled': 60},
    'Germany': {'Unskilled': 19.2, 'Semi-Skilled': 25.5, 'Skilled': 39, 'Highly Skilled': 67.5},
    'Saudi Arabia': {'Unskilled': 6.8, 'Semi-Skilled': 9.8, 'Skilled': 16.5, 'Highly Skilled': 32.3},
    'China': {'Unskilled': 4.5, 'Semi-Skilled': 7.5, 'Skilled': 15, 'Highly Skilled': 26.3},
    'Australia': {'Unskilled': 22.5, 'Semi-Skilled': 28.5, 'Skilled': 39, 'Highly Skilled': 60},
    'India': {'Unskilled': 1.2, 'Semi-Skilled': 2.63, 'Skilled': 6.38, 'Highly Skilled': 15},
    'Brazil': {'Unskilled': 3.8, 'Semi-Skilled': 6.38, 'Skilled': 10.5, 'Highly Skilled': 20.3},
    'Kazakhstan': {'Unskilled': 2.3, 'Semi-Skilled': 4.5, 'Skilled': 7.5, 'Highly Skilled': 15},
    'Canada': {'Unskilled': 21, 'Semi-Skilled': 27, 'Skilled': 36, 'Highly Skilled': 60},
    'Chile': {'Unskilled': 6, 'Semi-Skilled': 8.25, 'Skilled': 13.5, 'Highly Skilled': 20.3},
    'Peru': {'Unskilled': 3.8, 'Semi-Skilled': 5.3, 'Skilled': 9, 'Highly Skilled': 15},
    'Mexico': {'Unskilled': 6, 'Semi-Skilled': 7.5, 'Skilled': 12.8, 'Highly Skilled': 21},
    'Indonesia': {'Unskilled': 2.3, 'Semi-Skilled': 3, 'Skilled': 6, 'Highly Skilled': 12},
    'Japan': {'Unskilled': 15, 'Semi-Skilled': 18, 'Skilled': 24.8, 'Highly Skilled': 45},
    'South Korea': {'Unskilled': 10.8, 'Semi-Skilled': 13.5, 'Skilled': 20.3, 'Highly Skilled': 37.5}
}
packaging_costs = {
    "UK": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.45,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.12,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.65,
        "Thermal Insulated Boxes": 0.5
    },
    "USA": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.45,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.2,
        "Cardboard Tubes": 0.12,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.65,
        "Thermal Insulated Boxes": 0.5
    },
    "Germany": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.45,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.12,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.65,
        "Thermal Insulated Boxes": 0.5
    },
    "Saudi Arabia": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.54,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.2,
        "Cardboard Tubes": 0.14,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.78,
        "Thermal Insulated Boxes": 0.6
    },
    "China": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.45,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.2,
        "Cardboard Tubes": 0.12,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.65,
        "Thermal Insulated Boxes": 0.6
    },
    "Australia": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.45,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.12,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.65,
        "Thermal Insulated Boxes": 0.5
    },
    "India": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.54,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.14,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.78,
        "Thermal Insulated Boxes": 0.6
    },
    "Brazil": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.54,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.12,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.78,
        "Thermal Insulated Boxes": 0.6
    },
    "Kazakhstan": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.54,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.14,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.78,
        "Thermal Insulated Boxes": 0.6
    },
    "Canada": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.45,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.12,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.65,
        "Thermal Insulated Boxes": 0.5
    },
    "Chile": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.54,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.14,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.78,
        "Thermal Insulated Boxes": 0.6
    },
    "Peru": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.54,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.14,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.78,
        "Thermal Insulated Boxes": 0.6
    },
    "Mexico": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.54,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.14,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.78,
        "Thermal Insulated Boxes": 0.6
    },
    "Indonesia": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.54,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.14,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.78,
        "Thermal Insulated Boxes": 0.6
    },
    "Japan": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.45,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.12,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.65,
        "Thermal Insulated Boxes": 0.5
    },
    "South Korea": {
        "Fiberboard Boxes": 0.15,
        "Plastic Drums": 0.23,
        "Steel Drums": 0.3,
        "Wooden Crates": 0.4,
        "Vacuum-Sealed Foil Bags": 0.45,
        "Anti-Static Bags": 0.27,
        "Polyethylene Bags": 0.1,
        "Bubble/Foam Wrap": 0.18,
        "IBC Totes": 0.24,
        "Cardboard Tubes": 0.12,
        "Shrink-Wrapped Pallets": 0.08,
        "Cushioned Metal Boxes": 0.65,
        "Thermal Insulated Boxes": 0.5
    }
}
labour_hours = {
    "Shim Coils": {
        "Unskilled": 2.3,
        "Semi-Skilled": 4.6,
        "Skilled": 27.6,
        "Highly Skilled": 11.5
    },
    "RF Coils": {
        "Unskilled": 5.8,
        "Semi-Skilled": 11.5,
        "Skilled": 69,
        "Highly Skilled": 28.8
    },
    "Gradient Coil": {
        "Unskilled": 7.5,
        "Semi-Skilled": 22.5,
        "Skilled": 90,
        "Highly Skilled": 30
    },
    "Patient Table": {
        "Unskilled": 6.9,
        "Semi-Skilled": 20.7,
        "Skilled": 34.5,
        "Highly Skilled": 6.9
    },
    "PDU": {
        "Unskilled": 4.4,
        "Semi-Skilled": 11.6,
        "Skilled": 10.2,
        "Highly Skilled": 2.9
    },
    "Gradient Amplifier": {
        "Unskilled": 2.3,
        "Semi-Skilled": 4.6,
        "Skilled": 27.6,
        "Highly Skilled": 11.5
    },
    "RF Amplifier": {
        "Unskilled": 1.8,
        "Semi-Skilled": 5.2,
        "Skilled": 21,
        "Highly Skilled": 7
    },
    "RF Receiver Assembly": {
        "Unskilled": 2,
        "Semi-Skilled": 4,
        "Skilled": 24,
        "Highly Skilled": 10
    },
    "Image Reconstruction Computer": {
        "Unskilled": 1.4,
        "Semi-Skilled": 2.9,
        "Skilled": 17.4,
        "Highly Skilled": 7.2
    },
    "Peripheral Devices": {
        "Unskilled": 3.4,
        "Semi-Skilled": 9.2,
        "Skilled": 9.2,
        "Highly Skilled": 1.2
    },
    "MRI Safety System": {
        "Unskilled": 2.9,
        "Semi-Skilled": 8.7,
        "Skilled": 14.5,
        "Highly Skilled": 2.9
    },
    "RF Shielding": {
        "Unskilled": 69,
        "Semi-Skilled": 69,
        "Skilled": 69,
        "Highly Skilled": 23
    }}


System_Integration = {
        "Unskilled": 58,
        "Semi-Skilled": 122.8,
        "Skilled": 580.4,
        "Highly Skilled": 397.7
    }
PRICE_SHIP = 0.000001 #PER KG PER KM
PRICE_AIR  = 0.003   #per kg per km 
                

m = gp.Model("prodplan") 
#VARIABLES ADDITION 

# Add continuous variables y[i,j,k]
y = m.addVars(E, B, A, vtype=GRB.CONTINUOUS, name="y")
y_BINARY = m.addVars(E, B, A, lb=0, ub= 1, vtype=GRB.BINARY, name="y_BINARY")
country_part = m.addVars (B, A, lb=0, ub= 1, vtype=GRB.BINARY, name="country_part")
assembly_cont = m.addVars (A, lb=0, ub= 1, vtype=GRB.BINARY, name="assembly_cont")
air_parts =  m.addVars (B, A, A, lb=0, ub= 1, vtype=GRB.BINARY, name="air_parts")
ship_parts =  m.addVars (B, A, A, lb=0, ub= 1, vtype=GRB.BINARY, name="ship_parts")
air_components = m.addVars (E, A, A,lb=0, ub= 1, vtype=GRB.BINARY, name="air_components")
ship_components = m.addVars (E, A, A, lb=0, ub= 1, vtype=GRB.BINARY, name="ship_components")
amount_air_parts = m.addVars(B, A, A, vtype=GRB.CONTINUOUS, name="mount_air_parts")
amount_ship_parts = m.addVars(B, A, A, vtype=GRB.CONTINUOUS, name="amount_ship_part")
amount_air_components = m.addVars(E, A, A, vtype=GRB.CONTINUOUS, name="amount_air_components")
amount_ship_components = m.addVars(E, A, A, vtype=GRB.CONTINUOUS, name="amount_ship_components")
num_labours = m.addVars(D, B, A, lb=0, ub= 100, vtype=GRB.CONTINUOUS, name="num_labours")
num_days =  m.addVars(D, B, A, lb=0, ub= 30, vtype=GRB.CONTINUOUS, name="num_days")
pacaging_binary_parts = m.addVars (C, B, A, lb=0, ub= 1, vtype=GRB.BINARY, name="pacaging_binary_parts")
pacaging_binary_components = m.addVars (C, E, A, lb=0, ub= 1, vtype=GRB.BINARY, name="pacaging_binary_components")
pacaging_parts = m.addVars (C,B,A, vtype=GRB.CONTINUOUS, name="pacaging_parts")
pacaging_components =m.addVars (C,E,A,vtype=GRB.CONTINUOUS, name="pacaging_components")
num_days_assembly = m.addVars ( D, A, lb=0, ub= 30, vtype=GRB.CONTINUOUS, name="num_days_assembly")
num_labours_assembly = m.addVars (D, A, lb=0, ub= 300, vtype=GRB.CONTINUOUS, name="num_labours_assembly")
# Binary variables (1 if shipping method is used for part b from country a to India)
use_air_to_india = m.addVars(B, A, vtype=GRB.BINARY, name="use_air_to_india")
use_sea_to_india = m.addVars(B, A, vtype=GRB.BINARY, name="use_sea_to_india")


#Objective Function

# Objective Function: Minimize Total Cost
total_sourcing_cost = gp.quicksum(
    # Sourcing Cost for Components
    Sourcing_cost[a][e] * y[e, b, a] * y_BINARY[e, b, a]
    for e in E for b in B for a in A ) 
total_labour_cost = gp.quicksum(
    # Labour Cost for Manufacturing Parts
    labour_data[a][d] * num_labours[d, b, a] * num_days[d, b, a] * country_part[b, a]
    for d in D for b in B for a in A)

total_integration_setup = gp.quicksum (assembly_cont[a] * assembly_cost[a] for a in A)

total_integration_cost = gp.quicksum(
    # Labour Cost for System Integration
    labour_data[a][d] * num_labours_assembly[d, a] * num_days_assembly[d, a] * assembly_cont[a]
    for d in D for a in A) 
total_pacaging_parts =  gp.quicksum(
    # Packaging Cost for Parts
    packaging_costs[a][c] * pacaging_parts[c, b, a] * pacaging_binary_parts[c, b, a]
    for c in C for b in B for a in A)
total_pacaging_components = gp.quicksum(
    # Packaging Cost for Components
    packaging_costs[a][c] * pacaging_components[c, e, a] * pacaging_binary_components[c, e, a]
    for c in C for e in E for a in A)

total_air_cost_parts = gp.quicksum(
    # Air Freight Cost for Parts (only where distance is available)
    PRICE_AIR * amount_air_parts[b, a1, a2] * air_freight_costs[a1][a2] * air_parts[b, a1, a2]
    for b in B for a1 in A for a2 in A ) 

total_ship_cost_parts = gp.quicksum(
    PRICE_SHIP * amount_ship_parts[b, a1, a2] * shipping_distances[a1][a2] * ship_parts[b, a1, a2]
    for b in B for a1 in A for a2 in A
    
)

total_air_cost_components =  gp.quicksum(
    # Air Freight Cost for Components (only where distance is available)
    PRICE_AIR * amount_air_components[e, a1, a2] * air_freight_costs[a1][a2] * air_components[e, a1, a2]
    for e in E for a1 in A for a2 in A )
total_ship_cost_components =  gp.quicksum(
    # Shipping Cost for Components (only where distance is available)
    PRICE_SHIP * amount_ship_components[e, a1, a2] * shipping_distances[a1][a2] * ship_components[e, a1, a2]
    for e in E for a1 in A for a2 in A 
    if not math.isnan(shipping_distances[a1][a2]) and not math.isinf(shipping_distances[a1][a2])) 
    
total_insurance_cost_components = gp.quicksum(insurance_data[a] * Sourcing_cost[a][e] * y[e, b, a] * y_BINARY[e, b, a] * 0.01 
for a in A for b in B for e in E
)

total_setup_cost =  gp.quicksum(
    # Setup Cost
    setup_cost_data[a] * Sourcing_cost[a][e] * y[e, b, a] * y_BINARY[e, b, a] * 0.01 
    for a in A for b in B for e in E) 

total_import_cost_components =  gp.quicksum(
    # Import Cost
    import_cost[a] * total_sourcing_cost * 0.01 * country_part[b, a]

    for a in A for b in B)

total_risk_cost = gp.quicksum ( (uplift_data[a] - 1 ) * Sourcing_cost[a][e] * y[e, b, a] * y_BINARY[e, b, a]
for a in A for b in B for e in E ) 

market = "India"
# Revised cost calculations using binaries
india_air_cost = gp.quicksum(
    PRICE_AIR * amount_air_parts[b, a, market] * air_freight_costs[a][market] * use_air_to_india[b, a]
    for b in B for a in A
)
india_sea_cost = gp.quicksum(
    PRICE_SHIP * amount_ship_parts[b, a, market] * shipping_distances[a][market] * use_sea_to_india[b, a]
    for b in B for a in A if not math.isnan(shipping_distances[a][market]) and not math.isinf(shipping_distances[a][market]))
# Combine all costs into the total cost
# Enable non-convex quadratic handling
m.Params.NonConvex = 2

# 1. LINEAR TERMS (use directly)
linear_integration_setup = total_integration_setup  # Already linear

# 2. QUADRATIC TERMS (keep as is)
quadratic_objective = (
    total_sourcing_cost +
    total_pacaging_parts +
    total_pacaging_components +
    total_air_cost_parts +
    total_ship_cost_parts +
    total_air_cost_components +
    total_ship_cost_components +
    total_insurance_cost_components +
    total_setup_cost +
    total_risk_cost +
    india_air_cost +
    india_sea_cost
)

# 3. NON-LINEAR TERMS (reformulate)
# 3a. Labour cost reformulation
labour_prod = m.addVars(D, B, A, name="labour_prod")
for d in D:
    for b in B:
        for a in A:
            # Constrain product when country_part=1
            m.addConstr(labour_prod[d,b,a] <= num_labours[d,b,a] * num_days[d,b,a])
            m.addConstr(labour_prod[d,b,a] <= country_part[b,a] * 1e6)
            m.addConstr(labour_prod[d,b,a] >= 0)

linear_labour_cost = gp.quicksum(
    labour_data[a][d] * labour_prod[d,b,a]
    for d in D for b in B for a in A
)

# 3b. Integration cost reformulation (same pattern)
integration_prod = m.addVars(D, A, name="integration_prod")
for d in D:
    for a in A:
        m.addConstr(integration_prod[d,a] <= num_labours_assembly[d,a] * num_days_assembly[d,a])
        m.addConstr(integration_prod[d,a] <= assembly_cont[a] * 1e6)
        m.addConstr(integration_prod[d,a] >= 0)

linear_integration_cost = gp.quicksum(
    labour_data[a][d] * integration_prod[d,a]
    for d in D for a in A
)

total_import_cost_components = gp.quicksum(
    import_cost[a] * Sourcing_cost[a][e] * y[e, b, a] * y_BINARY[e, b, a] * country_part[b, a] * 0.01
    for a in A for b in B for e in E
)



# FINAL LINEARIZED OBJECTIVE
linearized_objective = (
    linear_integration_setup +
    quadratic_objective +
    linear_labour_cost +
    linear_integration_cost )


 # 0) BIG‐M PARAMETERS
M_qty = 1e6
eps   = 1e-6

# 1) NON-NEGATIVITY
for e in E:
    for b in B:
        for a in A:
            m.addConstr(y[e, b, a] >= 0,
                        name=f"nonneg_y_{e}_{b}_{a}")
for e in E:
    for b in B:
        m.addConstr(gp.quicksum(y_BINARY[e, b, a] for a in A) <= 1, name=f"ExactOneAssignment_e{e}_b{b}")


for e in E:
    for i in A:
        for j in A:
            m.addConstr(amount_air_components[e, i, j]  >= 0,
                        name=f"nonneg_air_comp_{e}_{i}_{j}")
            m.addConstr(amount_ship_components[e, i, j] >= 0,
                        name=f"nonneg_sea_comp_{e}_{i}_{j}")

for b in B:
    for i in A:
        for j in A:
            m.addConstr(amount_air_parts[b, i, j]  >= 0,
                        name=f"nonneg_air_part_{b}_{i}_{j}")
            m.addConstr(amount_ship_parts[b, i, j] >= 0,
                        name=f"nonneg_sea_part_{b}_{i}_{j}")

# 2) COMPONENT-USAGE (Bill of Materials)
for b in B:
    for a in A:
        for e in E:
            required_qty = component_usage
m.addConstr(y[e, b, a] >= required_qty[b][e] * country_part[b, a],
                    name=f"component_usage_{e}_{b}_{a}"
                )



# 3) SOURCING: continuous y ↔ binary y_BINARY
for e in E:
    for b in B:
        for a in A:
            # upper-bound: if y_BINARY=0 then y=0
            m.addConstr(
                y[e, b, a] <= M_qty * y_BINARY[e, b, a],
                name=f"bigM_source_ub_{e}_{b}_{a}"
            )
            # lower-bound: if y_BINARY=1 then y≥eps
            m.addConstr(
                y[e, b, a] >= eps * y_BINARY[e, b, a],
                name=f"bigM_source_lb_{e}_{b}_{a}"
            )

# 4) COMPONENT SHIPPING: amount_*_components ↔ air_components / ship_components
for e in E:
    for i in A:
        for j in A:
            m.addConstr(
                amount_air_components[e, i, j]
                <= M_qty * air_components[e, i, j],
                name=f"bigM_air_comp_{e}_{i}_{j}"
            )
            m.addConstr(
                amount_ship_components[e, i, j]
                <= M_qty * ship_components[e, i, j],
                name=f"bigM_sea_comp_{e}_{i}_{j}"
            )

# 5) PART SHIPPING: amount_*_parts ↔ air_parts / ship_parts
for b in B:
    for i in A:
        for j in A:
            m.addConstr(
                amount_air_parts[b, i, j]
                <= M_qty * air_parts[b, i, j],
                name=f"bigM_air_part_{b}_{i}_{j}"
            )
            m.addConstr(
                amount_ship_parts[b, i, j]
                <= M_qty * ship_parts[b, i, j],
                name=f"bigM_sea_part_{b}_{i}_{j}"
            )
       
for b in B:
    m.addConstr(
        gp.quicksum(amount_air_parts[b, a, "India"] + amount_ship_parts[b, a, "India"] for a in A) >= 1,
        name=f"demand_{b}_India"
    )

for b in B:
    m.addConstr(
        gp.quicksum(country_part[b, a] for a in A) == 1,
        name=f"unique_mfg_{b}"
    )


for b in B:
    for a in A:
        m.addConstr(
            gp.quicksum(amount_air_parts[b, a, d] + amount_ship_parts[b, a, d] for d in A) ==
            country_part[b, a],
            name=f"flow_bal_{b}_{a}"
        )

m.addConstr(gp.quicksum(assembly_cont[a] for a in A) == 1, name="one_assembly_site")

for a in A:
    m.addConstr(
        gp.quicksum(y["Magnets", b, a] for b in B) >= 1 * assembly_cont[a],
        name=f"magnet_required_at_assembly_{a}"
    )
    m.addConstr(
        gp.quicksum(y["Liquid helium", b, a] for b in B) >= 200 * assembly_cont[a],
        name=f"helium_required_at_assembly_{a}"
    )
for b in B:
    for a in A:
        total_available = gp.quicksum(
            num_labours[d, b, a] * num_days[d, b, a] * 8 for d in D
        )
        total_required = gp.quicksum(
            labour_hours[b][d] * country_part[b, a] for d in D
        )
        m.addConstr(
            total_available >= total_required,
            name=f"labour_hours_requirement_{b}_{a}"
        )
for a in A:
    total_assembly_available = gp.quicksum(
        num_labours_assembly[d, a] * num_days_assembly[d, a] * 8 for d in D
    )
    total_assembly_required = gp.quicksum(
        System_Integration[d] * assembly_cont[a] for d in D
    )
    m.addConstr(
        total_assembly_available >= total_assembly_required,
        name=f"assembly_labour_requirement_{a}"
    )


m.setObjective( linearized_objective, GRB.MINIMIZE)
m.optimize()
# print("\n--- Assembly Labour Schedule ---\n")
# for a in A:
#     if assembly_cont[a].X > 0.5:  # assembly chosen
#         print(f"\nAssembly Location: {a}")


# print("\n--- Part Manufacturing ---")
# for b in B:
#     for a in A:
#         if country_part[b, a].X > 0.5:
#             print(f"🛠️ Part '{b}' is manufactured in {a}")


# print("\n--- Component Sourcing ---")
# for e in E:
#     for b in B:
#         for a in A:
#             if y_BINARY[e, b, a].X > 0.5:
#                 print(f"📦 Component '{e}' for part '{b}' is sourced from {a} — amount: {y[e,b,a].X:.2f}")



# print("\n--- Part Transport (Air) ---")
# for b in B:
#     for a1 in A:
#         for a2 in A:
#             if air_parts[b, a1, a2].X > 0.5:
#                 print(f"✈️ Part '{b}' shipped by air from {a1} to {a2} — Qty: {amount_air_parts[b,a1,a2].X:.2f}")

# print("\n--- Part Transport (Sea) ---")
# for b in B:
#     for a1 in A:
#         for a2 in A:
#             if ship_parts[b, a1, a2].X > 0.5:
#                 print(f"🚢 Part '{b}' shipped by sea from {a1} to {a2} — Qty: {amount_ship_parts[b,a1,a2].X:.2f}")



# print("\n--- Packaging Choices for Parts ---")
# for c in C:
#     for b in B:
#         for a in A:
#             if pacaging_binary_parts[c, b, a].X > 0.5:
#                 print(f"📦 Part '{b}' in {a} uses packaging: {c} — Qty: {pacaging_parts[c,b,a].X:.2f}")


# import csv

# with open("component_flows.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["Component", "Part", "Country", "Amount"])
#     for e in E:
#         for b in B:
#             for a in A:
#                 if y_BINARY[e, b, a].X > 0.5:
#                     writer.writerow([e, b, a, y[e,b,a].X])

import sys

# Redirect all stdout to a file
sys.stdout = open('output_log.txt', 'w')

# Your optimization reporting code
if m.status == GRB.OPTIMAL:
    print(" Optimization succesl.")
    print(" Objective Value (Total Cost):", m.ObjVal)
    print("\n Variables with value exactly 1:\n")
    
    for var in m.getVars():
        if abs(var.X - 1) < 1e-6:
            print(f"{var.VarName} = {var.X}")
else:
    print(" Optimization failed. Status code:", m.status)

# Reset stdout back to terminal (optional)
sys.stdout.close()
sys.stdout = sys.__stdout__



   


"""whole_cost = (
    total_air_cost_components + total_risk_cost + total_air_cost_parts +
    total_import_cost_components + total_sourcing_cost + total_insurance_cost_components +
    total_integration_cost + total_labour_cost + total_setup_cost +
    total_pacaging_components + total_pacaging_parts + total_integration_setup +
    total_ship_cost_components + total_ship_cost_parts + india_air_cost + india_sea_cost 
)"""

"""# After defining all your variables and the objective function, but before optimizing:
m.setObjective(whole_cost, GRB.MINIMIZE)  # Add this before optimizing
# Example constraint: Each part must be manufactured in exactly one country
for b in B:
    m.addConstr(gp.quicksum(country_part[b,a] for a in A) == 1, name=f"manufacture_{b}")
print("\nObjective Function Analysis:")
print("-" * 30)

# Basic model information
print(f"Model sense: {'MINIMIZE' if m.ModelSense == GRB.MINIMIZE else 'MAXIMIZE'}")
print(f"Number of quadratic terms: {m.NumQNZs}")

# Get the objective expression
obj = m.getObjective()

# Determine if linear or quadratic
if m.NumQNZs == 0:
    print("Objective type: LINEAR")
    print(f"Number of linear terms: {obj.size()}")
    
    # Print first few linear terms
    print("\nFirst 5 linear terms:")
    for i in range(min(5, obj.size())):
        var = obj.getVar(i)
        coeff = obj.getCoeff(i)
        print(f"  {var.VarName}: {coeff}")
else:
    print("Objective type: QUADRATIC")
    print(f"Number of linear terms: {obj.size() - 2*m.NumQNZs}")
    print(f"Number of quadratic terms: {m.NumQNZs}")
    
    # For quadratic objectives, we need a different approach to examine terms
    print("\nQuadratic objective structure:")
    print("(Note: Detailed quadratic term inspection requires more advanced methods)")

# Additional diagnostics
print("\nModel statistics:")
print(f"Variables: {m.NumVars}")
print(f"Linear constraints: {m.NumConstrs}")
print(f"Quadratic constraints: {m.NumQConstrs}")
m.optimize()"""

