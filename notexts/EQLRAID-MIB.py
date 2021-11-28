#
# PySNMP MIB module EQLRAID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLRAID-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:18:03 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
eqlGroupId, = mibBuilder.importSymbols("EQLGROUP-MIB", "eqlGroupId")
eqlDriveGroupIndex, eqlMemberIndex = mibBuilder.importSymbols("EQLMEMBER-MIB", "eqlDriveGroupIndex", "eqlMemberIndex")
eqlStoragePoolIndex, = mibBuilder.importSymbols("EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ifEntry, = mibBuilder.importSymbols("IF-MIB", "ifEntry")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter32, ModuleIdentity, NotificationType, IpAddress, MibIdentifier, Gauge32, Unsigned32, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter32", "ModuleIdentity", "NotificationType", "IpAddress", "MibIdentifier", "Gauge32", "Unsigned32", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Bits", "TimeTicks")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
eqlRAIDModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 10))
eqlRAIDModule.setRevisions(('2002-11-11 00:00',))
if mibBuilder.loadTexts: eqlRAIDModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlRAIDModule.setOrganization('EqualLogic Inc.')
eqlRAIDObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 10, 1))
eqlRAIDNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 10, 2))
eqlRAIDConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 10, 3))
eqlRAIDDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1), )
if mibBuilder.loadTexts: eqlRAIDDeviceTable.setStatus('current')
eqlRAIDDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"))
if mibBuilder.loadTexts: eqlRAIDDeviceEntry.setStatus('current')
eqlRAIDDeviceLUNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLUNIndex.setStatus('current')
eqlRAIDDeviceLUN = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLUN.setStatus('current')
eqlRAIDDeviceOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noDevice", 1), ("dataLoss", 2), ("nominal", 3), ("degraded", 4), ("failed", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceOperStatus.setStatus('current')
eqlRAIDDeviceUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceUUID.setStatus('current')
eqlRAIDDeviceDriveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceDriveCount.setStatus('current')
eqlRAIDDeviceLayoutOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noOp", 1), ("expSuspended", 2), ("expInProgress", 3), ("swapSuspended", 4), ("swapInProgress", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLayoutOperStatus.setStatus('current')
eqlRAIDDeviceLayoutSectPerSU = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLayoutSectPerSU.setStatus('current')
eqlRAIDDeviceLUNCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLUNCapacity.setStatus('current')
eqlRAIDDeviceLostBlocks = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceLostBlocks.setStatus('current')
eqlRAIDDeviceOutIOOps = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceOutIOOps.setStatus('current')
eqlRAIDDeviceCacheWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceCacheWrites.setStatus('current')
eqlRAIDDeviceCacheReads = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceCacheReads.setStatus('current')
eqlRAIDDeviceCompCacheWrites = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceCompCacheWrites.setStatus('current')
eqlRAIDDeviceCompCacheReads = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceCompCacheReads.setStatus('current')
eqlRAIDDeviceSectWritten = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceSectWritten.setStatus('current')
eqlRAIDDeviceSectRead = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceSectRead.setStatus('current')
eqlRAIDDeviceStoragePoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 17), Unsigned32())
if mibBuilder.loadTexts: eqlRAIDDeviceStoragePoolIndex.setStatus('current')
eqlRAIDDeviceDriveGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 1, 1, 18), Unsigned32())
if mibBuilder.loadTexts: eqlRAIDDeviceDriveGroupIndex.setStatus('current')
eqlRAIDLayoutTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2), )
if mibBuilder.loadTexts: eqlRAIDLayoutTable.setStatus('current')
eqlRAIDLayoutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"), (0, "EQLRAID-MIB", "eqlRAIDLayoutIndex"))
if mibBuilder.loadTexts: eqlRAIDLayoutEntry.setStatus('current')
eqlRAIDLayoutIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("first", 1), ("second", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutIndex.setStatus('current')
eqlRAIDLayoutOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noDevice", 1), ("noLayout", 2), ("failed", 3), ("nominal", 4), ("degraded", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutOperStatus.setStatus('current')
eqlRAIDLayoutNumParityGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutNumParityGrp.setStatus('current')
eqlRAIDLayoutParityType = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 10, 5, 50))).clone(namedValues=NamedValues(("stripe", 0), ("raid1", 1), ("raid10", 10), ("raid5", 5), ("raid50", 50)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutParityType.setStatus('current')
eqlRAIDLayoutBeginLBA = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutBeginLBA.setStatus('current')
eqlRAIDLayoutLength = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDLayoutLength.setStatus('current')
eqlRAIDParityGroupTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3), )
if mibBuilder.loadTexts: eqlRAIDParityGroupTable.setStatus('current')
eqlRAIDParityGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"), (0, "EQLRAID-MIB", "eqlRAIDLayoutIndex"), (0, "EQLRAID-MIB", "eqlParityGrpIndex"))
if mibBuilder.loadTexts: eqlRAIDParityGroupEntry.setStatus('current')
eqlParityGrpIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpIndex.setStatus('current')
eqlParityGrpOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noDevice", 1), ("noLayout", 2), ("noGroup", 3), ("degraded", 4), ("failed", 5), ("nominal", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpOperStatus.setStatus('current')
eqlParityGrpDriveCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpDriveCount.setStatus('current')
eqlParityGrpOperation = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("verify", 1), ("reconstruct", 2), ("noOp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpOperation.setStatus('current')
eqlParityGrpReconstChkpt = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpReconstChkpt.setStatus('current')
eqlParityGrpVerifyChkpt = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 3, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlParityGrpVerifyChkpt.setStatus('current')
eqlRAIDDriveTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4), )
if mibBuilder.loadTexts: eqlRAIDDriveTable.setStatus('current')
eqlRAIDDriveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1), ).setIndexNames((0, "EQLGROUP-MIB", "eqlGroupId"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLRAID-MIB", "eqlRAIDDriveDriveLUNIndex"))
if mibBuilder.loadTexts: eqlRAIDDriveEntry.setStatus('current')
eqlRAIDDriveDriveLUNIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDriveDriveLUNIndex.setStatus('current')
eqlRAIDDriveDriveLUN = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDriveDriveLUN.setStatus('current')
eqlRAIDDriveOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noDrive", 1), ("active", 2), ("failed", 3), ("tooSmall", 4), ("reconstruct", 5), ("swap", 6), ("spare", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDriveOperStatus.setStatus('current')
eqlRAIDDriveUUID = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDriveUUID.setStatus('current')
eqlRAIDDiskIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDiskIndex.setStatus('current')
eqlRAIDDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 4, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlRAIDDeviceIndex.setStatus('current')
eqlStoragePoolRAIDLUNTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 10, 1, 5), )
if mibBuilder.loadTexts: eqlStoragePoolRAIDLUNTable.setStatus('current')
eqlStoragePoolRAIDLUNEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 10, 1, 5, 1), ).setIndexNames((0, "EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex"), (0, "EQLMEMBER-MIB", "eqlMemberIndex"), (0, "EQLMEMBER-MIB", "eqlDriveGroupIndex"), (0, "EQLRAID-MIB", "eqlRAIDDeviceLUNIndex"))
if mibBuilder.loadTexts: eqlStoragePoolRAIDLUNEntry.setStatus('current')
eqlStoragePoolRAIDLUNfoo = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 10, 1, 5, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStoragePoolRAIDLUNfoo.setStatus('current')
mibBuilder.exportSymbols("EQLRAID-MIB", eqlRAIDDeviceLayoutSectPerSU=eqlRAIDDeviceLayoutSectPerSU, eqlParityGrpDriveCount=eqlParityGrpDriveCount, eqlRAIDDiskIndex=eqlRAIDDiskIndex, eqlRAIDDeviceOperStatus=eqlRAIDDeviceOperStatus, eqlStoragePoolRAIDLUNfoo=eqlStoragePoolRAIDLUNfoo, eqlRAIDDriveTable=eqlRAIDDriveTable, eqlRAIDDriveEntry=eqlRAIDDriveEntry, eqlRAIDDeviceTable=eqlRAIDDeviceTable, eqlRAIDLayoutIndex=eqlRAIDLayoutIndex, eqlRAIDDeviceCompCacheWrites=eqlRAIDDeviceCompCacheWrites, eqlStoragePoolRAIDLUNEntry=eqlStoragePoolRAIDLUNEntry, eqlRAIDNotifications=eqlRAIDNotifications, eqlRAIDDeviceLUNIndex=eqlRAIDDeviceLUNIndex, eqlRAIDDeviceLostBlocks=eqlRAIDDeviceLostBlocks, eqlRAIDDeviceCompCacheReads=eqlRAIDDeviceCompCacheReads, eqlRAIDConformance=eqlRAIDConformance, eqlRAIDLayoutOperStatus=eqlRAIDLayoutOperStatus, eqlRAIDLayoutBeginLBA=eqlRAIDLayoutBeginLBA, eqlParityGrpVerifyChkpt=eqlParityGrpVerifyChkpt, eqlRAIDLayoutParityType=eqlRAIDLayoutParityType, eqlRAIDDeviceLayoutOperStatus=eqlRAIDDeviceLayoutOperStatus, eqlRAIDDeviceUUID=eqlRAIDDeviceUUID, eqlRAIDObjects=eqlRAIDObjects, eqlRAIDLayoutLength=eqlRAIDLayoutLength, eqlParityGrpOperation=eqlParityGrpOperation, eqlRAIDDeviceIndex=eqlRAIDDeviceIndex, PYSNMP_MODULE_ID=eqlRAIDModule, eqlRAIDDeviceSectRead=eqlRAIDDeviceSectRead, eqlRAIDParityGroupEntry=eqlRAIDParityGroupEntry, eqlParityGrpIndex=eqlParityGrpIndex, eqlRAIDDriveOperStatus=eqlRAIDDriveOperStatus, eqlRAIDDeviceDriveGroupIndex=eqlRAIDDeviceDriveGroupIndex, eqlStoragePoolRAIDLUNTable=eqlStoragePoolRAIDLUNTable, eqlRAIDParityGroupTable=eqlRAIDParityGroupTable, eqlRAIDDriveDriveLUN=eqlRAIDDriveDriveLUN, eqlRAIDDriveUUID=eqlRAIDDriveUUID, eqlRAIDDeviceLUN=eqlRAIDDeviceLUN, eqlRAIDLayoutNumParityGrp=eqlRAIDLayoutNumParityGrp, eqlParityGrpReconstChkpt=eqlParityGrpReconstChkpt, eqlRAIDModule=eqlRAIDModule, eqlRAIDDeviceSectWritten=eqlRAIDDeviceSectWritten, eqlRAIDDeviceCacheWrites=eqlRAIDDeviceCacheWrites, eqlRAIDDeviceDriveCount=eqlRAIDDeviceDriveCount, eqlRAIDDeviceLUNCapacity=eqlRAIDDeviceLUNCapacity, eqlRAIDDeviceStoragePoolIndex=eqlRAIDDeviceStoragePoolIndex, eqlRAIDDeviceEntry=eqlRAIDDeviceEntry, eqlRAIDDeviceOutIOOps=eqlRAIDDeviceOutIOOps, eqlRAIDLayoutEntry=eqlRAIDLayoutEntry, eqlRAIDDeviceCacheReads=eqlRAIDDeviceCacheReads, eqlParityGrpOperStatus=eqlParityGrpOperStatus, eqlRAIDDriveDriveLUNIndex=eqlRAIDDriveDriveLUNIndex, eqlRAIDLayoutTable=eqlRAIDLayoutTable)
