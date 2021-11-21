#
# PySNMP MIB module ROOMALERT24E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/ROOMALERT24E-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:44:35 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ModuleIdentity, Counter32, Integer32, Counter64, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Unsigned32, iso, NotificationType, MibIdentifier, IpAddress, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "Counter32", "Integer32", "Counter64", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Unsigned32", "iso", "NotificationType", "MibIdentifier", "IpAddress", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
roomalert24e = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 2))
internal = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1))
temperature = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 1))
humidity = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 2))
heat_index = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 3)).setLabel("heat-index")
digital = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2))
digital_sen1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1)).setLabel("digital-sen1")
digital_sen2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2)).setLabel("digital-sen2")
digital_sen3 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3)).setLabel("digital-sen3")
digital_sen4 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4)).setLabel("digital-sen4")
digital_sen5 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5)).setLabel("digital-sen5")
digital_sen6 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6)).setLabel("digital-sen6")
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3))
internal_tempf = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempf").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempf.setStatus('mandatory')
internal_tempc = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-tempc").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_tempc.setStatus('mandatory')
internal_humidity = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-humidity").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_humidity.setStatus('mandatory')
internal_heat_index = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-heat-index").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_heat_index.setStatus('mandatory')
internal_heat_indexc = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("internal-heat-indexc").setMaxAccess("readonly")
if mibBuilder.loadTexts: internal_heat_indexc.setStatus('mandatory')
digital_sen1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_1.setStatus('mandatory')
digital_sen1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_2.setStatus('mandatory')
digital_sen1_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_3.setStatus('mandatory')
digital_sen1_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_4.setStatus('mandatory')
digital_sen1_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen1-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen1_5.setStatus('mandatory')
digital_sen2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_1.setStatus('mandatory')
digital_sen2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_2.setStatus('mandatory')
digital_sen2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_3.setStatus('mandatory')
digital_sen2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_4.setStatus('mandatory')
digital_sen2_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen2-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen2_5.setStatus('mandatory')
digital_sen3_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_1.setStatus('mandatory')
digital_sen3_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_2.setStatus('mandatory')
digital_sen3_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_3.setStatus('mandatory')
digital_sen3_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_4.setStatus('mandatory')
digital_sen3_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen3-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen3_5.setStatus('mandatory')
digital_sen4_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen4-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen4_1.setStatus('mandatory')
digital_sen4_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen4-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen4_2.setStatus('mandatory')
digital_sen4_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen4-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen4_3.setStatus('mandatory')
digital_sen4_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen4-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen4_4.setStatus('mandatory')
digital_sen4_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen4-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen4_5.setStatus('mandatory')
digital_sen5_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen5-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen5_1.setStatus('mandatory')
digital_sen5_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen5-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen5_2.setStatus('mandatory')
digital_sen5_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen5-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen5_3.setStatus('mandatory')
digital_sen5_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen5-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen5_4.setStatus('mandatory')
digital_sen5_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 5, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen5-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen5_5.setStatus('mandatory')
digital_sen6_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen6-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen6_1.setStatus('mandatory')
digital_sen6_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen6-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen6_2.setStatus('mandatory')
digital_sen6_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen6-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen6_3.setStatus('mandatory')
digital_sen6_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen6-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen6_4.setStatus('mandatory')
digital_sen6_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 2, 6, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("digital-sen6-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: digital_sen6_5.setStatus('mandatory')
switch_sen1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen1").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen1.setStatus('mandatory')
switch_sen2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen2.setStatus('mandatory')
switch_sen3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen3").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen3.setStatus('mandatory')
switch_sen4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen4").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen4.setStatus('mandatory')
switch_sen5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen5").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen5.setStatus('mandatory')
switch_sen6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen6").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen6.setStatus('mandatory')
switch_sen7 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen7").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen7.setStatus('mandatory')
switch_sen8 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen8").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen8.setStatus('mandatory')
switch_sen9 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen9").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen9.setStatus('mandatory')
switch_sen10 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen10").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen10.setStatus('mandatory')
switch_sen11 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen11").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen11.setStatus('mandatory')
switch_sen12 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen12").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen12.setStatus('mandatory')
switch_sen13 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen13").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen13.setStatus('mandatory')
switch_sen14 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen14").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen14.setStatus('mandatory')
switch_sen15 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen15").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen15.setStatus('mandatory')
switch_sen16 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 1, 3, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("switch-sen16").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_sen16.setStatus('mandatory')
alarmmessage = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 5, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmmessage.setStatus('mandatory')
tempalarm1_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,1)).setLabel("tempalarm1-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
room_alert_24e_snmp_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,2)).setLabel("room-alert-24e-snmp-trap").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
tempalarm2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,3)).setLabel("tempalarm2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
tempclear2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,4)).setLabel("tempclear2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
tempalarm3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,5)).setLabel("tempalarm3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
tempclear3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,6)).setLabel("tempclear3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
humidityalarm1_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,7)).setLabel("humidityalarm1-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
humidityclear1_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,8)).setLabel("humidityclear1-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
humidityalarm2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,9)).setLabel("humidityalarm2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
humidityclear2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,10)).setLabel("humidityclear2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
humidityalarm3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,11)).setLabel("humidityalarm3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
humidityclear3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,12)).setLabel("humidityclear3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchalarm1_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,13)).setLabel("switchalarm1-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchclear1_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,14)).setLabel("switchclear1-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchalarm2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,15)).setLabel("switchalarm2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchclear2_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,16)).setLabel("switchclear2-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchalarm3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,17)).setLabel("switchalarm3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchclear3_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,18)).setLabel("switchclear3-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchalarm4_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,19)).setLabel("switchalarm4-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchclear4_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,20)).setLabel("switchclear4-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchalarm5_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,21)).setLabel("switchalarm5-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchclear5_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,22)).setLabel("switchclear5-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchalarm6_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,23)).setLabel("switchalarm6-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchclear6_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,24)).setLabel("switchclear6-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchalarm7_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,25)).setLabel("switchalarm7-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchclear7_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,26)).setLabel("switchclear7-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchalarm8_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,27)).setLabel("switchalarm8-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
switchclear8_24e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 5) + (0,28)).setLabel("switchclear8-24e").setObjects(("ROOMALERT24E-MIB", "alarmmessage"))
mibBuilder.exportSymbols("ROOMALERT24E-MIB", digital_sen3_2=digital_sen3_2, digital_sen2_2=digital_sen2_2, switch_sen13=switch_sen13, internal=internal, switchalarm4_24e=switchalarm4_24e, switchclear6_24e=switchclear6_24e, internal_heat_index=internal_heat_index, switch_sen3=switch_sen3, switchclear7_24e=switchclear7_24e, heat_index=heat_index, digital_sen6=digital_sen6, switch_sen12=switch_sen12, alarmmessage=alarmmessage, digital_sen6_3=digital_sen6_3, switchclear5_24e=switchclear5_24e, digital_sen6_4=digital_sen6_4, digital_sen2_1=digital_sen2_1, digital_sen5_4=digital_sen5_4, traps=traps, digital_sen2_4=digital_sen2_4, roomalert24e=roomalert24e, digital_sen2=digital_sen2, internal_heat_indexc=internal_heat_indexc, tempalarm2_24e=tempalarm2_24e, switch_sen5=switch_sen5, humidityalarm2_24e=humidityalarm2_24e, switchclear1_24e=switchclear1_24e, humidityclear2_24e=humidityclear2_24e, humidityclear3_24e=humidityclear3_24e, digital_sen1_5=digital_sen1_5, digital_sen4=digital_sen4, tempclear2_24e=tempclear2_24e, digital_sen3=digital_sen3, switch_sen9=switch_sen9, digital_sen5_5=digital_sen5_5, humidityalarm1_24e=humidityalarm1_24e, digital_sen3_4=digital_sen3_4, switch_sen11=switch_sen11, digital_sen6_5=digital_sen6_5, switch_sen8=switch_sen8, digital_sen1=digital_sen1, switchalarm1_24e=switchalarm1_24e, switch_sen2=switch_sen2, humidityalarm3_24e=humidityalarm3_24e, switchclear3_24e=switchclear3_24e, humidity=humidity, internal_humidity=internal_humidity, digital_sen3_3=digital_sen3_3, digital_sen1_4=digital_sen1_4, tempalarm1_24e=tempalarm1_24e, switchalarm5_24e=switchalarm5_24e, switch_sen15=switch_sen15, tempclear3_24e=tempclear3_24e, temperature=temperature, switchalarm6_24e=switchalarm6_24e, tempalarm3_24e=tempalarm3_24e, switch=switch, digital_sen6_2=digital_sen6_2, switchalarm3_24e=switchalarm3_24e, avtech=avtech, digital_sen2_3=digital_sen2_3, sensors=sensors, digital_sen5_3=digital_sen5_3, digital_sen5=digital_sen5, switchclear2_24e=switchclear2_24e, switch_sen10=switch_sen10, digital_sen4_4=digital_sen4_4, digital=digital, digital_sen3_5=digital_sen3_5, internal_tempf=internal_tempf, switchclear4_24e=switchclear4_24e, digital_sen1_3=digital_sen1_3, switch_sen1=switch_sen1, products=products, digital_sen4_3=digital_sen4_3, internal_tempc=internal_tempc, digital_sen2_5=digital_sen2_5, switchclear8_24e=switchclear8_24e, digital_sen1_2=digital_sen1_2, switch_sen7=switch_sen7, humidityclear1_24e=humidityclear1_24e, switch_sen14=switch_sen14, switchalarm8_24e=switchalarm8_24e, digital_sen4_1=digital_sen4_1, switchalarm7_24e=switchalarm7_24e, digital_sen6_1=digital_sen6_1, digital_sen1_1=digital_sen1_1, digital_sen3_1=digital_sen3_1, digital_sen4_5=digital_sen4_5, switch_sen16=switch_sen16, switchalarm2_24e=switchalarm2_24e, digital_sen5_1=digital_sen5_1, switch_sen6=switch_sen6, digital_sen5_2=digital_sen5_2, switch_sen4=switch_sen4, digital_sen4_2=digital_sen4_2, room_alert_24e_snmp_trap=room_alert_24e_snmp_trap)
