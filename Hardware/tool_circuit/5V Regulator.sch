EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 4 6
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text HLabel 1950 2850 1    50   Input ~ 0
12V_BATTERY
Wire Wire Line
	1950 2850 1950 3500
$Comp
L KCM55QR7YA226KH01L:KCM55QR7YA226KH01L C1
U 1 1 61326360
P 2450 4400
F 0 "C1" H 2500 4640 50  0000 C CNN
F 1 "KCM55QR7YA226KH01L" H 2500 4549 50  0000 C CNN
F 2 "KCM55QR7YA226KH01L:CAPC6153X390N" H 2450 4400 50  0001 L BNN
F 3 "https://www.snapeda.com/parts/KCM55QR7YA226KH01L/Murata%20Electronics/view-part/1365129/?welcome=home&ref=search&t=KCM55QR7YA226KH01L#" H 2450 4400 50  0001 L BNN
	1    2450 4400
	0    -1   -1   0   
$EndComp
$Comp
L CGA3E2X7R1H104K080AA:CGA3E2X7R1H104K080AA C2
U 1 1 61326D86
P 3000 4400
F 0 "C2" H 3050 4640 50  0000 C CNN
F 1 "CGA3E2X7R1H104K080AA" H 3050 4549 50  0000 C CNN
F 2 "CGA3E2X7R1H104K080AA:CAPC1608X90N" H 3000 4400 50  0001 L BNN
F 3 "" H 3000 4400 50  0001 L BNN
	1    3000 4400
	0    -1   -1   0   
$EndComp
$Comp
L 12063D106MAT2A:12063D106MAT2A C4
U 1 1 613292F8
P 9600 4400
F 0 "C4" H 9650 4640 50  0000 C CNN
F 1 "12063D106MAT2A" H 9650 4549 50  0000 C CNN
F 2 "12063D106MAT2A:CAPC3216X178N" H 9600 4400 50  0001 L BNN
F 3 "" H 9600 4400 50  0001 L BNN
	1    9600 4400
	0    -1   -1   0   
$EndComp
$Comp
L CL31B104KBCNNNC:CL31B104KBCNNNC C3
U 1 1 6138E334
P 6400 3500
F 0 "C3" H 6450 3740 50  0000 C CNN
F 1 "CL31B104KBCNNNC" H 6450 3649 50  0000 C CNN
F 2 "CL31B104KBCNNNC:CAPC3216X180N" H 6400 3500 50  0001 L BNN
F 3 "" H 6400 3500 50  0001 L BNN
	1    6400 3500
	1    0    0    -1  
$EndComp
$Comp
L TPS563211DRLR:TPS563211DRLR U2
U 1 1 61393280
P 4300 3500
F 0 "U2" H 5050 3888 60  0000 C CNN
F 1 "TPS563211DRLR" H 5050 3782 60  0000 C CNN
F 2 "ul_TPS563211DRLR:TPS563211DRLR" H 4300 3440 60  0001 C CNN
F 3 "" H 4300 3500 60  0000 C CNN
	1    4300 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	1950 3500 2450 3500
Wire Wire Line
	2450 4200 2450 3500
Connection ~ 2450 3500
Wire Wire Line
	2450 3500 3000 3500
Wire Wire Line
	3000 4200 3000 3500
Connection ~ 3000 3500
Wire Wire Line
	3000 3500 4300 3500
$Comp
L power:GND #PWR0107
U 1 1 61401F04
P 3450 5050
F 0 "#PWR0107" H 3450 4800 50  0001 C CNN
F 1 "GND" H 3455 4877 50  0000 C CNN
F 2 "" H 3450 5050 50  0001 C CNN
F 3 "" H 3450 5050 50  0001 C CNN
	1    3450 5050
	1    0    0    -1  
$EndComp
Wire Wire Line
	3000 4500 3000 5000
Wire Wire Line
	3000 5000 3450 5000
Wire Wire Line
	3450 5000 3450 5050
Wire Wire Line
	2450 4500 2450 5000
