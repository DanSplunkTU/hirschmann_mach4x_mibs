#
# PySNMP MIB module ROOMALERTST4E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/ROOMALERTST4E-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:32:13 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, Counter32, NotificationType, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, enterprises, ModuleIdentity, IpAddress, NotificationType, MibIdentifier, TimeTicks, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "Counter32", "NotificationType", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "enterprises", "ModuleIdentity", "IpAddress", "NotificationType", "MibIdentifier", "TimeTicks", "Counter64", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
ROOMALERTST4E = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1))
signaltower = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 3))
internal = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1))
temperature = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 1))
humidity = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 2))
heat_index = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 3)).setLabel("heat-index")
digital = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2))
digital_sen1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1)).setLabel("digital-sen1")
digital_sen2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2)).setLabel("digital-sen2")
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 3))
internal_tempf = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempf").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempf.setStatus('mandatory')
internal_tempc = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempc").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempc.setStatus('mandatory')
internal_humidity = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-humidity").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_humidity.setStatus('mandatory')
internal_heat_index = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-heat-index").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_heat_index.setStatus('mandatory')
digital_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_1.setStatus('mandatory')
digital_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_2.setStatus('mandatory')
digital_sen1_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_3.setStatus('mandatory')
digital_sen1_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_4.setStatus('mandatory')
digital_sen2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_1.setStatus('mandatory')
digital_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_2.setStatus('mandatory')
digital_sen2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_3.setStatus('mandatory')
digital_sen2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_4.setStatus('mandatory')
switch_sen1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen1").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen1.setStatus('mandatory')
red_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("red-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: red_led.setStatus('current')
amber_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("amber-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: amber_led.setStatus('current')
green_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("green-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: green_led.setStatus('current')
blue_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("blue-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: blue_led.setStatus('current')
white_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("white-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: white_led.setStatus('current')
alarm1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarm1.setStatus('current')
alarm2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarm2.setStatus('current')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 3, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
room_alert_st4e_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 6) + (0,2)).setLabel("room-alert-st4e-snmp-trap").setObjects(("ROOMALERTST4E-MIB", "alarmmessage"))
mibBuilder.exportSymbols("ROOMALERTST4E-MIB", signaltower=signaltower, traps=traps, alarm1=alarm1, red_led=red_led, digital_sen2_1=digital_sen2_1, digital_sen2=digital_sen2, internal=internal, digital_sen1_1=digital_sen1_1, internal_tempc=internal_tempc, digital_sen1_2=digital_sen1_2, digital_sen2_2=digital_sen2_2, products=products, switch=switch, digital_sen1_3=digital_sen1_3, switch_sen1=switch_sen1, sensors=sensors, blue_led=blue_led, heat_index=heat_index, alarm2=alarm2, digital_sen2_4=digital_sen2_4, digital_sen2_3=digital_sen2_3, temperature=temperature, internal_humidity=internal_humidity, internal_tempf=internal_tempf, digital_sen1_4=digital_sen1_4, digital=digital, internal_heat_index=internal_heat_index, humidity=humidity, white_led=white_led, alarmmessage=alarmmessage, digital_sen1=digital_sen1, ROOMALERTST4E=ROOMALERTST4E, avtech=avtech, green_led=green_led, room_alert_st4e_snmp_trap=room_alert_st4e_snmp_trap, amber_led=amber_led)
