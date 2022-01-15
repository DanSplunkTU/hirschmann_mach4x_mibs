#
# PySNMP MIB module EdgeSwitch-LOGGING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/edgeswitch/EdgeSwitch-LOGGING-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:01:03 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
agentInventoryComponentIndex, = mibBuilder.importSymbols("EdgeSwitch-INVENTORY-MIB", "agentInventoryComponentIndex")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddress, InetPortNumber, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetPortNumber", "InetAddressType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Counter32, iso, TimeTicks, Bits, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, IpAddress, Unsigned32, ModuleIdentity, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter32", "iso", "TimeTicks", "Bits", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "IpAddress", "Unsigned32", "ModuleIdentity", "Gauge32")
TextualConvention, RowStatus, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "DateAndTime")
class AgentLogFacility(TextualConvention, Integer32):
    reference = 'RFC3164 - 4.1.1: Table 1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23))
    namedValues = NamedValues(("kernel", 0), ("user", 1), ("mail", 2), ("system", 3), ("security", 4), ("syslog", 5), ("lpr", 6), ("nntp", 7), ("uucp", 8), ("cron", 9), ("auth", 10), ("ftp", 11), ("ntp", 12), ("audit", 13), ("alert", 14), ("clock", 15), ("local0", 16), ("local1", 17), ("local2", 18), ("local3", 19), ("local4", 20), ("local5", 21), ("local6", 22), ("local7", 23))

class AgentLogSeverity(TextualConvention, Integer32):
    reference = 'RFC3164 - 4.1.1: Table 2'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("informational", 6), ("debug", 7))

