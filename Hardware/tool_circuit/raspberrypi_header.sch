EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 8 8
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
L Connector_Generic:Conn_02x20_Odd_Even J4
U 1 1 5C77771F
P 5250 2950
F 0 "J4" H 5300 4067 50  0000 C CNN
F 1 "GPIO_CONNECTOR" H 5300 3976 50  0000 C CNN
F 2 "lib:PinSocket_2x20_P2.54mm_Vertical_Centered_Anchor" H 5250 2950 50  0001 C CNN
F 3 "~" H 5250 2950 50  0001 C CNN
	1    5250 2950
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR014
U 1 1 5C777805
P 4850 4100
F 0 "#PWR014" H 4850 3850 50  0001 C CNN
F 1 "GND" H 4855 3927 50  0001 C CNN
F 2 "" H 4850 4100 50  0001 C CNN
F 3 "" H 4850 4100 50  0001 C CNN
	1    4850 4100
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR015
U 1 1 5C777838
P 5750 4100
F 0 "#PWR015" H 5750 3850 50  0001 C CNN
F 1 "GND" H 5755 3927 50  0001 C CNN
F 2 "" H 5750 4100 50  0001 C CNN
F 3 "" H 5750 4100 50  0001 C CNN
	1    5750 4100
	1    0    0    -1  
$EndComp
Wire Wire Line
	5050 2450 4850 2450
Wire Wire Line
	4850 2450 4850 3250
Wire Wire Line
	5050 3250 4850 3250
Connection ~ 4850 3250
Wire Wire Line
	4850 3250 4850 3950
Wire Wire Line
	5050 3950 4850 3950
Connection ~ 4850 3950
Wire Wire Line
	4850 3950 4850 4100
Wire Wire Line
	5550 2250 5750 2250
Wire Wire Line
	5750 2250 5750 2650
Wire Wire Line
	5550 2650 5750 2650
Connection ~ 5750 2650
Wire Wire Line
	5750 2650 5750 2950
Wire Wire Line
	5550 2950 5750 2950
Connection ~ 5750 2950
Wire Wire Line
	5550 3450 5750 3450
Wire Wire Line
	5750 2950 5750 3450
Connection ~ 5750 3450
Wire Wire Line
	5750 3450 5750 3650
Wire Wire Line
	5550 3650 5750 3650
Connection ~ 5750 3650
Wire Wire Line
	5750 3650 5750 4100
$Comp
L power:+3.3V #PWR013
U 1 1 5C777AB0
P 4800 1950
F 0 "#PWR013" H 4800 1800 50  0001 C CNN
F 1 "+3.3V" H 4815 2123 50  0000 C CNN
F 2 "" H 4800 1950 50  0001 C CNN
F 3 "" H 4800 1950 50  0001 C CNN
	1    4800 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	4800 2050 4800 1950
Wire Wire Line
	5050 2850 4800 2850
Wire Wire Line
	4800 2850 4800 2050
Connection ~ 4800 2050
$Comp
L power:+5V #PWR016
U 1 1 5C777E01
P 5850 1950
F 0 "#PWR016" H 5850 1800 50  0001 C CNN
F 1 "+5V" H 5865 2123 50  0000 C CNN
F 2 "" H 5850 1950 50  0001 C CNN
F 3 "" H 5850 1950 50  0001 C CNN
	1    5850 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	5550 2050 5850 2050
Wire Wire Line
	5850 2050 5850 1950
Wire Wire Line
	5550 2150 5850 2150
Wire Wire Line
	5850 2150 5850 2050
Connection ~ 5850 2050
$Comp
L power:GND #PWR012
U 1 1 5C778504
P 4450 4200
F 0 "#PWR012" H 4450 3950 50  0001 C CNN
F 1 "GND" H 4455 4027 50  0001 C CNN
F 2 "" H 4450 4200 50  0001 C CNN
F 3 "" H 4450 4200 50  0001 C CNN
	1    4450 4200
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG02
U 1 1 5C778511
P 4450 4150
F 0 "#FLG02" H 4450 4225 50  0001 C CNN
F 1 "PWR_FLAG" H 4450 4324 50  0000 C CNN
F 2 "" H 4450 4150 50  0001 C CNN
F 3 "~" H 4450 4150 50  0001 C CNN
	1    4450 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	4450 4150 4450 4200
Text Notes 7100 1100 0    50   ~ 10
If back powering Pi with 5V \nNOTE that the Raspberry Pi 3B+ and Pi Zero \nand ZeroW do not include an input ZVD.
Wire Notes Line
	7050 800  7050 1150
