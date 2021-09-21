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
Text HLabel 5350 3100 0    50   BiDi ~ 0
GPIO_27
$Comp
L Connector:Conn_01x03_Female J1
U 1 1 6144B415
P 5550 3100
F 0 "J1" H 5578 3126 50  0000 L CNN
F 1 "Conn_01x03_Female" H 5578 3035 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5550 3100 50  0001 C CNN
F 3 "~" H 5550 3100 50  0001 C CNN
	1    5550 3100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0105
U 1 1 614A4174
P 5150 3200
F 0 "#PWR0105" H 5150 2950 50  0001 C CNN
F 1 "GND" H 5155 3027 50  0000 C CNN
F 2 "" H 5150 3200 50  0001 C CNN
F 3 "" H 5150 3200 50  0001 C CNN
	1    5150 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5350 3200 5150 3200
Wire Wire Line
	5100 2950 5100 3000
Wire Wire Line
	5100 3000 5350 3000
$Comp
L power:+5V #PWR0106
U 1 1 614A5231
P 5100 2950
F 0 "#PWR0106" H 5100 2800 50  0001 C CNN
F 1 "+5V" H 5115 3123 50  0000 C CNN
F 2 "" H 5100 2950 50  0001 C CNN
F 3 "" H 5100 2950 50  0001 C CNN
	1    5100 2950
	1    0    0    -1  
$EndComp
$EndSCHEMATC
