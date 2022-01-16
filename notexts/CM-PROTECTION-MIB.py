#
# PySNMP MIB module CM-PROTECTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/CM-PROTECTION-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:21 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
slotIndex, shelfIndex, neIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "slotIndex", "shelfIndex", "neIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Counter64, TimeTicks, MibIdentifier, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, IpAddress, Integer32, Unsigned32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "TimeTicks", "MibIdentifier", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "IpAddress", "Integer32", "Unsigned32", "ModuleIdentity", "iso")
RowStatus, MacAddress, TruthValue, DisplayString, TextualConvention, StorageType, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "MacAddress", "TruthValue", "DisplayString", "TextualConvention", "StorageType", "VariablePointer")
cmProtectionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7))
cmProtectionMIB.setRevisions(('2010-06-23 00:00',))
if mibBuilder.loadTexts: cmProtectionMIB.setLastUpdated('201006230000Z')
if mibBuilder.loadTexts: cmProtectionMIB.setOrganization('ADVA Optical Networking')
cmProtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1))
cmProtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 2))
cmProtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3))
class CmProtSwitchMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("oneplusone", 1), ("dualactiverx", 2), ("universalring", 3))

class CmProtSwitchDirection(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("unidirectional", 1), ("bidirectional", 2))

class CmProtSwitchAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("none", 1), ("releaseprotswitch", 2), ("manualfromworking", 3), ("forcedfromworking", 4), ("manualfromprotect", 5), ("forcedfromprotect", 6), ("lockoutfromprotect", 7))

class CmProtUnitType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("working", 1), ("protect", 2))

class CmProtUnitState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("standby", 2))

class CmProtGroupStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("nooutstandingreq", 1), ("sf-protect", 2), ("sf-working", 3), ("sd-protect", 4), ("sd-working", 5), ("manual-protect", 6), ("manual-working", 7), ("forced-protect", 8), ("forced-working", 9), ("lockout-protect", 10), ("waitToRestore", 11))

cmFacProtGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1), )
if mibBuilder.loadTexts: cmFacProtGroupTable.setStatus('current')
cmFacProtGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-PROTECTION-MIB", "cmFacProtGroupIndex"))
if mibBuilder.loadTexts: cmFacProtGroupEntry.setStatus('current')
cmFacProtGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtGroupIndex.setStatus('current')
cmFacProtGroupUserLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupUserLabel.setStatus('current')
cmFacProtGroupSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 3), CmProtSwitchMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupSwitchMode.setStatus('current')
cmFacProtGroupRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupRevertive.setStatus('current')
cmFacProtGroupWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 60), ValueRangeConstraint(0, 0), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupWaitToRestore.setStatus('current')
cmFacProtGroupDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 6), CmProtSwitchDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupDirection.setStatus('current')
cmFacProtGroupWorkPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 7), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupWorkPort.setStatus('current')
cmFacProtGroupProtPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 8), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupProtPort.setStatus('current')
cmFacProtGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 9), CmProtGroupStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtGroupStatus.setStatus('current')
cmFacProtGroupAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 10), CmProtSwitchAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmFacProtGroupAction.setStatus('current')
cmFacProtGroupStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 11), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupStorageType.setStatus('current')
cmFacProtGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmFacProtGroupRowStatus.setStatus('current')
cmFacProtGroupMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 1, 1, 13), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtGroupMacAddress.setStatus('current')
cmFacProtUnitTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2), )
if mibBuilder.loadTexts: cmFacProtUnitTable.setStatus('current')
cmFacProtUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-PROTECTION-MIB", "cmFacProtGroupIndex"), (0, "CM-PROTECTION-MIB", "cmFacProtUnitIndex"))
if mibBuilder.loadTexts: cmFacProtUnitEntry.setStatus('current')
cmFacProtUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtUnitIndex.setStatus('current')
cmFacProtUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 2), CmProtUnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtUnitType.setStatus('current')
cmFacProtUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 3), CmProtUnitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtUnitState.setStatus('current')
cmFacProtUnitPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 2, 1, 4), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmFacProtUnitPort.setStatus('current')
cmMSPGroupTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3), )
if mibBuilder.loadTexts: cmMSPGroupTable.setStatus('current')
cmMSPGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-PROTECTION-MIB", "cmMSPGroupIndex"))
if mibBuilder.loadTexts: cmMSPGroupEntry.setStatus('current')
cmMSPGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPGroupIndex.setStatus('current')
cmMSPGroupUserLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupUserLabel.setStatus('current')
cmMSPGroupSwitchMode = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 3), CmProtSwitchMode()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupSwitchMode.setStatus('current')
cmMSPGroupRevertive = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupRevertive.setStatus('current')
cmMSPGroupWaitToRestore = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(1, 60), ValueRangeConstraint(0, 0), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupWaitToRestore.setStatus('current')
cmMSPGroupB2DEGTrigger = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupB2DEGTrigger.setStatus('current')
cmMSPGroupDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 7), CmProtSwitchDirection()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupDirection.setStatus('current')
cmMSPGroupWorkPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 8), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupWorkPort.setStatus('current')
cmMSPGroupProtPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 9), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupProtPort.setStatus('current')
cmMSPGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 10), CmProtGroupStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPGroupStatus.setStatus('current')
cmMSPGroupAction = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 11), CmProtSwitchAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cmMSPGroupAction.setStatus('current')
cmMSPGroupStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 12), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupStorageType.setStatus('current')
cmMSPGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmMSPGroupRowStatus.setStatus('current')
cmMSPGroupMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 3, 1, 14), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPGroupMacAddress.setStatus('current')
cmMSPUnitTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4), )
if mibBuilder.loadTexts: cmMSPUnitTable.setStatus('current')
cmMSPUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-PROTECTION-MIB", "cmMSPGroupIndex"), (0, "CM-PROTECTION-MIB", "cmMSPUnitIndex"))
if mibBuilder.loadTexts: cmMSPUnitEntry.setStatus('current')
cmMSPUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPUnitIndex.setStatus('current')
cmMSPUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 2), CmProtUnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPUnitType.setStatus('current')
cmMSPUnitState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 3), CmProtUnitState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPUnitState.setStatus('current')
cmMSPUnitPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 1, 4, 1, 4), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmMSPUnitPort.setStatus('current')
cmProtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 1))
cmProtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 2))
cmProtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 1, 1)).setObjects(("CM-PROTECTION-MIB", "cmProtObjectGroup"), ("CM-PROTECTION-MIB", "cmMSProtObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmProtCompliance = cmProtCompliance.setStatus('current')
cmProtObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 2, 1)).setObjects(("CM-PROTECTION-MIB", "cmFacProtGroupIndex"), ("CM-PROTECTION-MIB", "cmFacProtGroupUserLabel"), ("CM-PROTECTION-MIB", "cmFacProtGroupSwitchMode"), ("CM-PROTECTION-MIB", "cmFacProtGroupRevertive"), ("CM-PROTECTION-MIB", "cmFacProtGroupWaitToRestore"), ("CM-PROTECTION-MIB", "cmFacProtGroupDirection"), ("CM-PROTECTION-MIB", "cmFacProtGroupWorkPort"), ("CM-PROTECTION-MIB", "cmFacProtGroupProtPort"), ("CM-PROTECTION-MIB", "cmFacProtGroupStatus"), ("CM-PROTECTION-MIB", "cmFacProtGroupAction"), ("CM-PROTECTION-MIB", "cmFacProtGroupStorageType"), ("CM-PROTECTION-MIB", "cmFacProtGroupRowStatus"), ("CM-PROTECTION-MIB", "cmFacProtGroupMacAddress"), ("CM-PROTECTION-MIB", "cmFacProtUnitIndex"), ("CM-PROTECTION-MIB", "cmFacProtUnitType"), ("CM-PROTECTION-MIB", "cmFacProtUnitState"), ("CM-PROTECTION-MIB", "cmFacProtUnitPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmProtObjectGroup = cmProtObjectGroup.setStatus('current')
cmMSProtObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 7, 3, 2, 2)).setObjects(("CM-PROTECTION-MIB", "cmMSPGroupIndex"), ("CM-PROTECTION-MIB", "cmMSPGroupUserLabel"), ("CM-PROTECTION-MIB", "cmMSPGroupSwitchMode"), ("CM-PROTECTION-MIB", "cmMSPGroupRevertive"), ("CM-PROTECTION-MIB", "cmMSPGroupWaitToRestore"), ("CM-PROTECTION-MIB", "cmMSPGroupB2DEGTrigger"), ("CM-PROTECTION-MIB", "cmMSPGroupDirection"), ("CM-PROTECTION-MIB", "cmMSPGroupWorkPort"), ("CM-PROTECTION-MIB", "cmMSPGroupProtPort"), ("CM-PROTECTION-MIB", "cmMSPGroupStatus"), ("CM-PROTECTION-MIB", "cmMSPGroupAction"), ("CM-PROTECTION-MIB", "cmMSPGroupStorageType"), ("CM-PROTECTION-MIB", "cmMSPGroupRowStatus"), ("CM-PROTECTION-MIB", "cmMSPGroupMacAddress"), ("CM-PROTECTION-MIB", "cmMSPUnitIndex"), ("CM-PROTECTION-MIB", "cmMSPUnitType"), ("CM-PROTECTION-MIB", "cmMSPUnitState"), ("CM-PROTECTION-MIB", "cmMSPUnitPort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cmMSProtObjectGroup = cmMSProtObjectGroup.setStatus('current')
mibBuilder.exportSymbols("CM-PROTECTION-MIB", cmFacProtUnitTable=cmFacProtUnitTable, cmMSPGroupIndex=cmMSPGroupIndex, cmFacProtGroupStorageType=cmFacProtGroupStorageType, cmProtObjects=cmProtObjects, cmMSPGroupRevertive=cmMSPGroupRevertive, cmMSPGroupProtPort=cmMSPGroupProtPort, cmFacProtGroupUserLabel=cmFacProtGroupUserLabel, cmMSPUnitTable=cmMSPUnitTable, cmFacProtGroupRowStatus=cmFacProtGroupRowStatus, cmMSPGroupSwitchMode=cmMSPGroupSwitchMode, cmMSPGroupStorageType=cmMSPGroupStorageType, CmProtUnitType=CmProtUnitType, cmProtNotifications=cmProtNotifications, cmMSPGroupB2DEGTrigger=cmMSPGroupB2DEGTrigger, cmProtConformance=cmProtConformance, cmMSPGroupWorkPort=cmMSPGroupWorkPort, cmProtGroups=cmProtGroups, cmFacProtGroupStatus=cmFacProtGroupStatus, cmMSPGroupStatus=cmMSPGroupStatus, cmMSPGroupUserLabel=cmMSPGroupUserLabel, cmFacProtGroupMacAddress=cmFacProtGroupMacAddress, cmMSPGroupEntry=cmMSPGroupEntry, CmProtGroupStatus=CmProtGroupStatus, cmFacProtGroupProtPort=cmFacProtGroupProtPort, cmProtCompliances=cmProtCompliances, cmProtCompliance=cmProtCompliance, cmFacProtUnitPort=cmFacProtUnitPort, cmMSPGroupDirection=cmMSPGroupDirection, cmFacProtGroupEntry=cmFacProtGroupEntry, cmFacProtGroupRevertive=cmFacProtGroupRevertive, cmMSPGroupTable=cmMSPGroupTable, cmMSPUnitType=cmMSPUnitType, CmProtSwitchDirection=CmProtSwitchDirection, cmFacProtGroupIndex=cmFacProtGroupIndex, cmMSPGroupMacAddress=cmMSPGroupMacAddress, cmMSProtObjectGroup=cmMSProtObjectGroup, cmFacProtUnitEntry=cmFacProtUnitEntry, cmFacProtGroupTable=cmFacProtGroupTable, cmFacProtGroupAction=cmFacProtGroupAction, cmMSPGroupWaitToRestore=cmMSPGroupWaitToRestore, cmFacProtUnitIndex=cmFacProtUnitIndex, cmFacProtGroupDirection=cmFacProtGroupDirection, CmProtSwitchAction=CmProtSwitchAction, cmFacProtUnitState=cmFacProtUnitState, CmProtSwitchMode=CmProtSwitchMode, cmFacProtGroupWaitToRestore=cmFacProtGroupWaitToRestore, cmMSPUnitState=cmMSPUnitState, cmMSPGroupRowStatus=cmMSPGroupRowStatus, cmFacProtUnitType=cmFacProtUnitType, cmMSPGroupAction=cmMSPGroupAction, CmProtUnitState=CmProtUnitState, cmMSPUnitPort=cmMSPUnitPort, cmMSPUnitIndex=cmMSPUnitIndex, cmFacProtGroupWorkPort=cmFacProtGroupWorkPort, PYSNMP_MODULE_ID=cmProtectionMIB, cmFacProtGroupSwitchMode=cmFacProtGroupSwitchMode, cmProtObjectGroup=cmProtObjectGroup, cmMSPUnitEntry=cmMSPUnitEntry, cmProtectionMIB=cmProtectionMIB)
