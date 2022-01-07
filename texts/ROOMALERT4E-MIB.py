#
# PySNMP MIB module ROOMALERT4E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/ROOMALERT4E-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:54:54 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, IpAddress, Integer32, TimeTicks, ModuleIdentity, MibIdentifier, ObjectIdentity, Bits, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Counter32, iso, NotificationType, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "Integer32", "TimeTicks", "ModuleIdentity", "MibIdentifier", "ObjectIdentity", "Bits", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Counter32", "iso", "NotificationType", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
roomalert4E = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1))
signaltower = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 3))
internal = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1))
temperature = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 1))
label = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 2))
digital = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2))
digital_sen1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1)).setLabel("digital-sen1")
digital_sen2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2)).setLabel("digital-sen2")
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 3))
internal_tempf = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempf").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempf.setStatus('mandatory')
if mibBuilder.loadTexts: internal_tempf.setDescription('The internal temperature reading in Fahrenheit.')
internal_tempc = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempc").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempc.setStatus('mandatory')
if mibBuilder.loadTexts: internal_tempc.setDescription('The internal temperature reading in Celsius.')
internal_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 2, 1), OctetString()).setLabel("internal-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_label.setStatus('mandatory')
if mibBuilder.loadTexts: internal_label.setDescription('The label of this sensor')
digital_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_1.setDescription('If this sensor is a Temperature, Temp/Humidity, Temp/Analog, or Temp/Active Power sensor, this value represents the current temperature in Celsius.')
digital_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_2.setDescription('If this sensor is a Temperature, Temp/Humidity, Temp/Analog, or Temp/Active Power sensor, this value represents the current temperature in Fahrenheit.')
digital_sen1_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Temp/Analog sensor, this value represents the current Voltage reading. If this is a Temp/Active Power sensor, this value represents the current power state (1=Power Detected, 0=No Power Detected).')
digital_sen1_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Temp/Analog sensor, this value represents the current custom reading.')
digital_sen1_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen1_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_6.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_6.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current dew point in Celsius.')
digital_sen1_7 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-7").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_7.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_7.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current dew point in Fahrenheit.')
digital_sen1_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 8), OctetString()).setLabel("digital-sen1-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_label.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_label.setDescription('The label of this sensor')
digital_sen2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_1.setDescription('If this sensor is a Temperature, Temp/Humidity, Temp/Analog, or Temp/Active Power sensor, this value represents the current temperature in Celsius.')
digital_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_2.setDescription('If this sensor is a Temperature, Temp/Humidity, Temp/Analog, or Temp/Active Power sensor, this value represents the current temperature in Fahrenheit.')
digital_sen2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Temp/Analog sensor, this value represents the current Voltage reading. If this is a Temp/Active Power sensor, this value represents the current power state (1=Power Detected, 0=No Power Detected).')
digital_sen2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_4.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Temp/Analog sensor, this value represents the current custom reading.')
digital_sen2_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_5.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_5.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current heat index in Celsius.')
digital_sen2_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_6.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_6.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current dew point in Celsius.')
digital_sen2_7 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-7").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_7.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_7.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current dew point in Fahrenheit.')
digital_sen2_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 8), OctetString()).setLabel("digital-sen2-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_label.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_label.setDescription('The label of this sensor')
switch_sen1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen1").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen1.setStatus('mandatory')
if mibBuilder.loadTexts: switch_sen1.setDescription('The reading for the switch sensor 1 (0 = OPEN, 1 = CLOSED).')
switch_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 3, 2), OctetString()).setLabel("switch-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label.setStatus('mandatory')
if mibBuilder.loadTexts: switch_label.setDescription('The label for the switch sensor')
red_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("red-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: red_led.setStatus('mandatory')
if mibBuilder.loadTexts: red_led.setDescription('The status of this Light Tower element (0 = OFF, 1 = ON).')
amber_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("amber-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: amber_led.setStatus('mandatory')
if mibBuilder.loadTexts: amber_led.setDescription('The status of this Light Tower element (0 = OFF, 1 = ON).')
green_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("green-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: green_led.setStatus('mandatory')
if mibBuilder.loadTexts: green_led.setDescription('The status of this Light Tower element (0 = OFF, 1 = ON).')
blue_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("blue-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: blue_led.setStatus('mandatory')
if mibBuilder.loadTexts: blue_led.setDescription('The status of this Light Tower element (0 = OFF, 1 = ON).')
white_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("white-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: white_led.setStatus('mandatory')
if mibBuilder.loadTexts: white_led.setDescription('The status of this Light Tower element (0 = OFF, 1 = ON).')
alarm1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarm1.setStatus('mandatory')
if mibBuilder.loadTexts: alarm1.setDescription('The status of this Light Tower element (0 = OFF, 1 = ON).')
alarm2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarm2.setStatus('mandatory')
if mibBuilder.loadTexts: alarm2.setDescription('The status of this Light Tower element (0 = OFF, 1 = ON).')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 3, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
if mibBuilder.loadTexts: alarmmessage.setDescription('Last Alarm Message')
room_alert_4e_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 6) + (0,2)).setLabel("room-alert-4e-snmp-trap").setObjects(("ROOMALERT4E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: room_alert_4e_snmp_trap.setDescription('A room-alert-4e-snmp-trap indicates that an alarm\n\t\t\tcondition has occurred on the sensor indicated\n\t\t\tby the alarmmessage variable.')
mibBuilder.exportSymbols("ROOMALERT4E-MIB", digital_sen1_7=digital_sen1_7, internal_label=internal_label, temperature=temperature, internal_tempc=internal_tempc, digital_sen1_2=digital_sen1_2, digital_sen2_1=digital_sen2_1, red_led=red_led, green_led=green_led, digital_sen1_1=digital_sen1_1, digital_sen2=digital_sen2, alarm2=alarm2, products=products, label=label, avtech=avtech, switch_label=switch_label, digital_sen1_3=digital_sen1_3, traps=traps, white_led=white_led, digital_sen1_5=digital_sen1_5, signaltower=signaltower, digital_sen2_label=digital_sen2_label, digital_sen2_3=digital_sen2_3, alarmmessage=alarmmessage, blue_led=blue_led, roomalert4E=roomalert4E, digital_sen2_4=digital_sen2_4, amber_led=amber_led, digital_sen1=digital_sen1, digital_sen2_5=digital_sen2_5, internal=internal, switch_sen1=switch_sen1, alarm1=alarm1, switch=switch, internal_tempf=internal_tempf, digital_sen2_7=digital_sen2_7, room_alert_4e_snmp_trap=room_alert_4e_snmp_trap, digital_sen1_label=digital_sen1_label, digital=digital, digital_sen1_6=digital_sen1_6, digital_sen2_6=digital_sen2_6, digital_sen2_2=digital_sen2_2, sensors=sensors, digital_sen1_4=digital_sen1_4)
