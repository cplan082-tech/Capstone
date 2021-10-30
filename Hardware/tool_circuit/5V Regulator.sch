EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 8
Title "12V-5V Regulator"
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	2350 800  2350 900 
$Comp
L KCM55QR7YA226KH01L:KCM55QR7YA226KH01L C1
U 1 1 61326360
P 2850 2350
F 0 "C1" H 2900 2590 50  0000 C CNN
F 1 "22UF" H 2900 2499 50  0000 C CNN
F 2 "KCM55QR7YA226KH01L:CAPC6153X390N" H 2850 2350 50  0001 L BNN
F 3 "https://www.snapeda.com/parts/KCM55QR7YA226KH01L/Murata%20Electronics/view-part/1365129/?welcome=home&ref=search&t=KCM55QR7YA226KH01L#" H 2850 2350 50  0001 L BNN
	1    2850 2350
	0    -1   -1   0   
$EndComp
$Comp
L 12063D106MAT2A:12063D106MAT2A C4
U 1 1 613292F8
P 10000 2350
F 0 "C4" H 10050 2590 50  0000 C CNN
F 1 "10UF" H 10050 2499 50  0000 C CNN
F 2 "12063D106MAT2A:CAPC3216X178N" H 10000 2350 50  0001 L BNN
F 3 "" H 10000 2350 50  0001 L BNN
	1    10000 2350
	0    -1   -1   0   
$EndComp
$Comp
L CL31B104KBCNNNC:CL31B104KBCNNNC C3
U 1 1 6138E334
P 6800 1450
F 0 "C3" H 6850 1690 50  0000 C CNN
F 1 "0.1UF" H 6850 1599 50  0000 C CNN
F 2 "CL31B104KBCNNNC:CAPC3216X180N" H 6800 1450 50  0001 L BNN
F 3 "" H 6800 1450 50  0001 L BNN
	1    6800 1450
	1    0    0    -1  
$EndComp
$Comp
L TPS563211DRLR:TPS563211DRLR U1
U 1 1 61393280
P 4700 1450
F 0 "U1" H 5450 1838 60  0000 C CNN
F 1 "TPS563211DRLR" H 5450 1732 60  0000 C CNN
F 2 "ul_TPS563211DRLR:TPS563211DRLR" H 4700 1390 60  0001 C CNN
F 3 "" H 4700 1450 60  0000 C CNN
	1    4700 1450
	1    0    0    -1  
$EndComp
Wire Wire Line
	2350 1450 2850 1450
Wire Wire Line
	2850 2150 2850 1450
Connection ~ 2850 1450
Wire Wire Line
	3400 2150 3400 1450
Connection ~ 3400 1450
Wire Wire Line
	3400 1450 4700 1450
Wire Wire Line
	3400 2450 3400 2950
Wire Wire Line
	3400 2950 3700 2950
Wire Wire Line
	4500 2950 4500 3000
Wire Wire Line
	2850 2450 2850 2950
Wire Wire Line
	2850 2950 3400 2950
Connection ~ 3400 2950
Wire Wire Line
	4700 2050 4500 2050
Wire Wire Line
	4500 2050 4500 2950
Wire Wire Line
	4700 1850 4400 1850
Wire Wire Line
	4400 1850 4400 800 
Wire Wire Line
	4400 800  5200 800 
$Comp
L RNCP1206FTD10K0:RNCP1206FTD10K0 R3
U 1 1 61403723
P 5600 800
F 0 "R3" H 5600 1042 50  0000 C CNN
F 1 "10K" H 5600 951 50  0000 C CNN
F 2 "RNCP1206FTD10K0:RESC3115X60N" H 5600 800 50  0001 L BNN
F 3 "" H 5600 800 50  0001 L BNN
	1    5600 800 
	1    0    0    -1  
$EndComp
Wire Wire Line
	6200 1450 6700 1450
Wire Wire Line
	6200 1650 7000 1650
Wire Wire Line
	7000 1650 7000 1450
$Comp
L 2021-09-13_22-06-51:SDR1307-4R7ML L1
U 1 1 6140681E
P 7100 1650
F 0 "L1" H 7400 1939 60  0000 C CNN
F 1 "4.7UH" H 7400 1833 60  0000 C CNN
F 2 "ul_SDR1307-4R7ML:SDR1307-4R7ML" H 7375 1365 60  0001 C CNN
F 3 "" H 7100 1650 60  0000 C CNN
	1    7100 1650
	1    0    0    -1  
