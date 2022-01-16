#
# PySNMP MIB module RADLAN-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SYSLOG-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:43:10 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Bits, Gauge32, iso, Unsigned32, ObjectIdentity, Counter64, Integer32, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Gauge32", "iso", "Unsigned32", "ObjectIdentity", "Counter64", "Integer32", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "NotificationType")
DisplayString, TruthValue, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention", "RowStatus")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlSyslog = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 82))
rlSyslog.setRevisions(('2003-09-22 00:00',))
if mibBuilder.loadTexts: rlSyslog.setLastUpdated('200309220000Z')
if mibBuilder.loadTexts: rlSyslog.setOrganization('Radlan Computer Communications Ltd.')
class RlSyslogSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7), ("notActive", 8))

rlSyslogPrivate = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 82, 2))
rlSyslogGlobalEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 1), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogGlobalEnable.setStatus('current')
rlSyslogMinLogToConsoleSeverity = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 2), RlSyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToConsoleSeverity.setStatus('current')
rlSyslogMinLogToFileSeverity = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 3), RlSyslogSeverity().clone('error')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToFileSeverity.setStatus('current')
rlSyslogMinLogToCacheSeverity = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 4), RlSyslogSeverity().clone('info')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogMinLogToCacheSeverity.setStatus('current')
rlSyslogClearLogfile = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 5), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogClearLogfile.setStatus('current')
rlSyslogClearCache = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 6), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogClearCache.setStatus('current')
rlSyslogMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogMibVersion.setStatus('current')
rlSyslogLogTable = MibTable((1, 3, 6, 1, 4, 1, 89, 82, 2, 8), )
if mibBuilder.loadTexts: rlSyslogLogTable.setStatus('current')
rlSyslogLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1), ).setIndexNames((0, "RADLAN-SYSLOG-MIB", "rlSyslogLogCounter"))
if mibBuilder.loadTexts: rlSyslogLogEntry.setStatus('current')
rlSyslogLogCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCounter.setStatus('current')
rlSyslogLogDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogDateTime.setStatus('current')
rlSyslogLogAppMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogAppMnemonic.setStatus('current')
rlSyslogLogSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 4), RlSyslogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogSeverity.setStatus('current')
rlSyslogLogMessageMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogMessageMnemonic.setStatus('current')
rlSyslogLogText1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText1.setStatus('current')
rlSyslogLogText2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText2.setStatus('current')
rlSyslogLogText3 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText3.setStatus('current')
rlSyslogLogText4 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 8, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogText4.setStatus('current')
rlSyslogLogCacheTable = MibTable((1, 3, 6, 1, 4, 1, 89, 82, 2, 9), )
if mibBuilder.loadTexts: rlSyslogLogCacheTable.setStatus('current')
rlSyslogLogCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1), ).setIndexNames((0, "RADLAN-SYSLOG-MIB", "rlSyslogLogCacheCounter"))
if mibBuilder.loadTexts: rlSyslogLogCacheEntry.setStatus('current')
rlSyslogLogCacheCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheCounter.setStatus('current')
rlSyslogLogCacheDateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheDateTime.setStatus('current')
rlSyslogLogCacheAppMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheAppMnemonic.setStatus('current')
rlSyslogLogCacheSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 4), RlSyslogSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheSeverity.setStatus('current')
rlSyslogLogCacheMessageMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheMessageMnemonic.setStatus('current')
rlSyslogLogCacheText1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText1.setStatus('current')
rlSyslogLogCacheText2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText2.setStatus('current')
rlSyslogLogCacheText3 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText3.setStatus('current')
rlSyslogLogCacheText4 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 82, 2, 9, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogLogCacheText4.setStatus('current')
rlSyslogConsoleMessagesIgnored = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogConsoleMessagesIgnored.setStatus('current')
rlSyslogFileMessagesIgnored = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogFileMessagesIgnored.setStatus('current')
rlSyslogFileMessagesLogged = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogFileMessagesLogged.setStatus('current')
rlSyslogCacheTotalMessages = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 2, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSyslogCacheTotalMessages.setStatus('current')
rlSyslogPhaseOneTests = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 82, 3))
rlSyslogPhaseOneTestGenerator = MibScalar((1, 3, 6, 1, 4, 1, 89, 82, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(11, 12, 13, 14, 15, 16, 17, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 36, 41, 42, 43, 47, 62))).clone(namedValues=NamedValues(("successfulRegistration", 11), ("regTheSameComponentTwice", 12), ("regWithInvalidComponentID", 13), ("regWithInvalidApplicationID", 14), ("regWithInvalidMessageString", 15), ("regWithInvalidMessageList", 16), ("regWithInvalidApplicationList", 17), ("successfulLoggingWithNoParams", 21), ("logWithUnregisteredComponentID", 22), ("logWithInvalidComponentID", 23), ("logWithBadApplicationID", 24), ("logWithBadMessageID", 25), ("paramFormatting", 31), ("insufficientParams", 32), ("incorrectParams", 33), ("tooManyParams", 34), ("oversizedParams", 35), ("trapParams", 36), ("successfulFatalError", 41), ("fatalErrorThroughNonFatalInterface", 42), ("nonFatalErrorThroughFatalInterface", 43), ("nestedFatalErrors", 47), ("snmpAccessToLongMessage", 62)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSyslogPhaseOneTestGenerator.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SYSLOG-MIB", rlSyslogClearCache=rlSyslogClearCache, rlSyslogMibVersion=rlSyslogMibVersion, rlSyslogLogCacheText3=rlSyslogLogCacheText3, rlSyslogPhaseOneTestGenerator=rlSyslogPhaseOneTestGenerator, rlSyslogLogCacheCounter=rlSyslogLogCacheCounter, rlSyslogLogCacheText4=rlSyslogLogCacheText4, rlSyslogLogCacheText1=rlSyslogLogCacheText1, rlSyslogMinLogToFileSeverity=rlSyslogMinLogToFileSeverity, rlSyslogClearLogfile=rlSyslogClearLogfile, rlSyslogGlobalEnable=rlSyslogGlobalEnable, rlSyslogLogAppMnemonic=rlSyslogLogAppMnemonic, rlSyslogLogSeverity=rlSyslogLogSeverity, rlSyslogLogText2=rlSyslogLogText2, rlSyslogMinLogToConsoleSeverity=rlSyslogMinLogToConsoleSeverity, rlSyslogLogDateTime=rlSyslogLogDateTime, rlSyslogLogCacheMessageMnemonic=rlSyslogLogCacheMessageMnemonic, rlSyslogLogCacheSeverity=rlSyslogLogCacheSeverity, rlSyslog=rlSyslog, rlSyslogMinLogToCacheSeverity=rlSyslogMinLogToCacheSeverity, rlSyslogLogText1=rlSyslogLogText1, rlSyslogLogCacheDateTime=rlSyslogLogCacheDateTime, rlSyslogFileMessagesLogged=rlSyslogFileMessagesLogged, rlSyslogLogTable=rlSyslogLogTable, rlSyslogConsoleMessagesIgnored=rlSyslogConsoleMessagesIgnored, rlSyslogLogCounter=rlSyslogLogCounter, rlSyslogLogCacheTable=rlSyslogLogCacheTable, rlSyslogLogEntry=rlSyslogLogEntry, rlSyslogPhaseOneTests=rlSyslogPhaseOneTests, RlSyslogSeverity=RlSyslogSeverity, rlSyslogCacheTotalMessages=rlSyslogCacheTotalMessages, PYSNMP_MODULE_ID=rlSyslog, rlSyslogPrivate=rlSyslogPrivate, rlSyslogLogCacheText2=rlSyslogLogCacheText2, rlSyslogFileMessagesIgnored=rlSyslogFileMessagesIgnored, rlSyslogLogText3=rlSyslogLogText3, rlSyslogLogText4=rlSyslogLogText4, rlSyslogLogMessageMnemonic=rlSyslogLogMessageMnemonic, rlSyslogLogCacheAppMnemonic=rlSyslogLogCacheAppMnemonic, rlSyslogLogCacheEntry=rlSyslogLogCacheEntry)