Wire Notes Line
	7050 1150 8900 1150
Wire Notes Line
	8900 1150 8900 800 
Wire Notes Line
	8900 800  7050 800 
Wire Wire Line
	4800 2050 4950 2050
Text Label 4100 2350 0    50   ~ 0
GPIO4_GPIO_GCLK
Text Label 4100 2950 0    50   ~ 0
GPIO10_SPI_MOSI
Wire Wire Line
	4000 2950 5050 2950
Wire Wire Line
	4000 3050 5050 3050
Wire Wire Line
	4000 3150 5050 3150
Wire Wire Line
	4000 3350 5050 3350
Wire Wire Line
	4000 3450 5050 3450
Wire Wire Line
	4000 3550 5050 3550
Wire Wire Line
	4000 3650 5050 3650
Wire Wire Line
	4000 3750 5050 3750
Wire Wire Line
	4000 3850 5050 3850
Wire Wire Line
	4000 2350 5050 2350
Text Label 4100 3050 0    50   ~ 0
GPIO9_SPI_MISO
Text Label 4100 3150 0    50   ~ 0
GPIO11_SPI_SCLK
Text Label 4100 3350 0    50   ~ 0
ID_SD
Text Label 4100 3450 0    50   ~ 0
GPIO5
Text Label 4100 3550 0    50   ~ 0
GPIO6
Text Label 4100 3650 0    50   ~ 0
GPIO13
Text Label 4100 3750 0    50   ~ 0
GPIO19
Text Label 4100 3850 0    50   ~ 0
GPIO26
NoConn ~ 4000 2350
NoConn ~ 4000 2950
NoConn ~ 4000 3050
NoConn ~ 4000 3150
NoConn ~ 4000 3350
NoConn ~ 4000 3450
NoConn ~ 4000 3550
NoConn ~ 4000 3650
NoConn ~ 4000 3750
NoConn ~ 4000 3850
Text Label 5900 2350 0    50   ~ 0
GPIO14_TXD0
Text Label 5900 2450 0    50   ~ 0
GPIO15_RXD0
Text Label 5900 2550 0    50   ~ 0
GPIO18_GEN1
Text Label 5900 2750 0    50   ~ 0
GPIO23_GEN4
Text Label 5900 2850 0    50   ~ 0
GPIO24_GEN5
Text Label 5900 3050 0    50   ~ 0
GPIO25_GEN6
Text Label 5900 3150 0    50   ~ 0
GPIO8_SPI_CE0_N
Text Label 5900 3250 0    50   ~ 0
GPIO7_SPI_CE1_N
Wire Wire Line
	5550 3150 6600 3150
Wire Wire Line
	5550 3250 6600 3250
Text Label 5900 3350 0    50   ~ 0
ID_SC
Text Label 5900 3550 0    50   ~ 0
GPIO12
Text Label 5900 3750 0    50   ~ 0
GPIO16
Text Label 5900 3850 0    50   ~ 0
GPIO20
Text Label 5900 3950 0    50   ~ 0
GPIO21
Wire Wire Line
	5550 2350 6600 2350
Wire Wire Line
	5550 2450 6600 2450
Wire Wire Line
	5550 2550 6600 2550
Wire Wire Line
	5550 3350 6600 3350
Wire Wire Line
	5550 3550 6600 3550
Wire Wire Line
	5550 3750 6600 3750
Wire Wire Line
	5550 3850 6600 3850
NoConn ~ 6600 2350
NoConn ~ 6600 2450
NoConn ~ 6600 2550
NoConn ~ 6600 3150
NoConn ~ 6600 3250
NoConn ~ 6600 3350
NoConn ~ 6600 3550
NoConn ~ 6600 3750
NoConn ~ 6600 3850
NoConn ~ 6600 3950
Wire Wire Line
	5550 3950 6600 3950
