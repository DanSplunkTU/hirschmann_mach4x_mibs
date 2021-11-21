#
# PySNMP MIB module SIAE-PMG828-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-PMG828-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:48:51 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, MibIdentifier, iso, ModuleIdentity, TimeTicks, NotificationType, Gauge32, Unsigned32, ObjectIdentity, Bits, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "MibIdentifier", "iso", "ModuleIdentity", "TimeTicks", "NotificationType", "Gauge32", "Unsigned32", "ObjectIdentity", "Bits", "IpAddress", "Integer32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
pmG828 = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 11))
pmG828.setRevisions(('2014-10-07 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pmG828.setRevisionsDescriptions(('Changed MAX-ACCESS caluse of some object of pmG828TpClassTable\n             from read-write to read-create\n            ', 'Improved description of pmG828MibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: pmG828.setLastUpdated('201410070000Z')
if mibBuilder.loadTexts: pmG828.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: pmG828.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: pmG828.setDescription('Perforfamce Monitoring according to ITU-T G.829 for Radio Link\n             and E1 Tributaries\n             ')
pmG828MibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828MibVersion.setStatus('current')
if mibBuilder.loadTexts: pmG828MibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
pmG828CounterTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2), )
if mibBuilder.loadTexts: pmG828CounterTable.setStatus('current')
if mibBuilder.loadTexts: pmG828CounterTable.setDescription('Table with PmG828 records: one record for 1+0 configuration and two\n             record for 1+1 configuration.')
pmG828CounterRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1), ).setIndexNames((0, "SIAE-PMG828-MIB", "pmG828TPointId"), (0, "SIAE-PMG828-MIB", "pmG828CounterBlockId"))
if mibBuilder.loadTexts: pmG828CounterRecord.setStatus('current')
if mibBuilder.loadTexts: pmG828CounterRecord.setDescription('PmG828Counter record.')
pmG828TPointId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TPointId.setStatus('current')
if mibBuilder.loadTexts: pmG828TPointId.setDescription('This object identifies the Termination Point.')
pmG828CounterBlockId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828CounterBlockId.setStatus('current')
if mibBuilder.loadTexts: pmG828CounterBlockId.setDescription('This object identifies the counters block and the counter type\n             according to the following code:\n              1  Current Daily counters\n              2  Daily counters (Day before counters)\n              3  Current 15 minutes counters\n              4  15 minutes counters N. 1 (The most recent 15 minutes counters)\n                  ..............................................\n              n  15 minutes counters N. n\n              20 15 minutes counters N.16(The oldest 15 min.counters 4 hours before).')
pmG828CounterBlockType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("daily", 1), ("fifteenMin", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828CounterBlockType.setStatus('current')
if mibBuilder.loadTexts: pmG828CounterBlockType.setDescription('The type of the counter block.')
pmG828CounterBlockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("meaningless", 1), ("meaningfull", 2), ("incomplete", 3), ("dummy", 4), ("lost", 5), ("restarted", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828CounterBlockStatus.setStatus('current')
if mibBuilder.loadTexts: pmG828CounterBlockStatus.setDescription('Status of the block counter.')
pmG828CounterTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828CounterTimeStamp.setStatus('current')
if mibBuilder.loadTexts: pmG828CounterTimeStamp.setDescription('The object is the time when the performance record is closed reported\n             as the second number since 1-Gen-1970.')
pmG828BBECounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828BBECounter.setStatus('current')
if mibBuilder.loadTexts: pmG828BBECounter.setDescription('G828 BBE counter.')
pmG828ESCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828ESCounter.setStatus('current')
if mibBuilder.loadTexts: pmG828ESCounter.setDescription('G828 Es counter.')
pmG828SESCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828SESCounter.setStatus('current')
if mibBuilder.loadTexts: pmG828SESCounter.setDescription('G828 SES counter.')
pmG828UASCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828UASCounter.setStatus('current')
if mibBuilder.loadTexts: pmG828UASCounter.setDescription('G828 UAS counter.')
pmG828SEPCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828SEPCounter.setStatus('current')
if mibBuilder.loadTexts: pmG828SEPCounter.setDescription('G828 SEP counter.')
pmG828TpClassTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3), )
if mibBuilder.loadTexts: pmG828TpClassTable.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClassTable.setDescription('Table with PmG828TpClass records: one record for 1+0 configuration and\n             two record for 1+1 configuration.')
pmG828TpClassRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1), ).setIndexNames((0, "SIAE-PMG828-MIB", "pmG828TpClassId"))
if mibBuilder.loadTexts: pmG828TpClassRecord.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClassRecord.setDescription('PmG828TpClass record.')
pmG828TpClassId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClassId.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClassId.setDescription('This object identifies the Termination Point.')
pmG828TpClassStartStop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClassStartStop.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClassStartStop.setDescription('This object is used to start and to stop the Perfomance Monitoring\n             counter evaluation.')
pmG828TpClassLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClassLabel.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClassLabel.setDescription('ASCII string used to identify  the Tp class:\n             for example:\n             pmG828TpClassBranchId = 1 label = Radio 1\n             pmG828TpClassBranchId = 2 label = Radio 2\n             pmG828TpClassBranchId = 3 label = Radio(switched)\n             pmG828TpClassBranchId = 4 label = Trib E1 line side\n             pmG828TpClassBranchId = 5 label = Trib E1 radio side.')
pmG828TpClassTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClassTimeStamp.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClassTimeStamp.setDescription('')
pmG828TpClass15MEsAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass15MEsAlarm.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass15MEsAlarm.setDescription('15 minutes ES threshold cross alarm with associated severity.')
pmG828TpClass15MSesAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass15MSesAlarm.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass15MSesAlarm.setDescription('15 minutes SES threshold cross alarm with associated severity.')
pmG828TpClass15MSepAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass15MSepAlarm.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass15MSepAlarm.setDescription('15 minutes SEP threshold cross alarm with associated severity.')
pmG828TpClass24HEsAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass24HEsAlarm.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass24HEsAlarm.setDescription('Daily ES threshold cross alarm with associated severity.')
pmG828TpClass24HSesAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass24HSesAlarm.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass24HSesAlarm.setDescription('Daily SES threshold cross alarm with associated severity.')
pmG828TpClass24HSepAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClass24HSepAlarm.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass24HSepAlarm.setDescription('Daily SEP threshold cross alarm with associated severity.')
pmG828TpClassUasAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 11), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmG828TpClassUasAlarm.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClassUasAlarm.setDescription('UAS alarm with associated severity.')
pmG828TpClass15MEsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 12), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass15MEsThreshold.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass15MEsThreshold.setDescription('Number of ES within 15 minutes to set pmG828TpClass15MEsAlarm\n             (zero value disables the alarm).')
pmG828TpClass15MSesThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 13), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass15MSesThreshold.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass15MSesThreshold.setDescription('Number of SES within 15 minutes to set pmG828TpClass15MSesAlarm\n             (zero value disables the alarm).')
pmG828TpClass15MSepThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 14), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass15MSepThreshold.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass15MSepThreshold.setDescription('Number of SEP within 15 minutes to set pmG828TpClass15MSepAlarm\n             (zero value disables the alarm).')
pmG828TpClass24HEsThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 15), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass24HEsThreshold.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass24HEsThreshold.setDescription('Number of ES within one day to set pmG828TpClass24HEsAlarm\n             (zero value disables the alarm).')
pmG828TpClass24HSesThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 16), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass24HSesThreshold.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass24HSesThreshold.setDescription('Number of SES within one day to set pmG828TpClass24HSesAlarm\n             (zero value disables the alarm).')
pmG828TpClass24HSepThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 17), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClass24HSepThreshold.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass24HSepThreshold.setDescription('Number of SEP within one day to set pmG828TpClass24HSepAlarm\n             (zero value disables the alarm).')
pmG828TpClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 3, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmG828TpClassRowStatus.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClassRowStatus.setDescription('Status of this row of pmRxPwrTpClass.\n            ')
pmG828TpMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4), )
if mibBuilder.loadTexts: pmG828TpMaintTable.setStatus('current')
if mibBuilder.loadTexts: pmG828TpMaintTable.setDescription('Table with Command for maintenance of Termination Point.\n             Objects in this table is not persistent. An Instance of this \n             table is created on creation of pmG828TpClassTable')
pmG828TpMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4, 1), ).setIndexNames((0, "SIAE-PMG828-MIB", "pmG828TpClassId"))
if mibBuilder.loadTexts: pmG828TpMaintRecord.setStatus('current')
if mibBuilder.loadTexts: pmG828TpMaintRecord.setDescription('PmG828 Termination Point Maintenance record.')
pmG828TpMaintCounterClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpMaintCounterClear.setStatus('current')
if mibBuilder.loadTexts: pmG828TpMaintCounterClear.setDescription('This object is used to clear the Perfomance Monitoring counters.')
pmG828TpMaintAlarmClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpMaintAlarmClear.setStatus('current')
if mibBuilder.loadTexts: pmG828TpMaintAlarmClear.setDescription('This object is used to clear the Perfomance Monitoring threshold cross alarms.')
pmG828NSesSetUAS = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 5), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828NSesSetUAS.setStatus('current')
if mibBuilder.loadTexts: pmG828NSesSetUAS.setDescription('Number of SES (according G.828) to set UAS.')
pmG828NSesResetUAS = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 6), Integer32().clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828NSesResetUAS.setStatus('current')
if mibBuilder.loadTexts: pmG828NSesResetUAS.setDescription('Number of seconds whitout errors (according G.828) to reset UAS.')
pmG828TpClass15MEsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass15MEsAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass15MEsAlarmSeverityCode.setDescription('Defines the severity associated to the pmG828TpClass15MEsAlarm and\n             enables/disables the trap generation on status change event.')
pmG828TpClass15MSesAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass15MSesAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass15MSesAlarmSeverityCode.setDescription('Define the severity associated to the pmG828TpClass15MSesAlarm and\n             enables/disables the trap generation on status change event.')
pmG828TpClass24HEsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 9), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass24HEsAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass24HEsAlarmSeverityCode.setDescription('Define the severity associated to the pmG828TpClass15MEsAlarm and\n             enables/disables the trap generation on status change event.')
pmG828TpClass24HSesAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 10), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass24HSesAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass24HSesAlarmSeverityCode.setDescription('Define the severity associated to the pmG828TpClass15MSesAlarm and\n             enables/disables the trap generation on status change event.')
pmG828TpClassUASAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 11), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClassUASAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClassUASAlarmSeverityCode.setDescription('Define the severity associated to the pmG828TpClassUASAlarm and\n             enables/disables the trap generation on status change event.')
pmG828TpClass15MSepAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 12), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass15MSepAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass15MSepAlarmSeverityCode.setDescription('Define the severity associated to the pmG828TpClass15MSepAlarm and\n             enables/disables the trap generation on status change event.')
pmG828TpClass24HSepAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 11, 13), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmG828TpClass24HSepAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmG828TpClass24HSepAlarmSeverityCode.setDescription('Define the severity associated to the pmG828TpClass24HSepAlarm and\n             enables/disables the trap generation on status change event.')
mibBuilder.exportSymbols("SIAE-PMG828-MIB", pmG828TPointId=pmG828TPointId, pmG828TpMaintCounterClear=pmG828TpMaintCounterClear, pmG828TpClassUASAlarmSeverityCode=pmG828TpClassUASAlarmSeverityCode, pmG828TpClassRecord=pmG828TpClassRecord, pmG828TpClass24HSepAlarmSeverityCode=pmG828TpClass24HSepAlarmSeverityCode, pmG828BBECounter=pmG828BBECounter, pmG828TpClass15MEsAlarmSeverityCode=pmG828TpClass15MEsAlarmSeverityCode, pmG828TpClassStartStop=pmG828TpClassStartStop, pmG828TpClass24HSesThreshold=pmG828TpClass24HSesThreshold, pmG828TpClass15MEsAlarm=pmG828TpClass15MEsAlarm, pmG828TpClass15MSesAlarmSeverityCode=pmG828TpClass15MSesAlarmSeverityCode, pmG828CounterTable=pmG828CounterTable, pmG828TpMaintRecord=pmG828TpMaintRecord, pmG828TpClass15MSepThreshold=pmG828TpClass15MSepThreshold, pmG828TpClass24HSesAlarmSeverityCode=pmG828TpClass24HSesAlarmSeverityCode, pmG828CounterTimeStamp=pmG828CounterTimeStamp, pmG828TpClassRowStatus=pmG828TpClassRowStatus, pmG828NSesResetUAS=pmG828NSesResetUAS, pmG828ESCounter=pmG828ESCounter, pmG828TpClass15MSesThreshold=pmG828TpClass15MSesThreshold, PYSNMP_MODULE_ID=pmG828, pmG828TpClass24HEsAlarm=pmG828TpClass24HEsAlarm, pmG828SESCounter=pmG828SESCounter, pmG828TpClass24HSepAlarm=pmG828TpClass24HSepAlarm, pmG828TpClass24HSepThreshold=pmG828TpClass24HSepThreshold, pmG828=pmG828, pmG828CounterBlockStatus=pmG828CounterBlockStatus, pmG828TpClass15MSesAlarm=pmG828TpClass15MSesAlarm, pmG828TpMaintAlarmClear=pmG828TpMaintAlarmClear, pmG828NSesSetUAS=pmG828NSesSetUAS, pmG828TpClassUasAlarm=pmG828TpClassUasAlarm, pmG828CounterBlockId=pmG828CounterBlockId, pmG828SEPCounter=pmG828SEPCounter, pmG828TpClassTable=pmG828TpClassTable, pmG828CounterBlockType=pmG828CounterBlockType, pmG828TpClassId=pmG828TpClassId, pmG828TpClass15MSepAlarmSeverityCode=pmG828TpClass15MSepAlarmSeverityCode, pmG828TpClass24HEsThreshold=pmG828TpClass24HEsThreshold, pmG828TpClass15MEsThreshold=pmG828TpClass15MEsThreshold, pmG828TpClassLabel=pmG828TpClassLabel, pmG828TpClass24HSesAlarm=pmG828TpClass24HSesAlarm, pmG828TpClass24HEsAlarmSeverityCode=pmG828TpClass24HEsAlarmSeverityCode, pmG828MibVersion=pmG828MibVersion, pmG828UASCounter=pmG828UASCounter, pmG828CounterRecord=pmG828CounterRecord, pmG828TpMaintTable=pmG828TpMaintTable, pmG828TpClass15MSepAlarm=pmG828TpClass15MSepAlarm, pmG828TpClassTimeStamp=pmG828TpClassTimeStamp)
