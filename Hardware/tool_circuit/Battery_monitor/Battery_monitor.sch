EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
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
L Battery_Management:DS2745U U?
U 1 1 613A08E6
P 4600 3300
F 0 "U?" H 4600 3781 50  0000 C CNN
F 1 "DS2745U" H 4600 3690 50  0000 C CNN
F 2 "Package_SO:TSSOP-8_3x3mm_P0.65mm" H 4600 2800 50  0001 C CNN
F 3 "https://datasheets.maximintegrated.com/en/ds/DS2745.pdf" H 4700 2900 50  0001 C CNN
	1    4600 3300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5000 3200 5300 3200
Text Label 5300 3200 0    50   ~ 0
VIN
Wire Wire Line
	5000 3300 5300 3300
Text Label 5300 3300 0    50   ~ 0
SNS
Wire Wire Line
	5000 3500 5350 3500
Text Label 5350 3500 0    50   ~ 0
CTG
Wire Wire Line
	4600 3700 4600 3950
Text Label 4600 3950 0    50   ~ 0
VSS
Wire Wire Line
	4200 3500 3850 3500
Text Label 3850 3500 0    50   ~ 0
SDA
Wire Wire Line
	4200 3400 4000 3400
Text Label 4000 3400 0    50   ~ 0
SCL
Wire Wire Line
	4200 3200 3950 3200
Text Label 3950 3200 0    50   ~ 0
PIO
Wire Wire Line
	4600 3000 4950 3000
Text Label 4950 3000 0    50   ~ 0
VDD
$EndSCHEMATC