$Comp
L Mechanical:MountingHole H1
U 1 1 5C7C4C81
P 8850 2500
F 0 "H1" H 8950 2546 50  0000 L CNN
F 1 "MountingHole" H 8950 2455 50  0000 L CNN
F 2 "lib:MountingHole_2.7mm_M2.5_uHAT_RPi" H 8850 2500 50  0001 C CNN
F 3 "~" H 8850 2500 50  0001 C CNN
	1    8850 2500
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H2
U 1 1 5C7C7FBC
P 8850 2700
F 0 "H2" H 8950 2746 50  0000 L CNN
F 1 "MountingHole" H 8950 2655 50  0000 L CNN
F 2 "lib:MountingHole_2.7mm_M2.5_uHAT_RPi" H 8850 2700 50  0001 C CNN
F 3 "~" H 8850 2700 50  0001 C CNN
	1    8850 2700
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H3
U 1 1 5C7C8014
P 8850 2900
F 0 "H3" H 8950 2946 50  0000 L CNN
F 1 "MountingHole" H 8950 2855 50  0000 L CNN
F 2 "lib:MountingHole_2.7mm_M2.5_uHAT_RPi" H 8850 2900 50  0001 C CNN
F 3 "~" H 8850 2900 50  0001 C CNN
	1    8850 2900
	1    0    0    -1  
$EndComp
$Comp
L Mechanical:MountingHole H4
U 1 1 5C7C8030
P 8850 3100
F 0 "H4" H 8950 3146 50  0000 L CNN
F 1 "MountingHole" H 8950 3055 50  0000 L CNN
F 2 "lib:MountingHole_2.7mm_M2.5_uHAT_RPi" H 8850 3100 50  0001 C CNN
F 3 "~" H 8850 3100 50  0001 C CNN
	1    8850 3100
	1    0    0    -1  
$EndComp
Wire Bus Line
	2350 1950 3050 1950
Entry Wire Line
	3050 2050 3150 2150
Entry Wire Line
	3050 2150 3150 2250
Entry Wire Line
	3050 2450 3150 2550
Entry Wire Line
	3050 2550 3150 2650
Wire Wire Line
	3150 2150 5050 2150
Wire Wire Line
	3150 2250 5050 2250
Wire Wire Line
	3150 2550 5050 2550
Wire Wire Line
	3150 2650 5050 2650
Text Label 3250 2150 0    50   ~ 0
GPIO2
Text Label 3250 2250 0    50   ~ 0
GPIO3
Text Label 3300 2650 0    50   ~ 0
GPIO27
Text Label 3300 2550 0    50   ~ 0
GPIO17
$Comp
L WP7113YD:WP7113YD D2
U 1 1 61534E0C
P 8100 3200
F 0 "D2" V 8196 3121 50  0000 R CNN
F 1 "WP7113YD" V 8105 3121 50  0000 R CNN
F 2 "LED_WP7113YD" H 8100 3200 50  0001 L BNN
F 3 "" H 8100 3200 50  0001 L BNN
F 4 "Kingbright" H 8100 3200 50  0001 L BNN "MANUFACTURER"
	1    8100 3200
	0    -1   -1   0   
$EndComp
Wire Wire Line
	8100 2750 8100 2800
$Comp
L power:GND #PWR0103
U 1 1 61539C99
P 7100 4450
F 0 "#PWR0103" H 7100 4200 50  0001 C CNN
F 1 "GND" H 7105 4277 50  0000 C CNN
F 2 "" H 7100 4450 50  0001 C CNN
F 3 "" H 7100 4450 50  0001 C CNN
	1    7100 4450
	1    0    0    -1  
$EndComp
Wire Wire Line
	5550 2750 7450 2750
Text Label 7550 2750 0    50   ~ 0
Data_Transfer
Wire Wire Line
	7450 2850 7450 2950
Wire Wire Line
	5550 2850 7300 2850
$Comp
L power:GND #PWR0104
U 1 1 6155009E
P 7450 4150
F 0 "#PWR0104" H 7450 3900 50  0001 C CNN
F 1 "GND" H 7455 3977 50  0000 C CNN
F 2 "" H 7450 4150 50  0001 C CNN
F 3 "" H 7450 4150 50  0001 C CNN
	1    7450 4150
	1    0    0    -1  
$EndComp
Text Label 6850 2850 0    50   ~ 0
Enable_LED
$Comp
L 2021-09-28_17-40-03:SLI-343M8C3F R11
U 1 1 61576EA3
P 7900 2000
F 0 "R11" H 8100 2388 60  0000 C CNN
F 1 "SLI-343M8C3F" H 8100 2282 60  0000 C CNN
F 2 "LED_SLI-343D_ROM" H 8100 1640 60  0001 C CNN
F 3 "" H 7900 2000 60  0000 C CNN
	1    7900 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	5850 2150 7000 2150
Wire Wire Line
	7000 2150 7000 2000
