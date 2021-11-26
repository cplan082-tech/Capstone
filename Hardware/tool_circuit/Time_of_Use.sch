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
$Comp
L power:GND #PWR06
U 1 1 61707039
P 5150 5400
F 0 "#PWR06" H 5150 5150 50  0001 C CNN
F 1 "GND" H 5155 5227 50  0000 C CNN
F 2 "" H 5150 5400 50  0001 C CNN
F 3 "" H 5150 5400 50  0001 C CNN
	1    5150 5400
	1    0    0    -1  
$EndComp
Wire Wire Line
	5150 4600 5650 4600
$Comp
L 2021-11-02_22-07-21:1825255-1 SW1
U 1 1 6186D287
P 5650 4300
F 0 "SW1" H 6450 4587 60  0000 C CNN
F 1 "Switch" H 6450 4481 60  0000 C CNN
F 2 "ul_1825255-1:1825255-1" H 6450 4440 60  0001 C CNN
F 3 "" H 5650 4300 60  0000 C CNN
	1    5650 4300
	1    0    0    -1  
$EndComp
Wire Wire Line
	6650 3500 5650 3500
Wire Wire Line
	5650 3500 5650 4300
Text GLabel 8350 3850 2    50   BiDi ~ 0
GPIO22_GEN3
$Comp
L power:+3.3V #PWR0101
U 1 1 619EFD57
P 6650 3500
F 0 "#PWR0101" H 6650 3350 50  0001 C CNN
F 1 "+3.3V" H 6665 3673 50  0000 C CNN
F 2 "" H 6650 3500 50  0001 C CNN
F 3 "" H 6650 3500 50  0001 C CNN
	1    6650 3500
	1    0    0    -1  
$EndComp
Wire Wire Line
	8350 3850 8350 4500
Wire Wire Line
	7250 4500 8350 4500
Wire Wire Line
	5150 4600 5150 5400
$EndSCHEMATC
