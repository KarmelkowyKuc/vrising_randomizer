#Randomizer V rising without mods

==============================================================================

Current work status of randomizer, so far basic list and *.prof to put it into.

Go under:

C:\Users\<USER>\AppData\LocalLow\Stunlock Studios\VRising\ConsoleProfile

in file DefaultProfile should have one that it is going to run after restart:

open that *.prof

copy below contents of ./misc/DESKTOP-asdf.prof under your ConsoleProfile default

==============================================================================

The config should load after you boot your game (check console for the profile name and amount of aliases (should be alot))

Run private brutal server (just set lvl to 100) with some fun settings,

Adminauth after you join, wake from your grave, type in console:
    
    ready
 
- place castle hearth and Altar of Recollection, some walls and chests - remove all blood skills.

- after every base teleport you will get 2 skill jewels - chose them to fight the next boss, if you get dash, or dupe just get a spell with command:

    givespell
    givespell2
    givespell3

- it is up to you if you want to use them or not, but it is quite nice ingame spell randomizer. To get your basic equipement type command:
 
    gear
    
- there isn't any form of weapon randomizer, you can choose which one you want or so you can use wheel like this: 

    https://wheelofnames.com/tp4-f7f
    
    
- same goes for blood, but would go for 15% 45% 75% 90% for each act or use wheel of scam:

    https://wheelofnames.com/6gv-98s

- afterwards if you want to go for boss fight type 
    
    goboss

If you die, instead type 

    repeat
    
If you kill the boss, type:

    base
    
should give you next 2 spells and proper gear to fight next boss.

IMPORTANT!

So far, there is an issue with traveling bosses, which you can teleport only once and if you die, or walk awya far enough you cannot use the same command to teleport to them.

Don't know the solution, since noone ever uses this command and will never be changed (probably):

    TeleportToNearestUnitOfType CHAR_Undead_BishopOfDeath_VBlood

Since I have not clue how to fix this issue, might be the best to teleport to your bag (if you die via TeleportToMapMarker) or follow the Vblood tracker.

There is a possibility to add shortcuts with Console.Bind command and add full path of traveling boss to teleport from one place to another (until you spot the boss), but it is just way too much work.

CBA, use teleport self mouse or smth with bind.

Added binds:

    Shift+b base  -- teleport to base location, give 2 random spells and gear for next boss
    Shift+s givespell  -- generate and give 1 jewel with random spell
    Shift+n goboss  -- teleport to the next 
    Shift+r repeat  -- repeat boss encounter if you die (might not work properly for traveling bosses - will tp you to first teleport - use shift+M or shift+A to get back to boss)
    Shift+M TeleportToMapMarker  -- teleport to marked place on map - helpful if you want to return to some bosses
    Shift+A Teleport Self Cursor -- teleport to current cursor position - helpful if you are searching for a boss

Should be even smoother now, if looking for a boss just mapmarker and shift+M afterwards or follow the blood trail with Shift+A until you find it.

=============================================================================

TODO:
    - finish scripting gear and boss progression, with usage of world position whenever it can be used
    - add progression - let's say random jewel after some bosses, or mats like ember bars to be able to smelt some nice gems
    - ENDGAME content - after killing drac, increase levels of bosses and start over with gear (except from jewels)
    - decide how to random passives and when add em

=============================================================================
The idea to look for traveling vbloods is like this, after you press Shift+V should look for it:

    swine0pos Console.MultiCommand teleport self WorldPosition -1552 0 -1730; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine1pos;
    swine1pos Console.MultiCommand teleport self WorldPosition -1552 0 -1700; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine2pos;
    swine2pos Console.MultiCommand teleport self WorldPosition -1552 0 -1680; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine3pos;
    swine3pos Console.MultiCommand teleport self WorldPosition -1542 0 -1670; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine4pos;
    swine4pos Console.MultiCommand teleport self WorldPosition -1532 0 -1657; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine5pos;
    swine5pos Console.MultiCommand teleport self WorldPosition -1522 0 -1648; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine6pos;
    swine6pos Console.MultiCommand teleport self WorldPosition -1512 0 -1637; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine7pos;
    swine7pos Console.MultiCommand teleport self WorldPosition -1492 0 -1625; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine8pos;
    swine8pos Console.MultiCommand teleport self WorldPosition -1472 0 -1623; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine9pos;
    swine9pos Console.MultiCommand teleport self WorldPosition -1452 0 -1625; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine10pos;
    swine10pos Console.MultiCommand teleport self WorldPosition -1432 0 -1621; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine11pos;
    swine11pos Console.MultiCommand teleport self WorldPosition -1412 0 -1636; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine12pos;
    swine12pos Console.MultiCommand teleport self WorldPosition -1395 0 -1641; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine13pos;
    swine13pos Console.MultiCommand teleport self WorldPosition -1370 0 -1641; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine14pos;
    swine14pos Console.MultiCommand teleport self WorldPosition -1350 0 -1635; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine15pos;
    swine15pos Console.MultiCommand teleport self WorldPosition -1330 0 -1630; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine16pos;
    swine16pos Console.MultiCommand teleport self WorldPosition -1310 0 -1630; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine17pos;
    swine17pos Console.MultiCommand teleport self WorldPosition -1290 0 -1630; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine18pos;
    swine18pos Console.MultiCommand teleport self WorldPosition -1270 0 -1630; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine19pos;
    swine19pos Console.MultiCommand teleport self WorldPosition -1250 0 -1640; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine20pos;
    swine20pos Console.MultiCommand teleport self WorldPosition -1230 0 -1650; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine21pos;
    swine21pos Console.MultiCommand teleport self WorldPosition -1210 0 -1660; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine22pos;
    swine22pos Console.MultiCommand teleport self WorldPosition -1218 0 -1660; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine23pos;
    swine23pos Console.MultiCommand teleport self WorldPosition -1218 0 -1680; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine24pos;
    swine24pos Console.MultiCommand teleport self WorldPosition -1218 0 -1700; Console.RemoveAlias find_vblood; Console.Alias find_vblood swine0pos;
    Shift+v find_vblood
    find_vblood swine0pos

this if the shortest vblood path, with about 25 markers, don't think it is worth anyones time to do it for Tristan, Vincent, Jade, Meredith, Ben, Gorecrusher, Lidia, Bane, Frostmaw, Elena, Cassius, Jakira, Belmont.

CBA
