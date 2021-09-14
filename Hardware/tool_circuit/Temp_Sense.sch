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
Text HLabel 6800 3550 2    50   BiDi ~ 0
TEMP_DATA
Wire Bus Line
	6800 3550 6350 3550
Entry Wire Line
	6350 3850 6250 3750
Wire Wire Line
	6250 3750 5800 3750
Wire Wire Line
	5100 3150 5100 3450
$Comp
L power:+3.3V #PWR?
U 1 1 611F0935
P 5100 3150
F 0 "#PWR?" H 5100 3000 50  0001 C CNN
F 1 "+3.3V" H 5115 3323 50  0000 C CNN
F 2 "" H 5100 3150 50  0001 C CNN
F 3 "" H 5100 3150 50  0001 C CNN
	1    5100 3150
	1    0    0    -1  
$EndComp
$Comp
L Sensor:DHT11 U?
U 1 1 611EBA26
P 5100 3750
AR Path="/611EBA26" Ref="U?"  Part="1" 
AR Path="/611DBC89/611EBA26" Ref="U?"  Part="1" 
F 0 "U?" H 4856 3796 50  0000 R CNN
F 1 "DHT11" H 4856 3705 50  0000 R CNN
F 2 "Sensor:Aosong_DHT11_5.5x12.0_P2.54mm" H 5100 3350 50  0001 C CNN
F 3 "http://akizukidenshi.com/download/ds/aosong/DHT11.pdf" H 5250 4000 50  0001 C CNN
	1    5100 3750
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR?
U 1 1 6122E57C
P 5800 3150
F 0 "#PWR?" H 5800 3000 50  0001 C CNN
F 1 "+3.3V" H 5815 3323 50  0000 C CNN
F 2 "" H 5800 3150 50  0001 C CNN
F 3 "" H 5800 3150 50  0001 C CNN
	1    5800 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	5800 3150 5800 3250
Connection ~ 5800 3750
Wire Wire Line
	5800 3750 5400 3750
$Comp
L Device:R R?
U 1 1 612305FD
P 5800 3400
F 0 "R?" H 5870 3446 50  0000 L CNN
F 1 "5K" H 5870 3355 50  0000 L CNN
F 2 "" V 5730 3400 50  0001 C CNN
F 3 "~" H 5800 3400 50  0001 C CNN
	1    5800 3400
	1    0    0    -1  
$EndComp
Wire Wire Line
	5800 3550 5800 3750
$Comp
L power:GND #PWR?
U 1 1 61232568
P 5100 4050
F 0 "#PWR?" H 5100 3800 50  0001 C CNN
F 1 "GND" H 5105 3877 50  0000 C CNN
F 2 "" H 5100 4050 50  0001 C CNN
F 3 "" H 5100 4050 50  0001 C CNN
	1    5100 4050
	1    0    0    -1  
$EndComp
Wire Bus Line
	6350 3550 6350 4250
$EndSCHEMATC