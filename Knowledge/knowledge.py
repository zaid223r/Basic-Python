import termcolor
from logic import *

# Define symbols
ChemicalExposure = Symbol("Chemical Exposure")
NoiseExposure = Symbol("Noise Exposure")
PhysicalStrain = Symbol("Physical Strain")

Symptoms1 = [Symbol("Eye Irritation"), Symbol("Hearing Loss"), Symbol("Muscle Pain")]
Symptoms2 = [Symbol("Respiratory Issues"), Symbol("Headache"), Symbol("Back Pain")]

# Define logical model
symbols = [ChemicalExposure, NoiseExposure, PhysicalStrain] + Symptoms1 + Symptoms2

def check_occupational_hazards(knowledge):
    for symbol in symbols:
        if model_check(knowledge, symbol):
            termcolor.cprint(f"{symbol}: YES", "green")
        elif not model_check(knowledge, Not(symbol)):
            print(f"{symbol}: MAYBE")

# Construct the logical model (students need to complete this part)

# Example knowledge
knowledge = And(
    Biconditional(ChemicalExposure, And(Symptoms1[0],Symptoms2[0])), 
    Biconditional(NoiseExposure, And(Symptoms1[1],Symptoms2[1])),
    Biconditional(PhysicalStrain, And(Or(Symptoms1[2],Symptoms2[2]),Symptoms2[0])), #respiratory issues may be because of physicalstrain
    Implication(Symptoms1[1],Symptoms2[1]), #in my opinion every one that have hearing loss will have headache too
    Implication(Symptoms1[0],Symptoms2[1]), #in my opinion every one that have eye irritation will have headache too
    #Symptoms1[1],       #if you uncommented this you will have solution
    
    #Symptoms1[2],Symptoms2[0],       #if you uncommented this you will have solution
    
    #PhysicalStrain, Symptoms1[0],     #if you uncommented this you will have solution
)

check_occupational_hazards(knowledge)