Connection ~ 5850 2150
Text Label 6700 2150 0    50   ~ 0
5V_LED
Connection ~ 4800 2850
$Comp
L power:GND #PWR0105
U 1 1 6157F3DC
P 8300 2000
F 0 "#PWR0105" H 8300 1750 50  0001 C CNN
F 1 "GND" V 8305 1872 50  0000 R CNN
F 2 "" H 8300 2000 50  0001 C CNN
F 3 "" H 8300 2000 50  0001 C CNN
	1    8300 2000
	0    -1   -1   0   
$EndComp
$Comp
L 2021-09-28_17-40-03:SLI-343M8C3F R9
U 1 1 615803BB
P 3300 3050
F 0 "R9" V 3447 3278 60  0000 L CNN
F 1 "SLI-343M8C3F" V 3553 3278 60  0000 L CNN
F 2 "LED_SLI-343D_ROM" H 3500 2690 60  0001 C CNN
F 3 "" H 3300 3050 60  0000 C CNN
	1    3300 3050
	0    1    1    0   
$EndComp
Wire Wire Line
	3300 2850 3600 2850
$Comp
L power:GND #PWR0106
U 1 1 61585D7E
P 3300 4250
F 0 "#PWR0106" H 3300 4000 50  0001 C CNN
F 1 "GND" H 3305 4077 50  0000 C CNN
F 2 "" H 3300 4250 50  0001 C CNN
F 3 "" H 3300 4250 50  0001 C CNN
	1    3300 4250
	1    0    0    -1  
$EndComp
Text Label 3400 2850 0    50   ~ 0
3.3V_LED
Wire Wire Line
	7000 2000 7100 2000
Text Label 2850 2750 0    50   ~ 0
Tool_In_Use
Text HLabel 2350 1950 0    50   BiDi ~ 0
PI_CONN
Text Label 4100 2150 0    50   ~ 0
GPIO2_SDA1
Text Label 4100 2250 0    50   ~ 0
GPIO3_SCL1
Text Label 4100 2550 0    50   ~ 0
GPIO17_GEN0
Text Label 4100 2750 0    50   ~ 0
GPIO22_GEN3
Text Label 4100 2650 0    50   ~ 0
GPIO27_GEN2
$Comp
L 2021-09-28_17-40-03:SLI-343M8C3F R?
U 1 1 6161302E
P 7450 2950
F 0 "R?" H 7650 3338 60  0000 C CNN
F 1 "SLI-343M8C3F" H 7650 3232 60  0000 C CNN
F 2 "LED_SLI-343D_ROM" H 7650 2590 60  0001 C CNN
F 3 "" H 7450 2950 60  0000 C CNN
	1    7450 2950
	0    1    1    0   
$EndComp
$Comp
L WL-TMRC:WL-TMRC D?
U 1 1 6161A01D
P 7100 3450
F 0 "D?" V 7168 3311 50  0000 R CNN
F 1 "WL-TMRC" V 7077 3311 50  0000 R CNN
F 2 "" H 7100 3450 50  0001 C CNN
F 3 "" H 7100 3450 50  0001 L BNN
F 4 "http://www.we-online.de" H 7100 3450 50  0001 L BNN "COMPANY-URL"
F 5 "APR 2013" H 7100 3450 50  0001 L BNN "CREATED-DATE"
F 6 "http://katalog.we-online.de/en/led/WL-TMRC?m=t&sq=tmrc&sp=&sp=http%3A%2F%2Fwww.we-online.de%2Fweb%2Fen%2Felectronic_components%2Fsearchpage_PBS.php%3Fsearch%3Dtmrc" H 7100 3450 50  0001 L BNN "DATASHEET-URL"
F 7 "Würth Elektronik eiSos GmbH" H 7100 3450 50  0001 L BNN "MANUFACTURER"
F 8 "Christin Otto" H 7100 3450 50  0001 L BNN "CREATED-BY"
	1    7100 3450
	0    -1   -1   0   
$EndComp
Wire Wire Line
	7100 3050 7100 3250
Wire Wire Line
	5550 3050 6900 3050
$Comp
L RNCP1206FTD100R:RNCP1206FTD100R R?
U 1 1 61624927
P 7100 4050
F 0 "R?" V 7054 4155 50  0000 L CNN
F 1 "100" V 7145 4155 50  0000 L CNN
F 2 "RESC3115X60N" H 7100 4050 50  0001 L BNN
F 3 "" H 7100 4050 50  0001 L BNN
	1    7100 4050
	0    1    1    0   
