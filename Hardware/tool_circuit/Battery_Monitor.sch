EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 5
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text HLabel 4600 3100 0    50   BiDi ~ 0
BATT_MON_DATA
$Comp
L Battery_Management:DS2745U U?
U 1 1 611EC761
P 7400 3450
AR Path="/611EC761" Ref="U?"  Part="1" 
AR Path="/611DF2F9/611EC761" Ref="U?"  Part="1" 
F 0 "U?" H 7400 3931 50  0000 C CNN
F 1 "DS2745U" H 7400 3840 50  0000 C CNN
F 2 "Package_SO:TSSOP-8_3x3mm_P0.65mm" H 7400 2950 50  0001 C CNN
F 3 "https://datasheets.maximintegrated.com/en/ds/DS2745.pdf" H 7500 3050 50  0001 C CNN
	1    7400 3450
	1    0    0    -1  
$EndComp
$Comp
L power:+BATT #PWR?
U 1 1 611ED520
P 8300 3050
F 0 "#PWR?" H 8300 2900 50  0001 C CNN
F 1 "+BATT" H 8315 3223 50  0000 C CNN
F 2 "" H 8300 3050 50  0001 C CNN
F 3 "" H 8300 3050 50  0001 C CNN
	1    8300 3050
	1    0    0    -1  
$EndComp
Wire Wire Line
	8300 3050 8300 3350
Wire Wire Line
	8300 3350 7800 3350
$EndSCHEMATC
