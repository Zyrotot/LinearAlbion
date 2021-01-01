Tier = "5" # 4/5/6/7/8

Focus = "N" # Y/N

Type = "F" # Blacksmith/Imbuer/Fletcher

Materials = {"Cloth" : 1248,
             "Metal" : 1806,
             "Wood" : 609,
             "Leather": 300}

#------------------------------------------------------------------------------------------------------

from pulp import *
import math

prob = LpProblem("LinearAlbion",LpMaximize)

JournalFame = {"4" : 1200,
               "5" : 2400,
               "6" : 4800,
               "7" : 9600,
               "8" : 19200}

FameGenerated = {"4": {"2Hweapon":720, "1Hweapon":540, "BigArmor":360, "SmallArmor":180},
                 "5": {"2Hweapon":2880, "1Hweapon":2160, "BigArmor":1440, "SmallArmor":720},
                 "6": {"2Hweapon":8640, "1Hweapon":6480, "BigArmor":4320, "SmallArmor":2160},
                 "7": {"2Hweapon":20640, "1Hweapon":15480, "BigArmor":10320, "SmallArmor":5160},
                 "8": {"2Hweapon":44640, "1Hweapon":33480, "BigArmor":22320, "SmallArmor":11160}}

clothCost = {"BattleAxe" : 0,
             "Halberd" : 0,
             "Great_Axe" : 0,
             "Boots" : 0,
             "Shield" : 0,
             "1H_Crossbow" : 0,
             "2H_Crossbow" : 0,
             "Armor" : 0,
             "1H_Hammer" : 0,
             "2H_Hammer" : 12,
             "Helmet" : 0,
             "1H_Mace" : 8,
             "2H_Mace" : 12,
             "1H_Sword" : 0,
             "2H_Sword" : 0,
             "Robe" : 16,
             "Sandals" : 8,
             "Cowl" : 8,
             "1H_Damage_Staff" : 0,
             "2H_Damage_Staff" : 0,
             "1H_Holy_Staff" : 8,
             "2H_Holy_Staff" : 12,
             "SpellTome" : 4,
             "Torch" : 4,
             "1H_Nature_Staff" : 8,
             "2H_Nature_staff" : 12,
             "1H_Dagger" : 0,
             "2H_Dagger" : 0,
             "Claws" : 0,
             "Staff" : 0,
             "1H_Spear" : 0,
             "Pike" : 0,
             "Glaive" : 0,
             "Jacket" : 0,
             "Boots" : 0,
             "Hood" : 0}

metalCost = {"BattleAxe" : 16,
             "Halberd" : 12,
             "Great_Axe" : 20,
             "Boots" : 8,
             "Shield" : 4,
             "1H_Crossbow" : 8,
             "2H_Crossbow" : 12,
             "Armor" : 16,
             "1H_Hammer" : 24,
             "2H_Hammer" : 20,
             "Helmet" : 8,
             "1H_Mace" : 16,
             "2H_Mace" : 20,
             "1H_Sword" : 16,
             "2H_Sword" : 20,
             "Robe" : 0,
             "Sandals" : 0,
             "Cowl" : 0,
             "1H_Damage_Staff" : 8,
             "2H_Damage_Staff" : 12,
             "1H_Holy_Staff" : 0,
             "2H_Holy_Staff" : 0,
             "SpellTome" : 0,
             "Torch" : 0,
             "1H_Nature_Staff" : 0,
             "2H_Nature_staff" : 0,
             "1H_Dagger" : 12,
             "2H_Dagger" : 16,
             "Claws" : 12,
             "Staff" : 12,
             "1H_Spear" : 8,
             "Pike" : 12,
             "Glaive" : 20,
             "Jacket" : 0,
             "Boots" : 0,
             "Hood" : 0}

woodCost = {"BattleAxe" : 8,
             "Halberd" : 20,
             "Great_Axe" : 12,
             "Boots" : 0,
             "Shield" : 4,
             "1H_Crossbow" : 16,
             "2H_Crossbow" : 20,
             "Armor" : 0,
             "1H_Hammer" : 0,
             "2H_Hammer" : 0,
             "Helmet" : 0,
             "1H_Mace" : 0,
             "2H_Mace" : 0,
             "1H_Sword" : 0,
             "2H_Sword" : 0,
             "Robe" : 0,
             "Sandals" : 0,
             "Cowl" : 0,
             "1H_Damage_Staff" : 16,
             "2H_Damage_Staff" : 20,
             "1H_Holy_Staff" : 16,
             "2H_Holy_Staff" : 20,
             "SpellTome" : 0,
             "Torch" : 4,
             "1H_Nature_Staff" : 16,
             "2H_Nature_staff" : 20,
             "1H_Dagger" : 0,
             "2H_Dagger" : 0,
             "Claws" : 0,
             "Staff" : 0,
             "1H_Spear" : 16,
             "Pike" : 20,
             "Glaive" : 12,
             "Jacket" : 0,
             "Boots" : 0,
             "Hood" : 0}

