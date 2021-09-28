EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 7 8
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
Text HLabel 4700 4300 0    50   BiDi ~ 0
ACC_DATA
Entry Wire Line
	5550 4300 5650 4200
Entry Wire Line
	5450 4300 5550 4200
$Comp
L Connector:Conn_01x08_Female J3
U 1 1 6149E3EA
P 6200 3600
F 0 "J3" H 6228 3576 50  0000 L CNN
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
L power:+3.3V #PWR011
U 1 1 614A0E05
P 5300 3750
F 0 "#PWR011" H 5300 3600 50  0001 C CNN
F 1 "+3.3V" H 5315 3923 50  0000 C CNN
F 2 "" H 5300 3750 50  0001 C CNN
F 3 "" H 5300 3750 50  0001 C CNN
	1    5300 3750
	-1   0    0    1   
$EndComp
$Comp
L power:GND #PWR010
U 1 1 6149F537
P 5100 3750
F 0 "#PWR010" H 5100 3500 50  0001 C CNN
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
NoConn ~ 6000 3500
NoConn ~ 6000 3600
NoConn ~ 6000 3700
NoConn ~ 6000 3800
Wire Bus Line
	4700 4300 5550 4300
$EndSCHEMATC