Wire Wire Line
	2450 5000 3000 5000
Connection ~ 3000 5000
Wire Wire Line
	4300 4100 3450 4100
Wire Wire Line
	3450 4100 3450 5000
Connection ~ 3450 5000
Wire Wire Line
	4300 3900 4000 3900
Wire Wire Line
	4000 3900 4000 2850
Wire Wire Line
	4000 2850 4800 2850
$Comp
L RNCP1206FTD10K0:RNCP1206FTD10K0 R2
U 1 1 61403723
P 5200 2850
F 0 "R2" H 5200 3092 50  0000 C CNN
F 1 "RNCP1206FTD10K0" H 5200 3001 50  0000 C CNN
F 2 "RNCP1206FTD10K0:RESC3115X60N" H 5200 2850 50  0001 L BNN
F 3 "" H 5200 2850 50  0001 L BNN
	1    5200 2850
	1    0    0    -1  
$EndComp
Wire Wire Line
	5800 3500 6300 3500
Wire Wire Line
	5800 3700 6600 3700
Wire Wire Line
	6600 3700 6600 3500
$Comp
L 2021-09-13_22-06-51:SDR1307-4R7ML L1
U 1 1 6140681E
P 6700 3700
F 0 "L1" H 7000 3989 60  0000 C CNN
F 1 "SDR1307-4R7ML" H 7000 3883 60  0000 C CNN
F 2 "ul_SDR1307-4R7ML:SDR1307-4R7ML" H 6975 3415 60  0001 C CNN
F 3 "" H 6700 3700 60  0000 C CNN
	1    6700 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	6600 3700 6700 3700
Connection ~ 6600 3700
Wire Wire Line
	5600 2850 7900 2850
Wire Wire Line
	7900 2850 7900 3700
Wire Wire Line
	7900 3700 7300 3700
Wire Wire Line
	5800 4100 5800 5000
Wire Wire Line
	5800 5000 3450 5000
$Comp
L 2021-09-13_22-27-50:RC0603FR-0782KL R3
U 1 1 6140CEA8
P 8350 3750
F 0 "R3" V 8547 3829 60  0000 L CNN
F 1 "RC0603FR-0782KL" V 8653 3829 60  0000 L CNN
F 2 "ul_RC0603FR-0782KL:RC0603FR-0782KL" H 8600 3415 60  0001 C CNN
F 3 "" H 8350 3750 60  0000 C CNN
	1    8350 3750
	0    1    1    0   
$EndComp
Wire Wire Line
	7900 3700 8350 3700
Wire Wire Line
	8350 3700 8350 3750
Connection ~ 7900 3700
Wire Wire Line
	5800 3900 7950 3900
Wire Wire Line
	7950 3900 7950 4250
Wire Wire Line
	7950 4250 8350 4250
$Comp
L CRCW040210K0DHEDP:CRCW040210K0DHEDP R4
U 1 1 6140F8A3
P 8350 4800
F 0 "R4" V 8304 4905 50  0000 L CNN
F 1 "CRCW040210K0DHEDP" V 8395 4905 50  0000 L CNN
F 2 "CRCW040210K0DHEDP:RESC1005X40N" H 8350 4800 50  0001 L BNN
F 3 "" H 8350 4800 50  0001 L BNN
	1    8350 4800
	0    1    1    0   
$EndComp
Wire Wire Line
	8350 4250 8350 4400
Connection ~ 8350 4250
Wire Wire Line
	8350 5200 5800 5200
Wire Wire Line
	5800 5200 5800 5000
Connection ~ 5800 5000
Wire Wire Line
	8350 3700 9600 3700
Wire Wire Line
	9600 3700 9600 4200
Connection ~ 8350 3700
Wire Wire Line
	9600 4500 9600 5200
Wire Wire Line
	9600 5200 8350 5200
Connection ~ 8350 5200
Text HLabel 10200 3700 2    50   Output ~ 0
5V
Wire Wire Line
	9600 3700 10200 3700
Connection ~ 9600 3700
$EndSCHEMATC