leatherCost = {"BattleAxe" : 0,
               "Halberd" : 0,
               "Great_Axe" : 0,
               "Boots" : 0,
               "Shield" : 0,
               "1H_Crossbow" : 0,
               "2H_Crossbow" : 0,
               "Armor" : 0,
               "1H_Hammer" : 0,
               "2H_Hammer" : 0,
               "Helmet" : 0,
               "1H_Mace" : 0,
               "2H_Mace" : 0,
               "1H_Sword" : 8,
               "2H_Sword" : 12,
               "Robe" : 0,
               "Sandals" : 0,
               "Cowl" : 0,
               "1H_Damage_Staff" : 0,
               "2H_Damage_Staff" : 0,
               "1H_Holy_Staff" : 0,
               "2H_Holy_Staff" : 0,
               "SpellTome" : 4,
               "Torch" : 0,
               "1H_Nature_Staff" : 0,
               "2H_Nature_staff" : 0,
               "1H_Dagger" : 12,
               "2H_Dagger" : 16,
               "Claws" : 20,
               "Staff" : 20,
               "1H_Spear" : 0,
               "Pike" : 0,
               "Glaive" : 0,
               "Jacket" : 16,
               "Boots" : 8,
               "Hood" : 8}

craftedItems = {"BattleAxe" : 0,
                "Halberd" : 0,
                "Great_Axe" : 0,
                "Boots" : 0,
                "Shield" : 0,
                "1H_Crossbow" : 0,
                "2H_Crossbow" : 0,
                "Armor" : 0,
                "1H_Hammer" : 0,
                "2H_Hammer" : 0,
                "Helmet" : 0,
                "1H_Mace" : 0,
                "2H_Mace" : 0,
                "1H_Sword" : 0,
                "2H_Sword" : 0,
                "Robe" : 0,
                "Sandals" : 0,
                "Cowl" : 0,
                "1H_Damage_Staff" : 0,
                "2H_Damage_Staff" : 0,
                "1H_Holy_Staff" : 0,
                "2H_Holy_Staff" : 0,
                "SpellTome" : 0,
                "Torch" : 0,
                "1H_Nature_Staff" : 0,
                "2H_Nature_staff" : 0,
                "1H_Dagger" : 0,
                "2H_Dagger" : 0,
                "Claws" : 0,
                "Staff" : 0,
                "1H_Spear" : 0,
                "Pike" : 0,
                "Glaive" : 0,
                "Jacket" : 0,
                "Boots" : 0,
                "Hood" : 0}

RRR = {"N" : 0.248,
       "Y" : 0.479}

focusMessage = {"N" : "Focus was not used",
                "Y" : "Focus was used"}

totalFame = 0
generatedFame = 1

BA = LpVariable("BattleAxe",0,None,LpInteger)
HA = LpVariable("Halberd",0,None,LpInteger)
GA = LpVariable("Great_Axe",0,None,LpInteger)
BO = LpVariable("Boots",0,None,LpInteger)
SH = LpVariable("Shield",0,None,LpInteger)
CR = LpVariable("1H_Crossbow",0,None,LpInteger)
HC = LpVariable("2H_Crossbow",0,None,LpInteger)
AR = LpVariable("Armor",0,None,LpInteger)
HR = LpVariable("1H_Hammer",0,None,LpInteger)
HH = LpVariable("2H_Hammer",0,None,LpInteger)
HE = LpVariable("Helmet",0,None,LpInteger)
MA = LpVariable("1H_Mace",0,None,LpInteger)
HM = LpVariable("2H_Mace",0,None,LpInteger)
SW = LpVariable("1H_Sword",0,None,LpInteger)
HS = LpVariable("2H_Sword",0,None,LpInteger)

RO = LpVariable("Robe",0,None,LpInteger)
SA = LpVariable("Sandals",0,None,LpInteger)
CO = LpVariable("Cowl",0,None,LpInteger)
DS = LpVariable("1H_Damage_Staff",0,None,LpInteger)
HD = LpVariable("2H_Damage_Staff",0,None,LpInteger)
HS = LpVariable("1H_Holy_Staff",0,None,LpInteger)
HHO = LpVariable("2H_Holy_Staff",0,None,LpInteger)
ST = LpVariable("SpellTome",0,None,LpInteger)

