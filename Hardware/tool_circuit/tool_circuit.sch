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
L Analog:AD630ARZ U?
U 1 1 60E65657
P 4900 2850
F 0 "U?" H 4900 3831 50  0000 C CNN
F 1 "AD630ARZ" H 4900 3740 50  0000 C CNN
F 2 "Package_SO:SOIC-20W_7.5x12.8mm_P1.27mm" H 4900 1800 50  0001 C CNN
F 3 "https://www.analog.com/media/en/technical-documentation/data-sheets/ad630.pdf" H 4500 3950 50  0001 C CNN
	1    4900 2850
	1    0    0    -1  
$EndComp
$Comp
L dk_Encoders:PEC11R-4215F-S0024 S?
U 1 1 60E6847B
P 2650 2550
F 0 "S?" H 2600 2922 60  0000 C CNN
F 1 "PEC11R-4215F-S0024" H 2600 2816 60  0000 C CNN
F 2 "digikey-footprints:Rotary_Encoder_Switched_PEC11R" H 2850 2750 60  0001 L CNN
F 3 "https://www.bourns.com/docs/Product-Datasheets/PEC11R.pdf" H 2850 2850 60  0001 L CNN
F 4 "PEC11R-4215F-S0024-ND" H 2850 2950 60  0001 L CNN "Digi-Key_PN"
F 5 "PEC11R-4215F-S0024" H 2850 3050 60  0001 L CNN "MPN"
F 6 "Sensors, Transducers" H 2850 3150 60  0001 L CNN "Category"
F 7 "Encoders" H 2850 3250 60  0001 L CNN "Family"
F 8 "https://www.bourns.com/docs/Product-Datasheets/PEC11R.pdf" H 2850 3350 60  0001 L CNN "DK_Datasheet_Link"
F 9 "/product-detail/en/bourns-inc/PEC11R-4215F-S0024/PEC11R-4215F-S0024-ND/4499665" H 2850 3450 60  0001 L CNN "DK_Detail_Page"
F 10 "ROTARY ENCODER MECHANICAL 24PPR" H 2850 3550 60  0001 L CNN "Description"
F 11 "Bourns Inc." H 2850 3650 60  0001 L CNN "Manufacturer"
F 12 "Active" H 2850 3750 60  0001 L CNN "Status"
	1    2650 2550
	1    0    0    -1  
$EndComp
$Comp
L dk_Interface-I-O-Expanders:MCP23017-E_SO U?
U 1 1 60E6A211
P 8050 3250
F 0 "U?" H 8150 4253 60  0000 C CNN
F 1 "MCP23017-E_SO" H 8150 4147 60  0000 C CNN
F 2 "digikey-footprints:SOIC-28_W7.5mm" H 8250 3450 60  0001 L CNN
F 3 "http://www.microchip.com/mymicrochip/filehandler.aspx?ddocname=en023709" H 8250 3550 60  0001 L CNN
F 4 "MCP23017-E/SO-ND" H 8250 3650 60  0001 L CNN "Digi-Key_PN"
F 5 "MCP23017-E/SO" H 8250 3750 60  0001 L CNN "MPN"
F 6 "Integrated Circuits (ICs)" H 8250 3850 60  0001 L CNN "Category"
F 7 "Interface - I/O Expanders" H 8250 3950 60  0001 L CNN "Family"
F 8 "http://www.microchip.com/mymicrochip/filehandler.aspx?ddocname=en023709" H 8250 4050 60  0001 L CNN "DK_Datasheet_Link"
F 9 "/product-detail/en/microchip-technology/MCP23017-E-SO/MCP23017-E-SO-ND/894271" H 8250 4150 60  0001 L CNN "DK_Detail_Page"
F 10 "IC I/O EXPANDER I2C 16B 28SOIC" H 8250 4250 60  0001 L CNN "Description"
F 11 "Microchip Technology" H 8250 4350 60  0001 L CNN "Manufacturer"
F 12 "Active" H 8250 4450 60  0001 L CNN "Status"
	1    8050 3250
	1    0    0    -1  
$EndComp
$Comp
L dk_Balun:ETC1-1-13TR T?
U 1 1 60EA3E8C
P 3200 4900
F 0 "T?" H 3200 5287 60  0000 C CNN
F 1 "ETC1-1-13TR" H 3200 5181 60  0000 C CNN
F 2 "digikey-footprints:SMD-5-6_R_3.83x2.79mm" H 3400 5100 60  0001 L CNN
F 3 "http://cdn.macom.com/datasheets/ETC1-1-13.pdf" H 3400 5200 60  0001 L CNN
F 4 "1465-1217-1-ND" H 3400 5300 60  0001 L CNN "Digi-Key_PN"
F 5 "ETC1-1-13TR" H 3400 5400 60  0001 L CNN "MPN"
F 6 "RF/IF and RFID" H 3400 5500 60  0001 L CNN "Category"
F 7 "Balun" H 3400 5600 60  0001 L CNN "Family"
F 8 "http://cdn.macom.com/datasheets/ETC1-1-13.pdf" H 3400 5700 60  0001 L CNN "DK_Datasheet_Link"
F 9 "/product-detail/en/m-a-com-technology-solutions/ETC1-1-13TR/1465-1217-1-ND/4429914" H 3400 5800 60  0001 L CNN "DK_Detail_Page"
F 10 "BALUN 4.5MHZ-3GHZ 1:1 5SMD" H 3400 5900 60  0001 L CNN "Description"
F 11 "M/A-Com Technology Solutions" H 3400 6000 60  0001 L CNN "Manufacturer"
F 12 "Active" H 3400 6100 60  0001 L CNN "Status"
	1    3200 4900
	1    0    0    -1  
$EndComp
$EndSCHEMATC
