# generate random gear based of a randomizer/bossrush
import sys
import os
import shutil
import random
import math
import datetime

# user settings here
# give 2 spell after every base
generate_spells=0
# remove weapon from the pool before next roll
unique_weapons=1
# one weapon for whole thing
one_weapon=0
#

blood=["BloodType_Brute", "BloodType_Corruption", "BloodType_Warrior", "BloodType_Scholar", "BloodType_Draculin", "BloodType_Creature", "BloodType_Worker", "BloodType_Rogue", "BloodType_Mutant", "BloodType_None"]
copper_weapon=["give_copper_sword;", "give_copper_axe;",  "give_copper_cros;", "give_copper_mace;", "give_copper_bow;", "give_copper_spear;"]
rcopper_weapon=["give_rcopper_sword;", "give_rcopper_axe;", "give_rcopper_cros;", "give_rcopper_mace;", "give_rcopper_bow;", "give_rcopper_spear;"]
iron_weapon=["give_iron_sword;", "give_iron_axe;", "give_iron_cros;", "give_iron_bow;", "give_iron_mace;", "give_iron_spear;", "give_iron_gsword;", "give_iron_reaper;", "give_iron_claws;", "give_iron_whip;", "give_iron_daggers;", "give_iron_pistol;", "give_iron_slashers;", "give_iron_tblade;"]
riron_weapon=["give_riron_whip;", "give_riron_tblade;", "give_riron_sword;", "give_riron_spear;", "give_riron_slash;", "give_riron_reap;", "give_riron_pistol;", "give_riron_mace;", "give_riron_bow;", "give_riron_gsword;", "give_riron_dagger;", "give_riron_cros;", "give_riron_claws;", "give_riron_axe;"]
sriron_weapon=["GenerateLegendaryWeapon Item_Weapon_Axe_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_sword_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_cros_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_bow_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_mace_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_spear_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_gsword_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_reaper_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_claws_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_whip_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_daggers_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_pistol_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_slashers_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_tblade_Legendary_T06;"]
silver_weapon=["give_dsilver_wh;", "give_dsilver_tb;", "give_dsilver_sw;", "give_dsilver_sp;", "give_dsilver_sl;", "give_dsilver_re;", "give_dsilver_pi;", "give_dsilver_mc;", "give_dsilver_lb;", "give_dsilver_gs;", "give_dsilver_dg;", "give_dsilver_cb;", "give_dsilver_cl;", "give_dsilver_ax;"]
rsilver_weapon=["give_san_wh;", "give_san_tb;", "give_san_sw;", "give_san_sp;", "give_san_sl;", "give_san_re;", "give_san_pi;", "give_san_mc;", "give_san_lb;", "give_san_gs;", "give_san_dg;", "give_san_cb;", "give_san_cl;", "give_san_ax;"]
srsilver_weapon=["give_rsan_wh;", "give_rsan_tb;", "give_rsan_sw;", "give_rsan_sp;", "give_rsan_sl;", "give_rsan_re;", "give_rsan_pi;", "give_rsan_mc;", "give_rsan_lb;", "give_rsan_gs;", "give_rsan_dg;", "give_rsan_cb;", "give_rsan_cl;", "give_rsan_ax;"]
cloth_armour=["give_clothr_armour;", "give_clothb_armour;", "give_cloths_armour;", "give_clothw_armour;"]
rcotton_armour=["give_cottonr_armour;", "give_cottonb_armour;", "give_cottons_armour;", "give_cottonw_armour;"]
rsilk_armour=["give_silkw_armour;", "give_silkb_armour;", "give_silks_armour;", "give_silkr_armour;"]
drac_armour=["give_drac_w_bo;", "give_drac_w_ch;", "give_drac_w_gl;", "give_drac_w_le;"]
drac_boot=["give_drac_b_bo;", "give_drac_r_bo;", "give_drac_s_bo;", "give_drac_w_bo;"]
drac_gloves=["give_drac_b_gl;", "give_drac_r_gl;", "give_drac_s_gl;", "give_drac_w_gl;"]
drac_legs=["give_drac_b_le;", "give_drac_r_le;", "give_drac_s_le;", "give_drac_w_le;"]
drac_chest=["give_drac_b_ch;", "give_drac_r_ch;", "give_drac_s_ch;", "give_drac_w_ch;"]
t1_magic=["give_ring_red;", "give_ring_gre;", "give_ring_pin;", "give_ring_tea;", "give_ring_yel;", "give_ring_blu;"]
t2_magic=["give_rpendant_red;", "give_rpendant_yel;", "give_rpendant_gre;", "give_rpendant_tea;", "give_rpendant_blu;", "give_rpendant_vio;"]
t3_magic=["give_amu_red;", "give_amu_yel;", "give_amu_gre;", "give_amu_tea;", "give_amu_blu;", "give_amu_vio;"]

