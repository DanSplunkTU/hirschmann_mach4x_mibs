#
# PySNMP MIB module SIAE-SYNC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SYNC-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:19:33 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndexOrZero, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "ifIndex")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, TimeTicks, Integer32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso, Bits, Counter32, Counter64, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "TimeTicks", "Integer32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso", "Bits", "Counter32", "Counter64", "Gauge32", "ModuleIdentity")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
sync = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 28))
sync.setRevisions(('2014-04-02 00:00', '2014-02-17 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sync.setRevisionsDescriptions(('MIB version 01.00.01\n             Added esmcTable.\n             Changed MAX-ACCESS clause from read-write to read-create in\n             tables with row status.\n             Changed STATUS clause of timingSinkEthPortRole from current to \n             deprecated\n            ', 'MIB version 01.00.01\n             Added timingSinkSelectorTable\n            ', 'Improved description of syncMibVersion\n             Removed TimeTicks from IMPORTS list\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: sync.setLastUpdated('201404020000Z')
if mibBuilder.loadTexts: sync.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: sync.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: sync.setDescription('Timing Source Management.\n            ')
syncMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: syncMibVersion.setStatus('current')
if mibBuilder.loadTexts: syncMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
timingGeneratorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2), )
if mibBuilder.loadTexts: timingGeneratorTable.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorTable.setDescription('Table with TimingGenerator records.')
timingGeneratorRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1), ).setIndexNames((0, "SIAE-SYNC-MIB", "timingGeneratorId"))
if mibBuilder.loadTexts: timingGeneratorRecord.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorRecord.setDescription('TimingGenerator record.')
timingGeneratorId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorId.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorId.setDescription('This object is used as Index of the Timing Generator Table.')
timingGeneratorT4vsT0 = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("t4NotEqualT0", 1), ("t4EqualT0", 2))).clone('t4EqualT0')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorT4vsT0.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT4vsT0.setDescription('This object is used to set or reset the condition T4 equal T0.')
timingGeneratorHoldOffTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 1800)).clone(300)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorHoldOffTime.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorHoldOffTime.setDescription('HoldOff time in milliseconds (300..1800).')
timingGeneratorWtrTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorWtrTime.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorWtrTime.setDescription('Wait Time to Restore in minutes (0..12).')
timingGeneratorSinkLosSet = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorSinkLosSet.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorSinkLosSet.setDescription('Wait time (seconds) before to set Los of reference signal.')
timingGeneratorSinkLosReset = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 60)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorSinkLosReset.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorSinkLosReset.setDescription('Wait time (seconds) before to reset Los of reference signal.')
timingGeneratorT0SquelchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 7), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorT0SquelchAlarm.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT0SquelchAlarm.setDescription('T0 squelch Alarm (Probable cause = xxx) with associated severity.')
timingGeneratorT4SquelchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorT4SquelchAlarm.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT4SquelchAlarm.setDescription('T4 squelch Alarm (Probable cause = xxx) with associated severity.')
timingGeneratorFreeRunningStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorFreeRunningStatus.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorFreeRunningStatus.setDescription('Free running status (Probable cause = xxx) with associated severity.')
timingGeneratorHoldoverStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 10), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorHoldoverStatus.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorHoldoverStatus.setDescription('Holdover status (Probable cause = xxx) with associated severity.')
timingGeneratorActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cleared", 1), ("activeReportableStatus", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorActiveStatus.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorActiveStatus.setDescription('Active status (Probable cause = xxx) with associated severity.')
timingGeneratorT0CurrentQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorT0CurrentQuality.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT0CurrentQuality.setDescription('Current quality on T0.')
timingGeneratorT4CurrentQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingGeneratorT4CurrentQuality.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT4CurrentQuality.setDescription('Current quality on T4.')
timingGeneratorT4MinimumQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 4, 8, 11))).clone(namedValues=NamedValues(("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11))).clone('qSEC')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorT4MinimumQuality.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT4MinimumQuality.setDescription('If the Quality Level of the signal used to derive T4 falls below\n             timingGeneratorT4MinimumQuality then the output will be squelched.\n             The value ql-DNU inhibits T4 squelch due to this minimum Quality\n             Level. This feature is enabled by timingGeneratorT4Squelch when\n             timingGeneratorQualityEnable is on(2).')
timingGeneratorT0PreferredSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 15), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorT0PreferredSource.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT0PreferredSource.setDescription('Object identifier of the leaf timingSinkGenId of the timingSink\n             instance selected as preferential clock source of T0.\n             If no preferential timing sink is selected,\n             the value should be set to the OBJECT IDENTIFIER { 0 0 }.\n            ')
timingGeneratorT4PreferredSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 16), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorT4PreferredSource.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT4PreferredSource.setDescription('Object identifier of the leaf timingSinkGenId of the timingSink\n             instance selected as preferential clock source of T4.\n             If no preferential timing sink is selected,\n             the value should be set to the OBJECT IDENTIFIER { 0 0 }.\n            ')
timingGeneratorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 2, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingGeneratorRowStatus.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorRowStatus.setDescription('Status of this row of timingGeneratorTable.\n            ')
timingGeneratorMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3), )
if mibBuilder.loadTexts: timingGeneratorMaintTable.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorMaintTable.setDescription('Table with TimingGenerator records.')
timingGeneratorMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1), ).setIndexNames((0, "SIAE-SYNC-MIB", "timingGeneratorId"))
if mibBuilder.loadTexts: timingGeneratorMaintRecord.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorMaintRecord.setDescription('TimingGenerator record.')
timingGeneratorT4Squelch = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorT4Squelch.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT4Squelch.setDescription('This object is used to enable/disable T4 squelch.')
timingGeneratorStatusControl = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("freerunning", 1), ("holdover", 2), ("locked", 3))).clone('locked')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorStatusControl.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorStatusControl.setDescription('Clock generator operating mode control.\n             This item is linked to a manual operation (ManOpRecord) instance.')
timingGeneratorT0ForcedSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 3), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorT0ForcedSource.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT0ForcedSource.setDescription('Object identifier of the leaf timingSinkGenId of the timingSink\n             instance selected as forced clock source of T0.\n             If no forced timing sink is selected,\n             the value should be set to the OBJECT IDENTIFIER { 0 0 }.\n            ')
timingGeneratorT4ForcedSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 4), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorT4ForcedSource.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT4ForcedSource.setDescription('Object identifier of the leaf timingSinkGenId of the timingSink\n             instance selected as forced clock source of T4.\n             If no forced timing sink is selected,\n             the value should be set to the OBJECT IDENTIFIER { 0 0 }.\n            ')
timingGeneratorWtrClearSource = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 3, 1, 5), ObjectIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorWtrClearSource.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorWtrClearSource.setDescription('Object identifier of the leaf timingSinkGenId of the timingSink\n             instance selected to clear WTR time. On read, this object return\n             alvays an OBJECT IDENTIFIER {0 0}.\n            ')
timingSinkTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4), )
if mibBuilder.loadTexts: timingSinkTable.setStatus('current')
if mibBuilder.loadTexts: timingSinkTable.setDescription('Table with TimingSink records.')
timingSinkRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1), ).setIndexNames((0, "SIAE-SYNC-MIB", "timingSinkGenId"), (0, "SIAE-SYNC-MIB", "timingSinkId"), (0, "SIAE-SYNC-MIB", "timingSinkType"))
if mibBuilder.loadTexts: timingSinkRecord.setStatus('current')
if mibBuilder.loadTexts: timingSinkRecord.setDescription('TimingSink record.')
timingSinkGenId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkGenId.setStatus('current')
if mibBuilder.loadTexts: timingSinkGenId.setDescription('This object is used as Index of the timingGeneratorTable and\n             defines in union with timingSinkType and timingSinkId the\n             reference signal.\n            ')
timingSinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkId.setStatus('current')
if mibBuilder.loadTexts: timingSinkId.setDescription('This object is used as Index of the timingSinkTable and\n             defines in union with timingSinkType and timingSinkGenId the \n             reference signal.\n            ')
timingSinkType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("t0", 1), ("t4", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkType.setStatus('current')
if mibBuilder.loadTexts: timingSinkType.setDescription('This object is used as Index of the timingSinkTable and defines \n             if the reference signal is used to generate T0 or T4 system clock.\n            ')
timingSinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkIfIndex.setStatus('current')
if mibBuilder.loadTexts: timingSinkIfIndex.setDescription(' The ifIndex value the agent selected for this\n              timingSink interface.\n            ')
timingSinkSelector = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkSelector.setStatus('current')
if mibBuilder.loadTexts: timingSinkSelector.setDescription('This object is used to select one of the possible clock source\n             connected to this timingSink. Valid values are listed in\n             timingSinkSelectorTable: only values of timingSinkSelectorId\n             related to this instance of timinkSinkRecord are accepted.\n             Only the values corresponding to the index timingSinkSelectorId of\n             timinkSinkSelectorTable related to this instance of\n             timinkSinkRecord will be accepted.\n            ')
timingSinkPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("p1", 1), ("p2", 2), ("p3", 3), ("p4", 4), ("p5", 5), ("p6", 6), ("p7", 7), ("p8", 8), ("p9", 9), ("p10", 10), ("p11", 11), ("p12", 12), ("p13", 13), ("p14", 14), ("p15", 15), ("disable", 16))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkPriority.setStatus('current')
if mibBuilder.loadTexts: timingSinkPriority.setDescription('This object is used to set the priority of the reference signal (p1 is\n             the highest priority).')
timingSinkLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkLabel.setStatus('current')
if mibBuilder.loadTexts: timingSinkLabel.setDescription('ASCII string used to describe the reference signal when a trap is sent.')
timingSinkLosAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 8), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkLosAlarm.setStatus('current')
if mibBuilder.loadTexts: timingSinkLosAlarm.setDescription('Loss of reference signal (Probable cause = xxx) alarm\n             with associated severity.')
timingSinkDriftAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkDriftAlarm.setStatus('current')
if mibBuilder.loadTexts: timingSinkDriftAlarm.setDescription('Drift of reference signal (Probable cause = xxx) alarm\n             with associated severity.')
timingSinkActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cleared", 1), ("activeReportableStatus", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkActiveStatus.setStatus('current')
if mibBuilder.loadTexts: timingSinkActiveStatus.setDescription('Active status (Probable cause = xxx) status for the reference signal.')
timingSinkCurrentQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkCurrentQuality.setStatus('current')
if mibBuilder.loadTexts: timingSinkCurrentQuality.setDescription('Current quality on sink instance.')
timingSinkOverwriteTxQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("noOverwrite", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15))).clone('noOverwrite')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkOverwriteTxQuality.setStatus('current')
if mibBuilder.loadTexts: timingSinkOverwriteTxQuality.setDescription('Forcing of Tx quality parameter.')
timingSinkOverwriteRxQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("noOverwrite", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15))).clone('noOverwrite')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkOverwriteRxQuality.setStatus('current')
if mibBuilder.loadTexts: timingSinkOverwriteRxQuality.setDescription('Forcing of Rx quality parameter.')
timingSinkSentQuality = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkSentQuality.setStatus('current')
if mibBuilder.loadTexts: timingSinkSentQuality.setDescription('Quality level written in the S1 byte of the outgoing STM-n.')
timingSinkE1Sabit = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 8)).clone(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkE1Sabit.setStatus('current')
if mibBuilder.loadTexts: timingSinkE1Sabit.setDescription('Specifies the San synchronization status bit used \n             to indicate the clock quality level.\n             Meaningful when the Sink source is an E1  ')
timingSinkEthPortRole = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2))).clone('dynamic')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkEthPortRole.setStatus('deprecated')
if mibBuilder.loadTexts: timingSinkEthPortRole.setDescription("This item configures how to handle the role of a 1000BASE-T port\n             when it is used as a source of timing: choosing 'static', the\n             role is set according ethLanPhyTable settings, choosing 'dynamic',\n             the role is set consistently with the timing direction over the\n             1000baseT link chosen by SSM protocol.")
timingSinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 4, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: timingSinkRowStatus.setStatus('current')
if mibBuilder.loadTexts: timingSinkRowStatus.setDescription('Status of this row of timingSinkTable\n            ')
timingGeneratorManualSwitch = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorManualSwitch.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorManualSwitch.setDescription('timingGeneratorId of the forced timingGenerator instance.\n             If no preferred timing generator is selected, the value\n             should be set to 0.\n            ')
timingGeneratorForcedSwitch = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorForcedSwitch.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorForcedSwitch.setDescription('timingGeneratorId of the forced timingGenerator instance.\n             If no forced timing generator is selected, the value\n             should be set to 0.\n            ')
timingGeneratorT0SquelchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorT0SquelchAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT0SquelchAlarmSeverityCode.setDescription('Defines the severity associated to the TimingGeneratorT0SquelchAlarm\n             and enables/disables the trap generation on status change event.')
timingGeneratorT4SquelchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorT4SquelchAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorT4SquelchAlarmSeverityCode.setDescription('Defines the severity associated to the timingGeneratorT4SquelchAlarm\n             and enables/disables the trap generation on status change event.')
timingGeneratorFreeRunningStatusSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 9), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorFreeRunningStatusSeverityCode.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorFreeRunningStatusSeverityCode.setDescription('Defines the severity associated to the timingGeneratorFreeRunningStatus\n             and enables/disables the trap generation on status change event.')
timingGeneratorHoldoverStatusSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 10), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorHoldoverStatusSeverityCode.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorHoldoverStatusSeverityCode.setDescription('Defines the severity associated to the timingGeneratorHoldoverStatus\n             and enables/disables the trap generation on status change event.')
timingGeneratorActiveStatusSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("statusTrapEnable", 2))).clone('statusTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorActiveStatusSeverityCode.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorActiveStatusSeverityCode.setDescription('Defines the severity associated to the timingGeneratorActiveStatus\n             and enables/disables the trap generation on status change event.')
timingGeneratorQualityEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingGeneratorQualityEnable.setStatus('current')
if mibBuilder.loadTexts: timingGeneratorQualityEnable.setDescription('Quality policy enable ')
timingSinkLosAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 13), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingSinkLosAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: timingSinkLosAlarmSeverityCode.setDescription('Defines the severity associated to the TimingSinkLosAlarm\n             and enables/disables the trap generation on status change event.')
timingSinkDriftAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 14), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingSinkDriftAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: timingSinkDriftAlarmSeverityCode.setDescription('Defines the severity associated to the TimingSinkDriftAlarm\n             and enables/disables the trap generation on status change event.')
timingSinkActiveStatusSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("statusTrapEnable", 2))).clone('statusTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: timingSinkActiveStatusSeverityCode.setStatus('current')
if mibBuilder.loadTexts: timingSinkActiveStatusSeverityCode.setDescription('Defines the severity associated to the timingSinkActiveStatus\n             and enables/disables the trap generation on status change event.')
timingSinkSelectorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16), )
if mibBuilder.loadTexts: timingSinkSelectorTable.setStatus('current')
if mibBuilder.loadTexts: timingSinkSelectorTable.setDescription('Table with TimingSinkSelector records.')
timingSinkSelectorRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16, 1), ).setIndexNames((0, "SIAE-SYNC-MIB", "timingSinkGenId"), (0, "SIAE-SYNC-MIB", "timingSinkId"), (0, "SIAE-SYNC-MIB", "timingSinkType"), (0, "SIAE-SYNC-MIB", "timingSinkSelectorId"))
if mibBuilder.loadTexts: timingSinkSelectorRecord.setStatus('current')
if mibBuilder.loadTexts: timingSinkSelectorRecord.setDescription('TimingSinkSelector entry.\n             Several instances of this entry can be create for each instance of\n             timingSinkTable. Each entry represents a possible source selected\n             by a multiplexer outside the SETS for a specific timingSink.\n             Only the values corresponding to the index timingSinkSelectorId can\n             be set to timingSinkSelector.\n            ')
timingSinkSelectorId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkSelectorId.setStatus('current')
if mibBuilder.loadTexts: timingSinkSelectorId.setDescription('This object is used as Index of the timingSinkSelectorTable and\n             defines in union with timingSinkGenId, timingSinkType and\n             timingSinkId the selected source by a multiplexer outside the\n             SETS.\n            ')
timingSinkSelectorLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 16, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: timingSinkSelectorLabel.setStatus('current')
if mibBuilder.loadTexts: timingSinkSelectorLabel.setDescription('ASCII string used to describe the selectable timing source.\n            ')
esmcTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17), )
if mibBuilder.loadTexts: esmcTable.setStatus('current')
if mibBuilder.loadTexts: esmcTable.setDescription('Table with TimingSinkSelector records.')
esmcRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: esmcRecord.setStatus('current')
if mibBuilder.loadTexts: esmcRecord.setDescription('esmcTable entry.\n             Every entries describes an ESMC channel of a TE interface.\n            ')
esmcSsmEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: esmcSsmEnable.setStatus('current')
if mibBuilder.loadTexts: esmcSsmEnable.setDescription('This object enables SSM messaging on this ifIndex.\n            ')
esmcQlRx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcQlRx.setStatus('current')
if mibBuilder.loadTexts: esmcQlRx.setDescription('This object show quality received on ESMC-PDU this interface.\n            ')
esmcQlTx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 4, 8, 11, 15))).clone(namedValues=NamedValues(("qUNKN", 0), ("qPRC", 2), ("qSSUT", 4), ("qSSUL", 8), ("qSEC", 11), ("qDNU", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcQlTx.setStatus('current')
if mibBuilder.loadTexts: esmcQlTx.setDescription('This object show quality transmitted in ESMC-PDU on this interface.\n            ')
esmcPktsRx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcPktsRx.setStatus('current')
if mibBuilder.loadTexts: esmcPktsRx.setDescription('This object contains the total number of received ESMC-PDU packets\n             on this interface.\n            ')
esmcPktsTx = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcPktsTx.setStatus('current')
if mibBuilder.loadTexts: esmcPktsTx.setDescription('This object contains the total number of transmitted ESMC-PDU\n             packets on this interface.\n            ')
esmcPktsRxDropped = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcPktsRxDropped.setStatus('current')
if mibBuilder.loadTexts: esmcPktsRxDropped.setDescription('This object contains the total number of dropped ESMC-PDU packets\n             on this interface.\n            ')
esmcPktsRxErrored = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: esmcPktsRxErrored.setStatus('current')
if mibBuilder.loadTexts: esmcPktsRxErrored.setDescription('This object contains the total number of dropped ESMC-PDU packets\n             whose processing(decoding) resulted into error.\n            ')
esmc1000BaseTRole = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("slave", 1), ("master", 2), ("auto", 3))).clone('auto')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: esmc1000BaseTRole.setStatus('current')
if mibBuilder.loadTexts: esmc1000BaseTRole.setDescription('This object allows to input the clock generator role of a 1000BaseT\n             interface. This objects is applicable when the quality management\n             is disabled (timingGeneratorQualityEnable set to off(1)) and to \n             all interfaces not connected to any timingSink when the quality\n             management is enabled.\n            ')
esmcRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 28, 17, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: esmcRowStatus.setStatus('current')
if mibBuilder.loadTexts: esmcRowStatus.setDescription('Status of this row of esmcTable.\n            ')
mibBuilder.exportSymbols("SIAE-SYNC-MIB", timingGeneratorT0SquelchAlarm=timingGeneratorT0SquelchAlarm, timingGeneratorT4MinimumQuality=timingGeneratorT4MinimumQuality, timingGeneratorT4Squelch=timingGeneratorT4Squelch, timingSinkIfIndex=timingSinkIfIndex, timingSinkActiveStatusSeverityCode=timingSinkActiveStatusSeverityCode, timingGeneratorTable=timingGeneratorTable, timingSinkGenId=timingSinkGenId, timingGeneratorT4ForcedSource=timingGeneratorT4ForcedSource, esmcQlTx=esmcQlTx, timingGeneratorActiveStatusSeverityCode=timingGeneratorActiveStatusSeverityCode, timingGeneratorT0ForcedSource=timingGeneratorT0ForcedSource, timingSinkRecord=timingSinkRecord, timingSinkSentQuality=timingSinkSentQuality, timingGeneratorFreeRunningStatusSeverityCode=timingGeneratorFreeRunningStatusSeverityCode, timingSinkOverwriteRxQuality=timingSinkOverwriteRxQuality, timingGeneratorHoldOffTime=timingGeneratorHoldOffTime, timingGeneratorHoldoverStatus=timingGeneratorHoldoverStatus, timingSinkE1Sabit=timingSinkE1Sabit, timingGeneratorManualSwitch=timingGeneratorManualSwitch, timingGeneratorHoldoverStatusSeverityCode=timingGeneratorHoldoverStatusSeverityCode, timingSinkLosAlarmSeverityCode=timingSinkLosAlarmSeverityCode, timingSinkSelectorRecord=timingSinkSelectorRecord, esmc1000BaseTRole=esmc1000BaseTRole, esmcPktsTx=esmcPktsTx, timingGeneratorT4PreferredSource=timingGeneratorT4PreferredSource, timingGeneratorRecord=timingGeneratorRecord, timingGeneratorWtrClearSource=timingGeneratorWtrClearSource, timingSinkLosAlarm=timingSinkLosAlarm, esmcPktsRxDropped=esmcPktsRxDropped, timingGeneratorId=timingGeneratorId, timingGeneratorMaintRecord=timingGeneratorMaintRecord, timingSinkOverwriteTxQuality=timingSinkOverwriteTxQuality, esmcQlRx=esmcQlRx, timingGeneratorT4SquelchAlarm=timingGeneratorT4SquelchAlarm, esmcPktsRxErrored=esmcPktsRxErrored, timingSinkPriority=timingSinkPriority, timingSinkSelectorLabel=timingSinkSelectorLabel, timingGeneratorRowStatus=timingGeneratorRowStatus, timingGeneratorQualityEnable=timingGeneratorQualityEnable, timingSinkRowStatus=timingSinkRowStatus, esmcSsmEnable=esmcSsmEnable, timingGeneratorStatusControl=timingGeneratorStatusControl, timingGeneratorWtrTime=timingGeneratorWtrTime, timingGeneratorSinkLosReset=timingGeneratorSinkLosReset, timingSinkTable=timingSinkTable, timingSinkActiveStatus=timingSinkActiveStatus, timingGeneratorT4CurrentQuality=timingGeneratorT4CurrentQuality, timingGeneratorT4SquelchAlarmSeverityCode=timingGeneratorT4SquelchAlarmSeverityCode, timingGeneratorActiveStatus=timingGeneratorActiveStatus, timingSinkSelectorId=timingSinkSelectorId, timingGeneratorSinkLosSet=timingGeneratorSinkLosSet, timingSinkEthPortRole=timingSinkEthPortRole, timingSinkCurrentQuality=timingSinkCurrentQuality, esmcTable=esmcTable, timingGeneratorT0SquelchAlarmSeverityCode=timingGeneratorT0SquelchAlarmSeverityCode, timingSinkType=timingSinkType, timingSinkLabel=timingSinkLabel, timingGeneratorT0PreferredSource=timingGeneratorT0PreferredSource, esmcRowStatus=esmcRowStatus, PYSNMP_MODULE_ID=sync, sync=sync, timingSinkDriftAlarm=timingSinkDriftAlarm, timingSinkSelector=timingSinkSelector, timingGeneratorFreeRunningStatus=timingGeneratorFreeRunningStatus, timingGeneratorMaintTable=timingGeneratorMaintTable, timingSinkId=timingSinkId, timingSinkSelectorTable=timingSinkSelectorTable, esmcPktsRx=esmcPktsRx, timingGeneratorT0CurrentQuality=timingGeneratorT0CurrentQuality, esmcRecord=esmcRecord, timingGeneratorForcedSwitch=timingGeneratorForcedSwitch, timingSinkDriftAlarmSeverityCode=timingSinkDriftAlarmSeverityCode, syncMibVersion=syncMibVersion, timingGeneratorT4vsT0=timingGeneratorT4vsT0)
