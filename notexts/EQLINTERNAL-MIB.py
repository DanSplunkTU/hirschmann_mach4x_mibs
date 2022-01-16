#
# PySNMP MIB module EQLINTERNAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLINTERNAL-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:32 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
UTFString, = mibBuilder.importSymbols("EQLGROUP-MIB", "UTFString")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, Bits, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, Integer32, IpAddress, iso, MibIdentifier, enterprises, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Bits", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "Integer32", "IpAddress", "iso", "MibIdentifier", "enterprises", "ObjectIdentity", "ModuleIdentity")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
eqlInternalModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 27))
eqlInternalModule.setRevisions(('2013-01-28 00:00',))
if mibBuilder.loadTexts: eqlInternalModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlInternalModule.setOrganization('Dell Inc.')
eqlInternalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 27, 1))
eqlMonitorTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1), )
if mibBuilder.loadTexts: eqlMonitorTable.setStatus('current')
eqlMonitorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1), ).setIndexNames((0, "EQLINTERNAL-MIB", "eqlMonitorIndex"))
if mibBuilder.loadTexts: eqlMonitorEntry.setStatus('current')
eqlMonitorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlMonitorIndex.setStatus('current')
eqlMonitorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorRowStatus.setStatus('current')
eqlMonitorUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorUUID.setStatus('current')
eqlMonitorServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 4), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorServerName.setStatus('current')
eqlMonitorDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 5), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorDomainName.setStatus('current')
eqlMonitorInetAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 6), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorInetAddressType.setStatus('current')
eqlMonitorInetAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 7), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorInetAddress.setStatus('current')
eqlMonitorSupportAssist = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("supportAssistNone", 0), ("supportAssistInstalledNotEnabled", 1), ("supportAssistEnabled", 2), ("supportAssistCommunicatingWithDell", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorSupportAssist.setStatus('current')
eqlMonitorTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 9), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorTimestamp.setStatus('current')
eqlMonitorSupportAssistTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 10), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorSupportAssistTimestamp.setStatus('current')
eqlMonitorLicensingTimestamp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 11), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorLicensingTimestamp.setStatus('current')
eqlMonitorDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 1, 1, 12), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlMonitorDescription.setStatus('current')
eqlMonitorStatusTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 27, 1, 2), )
if mibBuilder.loadTexts: eqlMonitorStatusTable.setStatus('current')
eqlMonitorStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 27, 1, 2, 1), ).setIndexNames((0, "EQLINTERNAL-MIB", "eqlMonitorIndex"))
if mibBuilder.loadTexts: eqlMonitorStatusEntry.setStatus('current')
eqlMonitorStatusReminder = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 27, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("monitoringExpired", 0), ("monitoringCurrent", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlMonitorStatusReminder.setStatus('current')
mibBuilder.exportSymbols("EQLINTERNAL-MIB", eqlMonitorServerName=eqlMonitorServerName, eqlMonitorTable=eqlMonitorTable, eqlMonitorStatusEntry=eqlMonitorStatusEntry, eqlMonitorLicensingTimestamp=eqlMonitorLicensingTimestamp, eqlMonitorSupportAssist=eqlMonitorSupportAssist, eqlMonitorStatusReminder=eqlMonitorStatusReminder, eqlMonitorSupportAssistTimestamp=eqlMonitorSupportAssistTimestamp, eqlMonitorDescription=eqlMonitorDescription, eqlMonitorIndex=eqlMonitorIndex, eqlInternalObjects=eqlInternalObjects, eqlMonitorEntry=eqlMonitorEntry, eqlMonitorUUID=eqlMonitorUUID, eqlMonitorStatusTable=eqlMonitorStatusTable, eqlMonitorRowStatus=eqlMonitorRowStatus, PYSNMP_MODULE_ID=eqlInternalModule, eqlMonitorInetAddress=eqlMonitorInetAddress, eqlMonitorInetAddressType=eqlMonitorInetAddressType, eqlInternalModule=eqlInternalModule, eqlMonitorDomainName=eqlMonitorDomainName, eqlMonitorTimestamp=eqlMonitorTimestamp)