config=one_weapon*4+unique_weapons*2+generate_spells*1
x = datetime.datetime.now()
now=str(x.year)+"_"+str(x.month)+"_"+str(x.day)+"_"+str(x.hour)+"_"+str(x.minute)+"_"+str(x.second);
template_prof_path="./../misc/DESKTOP-asdf.prof"
random_prof_path="./../examples/random_"+str(config)+"_"+now+".prof"

def add_blood(boss_loot, level_local):
    random_blood_lvl = level_local+random.randrange(math.ceil(-level/2),level)
    random_blood_lvl = 100 if random_blood_lvl > 100 else random_blood_lvl
    if((level/100+random.random())>1.0):
        boss_loot=boss_loot+"ConsumeBlood " + random.choice(blood[1:9]) + " " + str(random_blood_lvl) + " " + random.choice(blood[1:9]) + " " + str(random.randrange(30,100)) + " " + str(random.randrange(1,3))+ ";"
    else:
        boss_loot=boss_loot+" ConsumeBlood " + random.choice(blood[1:10]) + " " + str(random_blood_lvl) + ";"
    return(boss_loot)

def add_weapon(boss_loot, level_local):
    global copper_weapon, rcopper_weapon, iron_weapon, riron_weapon, sriron_weapon, silver_weapon, rsilver_weapon, srsilver_weapon
    if(level_local>= 27 and level_local<30):
        if(unique_weapons==0):
            boss_loot=boss_loot+copper_weapon.remove(random.choice(copper_weapon))
        else:
            if(len(copper_weapon)>1):
                boss_loot=boss_loot+copper_weapon.pop(random.randrange(1,len(copper_weapon)))
            elif(len(copper_weapon)==1):
                boss_loot=boss_loot+copper_weapon.pop()
        if(one_weapon==1):
                copper_weapon=[]
    elif(level_local>= 30 and level_local<40):
        if(unique_weapons==0):
            boss_loot=boss_loot+rcopper_weapon.remove(random.choice(rcopper_weapon))
        else:
            if(len(rcopper_weapon)>1):
                boss_loot=boss_loot+rcopper_weapon.pop(random.randrange(1,len(rcopper_weapon)))
            elif(len(rcopper_weapon)==1):
                boss_loot=boss_loot+rcopper_weapon.pop()
        if(one_weapon==1):
                rcopper_weapon=[]
    elif(level_local>= 40 and level_local<53):
        if(unique_weapons==0):
            boss_loot=boss_loot+iron_weapon.remove(random.choice(iron_weapon))
        else:
            if(len(iron_weapon)>1):
                boss_loot=boss_loot+iron_weapon.pop(random.randrange(1,len(iron_weapon)))
            elif(len(iron_weapon)==1):
                boss_loot=boss_loot+iron_weapon.pop()
        if(one_weapon==1):
                iron_weapon=[]
    elif(level_local>= 53 and level_local<63):
        if(unique_weapons==0):
            boss_loot=boss_loot+riron_weapon.remove(random.choice(riron_weapon))
        else:
            if(len(riron_weapon)>1):
                boss_loot=boss_loot+riron_weapon.pop(random.randrange(1,len(riron_weapon)))
            elif(len(riron_weapon)==1):
                boss_loot=boss_loot+riron_weapon.pop()
        if(one_weapon==1):
                riron_weapon=[]
    elif(level_local>= 63 and level_local<70):
        if(unique_weapons==0):
            boss_loot=boss_loot+sriron_weapon.remove(random.choice(sriron_weapon))
        else:
            if(len(sriron_weapon)>1):
                boss_loot=boss_loot+sriron_weapon.pop(random.randrange(1,len(sriron_weapon)))
            elif(len(sriron_weapon)==1):
                boss_loot=boss_loot+sriron_weapon.pop()
        if(one_weapon==1):
                sriron_weapon=[]
    elif(level_local>= 70 and level_local<80):
        if(unique_weapons==0):
            boss_loot=boss_loot+silver_weapon.remove(random.choice(silver_weapon))
        else:
            if(len(silver_weapon)>1):
                boss_loot=boss_loot+silver_weapon.pop(random.randrange(1,len(silver_weapon)))
            elif(len(silver_weapon)==1):
                boss_loot=boss_loot+silver_weapon.pop()
        if(one_weapon==1):
                silver_weapon=[]
    elif(level_local>= 80 and level_local<88):
        if(unique_weapons==0):
            boss_loot=boss_loot+rsilver_weapon.remove(random.choice(rsilver_weapon))
        else:
            if(len(rsilver_weapon)>1):
                boss_loot=boss_loot+rsilver_weapon.pop(random.randrange(1,len(rsilver_weapon)))
            elif(len(rsilver_weapon)==1):
                boss_loot=boss_loot+rsilver_weapon.pop()
        if(one_weapon==1):
                rsilver_weapon=[]
    elif(level_local>= 88):
        if(unique_weapons==0):
            boss_loot=boss_loot+srsilver_weapon.remove(random.choice(srsilver_weapon))
        else:
            if(len(srsilver_weapon)>1):
                boss_loot=boss_loot+srsilver_weapon.pop(random.randrange(1,len(srsilver_weapon)))
            elif(len(srsilver_weapon)==1):
                boss_loot=boss_loot+srsilver_weapon.pop()
        if(one_weapon==1):
                srsilver_weapon=[]
    return(boss_loot)

