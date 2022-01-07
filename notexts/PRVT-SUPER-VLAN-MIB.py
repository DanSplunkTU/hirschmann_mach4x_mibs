#
# PySNMP MIB module PRVT-SUPER-VLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-SUPER-VLAN-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:32 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, NotificationType, Unsigned32, Counter64, MibIdentifier, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, TimeTicks, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "NotificationType", "Unsigned32", "Counter64", "MibIdentifier", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
prvtSuperVlanMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 136))
prvtSuperVlanMIB.setRevisions(('2010-08-04 00:00',))
if mibBuilder.loadTexts: prvtSuperVlanMIB.setLastUpdated('201008040000Z')
if mibBuilder.loadTexts: prvtSuperVlanMIB.setOrganization('BATM Advanced Communication')
prvtSuperVlanMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1))
prvtSuperVlanIfTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 1), )
if mibBuilder.loadTexts: prvtSuperVlanIfTable.setStatus('current')
prvtSuperVlanIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 1, 1), ).setIndexNames((0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfIndex"))
if mibBuilder.loadTexts: prvtSuperVlanIfEntry.setStatus('current')
prvtSuperVlanIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: prvtSuperVlanIfIndex.setStatus('current')
prvtSuperVlanIfTargetPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 1, 1, 2), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtSuperVlanIfTargetPort.setStatus('current')
prvtSuperVlanIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtSuperVlanIfRowStatus.setStatus('current')
prvtSuperVlanIfCVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 2), )
if mibBuilder.loadTexts: prvtSuperVlanIfCVlanTable.setStatus('current')
prvtSuperVlanIfCVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 2, 1), ).setIndexNames((0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfIndex"), (0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfCVlanId"))
if mibBuilder.loadTexts: prvtSuperVlanIfCVlanEntry.setStatus('current')
prvtSuperVlanIfCVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4092)))
if mibBuilder.loadTexts: prvtSuperVlanIfCVlanId.setStatus('current')
prvtSuperVlanIfCVlanMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtSuperVlanIfCVlanMask.setStatus('current')
prvtSuperVlanIfCVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtSuperVlanIfCVlanRowStatus.setStatus('current')
prvtSuperVlanIfRingPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 3), )
if mibBuilder.loadTexts: prvtSuperVlanIfRingPortTable.setStatus('current')
prvtSuperVlanIfRingPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 3, 1), ).setIndexNames((0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfIndex"), (0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfRingPort1"), (0, "PRVT-SUPER-VLAN-MIB", "prvtSuperVlanIfRingPort2"))
if mibBuilder.loadTexts: prvtSuperVlanIfRingPortEntry.setStatus('current')
prvtSuperVlanIfRingPort1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: prvtSuperVlanIfRingPort1.setStatus('current')
prvtSuperVlanIfRingPort2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 3, 1, 2), InterfaceIndex())
if mibBuilder.loadTexts: prvtSuperVlanIfRingPort2.setStatus('current')
prvtSuperVlanIfRingPortVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4092))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtSuperVlanIfRingPortVlanId.setStatus('current')
prvtSuperVlanIfRingPortPreferred = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtSuperVlanIfRingPortPreferred.setStatus('current')
prvtSuperVlanIfRingPortActive = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 3, 1, 5), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtSuperVlanIfRingPortActive.setStatus('current')
prvtSuperVlanIfRingPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 136, 1, 3, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtSuperVlanIfRingPortRowStatus.setStatus('current')
mibBuilder.exportSymbols("PRVT-SUPER-VLAN-MIB", prvtSuperVlanIfRingPort1=prvtSuperVlanIfRingPort1, prvtSuperVlanIfTargetPort=prvtSuperVlanIfTargetPort, prvtSuperVlanIfEntry=prvtSuperVlanIfEntry, prvtSuperVlanIfCVlanTable=prvtSuperVlanIfCVlanTable, PYSNMP_MODULE_ID=prvtSuperVlanMIB, prvtSuperVlanIfRingPortEntry=prvtSuperVlanIfRingPortEntry, prvtSuperVlanIfRingPortActive=prvtSuperVlanIfRingPortActive, prvtSuperVlanMIB=prvtSuperVlanMIB, prvtSuperVlanIfIndex=prvtSuperVlanIfIndex, prvtSuperVlanIfRowStatus=prvtSuperVlanIfRowStatus, prvtSuperVlanIfRingPortTable=prvtSuperVlanIfRingPortTable, prvtSuperVlanIfRingPortRowStatus=prvtSuperVlanIfRingPortRowStatus, prvtSuperVlanIfCVlanRowStatus=prvtSuperVlanIfCVlanRowStatus, prvtSuperVlanMIBObjects=prvtSuperVlanMIBObjects, prvtSuperVlanIfCVlanMask=prvtSuperVlanIfCVlanMask, prvtSuperVlanIfRingPort2=prvtSuperVlanIfRingPort2, prvtSuperVlanIfCVlanId=prvtSuperVlanIfCVlanId, prvtSuperVlanIfRingPortPreferred=prvtSuperVlanIfRingPortPreferred, prvtSuperVlanIfCVlanEntry=prvtSuperVlanIfCVlanEntry, prvtSuperVlanIfRingPortVlanId=prvtSuperVlanIfRingPortVlanId, prvtSuperVlanIfTable=prvtSuperVlanIfTable)