$EndComp
Wire Wire Line
	7000 1650 7100 1650
Connection ~ 7000 1650
Wire Wire Line
	6000 800  8300 800 
Wire Wire Line
	8300 800  8300 1650
Wire Wire Line
	8300 1650 7700 1650
Wire Wire Line
	6200 2050 6200 2950
$Comp
L 2021-09-13_22-27-50:RC0603FR-0782KL R4
U 1 1 6140CEA8
P 8750 1700
F 0 "R4" V 8947 1779 60  0000 L CNN
F 1 "82K" V 9053 1779 60  0000 L CNN
F 2 "ul_RC0603FR-0782KL:RC0603FR-0782KL" H 9000 1365 60  0001 C CNN
F 3 "" H 8750 1700 60  0000 C CNN
	1    8750 1700
	0    1    1    0   
$EndComp
Wire Wire Line
	8300 1650 8750 1650
Wire Wire Line
	8750 1650 8750 1700
Connection ~ 8300 1650
Wire Wire Line
	6200 1850 8350 1850
Wire Wire Line
	8350 1850 8350 2200
Wire Wire Line
	8350 2200 8750 2200
$Comp
L CRCW040210K0DHEDP:CRCW040210K0DHEDP R5
U 1 1 6140F8A3
P 8750 2750
F 0 "R5" V 8704 2855 50  0000 L CNN
F 1 "10K" V 8795 2855 50  0000 L CNN
F 2 "CRCW040210K0DHEDP:RESC1005X40N" H 8750 2750 50  0001 L BNN
F 3 "" H 8750 2750 50  0001 L BNN
	1    8750 2750
	0    1    1    0   
$EndComp
Wire Wire Line
	8750 2200 8750 2350
Connection ~ 8750 2200
Wire Wire Line
	8750 3150 6200 3150
Wire Wire Line
	6200 3150 6200 2950
Connection ~ 6200 2950
Wire Wire Line
	8750 1650 10000 1650
Wire Wire Line
	10000 1650 10000 2150
Connection ~ 8750 1650
Wire Wire Line
	10000 2450 10000 3150
Wire Wire Line
	10000 3150 8750 3150
Connection ~ 8750 3150
Connection ~ 10000 1650
$Comp
L power:+12V #PWR02
U 1 1 614E38F8
P 2350 800
F 0 "#PWR02" H 2350 650 50  0001 C CNN
F 1 "+12V" H 2365 973 50  0000 C CNN
F 2 "" H 2350 800 50  0001 C CNN
F 3 "" H 2350 800 50  0001 C CNN
	1    2350 800 
	1    0    0    -1  
$EndComp
$Comp
L power:+5V #PWR04
U 1 1 614E7ADA
P 10600 1650
F 0 "#PWR04" H 10600 1500 50  0001 C CNN
F 1 "+5V" V 10615 1778 50  0000 L CNN
F 2 "" H 10600 1650 50  0001 C CNN
F 3 "" H 10600 1650 50  0001 C CNN
	1    10600 1650
	0    1    1    0   
$EndComp
Wire Wire Line
	2350 900  1850 900 
Wire Wire Line
	1850 900  1850 1000
Connection ~ 2350 900 
Wire Wire Line
	2350 900  2350 1450
Wire Wire Line
	10000 1650 10600 1650
$Comp
L power:GND #PWR01
U 1 1 615ABBAB
P 1850 2500
F 0 "#PWR01" H 1850 2250 50  0001 C CNN
F 1 "GND" H 1855 2327 50  0000 C CNN
F 2 "" H 1850 2500 50  0001 C CNN
F 3 "" H 1850 2500 50  0001 C CNN
	1    1850 2500
	1    0    0    -1  
$EndComp
$Comp
L CRGCQ1206F820R:CRGCQ1206F820R R1
U 1 1 615F0A81
P 1850 2100
F 0 "R1" V 1804 2205 50  0000 L CNN
F 1 "820" V 1895 2205 50  0000 L CNN
F 2 "CRGCQ1206F820R:RESC3115X65N" H 1850 2100 50  0001 L BNN
F 3 "" H 1850 2100 50  0001 L BNN
F 4 "2-2176343-4" H 1850 2100 50  0001 L BNN "Comment"
	1    1850 2100
	0    1    1    0   
