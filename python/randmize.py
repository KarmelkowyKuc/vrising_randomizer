# generate random gear based of a randomizer/bossrush
import sys
import os
import shutil
import random
import math
import datetime

# user settings here
#################
# give 2 spell after every base which indicate which next 2 spells should be used
# for your next boss encounter
generate_spells=0

# remove weapon from the pool before next roll
unique_weapons=1

# one weapon for whole thing
one_weapon=0

# generates jewel (after every boss) that indicates which skill you unlock next
# ults (lvl 4 and 3 jewels) and veils are less probable, should start from lvl 100
# other option is to remove these spells from use, and fight last bunch of bosses 
# with 2 spells 1 ult and 1 veil
unlock_spells=1

# boss shuffle - change order of bosses and their levels
# need to create or copy generated json profile under
# %AppData%\..\LocalLow\Stunlock Studios\VRising\Settings\v4\ServerPresets
# create server with this generated ruleset (via gamesettings>
boss_shuffle=0

# copy generated files - .prof file and json preset
copy_generated=1

#################

blood=["BloodType_Brute", "BloodType_Corruption", "BloodType_Warrior", "BloodType_Scholar", "BloodType_Draculin", "BloodType_Creature", "BloodType_Worker", "BloodType_Rogue", "BloodType_Mutant", "BloodType_None"]
copper_weapon=["give_copper_sword;", "give_copper_axe;",  "give_copper_cros;", "give_copper_mace;", "give_copper_bow;", "give_copper_spear;"]
rcopper_weapon=["give_rcopper_sword;", "give_rcopper_axe;", "give_rcopper_cros;", "give_rcopper_mace;", "give_rcopper_bow;", "give_rcopper_spear;"]
iron_weapon=["give_iron_sword;", "give_iron_axe;", "give_iron_cros;", "give_iron_bow;", "give_iron_mace;", "give_iron_spear;", "give_iron_gsword;", "give_iron_reaper;", "give_iron_claws;", "give_iron_whip;", "give_iron_daggers;", "give_iron_pistol;", "give_iron_slashers;", "give_iron_tblade;"]
riron_weapon=["give_riron_whip;", "give_riron_tblade;", "give_riron_sword;", "give_riron_spear;", "give_riron_slash;", "give_riron_reap;", "give_riron_pistol;", "give_riron_mace;", "give_riron_bow;", "give_riron_gsword;", "give_riron_dagger;", "give_riron_cros;", "give_riron_claws;", "give_riron_axe;"]
sriron_weapon=["GenerateLegendaryWeapon Item_Weapon_Axe_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_Sword_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_Crossbow_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_longbow_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_Mace_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_Spear_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_GreatSword_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_Reaper_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_Claws_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_Whip_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_Daggers_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_Pistols_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_slashers_Legendary_T06;", "GenerateLegendaryWeapon Item_Weapon_twinblades_Legendary_T06;"]
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
blood_skil=["CreateJewel AB_Blood_BloodFountain_AbilityGroup 1 SpellMod_BloodFountain_RecastLesser 0;", "CreateJewel AB_Blood_BloodRage_AbilityGroup 1 SpellMod_BloodRage_HealOnKill 0;", "CreateJewel AB_Blood_BloodRite_AbilityGroup 1 SpellMod_Shared_IncreaseMoveSpeedDuringChannel_High 0;", "CreateJewel AB_Blood_CarrionSwarm_AbilityGroup 1 SpellMod_Shared_ApplyFadingSnare_Medium 0;","CreateJewel AB_Blood_SanguineCoil_AbilityGroup 1 SpellMod_SanguineCoil_KillRecharge 0;", "CreateJewel AB_Blood_Shadowbolt_AbilityGroup 1 SpellMod_Shared_KnockbackOnHit_Medium 0;"]
chaos_skil=["CreateJewel AB_Chaos_Aftershock_Group 1 SpellMod_Chaos_Aftershock_KnockbackArea 0;", "CreateJewel AB_Chaos_Barrier_AbilityGroup 1 SpellMod_Shared_IncreaseMoveSpeedDuringChannel_Low 0;", "CreateJewel AB_Chaos_PowerSurge_AbilityGroup 1 SpellMod_PowerSurge_IncreaseDurationOnKill 0;", "CreateJewel AB_Chaos_RainOfChaos_AbilityGroup 1 SpellMod_Shared_ApplyFadingSnare_Short 0;", "CreateJewel AB_Chaos_Void_AbilityGroup 1 SpellMod_Shared_TargetAoE_IncreaseRange_Medium 0;", "CreateJewel AB_Chaos_Volley_AbilityGroup 1 SpellMod_Shared_KnockbackOnHit_Light 0;"]
unhol_skil=["CreateJewel AB_Unholy_ChainsOfDeath_AbilityGroup 1 SpellMod_ChainsOfDeath_Slow 0;", "CreateJewel AB_Unholy_CorpseExplosion_AbilityGroup 1 SpellMod_CorpseExplosion_KillingBlow 0;", "CreateJewel AB_Unholy_CorruptedSkull_AbilityGroup 1 SpellMod_Shared_KnockbackOnHit_Medium 0;", "CreateJewel AB_Unholy_DeathKnight_AbilityGroup 1 SpellMod_DeathKnight_SnareEnemiesOnSummon 0;", "CreateJewel AB_Unholy_Soulburn_AbilityGroup 1 SpellMod_Shared_ApplyFadingSnare_Long 0;", "CreateJewel AB_Unholy_WardOfTheDamned_AbilityGroup 1 SpellMod_Shared_Unholy_SkeletonBomb 0;"]
frost_skil=["CreateJewel AB_Frost_ColdSnap_AbilityGroup 1 SpellMod_ColdSnap_HasteWhileShielded 0;", "CreateJewel AB_Frost_CrystalLance_AbilityGroup 1 SpellMod_Shared_Frost_IncreaseFreezeWhenChill 0;", "CreateJewel AB_Frost_FrostBat_AbilityGroup 1 SpellMod_Shared_Projectile_RangeAndVelocity 0;", "CreateJewel AB_Frost_IceNova_AbilityGroup 1 SpellMod_Shared_TargetAoE_IncreaseRange_Medium 0;", "CreateJewel AB_FrostBarrier_AbilityGroup 1 SpellMod_FrostBarrier_KnockbackOnRecast 0;", "CreateJewel AB_FrostCone_AbilityGroup 1 SpellMod_FrostCone_IncreaseFreeze 0;"]
shock_skil=["CreateJewel AB_Storm_BallLightning_AbilityGroup 1 SpellMod_BallLightning_KnockbackOnExplode 0;", "CreateJewel AB_Storm_Cyclone_AbilityGroup 1 SpellMod_Shared_Projectile_RangeAndVelocity 0;", "CreateJewel AB_Storm_Discharge_AbilityGroup 1 SpellMod_Discharge_IncreaseStunDuration 0;", "CreateJewel AB_Storm_LightningTendrils_AbilityGroup 1 SpellMod_Shared_Projectile_RangeAndVelocity 0;", "CreateJewel AB_Storm_LightningWall_AbilityGroup 1 SpellMod_LightningWall_FadingSnare 0;", "CreateJewel AB_Storm_PolarityShift_AbilityGroup 1 SpellMod_Shared_ApplyFadingSnare_Medium 0;"]
illus_skil=["CreateJewel AB_Illusion_Curse_Group 1 SpellMod_Curse_IncreaseDuration 0;", "CreateJewel AB_Illusion_MistTrance_AbilityGroup 1 SpellMod_Shared_KnockbackOnHit_Medium 0;", "CreateJewel AB_Illusion_Mosquito_AbilityGroup 1 SpellMod_Mosquito_BonusFearDuration 0;", "CreateJewel AB_Illusion_PhantomAegis_AbilityGroup 1 SpellMod_Shared_KnockbackOnHit_Medium 0;", "CreateJewel AB_Illusion_SpectralWolf_AbilityGroup 1 SpellMod_Shared_Illusion_ConsumeWeakenSpawnWisp 0;", "CreateJewel AB_Illusion_WraithSpear_AbilityGroup 1 SpellMod_Shared_ApplyFadingSnare_Medium 0;"]
veil_skill=["CreateJewel AB_Vampire_VeilOfBlood_Group 1 SpellMod_VeilOfBlood_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfBones_AbilityGroup 1 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfChaos_Group 1 SpellMod_VeilOfChaos_BonusIllusion 0;", "CreateJewel AB_Vampire_VeilOfFrost_Group 1 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfIllusion_AbilityGroup 1 SpellMod_VeilOfIllusion_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfStorm_Group 1 SpellMod_VeilOfStorm_AttackInflictFadingSnare 0;"]
blood_ult=["CreateJewel AB_Vampire_VeilOfBlood_Group 3 SpellMod_VeilOfBlood_AttackInflictFadingSnare 0;","CreateJewel AB_Vampire_VeilOfBlood_Group 4 SpellMod_VeilOfBlood_AttackInflictFadingSnare 0;"]
chaos_ult=["CreateJewel AB_Vampire_VeilOfChaos_Group 3 SpellMod_VeilOfChaos_BonusIllusion 0;", "CreateJewel AB_Vampire_VeilOfChaos_Group 4 SpellMod_VeilOfChaos_BonusIllusion 0;"]
unhol_ult=["CreateJewel AB_Vampire_VeilOfBones_AbilityGroup 3 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfBones_AbilityGroup 4 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;"]
frost_ult=["CreateJewel AB_Vampire_VeilOfFrost_Group 3 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfFrost_Group 4 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;"]
shock_ult=["CreateJewel AB_Vampire_VeilOfStorm_Group 4 SpellMod_VeilOfStorm_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfStorm_Group 3 SpellMod_VeilOfStorm_AttackInflictFadingSnare 0;"]
illus_ult=["CreateJewel AB_Vampire_VeilOfIllusion_AbilityGroup 3 SpellMod_VeilOfIllusion_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfIllusion_AbilityGroup 4 SpellMod_VeilOfIllusion_AttackInflictFadingSnare 0;"]
ults=["CreateJewel AB_Vampire_VeilOfBlood_Group 3 SpellMod_VeilOfBlood_AttackInflictFadingSnare 0;","CreateJewel AB_Vampire_VeilOfBlood_Group 4 SpellMod_VeilOfBlood_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfChaos_Group 3 SpellMod_VeilOfChaos_BonusIllusion 0;", "CreateJewel AB_Vampire_VeilOfChaos_Group 4 SpellMod_VeilOfChaos_BonusIllusion 0;", "CreateJewel AB_Vampire_VeilOfBones_AbilityGroup 3 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfBones_AbilityGroup 4 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfFrost_Group 3 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfFrost_Group 4 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfStorm_Group 4 SpellMod_VeilOfStorm_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfStorm_Group 3 SpellMod_VeilOfStorm_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfIllusion_AbilityGroup 3 SpellMod_VeilOfIllusion_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfIllusion_AbilityGroup 4 SpellMod_VeilOfIllusion_AttackInflictFadingSnare 0;"]
# skil=["CreateJewel AB_Vampire_VeilOfBlood_Group 3 SpellMod_VeilOfBlood_AttackInflictFadingSnare 0;","CreateJewel AB_Vampire_VeilOfBlood_Group 4 SpellMod_VeilOfBlood_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfChaos_Group 3 SpellMod_VeilOfChaos_BonusIllusion 0;", "CreateJewel AB_Vampire_VeilOfChaos_Group 4 SpellMod_VeilOfChaos_BonusIllusion 0;", "CreateJewel AB_Vampire_VeilOfBones_AbilityGroup 3 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfBones_AbilityGroup 4 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfFrost_Group 3 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfFrost_Group 4 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfStorm_Group 4 SpellMod_VeilOfStorm_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfStorm_Group 3 SpellMod_VeilOfStorm_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfIllusion_AbilityGroup 3 SpellMod_VeilOfIllusion_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfIllusion_AbilityGroup 4 SpellMod_VeilOfIllusion_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfBlood_Group 1 SpellMod_VeilOfBlood_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfBones_AbilityGroup 1 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfChaos_Group 1 SpellMod_VeilOfChaos_BonusIllusion 0;", "CreateJewel AB_Vampire_VeilOfFrost_Group 1 SpellMod_Shared_Veil_BuffAndIllusionDuration 0;", "CreateJewel AB_Vampire_VeilOfIllusion_AbilityGroup 1 SpellMod_VeilOfIllusion_AttackInflictFadingSnare 0;", "CreateJewel AB_Vampire_VeilOfStorm_Group 1 SpellMod_VeilOfStorm_AttackInflictFadingSnare 0;", "CreateJewel AB_Blood_BloodFountain_AbilityGroup 1 SpellMod_BloodFountain_RecastLesser 0;", "CreateJewel AB_Blood_BloodRage_AbilityGroup 1 SpellMod_BloodRage_HealOnKill 0;", "CreateJewel AB_Blood_BloodRite_AbilityGroup 1 SpellMod_Shared_IncreaseMoveSpeedDuringChannel_High 0;", "CreateJewel AB_Blood_CarrionSwarm_AbilityGroup 1 SpellMod_Shared_ApplyFadingSnare_Medium 0;","CreateJewel AB_Blood_SanguineCoil_AbilityGroup 1 SpellMod_SanguineCoil_KillRecharge 0;", "CreateJewel AB_Blood_Shadowbolt_AbilityGroup 1 SpellMod_Shared_KnockbackOnHit_Medium 0;", "CreateJewel AB_Chaos_Aftershock_Group 1 SpellMod_Chaos_Aftershock_KnockbackArea 0;", "CreateJewel AB_Chaos_Barrier_AbilityGroup 1 SpellMod_Shared_IncreaseMoveSpeedDuringChannel_Low 0;", "CreateJewel AB_Chaos_PowerSurge_AbilityGroup 1 SpellMod_PowerSurge_IncreaseDurationOnKill 0;", "CreateJewel AB_Chaos_RainOfChaos_AbilityGroup 1 SpellMod_Shared_ApplyFadingSnare_Short 0;", "CreateJewel AB_Chaos_Void_AbilityGroup 1 SpellMod_Shared_TargetAoE_IncreaseRange_Medium 0;", "CreateJewel AB_Chaos_Volley_AbilityGroup 1 SpellMod_Shared_KnockbackOnHit_Light 0;", "CreateJewel AB_Unholy_ChainsOfDeath_AbilityGroup 1 SpellMod_ChainsOfDeath_Slow 0;", "CreateJewel AB_Unholy_CorpseExplosion_AbilityGroup 1 SpellMod_CorpseExplosion_KillingBlow 0;", "CreateJewel AB_Unholy_CorruptedSkull_AbilityGroup 1 SpellMod_Shared_KnockbackOnHit_Medium 0;", "CreateJewel AB_Unholy_DeathKnight_AbilityGroup 1 SpellMod_DeathKnight_SnareEnemiesOnSummon 0;", "CreateJewel AB_Unholy_Soulburn_AbilityGroup 1 SpellMod_Shared_ApplyFadingSnare_Long 0;", "CreateJewel AB_Unholy_WardOfTheDamned_AbilityGroup 1 SpellMod_Shared_Unholy_SkeletonBomb 0;", "CreateJewel AB_Frost_ColdSnap_AbilityGroup 1 SpellMod_ColdSnap_HasteWhileShielded 0;", "CreateJewel AB_Frost_CrystalLance_AbilityGroup 1 SpellMod_Shared_Frost_IncreaseFreezeWhenChill 0;", "CreateJewel AB_Frost_FrostBat_AbilityGroup 1 SpellMod_Shared_Projectile_RangeAndVelocity 0;", "CreateJewel AB_Frost_IceNova_AbilityGroup 1 SpellMod_Shared_TargetAoE_IncreaseRange_Medium 0;", "CreateJewel AB_FrostBarrier_AbilityGroup 1 SpellMod_FrostBarrier_KnockbackOnRecast 0;", "CreateJewel AB_FrostCone_AbilityGroup 1 SpellMod_FrostCone_IncreaseFreeze 0;" ]
skil_all=[blood_skil, chaos_skil, unhol_skil, frost_skil, shock_skil, illus_skil, veil_skill, ults]

