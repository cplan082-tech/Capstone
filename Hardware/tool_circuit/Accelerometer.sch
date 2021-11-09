EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 8 8
Title "Accelerometer "
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Conn_01x08_Female J3
U 1 1 6149E3EA
P 6200 3600
F 0 "J3" H 6228 3576 50  0000 L CNN
F 1 "Accel." H 6228 3485 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x08_P2.54mm_Vertical" H 6200 3600 50  0001 C CNN
F 3 "~" H 6200 3600 50  0001 C CNN
	1    6200 3600
	1    0    0    -1  
$EndComp
Wire Wire Line
	5300 3400 6000 3400
$Comp
L power:+3.3V #PWR010
U 1 1 614A0E05
P 5300 3750
F 0 "#PWR010" H 5300 3600 50  0001 C CNN
F 1 "+3.3V" H 5315 3923 50  0000 C CNN
F 2 "" H 5300 3750 50  0001 C CNN
F 3 "" H 5300 3750 50  0001 C CNN
	1    5300 3750
	-1   0    0    1   
$EndComp
Wire Wire Line
	5300 3400 5300 3750
NoConn ~ 6000 3500
NoConn ~ 6000 3600
NoConn ~ 6000 3700
NoConn ~ 6000 3800
$Comp
L power:GND #PWR011
U 1 1 617F6689
P 6000 3300
F 0 "#PWR011" H 6000 3050 50  0001 C CNN
F 1 "GND" V 6005 3172 50  0000 R CNN
F 2 "" H 6000 3300 50  0001 C CNN
F 3 "" H 6000 3300 50  0001 C CNN
	1    6000 3300
	0    1    1    0   
$EndComp
Text GLabel 6000 3900 0    50   BiDi ~ 0
GPIO2_SDA1
Text GLabel 6000 4000 0    50   BiDi ~ 0
GPIO3_SCL1
$EndSCHEMATC
