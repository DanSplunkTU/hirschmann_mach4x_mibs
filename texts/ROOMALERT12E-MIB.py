#
# PySNMP MIB module ROOMALERT12E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/ROOMALERT12E-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:10:54 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, NotificationType, MibIdentifier, Counter32, NotificationType, Counter64, Gauge32, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "MibIdentifier", "Counter32", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
roomalert12E = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1))
lightTower = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2))
internal_sen = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1)).setLabel("internal-sen")
digital_sen1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2)).setLabel("digital-sen1")
digital_sen2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3)).setLabel("digital-sen2")
digital_sen3 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4)).setLabel("digital-sen3")
switch1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 5))
switch2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 6))
switch3 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 7))
switch4 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 8))
analog = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 9))
relay = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 10))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 9, 3))
internal_sen_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-sen-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_1.setStatus('mandatory')
if mibBuilder.loadTexts: internal_sen_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
internal_sen_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-sen-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_2.setStatus('mandatory')
if mibBuilder.loadTexts: internal_sen_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
internal_sen_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-sen-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_3.setStatus('mandatory')
if mibBuilder.loadTexts: internal_sen_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
internal_sen_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-sen-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_4.setStatus('mandatory')
if mibBuilder.loadTexts: internal_sen_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
internal_sen_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-sen-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_5.setStatus('mandatory')
if mibBuilder.loadTexts: internal_sen_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
internal_sen_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 1, 6), OctetString()).setLabel("internal-sen-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_sen_6.setStatus('mandatory')
if mibBuilder.loadTexts: internal_sen_6.setDescription("Represents the sensor's label/")
analog_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 9, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("analog-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: analog_1.setStatus('mandatory')
if mibBuilder.loadTexts: analog_1.setDescription('The current status of the Room Alert 12E analog input (0-5VDC).')
analog_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 9, 2), OctetString()).setLabel("analog-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: analog_2.setStatus('mandatory')
if mibBuilder.loadTexts: analog_2.setDescription("The analog sensor's label.")
relay_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 10, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("relay-1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: relay_1.setStatus('mandatory')
if mibBuilder.loadTexts: relay_1.setDescription('The current status of the Room Alert 12E relay output.')
relay_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 10, 2), OctetString()).setLabel("relay-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: relay_2.setStatus('mandatory')
if mibBuilder.loadTexts: relay_2.setDescription("The relay output's label.")
digital_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen1_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen1_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
digital_sen1_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen1_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 2, 6), OctetString()).setLabel("digital-sen1-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_6.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_6.setDescription("Represents the sensor's label/")
digital_sen2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
digital_sen2_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen2_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 3, 6), OctetString()).setLabel("digital-sen2-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_6.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_6.setDescription("Represents the sensor's label/")
digital_sen3_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen3_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen3_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen3_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
digital_sen3_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen3_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 4, 6), OctetString()).setLabel("digital-sen3-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_6.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen3_6.setDescription("Represents the sensor's label/")
switch_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen1_1.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen1_1.setDescription('The reading for switch sensor 1 (0 = OPEN, 1 = CLOSED).')
switch_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 5, 2), OctetString()).setLabel("switch-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen1_2.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen1_2.setDescription('The label for switch sensor 1.')
switch_sen2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen2.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen2.setDescription('The reading for switch sensor 2 (0 = OPEN, 1 = CLOSED).')
switch_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 6, 2), OctetString()).setLabel("switch-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen2_2.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen2_2.setDescription('The label for switch sensor 2.')
switch_sen3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen3").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen3.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen3.setDescription('The reading for switch sensor 3 (0 = OPEN, 1 = CLOSED).')
switch_sen3_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 7, 2), OctetString()).setLabel("switch-sen3-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen3_2.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen3_2.setDescription('The label for switch sensor 3.')
switch_sen4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 8, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen4").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen4.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen4.setDescription('The reading for switch sensor 4 (0 = OPEN, 1 = CLOSED).')
switch_sen4_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 1, 8, 2), OctetString()).setLabel("switch-sen4-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen4_2.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen4_2.setDescription('The label for switch sensor 4.')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 3, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
if mibBuilder.loadTexts: alarmmessage.setDescription('Last Alarm Message')
lightTower_RE = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-RE").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_RE.setStatus('mandatory')
if mibBuilder.loadTexts: lightTower_RE.setDescription('The status of the red LED on the Light Tower.')
lightTower_OR = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-OR").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_OR.setStatus('mandatory')
if mibBuilder.loadTexts: lightTower_OR.setDescription('The status of the orange LED on the Light Tower.')
lightTower_GR = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-GR").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_GR.setStatus('mandatory')
if mibBuilder.loadTexts: lightTower_GR.setDescription('The status of the green LED on the Light Tower.')
lightTower_WH = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-WH").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_WH.setStatus('mandatory')
if mibBuilder.loadTexts: lightTower_WH.setDescription('The status of the white LED on the Light Tower.')
lightTower_BL = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-BL").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_BL.setStatus('mandatory')
if mibBuilder.loadTexts: lightTower_BL.setDescription('The status of the blue LED on the Light Tower.')
lightTower_A1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-A1").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_A1.setStatus('mandatory')
if mibBuilder.loadTexts: lightTower_A1.setDescription('The status of the 1st audio alarm on the Light Tower.')
lightTower_A2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-A2").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_A2.setStatus('mandatory')
if mibBuilder.loadTexts: lightTower_A2.setDescription('The status of the 2nd audio alarm on the Light Tower.')
lightTower_RL = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 9, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("lightTower-RL").setMaxAccess("readwrite")
if mibBuilder.loadTexts: lightTower_RL.setStatus('mandatory')
if mibBuilder.loadTexts: lightTower_RL.setDescription("The status of the LTA's on-board relay output")
tempalarm1_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,1)).setLabel("tempalarm1-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempalarm1_12E.setDescription('A tempalarm1 trap signifies that the current\n\t\t\ttemperature on external sensor 1 is outside the\n\t\t\tdefined high or low threshold.')
room_alert_12E_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,2)).setLabel("room-alert-12E-snmp-trap").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: room_alert_12E_snmp_trap.setDescription('A room-alert-12E-snmp-trap indicates that an alarm\n\t\t\tcondition has occurred on the sensor inidcated\n\t\t\tby the alarmMessage variable.')
tempalarm2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,3)).setLabel("tempalarm2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempalarm2_12E.setDescription('A tempalarm2 trap signifies that the current\n\t\t\ttemperature on external sensor 2 is outside the\n\t\t\tdefined high or low threshold.')
tempclear2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,4)).setLabel("tempclear2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempclear2_12E.setDescription('A tempclear2 trap signifies that the current\n\t\t\ttemperature on external sensor 2 has returned to\n\t\t\ta normal condition and is within the defined\n\t\t\thigh or low threshold.')
tempalarm3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,5)).setLabel("tempalarm3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempalarm3_12E.setDescription('A tempalarm3 trap signifies that the current\n\t\t\ttemperature on external sensor 3 is outside the\n\t\t\tdefined high or low threshold.')
tempclear3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,6)).setLabel("tempclear3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempclear3_12E.setDescription('A tempclear3 trap signifies that the current\n\t\t\ttemperature on external sensor 3 has returned to\n\t\t\ta normal condition and is within the defined\n\t\t\thigh or low threshold.')
humidityalarm1_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,7)).setLabel("humidityalarm1-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityalarm1_12E.setDescription('A humidityalarm1 trap signifies that the current\n\t\t\thumidity on external sensor 1 is outside the\n\t\t\tdefined high or low threshold.')
humidityclear1_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,8)).setLabel("humidityclear1-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityclear1_12E.setDescription('A humidityclear1 trap signifies that the current\n\t\t\thumidity on external sensor 1 has returned to\n\t\t\ta normal condition and is within the defined\n\t\t\thigh or low threshold.')
humidityalarm2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,9)).setLabel("humidityalarm2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityalarm2_12E.setDescription('A humidityalarm2 trap signifies that the current\n\t\t\thumidity on external sensor 2 is outside the\n\t\t\tdefined high or low threshold.')
humidityclear2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,10)).setLabel("humidityclear2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityclear2_12E.setDescription('A humidityclear2 trap signifies that the current\n\t\t\thumidity on external sensor 2 has returned to\n\t\t\ta normal condition and is within the defined\n\t\t\thigh or low threshold.')
humidityalarm3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,11)).setLabel("humidityalarm3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityalarm3_12E.setDescription('A humidityalarm3 trap signifies that the current\n\t\t\thumidity on external sensor 3 is outside the\n\t\t\tdefined high or low threshold.')
humidityclear3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,12)).setLabel("humidityclear3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: humidityclear3_12E.setDescription('A humidityclear3 trap signifies that the current\n\t\t\thumidity on external sensor 3 has returned to\n\t\t\ta normal condition and is within the defined\n\t\t\thigh or low threshold.')
switchalarm1_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,13)).setLabel("switchalarm1-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm1_12E.setDescription('A switchalarm1 trap signifies that switch sensor 1\n\t\t\tis in an alarm state.')
switchclear1_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,14)).setLabel("switchclear1-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear1_12E.setDescription('A switchclear1 trap signifies that the switch sensor 1\n\t\t\thas returned to a normal state.')
switchalarm2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,15)).setLabel("switchalarm2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm2_12E.setDescription('A switchalarm2 trap signifies that switch sensor 2\n\t\t\tis in an alarm state.')
switchclear2_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,16)).setLabel("switchclear2-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear2_12E.setDescription('A switchclear2 trap signifies that the switch sensor 2\n\t\t\thas returned to a normal state.')
switchalarm3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,17)).setLabel("switchalarm3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm3_12E.setDescription('A switchalarm3 trap signifies that switch sensor 3\n\t\t\tis in an alarm state.')
switchclear3_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,18)).setLabel("switchclear3-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear3_12E.setDescription('A switchclear3 trap signifies that the switch sensor 3\n\t\t\thas returned to a normal state.')
switchalarm4_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,19)).setLabel("switchalarm4-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchalarm4_12E.setDescription('A switchalarm4 trap signifies that switch sensor 4\n\t\t\tis in an alarm state.')
switchclear4_12E = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 9) + (0,20)).setLabel("switchclear4-12E").setObjects(("ROOMALERT12E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: switchclear4_12E.setDescription('A switchclear4 trap signifies that the switch sensor 4\n\t\t\thas returned to a normal state.')
mibBuilder.exportSymbols("ROOMALERT12E-MIB", traps=traps, switchalarm3_12E=switchalarm3_12E, digital_sen3=digital_sen3, digital_sen3_1=digital_sen3_1, relay_1=relay_1, digital_sen3_4=digital_sen3_4, internal_sen_2=internal_sen_2, lightTower_OR=lightTower_OR, switchclear2_12E=switchclear2_12E, digital_sen1_6=digital_sen1_6, switch_sen4=switch_sen4, relay_2=relay_2, digital_sen3_5=digital_sen3_5, humidityclear1_12E=humidityclear1_12E, digital_sen2_1=digital_sen2_1, switch_sen1_1=switch_sen1_1, tempclear3_12E=tempclear3_12E, lightTower_A2=lightTower_A2, switch1=switch1, switch_sen4_2=switch_sen4_2, digital_sen1_4=digital_sen1_4, switchclear3_12E=switchclear3_12E, internal_sen_6=internal_sen_6, switch4=switch4, digital_sen2_2=digital_sen2_2, humidityclear3_12E=humidityclear3_12E, tempalarm1_12E=tempalarm1_12E, digital_sen3_3=digital_sen3_3, switchclear4_12E=switchclear4_12E, switch_sen2=switch_sen2, analog=analog, lightTower=lightTower, digital_sen1_3=digital_sen1_3, humidityalarm1_12E=humidityalarm1_12E, digital_sen1_5=digital_sen1_5, digital_sen3_2=digital_sen3_2, relay=relay, lightTower_GR=lightTower_GR, lightTower_RE=lightTower_RE, lightTower_A1=lightTower_A1, internal_sen_4=internal_sen_4, internal_sen=internal_sen, roomalert12E=roomalert12E, humidityalarm3_12E=humidityalarm3_12E, digital_sen2=digital_sen2, lightTower_WH=lightTower_WH, sensors=sensors, digital_sen1_1=digital_sen1_1, humidityclear2_12E=humidityclear2_12E, digital_sen2_5=digital_sen2_5, internal_sen_5=internal_sen_5, tempclear2_12E=tempclear2_12E, tempalarm2_12E=tempalarm2_12E, switch_sen1_2=switch_sen1_2, analog_1=analog_1, switchalarm4_12E=switchalarm4_12E, switch_sen2_2=switch_sen2_2, analog_2=analog_2, tempalarm3_12E=tempalarm3_12E, digital_sen1=digital_sen1, lightTower_BL=lightTower_BL, products=products, lightTower_RL=lightTower_RL, switch3=switch3, avtech=avtech, room_alert_12E_snmp_trap=room_alert_12E_snmp_trap, switchclear1_12E=switchclear1_12E, switch_sen3=switch_sen3, alarmmessage=alarmmessage, internal_sen_3=internal_sen_3, internal_sen_1=internal_sen_1, digital_sen2_4=digital_sen2_4, switchalarm1_12E=switchalarm1_12E, switch_sen3_2=switch_sen3_2, switch2=switch2, digital_sen1_2=digital_sen1_2, digital_sen2_6=digital_sen2_6, switchalarm2_12E=switchalarm2_12E, digital_sen2_3=digital_sen2_3, humidityalarm2_12E=humidityalarm2_12E, digital_sen3_6=digital_sen3_6)
