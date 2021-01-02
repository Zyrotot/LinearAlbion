Tier = "5" # 4/5/6/7/8

Focus = "N" # Y/N

Type = "B" # Blacksmith/Imbuer/Fletcher/All

Materials = {"Cloth" : 376,
             "Metal" : 135,
             "Wood" : 40,
             "Leather": 0}

#--------------------------------------------------------------------

from pulp import LpProblem, LpVariable, LpMaximize, LpInteger, value, PULP_CBC_CMD
from data import *
import math

prob = LpProblem("LinearAlbion", LpMaximize)

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
HSW = LpVariable("2H_Sword",0,None,LpInteger)

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
SO = LpVariable("Shoes",0,None,LpInteger)
HO = LpVariable("Hood",0,None,LpInteger)

clothUse = {"B" : 12*(HH + HM) + 8*MA,
            "I" : 16*RO + 12*HHO + 8*(SA + CO + HS) + 4*ST,
            "F" : 12*HN + 8*NS + 4*TO,
            "A" : 16*RO + 12*(HH + HM + HN + HHO) + 8*(MA + SA + CO + HS + NS) + 4*(ST + TO)}

metalUse = {"B" : 24*HR + 20*(GA + HH + HM + HSW) + 16*(BA + AR + MA + SW) + 12*(HA + HC) + 8*(BO + CR + HE) + 4*SH,
            "I" : 12*HD + 8*DS,
            "F" : 20*GL + 16*HDA + 12*(DA + CL + SF + PI) + 8*SP,
            "A" : 24*HR + 20*(GL + GA + HH + HM + HSW) + 16*(BA + AR + MA + SW + HDA) + 12*(HA + HC + HD + DA + CL + SF + PI) + 8*(BO + CR + HE + DS + SP) + 4*SH}

woodUse = {"B" : 20*(HA + HC) + 16*CR + 12*GA + 8*BA + 4*SH,
           "I" : 20*(HD + HHO) + 16*(DS + HS),
           "F" : 20*(HN + PI) + 16*(NS + SP) + 12*GL + 4*TO,
           "A" : 20*(HA + HC + HD + HHO + HN + PI) + 16*(CR + DS + HS + NS + SP) + 12*(GA + GL) + 8*BA + 4*(TO + SH)}

leatherUse = {"B" : 12*HSW + 8*SW,
              "I" : 4*ST,
              "F" : 20*(CL + SF) + 16*(HDA + JA) + 12*DA + 8*(SO + HO),
              "A" : 20*(CL + SF) + 16*(HDA + JA) + 12*(DA + HSW) + 8*(SW + SO + HO) + 4*ST}

typeFame = {"B" : FameGenerated[Tier]["2Hweapon"]*(HA + GA + HC + HH + HM + HSW) + FameGenerated[Tier]["1Hweapon"]*(BA + CR + HR + MA + SW) + FameGenerated[Tier]["BigArmor"]*AR + FameGenerated[Tier]["SmallArmor"]*(BO + SH + HE),
            "I" : FameGenerated[Tier]["2Hweapon"]*(HD + HHO) + FameGenerated[Tier]["1Hweapon"]*(DS + HS) + FameGenerated[Tier]["BigArmor"]*RO + FameGenerated[Tier]["SmallArmor"]*(SA + CO + ST),
            "F" : FameGenerated[Tier]["2Hweapon"]*(HN + HDA + CL + SF + PI + GL) + FameGenerated[Tier]["1Hweapon"]*(NS + DA + SP) + FameGenerated[Tier]["BigArmor"]*JA + FameGenerated[Tier]["SmallArmor"]*(TO + SO + HO),
            "A" : FameGenerated[Tier]["2Hweapon"]*(HA + GA + HC + HH + HM + HSW + HD + HHO + HN + HDA + CL + SF + PI + GL) + FameGenerated[Tier]["1Hweapon"]*(BA + CR + HR + MA + SW + DS + HS + NS + DA + SP) + FameGenerated[Tier]["BigArmor"]*(AR + RO + JA) + FameGenerated[Tier]["SmallArmor"]*(BO + SH + HE + SA + CO + ST + TO + SO + HO)}

prob += typeFame[Type], "totalFame"

while generatedFame > 0:

    prob.constraints["clothUsed"] = clothUse[Type] <= Materials["Cloth"]
    prob.constraints["metalUsed"] = metalUse[Type] <= Materials["Metal"]
    prob.constraints["woodUsed"] = woodUse[Type] <= Materials["Wood"]
    prob.constraints["leatherUsed"] = leatherUse[Type] <= Materials["Leather"]

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
if Type == "A":
    fameTree = {"Imbuer" : 0,
                "Blacksmith" : 0,
                "Fletcher" : 0}

    for v in craftedItems:
        if(craftedItems[v] != 0):
            fameTree[itemTree[v]] += craftedItems[v]*FameGenerated[Tier][itemType[v]]

    for t in fameTree:
        print(t,"journals filled:", math.floor(fameTree[t]/JournalFame[Tier]))

else:
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
