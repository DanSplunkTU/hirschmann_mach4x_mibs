#
# PySNMP MIB module SIAE-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-ALARM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:19:33 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
siaeMicroelettronicaSpa, siaeMib = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMicroelettronicaSpa", "siaeMib")
accessControlLoginIpAddress, = mibBuilder.importSymbols("SIAE-USER-MIB", "accessControlLoginIpAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, TimeTicks, Integer32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Bits, Counter32, Counter64, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "TimeTicks", "Integer32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Bits", "Counter32", "Counter64", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
smalarm = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 4))
smalarm.setRevisions(('2016-10-04 00:00', '2015-07-17 00:00', '2015-03-23 00:00', '2015-03-16 00:00', '2014-06-23 00:00', '2014-03-03 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: smalarm.setRevisionsDescriptions(('Fixed alarmIpSnmpAgentAddress type.\n            ', 'Fixed alarmTrap OID.\n            ', 'Removed alarmTrapNumber from alarmLogFTPStatusTrap.\n            ', 'MAX-ACCESS clause of alarmTrapNumber is back to read-only \n             value in order to allow a manager to synchronize alarms.\n            ', 'Removed circular dependence from SIAE-EQUIP-MIB in IMPORTS.\n             Added alarmIpSnmpAgentAddress.\n             Changed MAX-ACCESS clause of alarmObjectId, alarmObjectVal,\n             alarmTrapDescription and alarmTrapNumber from read-only to \n             accessible-for-notify.\n            ', 'MIB version 01.00.01\n             Added alarmTable\n            ', 'Improved description of alarmMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: smalarm.setLastUpdated('201610040000Z')
if mibBuilder.loadTexts: smalarm.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: smalarm.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: help@siaemic.com\n            ')
if mibBuilder.loadTexts: smalarm.setDescription('Logger of the transitions of NE alarms and active alarm table.\n            ')
class AlarmStatus(TextualConvention, Integer32):
    description = 'This textual convenion defines the status of an alarm. The active \n          status is related to the perceived severity.\n         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("cleared", 1), ("activeReportableStatus", 2), ("activeReportableWarning", 3), ("activeReportableMinor", 4), ("activeReportableMajor", 5), ("activeReportableCritical", 6))

class AlarmSeverityCode(TextualConvention, Integer32):
    description = 'This textual convention defines the perceived severity associated\n          to an alarm.\n         '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 18, 19, 20, 21, 22))
    namedValues = NamedValues(("disable", 1), ("statusTrapEnable", 2), ("warningTrapEnable", 3), ("minorTrapEnable", 4), ("majorTrapEnable", 5), ("criticalTrapEnable", 6), ("statusTrapDisable", 18), ("warningTrapDisable", 19), ("minorTrapDisable", 20), ("majorTrapDisable", 21), ("criticalTrapDisable", 22))

