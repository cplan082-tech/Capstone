EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 8
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Bus Line
	5950 2550 5250 2550
$Sheet
S 2600 2350 1400 850 
U 611DBAE9
F0 "Power_Src" 50
F1 "Power_Src.sch" 50
$EndSheet
Connection ~ 5250 4450
Wire Bus Line
	5250 4450 5250 4550
$Sheet
S 5850 4200 1150 700 
U 611DF2F9
F0 "Time_of_Use" 50
F1 "Time_of_Use.sch" 50
F2 "TIME_OF_USE_DATA" B L 5850 4450 50 
$EndSheet
$Sheet
S 5950 2200 1250 750 
U 611DBC89
F0 "Temp_Sense" 50
F1 "Temp_Sense.sch" 50
F2 "TEMP_DATA" B L 5950 2550 50 
$EndSheet
Wire Bus Line
	5250 2550 5250 4450
Wire Bus Line
	5250 4450 5850 4450
$Sheet
S 5900 5500 1150 650 
U 61514F06
F0 "Accelerometer.sch" 50
F1 "Accelerometer.sch" 50
F2 "ACC_DATA" B L 5900 5750 50 
$EndSheet
Wire Bus Line
	5250 5750 5900 5750
$Sheet
S 1550 4300 1800 900 
U 61514F71
F0 "raspberrypi_header.sch" 50
F1 "raspberrypi_header.sch" 50
F2 "PI_CONN" B R 3350 4550 50 
$EndSheet
Connection ~ 5250 4550
Wire Bus Line
	5250 4550 5250 5750
Wire Bus Line
	3350 4550 5250 4550
$EndSCHEMATC
