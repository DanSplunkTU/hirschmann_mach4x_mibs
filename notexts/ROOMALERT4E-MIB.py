#
# PySNMP MIB module ROOMALERT4E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/ROOMALERT4E-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:10:53 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Bits, ModuleIdentity, Unsigned32, NotificationType, Counter32, IpAddress, Integer32, Counter64, NotificationType, iso, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Bits", "ModuleIdentity", "Unsigned32", "NotificationType", "Counter32", "IpAddress", "Integer32", "Counter64", "NotificationType", "iso", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "TimeTicks")
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
internal_tempc = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempc").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempc.setStatus('mandatory')
internal_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 2, 1), OctetString()).setLabel("internal-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_label.setStatus('mandatory')
digital_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_1.setStatus('mandatory')
digital_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_2.setStatus('mandatory')
digital_sen1_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_3.setStatus('mandatory')
digital_sen1_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_4.setStatus('mandatory')
digital_sen1_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_5.setStatus('mandatory')
digital_sen1_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_6.setStatus('mandatory')
digital_sen1_7 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-7").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_7.setStatus('mandatory')
digital_sen1_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 8), OctetString()).setLabel("digital-sen1-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_label.setStatus('mandatory')
digital_sen2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_1.setStatus('mandatory')
digital_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_2.setStatus('mandatory')
digital_sen2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_3.setStatus('mandatory')
digital_sen2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_4.setStatus('mandatory')
digital_sen2_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_5.setStatus('mandatory')
digital_sen2_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_6.setStatus('mandatory')
digital_sen2_7 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-7").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_7.setStatus('mandatory')
digital_sen2_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 8), OctetString()).setLabel("digital-sen2-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_label.setStatus('mandatory')
switch_sen1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen1").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen1.setStatus('mandatory')
switch_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 3, 2), OctetString()).setLabel("switch-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label.setStatus('mandatory')
red_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("red-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: red_led.setStatus('mandatory')
amber_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("amber-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: amber_led.setStatus('mandatory')
green_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("green-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: green_led.setStatus('mandatory')
blue_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("blue-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: blue_led.setStatus('mandatory')
white_led = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("white-led").setMaxAccess("readwrite")
if mibBuilder.loadTexts: white_led.setStatus('mandatory')
alarm1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarm1.setStatus('mandatory')
alarm2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarm2.setStatus('mandatory')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 6, 3, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
room_alert_4e_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 6) + (0,2)).setLabel("room-alert-4e-snmp-trap").setObjects(("ROOMALERT4E-MIB", "alarmmessage"))
mibBuilder.exportSymbols("ROOMALERT4E-MIB", digital_sen2_5=digital_sen2_5, alarm2=alarm2, traps=traps, red_led=red_led, digital_sen2_3=digital_sen2_3, switch_label=switch_label, digital_sen1_2=digital_sen1_2, digital_sen2_label=digital_sen2_label, digital_sen1=digital_sen1, amber_led=amber_led, digital_sen1_6=digital_sen1_6, white_led=white_led, alarmmessage=alarmmessage, sensors=sensors, internal_tempf=internal_tempf, digital_sen2_7=digital_sen2_7, internal=internal, roomalert4E=roomalert4E, signaltower=signaltower, digital_sen2_2=digital_sen2_2, digital_sen1_1=digital_sen1_1, switch_sen1=switch_sen1, blue_led=blue_led, alarm1=alarm1, digital_sen1_3=digital_sen1_3, digital_sen1_7=digital_sen1_7, temperature=temperature, digital_sen1_4=digital_sen1_4, digital_sen2=digital_sen2, digital_sen1_label=digital_sen1_label, avtech=avtech, digital=digital, internal_label=internal_label, label=label, digital_sen2_6=digital_sen2_6, green_led=green_led, digital_sen1_5=digital_sen1_5, switch=switch, room_alert_4e_snmp_trap=room_alert_4e_snmp_trap, products=products, internal_tempc=internal_tempc, digital_sen2_1=digital_sen2_1, digital_sen2_4=digital_sen2_4)
