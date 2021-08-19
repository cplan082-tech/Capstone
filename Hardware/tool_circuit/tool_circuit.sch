EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 5
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Sheet
S 5950 2200 1250 750 
U 611DBC89
F0 "Temp_Sense" 50
F1 "Temp_Sense.sch" 50
F2 "TEMP_DATA" B L 5950 2550 50 
$EndSheet
$Sheet
S 5850 4200 1150 700 
U 611DF2F9
F0 "Battery_Monitor" 50
F1 "Battery_Monitor.sch" 50
F2 "BATT_MON_DATA" B L 5850 4450 50 
$EndSheet
$Sheet
S 2100 4250 1250 650 
U 611E1BEE
F0 "Pi_Connection" 50
F1 "Pi_Connection.sch" 50
F2 "DATA" B R 3350 4450 50 
$EndSheet
Wire Bus Line
	3350 4450 5250 4450
Wire Bus Line
	5950 2550 5250 2550
Wire Bus Line
	5250 2550 5250 4450
Connection ~ 5250 4450
Wire Bus Line
	5250 4450 5850 4450
$Sheet
S 2000 2450 1400 850 
U 611DBAE9
F0 "Power_Src" 50
F1 "Power_Src.sch" 50
$EndSheet
Wire Wire Line
	8100 2500 9850 2500
Wire Wire Line
	9850 2500 9850 1450
Wire Wire Line
	9850 1450 8800 1450
Wire Wire Line
	8800 1450 8800 3650
Wire Wire Line
	8800 3650 8850 3650
$EndSCHEMATC
