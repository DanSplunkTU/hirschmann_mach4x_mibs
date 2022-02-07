#
# PySNMP MIB module AT-FIBER-MONITORING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-FIBER-MONITORING-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:17 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SYSINFO-MIB", "sysinfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, Counter64, Gauge32, MibIdentifier, ModuleIdentity, IpAddress, TimeTicks, NotificationType, ObjectIdentity, Unsigned32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Counter64", "Gauge32", "MibIdentifier", "ModuleIdentity", "IpAddress", "TimeTicks", "NotificationType", "ObjectIdentity", "Unsigned32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atFiberMon = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27))
atFiberMon.setRevisions(('2015-09-08 00:00',))
if mibBuilder.loadTexts: atFiberMon.setLastUpdated('201509080000Z')
if mibBuilder.loadTexts: atFiberMon.setOrganization('Allied Telesis, Inc')
atFiberMonNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 0))
atFiberMonAlarmSetNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 0, 1)).setObjects(("AT-FIBER-MONITORING-MIB", "atFiberMonIfindex"), ("AT-FIBER-MONITORING-MIB", "atFiberMonChannel"), ("AT-FIBER-MONITORING-MIB", "atFiberMonIfname"), ("AT-FIBER-MONITORING-MIB", "atFiberMonReading"), ("AT-FIBER-MONITORING-MIB", "atFiberMonThreshold"))
if mibBuilder.loadTexts: atFiberMonAlarmSetNotify.setStatus('current')
atFiberMonAlarmClearedNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 0, 2)).setObjects(("AT-FIBER-MONITORING-MIB", "atFiberMonIfindex"), ("AT-FIBER-MONITORING-MIB", "atFiberMonChannel"), ("AT-FIBER-MONITORING-MIB", "atFiberMonIfname"), ("AT-FIBER-MONITORING-MIB", "atFiberMonReading"), ("AT-FIBER-MONITORING-MIB", "atFiberMonThreshold"))
if mibBuilder.loadTexts: atFiberMonAlarmClearedNotify.setStatus('current')
atFiberMonTrapVariable = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 1))
atFiberMonReading = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: atFiberMonReading.setStatus('current')
atFiberMonConfigTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2), )
if mibBuilder.loadTexts: atFiberMonConfigTable.setStatus('current')
atFiberMonConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1), ).setIndexNames((0, "AT-FIBER-MONITORING-MIB", "atFiberMonIfname"))
if mibBuilder.loadTexts: atFiberMonConfigEntry.setStatus('current')
atFiberMonIfname = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFiberMonIfname.setStatus('current')
atFiberMonEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFiberMonEnable.setStatus('current')
atFiberMonInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFiberMonInterval.setStatus('current')
atFiberMonSensitivity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFiberMonSensitivity.setStatus('current')
atFiberMonBaseline = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 5), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFiberMonBaseline.setStatus('current')
atFiberMonAlarmAction = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("logOnly", 1), ("sendTrap", 2), ("shutdown", 3), ("sendtrapAndShutdown", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atFiberMonAlarmAction.setStatus('current')
atFiberMonStateTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3), )
if mibBuilder.loadTexts: atFiberMonStateTable.setStatus('current')
atFiberMonStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1), ).setIndexNames((0, "AT-FIBER-MONITORING-MIB", "atFiberMonIfindex"), (0, "AT-FIBER-MONITORING-MIB", "atFiberMonChannel"))
if mibBuilder.loadTexts: atFiberMonStateEntry.setStatus('current')
atFiberMonIfindex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFiberMonIfindex.setStatus('current')
atFiberMonChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFiberMonChannel.setStatus('current')
atFiberMonlIfDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFiberMonlIfDescription.setStatus('current')
atFiberMonActualBaseline = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFiberMonActualBaseline.setStatus('current')
atFiberMonThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFiberMonThreshold.setStatus('current')
atFiberMonReadingHistory = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFiberMonReadingHistory.setStatus('current')
atFiberMonMinReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFiberMonMinReading.setStatus('current')
atFiberMonMaxReading = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 27, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atFiberMonMaxReading.setStatus('current')
mibBuilder.exportSymbols("AT-FIBER-MONITORING-MIB", atFiberMonReadingHistory=atFiberMonReadingHistory, atFiberMonAlarmClearedNotify=atFiberMonAlarmClearedNotify, atFiberMonTrapVariable=atFiberMonTrapVariable, atFiberMonlIfDescription=atFiberMonlIfDescription, atFiberMonNotifications=atFiberMonNotifications, atFiberMonAlarmAction=atFiberMonAlarmAction, atFiberMonAlarmSetNotify=atFiberMonAlarmSetNotify, atFiberMonInterval=atFiberMonInterval, atFiberMonBaseline=atFiberMonBaseline, atFiberMonThreshold=atFiberMonThreshold, atFiberMonMinReading=atFiberMonMinReading, atFiberMonStateTable=atFiberMonStateTable, atFiberMonStateEntry=atFiberMonStateEntry, atFiberMonSensitivity=atFiberMonSensitivity, atFiberMonEnable=atFiberMonEnable, atFiberMon=atFiberMon, atFiberMonChannel=atFiberMonChannel, atFiberMonConfigTable=atFiberMonConfigTable, atFiberMonActualBaseline=atFiberMonActualBaseline, atFiberMonIfindex=atFiberMonIfindex, atFiberMonIfname=atFiberMonIfname, atFiberMonConfigEntry=atFiberMonConfigEntry, PYSNMP_MODULE_ID=atFiberMon, atFiberMonMaxReading=atFiberMonMaxReading, atFiberMonReading=atFiberMonReading)
