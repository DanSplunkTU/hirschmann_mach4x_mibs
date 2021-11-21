#
# PySNMP MIB module SIAE-SECURITY-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SECURITY-MANAGEMENT-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:48:49 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, Integer32, Bits, ObjectIdentity, TimeTicks, Unsigned32, IpAddress, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "Integer32", "Bits", "ObjectIdentity", "TimeTicks", "Unsigned32", "IpAddress", "Counter32", "iso")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
securityManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 82))
securityManagement.setRevisions(('2014-04-17 00:00',))
if mibBuilder.loadTexts: securityManagement.setLastUpdated('201404170000Z')
if mibBuilder.loadTexts: securityManagement.setOrganization('SIAE MICROELETTRONICA spa')
securityManagementMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: securityManagementMibVersion.setStatus('current')
servicesTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2), )
if mibBuilder.loadTexts: servicesTable.setStatus('current')
serviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1), ).setIndexNames((0, "SIAE-SECURITY-MANAGEMENT-MIB", "serviceIndex"))
if mibBuilder.loadTexts: serviceEntry.setStatus('current')
serviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceIndex.setStatus('current')
serviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceName.setStatus('current')
serviceProtocolVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceProtocolVersion.setStatus('current')
serviceAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: serviceAdminStatus.setStatus('current')
serviceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notAvailable", 0), ("running", 1), ("stopped", 2))).clone('notAvailable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: serviceOperStatus.setStatus('current')
serviceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 82, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: serviceRowStatus.setStatus('current')
mibBuilder.exportSymbols("SIAE-SECURITY-MANAGEMENT-MIB", serviceOperStatus=serviceOperStatus, serviceRowStatus=serviceRowStatus, servicesTable=servicesTable, serviceIndex=serviceIndex, serviceName=serviceName, securityManagementMibVersion=securityManagementMibVersion, serviceEntry=serviceEntry, serviceProtocolVersion=serviceProtocolVersion, serviceAdminStatus=serviceAdminStatus, PYSNMP_MODULE_ID=securityManagement, securityManagement=securityManagement)