$EndComp
$Comp
L RNCP1206FTD100R:RNCP1206FTD100R R?
U 1 1 616261C1
P 7450 3750
F 0 "R?" V 7404 3855 50  0000 L CNN
F 1 "100" V 7495 3855 50  0000 L CNN
F 2 "RESC3115X60N" H 7450 3750 50  0001 L BNN
F 3 "" H 7450 3750 50  0001 L BNN
	1    7450 3750
	0    1    1    0   
$EndComp
$Comp
L RNCP1206FTD100R:RNCP1206FTD100R R?
U 1 1 61626B9B
P 3300 3850
F 0 "R?" V 3254 3955 50  0000 L CNN
F 1 "100" V 3345 3955 50  0000 L CNN
F 2 "RESC3115X60N" H 3300 3850 50  0001 L BNN
F 3 "" H 3300 3850 50  0001 L BNN
	1    3300 3850
	0    1    1    0   
$EndComp
Text Label 6500 3050 0    50   ~ 0
Disable_LED
$Comp
L 2021-09-28_17-07-40:151034BS03000 LED?
U 1 1 61630B5E
P 2050 3300
AR Path="/611DF2F9/61630B5E" Ref="LED?"  Part="1" 
AR Path="/61514F71/61630B5E" Ref="LED?"  Part="1" 
F 0 "LED?" V 2197 3528 60  0000 L CNN
F 1 "151034BS03000" V 2303 3528 60  0000 L CNN
F 2 "LED_BS03000_WRE" H 2250 2940 60  0001 C CNN
F 3 "" H 2050 3300 60  0000 C CNN
	1    2050 3300
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 61630B6B
P 2050 4500
AR Path="/611DF2F9/61630B6B" Ref="#PWR?"  Part="1" 
AR Path="/61514F71/61630B6B" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 2050 4250 50  0001 C CNN
F 1 "GND" H 2055 4327 50  0000 C CNN
F 2 "" H 2050 4500 50  0001 C CNN
F 3 "" H 2050 4500 50  0001 C CNN
	1    2050 4500
	1    0    0    -1  
$EndComp
Wire Wire Line
	2050 2750 2050 3300
Wire Wire Line
	2050 2750 2350 2750
$Comp
L S2751-46R:S2751-46R TP?
U 1 1 61650FDF
P 4950 1950
F 0 "TP?" H 5035 2017 50  0000 L CNN
F 1 "S2751-46R" H 5035 1926 50  0000 L CNN
F 2 "HARWIN_S2751-46R" H 4950 1950 50  0001 L BNN
F 3 "" H 4950 1950 50  0001 L BNN
F 4 "HARWIN" H 4950 1950 50  0001 L BNN "MANUFACTURER"
F 5 "Manufacturer Recommendations" H 4950 1950 50  0001 L BNN "STANDARD"
F 6 "" H 4950 1950 50  0001 L BNN "PARTREV"
	1    4950 1950
	1    0    0    -1  
$EndComp
Connection ~ 4950 2050
Wire Wire Line
	4950 2050 5050 2050
$Comp
L S2751-46R:S2751-46R TP?
U 1 1 61651CC8
P 7450 2650
F 0 "TP?" H 7535 2717 50  0000 L CNN
F 1 "S2751-46R" H 7535 2626 50  0000 L CNN
F 2 "HARWIN_S2751-46R" H 7450 2650 50  0001 L BNN
F 3 "" H 7450 2650 50  0001 L BNN
F 4 "HARWIN" H 7450 2650 50  0001 L BNN "MANUFACTURER"
F 5 "Manufacturer Recommendations" H 7450 2650 50  0001 L BNN "STANDARD"
F 6 "" H 7450 2650 50  0001 L BNN "PARTREV"
	1    7450 2650
	1    0    0    -1  
$EndComp
Connection ~ 7450 2750
Wire Wire Line
	7450 2750 8100 2750
$Comp
L S2751-46R:S2751-46R TP?
U 1 1 6165274B
P 7300 2950
F 0 "TP?" H 7215 2924 50  0000 R CNN
F 1 "S2751-46R" H 7215 3015 50  0000 R CNN
F 2 "HARWIN_S2751-46R" H 7300 2950 50  0001 L BNN
F 3 "" H 7300 2950 50  0001 L BNN
F 4 "HARWIN" H 7300 2950 50  0001 L BNN "MANUFACTURER"
F 5 "Manufacturer Recommendations" H 7300 2950 50  0001 L BNN "STANDARD"
F 6 "" H 7300 2950 50  0001 L BNN "PARTREV"
	1    7300 2950
	-1   0    0    1   
$EndComp
Connection ~ 7300 2850
Wire Wire Line
	7300 2850 7450 2850
