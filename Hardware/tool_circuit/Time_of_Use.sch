EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
Text HLabel 4650 3450 0    50   BiDi ~ 0
GPIO_27
Wire Wire Line
	4400 3300 4400 3350
Wire Wire Line
	4400 3350 4650 3350
$Comp
L power:+5V #PWR0106
U 1 1 614A5231
P 4400 3300
F 0 "#PWR0106" H 4400 3150 50  0001 C CNN
F 1 "+5V" H 4415 3473 50  0000 C CNN
F 2 "" H 4400 3300 50  0001 C CNN
F 3 "" H 4400 3300 50  0001 C CNN
	1    4400 3300
	1    0    0    -1  
$EndComp
Wire Wire Line
	4650 3550 4450 3550
$Comp
L Connector:Conn_01x03_Female J1
U 1 1 6144B415
P 4850 3450
F 0 "J1" H 4878 3476 50  0000 L CNN
F 1 "Conn_01x03_Female" H 4878 3385 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 4850 3450 50  0001 C CNN
F 3 "~" H 4850 3450 50  0001 C CNN
	1    4850 3450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 614A4174
P 4450 3550
F 0 "#PWR0105" H 4450 3300 50  0001 C CNN
F 1 "GND" H 4455 3377 50  0000 C CNN
F 2 "" H 4450 3550 50  0001 C CNN
F 3 "" H 4450 3550 50  0001 C CNN
	1    4450 3550
	1    0    0    -1  
$EndComp
$EndSCHEMATC
