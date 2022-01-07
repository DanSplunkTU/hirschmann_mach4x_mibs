#
# PySNMP MIB module SIAE-PMG828-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-PMG828-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:37:55 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Gauge32, Unsigned32, IpAddress, Counter64, Bits, NotificationType, ObjectIdentity, Counter32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Gauge32", "Unsigned32", "IpAddress", "Counter64", "Bits", "NotificationType", "ObjectIdentity", "Counter32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
pmG828 = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 11))
pmG828.setRevisions(('2014-10-07 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: pmG828.setLastUpdated('201410070000Z')
if mibBuilder.loadTexts: pmG828.setOrganization('SIAE MICROELETTRONICA spa')
pmG828MibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828MibVersion.setStatus('current')
pmG828CounterTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2), )
if mibBuilder.loadTexts: pmG828CounterTable.setStatus('current')
pmG828CounterRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1), ).setIndexNames((0, "SIAE-PMG828-MIB", "pmG828TPointId"), (0, "SIAE-PMG828-MIB", "pmG828CounterBlockId"))
if mibBuilder.loadTexts: pmG828CounterRecord.setStatus('current')
pmG828TPointId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TPointId.setStatus('current')
pmG828CounterBlockId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828CounterBlockId.setStatus('current')
pmG828CounterBlockType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("daily", 1), ("fifteenMin", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828CounterBlockType.setStatus('current')
pmG828CounterBlockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("meaningless", 1), ("meaningfull", 2), ("incomplete", 3), ("dummy", 4), ("lost", 5), ("restarted", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828CounterBlockStatus.setStatus('current')
pmG828CounterTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828CounterTimeStamp.setStatus('current')
pmG828BBECounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828BBECounter.setStatus('current')
pmG828ESCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828ESCounter.setStatus('current')
pmG828SESCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828SESCounter.setStatus('current')
pmG828UASCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828UASCounter.setStatus('current')
pmG828SEPCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828SEPCounter.setStatus('current')
pmG828TpClassTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3), )
if mibBuilder.loadTexts: pmG828TpClassTable.setStatus('current')
pmG828TpClassRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1), ).setIndexNames((0, "SIAE-PMG828-MIB", "pmG828TpClassId"))
if mibBuilder.loadTexts: pmG828TpClassRecord.setStatus('current')
pmG828TpClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClassId.setStatus('current')
pmG828TpClassStartStop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClassStartStop.setStatus('current')
pmG828TpClassLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClassLabel.setStatus('current')
pmG828TpClassTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClassTimeStamp.setStatus('current')
pmG828TpClass15MEsAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass15MEsAlarm.setStatus('current')
pmG828TpClass15MSesAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass15MSesAlarm.setStatus('current')
pmG828TpClass15MSepAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass15MSepAlarm.setStatus('current')
pmG828TpClass24HEsAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass24HEsAlarm.setStatus('current')
pmG828TpClass24HSesAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass24HSesAlarm.setStatus('current')
pmG828TpClass24HSepAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass24HSepAlarm.setStatus('current')
pmG828TpClassUasAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 11), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClassUasAlarm.setStatus('current')
pmG828TpClass15MEsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass15MEsThreshold.setStatus('current')
pmG828TpClass15MSesThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass15MSesThreshold.setStatus('current')
pmG828TpClass15MSepThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass15MSepThreshold.setStatus('current')
pmG828TpClass24HEsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass24HEsThreshold.setStatus('current')
pmG828TpClass24HSesThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 16), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass24HSesThreshold.setStatus('current')
pmG828TpClass24HSepThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass24HSepThreshold.setStatus('current')
pmG828TpClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClassRowStatus.setStatus('current')
pmG828TpMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4), )
if mibBuilder.loadTexts: pmG828TpMaintTable.setStatus('current')
pmG828TpMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4, 1), ).setIndexNames((0, "SIAE-PMG828-MIB", "pmG828TpClassId"))
if mibBuilder.loadTexts: pmG828TpMaintRecord.setStatus('current')
pmG828TpMaintCounterClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpMaintCounterClear.setStatus('current')
pmG828TpMaintAlarmClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpMaintAlarmClear.setStatus('current')
pmG828NSesSetUAS = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 5), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828NSesSetUAS.setStatus('current')
pmG828NSesResetUAS = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 6), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828NSesResetUAS.setStatus('current')
pmG828TpClass15MEsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass15MEsAlarmSeverityCode.setStatus('current')
pmG828TpClass15MSesAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass15MSesAlarmSeverityCode.setStatus('current')
pmG828TpClass24HEsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 9), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass24HEsAlarmSeverityCode.setStatus('current')
pmG828TpClass24HSesAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 10), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass24HSesAlarmSeverityCode.setStatus('current')
pmG828TpClassUASAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 11), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClassUASAlarmSeverityCode.setStatus('current')
pmG828TpClass15MSepAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 12), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass15MSepAlarmSeverityCode.setStatus('current')
pmG828TpClass24HSepAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 13), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass24HSepAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-PMG828-MIB", pmG828TpClassUasAlarm=pmG828TpClassUasAlarm, pmG828ESCounter=pmG828ESCounter, pmG828TpClass24HSesAlarm=pmG828TpClass24HSesAlarm, pmG828TpClassRecord=pmG828TpClassRecord, pmG828TpClass15MEsAlarm=pmG828TpClass15MEsAlarm, pmG828TpClass24HSepAlarm=pmG828TpClass24HSepAlarm, pmG828TpClass15MSepThreshold=pmG828TpClass15MSepThreshold, pmG828TpClass24HSepAlarmSeverityCode=pmG828TpClass24HSepAlarmSeverityCode, pmG828TpClassTable=pmG828TpClassTable, pmG828NSesResetUAS=pmG828NSesResetUAS, pmG828TpMaintTable=pmG828TpMaintTable, pmG828NSesSetUAS=pmG828NSesSetUAS, pmG828=pmG828, pmG828CounterTimeStamp=pmG828CounterTimeStamp, pmG828TpClassLabel=pmG828TpClassLabel, pmG828TpClass24HSesThreshold=pmG828TpClass24HSesThreshold, pmG828CounterRecord=pmG828CounterRecord, pmG828CounterBlockType=pmG828CounterBlockType, pmG828CounterBlockStatus=pmG828CounterBlockStatus, pmG828TpClass15MSesAlarmSeverityCode=pmG828TpClass15MSesAlarmSeverityCode, PYSNMP_MODULE_ID=pmG828, pmG828TpClass24HEsAlarmSeverityCode=pmG828TpClass24HEsAlarmSeverityCode, pmG828CounterTable=pmG828CounterTable, pmG828MibVersion=pmG828MibVersion, pmG828TpMaintCounterClear=pmG828TpMaintCounterClear, pmG828TpClass24HSepThreshold=pmG828TpClass24HSepThreshold, pmG828CounterBlockId=pmG828CounterBlockId, pmG828TpClassTimeStamp=pmG828TpClassTimeStamp, pmG828TpClass15MEsThreshold=pmG828TpClass15MEsThreshold, pmG828TpClass15MSesAlarm=pmG828TpClass15MSesAlarm, pmG828SEPCounter=pmG828SEPCounter, pmG828TpClassId=pmG828TpClassId, pmG828TpClass15MSepAlarmSeverityCode=pmG828TpClass15MSepAlarmSeverityCode, pmG828TpClassStartStop=pmG828TpClassStartStop, pmG828TpClassRowStatus=pmG828TpClassRowStatus, pmG828TpClass24HEsAlarm=pmG828TpClass24HEsAlarm, pmG828TpClass24HSesAlarmSeverityCode=pmG828TpClass24HSesAlarmSeverityCode, pmG828TpClassUASAlarmSeverityCode=pmG828TpClassUASAlarmSeverityCode, pmG828TpClass15MSepAlarm=pmG828TpClass15MSepAlarm, pmG828TpMaintRecord=pmG828TpMaintRecord, pmG828BBECounter=pmG828BBECounter, pmG828TpClass15MEsAlarmSeverityCode=pmG828TpClass15MEsAlarmSeverityCode, pmG828TpMaintAlarmClear=pmG828TpMaintAlarmClear, pmG828TpClass24HEsThreshold=pmG828TpClass24HEsThreshold, pmG828TPointId=pmG828TPointId, pmG828UASCounter=pmG828UASCounter, pmG828TpClass15MSesThreshold=pmG828TpClass15MSesThreshold, pmG828SESCounter=pmG828SESCounter)