$Comp
L S2751-46R:S2751-46R TP?
U 1 1 61653544
P 6900 3150
F 0 "TP?" H 6815 3124 50  0000 R CNN
F 1 "S2751-46R" H 6815 3215 50  0000 R CNN
F 2 "HARWIN_S2751-46R" H 6900 3150 50  0001 L BNN
F 3 "" H 6900 3150 50  0001 L BNN
F 4 "HARWIN" H 6900 3150 50  0001 L BNN "MANUFACTURER"
F 5 "Manufacturer Recommendations" H 6900 3150 50  0001 L BNN "STANDARD"
F 6 "" H 6900 3150 50  0001 L BNN "PARTREV"
	1    6900 3150
	-1   0    0    1   
$EndComp
Connection ~ 6900 3050
Wire Wire Line
	6900 3050 7100 3050
$Comp
L S2751-46R:S2751-46R TP?
U 1 1 61653BD5
P 3600 2950
F 0 "TP?" H 3515 2924 50  0000 R CNN
F 1 "S2751-46R" H 3515 3015 50  0000 R CNN
F 2 "HARWIN_S2751-46R" H 3600 2950 50  0001 L BNN
F 3 "" H 3600 2950 50  0001 L BNN
F 4 "HARWIN" H 3600 2950 50  0001 L BNN "MANUFACTURER"
F 5 "Manufacturer Recommendations" H 3600 2950 50  0001 L BNN "STANDARD"
F 6 "" H 3600 2950 50  0001 L BNN "PARTREV"
	1    3600 2950
	-1   0    0    1   
$EndComp
Connection ~ 3600 2850
Wire Wire Line
	3600 2850 4800 2850
$Comp
L S2751-46R:S2751-46R TP?
U 1 1 61654750
P 2350 2850
F 0 "TP?" H 2265 2824 50  0000 R CNN
F 1 "S2751-46R" H 2265 2915 50  0000 R CNN
F 2 "HARWIN_S2751-46R" H 2350 2850 50  0001 L BNN
F 3 "" H 2350 2850 50  0001 L BNN
F 4 "HARWIN" H 2350 2850 50  0001 L BNN "MANUFACTURER"
F 5 "Manufacturer Recommendations" H 2350 2850 50  0001 L BNN "STANDARD"
F 6 "" H 2350 2850 50  0001 L BNN "PARTREV"
	1    2350 2850
	-1   0    0    1   
$EndComp
Connection ~ 2350 2750
Wire Wire Line
	2350 2750 5050 2750
$Comp
L AC1206FR-07130RL:AC1206FR-07130RL R?
U 1 1 61659CB7
P 8100 3900
F 0 "R?" V 8054 4005 50  0000 L CNN
F 1 "130" V 8145 4005 50  0000 L CNN
F 2 "RESC3116X65N" H 8100 3900 50  0001 L BNN
F 3 "" H 8100 3900 50  0001 L BNN
	1    8100 3900
	0    1    1    0   
$EndComp
$Comp
L power:GND #PWR?
U 1 1 6165AE6F
P 8100 4300
F 0 "#PWR?" H 8100 4050 50  0001 C CNN
F 1 "GND" H 8105 4127 50  0000 C CNN
F 2 "" H 8100 4300 50  0001 C CNN
F 3 "" H 8100 4300 50  0001 C CNN
	1    8100 4300
	1    0    0    -1  
$EndComp
$Comp
L RC1206FR-0742R2L:RC1206FR-0742R2L R?
U 1 1 6165D04D
P 2050 4100
F 0 "R?" V 2004 4205 50  0000 L CNN
F 1 "42.2" V 2095 4205 50  0000 L CNN
F 2 "RESC3116X65N" H 2050 4100 50  0001 L BNN
F 3 "" H 2050 4100 50  0001 L BNN
	1    2050 4100
	0    1    1    0   
$EndComp
Wire Wire Line
	3300 2850 3300 3050
$Comp
L RMCF1206JT220R:RMCF1206JT220R R?
U 1 1 61665485
P 7500 2000
F 0 "R?" H 7500 2242 50  0000 C CNN
F 1 "220" H 7500 2151 50  0000 C CNN
F 2 "RESC3216X70N" H 7500 2000 50  0001 L BNN
F 3 "" H 7500 2000 50  0001 L BNN
	1    7500 2000
	1    0    0    -1  
$EndComp
Wire Bus Line
	3050 1950 3050 2550
$EndSCHEMATC