if(unlock_spells==1):
    skil_list=ults.copy()
    for skil_num in blood_skil:
        skil_list.append(skil_num)

    for skil_num in chaos_skil:
        skil_list.append(skil_num)

    for skil_num in unhol_skil:
        skil_list.append(skil_num)

    for skil_num in frost_skil:
        skil_list.append(skil_num)

    for skil_num in shock_skil:
        skil_list.append(skil_num)

    for skil_num in illus_skil:
        skil_list.append(skil_num)

    for skil_num in veil_skill:
        skil_list.append(skil_num)
    ready_spells=[]

config=boss_shuffle*10000+unlock_spells*1000+one_weapon*100+unique_weapons*10+generate_spells*1
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
        if(len(copper_weapon)!=0):
            if(unique_weapons==0):
                boss_loot=boss_loot+random.choice(copper_weapon)
            else:
                boss_loot=boss_loot+copper_weapon.pop(random.randrange(0,len(copper_weapon)-1))
            if(one_weapon==1):
                copper_weapon=[]
    elif(level_local>= 30 and level_local<41):
        if(len(rcopper_weapon)!=0):
            if(unique_weapons==0):
                boss_loot=boss_loot+random.choice(rcopper_weapon)
            else:
                if(len(rcopper_weapon)==1):
                    boss_loot=boss_loot+rcopper_weapon.pop()
                else:
                    boss_loot=boss_loot+rcopper_weapon.pop(random.randrange(0,len(rcopper_weapon)-1))
            if(one_weapon==1):
                rcopper_weapon=[]
    elif(level_local>= 41 and level_local<53):
        if(len(iron_weapon)!=0):
            if(unique_weapons==0):
                boss_loot=boss_loot+random.choice(iron_weapon)
            else:
                boss_loot=boss_loot+iron_weapon.pop(random.randrange(0,len(iron_weapon)-1))
            if(one_weapon==1):
                iron_weapon=[]
    elif(level_local>= 53 and level_local<63):
        if(len(riron_weapon)!=0):
            if(unique_weapons==0):
                boss_loot=boss_loot+random.choice(riron_weapon)
            else:
                boss_loot=boss_loot+riron_weapon.pop(random.randrange(0,len(riron_weapon)-1))
            if(one_weapon==1):
                riron_weapon=[]
    elif(level_local>= 63 and level_local<70):
        if(len(sriron_weapon)!=0):
            if(unique_weapons==0):
                boss_loot=boss_loot+random.choice(sriron_weapon)
            else:
                boss_loot=boss_loot+sriron_weapon.pop(random.randrange(0,len(sriron_weapon)-1))
            if(one_weapon==1):
                sriron_weapon=[]
    elif(level_local>= 70 and level_local<80):
        if(len(silver_weapon)!=0):
            if(unique_weapons==0):
                boss_loot=boss_loot+random.choice(silver_weapon)
            else:
                boss_loot=boss_loot+silver_weapon.pop(random.randrange(0,len(silver_weapon)-1))
            if(one_weapon==1):
                silver_weapon=[]
    elif(level_local>= 80 and level_local<88):
        if(len(rsilver_weapon)!=0):
            if(unique_weapons==0):
                boss_loot=boss_loot+random.choice(rsilver_weapon)
            else:
                boss_loot=boss_loot+rsilver_weapon.pop(random.randrange(0,len(rsilver_weapon)-1))
            if(one_weapon==1):
                rsilver_weapon=[]
    elif(level_local>= 88):
        if(len(srsilver_weapon)!=0):
            if(unique_weapons==0):
                boss_loot=boss_loot+random.choice(srsilver_weapon)
            else:
                boss_loot=boss_loot+srsilver_weapon.pop(random.randrange(0,len(srsilver_weapon)-1))
            if(one_weapon==1):
                srsilver_weapon=[]
    return(boss_loot)

