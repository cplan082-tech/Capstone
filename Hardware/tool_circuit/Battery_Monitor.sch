EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text HLabel 5400 2600 0    50   BiDi ~ 0
BATT_MON_DATA
$Comp
L Battery_Management:DS2745U U?
U 1 1 611EC761
P 5850 3700
AR Path="/611EC761" Ref="U?"  Part="1" 
AR Path="/611DF2F9/611EC761" Ref="U?"  Part="1" 
F 0 "U?" H 5850 4181 50  0000 C CNN
F 1 "DS2745U" H 5850 4090 50  0000 C CNN
F 2 "Package_SO:TSSOP-8_3x3mm_P0.65mm" H 5850 3200 50  0001 C CNN
F 3 "https://datasheets.maximintegrated.com/en/ds/DS2745.pdf" H 5950 3300 50  0001 C CNN
	1    5850 3700
	1    0    0    -1  
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 611ED520
P 6750 3300
F 0 "#PWR?" H 6750 3150 50  0001 C CNN
F 1 "+BATT" H 6765 3473 50  0000 C CNN
F 2 "" H 6750 3300 50  0001 C CNN
F 3 "" H 6750 3300 50  0001 C CNN
	1    6750 3300
	1    0    0    -1  
$EndComp
Wire Wire Line
	6750 3300 6750 3600
Wire Wire Line
	6750 3600 6250 3600
$Comp
L power:GND #PWR?
U 1 1 612D54EC
P 6450 4000
F 0 "#PWR?" H 6450 3750 50  0001 C CNN
F 1 "GND" H 6455 3827 50  0000 C CNN
F 2 "" H 6450 4000 50  0001 C CNN
F 3 "" H 6450 4000 50  0001 C CNN
	1    6450 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	6250 3900 6450 3900
Wire Wire Line
	6450 3900 6450 4000
$EndSCHEMATC
