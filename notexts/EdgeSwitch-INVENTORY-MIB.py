#
# PySNMP MIB module EdgeSwitch-INVENTORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/edgeswitch/EdgeSwitch-INVENTORY-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:11:32 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
fastPath, = mibBuilder.importSymbols("EdgeSwitch-REF-MIB", "fastPath")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Integer32, TimeTicks, Unsigned32, ModuleIdentity, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Bits, Counter64, Counter32, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "Unsigned32", "ModuleIdentity", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Bits", "Counter64", "Counter32", "NotificationType", "IpAddress")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
fastPathInventory = ModuleIdentity((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13))
fastPathInventory.setRevisions(('2013-10-15 00:00', '2011-01-26 00:00', '2007-05-23 00:00', '2004-10-28 20:37', '2003-05-26 19:30',))
if mibBuilder.loadTexts: fastPathInventory.setLastUpdated('201310150000Z')
if mibBuilder.loadTexts: fastPathInventory.setOrganization('Broadcom Inc')
class AgentInventoryUnitPreference(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("unsassigned", 1), ("assigned", 2))

class AgentInventoryUnitType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'

class AgentInventoryCardType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'x'

agentInventoryStackGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1))
agentInventoryStackReplicateSTK = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackReplicateSTK.setStatus('current')
agentInventoryStackReload = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackReload.setStatus('current')
agentInventoryStackMaxUnitNumber = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackMaxUnitNumber.setStatus('current')
agentInventoryStackReplicateSTKStatus = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inProgress", 1), ("notInProgress", 2), ("finishedWithSuccess", 3), ("finishedWithError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackReplicateSTKStatus.setStatus('current')
agentInventoryStackSTKname = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unconfigured", 1), ("image1", 2), ("image2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackSTKname.setStatus('current')
agentInventoryStackActivateSTK = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackActivateSTK.setStatus('current')
agentInventoryStackDeleteSTK = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackDeleteSTK.setStatus('current')
agentInventoryStackTemplateId = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 1, 8), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackTemplateId.setStatus('current')
agentInventoryUnitGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2))
agentInventorySupportedUnitTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1), )
if mibBuilder.loadTexts: agentInventorySupportedUnitTable.setStatus('current')
agentInventorySupportedUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1, 1), ).setIndexNames((0, "EdgeSwitch-INVENTORY-MIB", "agentInventorySupportedUnitIndex"))
if mibBuilder.loadTexts: agentInventorySupportedUnitEntry.setStatus('current')
agentInventorySupportedUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: agentInventorySupportedUnitIndex.setStatus('current')
agentInventorySupportedUnitModelIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySupportedUnitModelIdentifier.setStatus('current')
agentInventorySupportedUnitDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySupportedUnitDescription.setStatus('current')
agentInventorySupportedUnitExpectedCodeVer = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySupportedUnitExpectedCodeVer.setStatus('obsolete')
agentInventoryUnitTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2), )
if mibBuilder.loadTexts: agentInventoryUnitTable.setStatus('current')
agentInventoryUnitEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1), ).setIndexNames((0, "EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitNumber"))
if mibBuilder.loadTexts: agentInventoryUnitEntry.setStatus('current')
agentInventoryUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryUnitNumber.setStatus('current')
agentInventoryUnitAssignNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 2), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitAssignNumber.setStatus('current')
agentInventoryUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 3), AgentInventoryUnitType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitType.setStatus('current')
agentInventoryUnitSupportedUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 4), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitSupportedUnitIndex.setStatus('current')
agentInventoryUnitMgmtAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("mgmtUnit", 1), ("stackUnit", 2), ("mgmtUnassigned", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitMgmtAdmin.setStatus('current')
agentInventoryUnitHWMgmtPref = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 7), AgentInventoryUnitPreference()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitHWMgmtPref.setStatus('obsolete')
agentInventoryUnitHWMgmtPrefValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 8), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 15), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitHWMgmtPrefValue.setStatus('obsolete')
agentInventoryUnitAdminMgmtPref = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 9), AgentInventoryUnitPreference()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitAdminMgmtPref.setStatus('obsolete')
agentInventoryUnitAdminMgmtPrefValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 10), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 15), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitAdminMgmtPrefValue.setStatus('obsolete')
agentInventoryUnitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("ok", 1), ("unsupported", 2), ("codeMismatch", 3), ("configMismatch", 4), ("sdmMismatch", 5), ("notPresent", 6), ("codeUpdate", 7), ("stmMismatch", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitStatus.setStatus('current')
agentInventoryUnitDetectedCodeVer = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitDetectedCodeVer.setStatus('current')
agentInventoryUnitDetectedCodeInFlashVer = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitDetectedCodeInFlashVer.setStatus('current')
agentInventoryUnitUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 14), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitUpTime.setStatus('current')
agentInventoryUnitDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitDescription.setStatus('current')
agentInventoryUnitReplicateSTK = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitReplicateSTK.setStatus('current')
agentInventoryUnitReload = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitReload.setStatus('current')
agentInventoryUnitRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: agentInventoryUnitRowStatus.setStatus('current')
agentInventoryUnitSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitSerialNumber.setStatus('current')
agentInventoryUnitImage1Version = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitImage1Version.setStatus('current')
agentInventoryUnitImage2Version = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitImage2Version.setStatus('current')
agentInventoryUnitSTKname = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("image1", 2), ("image2", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitSTKname.setStatus('current')
agentInventoryUnitActivateSTK = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitActivateSTK.setStatus('current')
agentInventoryUnitDeleteSTK = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitDeleteSTK.setStatus('current')
agentInventoryUnitReplicateSTKStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("inProgress", 1), ("notInProgress", 2), ("finishedWithSuccess", 3), ("finishedWithError", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitReplicateSTKStatus.setStatus('current')
agentInventoryUnitStandby = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unassigned", 1), ("standby-opr", 2), ("standby-cfg", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryUnitStandby.setStatus('current')
agentInventoryUnitSFSTransferStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("inProgress", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitSFSTransferStatus.setStatus('current')
agentInventoryUnitSFSLastAttemptStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 2, 2, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("success", 2), ("failure", 3), ("min-bootcode-version-not-present", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryUnitSFSLastAttemptStatus.setStatus('current')
agentInventorySlotGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3))
agentInventorySlotTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1), )
if mibBuilder.loadTexts: agentInventorySlotTable.setStatus('current')
agentInventorySlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1), ).setIndexNames((0, "EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitNumber"), (0, "EdgeSwitch-INVENTORY-MIB", "agentInventorySlotNumber"))
if mibBuilder.loadTexts: agentInventorySlotEntry.setStatus('current')
agentInventorySlotNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventorySlotNumber.setStatus('current')
agentInventorySlotStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("empty", 1), ("full", 2), ("error", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySlotStatus.setStatus('current')
agentInventorySlotPowerMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventorySlotPowerMode.setStatus('current')
agentInventorySlotAdminMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventorySlotAdminMode.setStatus('current')
agentInventorySlotInsertedCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 6), AgentInventoryCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySlotInsertedCardType.setStatus('current')
agentInventorySlotConfiguredCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 7), AgentInventoryCardType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventorySlotConfiguredCardType.setStatus('current')
agentInventorySlotCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 3, 1, 1, 8), Bits().clone(namedValues=NamedValues(("pluggable", 0), ("power-down", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventorySlotCapabilities.setStatus('current')
agentInventoryCardGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4))
agentInventoryCardTypeTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1), )
if mibBuilder.loadTexts: agentInventoryCardTypeTable.setStatus('current')
agentInventoryCardTypeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1), ).setIndexNames((0, "EdgeSwitch-INVENTORY-MIB", "agentInventoryCardIndex"))
if mibBuilder.loadTexts: agentInventoryCardTypeEntry.setStatus('current')
agentInventoryCardIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryCardIndex.setStatus('current')
agentInventoryCardType = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 2), AgentInventoryCardType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardType.setStatus('current')
agentInventoryCardModelIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardModelIdentifier.setStatus('current')
agentInventoryCardDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 4, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryCardDescription.setStatus('current')
agentInventoryComponentGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5))
agentInventoryComponentTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1), )
if mibBuilder.loadTexts: agentInventoryComponentTable.setStatus('current')
agentInventoryComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1), ).setIndexNames((0, "EdgeSwitch-INVENTORY-MIB", "agentInventoryComponentIndex"))
if mibBuilder.loadTexts: agentInventoryComponentEntry.setStatus('current')
agentInventoryComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryComponentIndex.setStatus('current')
agentInventoryComponentMnemonic = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryComponentMnemonic.setStatus('current')
agentInventoryComponentName = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 5, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryComponentName.setStatus('current')
agentInventoryStackPortGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7))
agentInventoryStackPortIpTelephonyQOSSupport = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackPortIpTelephonyQOSSupport.setStatus('current')
agentInventorySFSGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 8))
agentInventoryStackUnitNumber = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 8, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryStackUnitNumber.setStatus('current')
agentInventorySFS = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventorySFS.setStatus('current')
agentInventorySFSAllowDowngrade = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 8, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventorySFSAllowDowngrade.setStatus('current')
agentInventorySFSTrap = MibScalar((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 8, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventorySFSTrap.setStatus('current')
agentInventoryStackPortTable = MibTable((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2), )
if mibBuilder.loadTexts: agentInventoryStackPortTable.setStatus('current')
agentInventoryStackPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1), ).setIndexNames((0, "EdgeSwitch-INVENTORY-MIB", "agentInventoryStackPortIndex"))
if mibBuilder.loadTexts: agentInventoryStackPortEntry.setStatus('current')
agentInventoryStackPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: agentInventoryStackPortIndex.setStatus('current')
agentInventoryStackPortUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortUnit.setStatus('current')
agentInventoryStackPortTag = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortTag.setStatus('current')
agentInventoryStackPortConfiguredStackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stack", 1), ("ethernet", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: agentInventoryStackPortConfiguredStackMode.setStatus('current')
agentInventoryStackPortRunningStackMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stack", 1), ("ethernet", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortRunningStackMode.setStatus('current')
agentInventoryStackPortLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortLinkStatus.setStatus('current')
agentInventoryStackPortLinkSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortLinkSpeed.setStatus('current')
agentInventoryStackPortDataRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortDataRate.setStatus('current')
agentInventoryStackPortErrorRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortErrorRate.setStatus('current')
agentInventoryStackPortTotalErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 7, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: agentInventoryStackPortTotalErrors.setStatus('current')
agentInventoryTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0))
agentInventoryCardMismatch = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 1)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitNumber"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotNumber"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotInsertedCardType"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotConfiguredCardType"))
if mibBuilder.loadTexts: agentInventoryCardMismatch.setStatus('current')
agentInventoryCardUnsupported = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 2)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitNumber"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotNumber"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotInsertedCardType"))
if mibBuilder.loadTexts: agentInventoryCardUnsupported.setStatus('current')
agentInventoryStackPortLinkUp = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 3)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackPortUnit"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackPortTag"))
if mibBuilder.loadTexts: agentInventoryStackPortLinkUp.setStatus('current')
agentInventoryStackPortLinkDown = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 4)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackPortUnit"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackPortTag"))
if mibBuilder.loadTexts: agentInventoryStackPortLinkDown.setStatus('current')
agentInventorySFSStart = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 5)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackUnitNumber"))
if mibBuilder.loadTexts: agentInventorySFSStart.setStatus('current')
agentInventorySFSComplete = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 6)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackUnitNumber"))
if mibBuilder.loadTexts: agentInventorySFSComplete.setStatus('current')
agentInventorySFSFail = NotificationType((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 0, 7)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventoryStackUnitNumber"))
if mibBuilder.loadTexts: agentInventorySFSFail.setStatus('current')
fastPathInventoryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6))
fastPathInventoryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 1))
fastPathInventoryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2))
fastPathInventoryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 1, 1)).setObjects(("EdgeSwitch-INVENTORY-MIB", "fastPathInventorySlotGroup"), ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryCardGroup"), ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryCardGroup"), ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryUnitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventoryCompliance = fastPathInventoryCompliance.setStatus('obsolete')
fastPathInventoryCompliance2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 1, 2)).setObjects(("EdgeSwitch-INVENTORY-MIB", "fastPathInventorySlotGroup"), ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryCardGroup"), ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryCardGroup"), ("EdgeSwitch-INVENTORY-MIB", "fastPathInventoryUnitGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventoryCompliance2 = fastPathInventoryCompliance2.setStatus('current')
fastPathInventorySupportedUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2, 1)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventorySupportedUnitIndex"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySupportedUnitModelIdentifier"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySupportedUnitDescription"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySupportedUnitExpectedCodeVer"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventorySupportedUnitGroup = fastPathInventorySupportedUnitGroup.setStatus('current')
fastPathInventoryUnitGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2, 2)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitNumber"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitAssignNumber"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitType"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitMgmtAdmin"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitHWMgmtPref"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitAdminMgmtPref"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitStatus"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitDetectedCodeVer"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitDetectedCodeInFlashVer"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitUpTime"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitDescription"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitReplicateSTK"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitRowStatus"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitImage1Version"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitImage2Version"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitSTKname"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitActivateSTK"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitDeleteSTK"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryUnitSTKname"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventoryUnitGroup = fastPathInventoryUnitGroup.setStatus('current')
fastPathInventorySlotGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2, 3)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotNumber"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotStatus"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotPowerMode"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotAdminMode"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotInsertedCardType"), ("EdgeSwitch-INVENTORY-MIB", "agentInventorySlotConfiguredCardType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventorySlotGroup = fastPathInventorySlotGroup.setStatus('current')
fastPathInventoryCardGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2, 4)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardIndex"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardType"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardModelIdentifier"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventoryCardGroup = fastPathInventoryCardGroup.setStatus('current')
fastPathInventoryNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4413, 1, 1, 13, 6, 2, 5)).setObjects(("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardMismatch"), ("EdgeSwitch-INVENTORY-MIB", "agentInventoryCardUnsupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    fastPathInventoryNotificationsGroup = fastPathInventoryNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("EdgeSwitch-INVENTORY-MIB", fastPathInventoryCardGroup=fastPathInventoryCardGroup, agentInventoryStackPortTable=agentInventoryStackPortTable, fastPathInventory=fastPathInventory, agentInventoryUnitImage1Version=agentInventoryUnitImage1Version, agentInventoryStackPortRunningStackMode=agentInventoryStackPortRunningStackMode, agentInventoryUnitHWMgmtPrefValue=agentInventoryUnitHWMgmtPrefValue, agentInventoryStackGroup=agentInventoryStackGroup, agentInventoryStackActivateSTK=agentInventoryStackActivateSTK, agentInventoryComponentMnemonic=agentInventoryComponentMnemonic, agentInventoryUnitActivateSTK=agentInventoryUnitActivateSTK, agentInventoryUnitReplicateSTKStatus=agentInventoryUnitReplicateSTKStatus, fastPathInventoryCompliance=fastPathInventoryCompliance, agentInventoryComponentGroup=agentInventoryComponentGroup, agentInventorySlotAdminMode=agentInventorySlotAdminMode, agentInventoryUnitNumber=agentInventoryUnitNumber, fastPathInventoryCompliance2=fastPathInventoryCompliance2, fastPathInventorySupportedUnitGroup=fastPathInventorySupportedUnitGroup, agentInventoryTraps=agentInventoryTraps, agentInventoryStackReplicateSTKStatus=agentInventoryStackReplicateSTKStatus, agentInventorySupportedUnitIndex=agentInventorySupportedUnitIndex, agentInventoryUnitUpTime=agentInventoryUnitUpTime, agentInventorySlotStatus=agentInventorySlotStatus, agentInventoryStackPortIpTelephonyQOSSupport=agentInventoryStackPortIpTelephonyQOSSupport, agentInventoryUnitDeleteSTK=agentInventoryUnitDeleteSTK, agentInventorySFS=agentInventorySFS, agentInventorySupportedUnitEntry=agentInventorySupportedUnitEntry, agentInventorySFSFail=agentInventorySFSFail, agentInventoryStackPortIndex=agentInventoryStackPortIndex, fastPathInventoryGroups=fastPathInventoryGroups, agentInventoryUnitStandby=agentInventoryUnitStandby, agentInventorySupportedUnitModelIdentifier=agentInventorySupportedUnitModelIdentifier, agentInventoryStackPortConfiguredStackMode=agentInventoryStackPortConfiguredStackMode, PYSNMP_MODULE_ID=fastPathInventory, agentInventoryUnitDetectedCodeVer=agentInventoryUnitDetectedCodeVer, agentInventoryComponentEntry=agentInventoryComponentEntry, agentInventoryStackReplicateSTK=agentInventoryStackReplicateSTK, fastPathInventoryConformance=fastPathInventoryConformance, agentInventoryStackPortTag=agentInventoryStackPortTag, agentInventoryStackTemplateId=agentInventoryStackTemplateId, agentInventoryUnitSupportedUnitIndex=agentInventoryUnitSupportedUnitIndex, agentInventoryStackPortGroup=agentInventoryStackPortGroup, agentInventoryStackPortEntry=agentInventoryStackPortEntry, fastPathInventoryUnitGroup=fastPathInventoryUnitGroup, agentInventoryComponentIndex=agentInventoryComponentIndex, agentInventorySlotInsertedCardType=agentInventorySlotInsertedCardType, agentInventorySFSComplete=agentInventorySFSComplete, agentInventoryUnitAdminMgmtPref=agentInventoryUnitAdminMgmtPref, agentInventorySupportedUnitDescription=agentInventorySupportedUnitDescription, agentInventoryUnitGroup=agentInventoryUnitGroup, fastPathInventoryNotificationsGroup=fastPathInventoryNotificationsGroup, agentInventoryUnitReload=agentInventoryUnitReload, agentInventoryUnitSTKname=agentInventoryUnitSTKname, agentInventoryUnitMgmtAdmin=agentInventoryUnitMgmtAdmin, agentInventoryUnitImage2Version=agentInventoryUnitImage2Version, agentInventoryCardType=agentInventoryCardType, agentInventoryComponentTable=agentInventoryComponentTable, fastPathInventorySlotGroup=fastPathInventorySlotGroup, agentInventorySlotConfiguredCardType=agentInventorySlotConfiguredCardType, agentInventoryStackPortLinkUp=agentInventoryStackPortLinkUp, agentInventoryUnitSerialNumber=agentInventoryUnitSerialNumber, agentInventoryUnitHWMgmtPref=agentInventoryUnitHWMgmtPref, agentInventoryUnitSFSTransferStatus=agentInventoryUnitSFSTransferStatus, agentInventoryCardModelIdentifier=agentInventoryCardModelIdentifier, AgentInventoryCardType=AgentInventoryCardType, agentInventoryStackSTKname=agentInventoryStackSTKname, agentInventoryCardIndex=agentInventoryCardIndex, agentInventorySFSTrap=agentInventorySFSTrap, agentInventoryStackPortUnit=agentInventoryStackPortUnit, agentInventoryStackPortLinkDown=agentInventoryStackPortLinkDown, agentInventoryStackPortLinkStatus=agentInventoryStackPortLinkStatus, agentInventoryUnitStatus=agentInventoryUnitStatus, agentInventoryCardTypeTable=agentInventoryCardTypeTable, agentInventoryUnitEntry=agentInventoryUnitEntry, agentInventoryStackPortTotalErrors=agentInventoryStackPortTotalErrors, agentInventorySFSAllowDowngrade=agentInventorySFSAllowDowngrade, agentInventorySFSStart=agentInventorySFSStart, agentInventoryCardTypeEntry=agentInventoryCardTypeEntry, AgentInventoryUnitPreference=AgentInventoryUnitPreference, agentInventoryUnitDescription=agentInventoryUnitDescription, agentInventoryUnitReplicateSTK=agentInventoryUnitReplicateSTK, agentInventoryCardGroup=agentInventoryCardGroup, agentInventoryStackDeleteSTK=agentInventoryStackDeleteSTK, agentInventorySupportedUnitExpectedCodeVer=agentInventorySupportedUnitExpectedCodeVer, agentInventoryUnitTable=agentInventoryUnitTable, agentInventorySlotCapabilities=agentInventorySlotCapabilities, agentInventoryCardDescription=agentInventoryCardDescription, agentInventoryStackUnitNumber=agentInventoryStackUnitNumber, agentInventorySlotGroup=agentInventorySlotGroup, agentInventoryUnitRowStatus=agentInventoryUnitRowStatus, agentInventorySlotPowerMode=agentInventorySlotPowerMode, agentInventorySupportedUnitTable=agentInventorySupportedUnitTable, agentInventoryUnitAdminMgmtPrefValue=agentInventoryUnitAdminMgmtPrefValue, agentInventoryUnitDetectedCodeInFlashVer=agentInventoryUnitDetectedCodeInFlashVer, agentInventoryCardUnsupported=agentInventoryCardUnsupported, agentInventoryUnitAssignNumber=agentInventoryUnitAssignNumber, fastPathInventoryCompliances=fastPathInventoryCompliances, agentInventoryCardMismatch=agentInventoryCardMismatch, agentInventoryStackPortDataRate=agentInventoryStackPortDataRate, agentInventoryStackMaxUnitNumber=agentInventoryStackMaxUnitNumber, agentInventorySlotNumber=agentInventorySlotNumber, agentInventoryComponentName=agentInventoryComponentName, agentInventoryStackPortLinkSpeed=agentInventoryStackPortLinkSpeed, agentInventoryStackPortErrorRate=agentInventoryStackPortErrorRate, agentInventorySFSGroup=agentInventorySFSGroup, agentInventoryUnitSFSLastAttemptStatus=agentInventoryUnitSFSLastAttemptStatus, agentInventorySlotEntry=agentInventorySlotEntry, agentInventorySlotTable=agentInventorySlotTable, AgentInventoryUnitType=AgentInventoryUnitType, agentInventoryStackReload=agentInventoryStackReload, agentInventoryUnitType=agentInventoryUnitType)