$EndComp
$Comp
L 2021-10-08_20-10-06:RK73Z2BTTD R2
U 1 1 616405FD
P 3700 1950
F 0 "R2" V 3897 2029 60  0000 L CNN
F 1 "0" V 4003 2029 60  0000 L CNN
F 2 "RK73Z2BTTD:RK73Z2BTTD" H 3950 1615 60  0001 C CNN
F 3 "" H 3700 1950 60  0000 C CNN
	1    3700 1950
	0    1    1    0   
$EndComp
Wire Wire Line
	4700 1650 3700 1650
Wire Wire Line
	3700 1650 3700 1950
Wire Wire Line
	3700 2450 3700 2950
Connection ~ 3700 2950
Connection ~ 4500 2950
$Comp
L power:GND #PWR03
U 1 1 61401F04
P 4500 3000
F 0 "#PWR03" H 4500 2750 50  0001 C CNN
F 1 "GND" H 4505 2827 50  0000 C CNN
F 2 "" H 4500 3000 50  0001 C CNN
F 3 "" H 4500 3000 50  0001 C CNN
	1    4500 3000
	1    0    0    -1  
$EndComp
Wire Wire Line
	3700 2950 4500 2950
Wire Wire Line
	4500 2950 6200 2950
$Comp
L CL31B104KBCNNNC:CL31B104KBCNNNC C2
U 1 1 6164A2E7
P 3400 2250
F 0 "C2" V 3404 2353 50  0000 L CNN
F 1 "0.1UF" V 3495 2353 50  0000 L CNN
F 2 "" H 3400 2250 50  0001 L BNN
F 3 "" H 3400 2250 50  0001 L BNN
	1    3400 2250
	0    1    1    0   
$EndComp
Text Label 1900 900  0    50   ~ 0
12V_LED
$Comp
L S2751-46R:S2751-46R TP1
U 1 1 6164D605
P 3400 1350
F 0 "TP1" H 3485 1417 50  0000 L CNN
F 1 "S2751-46R" H 3485 1326 50  0000 L CNN
F 2 "S2751-46R:HARWIN_S2751-46R" H 3400 1350 50  0001 L BNN
F 3 "" H 3400 1350 50  0001 L BNN
F 4 "HARWIN" H 3400 1350 50  0001 L BNN "MANUFACTURER"
F 5 "Manufacturer Recommendations" H 3400 1350 50  0001 L BNN "STANDARD"
F 6 "" H 3400 1350 50  0001 L BNN "PARTREV"
	1    3400 1350
	1    0    0    -1  
$EndComp
Wire Wire Line
	2850 1450 3400 1450
$Comp
L S2751-46R:S2751-46R TP2
U 1 1 6164FDC2
P 8750 1550
F 0 "TP2" H 8835 1617 50  0000 L CNN
F 1 "S2751-46R" H 8835 1526 50  0000 L CNN
F 2 "S2751-46R:HARWIN_S2751-46R" H 8750 1550 50  0001 L BNN
F 3 "" H 8750 1550 50  0001 L BNN
F 4 "HARWIN" H 8750 1550 50  0001 L BNN "MANUFACTURER"
F 5 "Manufacturer Recommendations" H 8750 1550 50  0001 L BNN "STANDARD"
F 6 "" H 8750 1550 50  0001 L BNN "PARTREV"
	1    8750 1550
	1    0    0    -1  
$EndComp
$Comp
L WP7113GD:WP7113GD D1
U 1 1 617EBD7B
P 1850 1400
F 0 "D1" V 1946 1321 50  0000 R CNN
F 1 "Green" V 1855 1321 50  0000 R CNN
F 2 "WP7113GD:LED_WP7113GD" H 1850 1400 50  0001 L BNN
F 3 "" H 1850 1400 50  0001 L BNN
F 4 "Kingbright" H 1850 1400 50  0001 L BNN "MANUFACTURER"
	1    1850 1400
	0    -1   -1   0   
$EndComp
$EndSCHEMATC