def add_thing(boss_loot, the_thing):
    boss_loot=boss_loot+random.choice(the_thing)
    return(boss_loot)

def add_tofile(fileptr, boss_string):
    fileptr.write(boss_string+"\n")


# create random profile if there is none
if(os.path.isfile(random_prof_path)==False):
    shutil.copyfile(template_prof_path, random_prof_path)

file1 = open(random_prof_path, "a+")
# file1.find
file1.write("\nrandomizer_code_below Console.MultiCommand give_vermin; give_vermin;\n")

tier=1
level=20
stol="stone_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, add_blood(stol,level))
rufl="rufus_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, add_blood(rufl,level))
level=27
kell="kelly_loot Console.MultiCommand give_cloth_armour;"
add_tofile(file1, add_blood(add_weapon(kell,level),level))
swil="swine_loot Console.MultiCommand give \"[Name]Gravedigger Ring - Item_MagicSource_General_T03_GravediggerRing - Guid: -1588051702\"; give \"[Name]Grave Dust - Item_Ingredient_Gravedust - Guid: -608131642\" 50;"
add_tofile(file1, add_blood(add_weapon(swil,level),level))
gral="grayson_loot Console.MultiCommand give_vermin;"
add_tofile(file1, add_blood(add_weapon(gral,level),level))
level=30
clil="clive_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, add_blood(add_weapon(clil,level),level))
chal="chaos_loot Console.MultiCommand give_vermin 10; give_brew_p; give_brew_s;"
add_tofile(file1, add_blood(add_weapon(chal,level),level))
level=33
fisl="fish_loot Console.MultiCommand give_vermin;"
add_tofile(file1, add_thing(add_blood(add_weapon(fisl,level),level),t1_magic))
level=36
beal="bear_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, add_blood(add_weapon(beal,level),level))
nicl="nick_loot Console.MultiCommand give_vermin;"
add_tofile(file1, add_thing(add_blood(add_weapon(nicl,level),level),cloth_armour))
level=40
poll="polora_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, add_blood(add_weapon(poll,level),level))
level=43
quil="quincy_loot Console.MultiCommand give_vermin;give_vermin;"
add_tofile(file1, add_blood(add_weapon(quil,level),level))
tier=2
level=47
deal="deamon_loot Console.Multicommand give_cotton_armour; give \"[Prefab]Item_Cloak_Main_T02_Hunter - Guid: 786585343\"; give \"[Name]Minor Sun Resistance Brew - Item_Consumable_SunResistancePotion_T01 - Guid: -38051433\" 10; give_brew_p; give_brew_s; give_brew_hp 20;"
add_tofile(file1, add_blood(add_weapon(deal,level),level))
vinl="vinc_loot Console.Multicommand give \"[Name]Iron Ingot - Item_Ingredient_Mineral_IronBar - Guid: -1750550553\" 16; give \"[Name]Reinforced Plank - Item_Ingredient_ReinforcedPlank - Guid: -1397591435\" 4;"
add_tofile(file1, add_blood(add_weapon(vinl,level),level))
nunl="nun_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, add_blood(add_weapon(nunl,level),level))
horl="horse_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, add_blood(add_weapon(horl,level),level))
level=50
leal="leandr_loot Console.Multicommand give \"[Name]Scourgestone - Item_Ingredient_Scourgestone - Guid: 1005440012\" 100; give \"[Name]Scourgestone Pendant - Item_MagicSource_General_T05_Relic - Guid: -650855520\"; give \"[Prefab]Item_Consumable_DuskCaller - Guid: 1128262258\" 10; give \"[Name]Sulphur - Item_Ingredient_Mineral_Sulfur - Guid: 880699252\" 200;"
add_tofile(file1, add_blood(add_weapon(leal,level),level))
kril="kriig_loot Console.Multicommand give \"[Prefab]Item_Weapon_Reaper_T01_Bone - Guid: -152327780\"; give \"[Name]Hell’s Clarion - Item_Ingredient_Plant_HellsClarion - Guid: 813370507\" 200; give \"[Name]Undead General Helmet - Item_Headgear_GeneralHelmet - Guid: 409678749\"; GenerateLegendaryWeapon Item_Weapon_Reaper_Legendary_T06_Shattered;"
add_tofile(file1, add_blood(add_weapon(kril,level),level))
majl="maja_loot Console.Multicommand give \"[Prefab]Item_Ingredient_Research_Scroll - Guid: 2065714452\" 1000; GenerateLegendaryWeapon Item_Weapon_Sword_Legendary_T06_Shattered; give \"[Name]Rat - Item_Consumable_Eat_Rat - Guid: -869864524\" 100;"
add_tofile(file1, add_blood(add_weapon(majl,level),level))
banl="bane_loot Console.Multicommand give \"[Name]Immortal King's Greathelm - Item_Headgear_DraculaHelmet - Guid: 238268650\"; give_silver_cash 100; GenerateLegendaryWeapon Item_Weapon_Daggers_Legendary_T06_Shattered; GenerateLegendaryWeapon Item_Weapon_Slashers_Legendary_T06_Shattered;"
add_tofile(file1, add_blood(add_weapon(banl,level),level))
glal="glass_loot Console.Multicommand give \"[Name]Empty Glass Bottle - Item_Consumable_EmptyBottle - Guid: -437611596\" 10; give_pot_hp 10; give \"[Name]Blood Rose - Item_Ingredient_Plant_BloodRose - Guid: 1726420644\" 200; GenerateLegendaryWeapon Item_Weapon_Axes_Legendary_T06_Shattered;"
add_tofile(file1, add_blood(add_weapon(glal,level),level))
level=53
blel="bless_loot  Console.Multicommand give \"[Name]Holy Resistance Potion - Item_Consumable_HolyResistancePotion_T01 - Guid: 890484447\" 10; give \"[Name]Elixir of the Prowler - Item_Elixir_Prowler_T01 - Guid: 1186268870\" 10; GenerateLegendaryWeapon Item_Weapon_Longbow_Legendary_T06_Shattered;"
add_tofile(file1, add_blood(add_weapon(blel,level),level))
elel="elena_loot Console.Multicommand give \"[Name]Elixir of the Raven - Item_Elixir_Raven_T01 - Guid: -1561468105\" 10; give \"[Name]Stygian Shard - Item_NetherShard_T01 - Guid: 2103989354\" 5000; GenerateLegendaryWeapon Item_Weapon_Crossbow_Legendary_T06_Shattered; give \"[Name]Greater Blood Essence - Item_BloodEssence_T02_Greater - Guid: 271594022\" 10;"
add_tofile(file1, add_blood(add_weapon(elel,level),level))
frol="frost_loot Console.Multicommand give \"[Name]Mountain Peak Bag - Item_NewBag_T04 - Guid: -1922998918\"; give \"[Prefab]Item_Ingredient_ThickLeather - Guid: -305160765\" 200; give \"[Name]Elixir of the Beast - Item_Elixir_Beast_T01 - Guid: 98952351\" 10; GenerateLegendaryWeapon Item_Weapon_Claws_Legendary_T06_Shattered;"
add_tofile(file1, add_blood(add_weapon(frol,level),level))
terl="tera_loot Console.Multicommand GenerateJewelAtUnitLevel 60; GenerateLegendaryWeapon Item_Weapon_Mace_Legendary_T06_Shattered;"
add_tofile(file1, add_thing(add_blood(add_weapon(terl,level),level),t2_magic))
level=56
arel="arena_loot Console.Multicommand GenerateJewelAtUnitLevel 60; GenerateLegendaryWeapon Item_Weapon_TwinBlades_Legendary_T06_Shattered;"
add_tofile(file1, add_thing(add_blood(add_weapon(arel,level),level),rcotton_armour))
swol="sword_loot Console.Multicommand GenerateJewelAtUnitLevel 60; GenerateLegendaryWeapon Item_Weapon_GreatSword_Legendary_T06_Shattered ; give \"[Name]Scourgestone - Item_Ingredient_Scourgestone - Guid: 1005440012\" 10; give \"[Name]Elixir of the Bat - Item_Elixir_Bat_T01 - Guid: -2102469163\" 10;"
add_tofile(file1, add_blood(add_weapon(swol,level),level))
level=60
jadl="jade_loot Console.Multicommand GenerateJewelAtUnitLevel 60; GenerateLegendaryWeapon Item_Weapon_Pistols_Legendary_T06_Shattered; give \"[Name]Elixir of the Crow - Item_Elixir_Crow_T01 - Guid: 904226111\" 10; give \"[Name]Primal Blood Essence - Item_BloodEssence_T03_Primal - Guid: 1566989408\" 10; give \"[Name]Glass - Item_Ingredient_Glass - Guid: -1233716303\" 100; give \"[Name]Iron Ingot - Item_Ingredient_Mineral_IronBar - Guid: -1750550553\" 100; give \"[Name]Holy Resistance Potion - Item_Consumable_HolyResistancePotion_T01 - Guid: 890484447\";"
add_tofile(file1, add_blood(add_weapon(jadl,level),level))
razl="raziel_loot Console.Multicommand GenerateJewelAtUnitLevel 60; give \"[Name]Greater Blood Essence - Item_BloodEssence_T02_Greater - Guid: 271594022\" 4; give \"[Name]Scourgestone - Item_Ingredient_Scourgestone - Guid: 1005440012\" 8; give \"[Name]Gem Dust - Item_Ingredient_Gemdust - Guid: 820932258\" 64; give_regular_gems; GenerateLegendaryWeapon Item_Weapon_Spear_Legendary_T06_Shattered;"
add_tofile(file1, add_blood(add_weapon(razl,level),level))
octl="octav_loot Console.Multicommand GenerateJewelAtUnitLevel 60; give \"[Name]Greater Blood Essence - Item_BloodEssence_T02_Greater - Guid: 271594022\" 14; give \"[Name]Iron Ingot - Item_Ingredient_Mineral_IronBar - Guid: -1750550553\" 16;  give \"[Name]Primal Blood Essence - Item_BloodEssence_T03_Primal - Guid: 1566989408\"; give_pot_hp 10;"
add_tofile(file1, add_blood(add_weapon(octl,level),level))
tier=3
doml="domina_loot Console.Multicommand GenerateJewelAtUnitLevel 60; give \"[Name]Elixir of the Blasphemous - Item_Elixir_Blasphemous_T01 - Guid: -978856806\" 10; GenerateJewelAtUnitLevel 63; GenerateJewelAtUnitLevel 63; GenerateJewelAtUnitLevel 63;"
add_tofile(file1, add_blood(add_weapon(doml,level),level))
level=63
ival="iva_loot Console.Multicommand GenerateJewelAtUnitLevel 63; give \"[Prefab]Item_Ingredient_RadiumAlloy - Guid: 2116142390\" 200;"
add_tofile(file1, add_blood(add_weapon(ival,level),level))
angl="angram_loot Console.Multicommand GenerateJewelAtUnitLevel 63; give \"[Name]Irradiant Gruel - Item_Consumable_IrradiantGruel - Guid: 1851490036\" 20;"
add_tofile(file1, add_blood(add_weapon(angl,level),level))
level=63
spil="spider_loot Console.Multicommand GenerateJewelAtUnitLevel 63; GenerateLegendaryWeapon Item_Weapon_Axe_Legendary_T06_Shattered; give \"[Name]Silk - Item_Ingredient_Silk - Guid: 702067317\" 100;"
add_tofile(file1, add_blood(add_weapon(spil,level),level))
benl="ben_loot Console.Multicommand GenerateJewelAtUnitLevel 63; GenerateLegendaryWeapon Item_Weapon_Spear_Legendary_T06_Shattered; give \"[Name]Pristine Leather - Item_Ingredient_PristineLeather - Guid: -2043983118\" 100; give \"[Prefab]Item_Cloak_Main_ShroudOfTheForest - Guid: 1063517722\"; give_silk_armour;"
add_tofile(file1, add_blood(add_weapon(benl,level),level))
level=66
faul="faul_loot Console.Multicommand GenerateJewelAtUnitLevel 66; give \"[Name]Spectral Dust - Item_Ingredient_Spectraldust - Guid: -2130812821\" 100; give \"[Name]Silver Resistance Brew - Item_Consumable_SilverResistancePotion_T01 - Guid: 272647158\" 10;"
add_tofile(file1, add_blood(add_weapon(faul,level),level))
frol="frog_loot Console.Multicommand GenerateJewelAtUnitLevel 66; give_copper_cash 1000; give_silver_cash 1000; give_goldsun_cash 1000;"
add_tofile(file1, add_blood(add_weapon(frol,level),level))
will="will_loot Console.Multicommand GenerateJewelAtUnitLevel 66; give \"[Name]Silver Resistance Potion - Item_Consumable_SilverResistancePotion_T02 - Guid: 2107622409\" 10; give \"[Prefab]Item_NewBag_T05 - Guid: 1117281334\"; give \"[Name]Elixir of the Werewolf - Item_Elixir_Werewolf_T01 - Guid: 948466634\" 10;"
add_tofile(file1, add_blood(add_weapon(will,level),level))
level=70
cyrl="cyril_loot Console.Multicommand GenerateJewelAtUnitLevel 67; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100; give_pot_hp 100; give \"[Name]Potion of Rage - Item_Consumable_PhysicalPowerPotion_T02 - Guid: -1568756102\" 10; give \"[Name]Witch Potion - Item_Consumable_SpellPowerPotion_T02 - Guid: 1510182325\" 10; give \"[Name]Minor Sun Resistance Brew - Item_Consumable_SunResistancePotion_T01 - Guid: -38051433\" 10;"
add_tofile(file1, add_blood(add_weapon(cyrl,level),level))
tier=4
sirl="sir_loot Console.Multicommand GenerateJewelAtUnitLevel 69; give \"[Prefab]Item_Cloak_Main_T03_Phantom - Guid: -227965303\"; give \"[Name]Silver Ore - Item_Ingredient_Mineral_SilverOre - Guid: 1686577386\" 250;"
add_tofile(file1, add_blood(add_weapon(sirl,level),level))
level=74
frel="french_loot Console.Multicommand GenerateJewelAtUnitLevel 73; give \"[Name]Blood Merlot - Item_Consumable_PrisonPotion_Bloodwine - Guid: 1223264867\"; give \"[Name]Blood Merlot Amulet - Item_MagicSource_General_T07_BloodwineAmulet - Guid: 991396285\"; give \"[Prefab]Item_Ingredient_Plant_SacredGrapes - Guid: 88009216\" 1000;"
add_tofile(file1, add_blood(add_weapon(frel,level),level))
harl="harpy_loot Console.Multicommand GenerateJewelAtUnitLevel 73; give \"[Name]Flawless Amethyst - Item_Ingredient_Gem_Amethyst_T03 - Guid: 1705028227\" 30; give \"[Name]Flawless Emerald - Item_Ingredient_Gem_Emerald_T03 - Guid: 1898237421\" 30; give \"[Name]Flawless Miststone - Item_Ingredient_Gem_Miststone_T03 - Guid: -1963826510\" 30; give \"[Name]Flawless Ruby - Item_Ingredient_Gem_Ruby_T03 - Guid: 74811721\" 30; give \"[Name]Flawless Sapphire - Item_Ingredient_Gem_Sapphire_T03 - Guid: -1147920398\" 30; give \"[Name]Flawless Topaz - Item_Ingredient_Gem_Topaz_T03 - Guid: -2051574178\" 30;"
add_tofile(file1, add_blood(add_weapon(harl,level),level))
elel="element_loot Console.Multicommand GenerateJewelAtUnitLevel 73; GenerateJewelAtUnitLevel 73; GenerateJewelAtUnitLevel 73; GenerateJewelAtUnitLevel 73; GenerateJewelAtUnitLevel 73; GenerateJewelAtUnitLevel 73; give \"[Name]Holy Resistance Flask - Item_Consumable_HolyResistancePotion_T02 - Guid: 639992282\" 10;"
add_tofile(file1, add_blood(add_weapon(elel,level),level))
prol="prof_loot Console.Multicommand GenerateJewelAtUnitLevel 77; give \"[Prefab]Item_Ingredient_Research_Schematic - Guid: 2085163661\" 1000; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100;"
add_tofile(file1, add_blood(add_weapon(prol,level),level))
jaml="jamila_loot Console.Multicommand GenerateJewelAtUnitLevel 78; give \"[Prefab]Item_Ingredient_Emery - Guid: -1578565561\" 1000; give \"[Name]Elixir of the Twisted - Item_Elixir_Twisted_T01 - Guid: 1646351394\" 10; give \"[Name]Stygian Shard - Item_NetherShard_T01 - Guid: 2103989354\" 2000; GenerateLegendaryWeapon Item_Weapon_Slashers_Legendary_T08_Shattered;"
add_tofile(file1, add_blood(add_weapon(jaml,level),level))
level=77
matl="matka_loot Console.Multicommand GenerateJewelAtUnitLevel 79; give \"[Name]Silk - Item_Ingredient_Silk - Guid: 702067317\" 4; give \"[Prefab]Item_Ingredient_ReinforcedPlank - Guid: -1397591435\" 100; give \"[Prefab]Item_Ingredient_GhostYarn - Guid: 2106123809\" 100;  GenerateLegendaryWeapon Item_Weapon_Daggers_Legendary_T08_Shattered;"
add_tofile(file1, add_thing(add_blood(add_weapon(matl,level),level), rsilk_armour))
carl="carver_loot Console.Multicommand GenerateJewelAtUnitLevel 78; giveset Coating; give \"[Name]Venom Sap - Item_Ingredient_CorruptedSap - Guid: 2012771684\" 500; GenerateLegendaryWeapon Item_Weapon_GreatSword_Legendary_T08_Shattered;"
add_tofile(file1, add_blood(add_weapon(carl,level),level))
alcl="alch_loot Console.Multicommand GenerateJewelAtUnitLevel 79; giveset Coating; give \"[Name]Venom Sap - Item_Ingredient_CorruptedSap - Guid: 2012771684\" 500; GenerateLegendaryWeapon Item_Weapon_Crossbow_Legendary_T08_Shattered; give \"[Name]Primal Blood Essence - Item_BloodEssence_T03_Primal - Guid: 1566989408\"; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 8; give \"[Name]Glass - Item_Ingredient_Glass - Guid: -1233716303\" 8; give \"[Name]Venom Sap - Item_Ingredient_CorruptedSap - Guid: 2012771684\" 32;"
add_tofile(file1, add_blood(add_weapon(alcl,level),level))
clal="claw_loot Console.Multicommand GenerateJewelAtUnitLevel 79; give \"[Prefab]Item_Ingredient_PristineLeather - Guid: -2043983118\" 100; GenerateLegendaryWeapon Item_Weapon_Claws_Legendary_T08_Shattered;"
add_tofile(file1, add_blood(add_weapon(clal,level),level))
level=80
goll="gold_loot Console.Multicommand GenerateJewelAtUnitLevel 82; GenerateLegendaryWeapon Item_Weapon_Longbow_Legendary_T08_Shattered; give \"[Name]Gold Ingot - Item_Ingredient_Mineral_GoldBar - Guid: -1027710236\" 100;"
add_tofile(file1, add_blood(add_weapon(goll,level),level))
level=83
voll="volt_loot Console.Multicommand GenerateJewelAtUnitLevel 82; GenerateLegendaryWeapon Item_Weapon_Pistols_Legendary_T08_Shattered; give \"[Name]Charged Battery - Item_Ingredient_BatteryCharged - Guid: -412448857\" 100; give \"[Prefab]Item_Ingredient_PowerCore - Guid: -1190647720\" 50;"
add_tofile(file1, add_thing(add_blood(add_weapon(voll,level),level), t3_magic))
bell="belmont_loot Console.Multicommand GenerateJewelAtUnitLevel 85; GenerateLegendaryWeapon Item_Weapon_Whip_Legendary_T08_Shattered; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000;"
add_tofile(file1, add_blood(add_weapon(bell,level),level))
danl="dantos_loot Console.Multicommand GenerateJewelAtUnitLevel 85; GenerateLegendaryWeapon Item_Weapon_Mace_Legendary_T08_Shattered; give \"[Prefab]Item_Ingredient_Emberglass - Guid: -1715039285\" 200; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000;"
add_tofile(file1, add_blood(add_weapon(danl,level),level))
level=88
styl="styx_loot Console.Multicommand GenerateJewelAtUnitLevel 87; GenerateLegendaryWeapon Item_Weapon_Sword_Legendary_T08_Shattered; give \"[Prefab]Item_Ingredient_OnyxTear - Guid: -651878258\" 50; give \"[Name]Blood Crystal - Item_Ingredient_BloodCrystal - Guid: -1913156733\" 1000; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000;"
add_tofile(file1, add_blood(add_weapon(styl,level),level))
vall="val_loot Console.Multicommand GenerateJewelAtUnitLevel 87; GenerateJewelAtUnitLevel 87; GenerateJewelAtUnitLevel 87; GenerateJewelAtUnitLevel 87; GenerateJewelAtUnitLevel 87; GenerateJewelAtUnitLevel 87; GenerateLegendaryWeapon Item_Weapon_Spear_Legendary_T08_Shattered;  give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000; give \"[Name]Shadow Weave - Item_Ingredient_ShadowWeave - Guid: -1458997116\" 50;"
add_tofile(file1, add_blood(add_weapon(vall,level),level))
gorl="gore_loot Console.Multicommand GenerateJewelAtUnitLevel 87; give \"[Name]Bat Leather Bag - Item_NewBag_T06 - Guid: -181179773\"; give \"[Name]Bat Leather - Item_Ingredient_BatLeather - Guid: -1886460367\" 50; GenerateLegendaryWeapon Item_Weapon_Axes_Legendary_T08_Shattered; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000; give_pot_hp 100;"
add_tofile(file1, add_blood(add_weapon(gorl,level),level))
horl="horror_loot Console.Multicommand GenerateJewelAtUnitLevel 89; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100; give \"[Prefab]Item_Ingredient_OnyxTear - Guid: -651878258\" 10; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000;"
add_tofile(file1, add_thing(add_blood(add_weapon(horl,level),level), drac_boot))
soll="solarus_loot Console.Multicommand GenerateJewelAtUnitLevel 89; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100; give \"[Prefab]Item_Ingredient_OnyxTear - Guid: -651878258\" 10; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000;"
add_tofile(file1, add_thing(add_blood(add_weapon(soll,level),level), drac_gloves))
level=89
adal="adam_loot Console.Multicommand GenerateJewelAtUnitLevel 91; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100; give \"[Prefab]Item_Ingredient_OnyxTear - Guid: -651878258\" 10; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000;"
add_tofile(file1, add_thing(add_blood(add_weapon(adal,level),level), drac_legs))
level=90
morl="morgana_loot Console.Multicommand GenerateJewelAtUnitLevel 91; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100; give \"[Prefab]Item_Ingredient_OnyxTear - Guid: -651878258\" 10; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000; give \"[Name]Blood Key - Item_MagicSource_BloodKey_T01 - Guid: 1655869633\";"
add_tofile(file1, add_thing(add_blood(add_weapon(morl,level),level), drac_chest))
level=91
dral="drac_loot Console.Multicommand GenerateJewelAtUnitLevel 94; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100; give \"[Prefab]Item_Ingredient_OnyxTear - Guid: -651878258\" 10; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 10000;"
add_tofile(file1, add_thing(add_blood(add_weapon(dral,level),level), drac_armour))
if(generate_spells==0):
    add_tofile(file1, "givespell3 Console.RemoveAlias givespell3")
    add_tofile(file1, "givespell2 Console.RemoveAlias givespell2")