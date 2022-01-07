#
# PySNMP MIB module T11-FC-VIRTUAL-FABRIC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/T11-FC-VIRTUAL-FABRIC-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
fcmPortEntry, FcNameIdOrZero, fcmInstanceIndex, fcmSwitchEntry = mibBuilder.importSymbols("FC-MGMT-MIB", "fcmPortEntry", "FcNameIdOrZero", "fcmInstanceIndex", "fcmSwitchEntry")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
TextualConvention, StorageType, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "StorageType", "RowStatus", "DisplayString")
T11FabricIndex, = mibBuilder.importSymbols("T11-TC-MIB", "T11FabricIndex")
t11FcVirtualFabricMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 147))
t11FcVirtualFabricMIB.setRevisions(('2006-11-10 00:00',))
if mibBuilder.loadTexts: t11FcVirtualFabricMIB.setLastUpdated('200611100000Z')
if mibBuilder.loadTexts: t11FcVirtualFabricMIB.setOrganization('IETF IMSS (Internet and Management Support for Storage) Working Group')
t11vfObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 1))
t11vfConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 2))
t11vfCoreSwitchTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 1), )
if mibBuilder.loadTexts: t11vfCoreSwitchTable.setStatus('current')
t11vfCoreSwitchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 1, 1), ).setIndexNames((0, "FC-MGMT-MIB", "fcmInstanceIndex"), (0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchSwitchName"))
if mibBuilder.loadTexts: t11vfCoreSwitchEntry.setStatus('current')
t11vfCoreSwitchSwitchName = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 1), FcNameIdOrZero().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: t11vfCoreSwitchSwitchName.setStatus('current')
t11vfCoreSwitchMaxSupported = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfCoreSwitchMaxSupported.setStatus('current')
t11vfCoreSwitchStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 1, 1, 3), StorageType().clone('nonVolatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfCoreSwitchStorageType.setStatus('current')
t11vfVirtualSwitchTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 2), )
if mibBuilder.loadTexts: t11vfVirtualSwitchTable.setStatus('current')
t11vfVirtualSwitchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 2, 1), )
fcmSwitchEntry.registerAugmentions(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchEntry"))
t11vfVirtualSwitchEntry.setIndexNames(*fcmSwitchEntry.getIndexNames())
if mibBuilder.loadTexts: t11vfVirtualSwitchEntry.setStatus('current')
t11vfVirtualSwitchVfId = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 1), T11FabricIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfVirtualSwitchVfId.setStatus('current')
t11vfVirtualSwitchCoreSwitchName = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 2), FcNameIdOrZero().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11vfVirtualSwitchCoreSwitchName.setStatus('current')
t11vfVirtualSwitchRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfVirtualSwitchRowStatus.setStatus('current')
t11vfVirtualSwitchStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 2, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfVirtualSwitchStorageType.setStatus('current')
t11vfPortTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 3), )
if mibBuilder.loadTexts: t11vfPortTable.setStatus('current')
t11vfPortEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 3, 1), )
fcmPortEntry.registerAugmentions(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortEntry"))
t11vfPortEntry.setIndexNames(*fcmPortEntry.getIndexNames())
if mibBuilder.loadTexts: t11vfPortEntry.setStatus('current')
t11vfPortVfId = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 1), T11FabricIndex().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfPortVfId.setStatus('current')
t11vfPortTaggingAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("off", 1), ("on", 2), ("auto", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfPortTaggingAdminStatus.setStatus('current')
t11vfPortTaggingOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11vfPortTaggingOperStatus.setStatus('current')
t11vfPortStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 3, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: t11vfPortStorageType.setStatus('current')
t11vfLocallyEnabledTable = MibTable((1, 3, 6, 1, 2, 1, 147, 1, 4), )
if mibBuilder.loadTexts: t11vfLocallyEnabledTable.setStatus('current')
t11vfLocallyEnabledEntry = MibTableRow((1, 3, 6, 1, 2, 1, 147, 1, 4, 1), ).setIndexNames((0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledPortIfIndex"), (0, "T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledVfId"))
if mibBuilder.loadTexts: t11vfLocallyEnabledEntry.setStatus('current')
t11vfLocallyEnabledPortIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: t11vfLocallyEnabledPortIfIndex.setStatus('current')
t11vfLocallyEnabledVfId = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 2), T11FabricIndex())
if mibBuilder.loadTexts: t11vfLocallyEnabledVfId.setStatus('current')
t11vfLocallyEnabledOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("off", 1), ("on", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: t11vfLocallyEnabledOperStatus.setStatus('current')
t11vfLocallyEnabledRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfLocallyEnabledRowStatus.setStatus('current')
t11vfLocallyEnabledStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 147, 1, 4, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: t11vfLocallyEnabledStorageType.setStatus('current')
t11vfMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 2, 1))
t11vfMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 147, 2, 2))
t11vfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 147, 2, 1, 1)).setObjects(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11vfMIBCompliance = t11vfMIBCompliance.setStatus('current')
t11vfGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 147, 2, 2, 1)).setObjects(("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchMaxSupported"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchVfId"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchCoreSwitchName"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchRowStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortVfId"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortTaggingAdminStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledOperStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortTaggingOperStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledRowStatus"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfCoreSwitchStorageType"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfVirtualSwitchStorageType"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfPortStorageType"), ("T11-FC-VIRTUAL-FABRIC-MIB", "t11vfLocallyEnabledStorageType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    t11vfGeneralGroup = t11vfGeneralGroup.setStatus('current')
mibBuilder.exportSymbols("T11-FC-VIRTUAL-FABRIC-MIB", t11vfMIBGroups=t11vfMIBGroups, PYSNMP_MODULE_ID=t11FcVirtualFabricMIB, t11vfLocallyEnabledOperStatus=t11vfLocallyEnabledOperStatus, t11vfCoreSwitchStorageType=t11vfCoreSwitchStorageType, t11vfPortEntry=t11vfPortEntry, t11vfCoreSwitchEntry=t11vfCoreSwitchEntry, t11FcVirtualFabricMIB=t11FcVirtualFabricMIB, t11vfVirtualSwitchCoreSwitchName=t11vfVirtualSwitchCoreSwitchName, t11vfPortStorageType=t11vfPortStorageType, t11vfLocallyEnabledStorageType=t11vfLocallyEnabledStorageType, t11vfVirtualSwitchVfId=t11vfVirtualSwitchVfId, t11vfCoreSwitchSwitchName=t11vfCoreSwitchSwitchName, t11vfVirtualSwitchStorageType=t11vfVirtualSwitchStorageType, t11vfPortTaggingAdminStatus=t11vfPortTaggingAdminStatus, t11vfObjects=t11vfObjects, t11vfLocallyEnabledRowStatus=t11vfLocallyEnabledRowStatus, t11vfPortVfId=t11vfPortVfId, t11vfLocallyEnabledTable=t11vfLocallyEnabledTable, t11vfCoreSwitchMaxSupported=t11vfCoreSwitchMaxSupported, t11vfLocallyEnabledEntry=t11vfLocallyEnabledEntry, t11vfGeneralGroup=t11vfGeneralGroup, t11vfVirtualSwitchTable=t11vfVirtualSwitchTable, t11vfVirtualSwitchRowStatus=t11vfVirtualSwitchRowStatus, t11vfMIBCompliance=t11vfMIBCompliance, t11vfPortTaggingOperStatus=t11vfPortTaggingOperStatus, t11vfLocallyEnabledPortIfIndex=t11vfLocallyEnabledPortIfIndex, t11vfMIBCompliances=t11vfMIBCompliances, t11vfConformance=t11vfConformance, t11vfPortTable=t11vfPortTable, t11vfLocallyEnabledVfId=t11vfLocallyEnabledVfId, t11vfCoreSwitchTable=t11vfCoreSwitchTable, t11vfVirtualSwitchEntry=t11vfVirtualSwitchEntry)
