#
# PySNMP MIB module ROOMALERT11E-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avtech/ROOMALERT11E-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:58 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, NotificationType, ObjectIdentity, Counter32, iso, Gauge32, Unsigned32, Integer32, NotificationType, MibIdentifier, ModuleIdentity, Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "NotificationType", "ObjectIdentity", "Counter32", "iso", "Gauge32", "Unsigned32", "Integer32", "NotificationType", "MibIdentifier", "ModuleIdentity", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avtech = MibIdentifier((1, 3, 6, 1, 4, 1, 20916))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1))
roomalert11E = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3))
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 2))
thresholds = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3))
channel1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1))
channel2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 2))
channel3 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 3))
channel4 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 4))
channels = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1))
channels1 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 1))
channels2 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 2))
channels3 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 3))
channels4 = MibIdentifier((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 4))
sensor1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("sensor1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1_1.setStatus('mandatory')
sensor1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("sensor1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1_2.setStatus('mandatory')
sensor1_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("sensor1-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1_3.setStatus('mandatory')
sensor1_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("sensor1-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1_4.setStatus('mandatory')
sensor1_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("sensor1-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1_5.setStatus('mandatory')
sensor1_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("sensor1-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1_6.setStatus('mandatory')
sensor1_7 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("sensor1-7").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1_7.setStatus('mandatory')
sensor1_8 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setLabel("sensor1-8").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor1_8.setStatus('mandatory')
switch_label_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 9), OctetString()).setLabel("switch-label-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label_1.setStatus('mandatory')
switch_label_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 10), OctetString()).setLabel("switch-label-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label_2.setStatus('mandatory')
switch_label_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 11), OctetString()).setLabel("switch-label-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label_3.setStatus('mandatory')
switch_label_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 12), OctetString()).setLabel("switch-label-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label_4.setStatus('mandatory')
switch_label_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 13), OctetString()).setLabel("switch-label-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label_5.setStatus('mandatory')
switch_label_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 14), OctetString()).setLabel("switch-label-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label_6.setStatus('mandatory')
switch_label_7 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 15), OctetString()).setLabel("switch-label-7").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label_7.setStatus('mandatory')
switch_label_8 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 1, 16), OctetString()).setLabel("switch-label-8").setMaxAccess("readonly")
if mibBuilder.loadTexts: switch_label_8.setStatus('mandatory')
sensor2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2_1.setStatus('mandatory')
sensor2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2_2.setStatus('mandatory')
sensor2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2_3.setStatus('mandatory')
sensor2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2_4.setStatus('mandatory')
sensor2_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor2-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2_5.setStatus('mandatory')
sensor2_6_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 2, 6), OctetString()).setLabel("sensor2-6-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor2_6_label.setStatus('mandatory')
sensor3_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor3-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3_1.setStatus('mandatory')
sensor3_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor3-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3_2.setStatus('mandatory')
sensor3_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor3-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3_3.setStatus('mandatory')
sensor3_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor3-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3_4.setStatus('mandatory')
sensor3_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor3-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3_5.setStatus('mandatory')
sensor3_6_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 3, 6), OctetString()).setLabel("sensor3-6-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor3_6_label.setStatus('mandatory')
sensor4_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor4-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4_1.setStatus('mandatory')
sensor4_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor4-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4_2.setStatus('mandatory')
sensor4_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor4-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4_3.setStatus('mandatory')
sensor4_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor4-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4_4.setStatus('mandatory')
sensor4_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("sensor4-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4_5.setStatus('mandatory')
sensor4_6_label = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 1, 4, 6), OctetString()).setLabel("sensor4-6-label").setMaxAccess("readonly")
if mibBuilder.loadTexts: sensor4_6_label.setStatus('mandatory')
alarm1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarm1.setStatus('mandatory')
alarm2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarm2.setStatus('mandatory')
alarm3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarm3.setStatus('mandatory')
alarm4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarm4.setStatus('mandatory')
alarmMessage1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMessage1.setStatus('mandatory')
alarmMessage2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 2, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMessage2.setStatus('mandatory')
alarmMessage3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 2, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMessage3.setStatus('mandatory')
alarmMessage4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 2, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMessage4.setStatus('mandatory')
threshold1_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold1-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold1_1.setStatus('mandatory')
threshold1_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold1-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold1_2.setStatus('mandatory')
threshold1_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold1-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold1_3.setStatus('mandatory')
threshold1_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold1-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold1_4.setStatus('mandatory')
threshold1_5 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold1-5").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold1_5.setStatus('mandatory')
threshold1_6 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold1-6").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold1_6.setStatus('mandatory')
threshold1_7 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold1-7").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold1_7.setStatus('mandatory')
threshold1_8 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold1-8").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold1_8.setStatus('mandatory')
threshold2_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold2-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold2_1.setStatus('mandatory')
threshold2_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold2-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold2_2.setStatus('mandatory')
threshold2_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold2-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold2_3.setStatus('mandatory')
threshold2_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold2-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold2_4.setStatus('mandatory')
threshold3_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold3-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold3_1.setStatus('mandatory')
threshold3_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold3-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold3_2.setStatus('mandatory')
threshold3_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold3-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold3_3.setStatus('mandatory')
threshold3_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold3-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold3_4.setStatus('mandatory')
threshold4_1 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold4-1").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold4_1.setStatus('mandatory')
threshold4_2 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold4-2").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold4_2.setStatus('mandatory')
threshold4_3 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold4-3").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold4_3.setStatus('mandatory')
threshold4_4 = MibScalar((1, 3, 6, 1, 4, 1, 20916, 1, 3, 3, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setLabel("threshold4-4").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshold4_4.setStatus('mandatory')
tempAlarm1_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,1)).setLabel("tempAlarm1-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage2"), ("ROOMALERT11E-MIB", "sensor2_1"), ("ROOMALERT11E-MIB", "sensor2_2"), ("ROOMALERT11E-MIB", "sensor2_1"))
room_alert_11E_SNMP_trap = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,2)).setLabel("room-alert-11E-SNMP-trap").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "alarmMessage2"), ("ROOMALERT11E-MIB", "alarmMessage3"), ("ROOMALERT11E-MIB", "alarmMessage4"))
tempAlarm2_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,3)).setLabel("tempAlarm2-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage3"), ("ROOMALERT11E-MIB", "sensor3_1"), ("ROOMALERT11E-MIB", "sensor3_2"), ("ROOMALERT11E-MIB", "sensor3_1"))
tempClear2_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,4)).setLabel("tempClear2-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage3"), ("ROOMALERT11E-MIB", "sensor3_1"), ("ROOMALERT11E-MIB", "sensor3_2"), ("ROOMALERT11E-MIB", "sensor3_1"))
tempAlarm3_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,5)).setLabel("tempAlarm3-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage4"), ("ROOMALERT11E-MIB", "sensor4_1"), ("ROOMALERT11E-MIB", "sensor4_2"), ("ROOMALERT11E-MIB", "sensor4_1"))
tempClear3_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,6)).setLabel("tempClear3-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage4"), ("ROOMALERT11E-MIB", "sensor4_1"), ("ROOMALERT11E-MIB", "sensor4_2"), ("ROOMALERT11E-MIB", "sensor4_1"))
humidityAlarm1_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,7)).setLabel("humidityAlarm1-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage2"), ("ROOMALERT11E-MIB", "sensor2_1"), ("ROOMALERT11E-MIB", "sensor2_2"), ("ROOMALERT11E-MIB", "sensor2_3"))
humidityClear1_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,8)).setLabel("humidityClear1-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage2"), ("ROOMALERT11E-MIB", "sensor2_1"), ("ROOMALERT11E-MIB", "sensor2_2"), ("ROOMALERT11E-MIB", "sensor2_3"))
humidityAlarm2_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,9)).setLabel("humidityAlarm2-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage3"), ("ROOMALERT11E-MIB", "sensor3_1"), ("ROOMALERT11E-MIB", "sensor3_2"), ("ROOMALERT11E-MIB", "sensor3_3"))
humidityClear2_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,10)).setLabel("humidityClear2-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage3"), ("ROOMALERT11E-MIB", "sensor3_1"), ("ROOMALERT11E-MIB", "sensor3_2"), ("ROOMALERT11E-MIB", "sensor3_3"))
humidityAlarm3_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,11)).setLabel("humidityAlarm3-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage4"), ("ROOMALERT11E-MIB", "sensor4_1"), ("ROOMALERT11E-MIB", "sensor4_2"), ("ROOMALERT11E-MIB", "sensor4_3"))
humidityClear3_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,12)).setLabel("humidityClear3-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage4"), ("ROOMALERT11E-MIB", "sensor4_1"), ("ROOMALERT11E-MIB", "sensor4_2"), ("ROOMALERT11E-MIB", "sensor4_3"))
switchAlarm1_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,13)).setLabel("switchAlarm1-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_1"), ("ROOMALERT11E-MIB", "sensor1_1"), ("ROOMALERT11E-MIB", "sensor1_1"))
switchClear1_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,14)).setLabel("switchClear1-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_1"), ("ROOMALERT11E-MIB", "sensor1_1"), ("ROOMALERT11E-MIB", "sensor1_1"))
switchAlarm2_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,15)).setLabel("switchAlarm2-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_2"), ("ROOMALERT11E-MIB", "sensor1_2"), ("ROOMALERT11E-MIB", "sensor1_2"))
switchClear2_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,16)).setLabel("switchClear2-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_2"), ("ROOMALERT11E-MIB", "sensor1_2"), ("ROOMALERT11E-MIB", "sensor1_2"))
switchAlarm3_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,17)).setLabel("switchAlarm3-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_3"), ("ROOMALERT11E-MIB", "sensor1_3"), ("ROOMALERT11E-MIB", "sensor1_3"))
switchClear3_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,18)).setLabel("switchClear3-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_3"), ("ROOMALERT11E-MIB", "sensor1_3"), ("ROOMALERT11E-MIB", "sensor1_3"))
switchAlarm4_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,19)).setLabel("switchAlarm4-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_4"), ("ROOMALERT11E-MIB", "sensor1_4"), ("ROOMALERT11E-MIB", "sensor1_4"))
switchClear4_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,20)).setLabel("switchClear4-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_4"), ("ROOMALERT11E-MIB", "sensor1_4"), ("ROOMALERT11E-MIB", "sensor1_4"))
switchAlarm5_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,21)).setLabel("switchAlarm5-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_5"), ("ROOMALERT11E-MIB", "sensor1_5"), ("ROOMALERT11E-MIB", "sensor1_5"))
switchClear5_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,22)).setLabel("switchClear5-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_5"), ("ROOMALERT11E-MIB", "sensor1_5"), ("ROOMALERT11E-MIB", "sensor1_5"))
switchAlarm6_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,23)).setLabel("switchAlarm6-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_6"), ("ROOMALERT11E-MIB", "sensor1_6"), ("ROOMALERT11E-MIB", "sensor1_6"))
switchClear6_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,24)).setLabel("switchClear6-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_6"), ("ROOMALERT11E-MIB", "sensor1_6"), ("ROOMALERT11E-MIB", "sensor1_6"))
switchAlarm7_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,25)).setLabel("switchAlarm7-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_7"), ("ROOMALERT11E-MIB", "sensor1_7"), ("ROOMALERT11E-MIB", "sensor1_7"))
switchClear7_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,26)).setLabel("switchClear7-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_7"), ("ROOMALERT11E-MIB", "sensor1_7"), ("ROOMALERT11E-MIB", "sensor1_7"))
switchAlarm8_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,27)).setLabel("switchAlarm8-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_8"), ("ROOMALERT11E-MIB", "sensor1_8"), ("ROOMALERT11E-MIB", "sensor1_8"))
switchClear8_11e = NotificationType((1, 3, 6, 1, 4, 1, 20916, 1, 3) + (0,28)).setLabel("switchClear8-11e").setObjects(("ROOMALERT11E-MIB", "alarmMessage1"), ("ROOMALERT11E-MIB", "sensor1_8"), ("ROOMALERT11E-MIB", "sensor1_8"), ("ROOMALERT11E-MIB", "sensor1_8"))
mibBuilder.exportSymbols("ROOMALERT11E-MIB", alarm2=alarm2, tempClear3_11e=tempClear3_11e, channels=channels, threshold1_2=threshold1_2, threshold1_7=threshold1_7, tempAlarm1_11e=tempAlarm1_11e, alarm4=alarm4, switchClear8_11e=switchClear8_11e, channel1=channel1, switch_label_7=switch_label_7, sensor4_6_label=sensor4_6_label, sensor3_6_label=sensor3_6_label, switch_label_8=switch_label_8, sensor3_2=sensor3_2, switchClear4_11e=switchClear4_11e, switchClear2_11e=switchClear2_11e, switch_label_1=switch_label_1, threshold2_4=threshold2_4, sensor2_2=sensor2_2, threshold3_3=threshold3_3, threshold4_4=threshold4_4, switchAlarm4_11e=switchAlarm4_11e, sensor2_6_label=sensor2_6_label, sensor1_4=sensor1_4, threshold1_4=threshold1_4, humidityAlarm2_11e=humidityAlarm2_11e, alarmMessage3=alarmMessage3, threshold3_4=threshold3_4, channels2=channels2, sensor2_1=sensor2_1, humidityAlarm1_11e=humidityAlarm1_11e, sensor1_1=sensor1_1, sensor1_8=sensor1_8, thresholds=thresholds, tempClear2_11e=tempClear2_11e, threshold1_8=threshold1_8, threshold4_3=threshold4_3, sensor4_1=sensor4_1, products=products, sensor2_5=sensor2_5, switchAlarm6_11e=switchAlarm6_11e, sensor4_4=sensor4_4, alarmMessage2=alarmMessage2, humidityClear1_11e=humidityClear1_11e, channel3=channel3, switch_label_6=switch_label_6, switch_label_3=switch_label_3, channels3=channels3, sensor1_6=sensor1_6, room_alert_11E_SNMP_trap=room_alert_11E_SNMP_trap, alarmMessage1=alarmMessage1, humidityAlarm3_11e=humidityAlarm3_11e, sensor2_4=sensor2_4, sensor4_2=sensor4_2, switchAlarm3_11e=switchAlarm3_11e, avtech=avtech, sensor2_3=sensor2_3, sensor1_3=sensor1_3, traps=traps, threshold3_2=threshold3_2, channel4=channel4, channels1=channels1, tempAlarm2_11e=tempAlarm2_11e, sensor3_4=sensor3_4, sensor4_3=sensor4_3, threshold2_3=threshold2_3, switchAlarm8_11e=switchAlarm8_11e, sensor1_2=sensor1_2, threshold2_1=threshold2_1, roomalert11E=roomalert11E, switchAlarm5_11e=switchAlarm5_11e, sensor4_5=sensor4_5, sensor1_5=sensor1_5, threshold4_2=threshold4_2, switchClear1_11e=switchClear1_11e, switchAlarm7_11e=switchAlarm7_11e, switchClear5_11e=switchClear5_11e, channels4=channels4, sensor3_5=sensor3_5, threshold3_1=threshold3_1, switch_label_4=switch_label_4, alarm3=alarm3, switch_label_5=switch_label_5, sensor1_7=sensor1_7, channel2=channel2, threshold1_6=threshold1_6, threshold1_3=threshold1_3, alarm1=alarm1, threshold4_1=threshold4_1, threshold1_1=threshold1_1, sensors=sensors, switchClear7_11e=switchClear7_11e, tempAlarm3_11e=tempAlarm3_11e, alarmMessage4=alarmMessage4, sensor3_1=sensor3_1, switch_label_2=switch_label_2, humidityClear2_11e=humidityClear2_11e, switchAlarm1_11e=switchAlarm1_11e, threshold2_2=threshold2_2, sensor3_3=sensor3_3, switchAlarm2_11e=switchAlarm2_11e, switchClear6_11e=switchClear6_11e, humidityClear3_11e=humidityClear3_11e, threshold1_5=threshold1_5, switchClear3_11e=switchClear3_11e)
