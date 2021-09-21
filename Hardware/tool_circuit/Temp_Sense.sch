EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 5 7
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Connector:Conn_01x03_Female J3
U 1 1 614AEC17
P 5700 3500
F 0 "J3" H 5728 3526 50  0000 L CNN
F 1 "Conn_01x03_Female" H 5728 3435 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x03_P2.54mm_Vertical" H 5700 3500 50  0001 C CNN
F 3 "~" H 5700 3500 50  0001 C CNN
	1    5700 3500
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR0102
U 1 1 614AF32D
P 5350 3700
F 0 "#PWR0102" H 5350 3450 50  0001 C CNN
F 1 "GND" H 5355 3527 50  0000 C CNN
F 2 "" H 5350 3700 50  0001 C CNN
F 3 "" H 5350 3700 50  0001 C CNN
	1    5350 3700
	1    0    0    -1  
$EndComp
Wire Wire Line
	5500 3600 5350 3600
Wire Wire Line
	5350 3600 5350 3700
$Comp
L power:+5V #PWR0103
U 1 1 614AFBC4
P 5050 3400
F 0 "#PWR0103" H 5050 3250 50  0001 C CNN
F 1 "+5V" H 5065 3573 50  0000 C CNN
F 2 "" H 5050 3400 50  0001 C CNN
F 3 "" H 5050 3400 50  0001 C CNN
	1    5050 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	5050 3400 5500 3400
Text HLabel 5500 3500 0    50   BiDi ~ 0
GPIO_17
$EndSCHEMATC
