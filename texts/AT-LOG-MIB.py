#
# PySNMP MIB module AT-LOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-LOG-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:24:51 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter64, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, TimeTicks, ModuleIdentity, NotificationType, Integer32, Unsigned32, Gauge32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "TimeTicks", "ModuleIdentity", "NotificationType", "Integer32", "Unsigned32", "Gauge32", "ObjectIdentity", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
log = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601))
log.setRevisions(('2016-06-23 00:00', '2012-06-08 00:00', '2012-06-07 00:00', '2011-05-30 00:00', '2011-04-18 00:00', '2010-09-07 00:00', '2010-06-14 05:11', '2008-10-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: log.setRevisionsDescriptions(('The AT Log MIB, for listing log entries from the buffered and permament logs.', 'Change OCTET STRING to DisplayString for all MIBs.', 'Change the MAX-ACCESS for the logIndex to not-accessible.', 'Updated enumeration type to use INTEGER.', 'Reformatted MIB file.', 'Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'Initial revision.',))
if mibBuilder.loadTexts: log.setLastUpdated('201606230000Z')
if mibBuilder.loadTexts: log.setOrganization('Allied Telesis Labs New Zealand')
if mibBuilder.loadTexts: log.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: log.setDescription('Added logProcessKilledNotify and MIB variable logProcessKilled.')
logNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 0))
logProcessKilledNotify = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 0, 1)).setObjects(("AT-LOG-MIB", "logProcessKilled"))
if mibBuilder.loadTexts: logProcessKilledNotify.setStatus('current')
if mibBuilder.loadTexts: logProcessKilledNotify.setDescription('A notification is generated when a process is killed.')
logTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1), )
if mibBuilder.loadTexts: logTable.setStatus('current')
if mibBuilder.loadTexts: logTable.setDescription('A list of log entries from the source specified in the\n                logSource object. The list is ordered from oldest entry to\n                newest entry.')
logEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1), ).setIndexNames((0, "AT-LOG-MIB", "logIndex"))
if mibBuilder.loadTexts: logEntry.setStatus('current')
if mibBuilder.loadTexts: logEntry.setDescription('A log entry from the source specified in the logSource object.')
logIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: logIndex.setStatus('current')
if mibBuilder.loadTexts: logIndex.setDescription('An index value. This index is not directly tied to any\n                specific log entry. Over time, the log will grow larger and\n                eventually older entries will be removed.')
logDate = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logDate.setStatus('current')
if mibBuilder.loadTexts: logDate.setDescription('The date that the log was generated, in the form YYYY MMM DD,\n                eg: 2008 Oct  9.')
logTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logTime.setStatus('current')
if mibBuilder.loadTexts: logTime.setDescription('The time that the log was generated, in the form HH:MM:SS,\n                eg: 07:15:04.')
logFacility = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logFacility.setStatus('current')
if mibBuilder.loadTexts: logFacility.setDescription('The syslog facility that generated the log entry. See the\n                Software Reference Manual for more information.')
logSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logSeverity.setStatus('current')
if mibBuilder.loadTexts: logSeverity.setDescription('The severity level of the log entry:\n\n                  emerg     Emergency, system is unusable\n                  alert     Action must be taken immediately\n                  crit      Critical conditions\n                  err       Error conditions\n                  warning   Warning conditions\n                  notice    Normal, but significant, conditions\n                  info      Informational messages\n                  debug     Debug-level messages')
logProgram = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logProgram.setStatus('current')
if mibBuilder.loadTexts: logProgram.setDescription('The program that generated the log entry. See the Software\n                Reference Manual for more information.')
logMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logMessage.setStatus('current')
if mibBuilder.loadTexts: logMessage.setDescription('The log message.')
logOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2))
logSource = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bufferedLog", 1), ("permanentLog", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logSource.setStatus('current')
if mibBuilder.loadTexts: logSource.setDescription('The source to retrieve the log entries from. Valid values are:\n\n                  1 - Buffered log\n                  2 - Permanent log\n\n                This source is used when retrieving the logTable objects, and\n                also specifies the log to be cleared when the clearLog object\n                is set.')
logAll = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: logAll.setStatus('current')
if mibBuilder.loadTexts: logAll.setDescription('Determines the quantity of logs to be retrieved. Valid values\n                are:\n\n                  0 - Display only recent log messages\n                  1 - Show all available log entries.\n\n                Note: Choosing to retrieve all log entries may result in a\n                delay of several seconds before they may be viewed via SNMP.')
clearLog = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: clearLog.setStatus('current')
if mibBuilder.loadTexts: clearLog.setDescription('Set with a value of 1 to clear the log that is specified by\n                the logSource object.')
logProcessKilled = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 601, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: logProcessKilled.setStatus('current')
if mibBuilder.loadTexts: logProcessKilled.setDescription('The process name that a process daemon was killed. This MIB variable is a\n                placeholder for the logProcessKilledNotify, but can be read independently if required.\n                A new process killed event can update this variable. No message will be displayed if\n                the specified process has not been killed after the device was first booted.')
mibBuilder.exportSymbols("AT-LOG-MIB", logAll=logAll, logOptions=logOptions, logSource=logSource, logMessage=logMessage, logEntry=logEntry, clearLog=clearLog, logProcessKilled=logProcessKilled, logTable=logTable, log=log, logSeverity=logSeverity, logProgram=logProgram, logFacility=logFacility, logIndex=logIndex, logNotifications=logNotifications, logDate=logDate, logTime=logTime, logProcessKilledNotify=logProcessKilledNotify, PYSNMP_MODULE_ID=log)
