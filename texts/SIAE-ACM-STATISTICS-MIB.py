#
# PySNMP MIB module SIAE-ACM-STATISTICS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-ACM-STATISTICS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:31:57 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
AlarmSeverityCode, AlarmStatus = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ModuleIdentity, Unsigned32, Integer32, Gauge32, IpAddress, MibIdentifier, Bits, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ModuleIdentity", "Unsigned32", "Integer32", "Gauge32", "IpAddress", "MibIdentifier", "Bits", "TimeTicks", "Counter64")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
acmStats = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 75))
acmStats.setRevisions(('2014-11-05 00:00', '2014-02-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acmStats.setRevisionsDescriptions(('MIB version 01.00.01\n             - Added ACM profilea 4096 QAM and 4096QAM strong\n              (changed AcmProfile TEXTUAL-CONVENTION)\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: acmStats.setLastUpdated('201411050000Z')
if mibBuilder.loadTexts: acmStats.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: acmStats.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: acmStats.setDescription('Adaptive Code Modulation (ACM) Statistics (Performance Monitoring)\n            ')
class AcmProfile(TextualConvention, Integer32):
    description = 'List of supported ACM profiles.\n         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27))
    namedValues = NamedValues(("unavailable", 1), ("downshift", 2), ("upshift", 3), ("acmBPSKstrong", 4), ("acmBPSK", 5), ("acm4QAMstrong", 6), ("acm4QAM", 7), ("acm8PSKstrong", 8), ("acm8PSK", 9), ("acm16QAMstrong", 10), ("acm16QAM", 11), ("acm32QAMstrong", 12), ("acm32QAM", 13), ("acm64QAMstrong", 14), ("acm64QAM", 15), ("acm128QAMstrong", 16), ("acm128QAM", 17), ("acm256QAMstrong", 18), ("acm256QAM", 19), ("acm512QAMstrong", 20), ("acm512QAM", 21), ("acm1024QAMstrong", 22), ("acm1024QAM", 23), ("acm2048QAMstrong", 24), ("acm2048QAM", 25), ("acm4096QAMstrong", 26), ("acm4096QAM", 27))

acmsMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsMibVersion.setStatus('current')
if mibBuilder.loadTexts: acmsMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
acmsTpLinkTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2), )
if mibBuilder.loadTexts: acmsTpLinkTable.setStatus('current')
if mibBuilder.loadTexts: acmsTpLinkTable.setDescription('Table with ACM Termination Point of the radio links.\n             This table contains object to activate and deactivate the\n             buildup of counters.\n            ')
acmsTpLinkRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1), ).setIndexNames((0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"))
if mibBuilder.loadTexts: acmsTpLinkRecord.setStatus('current')
if mibBuilder.loadTexts: acmsTpLinkRecord.setDescription('Entry of acmsTpLinkTable.\n            ')
acmsTpLinkId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: acmsTpLinkId.setStatus('current')
if mibBuilder.loadTexts: acmsTpLinkId.setDescription('This object identifies the Radio link.\n            ')
acmsTpLinkPolId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: acmsTpLinkPolId.setStatus('current')
if mibBuilder.loadTexts: acmsTpLinkPolId.setDescription('This object identifies the Radio link polarization for XPIC\n             configuration. In non XPIC link this object should be 1.\n            ')
acmsTpLinkStartStop = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("stop", 2))).clone('stop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acmsTpLinkStartStop.setStatus('current')
if mibBuilder.loadTexts: acmsTpLinkStartStop.setDescription('This object is used to start and to stop the statistic \n             (Perfomance Monitoring) counter evaluation.\n            ')
acmsTpLinkLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsTpLinkLabel.setStatus('current')
if mibBuilder.loadTexts: acmsTpLinkLabel.setDescription('ASCII string used to identify the ACM Termination Point.\n            ')
acmsTpLinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acmsTpLinkRowStatus.setStatus('current')
if mibBuilder.loadTexts: acmsTpLinkRowStatus.setDescription('Status of this row of acmsTpLinkTable.\n\n             When set to notInService, associated acmsTpProfileTable\n             rows may be added, deleted and modified.\n\n             When an attempt is made to set acmsTpLinkRowStatus to\n             active, there is at least a row in acmsTpProfileTable with\n             first index equal to acmsTpLinkId. Otherwise, the error\n             inconsistentValue is returned to the set attempt.\n\n             The creation of a row in this table, creates a row with the\n             same index in of acmsTpMaintTable.\n\n             The deletion of a row in this table, deletes a row with the\n             same index in of acmsTpMaintTable.\n\n             If this object is set to destroy, must not be no rows in \n             acmsTpProfileTable associated by acmsTpLinkId to the row\n             that is being deleted, otherwise, the error inconsistentValue\n             is returned to the set attempt. Hence, profile instances must\n             be deleted before this link instance.\n            ')
acmsTpProfileTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3), )
if mibBuilder.loadTexts: acmsTpProfileTable.setStatus('current')
if mibBuilder.loadTexts: acmsTpProfileTable.setDescription('ACM Termination Point Thresholds Class table.\n             Table with AcmsTpProfileRecord records.\n             This table contains alarms and related thresholds to notify them\n             within a specific time interval. \n            ')
acmsTpProfileRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1), ).setIndexNames((0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpProfileId"))
if mibBuilder.loadTexts: acmsTpProfileRecord.setStatus('current')
if mibBuilder.loadTexts: acmsTpProfileRecord.setDescription('Entry of acmsTpLinkTable.\n             Several instances (a instance for each ACM profile supported by\n             the radio system) of this record is created on creation of\n             acmsTpLinkTable.\n            ')
acmsTpProfileId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 1), AcmProfile())
if mibBuilder.loadTexts: acmsTpProfileId.setStatus('current')
if mibBuilder.loadTexts: acmsTpProfileId.setDescription('This object identifies the ACM profile of the radio system.\n            ')
acmsTpProfile15mAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 2), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsTpProfile15mAlarm.setStatus('current')
if mibBuilder.loadTexts: acmsTpProfile15mAlarm.setDescription('If acmsCounteValue crosses the threshold acmsTpProfile15mThreshold,\n             this alarm is notified.\n            ')
acmsTpProfile24hAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 3), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsTpProfile24hAlarm.setStatus('current')
if mibBuilder.loadTexts: acmsTpProfile24hAlarm.setDescription('If acmsCounteValue crosses the threshold acmsTpProfile24hThreshold,\n             this alarm is notified.\n            ')
acmsTpProfile15mThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acmsTpProfile15mThreshold.setStatus('current')
if mibBuilder.loadTexts: acmsTpProfile15mThreshold.setDescription('Number of seconds within a 15 minutes interval to set \n             acmsTpProfile15mAlarm. The special value 0 turn off the alarm.\n\n             For downshift and upshift profiles, this threshold reports\n             the number of times a profile must be changed within a 15 minutes\n             interval to set acmsTpProfile15mAlarm.\n            ')
acmsTpProfile24hThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acmsTpProfile24hThreshold.setStatus('current')
if mibBuilder.loadTexts: acmsTpProfile24hThreshold.setDescription('Number of seconds within a 24 hours interval to set \n             acmsTpProfile24hAlarm. The special value 0 turn off the alarm.\n\n             For the profiles downshift and upshift, this threshold reports\n             the number of times a profile must be changed within a 24 hours\n             interval to set acmsTpProfile24hAlarm.\n            ')
acmsTpProfileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acmsTpProfileRowStatus.setStatus('current')
if mibBuilder.loadTexts: acmsTpProfileRowStatus.setDescription('Status of this row of acmsTpProfileTable.\n\n             A row in the acmsTpProfileTable may not be created,\n             deleted, set to notInService or otherwise modified\n             if the there is no a row in acmsTpProfileTable with the \n             same acmsTpLinkId and the associated acmsTpLinkRowStatus\n             object is equal to active. However, if the acmsTpLinkRowStatus\n             object is equal to notInService, a row may be created, deleted\n             or modified. In other words, a profile may not be added,\n             deleted or modified if the ACM statistics of a radio link\n             is active.\n\n             The creation on a row in this table, creates a row with the same\n             index in of acmsProfileCounterTable.\n\n             If this object is set to destroy, the associated instance\n             of acmsProfileCounterTable will also be deleted by this action.\n            ')
acmsTpMaintTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4), )
if mibBuilder.loadTexts: acmsTpMaintTable.setStatus('current')
if mibBuilder.loadTexts: acmsTpMaintTable.setDescription('Table with Command for maintenance of Termination Point.\n             Objects in this table is not persistent.\n            ')
acmsTpMaintRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4, 1), ).setIndexNames((0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"))
if mibBuilder.loadTexts: acmsTpMaintRecord.setStatus('current')
if mibBuilder.loadTexts: acmsTpMaintRecord.setDescription('ACM Termination Point Maintenance record.\n             An Instance of this record is created on creation of\n             acmsTpLinkTable.\n            ')
acmsTpMaintCounterClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acmsTpMaintCounterClear.setStatus('current')
if mibBuilder.loadTexts: acmsTpMaintCounterClear.setDescription('This object is used to clear the statistic (Perfomance Monitoring)\n             counters.\n            ')
acmsTpMaintAlarmClear = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("notActive", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acmsTpMaintAlarmClear.setStatus('current')
if mibBuilder.loadTexts: acmsTpMaintAlarmClear.setDescription('This object is used to clear the threshold cross alarms.\n            ')
acmsIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5), )
if mibBuilder.loadTexts: acmsIntervalTable.setStatus('current')
if mibBuilder.loadTexts: acmsIntervalTable.setDescription('Table with records of block.\n            ')
acmsIntervalRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1), ).setIndexNames((0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsIntervalId"))
if mibBuilder.loadTexts: acmsIntervalRecord.setStatus('current')
if mibBuilder.loadTexts: acmsIntervalRecord.setDescription('Entry of acmsBlockTable.\n             There is an entry in acmsBlockTable for each radio link.\n             Several (up to 19) instances of this record are created since\n             the first time that acmsTpLinkStartStop becomes start.\n            ')
acmsIntervalId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsIntervalId.setStatus('current')
if mibBuilder.loadTexts: acmsIntervalId.setDescription('This object identifies time intervals according to the\n             following code:\n\n             (1)   Current Daily counters\n             (2)   Daily counters of the day before\n             (3)   Current a day counters\n             (4)   a day interval N. 1\n                   (The most recently completed 15 minute interval)\n             ...\n\n             (19)  a day interval N. 16\n                   (The oldest day counters - 4 hours ago).\n\n             The interval identified by 4 is the most recently completed 15\n             minute interval, and the interval identified by N is the interval\n             immediately preceding the one identified by N-1.\n            ')
acmsIntervalType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("daily", 1), ("fifteen-min", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsIntervalType.setStatus('current')
if mibBuilder.loadTexts: acmsIntervalType.setDescription('The type of the counter interval: it can describe a daily block\n             counter or a counter related to a 15 minutes interval.\n            ')
acmsIntervalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("meaningless", 1), ("meaningfull", 2), ("incomplete", 3), ("dummy", 4), ("lost", 5), ("restarted", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsIntervalStatus.setStatus('current')
if mibBuilder.loadTexts: acmsIntervalStatus.setDescription('Interval status.\n            ')
acmsIntervalTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 5, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsIntervalTimeStamp.setStatus('current')
if mibBuilder.loadTexts: acmsIntervalTimeStamp.setDescription('The object is the time when the performance record is closed.\n             The time is shown as the number of seconds since January 1, 1970\n            ')
acmsProfileCounterTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 6), )
if mibBuilder.loadTexts: acmsProfileCounterTable.setStatus('current')
if mibBuilder.loadTexts: acmsProfileCounterTable.setDescription('Table with records of ACM statistics counters.\n            ')
acmsProfileCounterRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 6, 1), ).setIndexNames((0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpLinkPolId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsTpProfileId"), (0, "SIAE-ACM-STATISTICS-MIB", "acmsIntervalId"))
if mibBuilder.loadTexts: acmsProfileCounterRecord.setStatus('current')
if mibBuilder.loadTexts: acmsProfileCounterRecord.setDescription('Entry of acmsProfileCounterTable.\n             There is an entry in acmsProfileCounterTable for each profile\n             of each radio link.\n             Several (up to 19) instances of this record are created since\n             the first time that acmsTpLinkStartStop becomes start.\n            ')
acmsProfileCounterValue = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acmsProfileCounterValue.setStatus('current')
if mibBuilder.loadTexts: acmsProfileCounterValue.setDescription('When index acmsTpProfileId is downshift, this object counts the\n             number of times that the active profile is moved to a lower one.\n  \n             When index acmsTpProfileId is upshift, this object counts the\n             number of times that the active profile is moved to an upper one.\n             \n             When index acmsTpProfileId is unavailable, this object counts\n             the number of seconds in which the modem is not locked.\n             \n             For all other values of acmsTpProfileId the object counts the\n             number of seconds for which the rx profile relative to this row\n             of the table has been active.\n            ')
acmsTpProfile15mAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acmsTpProfile15mAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: acmsTpProfile15mAlarmSeverityCode.setDescription('Define the severity associated to the acmsTpProfile15mAlarm\n             and enables/disables the trap generation on status change event.\n            ')
acmsTpProfile24hAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 75, 8), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acmsTpProfile24hAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: acmsTpProfile24hAlarmSeverityCode.setDescription('Define the severity associated to the acmsTpProfile24hAlarm\n             and enables/disables the trap generation on status change event.\n            ')
mibBuilder.exportSymbols("SIAE-ACM-STATISTICS-MIB", acmsTpMaintTable=acmsTpMaintTable, acmsTpMaintAlarmClear=acmsTpMaintAlarmClear, acmsTpLinkRecord=acmsTpLinkRecord, acmsProfileCounterTable=acmsProfileCounterTable, acmsTpProfileTable=acmsTpProfileTable, acmsTpProfile15mThreshold=acmsTpProfile15mThreshold, PYSNMP_MODULE_ID=acmStats, acmsTpProfile15mAlarm=acmsTpProfile15mAlarm, acmsTpProfile24hAlarm=acmsTpProfile24hAlarm, acmsTpProfileRowStatus=acmsTpProfileRowStatus, acmsTpLinkId=acmsTpLinkId, acmsTpLinkPolId=acmsTpLinkPolId, acmsTpProfile24hAlarmSeverityCode=acmsTpProfile24hAlarmSeverityCode, acmsTpProfileRecord=acmsTpProfileRecord, AcmProfile=AcmProfile, acmsTpLinkLabel=acmsTpLinkLabel, acmsIntervalStatus=acmsIntervalStatus, acmsIntervalTable=acmsIntervalTable, acmsTpProfileId=acmsTpProfileId, acmsTpLinkStartStop=acmsTpLinkStartStop, acmsIntervalType=acmsIntervalType, acmsMibVersion=acmsMibVersion, acmStats=acmStats, acmsIntervalRecord=acmsIntervalRecord, acmsTpMaintRecord=acmsTpMaintRecord, acmsProfileCounterValue=acmsProfileCounterValue, acmsTpProfile24hThreshold=acmsTpProfile24hThreshold, acmsIntervalId=acmsIntervalId, acmsTpMaintCounterClear=acmsTpMaintCounterClear, acmsIntervalTimeStamp=acmsIntervalTimeStamp, acmsProfileCounterRecord=acmsProfileCounterRecord, acmsTpProfile15mAlarmSeverityCode=acmsTpProfile15mAlarmSeverityCode, acmsTpLinkTable=acmsTpLinkTable, acmsTpLinkRowStatus=acmsTpLinkRowStatus)