fastPathLogging = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14))
fastPathLogging.setRevisions(('2011-01-26 00:00', '2007-05-23 00:00', '2004-10-26 13:03',))
if mibBuilder.loadTexts: fastPathLogging.setLastUpdated('201101260000Z')
if mibBuilder.loadTexts: fastPathLogging.setOrganization('Broadcom Inc')
agentLogConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1))
agentLogInMemoryConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 1))
agentLogInMemoryAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogInMemoryAdminStatus.setStatus('current')
agentLogInMemoryBehavior = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("wrap", 1), ("stop-on-full", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogInMemoryBehavior.setStatus('current')
agentLogConsoleConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 2))
agentLogConsoleAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogConsoleAdminStatus.setStatus('current')
agentLogConsoleSeverityFilter = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 2, 2), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogConsoleSeverityFilter.setStatus('current')
agentLogSysLogConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4))
agentLogSyslogAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogAdminStatus.setStatus('current')
agentLogSyslogLocalPort = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogLocalPort.setStatus('current')
agentLogSyslogMaxHosts = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMaxHosts.setStatus('current')
agentLogCliCommandsConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 5))
agentLogCliCommandsAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogCliCommandsAdminStatus.setStatus('current')
agentLogWebConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 7))
agentLogWebAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogWebAdminStatus.setStatus('current')
agentLogSnmpConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 8))
agentLogSnmpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSnmpAdminStatus.setStatus('current')
agentLogAuditConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 9))
agentLogAuditAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 9, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogAuditAdminStatus.setStatus('current')
agentLogSyslogHostTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 5), )
if mibBuilder.loadTexts: agentLogSyslogHostTable.setStatus('current')
agentLogSyslogHostEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 5, 1), ).setIndexNames((0, "EdgeSwitch-LOGGING-MIB", "agentLogHostTableIndex"))
if mibBuilder.loadTexts: agentLogSyslogHostEntry.setStatus('current')
agentLogHostTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentLogHostTableIndex.setStatus('current')
agentLogHostTableIpAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 5, 1, 2), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableIpAddressType.setStatus('current')
agentLogHostTableIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 5, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableIpAddress.setStatus('current')
agentLogHostTablePort = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTablePort.setStatus('current')
agentLogHostTableSeverityFilter = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 5, 1, 5), AgentLogSeverity()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableSeverityFilter.setStatus('current')
agentLogHostTableRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 5, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogHostTableRowStatus.setStatus('current')
agentLogSyslogSourceInterface = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 4, 6), InterfaceIndexOrZero()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogSyslogSourceInterface.setStatus('current')
agentLogStatisticsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2))
agentLogMessagesReceived = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessagesReceived.setStatus('current')
agentLogMessagesDropped = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessagesDropped.setStatus('current')
agentLogSyslogMessagesRelayed = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessagesRelayed.setStatus('current')
agentLogSyslogMessagesIgnored = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessagesIgnored.setStatus('deprecated')
agentLogMessageReceivedTime = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogMessageReceivedTime.setStatus('current')
agentLogSyslogMessageDeliveredTime = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogSyslogMessageDeliveredTime.setStatus('current')
agentLogEmailAlertConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6))
agentLogEmailAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailAdminStatus.setStatus('current')
agentLogEmailfromAddr = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailfromAddr.setStatus('current')
agentLogEmaillogDuration = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(30, 1440))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmaillogDuration.setStatus('current')
agentLogEmailUrgentSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 4), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailUrgentSeverity.setStatus('current')
agentLogEmailNonUrgentSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 5), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailNonUrgentSeverity.setStatus('current')
agentLogEmailTrapsSeverity = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 6), AgentLogSeverity()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailTrapsSeverity.setStatus('current')
agentLogEmailToAddrTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 7), )
if mibBuilder.loadTexts: agentLogEmailToAddrTable.setStatus('current')
agentLogEmailToAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 7, 1), ).setIndexNames((0, "EdgeSwitch-LOGGING-MIB", "agentLogEmailToAddrMessageType"), (0, "EdgeSwitch-LOGGING-MIB", "agentLogEmailToAddr"))
if mibBuilder.loadTexts: agentLogEmailToAddrEntry.setStatus('current')
agentLogEmailToAddrMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("critical", 1), ("non-critical", 2))))
if mibBuilder.loadTexts: agentLogEmailToAddrMessageType.setStatus('current')
agentLogEmailToAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 7, 1, 2), DisplayString())
if mibBuilder.loadTexts: agentLogEmailToAddr.setStatus('current')
agentLogEmailToAddrEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 7, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailToAddrEntryStatus.setStatus('current')
agentLogEmailSubjectTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 8), )
if mibBuilder.loadTexts: agentLogEmailSubjectTable.setStatus('current')
agentLogEmailSubjectEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 8, 1), ).setIndexNames((0, "EdgeSwitch-LOGGING-MIB", "agentLogEmailSubjectMessageType"))
if mibBuilder.loadTexts: agentLogEmailSubjectEntry.setStatus('current')
agentLogEmailSubjectMessageType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 8, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("critical", 1), ("non-critical", 2))))
if mibBuilder.loadTexts: agentLogEmailSubjectMessageType.setStatus('current')
agentLogEmailSubject = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 8, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailSubject.setStatus('current')
agentLogEmailSubjectEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 8, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailSubjectEntryStatus.setStatus('current')
agentLogEmailMailServerTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 9), )
if mibBuilder.loadTexts: agentLogEmailMailServerTable.setStatus('current')
agentLogEmailMailServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 9, 1), ).setIndexNames((0, "EdgeSwitch-LOGGING-MIB", "agentLogEmailSmtpAddrType"), (0, "EdgeSwitch-LOGGING-MIB", "agentLogEmailSmtpAddr"))
if mibBuilder.loadTexts: agentLogEmailMailServerEntry.setStatus('current')
agentLogEmailSmtpAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 9, 1, 1), InetAddressType())
if mibBuilder.loadTexts: agentLogEmailSmtpAddrType.setStatus('current')
agentLogEmailSmtpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 9, 1, 2), InetAddress())
if mibBuilder.loadTexts: agentLogEmailSmtpAddr.setStatus('current')
agentLogEmailSmtpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 9, 1, 3), InetPortNumber()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailSmtpPort.setStatus('current')
agentLogEmailSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("none", 1), ("tlsv1", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailSecurity.setStatus('current')
agentLogEmailloginID = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 9, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailloginID.setStatus('current')
agentLogEmailPassword = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 9, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailPassword.setStatus('current')
agentLogEmailEntryStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 1, 6, 9, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentLogEmailEntryStatus.setStatus('current')
agentLogEmailAlertStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 7))
agentLogEmailStatsemailsSentCount = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 7, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailStatsemailsSentCount.setStatus('current')
agentLogEmailStatsemailsFailureCount = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 7, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailStatsemailsFailureCount.setStatus('current')
agentLogEmailStatsTimeSinceLastEmailSent = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 7, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogEmailStatsTimeSinceLastEmailSent.setStatus('current')
agentLogEmailStatsClear = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 2, 7, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentLogEmailStatsClear.setStatus('current')
agentLogInMemoryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 3))
agentLogInMemoryLogCount = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogInMemoryLogCount.setStatus('current')
agentLogInMemoryTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 3, 2), )
if mibBuilder.loadTexts: agentLogInMemoryTable.setStatus('current')
agentLogInMemoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 3, 2, 1), ).setIndexNames((0, "EdgeSwitch-LOGGING-MIB", "agentLogInMemoryMsgIndex"))
if mibBuilder.loadTexts: agentLogInMemoryEntry.setStatus('current')
agentLogInMemoryMsgIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 3, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentLogInMemoryMsgIndex.setStatus('current')
agentLogInMemoryMsgText = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentLogInMemoryMsgText.setStatus('current')
agentLogTrapsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 5))
agentLogEmailAlertTrapsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 5, 1))
agentLogEmailSendFailed = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 14, 5, 1, 1)).setObjects(("EdgeSwitch-LOGGING-MIB", "agentLogEmailStatsemailsFailureCount"))
if mibBuilder.loadTexts: agentLogEmailSendFailed.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-LOGGING-MIB", agentLogEmailSubjectEntry=agentLogEmailSubjectEntry, agentLogEmailToAddrMessageType=agentLogEmailToAddrMessageType, agentLogCliCommandsAdminStatus=agentLogCliCommandsAdminStatus, agentLogHostTableIndex=agentLogHostTableIndex, agentLogEmailEntryStatus=agentLogEmailEntryStatus, agentLogConsoleAdminStatus=agentLogConsoleAdminStatus, agentLogHostTableIpAddress=agentLogHostTableIpAddress, agentLogAuditConfigGroup=agentLogAuditConfigGroup, agentLogEmailMailServerTable=agentLogEmailMailServerTable, agentLogSyslogLocalPort=agentLogSyslogLocalPort, PYSNMP_MODULE_ID=fastPathLogging, agentLogEmailSmtpAddrType=agentLogEmailSmtpAddrType, agentLogMessageReceivedTime=agentLogMessageReceivedTime, agentLogEmailSubjectTable=agentLogEmailSubjectTable, agentLogEmailStatsemailsFailureCount=agentLogEmailStatsemailsFailureCount, agentLogSyslogMaxHosts=agentLogSyslogMaxHosts, agentLogHostTableRowStatus=agentLogHostTableRowStatus, agentLogSyslogMessagesIgnored=agentLogSyslogMessagesIgnored, AgentLogFacility=AgentLogFacility, agentLogEmailAlertTrapsGroup=agentLogEmailAlertTrapsGroup, agentLogEmailToAddrEntryStatus=agentLogEmailToAddrEntryStatus, agentLogEmailToAddrEntry=agentLogEmailToAddrEntry, agentLogInMemoryTable=agentLogInMemoryTable, agentLogEmailToAddr=agentLogEmailToAddr, agentLogInMemoryConfigGroup=agentLogInMemoryConfigGroup, agentLogSyslogHostTable=agentLogSyslogHostTable, agentLogCliCommandsConfigGroup=agentLogCliCommandsConfigGroup, agentLogSnmpConfigGroup=agentLogSnmpConfigGroup, agentLogHostTableSeverityFilter=agentLogHostTableSeverityFilter, agentLogEmailSubjectMessageType=agentLogEmailSubjectMessageType, agentLogHostTableIpAddressType=agentLogHostTableIpAddressType, agentLogEmailNonUrgentSeverity=agentLogEmailNonUrgentSeverity, agentLogSysLogConfigGroup=agentLogSysLogConfigGroup, agentLogEmailPassword=agentLogEmailPassword, agentLogInMemoryMsgText=agentLogInMemoryMsgText, agentLogInMemoryBehavior=agentLogInMemoryBehavior, agentLogConsoleSeverityFilter=agentLogConsoleSeverityFilter, agentLogSnmpAdminStatus=agentLogSnmpAdminStatus, agentLogEmailToAddrTable=agentLogEmailToAddrTable, agentLogEmailloginID=agentLogEmailloginID, agentLogSyslogMessagesRelayed=agentLogSyslogMessagesRelayed, agentLogEmailSubjectEntryStatus=agentLogEmailSubjectEntryStatus, agentLogInMemoryLogCount=agentLogInMemoryLogCount, agentLogStatisticsGroup=agentLogStatisticsGroup, agentLogAuditAdminStatus=agentLogAuditAdminStatus, agentLogEmailStatsTimeSinceLastEmailSent=agentLogEmailStatsTimeSinceLastEmailSent, fastPathLogging=fastPathLogging, agentLogSyslogSourceInterface=agentLogSyslogSourceInterface, agentLogInMemoryMsgIndex=agentLogInMemoryMsgIndex, agentLogEmailMailServerEntry=agentLogEmailMailServerEntry, agentLogSyslogAdminStatus=agentLogSyslogAdminStatus, agentLogEmailSubject=agentLogEmailSubject, agentLogHostTablePort=agentLogHostTablePort, agentLogConfigGroup=agentLogConfigGroup, agentLogMessagesDropped=agentLogMessagesDropped, agentLogEmailSendFailed=agentLogEmailSendFailed, agentLogWebAdminStatus=agentLogWebAdminStatus, agentLogMessagesReceived=agentLogMessagesReceived, agentLogEmailUrgentSeverity=agentLogEmailUrgentSeverity, agentLogEmailTrapsSeverity=agentLogEmailTrapsSeverity, agentLogEmailfromAddr=agentLogEmailfromAddr, agentLogInMemoryEntry=agentLogInMemoryEntry, AgentLogSeverity=AgentLogSeverity, agentLogConsoleConfigGroup=agentLogConsoleConfigGroup, agentLogEmailAdminStatus=agentLogEmailAdminStatus, agentLogEmailStatsClear=agentLogEmailStatsClear, agentLogTrapsGroup=agentLogTrapsGroup, agentLogSyslogMessageDeliveredTime=agentLogSyslogMessageDeliveredTime, agentLogInMemoryAdminStatus=agentLogInMemoryAdminStatus, agentLogEmailAlertStatsGroup=agentLogEmailAlertStatsGroup, agentLogEmailSecurity=agentLogEmailSecurity, agentLogInMemoryGroup=agentLogInMemoryGroup, agentLogSyslogHostEntry=agentLogSyslogHostEntry, agentLogEmailSmtpAddr=agentLogEmailSmtpAddr, agentLogEmailStatsemailsSentCount=agentLogEmailStatsemailsSentCount, agentLogWebConfigGroup=agentLogWebConfigGroup, agentLogEmaillogDuration=agentLogEmaillogDuration, agentLogEmailSmtpPort=agentLogEmailSmtpPort, agentLogEmailAlertConfigGroup=agentLogEmailAlertConfigGroup)
