EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 7
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
S 5850 4200 1150 700 
U 611DF2F9
F0 "Vibration_Sensor" 50
F1 "Vibration_Sensor.sch" 50
F2 "VIB_DATA" B L 5850 4450 50 
$EndSheet
Wire Bus Line
	3350 4450 5250 4450
Wire Bus Line
	5950 2550 5250 2550
Wire Bus Line
	5250 4450 5850 4450
$Comp
L power:+12V #PWR0101
U 1 1 6125A008
P 2850 2050
F 0 "#PWR0101" H 2850 1900 50  0001 C CNN
F 1 "+12V" H 2865 2223 50  0000 C CNN
F 2 "" H 2850 2050 50  0001 C CNN
F 3 "" H 2850 2050 50  0001 C CNN
	1    2850 2050
	1    0    0    -1  
$EndComp
Text HLabel 2850 2450 3    50   Input ~ 0
12V_BATTERY
Wire Wire Line
	2850 2050 2850 2450
Text HLabel 3050 3300 1    50   Output ~ 0
12V_BATTERY
Text HLabel 3200 3300 1    50   Output ~ 0
5V
$Sheet
S 2000 2450 1400 850 
U 611DBAE9
F0 "Power_Src" 50
F1 "Power_Src.sch" 50
$EndSheet
$Sheet
S 5950 2200 1250 750 
U 611DBC89
F0 "Temp_Sense" 50
F1 "Temp_Sense.sch" 50
F2 "TEMP_DATA" B L 5950 2550 50 
$EndSheet
Connection ~ 5250 4450
Wire Bus Line
	5250 2550 5250 4450
$Sheet
S 1750 4200 1600 1050
U 61460B87
F0 "raspberrypi_zerow_uhat" 50
F1 "raspberrypi_zerow_uhat.sch" 50
$EndSheet
$Sheet
S 5850 5450 1150 650 
U 61495548
F0 "Accelerometer" 50
F1 "Accelerometer.sch" 50
$EndSheet
Wire Bus Line
	5250 4450 5250 5750
Wire Bus Line
	5250 5750 5850 5750
Text HLabel 5850 5750 2    50   BiDi ~ 0
ACC_DATA
Text HLabel 5950 2700 2    50   Input ~ 0
3v3
Text HLabel 5850 4650 2    50   Input ~ 0
5V_BATTERY
Text HLabel 5850 5900 2    50   Input ~ 0
3v3
$EndSCHEMATC
