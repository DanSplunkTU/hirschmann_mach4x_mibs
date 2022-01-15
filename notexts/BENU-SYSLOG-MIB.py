#
# PySNMP MIB module BENU-SYSLOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-SYSLOG-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:52:55 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
InetPortNumber, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetPortNumber")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, iso, MibIdentifier, ObjectIdentity, Integer32, Unsigned32, Counter32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "iso", "MibIdentifier", "ObjectIdentity", "Integer32", "Unsigned32", "Counter32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuSyslog = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 3))
benuSyslog.setRevisions(('2015-01-09 00:00', '2014-11-06 00:00', '2013-11-22 00:00',))
if mibBuilder.loadTexts: benuSyslog.setLastUpdated('201501090000Z')
if mibBuilder.loadTexts: benuSyslog.setOrganization('Benu Networks')
bSyslogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 3, 0))
bSyslogSize = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSyslogSize.setStatus('current')
bSyslogMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4096, 5242880)).clone(4096)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bSyslogMaxSize.setStatus('current')
bSyslogServerEnable = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bSyslogServerEnable.setStatus('current')
bSyslogServerTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 1, 3, 4), )
if mibBuilder.loadTexts: bSyslogServerTable.setStatus('current')
bSyslogServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1), ).setIndexNames((0, "BENU-SYSLOG-MIB", "bSyslogServerIndex"))
if mibBuilder.loadTexts: bSyslogServerEntry.setStatus('current')
bSyslogServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bSyslogServerIndex.setStatus('current')
bSyslogServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSyslogServerAddress.setStatus('current')
bSyslogServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 1, 3, 4, 1, 3), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bSyslogServerPort.setStatus('current')
bSyslogSeverity = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergencies", 0), ("alerts", 1), ("critical", 2), ("errors", 3), ("warnings", 4), ("notifications", 5), ("informational", 6), ("debugging", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bSyslogSeverity.setStatus('current')
bSyslogConsoleSeverity = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergencies", 0), ("alerts", 1), ("critical", 2), ("errors", 3), ("warnings", 4), ("notifications", 5), ("informational", 6), ("debugging", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bSyslogConsoleSeverity.setStatus('current')
bSyslogClear = MibScalar((1, 3, 6, 1, 4, 1, 39406, 1, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bSyslogClear.setStatus('current')
mibBuilder.exportSymbols("BENU-SYSLOG-MIB", bSyslogServerAddress=bSyslogServerAddress, PYSNMP_MODULE_ID=benuSyslog, bSyslogSeverity=bSyslogSeverity, bSyslogServerIndex=bSyslogServerIndex, bSyslogServerTable=bSyslogServerTable, bSyslogServerPort=bSyslogServerPort, bSyslogConsoleSeverity=bSyslogConsoleSeverity, bSyslogServerEntry=bSyslogServerEntry, bSyslogServerEnable=bSyslogServerEnable, bSyslogClear=bSyslogClear, bSyslogNotifications=bSyslogNotifications, benuSyslog=benuSyslog, bSyslogSize=bSyslogSize, bSyslogMaxSize=bSyslogMaxSize)
