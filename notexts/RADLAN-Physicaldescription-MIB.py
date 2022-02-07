#
# PySNMP MIB module RADLAN-Physicaldescription-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-Physicaldescription-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:18:39 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
EntitySensorValue, EntitySensorStatus = mibBuilder.importSymbols("ENTITY-SENSOR-MIB", "EntitySensorValue", "EntitySensorStatus")
ifIndex, InterfaceIndex, InterfaceIndexOrZero = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex", "InterfaceIndexOrZero")
JackType, = mibBuilder.importSymbols("MAU-MIB", "JackType")
RlEnvMonState, = mibBuilder.importSymbols("RADLAN-HWENVIROMENT", "RlEnvMonState")
rnd, rndErrorDesc, rndNotifications, rndErrorSeverity = mibBuilder.importSymbols("RADLAN-MIB", "rnd", "rndErrorDesc", "rndNotifications", "rndErrorSeverity")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, NotificationType, NotificationType, Integer32, Bits, Gauge32, IpAddress, ObjectIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, ModuleIdentity, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "NotificationType", "NotificationType", "Integer32", "Bits", "Gauge32", "IpAddress", "ObjectIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "ModuleIdentity", "iso", "Counter64")
DisplayString, TextualConvention, PhysAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "PhysAddress", "RowStatus")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlPhysicalDescription = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 53))
rlPhysicalDescription.setRevisions(('2003-10-18 00:00',))
if mibBuilder.loadTexts: rlPhysicalDescription.setLastUpdated('200310180000Z')
if mibBuilder.loadTexts: rlPhysicalDescription.setOrganization('Radlan Computer Communications Ltd.')
rlPhdMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdMibVersion.setStatus('current')
rlPhdModuleTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 2), )
if mibBuilder.loadTexts: rlPhdModuleTable.setStatus('current')
rlPhdModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 2, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdModuleStackUnit"), (0, "RADLAN-Physicaldescription-MIB", "rlPhdModuleIndex"))
if mibBuilder.loadTexts: rlPhdModuleEntry.setStatus('current')
rlPhdModuleStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleStackUnit.setStatus('current')
rlPhdModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleIndex.setStatus('current')
rlPhdModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleType.setStatus('current')
rlPhdModuleStartingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleStartingPort.setStatus('current')
rlPhdModuleNumberOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleNumberOfPorts.setStatus('current')
rlPhdModuleRow = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleRow.setStatus('current')
rlPhdModuleColumn = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleColumn.setStatus('current')
rlPhdModuleRole = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("standalone", 1), ("master", 2), ("backup", 3), ("slave", 4))).clone('standalone')).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleRole.setStatus('current')
rlPhdPortsTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 3), )
if mibBuilder.loadTexts: rlPhdPortsTable.setStatus('current')
rlPhdPortsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 3, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdPortsIfIndex"))
if mibBuilder.loadTexts: rlPhdPortsEntry.setStatus('current')
rlPhdPortsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsIfIndex.setStatus('current')
rlPhdPortsIfIndexName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsIfIndexName.setStatus('current')
rlPhdPortsMediaType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("copper", 1), ("optic-fiber", 2), ("combo", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsMediaType.setStatus('current')
rlPhdPortsStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsStackUnit.setStatus('current')
rlPhdPortsModuleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsModuleNumber.setStatus('current')
rlPhdPortsRow = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsRow.setStatus('current')
rlPhdPortsColumn = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortsColumn.setStatus('current')
rlPhdConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 8), JackType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdConnectorType.setStatus('current')
rlPhdPortHaul = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("not-relevant", 1), ("short", 2), ("long", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPortHaul.setStatus('current')
rlPhdStackTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 4), )
if mibBuilder.loadTexts: rlPhdStackTable.setStatus('current')
rlPhdStackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 4, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdStackUnit"))
if mibBuilder.loadTexts: rlPhdStackEntry.setStatus('current')
rlPhdStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackUnit.setStatus('current')
rlPhdStackType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackType.setStatus('current')
rlPhdStackConnect1 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackConnect1.setStatus('current')
rlPhdStackConnect2 = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackConnect2.setStatus('current')
rlPhdStackSofrwareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackSofrwareVer.setStatus('current')
rlPhdStackProductID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackProductID.setStatus('current')
rlPhdStackMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 4, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackMacAddr.setStatus('current')
rlPhdModuleHotSwapTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 5), )
if mibBuilder.loadTexts: rlPhdModuleHotSwapTable.setStatus('current')
rlPhdModuleHotSwapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 5, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdModuleStackUnit"), (0, "RADLAN-Physicaldescription-MIB", "rlPhdModuleIndex"))
if mibBuilder.loadTexts: rlPhdModuleHotSwapEntry.setStatus('current')
rlPhdModuleHotSwapAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdModuleHotSwapAdminStatus.setStatus('current')
rlPhdModuleHotSwapOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdModuleHotSwapOperStatus.setStatus('current')
rlPhdStackOrderTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 6), )
if mibBuilder.loadTexts: rlPhdStackOrderTable.setStatus('current')
rlPhdStackOrderEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 6, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdStackOrderCurrentUnitPosition"))
if mibBuilder.loadTexts: rlPhdStackOrderEntry.setStatus('current')
rlPhdStackOrderCurrentUnitPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 1), Integer32())
if mibBuilder.loadTexts: rlPhdStackOrderCurrentUnitPosition.setStatus('current')
rlPhdStackOrderDesiredUnitPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderDesiredUnitPosition.setStatus('current')
rlPhdStackOrderUnitIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 3), Integer32())
if mibBuilder.loadTexts: rlPhdStackOrderUnitIndex.setStatus('current')
rlPhdStackOrderUnitType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 6, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdStackOrderUnitType.setStatus('current')
rlPhdStackReorder = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reorder", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackReorder.setStatus('current')
rlPhdNumberOfUnits = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdNumberOfUnits.setStatus('current')
rlPhdMaxNumberOfUnits = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdMaxNumberOfUnits.setStatus('current')
rlPhdForceMasterUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdForceMasterUnit.setStatus('current')
rlPhdStackFixedUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackFixedUnit.setStatus('current')
rlPhdStackFixedUnitLocation = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bottom", 1), ("top", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackFixedUnitLocation.setStatus('current')
rlPhdStackReloadUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackReloadUnit.setStatus('current')
rlPhdUnitGenParamTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 14), )
if mibBuilder.loadTexts: rlPhdUnitGenParamTable.setStatus('current')
rlPhdUnitGenParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 14, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdUnitGenParamStackUnit"))
if mibBuilder.loadTexts: rlPhdUnitGenParamEntry.setStatus('current')
rlPhdUnitGenParamStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamStackUnit.setStatus('current')
rlPhdUnitGenParamSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamSoftwareVersion.setStatus('current')
rlPhdUnitGenParamFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamFirmwareVersion.setStatus('current')
rlPhdUnitGenParamHardwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamHardwareVersion.setStatus('current')
rlPhdUnitGenParamSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitGenParamSerialNum.setStatus('current')
rlPhdUnitGenParamAssetTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdUnitGenParamAssetTag.setStatus('current')
rlPhdUnitGenParamServiceTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 14, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitGenParamServiceTag.setStatus('current')
rlPhdUnitEnvParamTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 15), )
if mibBuilder.loadTexts: rlPhdUnitEnvParamTable.setStatus('current')
rlPhdUnitEnvParamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 15, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdUnitEnvParamStackUnit"))
if mibBuilder.loadTexts: rlPhdUnitEnvParamEntry.setStatus('current')
rlPhdUnitEnvParamStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamStackUnit.setStatus('current')
rlPhdUnitEnvParamMainPSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 2), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamMainPSStatus.setStatus('current')
rlPhdUnitEnvParamRedundantPSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 3), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamRedundantPSStatus.setStatus('current')
rlPhdUnitEnvParamFan1Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 4), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan1Status.setStatus('current')
rlPhdUnitEnvParamFan2Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 5), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan2Status.setStatus('current')
rlPhdUnitEnvParamFan3Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 6), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan3Status.setStatus('current')
rlPhdUnitEnvParamFan4Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 7), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan4Status.setStatus('current')
rlPhdUnitEnvParamFan5Status = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 8), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamFan5Status.setStatus('current')
rlPhdUnitEnvParamTempSensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 9), EntitySensorValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensorValue.setStatus('current')
rlPhdUnitEnvParamTempSensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 10), EntitySensorStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamTempSensorStatus.setStatus('current')
rlPhdUnitEnvParamUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 15, 1, 11), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdUnitEnvParamUpTime.setStatus('current')
rlPhdStackOrderTopUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 16), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderTopUnit.setStatus('current')
rlPhdStackOrderBottomUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderBottomUnit.setStatus('current')
rlPhdStackOrderPermutation = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 18), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdStackOrderPermutation.setStatus('current')
rlPhdNumberOfPoeUnits = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 19), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdNumberOfPoeUnits.setStatus('current')
rlPhdPoeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 20), )
if mibBuilder.loadTexts: rlPhdPoeTable.setStatus('current')
rlPhdPoeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 20, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlPhdPoeStackUnit"))
if mibBuilder.loadTexts: rlPhdPoeEntry.setStatus('current')
rlPhdPoeStackUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 20, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPoeStackUnit.setStatus('current')
rlPhdPoePresent = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPhdPoePresent.setStatus('current')
rlPhdPhyLedStackUnit = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdPhyLedStackUnit.setStatus('current')
rlPhdPhyLedTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 53, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlPhdPhyLedTimeout.setStatus('current')
rlCascadeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 23), )
if mibBuilder.loadTexts: rlCascadeTable.setStatus('current')
rlCascadeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 23, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: rlCascadeEntry.setStatus('current')
rlCascadeNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeNeighborIfIndex.setStatus('current')
rlCascadeNeighborUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeNeighborUnit.setStatus('current')
rlCascadeTrunkId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 23, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeTrunkId.setStatus('current')
rlCascadeAfterResetTable = MibTable((1, 3, 6, 1, 4, 1, 89, 53, 24), )
if mibBuilder.loadTexts: rlCascadeAfterResetTable.setStatus('current')
rlCascadeAfterResetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 53, 24, 1), ).setIndexNames((0, "RADLAN-Physicaldescription-MIB", "rlCascadeIfIndexAfterReset"))
if mibBuilder.loadTexts: rlCascadeAfterResetEntry.setStatus('current')
rlCascadeIfIndexAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCascadeIfIndexAfterReset.setStatus('current')
rlCascadeTrunkIdAfterReset = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCascadeTrunkIdAfterReset.setStatus('current')
rlCascadeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 53, 24, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlCascadeRowStatus.setStatus('current')
rlStackUnitRemoved = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 186)).setObjects(("RADLAN-MIB", "rndErrorDesc"), ("RADLAN-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackUnitRemoved.setStatus('current')
rlStackConfigChangedRingChain = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 187)).setObjects(("RADLAN-MIB", "rndErrorDesc"), ("RADLAN-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackConfigChangedRingChain.setStatus('current')
rlStackBackupUnitRemoved = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 188)).setObjects(("RADLAN-MIB", "rndErrorDesc"), ("RADLAN-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackBackupUnitRemoved.setStatus('current')
rlStackMasterSwitchover = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 189)).setObjects(("RADLAN-MIB", "rndErrorDesc"), ("RADLAN-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackMasterSwitchover.setStatus('current')
rlStackUnitDifferentSwVersion = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 190)).setObjects(("RADLAN-MIB", "rndErrorDesc"), ("RADLAN-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackUnitDifferentSwVersion.setStatus('current')
rlStackDuplicateUnitNotJoin = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 191)).setObjects(("RADLAN-MIB", "rndErrorDesc"), ("RADLAN-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackDuplicateUnitNotJoin.setStatus('current')
rlStackLinkChange = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 195)).setObjects(("RADLAN-MIB", "rndErrorDesc"), ("RADLAN-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlStackLinkChange.setStatus('current')
mibBuilder.exportSymbols("RADLAN-Physicaldescription-MIB", rlPhdStackOrderTopUnit=rlPhdStackOrderTopUnit, rlPhdUnitEnvParamEntry=rlPhdUnitEnvParamEntry, rlPhdUnitEnvParamFan2Status=rlPhdUnitEnvParamFan2Status, rlPhdPortsTable=rlPhdPortsTable, rlPhdPoeEntry=rlPhdPoeEntry, PYSNMP_MODULE_ID=rlPhysicalDescription, rlPhdPortHaul=rlPhdPortHaul, rlPhdModuleRow=rlPhdModuleRow, rlPhdModuleRole=rlPhdModuleRole, rlPhdStackSofrwareVer=rlPhdStackSofrwareVer, rlCascadeAfterResetEntry=rlCascadeAfterResetEntry, rlPhdPoeStackUnit=rlPhdPoeStackUnit, rlPhdUnitGenParamTable=rlPhdUnitGenParamTable, rlPhdStackUnit=rlPhdStackUnit, rlPhdUnitEnvParamTable=rlPhdUnitEnvParamTable, rlPhdModuleHotSwapEntry=rlPhdModuleHotSwapEntry, rlPhysicalDescription=rlPhysicalDescription, rlPhdModuleColumn=rlPhdModuleColumn, rlStackLinkChange=rlStackLinkChange, rlPhdUnitGenParamStackUnit=rlPhdUnitGenParamStackUnit, rlPhdStackOrderBottomUnit=rlPhdStackOrderBottomUnit, rlPhdNumberOfUnits=rlPhdNumberOfUnits, rlPhdPoeTable=rlPhdPoeTable, rlPhdUnitGenParamEntry=rlPhdUnitGenParamEntry, rlStackUnitRemoved=rlStackUnitRemoved, rlPhdConnectorType=rlPhdConnectorType, rlStackMasterSwitchover=rlStackMasterSwitchover, rlPhdUnitEnvParamTempSensorStatus=rlPhdUnitEnvParamTempSensorStatus, rlPhdMibVersion=rlPhdMibVersion, rlPhdUnitEnvParamFan1Status=rlPhdUnitEnvParamFan1Status, rlPhdStackFixedUnit=rlPhdStackFixedUnit, rlCascadeAfterResetTable=rlCascadeAfterResetTable, rlPhdUnitEnvParamRedundantPSStatus=rlPhdUnitEnvParamRedundantPSStatus, rlCascadeNeighborIfIndex=rlCascadeNeighborIfIndex, rlPhdUnitEnvParamFan3Status=rlPhdUnitEnvParamFan3Status, rlStackBackupUnitRemoved=rlStackBackupUnitRemoved, rlCascadeEntry=rlCascadeEntry, rlPhdPortsRow=rlPhdPortsRow, rlPhdPhyLedStackUnit=rlPhdPhyLedStackUnit, rlPhdUnitGenParamSoftwareVersion=rlPhdUnitGenParamSoftwareVersion, rlPhdUnitGenParamServiceTag=rlPhdUnitGenParamServiceTag, rlCascadeTrunkIdAfterReset=rlCascadeTrunkIdAfterReset, rlPhdModuleStartingPort=rlPhdModuleStartingPort, rlPhdStackOrderTable=rlPhdStackOrderTable, rlPhdStackProductID=rlPhdStackProductID, rlPhdPortsEntry=rlPhdPortsEntry, rlPhdStackEntry=rlPhdStackEntry, rlPhdStackOrderEntry=rlPhdStackOrderEntry, rlPhdStackType=rlPhdStackType, rlPhdUnitGenParamFirmwareVersion=rlPhdUnitGenParamFirmwareVersion, rlPhdNumberOfPoeUnits=rlPhdNumberOfPoeUnits, rlCascadeTable=rlCascadeTable, rlPhdPortsIfIndexName=rlPhdPortsIfIndexName, rlPhdStackOrderPermutation=rlPhdStackOrderPermutation, rlStackDuplicateUnitNotJoin=rlStackDuplicateUnitNotJoin, rlPhdPortsMediaType=rlPhdPortsMediaType, rlPhdPortsIfIndex=rlPhdPortsIfIndex, rlPhdModuleHotSwapOperStatus=rlPhdModuleHotSwapOperStatus, rlPhdStackReorder=rlPhdStackReorder, rlPhdModuleStackUnit=rlPhdModuleStackUnit, rlCascadeRowStatus=rlCascadeRowStatus, rlPhdUnitEnvParamFan5Status=rlPhdUnitEnvParamFan5Status, rlPhdPortsStackUnit=rlPhdPortsStackUnit, rlPhdUnitGenParamHardwareVersion=rlPhdUnitGenParamHardwareVersion, rlPhdPortsModuleNumber=rlPhdPortsModuleNumber, rlPhdUnitEnvParamTempSensorValue=rlPhdUnitEnvParamTempSensorValue, rlStackUnitDifferentSwVersion=rlStackUnitDifferentSwVersion, rlPhdStackReloadUnit=rlPhdStackReloadUnit, rlPhdPhyLedTimeout=rlPhdPhyLedTimeout, rlCascadeIfIndexAfterReset=rlCascadeIfIndexAfterReset, rlCascadeNeighborUnit=rlCascadeNeighborUnit, rlPhdUnitEnvParamStackUnit=rlPhdUnitEnvParamStackUnit, rlPhdStackConnect1=rlPhdStackConnect1, rlPhdModuleHotSwapAdminStatus=rlPhdModuleHotSwapAdminStatus, rlPhdStackOrderCurrentUnitPosition=rlPhdStackOrderCurrentUnitPosition, rlPhdModuleHotSwapTable=rlPhdModuleHotSwapTable, rlStackConfigChangedRingChain=rlStackConfigChangedRingChain, rlPhdPoePresent=rlPhdPoePresent, rlPhdForceMasterUnit=rlPhdForceMasterUnit, rlPhdModuleIndex=rlPhdModuleIndex, rlPhdModuleTable=rlPhdModuleTable, rlPhdUnitEnvParamUpTime=rlPhdUnitEnvParamUpTime, rlPhdStackFixedUnitLocation=rlPhdStackFixedUnitLocation, rlPhdUnitEnvParamMainPSStatus=rlPhdUnitEnvParamMainPSStatus, rlPhdUnitGenParamSerialNum=rlPhdUnitGenParamSerialNum, rlPhdMaxNumberOfUnits=rlPhdMaxNumberOfUnits, rlPhdUnitEnvParamFan4Status=rlPhdUnitEnvParamFan4Status, rlPhdModuleEntry=rlPhdModuleEntry, rlPhdPortsColumn=rlPhdPortsColumn, rlPhdStackOrderUnitType=rlPhdStackOrderUnitType, rlPhdUnitGenParamAssetTag=rlPhdUnitGenParamAssetTag, rlPhdStackOrderDesiredUnitPosition=rlPhdStackOrderDesiredUnitPosition, rlPhdStackMacAddr=rlPhdStackMacAddr, rlPhdStackTable=rlPhdStackTable, rlCascadeTrunkId=rlCascadeTrunkId, rlPhdStackConnect2=rlPhdStackConnect2, rlPhdModuleType=rlPhdModuleType, rlPhdStackOrderUnitIndex=rlPhdStackOrderUnitIndex, rlPhdModuleNumberOfPorts=rlPhdModuleNumberOfPorts)
