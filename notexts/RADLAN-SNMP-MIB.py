#
# PySNMP MIB module RADLAN-SNMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SNMP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:36:09 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, NotificationType, Bits, Counter64, TimeTicks, iso, Counter32, Unsigned32, MibIdentifier, Gauge32, ObjectIdentity, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "NotificationType", "Bits", "Counter64", "TimeTicks", "iso", "Counter32", "Unsigned32", "MibIdentifier", "Gauge32", "ObjectIdentity", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlSNMP = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 98))
rlSNMP.setRevisions(('1904-10-20 00:00',))
if mibBuilder.loadTexts: rlSNMP.setLastUpdated('0410200000Z')
if mibBuilder.loadTexts: rlSNMP.setOrganization('Radlan Computer Communications Ltd.')
rlSNMPv3 = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 98, 1))
rlTargetParamsTestingLevel = MibScalar((1, 3, 6, 1, 4, 1, 89, 98, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlTargetParamsTestingLevel.setStatus('current')
rlNotifyFilterTestingLevel = MibScalar((1, 3, 6, 1, 4, 1, 89, 98, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("low", 1), ("high", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlNotifyFilterTestingLevel.setStatus('current')
rlSnmpEngineID = MibScalar((1, 3, 6, 1, 4, 1, 89, 98, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 32)).clone(hexValue="0000000001")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSnmpEngineID.setStatus('current')
rlSNMPDomains = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 98, 2))
rlSnmpUDPMridDomain = ObjectIdentity((1, 3, 6, 1, 4, 1, 89, 98, 2, 1))
if mibBuilder.loadTexts: rlSnmpUDPMridDomain.setStatus('current')
class RlSnmpUDPMridAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d/2d/2d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

rlSnmpRequestMridTable = MibTable((1, 3, 6, 1, 4, 1, 89, 98, 3), )
if mibBuilder.loadTexts: rlSnmpRequestMridTable.setStatus('current')
rlSnmpRequestMridEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 98, 3, 1), ).setIndexNames((0, "RADLAN-SNMP-MIB", "rlSnmpRequestManagedMrid"))
if mibBuilder.loadTexts: rlSnmpRequestMridEntry.setStatus('current')
rlSnmpRequestManagedMrid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 98, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSnmpRequestManagedMrid.setStatus('current')
rlSnmpRequestMridStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 98, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("enable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSnmpRequestMridStatus.setStatus('current')
mibBuilder.exportSymbols("RADLAN-SNMP-MIB", rlSnmpUDPMridDomain=rlSnmpUDPMridDomain, rlSnmpRequestManagedMrid=rlSnmpRequestManagedMrid, rlSNMPv3=rlSNMPv3, rlSnmpEngineID=rlSnmpEngineID, RlSnmpUDPMridAddress=RlSnmpUDPMridAddress, rlTargetParamsTestingLevel=rlTargetParamsTestingLevel, rlSnmpRequestMridEntry=rlSnmpRequestMridEntry, PYSNMP_MODULE_ID=rlSNMP, rlSNMP=rlSNMP, rlSNMPDomains=rlSNMPDomains, rlSnmpRequestMridStatus=rlSnmpRequestMridStatus, rlNotifyFilterTestingLevel=rlNotifyFilterTestingLevel, rlSnmpRequestMridTable=rlSnmpRequestMridTable)