siaeNotificationEntry = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2))
alarmTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 0))
alarmMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMibVersion.setStatus('current')
if mibBuilder.loadTexts: alarmMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
alarmLogTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3), )
if mibBuilder.loadTexts: alarmLogTable.setStatus('current')
if mibBuilder.loadTexts: alarmLogTable.setDescription('Table with Alarm records of the logger.')
alarmLogRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1), ).setIndexNames((0, "SIAE-ALARM-MIB", "alarmLogRecordId"))
if mibBuilder.loadTexts: alarmLogRecord.setStatus('current')
if mibBuilder.loadTexts: alarmLogRecord.setDescription('Alarm record of the logger.')
alarmLogRecordId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogRecordId.setStatus('current')
if mibBuilder.loadTexts: alarmLogRecordId.setDescription('This object is used as Index of alarmLogTable.')
alarmLogObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogObjectId.setStatus('current')
if mibBuilder.loadTexts: alarmLogObjectId.setDescription('The Object Identifier of the Managed Object with\n             Alarms or Controls active (not cleared Alarm Status).')
alarmLogObjectVal = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 3), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogObjectVal.setStatus('current')
if mibBuilder.loadTexts: alarmLogObjectVal.setDescription('Alarm Status with associated severity.')
alarmLogObjectSev = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 4), AlarmSeverityCode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogObjectSev.setStatus('current')
if mibBuilder.loadTexts: alarmLogObjectSev.setDescription('Severity associated to the Alarm ')
alarmLogDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogDescription.setStatus('current')
if mibBuilder.loadTexts: alarmLogDescription.setDescription('ASCII string used to describe the event.')
alarmLogEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogEventTime.setStatus('current')
if mibBuilder.loadTexts: alarmLogEventTime.setDescription('The time (in secs) when the event was registered in the Log since\n             01-Gen-1970.')
alarmLogActionRequest = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notActive", 0), ("delete", 1), ("read", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogActionRequest.setStatus('current')
if mibBuilder.loadTexts: alarmLogActionRequest.setDescription('This object is used to delete or to read the LOG using Ftp (file transfer).')
alarmLogFTPfile = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogFTPfile.setStatus('current')
if mibBuilder.loadTexts: alarmLogFTPfile.setDescription('Path and file name used when the log is transferred using Ftp (action = read).')
alarmLogAlarmSeverityEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 6), Integer32().clone(31)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogAlarmSeverityEnable.setStatus('current')
if mibBuilder.loadTexts: alarmLogAlarmSeverityEnable.setDescription('This object enables the event record write in the log according to\n             the severity:\n             Bit0 = Status\n             Bit1 = Warning\n             Bit2 = Minor\n             Bit3 = Major\n             Bit4 = Critical.')
alarmLogStartHourEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogStartHourEnable.setStatus('current')
if mibBuilder.loadTexts: alarmLogStartHourEnable.setDescription('This object defines whit AlarmLogEndHourEnable the period during\n             a day when the alarm records must be written in the log.')
alarmLogEndHourEnable = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)).clone(23)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogEndHourEnable.setStatus('current')
if mibBuilder.loadTexts: alarmLogEndHourEnable.setDescription('This object defines whit AlarmLogStartHourEnable the period during\n             a day when the alarm records must be written in the log.')
alarmLogStartTimeFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogStartTimeFilter.setStatus('current')
if mibBuilder.loadTexts: alarmLogStartTimeFilter.setDescription('The events with EventTime greater than this object are read/delete\n             from the log. Null value means no filter.')
alarmLogEndTimeFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 10), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogEndTimeFilter.setStatus('current')
if mibBuilder.loadTexts: alarmLogEndTimeFilter.setDescription('The events with EventTime less than this object are read/delete\n             from the log. Null value means no filter.')
alarmLogManagedObjectFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 11), ObjectIdentifier().clone((1, 3, 6, 1, 4, 1, 3373))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogManagedObjectFilter.setStatus('current')
if mibBuilder.loadTexts: alarmLogManagedObjectFilter.setDescription('The Object Identifier of the Managed Object that has to be\n             read/delete from the log. Null value means no filter.')
alarmLogAlarmSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 12), Integer32().clone(31)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogAlarmSeverityFilter.setStatus('current')
if mibBuilder.loadTexts: alarmLogAlarmSeverityFilter.setDescription('This object defines the alarm severity of the records that must\n             be read/delete from the log.\n             Bit0 = Status\n             Bit1 = Warning\n             Bit2 = Minor\n             Bit3 = Major\n             Bit4 = Critical.')
alarmLogFTPStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("transferring", 1), ("completed", 2), ("interrupted", 3), ("empty", 4))).clone('completed')).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogFTPStatus.setStatus('current')
if mibBuilder.loadTexts: alarmLogFTPStatus.setDescription('Status of alarm logger Ftp transfer operation.')
alarmLogFTPStatusTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 34))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2), ("trapEnableWithACK", 34))).clone('trapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmLogFTPStatusTrapNotification.setStatus('current')
if mibBuilder.loadTexts: alarmLogFTPStatusTrapNotification.setDescription('Enables/disables the trap generation on FTP tranfer operation.')
alarmLogLastEventTime = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmLogLastEventTime.setStatus('current')
if mibBuilder.loadTexts: alarmLogLastEventTime.setDescription('It is the Event time of the last alarm inserted into the alarm log.')
alarmActiveTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17), )
if mibBuilder.loadTexts: alarmActiveTable.setStatus('current')
if mibBuilder.loadTexts: alarmActiveTable.setDescription('Table with one record for each Alarms&Controls that is active in\n             the NE.')
alarmActiveRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1), ).setIndexNames((0, "SIAE-ALARM-MIB", "alarmActiveObjectId"))
if mibBuilder.loadTexts: alarmActiveRecord.setStatus('current')
if mibBuilder.loadTexts: alarmActiveRecord.setDescription('Alarms&Controls record.')
alarmActiveObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveObjectId.setStatus('current')
if mibBuilder.loadTexts: alarmActiveObjectId.setDescription('The Object Identifier of the Managed Object with\n             Alarms or Controls active (not cleared Alarm Status).')
alarmActiveObjectVal = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 2), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveObjectVal.setStatus('current')
if mibBuilder.loadTexts: alarmActiveObjectVal.setDescription('Alarm Status with associated severity.')
alarmActiveDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveDescription.setStatus('current')
if mibBuilder.loadTexts: alarmActiveDescription.setDescription('ASCII string used to describe the event.')
alarmActiveEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveEventTime.setStatus('current')
if mibBuilder.loadTexts: alarmActiveEventTime.setDescription('The time when the Alarm became active.\n             In seconds since 01/01/70.')
alarmActiveFloodingStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 17, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmActiveFloodingStatus.setStatus('current')
if mibBuilder.loadTexts: alarmActiveFloodingStatus.setDescription("Indicates the 'flooding' status.")
alarmSyntesysCritical = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6))).clone(namedValues=NamedValues(("cleared", 1), ("activeReportableCritical", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSyntesysCritical.setStatus('current')
if mibBuilder.loadTexts: alarmSyntesysCritical.setDescription('OR of all Critical Alarms.')
alarmSyntesysCriticalSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 6, 22))).clone(namedValues=NamedValues(("disable", 1), ("criticalTrapEnable", 6), ("criticalTrapDisable", 22))).clone('criticalTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSyntesysCriticalSeverityCode.setStatus('current')
if mibBuilder.loadTexts: alarmSyntesysCriticalSeverityCode.setDescription('Defines the severity associated to the alarmSyntesysCritical\n             and enables/disables the trap generation on status change event.')
alarmSyntesysMajor = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 5))).clone(namedValues=NamedValues(("cleared", 1), ("activeReportableMajor", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSyntesysMajor.setStatus('current')
if mibBuilder.loadTexts: alarmSyntesysMajor.setDescription('OR of all Major Alarms.')
alarmSyntesysMajorSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 5, 21))).clone(namedValues=NamedValues(("disable", 1), ("majorTrapEnable", 5), ("majorTrapDisable", 21))).clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSyntesysMajorSeverityCode.setStatus('current')
if mibBuilder.loadTexts: alarmSyntesysMajorSeverityCode.setDescription('Defines the severity associated to alarmSyntesysMajor\n             and enables/disables the trap generation on status change event.')
alarmSyntesysMinor = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4))).clone(namedValues=NamedValues(("cleared", 1), ("activeReportableMinor", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSyntesysMinor.setStatus('current')
if mibBuilder.loadTexts: alarmSyntesysMinor.setDescription('OR of all Minor Alarms.')
alarmSyntesysMinorSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 4, 20))).clone(namedValues=NamedValues(("disable", 1), ("minorTrapEnable", 4), ("minorTrapDisable", 20))).clone('minorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSyntesysMinorSeverityCode.setStatus('current')
if mibBuilder.loadTexts: alarmSyntesysMinorSeverityCode.setDescription('Defines the severity associated to alarmSyntesysMinor\n             and enables/disables the trap generation on status change event.')
alarmSyntesysWarning = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3))).clone(namedValues=NamedValues(("cleared", 1), ("activeReportableWarning", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSyntesysWarning.setStatus('current')
if mibBuilder.loadTexts: alarmSyntesysWarning.setDescription('OR of all Warning Alarms.')
alarmSyntesysWarningSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 19))).clone(namedValues=NamedValues(("disable", 1), ("warningTrapEnable", 3), ("warningTrapDisable", 19))).clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSyntesysWarningSeverityCode.setStatus('current')
if mibBuilder.loadTexts: alarmSyntesysWarningSeverityCode.setDescription('Defines the severity associated to alarmSyntesysStatus\n             and enables/disables the trap generation on status change event.')
alarmSyntesysStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cleared", 1), ("activeReportableStatus", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmSyntesysStatus.setStatus('current')
if mibBuilder.loadTexts: alarmSyntesysStatus.setDescription('OR of all Warning Alarms.')
alarmSyntesysStatusSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 18))).clone(namedValues=NamedValues(("disable", 1), ("statusTrapEnable", 2), ("statusTrapDisable", 18))).clone('statusTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmSyntesysStatusSeverityCode.setStatus('current')
if mibBuilder.loadTexts: alarmSyntesysStatusSeverityCode.setDescription('Defines the severity associated to alarmSyntesysStatus\n             and enables/disables the trap generation on status change event.')
alarmAntiFlooding = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmAntiFlooding.setStatus('current')
if mibBuilder.loadTexts: alarmAntiFlooding.setDescription("Enables or disables the alarm anti-flooding (filtering)\n             algorithm. According to such algorithm if the number of\n             event notifications that an alarm receives within a\n             specified time period, namely the observation period, exceeds\n             a given high threshold value, the alarm enters a 'flooding'\n             state. Once an alarm has entered such flooding state,\n             its status is forced to active, according to its related\n             severity, and no further event notifications are processed\n             (neither trapped nor logged).\n             An alarm exits the flooding state when the number of event\n             notifications, received within a subsequent observation\n             period, drops below a given low thresold value. On exiting\n             the flooding state, the trap and log status of an alarm get\n             aligned to the last notified event.")
alarmAntiFloodingWindow = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 29), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 120)).clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmAntiFloodingWindow.setStatus('current')
if mibBuilder.loadTexts: alarmAntiFloodingWindow.setDescription('Defines the time duration in seconds of the observation\n             period, during which the number of event notifications\n             of any alarm is checked to determine the alarm flooding\n             state.')
alarmAntiFloodingHighWater = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 30), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 10)).clone(3)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmAntiFloodingHighWater.setStatus('current')
if mibBuilder.loadTexts: alarmAntiFloodingHighWater.setDescription('Defines the threshold value of the number of event\n             notifications, occurring during the observation period,\n             beyond which an alarm enters the flooding state.')
alarmAntiFloodingLowWater = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 31), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alarmAntiFloodingLowWater.setStatus('current')
if mibBuilder.loadTexts: alarmAntiFloodingLowWater.setDescription('Defines the threshold value of the number of event\n             notifications, occurring during the observation period,\n             below which an alarm exits the flooding state. The value\n             being assigned to this leaf must be strictly lower than \n             the current value of leaf alarmAntiFloodingHighWater.')
alarmItemTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32), )
if mibBuilder.loadTexts: alarmItemTable.setStatus('current')
if mibBuilder.loadTexts: alarmItemTable.setDescription('Table with record of available alarms in the NE.\n             This table reports every created alarm in the NE.\n            ')
alarmRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32, 1), ).setIndexNames((0, "SIAE-ALARM-MIB", "alarmOid"))
if mibBuilder.loadTexts: alarmRecord.setStatus('current')
if mibBuilder.loadTexts: alarmRecord.setDescription('Alarm record.')
alarmOid = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmOid.setStatus('current')
if mibBuilder.loadTexts: alarmOid.setDescription('The Object Identifier of the Managed Object with\n             Alarms or Controls active (not cleared Alarm Status).')
alarmDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 32, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmDescription.setStatus('current')
if mibBuilder.loadTexts: alarmDescription.setDescription('ASCII string used to describe the alarm.')
alarmObjectId = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmObjectId.setStatus('current')
if mibBuilder.loadTexts: alarmObjectId.setDescription('OID of the status changed alarm\n             ')
alarmObjectVal = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 2), AlarmStatus()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmObjectVal.setStatus('current')
if mibBuilder.loadTexts: alarmObjectVal.setDescription('INTEGER value of the status changed alarm\n             ')
alarmTrapDescription = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmTrapDescription.setStatus('current')
if mibBuilder.loadTexts: alarmTrapDescription.setDescription('Optional Description of the notification\n             ')
alarmTrapNumber = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTrapNumber.setStatus('current')
if mibBuilder.loadTexts: alarmTrapNumber.setDescription('Sequential number of trap sent from NE\n             ')
alarmIpSnmpAgentAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 4, 2, 5), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: alarmIpSnmpAgentAddress.setStatus('current')
if mibBuilder.loadTexts: alarmIpSnmpAgentAddress.setDescription('Reflects the value of equipIpSnmpAgentAddress.\n             ')
alarmTrapObject = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 3373)).setObjects(("SIAE-ALARM-MIB", "alarmIpSnmpAgentAddress"), ("SIAE-ALARM-MIB", "alarmObjectId"), ("SIAE-ALARM-MIB", "alarmObjectVal"), ("SIAE-ALARM-MIB", "alarmTrapDescription"), ("SIAE-ALARM-MIB", "alarmTrapNumber"))
if mibBuilder.loadTexts: alarmTrapObject.setStatus('current')
if mibBuilder.loadTexts: alarmTrapObject.setDescription('This event is generated for every changed alarm status. \n             ')
alarmLogFTPStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 401)).setObjects(("SIAE-ALARM-MIB", "alarmIpSnmpAgentAddress"), ("SIAE-ALARM-MIB", "alarmLogFTPStatus"), ("SIAE-USER-MIB", "accessControlLoginIpAddress"))
if mibBuilder.loadTexts: alarmLogFTPStatusTrap.setStatus('current')
if mibBuilder.loadTexts: alarmLogFTPStatusTrap.setDescription('This event is generated when the status of FTP transfer is changed.\n             The data passed with the event are:\n                1) alarmIpSnmpAgentAddress\n                2) alarmLogFTPStatus\n                3) accessControlLoginIpAddress')
mibBuilder.exportSymbols("SIAE-ALARM-MIB", AlarmStatus=AlarmStatus, alarmLogTable=alarmLogTable, alarmActiveFloodingStatus=alarmActiveFloodingStatus, alarmLogFTPStatusTrap=alarmLogFTPStatusTrap, alarmLogFTPfile=alarmLogFTPfile, alarmActiveTable=alarmActiveTable, alarmActiveDescription=alarmActiveDescription, alarmActiveRecord=alarmActiveRecord, alarmMibVersion=alarmMibVersion, alarmTrap=alarmTrap, alarmLogLastEventTime=alarmLogLastEventTime, alarmLogStartHourEnable=alarmLogStartHourEnable, siaeNotificationEntry=siaeNotificationEntry, alarmRecord=alarmRecord, alarmLogObjectSev=alarmLogObjectSev, alarmLogStartTimeFilter=alarmLogStartTimeFilter, alarmSyntesysWarningSeverityCode=alarmSyntesysWarningSeverityCode, alarmOid=alarmOid, alarmLogAlarmSeverityFilter=alarmLogAlarmSeverityFilter, alarmLogRecordId=alarmLogRecordId, alarmActiveObjectVal=alarmActiveObjectVal, alarmObjectVal=alarmObjectVal, alarmSyntesysCritical=alarmSyntesysCritical, alarmLogAlarmSeverityEnable=alarmLogAlarmSeverityEnable, alarmLogFTPStatus=alarmLogFTPStatus, alarmTrapDescription=alarmTrapDescription, alarmLogManagedObjectFilter=alarmLogManagedObjectFilter, alarmSyntesysWarning=alarmSyntesysWarning, alarmActiveObjectId=alarmActiveObjectId, alarmLogObjectVal=alarmLogObjectVal, alarmLogActionRequest=alarmLogActionRequest, alarmObjectId=alarmObjectId, PYSNMP_MODULE_ID=smalarm, alarmIpSnmpAgentAddress=alarmIpSnmpAgentAddress, alarmSyntesysStatus=alarmSyntesysStatus, alarmLogEndHourEnable=alarmLogEndHourEnable, alarmSyntesysCriticalSeverityCode=alarmSyntesysCriticalSeverityCode, alarmLogEventTime=alarmLogEventTime, alarmItemTable=alarmItemTable, alarmDescription=alarmDescription, alarmLogRecord=alarmLogRecord, alarmActiveEventTime=alarmActiveEventTime, alarmLogObjectId=alarmLogObjectId, alarmSyntesysMinorSeverityCode=alarmSyntesysMinorSeverityCode, AlarmSeverityCode=AlarmSeverityCode, alarmAntiFloodingLowWater=alarmAntiFloodingLowWater, alarmTrapObject=alarmTrapObject, alarmSyntesysMajorSeverityCode=alarmSyntesysMajorSeverityCode, alarmSyntesysMinor=alarmSyntesysMinor, smalarm=smalarm, alarmSyntesysStatusSeverityCode=alarmSyntesysStatusSeverityCode, alarmAntiFloodingHighWater=alarmAntiFloodingHighWater, alarmSyntesysMajor=alarmSyntesysMajor, alarmLogDescription=alarmLogDescription, alarmAntiFloodingWindow=alarmAntiFloodingWindow, alarmLogEndTimeFilter=alarmLogEndTimeFilter, alarmTrapNumber=alarmTrapNumber, alarmLogFTPStatusTrapNotification=alarmLogFTPStatusTrapNotification, alarmAntiFlooding=alarmAntiFlooding)
