EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 6 8
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
	5550 4200 5550 3900
Wire Wire Line
	5650 4200 5650 4000
Text Label 5550 3900 0    50   ~ 0
GPIO2
Text Label 5650 4000 0    50   ~ 0
GPIO3
Text Label 4750 4300 0    50   ~ 0
GPIO[2..3]
Text HLabel 4700 4300 0    50   Input ~ 0
ACC_DATA
Entry Wire Line
	5550 4300 5650 4200
Entry Wire Line
	5450 4300 5550 4200
$Comp
L Connector:Conn_01x08_Female J1
U 1 1 6149E3EA
P 6200 3600
F 0 "J1" H 6228 3576 50  0000 L CNN
F 1 "Conn_01x08_Female" H 6228 3485 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x08_P2.54mm_Vertical" H 6200 3600 50  0001 C CNN
F 3 "~" H 6200 3600 50  0001 C CNN
	1    6200 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	5650 4000 6000 4000
Wire Wire Line
	5550 3900 6000 3900
Wire Wire Line
	5300 3400 6000 3400
Wire Wire Line
	5100 3300 6000 3300
$Comp
L power:+3.3V #PWR07
U 1 1 614A0E05
P 5300 3750
F 0 "#PWR07" H 5300 3600 50  0001 C CNN
F 1 "+3.3V" H 5315 3923 50  0000 C CNN
F 2 "" H 5300 3750 50  0001 C CNN
F 3 "" H 5300 3750 50  0001 C CNN
	1    5300 3750
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR06
U 1 1 6149F537
P 5100 3750
F 0 "#PWR06" H 5100 3500 50  0001 C CNN
F 1 "GND" H 5105 3577 50  0000 C CNN
F 2 "" H 5100 3750 50  0001 C CNN
F 3 "" H 5100 3750 50  0001 C CNN
	1    5100 3750
	1    0    0    -1  
$EndComp
Wire Wire Line
	5100 3300 5100 3750
Wire Wire Line
	5300 3400 5300 3750
Wire Bus Line
	4700 4300 5550 4300
$EndSCHEMATC