TO = LpVariable("Torch",0,None,LpInteger)
NS = LpVariable("1H_Nature_Staff",0,None,LpInteger)
HN = LpVariable("2H_Nature_staff",0,None,LpInteger)
DA = LpVariable("1H_Dagger",0,None,LpInteger)
HDA = LpVariable("2H_Dagger",0,None,LpInteger)
CL = LpVariable("Claws",0,None,LpInteger)
SF = LpVariable("Staff",0,None,LpInteger)
SP = LpVariable("1H_Spear",0,None,LpInteger)
PI = LpVariable("Pike",0,None,LpInteger)
GL = LpVariable("Glaive",0,None,LpInteger)
JA = LpVariable("Jacket",0,None,LpInteger)
BO = LpVariable("Boots",0,None,LpInteger)
HO = LpVariable("Hood",0,None,LpInteger)

clothUse = {"B" : 12*(HH + HM) + 8*MA,
            "I" : 16*RO + 12*HHO + 8*(SA + CO + HS) + 4*ST,
            "F" : 12*HN + 8*NS + 4*TO}

metalUse = {"B" : 24*HR + 20*(GA + HH + HM + HS) + 16*(BA + AR + MA + SW) + 12*(HA + HC) + 8*(BO + CR + HE) + 4*SH,
            "I" : 12*HD + 8*DS,
            "F" : 20*GL + 16*HDA + 12*(DA + CL + SF + PI) + 8*SP}

woodUse = {"B" : 20*(HA + HC) + 16*CR + 12*GA + 8*BA + 4*SH,
           "I" : 20*(HD + HHO) + 16*(DS + HS),
           "F" : 20*(HN + PI) + 16*(NS + SP) + 12*GL + 4*TO}

leatherUse = {"B" : 8*SW + 12*HS,
              "I" : 4*ST,
              "F" : 20*(CL + SF) + 16*(HDA + JA) + 12*DA + 8*(BO + HO)}

typeFame = {"B" : FameGenerated[Tier]["2Hweapon"]*(HA + GA + HC + HH + HM) + FameGenerated[Tier]["1Hweapon"]*(BA + CR + HR + MA) + FameGenerated[Tier]["BigArmor"]*AR + FameGenerated[Tier]["SmallArmor"]*(BO + SH + HE),
            "I" : FameGenerated[Tier]["2Hweapon"]*(HD + HHO) + FameGenerated[Tier]["1Hweapon"]*(DS + HS) + FameGenerated[Tier]["BigArmor"]*RO + FameGenerated[Tier]["SmallArmor"]*(SA + CO + ST),
            "F" : FameGenerated[Tier]["2Hweapon"]*(HN + HDA + CL + SF + PI + GL) + FameGenerated[Tier]["1Hweapon"]*(NS + DA + SP) + FameGenerated[Tier]["BigArmor"]*JA + FameGenerated[Tier]["SmallArmor"]*(TO + BO + HO)}

prob += typeFame[Type], "totalFame"

while generatedFame > 0:

    prob.constraints["clothUsed"] =  clothUse[Type] <= Materials["Cloth"]
    prob.constraints["metalUsed"] =  metalUse[Type] <= Materials["Metal"]
    prob.constraints["woodUsed"] =  woodUse[Type] <= Materials["Wood"]
    prob.constraints["leatherUsed"] =  leatherUse[Type] <= Materials["Leather"]

    prob.writeLP("LinearAlbion.lp")

    stat = prob.solve(PULP_CBC_CMD(msg=0))

    if(stat == 1):
        for v in prob.variables():
            if(v.varValue != 0):
                craftedItems[v.name] += v.varValue
                Materials["Cloth"] -= math.ceil(clothCost[v.name]*v.varValue*(1-RRR[Focus]))
                Materials["Metal"] -= math.ceil(metalCost[v.name]*v.varValue*(1-RRR[Focus]))
                Materials["Wood"] -= math.ceil(woodCost[v.name]*v.varValue*(1-RRR[Focus]))
                Materials["Leather"] -= math.ceil(leatherCost[v.name]*v.varValue*(1-RRR[Focus]))

        totalFame += value(prob.objective)
        generatedFame = value(prob.objective)

    else:
        generatedFame = 0

print("Total fame generated = ", totalFame)
print("Total journals filled = ", math.floor(totalFame/JournalFame[Tier]))
print(focusMessage[Focus])
print("\n")
print("Materials leftover")
print("Cloth:", Materials["Cloth"])
print("Metal:", Materials["Metal"])
print("Wood:", Materials["Wood"])
print("Leather:", Materials["Leather"])
print("\n")
for v in craftedItems:
    if(craftedItems[v] != 0):
        print(v, "=", craftedItems[v])

#print(vars(prob))
