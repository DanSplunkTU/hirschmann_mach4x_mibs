#
# PySNMP MIB module TEMPAGER3E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/TEMPAGER3E-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:32:14 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, Counter32, NotificationType, ModuleIdentity, enterprises, Counter64, Gauge32, IpAddress, Integer32, ObjectIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "Counter32", "NotificationType", "ModuleIdentity", "enterprises", "Counter64", "Gauge32", "IpAddress", "Integer32", "ObjectIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
TEMPAGER3E = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 7))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 7, 2))
internal = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 1))
temperature = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 1, 1))
digital = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2))
digital_sen1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2, 1)).setLabel("digital-sen1")
digital_sen2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2, 2)).setLabel("digital-sen2")
internal_tempc = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempc").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempc.setStatus('mandatory')
if mibBuilder.loadTexts: internal_tempc.setDescription('The internal temperature reading in Celsius. Because the SNMP Protocol does not support floating point numbers, values are scaled by 100 and should be divided by 100 to get the actual value.')
internal_tempf = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempf").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempf.setStatus('mandatory')
if mibBuilder.loadTexts: internal_tempf.setDescription('The internal temperature reading in Fahrenheit. Because the SNMP Protocol does not support floating point numbers, values are scaled by 100 and should be divided by 100 to get the actual value.')
digital_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen1_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen1_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen1_4.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
digital_sen2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_1.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_1.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Celsius. If this sensor is a Digital Power Sensor, this value represents the Current reading in Amperage.')
digital_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_2.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_2.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current temperature in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Power reading in Watts.')
digital_sen2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_3.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_3.setDescription('If this sensor is a Temp/Humidity sensor, this value represents the current relative humidity in % Relative Humidity. If this sensor is a Digital Power Sensor, this value represents the Voltage reading in Volts.')
digital_sen2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 1, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_4.setStatus('mandatory')
if mibBuilder.loadTexts: digital_sen2_4.setDescription('If this sensor is a Temperature or Temp/Humidity sensor, this value represents the current heat index in Fahrenheit. If this sensor is a Digital Power Sensor, this value represents the Reference reading in Volts.')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 7, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
if mibBuilder.loadTexts: alarmmessage.setDescription('Last Alarm Message')
tempager3e_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 7) + (0,2)).setLabel("tempager3e-snmp-trap").setObjects(("TEMPAGER3E-MIB", "alarmmessage"))
if mibBuilder.loadTexts: tempager3e_snmp_trap.setDescription('A tempager3e-snmp-trap indicates that an alarm\n\t\t\tcondition has occurred on the sensor indicated\n\t\t\tby the alarmmessage variable.')
mibBuilder.exportSymbols("TEMPAGER3E-MIB", digital_sen1=digital_sen1, avtech=avtech, digital_sen1_4=digital_sen1_4, digital_sen2_2=digital_sen2_2, TEMPAGER3E=TEMPAGER3E, tempager3e_snmp_trap=tempager3e_snmp_trap, digital_sen2=digital_sen2, digital_sen1_1=digital_sen1_1, alarmmessage=alarmmessage, traps=traps, digital_sen2_3=digital_sen2_3, digital_sen1_3=digital_sen1_3, internal_tempc=internal_tempc, digital_sen2_1=digital_sen2_1, internal=internal, digital=digital, internal_tempf=internal_tempf, temperature=temperature, digital_sen1_2=digital_sen1_2, digital_sen2_4=digital_sen2_4, products=products, sensors=sensors)
