#
# PySNMP MIB module EQLSTORAGECONTAINER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/equallogic/EQLSTORAGECONTAINER-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:18:03 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
UTFString, = mibBuilder.importSymbols("EQLGROUP-MIB", "UTFString")
eqlStoragePoolIndex, = mibBuilder.importSymbols("EQLSTORAGEPOOL-MIB", "eqlStoragePoolIndex")
EQL2PartRowPointerStr, eqliscsiLocalMemberId = mibBuilder.importSymbols("EQLVOLUME-MIB", "EQL2PartRowPointerStr", "eqliscsiLocalMemberId")
equalLogic, = mibBuilder.importSymbols("EQUALLOGIC-SMI", "equalLogic")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, iso, NotificationType, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, Unsigned32, enterprises, Counter64, ModuleIdentity, Integer32, ObjectIdentity, Bits, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "NotificationType", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "Unsigned32", "enterprises", "Counter64", "ModuleIdentity", "Integer32", "ObjectIdentity", "Bits", "TimeTicks")
RowPointer, DisplayString, RowStatus, TruthValue, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DisplayString", "RowStatus", "TruthValue", "DateAndTime", "TextualConvention")
eqlStorageContainerModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 12740, 25))
eqlStorageContainerModule.setRevisions(('2012-06-20 00:00',))
if mibBuilder.loadTexts: eqlStorageContainerModule.setLastUpdated('201503171528Z')
if mibBuilder.loadTexts: eqlStorageContainerModule.setOrganization('EqualLogic Inc.')
eqlStorageContainerObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 25, 1))
eqlStorageContainerNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 25, 2))
eqlStorageContainerConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 12740, 25, 3))
class Unsigned64(TextualConvention, Counter64):
    status = 'current'

eqlStorageContainerTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 25, 1, 1), )
if mibBuilder.loadTexts: eqlStorageContainerTable.setStatus('current')
eqlStorageContainerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1), ).setIndexNames((0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"), (0, "EQLSTORAGECONTAINER-MIB", "eqlStorageContainerIndex"))
if mibBuilder.loadTexts: eqlStorageContainerEntry.setStatus('current')
eqlStorageContainerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlStorageContainerIndex.setStatus('current')
eqlStorageContainerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageContainerRowStatus.setStatus('current')
eqlStorageContainerUuid = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerUuid.setStatus('current')
eqlStorageContainerName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 4), UTFString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageContainerName.setStatus('current')
eqlStorageContainerLookupName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 5), UTFString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerLookupName.setStatus('current')
eqlStorageContainerDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 6), UTFString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageContainerDescription.setStatus('current')
eqlStorageContainerLogicalLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 1, 1, 7), Unsigned64().clone(8589934592)).setUnits('MB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageContainerLogicalLimit.setStatus('current')
eqlStorageContainerStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2), )
if mibBuilder.loadTexts: eqlStorageContainerStatisticsTable.setStatus('current')
eqlStorageContainerStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1), )
eqlStorageContainerEntry.registerAugmentions(("EQLSTORAGECONTAINER-MIB", "eqlStorageContainerStatisticsEntry"))
eqlStorageContainerStatisticsEntry.setIndexNames(*eqlStorageContainerEntry.getIndexNames())
if mibBuilder.loadTexts: eqlStorageContainerStatisticsEntry.setStatus('current')
eqlStorageContainerStatisticsLogicalUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 1), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerStatisticsLogicalUsed.setStatus('current')
eqlStorageContainerStatisticsLogicalFree = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 2), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerStatisticsLogicalFree.setStatus('current')
eqlStorageContainerStatisticsPhysicalUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 3), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerStatisticsPhysicalUsed.setStatus('current')
eqlStorageContainerStatisticsPhysicalFree = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 4), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerStatisticsPhysicalFree.setStatus('current')
eqlStorageContainerStatisticsThinProvFree = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 5), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerStatisticsThinProvFree.setStatus('current')
eqlStorageContainerStatisticsVvolsBound = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerStatisticsVvolsBound.setStatus('current')
eqlStorageContainerStatisticsSVCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerStatisticsSVCount.setStatus('current')
eqlStorageContainerStatisticsSVSCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerStatisticsSVSCount.setStatus('current')
eqlStorageContainerStatisticsThinProvisioned = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerStatisticsThinProvisioned.setStatus('current')
eqlStorageContainerStatisticsVvolsOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageContainerStatisticsVvolsOnline.setStatus('current')
eqlStorageBucketTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3), )
if mibBuilder.loadTexts: eqlStorageBucketTable.setStatus('current')
eqlStorageBucketEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1), ).setIndexNames((0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"), (0, "EQLSTORAGECONTAINER-MIB", "eqlStorageBucketIndex"))
if mibBuilder.loadTexts: eqlStorageBucketEntry.setStatus('current')
eqlStorageBucketIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: eqlStorageBucketIndex.setStatus('current')
eqlStorageBucketRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageBucketRowStatus.setStatus('current')
eqlStorageBucketName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 3), UTFString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageBucketName.setStatus('current')
eqlStorageBucketLookupName = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 4), UTFString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketLookupName.setStatus('current')
eqlStorageBucketUuid = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketUuid.setStatus('current')
eqlStorageBucketPhysicalSize = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 6), Unsigned64()).setUnits('MB').setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageBucketPhysicalSize.setStatus('current')
eqlStorageBucketThinProvision = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 7), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageBucketThinProvision.setStatus('current')
eqlStorageBucketThinMinReserve = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageBucketThinMinReserve.setStatus('current')
eqlStorageBucketThinMaxGrow = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(100)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageBucketThinMaxGrow.setStatus('current')
eqlStorageBucketFreeWarnPercentage = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlStorageBucketFreeWarnPercentage.setStatus('current')
eqlParentStorageContainerPointer = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 11), EQL2PartRowPointerStr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlParentStorageContainerPointer.setStatus('current')
eqlParentStoragePoolIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 3, 1, 12), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: eqlParentStoragePoolIndex.setStatus('current')
eqlStorageBucketDynamicConfigTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 25, 1, 4), )
if mibBuilder.loadTexts: eqlStorageBucketDynamicConfigTable.setStatus('current')
eqlStorageBucketDynamicConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 25, 1, 4, 1), ).setIndexNames((0, "EQLVOLUME-MIB", "eqliscsiLocalMemberId"), (0, "EQLSTORAGECONTAINER-MIB", "eqlStorageBucketIndex"))
if mibBuilder.loadTexts: eqlStorageBucketDynamicConfigEntry.setStatus('current')
eqlStorageBucketDynamicReservePages = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 4, 1, 1), Counter64()).setUnits('pages').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketDynamicReservePages.setStatus('current')
eqlStorageBucketFreeWarnInUsePageCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 4, 1, 2), Counter64()).setUnits('pages').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketFreeWarnInUsePageCount.setStatus('current')
eqlStorageBucketMaxResvInUsePageCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 4, 1, 3), Counter64()).setUnits('pages').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketMaxResvInUsePageCount.setStatus('current')
eqlStorageBucketFreeWarnThresholdPageCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 4, 1, 4), Counter64()).setUnits('pages').setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketFreeWarnThresholdPageCount.setStatus('current')
eqlStorageBucketStatisticsTable = MibTable((1, 3, 6, 1, 4, 1, 12740, 25, 1, 5), )
if mibBuilder.loadTexts: eqlStorageBucketStatisticsTable.setStatus('current')
eqlStorageBucketStatisticsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1), )
eqlStorageBucketEntry.registerAugmentions(("EQLSTORAGECONTAINER-MIB", "eqlStorageBucketStatisticsEntry"))
eqlStorageBucketStatisticsEntry.setIndexNames(*eqlStorageBucketEntry.getIndexNames())
if mibBuilder.loadTexts: eqlStorageBucketStatisticsEntry.setStatus('current')
eqlStorageBucketStatisticsPhysicalUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 1), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketStatisticsPhysicalUsed.setStatus('current')
eqlStorageBucketStatisticsPhysicalFree = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 2), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketStatisticsPhysicalFree.setStatus('current')
eqlStorageBucketStatisticsThinProvFree = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 3), Unsigned64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketStatisticsThinProvFree.setStatus('current')
eqlStorageBucketStatisticsVvolsBound = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketStatisticsVvolsBound.setStatus('current')
eqlStorageBucketStatisticsSVCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketStatisticsSVCount.setStatus('current')
eqlStorageBucketStatisticsSVSCount = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketStatisticsSVSCount.setStatus('current')
eqlStorageBucketStatisticsVvolsOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 12740, 25, 1, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eqlStorageBucketStatisticsVvolsOnline.setStatus('current')
mibBuilder.exportSymbols("EQLSTORAGECONTAINER-MIB", eqlStorageBucketTable=eqlStorageBucketTable, eqlStorageContainerObjects=eqlStorageContainerObjects, eqlStorageBucketEntry=eqlStorageBucketEntry, eqlStorageContainerModule=eqlStorageContainerModule, eqlStorageContainerStatisticsSVCount=eqlStorageContainerStatisticsSVCount, eqlStorageContainerStatisticsPhysicalUsed=eqlStorageContainerStatisticsPhysicalUsed, eqlStorageBucketDynamicConfigEntry=eqlStorageBucketDynamicConfigEntry, eqlStorageBucketMaxResvInUsePageCount=eqlStorageBucketMaxResvInUsePageCount, eqlStorageContainerConformance=eqlStorageContainerConformance, eqlStorageBucketStatisticsTable=eqlStorageBucketStatisticsTable, eqlStorageBucketRowStatus=eqlStorageBucketRowStatus, eqlStorageContainerStatisticsVvolsBound=eqlStorageContainerStatisticsVvolsBound, eqlStorageBucketFreeWarnInUsePageCount=eqlStorageBucketFreeWarnInUsePageCount, eqlStorageContainerStatisticsThinProvFree=eqlStorageContainerStatisticsThinProvFree, eqlStorageBucketDynamicConfigTable=eqlStorageBucketDynamicConfigTable, eqlStorageContainerDescription=eqlStorageContainerDescription, eqlStorageContainerEntry=eqlStorageContainerEntry, eqlStorageBucketUuid=eqlStorageBucketUuid, eqlParentStoragePoolIndex=eqlParentStoragePoolIndex, eqlStorageBucketStatisticsVvolsBound=eqlStorageBucketStatisticsVvolsBound, eqlStorageBucketThinMinReserve=eqlStorageBucketThinMinReserve, eqlStorageBucketStatisticsSVSCount=eqlStorageBucketStatisticsSVSCount, eqlStorageBucketStatisticsThinProvFree=eqlStorageBucketStatisticsThinProvFree, eqlParentStorageContainerPointer=eqlParentStorageContainerPointer, eqlStorageBucketStatisticsPhysicalUsed=eqlStorageBucketStatisticsPhysicalUsed, eqlStorageBucketStatisticsPhysicalFree=eqlStorageBucketStatisticsPhysicalFree, eqlStorageBucketName=eqlStorageBucketName, eqlStorageContainerStatisticsVvolsOnline=eqlStorageContainerStatisticsVvolsOnline, eqlStorageBucketStatisticsVvolsOnline=eqlStorageBucketStatisticsVvolsOnline, eqlStorageContainerStatisticsTable=eqlStorageContainerStatisticsTable, eqlStorageContainerStatisticsLogicalFree=eqlStorageContainerStatisticsLogicalFree, PYSNMP_MODULE_ID=eqlStorageContainerModule, eqlStorageContainerRowStatus=eqlStorageContainerRowStatus, eqlStorageContainerStatisticsEntry=eqlStorageContainerStatisticsEntry, eqlStorageBucketStatisticsSVCount=eqlStorageBucketStatisticsSVCount, eqlStorageContainerStatisticsThinProvisioned=eqlStorageContainerStatisticsThinProvisioned, eqlStorageContainerUuid=eqlStorageContainerUuid, eqlStorageBucketThinProvision=eqlStorageBucketThinProvision, eqlStorageContainerStatisticsSVSCount=eqlStorageContainerStatisticsSVSCount, eqlStorageBucketStatisticsEntry=eqlStorageBucketStatisticsEntry, Unsigned64=Unsigned64, eqlStorageBucketThinMaxGrow=eqlStorageBucketThinMaxGrow, eqlStorageContainerNotifications=eqlStorageContainerNotifications, eqlStorageBucketLookupName=eqlStorageBucketLookupName, eqlStorageContainerIndex=eqlStorageContainerIndex, eqlStorageContainerLookupName=eqlStorageContainerLookupName, eqlStorageContainerLogicalLimit=eqlStorageContainerLogicalLimit, eqlStorageContainerName=eqlStorageContainerName, eqlStorageContainerStatisticsLogicalUsed=eqlStorageContainerStatisticsLogicalUsed, eqlStorageContainerTable=eqlStorageContainerTable, eqlStorageBucketDynamicReservePages=eqlStorageBucketDynamicReservePages, eqlStorageBucketIndex=eqlStorageBucketIndex, eqlStorageBucketFreeWarnPercentage=eqlStorageBucketFreeWarnPercentage, eqlStorageBucketFreeWarnThresholdPageCount=eqlStorageBucketFreeWarnThresholdPageCount, eqlStorageContainerStatisticsPhysicalFree=eqlStorageContainerStatisticsPhysicalFree, eqlStorageBucketPhysicalSize=eqlStorageBucketPhysicalSize)
