EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 8
Title "12V-5V Regulator"
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L power:+12V #PWR01
U 1 1 614E38F8
P 4050 3450
F 0 "#PWR01" H 4050 3300 50  0001 C CNN
F 1 "+12V" V 4150 3500 50  0000 C CNN
F 2 "" H 4050 3450 50  0001 C CNN
F 3 "" H 4050 3450 50  0001 C CNN
	1    4050 3450
	0    -1   -1   0   
$EndComp
$Comp
L power:+5V #PWR03
U 1 1 614E7ADA
P 7850 3350
F 0 "#PWR03" H 7850 3200 50  0001 C CNN
F 1 "+5V" V 7865 3478 50  0000 L CNN
F 2 "" H 7850 3350 50  0001 C CNN
F 3 "" H 7850 3350 50  0001 C CNN
	1    7850 3350
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR02
U 1 1 61401F04
P 5300 4100
F 0 "#PWR02" H 5300 3850 50  0001 C CNN
F 1 "GND" H 5305 3927 50  0000 C CNN
F 2 "" H 5300 4100 50  0001 C CNN
F 3 "" H 5300 4100 50  0001 C CNN
	1    5300 4100
	1    0    0    -1  
$EndComp
$Comp
L S2751-46R:S2751-46R TP1
U 1 1 6164D605
P 4400 3350
F 0 "TP1" H 4485 3417 50  0000 L CNN
F 1 "S2751-46R" H 4485 3326 50  0000 L CNN
F 2 "S2751-46R:HARWIN_S2751-46R" H 4400 3350 50  0001 L BNN
F 3 "" H 4400 3350 50  0001 L BNN
F 4 "HARWIN" H 4400 3350 50  0001 L BNN "MANUFACTURER"
F 5 "Manufacturer Recommendations" H 4400 3350 50  0001 L BNN "STANDARD"
F 6 "" H 4400 3350 50  0001 L BNN "PARTREV"
	1    4400 3350
	1    0    0    -1  
$EndComp
$Comp
L LM2576D2TR4-5G:LM2576D2TR4-5G U1
U 1 1 617DD1AF
P 5500 3450
F 0 "U1" H 5500 3917 50  0000 C CNN
F 1 "LM2576D2TR4-5G" H 5500 3826 50  0000 C CNN
F 2 "LM2576D2TR4-5G:D2PAK-5" H 5500 3450 50  0001 L BNN
F 3 "" H 5500 3450 50  0001 L BNN
	1    5500 3450
	1    0    0    -1  
$EndComp
Wire Wire Line
	5300 3950 5300 4050
Wire Wire Line
	5700 3950 5700 4050
$Comp
L 2021-10-30_20-57-30:URS1E102MHD1TO C2
U 1 1 617E34C7
P 7200 3550
F 0 "C2" V 7297 3654 60  0000 L CNN
F 1 "1000uF" V 7403 3654 60  0000 L CNN
F 2 "URS1E102MHD1TO:URS1E102MHD1TO" H 7350 3190 60  0001 C CNN
F 3 "" H 7200 3550 60  0000 C CNN
	1    7200 3550
	0    1    1    0   
$EndComp
Wire Wire Line
	7200 3850 7200 4050
Wire Wire Line
	7200 4050 6350 4050
Wire Wire Line
	5700 4050 5300 4050
Connection ~ 5700 4050
Connection ~ 5300 4050
Wire Wire Line
	5300 4050 5300 4100
Wire Wire Line
	6300 3350 7200 3350
Wire Wire Line
	7200 3350 7850 3350
Connection ~ 7200 3350
Wire Wire Line
	7200 3350 7200 3550
$Comp
L S2751-46R:S2751-46R TP2
U 1 1 6164FDC2
P 7200 3250
F 0 "TP2" H 7285 3317 50  0000 L CNN
F 1 "S2751-46R" H 7285 3226 50  0000 L CNN
F 2 "S2751-46R:HARWIN_S2751-46R" H 7200 3250 50  0001 L BNN
F 3 "" H 7200 3250 50  0001 L BNN
F 4 "HARWIN" H 7200 3250 50  0001 L BNN "MANUFACTURER"
F 5 "Manufacturer Recommendations" H 7200 3250 50  0001 L BNN "STANDARD"
F 6 "" H 7200 3250 50  0001 L BNN "PARTREV"
	1    7200 3250
	1    0    0    -1  
$EndComp
$Comp
L EEUFS1K101:EEUFS1K101 C1
U 1 1 617EC29C
P 4400 3750
F 0 "C1" V 4404 3880 50  0000 L CNN
F 1 "100uF" V 4495 3880 50  0000 L CNN
F 2 "EEUFS1K101:CAPPRD500W60D1000H1250" H 4400 3750 50  0001 L BNN
F 3 "" H 4400 3750 50  0001 L BNN
F 4 "28-FEB-20" H 4400 3750 50  0001 L BNN "PARTREV"
F 5 "0.6" H 4400 3750 50  0001 L BNN "b_nom"
F 6 "12.5" H 4400 3750 50  0001 L BNN "A_max"
F 7 "10" H 4400 3750 50  0001 L BNN "D_nom"
F 8 "0.65" H 4400 3750 50  0001 L BNN "b_max"
F 9 "5" H 4400 3750 50  0001 L BNN "e_nom"
F 10 "PANASONIC" H 4400 3750 50  0001 L BNN "MF"
F 11 "FS-A" H 4400 3750 50  0001 L BNN "DESCRIPTION"
	1    4400 3750
	0    1    1    0   
$EndComp
Wire Wire Line
	4400 3650 4400 3450
Connection ~ 4400 3450
Wire Wire Line
	4400 3450 4700 3450
Wire Wire Line
	4400 3950 4400 4050
Wire Wire Line
	4400 4050 5300 4050
$Comp
L 2021-10-30_21-05-21:IHLP4040DZER101M11 L1
U 1 1 617F1E2E
P 6400 3550
F 0 "L1" H 6700 3700 60  0000 C CNN
F 1 "100 uH" H 6650 3450 60  0000 C CNN
F 2 "IHLP-4040DZ_VIS:IHLP4040DZER101M11" H 6675 3265 60  0001 C CNN
F 3 "" H 6400 3550 60  0000 C CNN
	1    6400 3550
	1    0    0    -1  
$EndComp
Wire Wire Line
	6300 3550 6350 3550
Wire Wire Line
	7000 3550 7200 3550
Connection ~ 7200 3550
Wire Wire Line
	4050 3450 4400 3450
$Comp
L tool_circuit-rescue:B380-13-F-2021-10-30_21-29-43 CR1
U 1 1 6180A80C
P 6350 3950
AR Path="/6180A80C" Ref="CR1"  Part="1" 
AR Path="/611DBAE9/6131D12D/6180A80C" Ref="CR1"  Part="1" 
F 0 "CR1" V 6603 3846 60  0000 R CNN
F 1 "B380-13-F" V 6497 3846 60  0000 R CNN
F 2 "B380-13-F:B380-13-F" H 6550 3590 60  0001 C CNN
F 3 "" H 6350 3950 60  0000 C CNN
	1    6350 3950
	0    -1   -1   0   
$EndComp
Connection ~ 6350 3550
Wire Wire Line
	6350 3550 6400 3550
Wire Wire Line
	6350 3950 6350 4050
Connection ~ 6350 4050
Wire Wire Line
	6350 4050 5700 4050
$EndSCHEMATC