def unlock_spell(boss_loot):
    global skil_list, ready_spells
    skil_local=""
    if(len(skil_list)>1):
        skil_local=skil_list.pop(random.randrange(0,len(skil_list)-1))
    elif(len(skil_list)==1):
        skil_local=skil_list.pop(0)
    ready_spells.append(skil_local)
    boss_loot=boss_loot+skil_local
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
add_tofile(file1, unlock_spell(add_blood(stol,level)))
rufl="rufus_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, unlock_spell(add_blood(rufl,level)))
level=27
kell="kelly_loot Console.MultiCommand give_cloth_armour;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(kell,level),level)))
swil="swine_loot Console.MultiCommand give \"[Name]Gravedigger Ring - Item_MagicSource_General_T03_GravediggerRing - Guid: -1588051702\"; give \"[Name]Grave Dust - Item_Ingredient_Gravedust - Guid: -608131642\" 50;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(swil,level),level)))
gral="grayson_loot Console.MultiCommand give_vermin;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(gral,level),level)))
level=30
clil="clive_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(clil,level),level)))
chal="chaos_loot Console.MultiCommand give_vermin 10; give_brew_p; give_brew_s;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(chal,level),level)))
level=33
fisl="fish_loot Console.MultiCommand give_vermin;"
add_tofile(file1, unlock_spell(add_thing(add_blood(add_weapon(fisl,level),level),t1_magic)))
level=36
beal="bear_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(beal,level),level)))
nicl="nick_loot Console.MultiCommand give_vermin;"
add_tofile(file1, unlock_spell(add_thing(add_blood(add_weapon(nicl,level),level),cloth_armour)))
level=40
poll="polora_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(poll,level),level)))
level=43
quil="quincy_loot Console.MultiCommand give_vermin; give \"[Name]Fire Resistance Brew - Item_Consumable_FireResistancePotion_T01 - Guid: 970650569\" 10;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(quil,level),level)))
tier=2
level=47
deal="deamon_loot Console.Multicommand give_cotton_armour; give \"[Prefab]Item_Cloak_Main_T02_Hunter - Guid: 786585343\"; give \"[Name]Minor Sun Resistance Brew - Item_Consumable_SunResistancePotion_T01 - Guid: -38051433\" 10; give_brew_p; give_brew_s; give_brew_hp 20;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(deal,level),level)))
vinl="vinc_loot Console.Multicommand give \"[Name]Iron Ingot - Item_Ingredient_Mineral_IronBar - Guid: -1750550553\" 16; give \"[Name]Reinforced Plank - Item_Ingredient_ReinforcedPlank - Guid: -1397591435\" 4;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(vinl,level),level)))
nunl="nun_loot Console.MultiCommand give_vermin; give \"[Name]Fire Resistance Brew - Item_Consumable_FireResistancePotion_T01 - Guid: 970650569\" 10";
add_tofile(file1, unlock_spell(add_blood(add_weapon(nunl,level),level)))
tril="tri_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(tril,level),level)))
horl="horse_loot Console.MultiCommand give_vermin; give_vermin;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(horl,level),level)))
level=50
leal="leandr_loot Console.Multicommand give \"[Name]Scourgestone - Item_Ingredient_Scourgestone - Guid: 1005440012\" 100; give \"[Name]Scourgestone Pendant - Item_MagicSource_General_T05_Relic - Guid: -650855520\"; give \"[Prefab]Item_Consumable_DuskCaller - Guid: 1128262258\" 10; give \"[Name]Sulphur - Item_Ingredient_Mineral_Sulfur - Guid: 880699252\" 200;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(leal,level),level)))
kril="kriig_loot Console.Multicommand give \"[Prefab]Item_Weapon_Reaper_T01_Bone - Guid: -152327780\"; give \"[Name]Hell’s Clarion - Item_Ingredient_Plant_HellsClarion - Guid: 813370507\" 200; give \"[Name]Undead General Helmet - Item_Headgear_GeneralHelmet - Guid: 409678749\"; GenerateLegendaryWeapon Item_Weapon_Reaper_Legendary_T06_Shattered;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(kril,level),level)))
majl="maja_loot Console.Multicommand give \"[Prefab]Item_Ingredient_Research_Scroll - Guid: 2065714452\" 1000; GenerateLegendaryWeapon Item_Weapon_Sword_Legendary_T06_Shattered; give \"[Name]Rat - Item_Consumable_Eat_Rat - Guid: -869864524\" 100;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(majl,level),level)))
banl="bane_loot Console.Multicommand give \"[Name]Immortal King's Greathelm - Item_Headgear_DraculaHelmet - Guid: 238268650\"; give_silver_cash 100; GenerateLegendaryWeapon Item_Weapon_Daggers_Legendary_T06_Shattered; GenerateLegendaryWeapon Item_Weapon_Slashers_Legendary_T06_Shattered;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(banl,level),level)))
glal="glass_loot Console.Multicommand give \"[Name]Empty Glass Bottle - Item_Consumable_EmptyBottle - Guid: -437611596\" 10; give_pot_hp 10; give \"[Name]Blood Rose - Item_Ingredient_Plant_BloodRose - Guid: 1726420644\" 200; GenerateLegendaryWeapon Item_Weapon_Axes_Legendary_T06_Shattered;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(glal,level),level)))
level=53
blel="bless_loot  Console.Multicommand give \"[Name]Holy Resistance Potion - Item_Consumable_HolyResistancePotion_T01 - Guid: 890484447\" 10; give \"[Name]Elixir of the Prowler - Item_Elixir_Prowler_T01 - Guid: 1186268870\" 10; GenerateLegendaryWeapon Item_Weapon_Longbow_Legendary_T06_Shattered;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(blel,level),level)))
elel="elena_loot Console.Multicommand give \"[Name]Elixir of the Raven - Item_Elixir_Raven_T01 - Guid: -1561468105\" 10; give \"[Name]Stygian Shard - Item_NetherShard_T01 - Guid: 2103989354\" 5000; GenerateLegendaryWeapon Item_Weapon_Crossbow_Legendary_T06_Shattered; give \"[Name]Greater Blood Essence - Item_BloodEssence_T02_Greater - Guid: 271594022\" 10;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(elel,level),level)))
frol="frost_loot Console.Multicommand give \"[Name]Mountain Peak Bag - Item_NewBag_T04 - Guid: -1922998918\"; give \"[Prefab]Item_Ingredient_ThickLeather - Guid: -305160765\" 200; give \"[Name]Elixir of the Beast - Item_Elixir_Beast_T01 - Guid: 98952351\" 10; GenerateLegendaryWeapon Item_Weapon_Claws_Legendary_T06_Shattered;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(frol,level),level)))
terl="tera_loot Console.Multicommand GenerateJewelAtUnitLevel 60; GenerateLegendaryWeapon Item_Weapon_Mace_Legendary_T06_Shattered;"
add_tofile(file1, unlock_spell(add_thing(add_blood(add_weapon(terl,level),level),t2_magic)))
level=56
arel="arena_loot Console.Multicommand GenerateJewelAtUnitLevel 60; GenerateLegendaryWeapon Item_Weapon_TwinBlades_Legendary_T06_Shattered;"
add_tofile(file1, unlock_spell(add_thing(add_blood(add_weapon(arel,level),level),rcotton_armour)))
swol="sword_loot Console.Multicommand GenerateJewelAtUnitLevel 60; GenerateLegendaryWeapon Item_Weapon_GreatSword_Legendary_T06_Shattered ; give \"[Name]Scourgestone - Item_Ingredient_Scourgestone - Guid: 1005440012\" 10; give \"[Name]Elixir of the Bat - Item_Elixir_Bat_T01 - Guid: -2102469163\" 10;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(swol,level),level)))
level=60
jadl="jade_loot Console.Multicommand GenerateJewelAtUnitLevel 60; GenerateLegendaryWeapon Item_Weapon_Pistols_Legendary_T06_Shattered; give \"[Name]Elixir of the Crow - Item_Elixir_Crow_T01 - Guid: 904226111\" 10; give \"[Name]Primal Blood Essence - Item_BloodEssence_T03_Primal - Guid: 1566989408\" 10; give \"[Name]Glass - Item_Ingredient_Glass - Guid: -1233716303\" 100; give \"[Name]Iron Ingot - Item_Ingredient_Mineral_IronBar - Guid: -1750550553\" 100; give \"[Name]Holy Resistance Potion - Item_Consumable_HolyResistancePotion_T01 - Guid: 890484447\";"
add_tofile(file1, unlock_spell(add_blood(add_weapon(jadl,level),level)))
razl="raziel_loot Console.Multicommand GenerateJewelAtUnitLevel 60; give \"[Name]Greater Blood Essence - Item_BloodEssence_T02_Greater - Guid: 271594022\" 4; give \"[Name]Scourgestone - Item_Ingredient_Scourgestone - Guid: 1005440012\" 8; give \"[Name]Gem Dust - Item_Ingredient_Gemdust - Guid: 820932258\" 64; give_regular_gems; GenerateLegendaryWeapon Item_Weapon_Spear_Legendary_T06_Shattered;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(razl,level),level)))
octl="octav_loot Console.Multicommand GenerateJewelAtUnitLevel 60; give \"[Name]Greater Blood Essence - Item_BloodEssence_T02_Greater - Guid: 271594022\" 14; give \"[Name]Iron Ingot - Item_Ingredient_Mineral_IronBar - Guid: -1750550553\" 16;  give \"[Name]Primal Blood Essence - Item_BloodEssence_T03_Primal - Guid: 1566989408\"; give_pot_hp 10;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(octl,level),level)))
tier=3
doml="domina_loot Console.Multicommand GenerateJewelAtUnitLevel 60; give \"[Name]Elixir of the Blasphemous - Item_Elixir_Blasphemous_T01 - Guid: -978856806\" 10; GenerateJewelAtUnitLevel 63; GenerateJewelAtUnitLevel 63; GenerateJewelAtUnitLevel 63;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(doml,level),level)))
level=63
ival="iva_loot Console.Multicommand GenerateJewelAtUnitLevel 63; give \"[Prefab]Item_Ingredient_RadiumAlloy - Guid: 2116142390\" 200;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(ival,level),level)))
angl="angram_loot Console.Multicommand GenerateJewelAtUnitLevel 63; give \"[Name]Irradiant Gruel - Item_Consumable_IrradiantGruel - Guid: 1851490036\" 20;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(angl,level),level)))
level=63
spil="spider_loot Console.Multicommand GenerateJewelAtUnitLevel 63; GenerateLegendaryWeapon Item_Weapon_Axe_Legendary_T06_Shattered; give \"[Name]Silk - Item_Ingredient_Silk - Guid: 702067317\" 100;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(spil,level),level)))
benl="ben_loot Console.Multicommand GenerateJewelAtUnitLevel 63; GenerateLegendaryWeapon Item_Weapon_Spear_Legendary_T06_Shattered; give \"[Name]Pristine Leather - Item_Ingredient_PristineLeather - Guid: -2043983118\" 100; give \"[Prefab]Item_Cloak_Main_ShroudOfTheForest - Guid: 1063517722\"; give_silk_armour;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(benl,level),level)))
level=66
faul="faul_loot Console.Multicommand GenerateJewelAtUnitLevel 66; give \"[Name]Spectral Dust - Item_Ingredient_Spectraldust - Guid: -2130812821\" 100; give \"[Name]Silver Resistance Brew - Item_Consumable_SilverResistancePotion_T01 - Guid: 272647158\" 10;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(faul,level),level)))
frol="frog_loot Console.Multicommand GenerateJewelAtUnitLevel 66; give_copper_cash 1000; give_silver_cash 1000; give_goldsun_cash 1000;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(frol,level),level)))
will="will_loot Console.Multicommand GenerateJewelAtUnitLevel 66; give \"[Name]Silver Resistance Potion - Item_Consumable_SilverResistancePotion_T02 - Guid: 2107622409\" 10; give \"[Prefab]Item_NewBag_T05 - Guid: 1117281334\"; give \"[Name]Elixir of the Werewolf - Item_Elixir_Werewolf_T01 - Guid: 948466634\" 10;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(will,level),level)))
level=70
cyrl="cyril_loot Console.Multicommand GenerateJewelAtUnitLevel 67; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100; give_pot_hp 100; give \"[Name]Potion of Rage - Item_Consumable_PhysicalPowerPotion_T02 - Guid: -1568756102\" 10; give \"[Name]Witch Potion - Item_Consumable_SpellPowerPotion_T02 - Guid: 1510182325\" 10; give \"[Name]Minor Sun Resistance Brew - Item_Consumable_SunResistancePotion_T01 - Guid: -38051433\" 10;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(cyrl,level),level)))
tier=4
sirl="sir_loot Console.Multicommand GenerateJewelAtUnitLevel 69; give \"[Prefab]Item_Cloak_Main_T03_Phantom - Guid: -227965303\"; give \"[Name]Silver Ore - Item_Ingredient_Mineral_SilverOre - Guid: 1686577386\" 250;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(sirl,level),level)))
level=74
frel="french_loot Console.Multicommand GenerateJewelAtUnitLevel 73; give \"[Name]Blood Merlot - Item_Consumable_PrisonPotion_Bloodwine - Guid: 1223264867\"; give \"[Name]Blood Merlot Amulet - Item_MagicSource_General_T07_BloodwineAmulet - Guid: 991396285\"; give \"[Prefab]Item_Ingredient_Plant_SacredGrapes - Guid: 88009216\" 1000;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(frel,level),level)))
harl="harpy_loot Console.Multicommand GenerateJewelAtUnitLevel 73; give \"[Name]Flawless Amethyst - Item_Ingredient_Gem_Amethyst_T03 - Guid: 1705028227\" 30; give \"[Name]Flawless Emerald - Item_Ingredient_Gem_Emerald_T03 - Guid: 1898237421\" 30; give \"[Name]Flawless Miststone - Item_Ingredient_Gem_Miststone_T03 - Guid: -1963826510\" 30; give \"[Name]Flawless Ruby - Item_Ingredient_Gem_Ruby_T03 - Guid: 74811721\" 30; give \"[Name]Flawless Sapphire - Item_Ingredient_Gem_Sapphire_T03 - Guid: -1147920398\" 30; give \"[Name]Flawless Topaz - Item_Ingredient_Gem_Topaz_T03 - Guid: -2051574178\" 30;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(harl,level),level)))
elel="element_loot Console.Multicommand GenerateJewelAtUnitLevel 73; GenerateJewelAtUnitLevel 73; GenerateJewelAtUnitLevel 73; GenerateJewelAtUnitLevel 73; GenerateJewelAtUnitLevel 73; GenerateJewelAtUnitLevel 73; give \"[Name]Holy Resistance Flask - Item_Consumable_HolyResistancePotion_T02 - Guid: 639992282\" 10;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(elel,level),level)))
prol="prof_loot Console.Multicommand GenerateJewelAtUnitLevel 77; give \"[Prefab]Item_Ingredient_Research_Schematic - Guid: 2085163661\" 1000; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(prol,level),level)))
jaml="jamila_loot Console.Multicommand GenerateJewelAtUnitLevel 78; give \"[Prefab]Item_Ingredient_Emery - Guid: -1578565561\" 1000; give \"[Name]Elixir of the Twisted - Item_Elixir_Twisted_T01 - Guid: 1646351394\" 10; give \"[Name]Stygian Shard - Item_NetherShard_T01 - Guid: 2103989354\" 2000; GenerateLegendaryWeapon Item_Weapon_Slashers_Legendary_T08_Shattered;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(jaml,level),level)))
level=77
matl="matka_loot Console.Multicommand GenerateJewelAtUnitLevel 79; give \"[Name]Silk - Item_Ingredient_Silk - Guid: 702067317\" 4; give \"[Prefab]Item_Ingredient_ReinforcedPlank - Guid: -1397591435\" 100; give \"[Prefab]Item_Ingredient_GhostYarn - Guid: 2106123809\" 100;  GenerateLegendaryWeapon Item_Weapon_Daggers_Legendary_T08_Shattered;"
add_tofile(file1, unlock_spell(add_thing(add_blood(add_weapon(matl,level),level), rsilk_armour)))
carl="carver_loot Console.Multicommand GenerateJewelAtUnitLevel 78; giveset Coating; give \"[Name]Venom Sap - Item_Ingredient_CorruptedSap - Guid: 2012771684\" 500; GenerateLegendaryWeapon Item_Weapon_GreatSword_Legendary_T08_Shattered;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(carl,level),level)))
alcl="alch_loot Console.Multicommand GenerateJewelAtUnitLevel 79; giveset Coating; give \"[Name]Venom Sap - Item_Ingredient_CorruptedSap - Guid: 2012771684\" 500; GenerateLegendaryWeapon Item_Weapon_Crossbow_Legendary_T08_Shattered; give \"[Name]Primal Blood Essence - Item_BloodEssence_T03_Primal - Guid: 1566989408\"; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 8; give \"[Name]Glass - Item_Ingredient_Glass - Guid: -1233716303\" 8; give \"[Name]Venom Sap - Item_Ingredient_CorruptedSap - Guid: 2012771684\" 32;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(alcl,level),level)))
clal="claw_loot Console.Multicommand GenerateJewelAtUnitLevel 79; give \"[Prefab]Item_Ingredient_PristineLeather - Guid: -2043983118\" 100; GenerateLegendaryWeapon Item_Weapon_Claws_Legendary_T08_Shattered;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(clal,level),level)))
level=80
goll="gold_loot Console.Multicommand GenerateJewelAtUnitLevel 82; GenerateLegendaryWeapon Item_Weapon_Longbow_Legendary_T08_Shattered; give \"[Name]Gold Ingot - Item_Ingredient_Mineral_GoldBar - Guid: -1027710236\" 100;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(goll,level),level)))
level=83
voll="volt_loot Console.Multicommand GenerateJewelAtUnitLevel 82; GenerateLegendaryWeapon Item_Weapon_Pistols_Legendary_T08_Shattered; give \"[Name]Charged Battery - Item_Ingredient_BatteryCharged - Guid: -412448857\" 100; give \"[Prefab]Item_Ingredient_PowerCore - Guid: -1190647720\" 50;"
add_tofile(file1, unlock_spell(add_thing(add_blood(add_weapon(voll,level),level), t3_magic)))
bell="belmont_loot Console.Multicommand GenerateJewelAtUnitLevel 85; GenerateLegendaryWeapon Item_Weapon_Whip_Legendary_T08_Shattered; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(bell,level),level)))
danl="dantos_loot Console.Multicommand GenerateJewelAtUnitLevel 85; GenerateLegendaryWeapon Item_Weapon_Mace_Legendary_T08_Shattered; give \"[Prefab]Item_Ingredient_Emberglass - Guid: -1715039285\" 200; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000;"
add_tofile(file1, unlock_spell(add_blood(add_weapon(danl,level),level)))
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
morl="morgana_loot Console.Multicommand GenerateJewelAtUnitLevel 91; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100; give \"[Prefab]Item_Ingredient_OnyxTear - Guid: -651878258\" 10; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 2000; give \"[Name]Blood Key - Item_MagicSource_BloodKey_T01 - Guid: 1655869633\"; give_drac_boot; give_drac_gloves; give_drac_legs; give_drac_chest;"
add_tofile(file1, add_thing(add_blood(add_weapon(morl,level),level), drac_chest))
level=91
dral="drac_loot Console.Multicommand GenerateJewelAtUnitLevel 94; give \"[Name]Dark Silver Ingot - Item_Ingredient_Mineral_DarkSilverBar - Guid: -762000259\" 100; give \"[Prefab]Item_Ingredient_OnyxTear - Guid: -651878258\" 10; give \"[Name]Greater Stygian Shard - Item_NetherShard_T02 - Guid: 576389135\" 10000;"
add_tofile(file1, add_thing(add_blood(add_weapon(dral,level),level), drac_armour))
if(generate_spells==0):
    add_tofile(file1, "givespell3 Console.RemoveAlias givespell3")
    add_tofile(file1, "givespell2 Console.RemoveAlias givespell2")

