EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 5 8
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Wire Wire Line
	6650 4000 6150 4000
$Comp
L 1825255-1:1825255-1 S1
U 1 1 61568B03
P 5800 4250
F 0 "S1" H 6030 4296 50  0000 L CNN
F 1 "1825255-1" H 6030 4205 50  0000 L CNN
F 2 "1825255-1:SW_1825255-1" H 5800 4250 50  0001 L BNN
F 3 "" H 5800 4250 50  0001 L BNN
F 4 "1825255-1" H 5800 4250 50  0001 L BNN "Comment"
	1    5800 4250
	1    0    0    -1  
$EndComp
Wire Wire Line
	6150 4000 6150 3850
Wire Wire Line
	6150 3850 5400 3850
Wire Wire Line
	5400 3850 5400 4050
Wire Wire Line
	6650 3500 6650 4000
$Comp
L power:GND #PWR06
U 1 1 61707039
P 4900 5050
F 0 "#PWR06" H 4900 4800 50  0001 C CNN
F 1 "GND" H 4905 4877 50  0000 C CNN
F 2 "" H 4900 5050 50  0001 C CNN
F 3 "" H 4900 5050 50  0001 C CNN
	1    4900 5050
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR07
U 1 1 6174D417
P 6650 3500
F 0 "#PWR07" H 6650 3350 50  0001 C CNN
F 1 "+3.3V" H 6665 3673 50  0000 C CNN
F 2 "" H 6650 3500 50  0001 C CNN
F 3 "" H 6650 3500 50  0001 C CNN
	1    6650 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	3950 4150 5400 4150
Wire Bus Line
	3850 3900 3850 4050
Text HLabel 3650 3900 0    50   BiDi ~ 0
TIME_OF_USE_DATA
Wire Bus Line
	3650 3900 3850 3900
Entry Wire Line
	3850 4050 3950 4150
Text Label 4150 4150 0    50   ~ 0
GPIO22
Wire Wire Line
	4900 4250 5400 4250
$Comp
L RNCP1206FTD10K0:RNCP1206FTD10K0 R1
U 1 1 617867AC
P 4900 4650
F 0 "R1" V 4854 4755 50  0000 L CNN
F 1 "10k" V 4945 4755 50  0000 L CNN
F 2 "RNCP1206FTD10K0:RESC3115X60N" H 4900 4650 50  0001 L BNN
F 3 "" H 4900 4650 50  0001 L BNN
	1    4900 4650
	0    1    1    0   
$EndComp
$EndSCHEMATC
