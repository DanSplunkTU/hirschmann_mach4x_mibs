#
# PySNMP MIB module SIAE-PMRXPWR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-PMRXPWR-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:44:13 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
AlarmSeverityCode, AlarmStatus = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Gauge32, Unsigned32, ModuleIdentity, iso, IpAddress, Counter32, NotificationType, MibIdentifier, Integer32, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Gauge32", "Unsigned32", "ModuleIdentity", "iso", "IpAddress", "Counter32", "NotificationType", "MibIdentifier", "Integer32", "Counter64", "ObjectIdentity")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
pmRxPwr = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 12))
pmRxPwr.setRevisions(('2014-10-07 00:00', '2014-05-13 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pmRxPwr.setRevisionsDescriptions(('Changed MAX-ACCESS caluse of some object of pmRxPwrTpClassTable\n             from read-write to read-create\n            ', 'Changed DEFVAL clause of pmRxPwrTpClassRltXThreshold.\n            ', 'Improved description of pmRxPwrMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: pmRxPwr.setLastUpdated('201410070000Z')
if mibBuilder.loadTexts: pmRxPwr.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: pmRxPwr.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: pmRxPwr.setDescription('Performance Monitoring on Received (RX) RF Power.\n            ')
pmRxPwrMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrMibVersion.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
pmRxPwrCounterTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2), )
if mibBuilder.loadTexts: pmRxPwrCounterTable.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrCounterTable.setDescription('Table with PmRxPwr records: one record for 1+0 configuration and two\n             record for 1+1 configuration.')
pmRxPwrCounterRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1), ).setIndexNames((0, "SIAE-PMRXPWR-MIB", "pmRxPwrBranchId"), (0, "SIAE-PMRXPWR-MIB", "pmRxPwrCounterBlockId"))
if mibBuilder.loadTexts: pmRxPwrCounterRecord.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrCounterRecord.setDescription('PmRxPwrCounter record.')
pmRxPwrBranchId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrBranchId.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrBranchId.setDescription('This object identifies the Radio Branch')
pmRxPwrCounterBlockId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrCounterBlockId.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrCounterBlockId.setDescription('This object identifies  the counters block and the counter type\n             according to the following code:\n             1  Current Daily counters\n             2  Daily counters (Day before counters)\n             3  Current 15 minutes counters\n             4  15 minutes counters N. 1 (The most recent 15 minutes counters)\n                ..............................................\n             n  15 minutes counters N. n\n             20 15 minutes counters N.16(The oldest 15 min. counters 4 hours before).')
pmRxPwrCounterBlockType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("daily", 1), ("fifteenMin", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrCounterBlockType.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrCounterBlockType.setDescription('The type of the counter block.')
pmRxPwrCounterBlockStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("meaningless", 1), ("meaningfull", 2), ("incomplete", 3), ("dummy", 4), ("lost", 5), ("restarted", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrCounterBlockStatus.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrCounterBlockStatus.setDescription('Status of the block counter.')
pmRxPwrCounterTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrCounterTimeStamp.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrCounterTimeStamp.setDescription('The object is the time when the performance record is closed reported\n             as the second number since 1-Gen-1970.')
pmRxPwrRlts1Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrRlts1Counter.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrRlts1Counter.setDescription('Number of seconds when the Received power is less than the threshold 1.')
pmRxPwrRlts2Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrRlts2Counter.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrRlts2Counter.setDescription('Number of seconds when the Received power is less than the threshold 2')
pmRxPwrRlts3Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrRlts3Counter.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrRlts3Counter.setDescription('Number of seconds when the Received power is less than the threshold 3')
pmRxPwrRlts4Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrRlts4Counter.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrRlts4Counter.setDescription('Number of seconds when the Received power is less than the threshold 4')
pmRxPwrRlts5Counter = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrRlts5Counter.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrRlts5Counter.setDescription('Number of seconds when the Received power is less than the threshold 5')
pmRxPwrTMMax = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTMMax.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTMMax.setDescription('Maximum Power Received Level Tide Mark.')
pmRxPwrTMMin = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTMMin.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTMMin.setDescription('Minimum Power Received Level Tide Mark.')
pmRxPwrAverageRxLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrAverageRxLevel.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrAverageRxLevel.setDescription(' Power Received Level  (Average value)')
pmRxPwrTpClassTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3), )
if mibBuilder.loadTexts: pmRxPwrTpClassTable.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassTable.setDescription('Table with PmRxPwrTpClass records: one record for 1+0 configuration\n             and two record for 1+1 configuration.')
pmRxPwrTpClassRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1), ).setIndexNames((0, "SIAE-PMRXPWR-MIB", "pmRxPwrTpClassBranchId"))
if mibBuilder.loadTexts: pmRxPwrTpClassRecord.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassRecord.setDescription('PmRxPwrTpClass record.')
pmRxPwrTpClassBranchId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClassBranchId.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassBranchId.setDescription('This object identifies the Radio Branch')
pmRxPwrTpClassStartStop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassStartStop.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassStartStop.setDescription('This object is used to start and to stop the Perfomance Monitoring\n             counter evaluation.')
pmRxPwrTpClassLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClassLabel.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassLabel.setDescription('ASCII string used to identify the Tp class:\n             pmRxPwrTpClassBranchId = 1 label = Radio 1\n             pmRxPwrTpClassBranchId = 2 label = Radio 2.')
pmRxPwrTpClassTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClassTimeStamp.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassTimeStamp.setDescription('The object is the time when the performance record is closed reported\n             as the second number since 1/1/70.')
pmRxPwrTpClass15MRlts1Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 5), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts1Alarm.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts1Alarm.setDescription('15 minutes Rlts1 threshold cross alarm with associated severity.')
pmRxPwrTpClass15MRlts2Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 6), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts2Alarm.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts2Alarm.setDescription('15 minutes Rlts2 threshold cross alarm with associated severity.')
pmRxPwrTpClass15MRlts3Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts3Alarm.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts3Alarm.setDescription('15 minutes Rlts3 threshold cross alarm with associated severity.')
pmRxPwrTpClass15MRlts4Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts4Alarm.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts4Alarm.setDescription('15 minutes Rlts4 threshold cross alarm with associated severity.')
pmRxPwrTpClass15MRlts5Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts5Alarm.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts5Alarm.setDescription('15 minutes Rlts5 threshold cross alarm with associated severity.')
pmRxPwrTpClass24HRlts1Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts1Alarm.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts1Alarm.setDescription('Daily Rlts1 threshold cross alarm with associated severity.')
pmRxPwrTpClass24HRlts2Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 11), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts2Alarm.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts2Alarm.setDescription('Daily Rlts2 threshold cross alarm with associated severity.')
pmRxPwrTpClass24HRlts3Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 12), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts3Alarm.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts3Alarm.setDescription('Daily Rlts3 threshold cross alarm with associated severity.')
pmRxPwrTpClass24HRlts4Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 13), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts4Alarm.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts4Alarm.setDescription('Daily Rlts4 threshold cross alarm with associated severity.')
pmRxPwrTpClass24HRlts5Alarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 14), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts5Alarm.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts5Alarm.setDescription('Daily Rlts5 threshold cross alarm with associated severity.')
pmRxPwrTpClassRlt1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-40)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRlt1Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassRlt1Threshold.setDescription('Received Power Level Threshold 1 (dBm value); range -100 to -20')
pmRxPwrTpClassRlt2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-50)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRlt2Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassRlt2Threshold.setDescription('Received Power Level Threshold 2 (dBm value); range -100 to -20')
pmRxPwrTpClassRlt3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-60)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRlt3Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassRlt3Threshold.setDescription('Received Power Level Threshold 3 (dBm value); range -100 to -20')
pmRxPwrTpClassRlt4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 18), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-70)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRlt4Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassRlt4Threshold.setDescription('Received Power Level Threshold 4 (dBm value); range -100 to -20')
pmRxPwrTpClassRlt5Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 19), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-100, -20)).clone(-80)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRlt5Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassRlt5Threshold.setDescription('Received Power Level Threshold 5 (dBm value); range -100 to -20')
pmRxPwrTpClass15MRlts1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 20), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts1Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts1Threshold.setDescription('Number of seconds within 15 minutes to set\n             pmRxPwrTpClass15MRlts1Alarm (zero value disables the alarm).')
pmRxPwrTpClass15MRlts2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 21), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts2Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts2Threshold.setDescription('Number of seconds within 15 minutes to set\n             pmRxPwrTpClass15MRlts2Alarm (zero value disables the alarm).')
pmRxPwrTpClass15MRlts3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 22), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts3Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts3Threshold.setDescription('Number of seconds within 15 minutes to set\n             pmRxPwrTpClass15MRlts3Alarm (zero value disables the alarm).')
pmRxPwrTpClass15MRlts4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 23), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts4Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts4Threshold.setDescription('Number of seconds within 15 minutes to set\n             pmRxPwrTpClass15MRlts4Alarm (zero value disables the alarm).')
pmRxPwrTpClass15MRlts5Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 24), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts5Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRlts5Threshold.setDescription('Number of seconds within 15 minutes to set\n             pmRxPwrTpClass15MRlts5Alarm (zero value disables the alarm).')
pmRxPwrTpClass24HRlts1Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 25), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts1Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts1Threshold.setDescription('Number of seconds within a day to set pmRxPwrTpClass24HRlts1Alarm\n             (zero value disables the alarm).')
pmRxPwrTpClass24HRlts2Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 26), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts2Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts2Threshold.setDescription('Number of seconds within a day to set pmRxPwrTpClass24HRlts2Alarm\n             (zero value disables the alarm).')
pmRxPwrTpClass24HRlts3Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 27), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts3Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts3Threshold.setDescription('Number of seconds within a day to set pmRxPwrTpClass24HRlts3Alarm\n             (zero value disables the alarm).')
pmRxPwrTpClass24HRlts4Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 28), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts4Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts4Threshold.setDescription('Number of seconds within a day to set pmRxPwrTpClass24HRlts4Alarm\n             (zero value disables the alarm).')
pmRxPwrTpClass24HRlts5Threshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 29), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts5Threshold.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRlts5Threshold.setDescription('Number of seconds within a day to set pmRxPwrTpClass24HRlts5Alarm\n             (zero value disables the alarm).')
pmRxPwrTpClassRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 3, 1, 30), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pmRxPwrTpClassRowStatus.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClassRowStatus.setDescription('Status of this row of pmRxPwrTpClass.\n            ')
pmRxPwrTpMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4), )
if mibBuilder.loadTexts: pmRxPwrTpMaintTable.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpMaintTable.setDescription('Table with Command for maintenance of Termination Point.\n             Objects in this table is not persistent. An Instance of this \n             table is created on creation of pmRxPwrTpClassTable')
pmRxPwrTpMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4, 1), ).setIndexNames((0, "SIAE-PMRXPWR-MIB", "pmRxPwrTpClassBranchId"))
if mibBuilder.loadTexts: pmRxPwrTpMaintRecord.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpMaintRecord.setDescription('PmG828 Termination Point Maintenance record.')
pmRxPwrTpMaintCounterClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmRxPwrTpMaintCounterClear.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpMaintCounterClear.setDescription('This object is used to clear the Perfomance Monitoring counters.')
pmRxPwrTpMaintAlarmClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmRxPwrTpMaintAlarmClear.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpMaintAlarmClear.setDescription('This object is used to clear the Perfomance Monitoring threshold cross alarms.')
pmRxPwrTpClass15MRltsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmRxPwrTpClass15MRltsAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass15MRltsAlarmSeverityCode.setDescription('Define the severity associated to the pmRxPwrTpClass15MRltsAlarm and\n             enables/disables the trap generation on status change event.')
pmRxPwrTpClass24HRltsAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 12, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pmRxPwrTpClass24HRltsAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: pmRxPwrTpClass24HRltsAlarmSeverityCode.setDescription('Define the severity associated to the pmRxPwrTpClass24HRltsAlarm and\n             enables/disables the trap generation on status change event.')
mibBuilder.exportSymbols("SIAE-PMRXPWR-MIB", pmRxPwrTpClass15MRlts2Alarm=pmRxPwrTpClass15MRlts2Alarm, pmRxPwrTpClassRlt1Threshold=pmRxPwrTpClassRlt1Threshold, pmRxPwrTpClass15MRlts4Alarm=pmRxPwrTpClass15MRlts4Alarm, pmRxPwrTpClass24HRlts3Alarm=pmRxPwrTpClass24HRlts3Alarm, pmRxPwrRlts1Counter=pmRxPwrRlts1Counter, pmRxPwrTMMax=pmRxPwrTMMax, pmRxPwrTpClass15MRlts5Threshold=pmRxPwrTpClass15MRlts5Threshold, pmRxPwrTpClassRlt2Threshold=pmRxPwrTpClassRlt2Threshold, pmRxPwrCounterTable=pmRxPwrCounterTable, pmRxPwrTpClass24HRlts1Threshold=pmRxPwrTpClass24HRlts1Threshold, pmRxPwrTpClass24HRlts3Threshold=pmRxPwrTpClass24HRlts3Threshold, pmRxPwrMibVersion=pmRxPwrMibVersion, pmRxPwrTpClass15MRlts4Threshold=pmRxPwrTpClass15MRlts4Threshold, pmRxPwrTpClass24HRlts4Threshold=pmRxPwrTpClass24HRlts4Threshold, pmRxPwrBranchId=pmRxPwrBranchId, pmRxPwrRlts5Counter=pmRxPwrRlts5Counter, pmRxPwrRlts3Counter=pmRxPwrRlts3Counter, pmRxPwrTpClassRowStatus=pmRxPwrTpClassRowStatus, pmRxPwrTpClass15MRlts3Alarm=pmRxPwrTpClass15MRlts3Alarm, pmRxPwrTpClass15MRlts3Threshold=pmRxPwrTpClass15MRlts3Threshold, pmRxPwrTpClassBranchId=pmRxPwrTpClassBranchId, pmRxPwrRlts4Counter=pmRxPwrRlts4Counter, pmRxPwrTpClass15MRlts1Threshold=pmRxPwrTpClass15MRlts1Threshold, pmRxPwrTpClass24HRlts5Alarm=pmRxPwrTpClass24HRlts5Alarm, pmRxPwrTpMaintRecord=pmRxPwrTpMaintRecord, pmRxPwrTpClass15MRlts1Alarm=pmRxPwrTpClass15MRlts1Alarm, pmRxPwrRlts2Counter=pmRxPwrRlts2Counter, pmRxPwrTpMaintTable=pmRxPwrTpMaintTable, pmRxPwrTpMaintCounterClear=pmRxPwrTpMaintCounterClear, pmRxPwrCounterBlockType=pmRxPwrCounterBlockType, pmRxPwrCounterRecord=pmRxPwrCounterRecord, pmRxPwrAverageRxLevel=pmRxPwrAverageRxLevel, PYSNMP_MODULE_ID=pmRxPwr, pmRxPwrTpClassRecord=pmRxPwrTpClassRecord, pmRxPwrTpClassStartStop=pmRxPwrTpClassStartStop, pmRxPwrTpClassLabel=pmRxPwrTpClassLabel, pmRxPwrTpClass24HRlts2Threshold=pmRxPwrTpClass24HRlts2Threshold, pmRxPwrTpClass24HRlts5Threshold=pmRxPwrTpClass24HRlts5Threshold, pmRxPwrTpClass24HRlts2Alarm=pmRxPwrTpClass24HRlts2Alarm, pmRxPwrTpClass24HRlts4Alarm=pmRxPwrTpClass24HRlts4Alarm, pmRxPwrTpClass15MRlts5Alarm=pmRxPwrTpClass15MRlts5Alarm, pmRxPwrTpClassRlt4Threshold=pmRxPwrTpClassRlt4Threshold, pmRxPwrTMMin=pmRxPwrTMMin, pmRxPwrCounterBlockStatus=pmRxPwrCounterBlockStatus, pmRxPwrCounterBlockId=pmRxPwrCounterBlockId, pmRxPwr=pmRxPwr, pmRxPwrTpClass15MRlts2Threshold=pmRxPwrTpClass15MRlts2Threshold, pmRxPwrTpClassTable=pmRxPwrTpClassTable, pmRxPwrTpClass24HRlts1Alarm=pmRxPwrTpClass24HRlts1Alarm, pmRxPwrTpClassRlt3Threshold=pmRxPwrTpClassRlt3Threshold, pmRxPwrTpMaintAlarmClear=pmRxPwrTpMaintAlarmClear, pmRxPwrTpClassTimeStamp=pmRxPwrTpClassTimeStamp, pmRxPwrTpClass15MRltsAlarmSeverityCode=pmRxPwrTpClass15MRltsAlarmSeverityCode, pmRxPwrTpClass24HRltsAlarmSeverityCode=pmRxPwrTpClass24HRltsAlarmSeverityCode, pmRxPwrCounterTimeStamp=pmRxPwrCounterTimeStamp, pmRxPwrTpClassRlt5Threshold=pmRxPwrTpClassRlt5Threshold)