if(boss_shuffle==1):
    boss_shuffle_path="./../misc/boss_shuffle.json"
    boss_lvl_def=[20, 20, 20, 27, 32, 27, 30, 30, 35, 35, 35, 37, 40, 44, 44, 44, 46, 47, 47, 47, 50, 50, 50, 53, 53, 53, 55, 57, 57, 57, 58, 60, 60, 75, 61, 63, 63, 63, 64, 64, 65, 66, 70, 70, 70, 74, 75, 76, 76, 76, 79, 79, 81, 82, 84, 84, 84, 86, 86, 88, 88, 91]
    boss_lvl_ptr=["<kel_lvl>", "<sto_lvl>", "<ruf_lvl>", "<gra_lvl>", "<fis_lvl>", "<swi_lvl>", "<cha_lvl>", "<cli_lvl>", "<pol_lvl>", "<bea_lvl>", "<nic_lvl>", "<qui_lvl>", "<dea_lvl>", "<vin_lvl>", "<nun_lvl>", "<tri_lvl>", "<hor_lvl>", "<maj_lvl>", "<lea_lvl>", "<kri_lvl>", "<gla_lvl>", "<ban_lvl>", "<ble_lvl>", "<fro_lvl>", "<ele_lvl>", "<ter_lvl>", "<are_lvl>", "<jad_lvl>", "<swo_lvl>", "<raz_lvl>", "<oct_lvl>", "<iva_lvl>", "<dom_lvl>", "<jam_lvl>", "<ang_lvl>", "<spi_lvl>", "<ben_lvl>", "<fau_lvl>", "<fro_lvl>", "<wil_lvl>", "<cyr_lvl>", "<sir_lvl>", "<fre_lvl>", "<har_lvl>", "<elm_lvl>", "<pro_lvl>", "<car_lvl>", "<mat_lvl>", "<alc_lvl>", "<cla_lvl>", "<vol_lvl>", "<bel_lvl>", "<gol_lvl>", "<dan_lvl>", "<stx_lvl>", "<gor_lvl>", "<val_lvl>", "<hor_lvl>", "<sol_lvl>", "<meg_lvl>", "<ada_lvl>", "<dra_lvl>"]
    boss_id_val=[1124739990, -2025101517, 2122229952, 1106149033, -2122682556, 577478542, 763273073, 1896428751, -484556888, -1391546313, 153390636, -1659822956, -1942352521, -29797003, -99012450, -1449631170, 619948378, 1945956671, 939467639, -1365931036, 910988233, 613251918, 850622034, 24378719, 795262842, -1065970933, -753453016, -1968372384, -496360395, -680831417, 1688478381, 172235178, -1101874342, -1383529374, 106480588, -548489519, 109969450, -1208888966, -203043163, -1505705712, 326378955, -26105228, 192051202, 685266977, -2013903325, 814083983, -1669199769, -910296704, 1295855316, -1347412392, 2054432370, 336560131, 114912615, 173259239, 1112948824, -1936575244, 495971434, -393555055, -740796338, 591725925, 1233988687, -327335305]
    boss_id_ptr=["<kel_id>", "<sto_id>", "<ruf_id>", "<gra_id>", "<fis_id>", "<swi_id>", "<cha_id>", "<cli_id>", "<pol_id>", "<bea_id>", "<nic_id>", "<qui_id>", "<dea_id>", "<vin_id>", 
    "<nun_id>", "<tri_id>", "<hor_id>", "<maj_id>", "<lea_id>", "<kri_id>", "<gla_id>", "<ban_id>", "<ble_id>", "<fro_id>", "<ele_id>", "<ter_id>", "<are_id>", "<jad_id>", "<swo_id>", 
    "<raz_id>", "<oct_id>", "<iva_id>", "<dom_id>", "<jam_id>", "<ang_id>", "<spi_id>", "<ben_id>", "<fau_id>", "<fro_id>", "<wil_id>", "<cyr_id>", "<sir_id>", "<fre_id>", "<har_id>", 
    "<elm_id>", "<pro_id>", "<car_id>", "<mat_id>", "<alc_id>", "<cla_id>", "<vol_id>", "<bel_id>", "<gol_id>", "<dan_id>", "<stx_id>", "<gor_id>", "<val_id>", "<hor_id>", "<sol_id>", 
    "<meg_id>", "<ada_id>", "<dra_id>"]
    boss_lvl_random=[]
    boss_id_val_copy=boss_id_val.copy()
    boss_lvl_copy=boss_lvl_def.copy()
    shuffle_name_ptr="<some_number>"
    date_time_ptr="<date_time>"
    boss_rush_file_name="./../examples/boss_shuffle_"+now+".json"
    if(os.path.isfile(boss_rush_file_name)==False):
        shutil.copyfile(boss_shuffle_path, boss_rush_file_name)
    
    with open(boss_rush_file_name, 'r') as file:
        filedata = file.read()
    
    filedata = filedata.replace(shuffle_name_ptr, now)
    filedata = filedata.replace(date_time_ptr, now)
    
    boss_num_local=0
    for boss_ptr in boss_lvl_ptr:
        filedata = filedata.replace(boss_ptr, str(boss_lvl_def[boss_lvl_ptr.index(boss_ptr)]))

    boss_id_local=0
    boss_random =[]
    for boss_id_num in boss_id_ptr:
        if(len(boss_id_val_copy)==1):
            boss_id_local=boss_id_val_copy.pop()
        else:
            boss_num_local=random.randrange(0,len(boss_id_val_copy)-1)
            boss_id_local=boss_id_val_copy.pop(boss_num_local)
        boss_random.append(boss_id_val.index(boss_id_local))
        # print(str(boss_id_val.index(boss_id_local)) + ",  ,")
        # print(str(boss_id_local) + ",  ,"+ str(boss_id_val.index(boss_id_local)))
        filedata = filedata.replace(boss_id_num, str(boss_id_local))
    
    with open(boss_rush_file_name, 'w') as file:
        file.write(filedata)
    boss_tp_arr=["teleport self WorldPosition -1000 0 -1380", "Teleport Self chunk:10,10", "teleport self WorldPosition -1220 0 -1550", "TeleportToNearestUnitOfType CHAR_Bandit_Stalker_VBlood", 
    "teleport self WorldPosition -828 0 -1230", "teleport self WorldPosition -1555 20 -1720", "TeleportToNearestUnitOfType CHAR_Bandit_Chaosarrow_VBlood", "teleport self WorldPosition -2150 0 -1500",
    "teleport self WorldPosition -2000 0 -1200", "TeleportToNearestUnitOfType CHAR_Forest_Bear_Dire_Vblood", "TeleportToNearestUnitOfType CHAR_Undead_Priest_Vblood", "TeleportToNearestUnitOfType CHAR_Bandit_Tourok_VBlood",
    "teleport self WorldPosition -1020 0 -880", "TeleportToNearestUnitOfType CHAR_Militia_Guard_VBlood", "TeleportToNearestUnitOfType CHAR_Militia_Nun_VBlood", "TeleportToNearestUnitOfType CHAR_VHunter_Leader_VBlood",
    "TeleportToNearestUnitOfType CHAR_Militia_Fabian_VBlood", "TeleportToNearestUnitOfType CHAR_Militia_Scribe_VBlood", "TeleportToNearestUnitOfType CHAR_Undead_BishopOfShadows_Vblood", "Teleport self WorldPosition -1368 0 -1050",
    "TeleportToNearestUnitOfType CHAR_Militia_Glassblower_VBlood", "TeleportToNearestUnitOfType CHAR_Undead_Infiltrator_Vblood", "Teleport self WorldPosition -1368 0 -890", "Teleport self WorldPosition -600 0 -1090", 
    "Teleport self WorldPosition -600 0 -790", "TeleportToNearestUnitOfType CHAR_Geomancer_Human_VBlood", "TeleportToNearestUnitOfType CHAR_Undead_ArenaChampion_Vblood", "TeleportToNearestUnitOfType CHAR_VHunter_Jade_VBlood",
    "TeleportToNearestUnitOfType CHAR_Vampire_HighLord_VBlood", "TeleportToNearestUnitOfType CHAR_Militia_BishopOfDunley_VBlood", "TeleportToNearestUnitOfType CHAR_Militia_Leader_VBlood", "TeleportToNearestUnitOfType CHAR_Gloomrot_Iva_VBlood",
    "Teleport self WorldPosition -1670 0 -200", "TeleportToNearestUnitOfType CHAR_Blackfang_Livith_VBlood", "Teleport self WorldPosition -1670 0 -5", "TeleportToNearestUnitOfType CHAR_Spider_Queen_Vblood", 
    "TeleportToNearestUnitOfType CHAR_Villager_CursedWanderer_VBlood", "TeleportToNearestUnitOfType CHAR_Undead_ZealousCultist_VBlood", "TeleportToNearestUnitOfType CHAR_Cursed_ToadKing_VBlood", "teleport self WorldPosition -1050 0 -250",
    "TeleportToNearestUnitOfType CHAR_Undead_CursedSmith_Vblood", "TeleportToNearestUnitOfType CHAR_ChurchOfLight_Overseer_VBlood", "TeleportToNearestUnitOfType CHAR_ChurchOfLight_Sommelier_VBlood",
    "TeleportToNearestUnitOfType CHAR_Harpy_Matriarch_VBlood", "TeleportToNearestUnitOfType CHAR_ArchMage_VBlood", "teleport self WorldPosition -1800 0 46", "TeleportToNearestUnitOfType CHAR_Blackfang_CarverBoss_VBlood", 
    "TeleportToNearestUnitOfType CHAR_Cursed_Witch_VBlood", "TeleportToNearestUnitOfType CHAR_Blackfang_Lucie_VBlood", "TeleportToNearestUnitOfType CHAR_Winter_Yeti_VBlood", "TeleportToNearestUnitOfType CHAR_Gloomrot_RailgunSergeant_VBlood",
    "TeleportToNearestUnitOfType CHAR_VHunter_CastleMan", "TeleportToNearestUnitOfType CHAR_ChurchOfLight_Cardinal_VBlood", "TeleportToNearestUnitOfType CHAR_Blackfang_Valyr_VBlood", "teleport self WorldPosition -1400 0 -250",
    "teleport self WorldPosition -700 10 -105", "TeleportToNearestUnitOfType CHAR_Vampire_BloodKnight_VBlood", "TeleportToNearestUnitOfType CHAR_Manticore_VBlood", "TeleportToNearestUnitOfType CHAR_ChurchOfLight_Paladin_VBlood",
    "TeleportToNearestUnitOfType CHAR_Blackfang_Morgana_VBlood", "TeleportToNearestUnitOfType CHAR_Gloomrot_Monster_VBlood", "teleport self WorldPosition 720 15 -2827"]
    boss_tp_names=["tp_wp_stone", "tp_wp_rufus", "tp_wp_kelly", "tp_wp_swine", "tp_vb_grayson", "tp_wp_clive", "tp_vb_chaos", "tp_wp_fish",
    "tp_vb_bear", "tp_vb_nick", "tp_wp_polora", "tp_vb_quincy", "tp_wp_deamon", "tp_vb_vinc", "tp_vb_nun", "tp_vb_tri", "tp_vb_horse", "tp_wp_mine", 
    "tp_vb_leandr", "tp_vb_maja", "tp_vb_assas", "tp_vb_glass", "tp_wp_bless", "tp_wp_elena", "tp_wp_frost", "tp_vb_tera", "tp_vb_arena", "tp_vb_sword", 
    "tp_vb_jade", "tp_vb_raziel", "tp_vb_octav", "tp_wp_domina", "tp_vb_iva", "tp_wp_angram", "tp_vb_spider", "tp_vb_ben", "tp_vb_faul", "tp_vb_frog", 
    "tp_wp_will", "tp_vb_cyril", "tp_vb_sir", "tp_vb_french", "tp_vb_harpy", "tp_vb_element", "tp_wp_prof", "tp_vp_jamila", "tp_vb_matka", "tp_vb_carver", 
    "tp_vb_alch", "tp_vb_claw", "tp_vb_gold", "tp_vb_volt", "tp_vb_belmont", "tp_vb_dantos", "tp_wp_styx", "tp_vb_val", "tp_wp_gore", "tp_vb_horror", 
    "tp_vb_solarus", "tp_vb_morgana", "tp_vb_adam", "tp_wp_drac"]
    file1 = open(random_prof_path, "a+")
    file1.write("bossshuffle_code_below Console.MultiCommand give_vermin; give_vermin;\n")
    for random_boss_num in range(0,len(boss_random)):
        add_tofile(file1, boss_tp_names[random_boss_num]+ " "+boss_tp_arr[boss_random[random_boss_num]])
