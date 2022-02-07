#
# PySNMP MIB module WISI-GTMODULES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/wisi/WISI-GTMODULES-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:20:43 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, ModuleIdentity, IpAddress, NotificationType, Counter32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, Integer32, ObjectIdentity, TimeTicks, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ModuleIdentity", "IpAddress", "NotificationType", "Counter32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "Integer32", "ObjectIdentity", "TimeTicks", "Unsigned32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gtUnit, = mibBuilder.importSymbols("WISI-TANGRAM-MIB", "gtUnit")
gtModulesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2))
gtModulesMIB.setRevisions(('2016-09-08 00:00', '2016-06-08 00:00', '2015-06-16 00:00', '2013-07-29 00:00', '2013-06-26 00:00', '2012-10-31 00:00', '2011-12-13 00:00', '2011-09-08 00:00', '2011-04-01 00:00',))
if mibBuilder.loadTexts: gtModulesMIB.setLastUpdated('201609080000Z')
if mibBuilder.loadTexts: gtModulesMIB.setOrganization('WISI Communications GmbH & Co. KG')
gtModulesNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0))
gtModulesObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1))
gtModulesConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2))
gtModulesCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 1))
gtModulesGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2))
gtModulesNotifyPlugin = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 1))
if mibBuilder.loadTexts: gtModulesNotifyPlugin.setStatus('current')
gtModulesNotifyPlugout = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 2))
if mibBuilder.loadTexts: gtModulesNotifyPlugout.setStatus('current')
gtModulesNotifyFailure = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 3))
if mibBuilder.loadTexts: gtModulesNotifyFailure.setStatus('current')
gtModulesNotifyRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 4))
if mibBuilder.loadTexts: gtModulesNotifyRedundancy.setStatus('current')
gtModulesNotifyRedundancyClear = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 5))
if mibBuilder.loadTexts: gtModulesNotifyRedundancyClear.setStatus('current')
gtModulesNotifyFailureClear = NotificationType((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 0, 6))
if mibBuilder.loadTexts: gtModulesNotifyFailureClear.setStatus('current')
gtThisModuleSlot = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtThisModuleSlot.setStatus('current')
gtNumModules = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtNumModules.setStatus('current')
gtModulesTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3), )
if mibBuilder.loadTexts: gtModulesTable.setStatus('current')
gtModulesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1), ).setIndexNames((0, "WISI-GTMODULES-MIB", "gtModule"))
if mibBuilder.loadTexts: gtModulesEntry.setStatus('current')
gtModule = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15)))
if mibBuilder.loadTexts: gtModule.setStatus('current')
gtModuleName = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleName.setStatus('current')
gtModuleHWID = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleHWID.setStatus('current')
gtModuleFWID = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleFWID.setStatus('current')
gtModuleSerNo = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleSerNo.setStatus('current')
gtModuleUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 6), Counter32()).setUnits('s').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleUptime.setStatus('current')
gtModuleLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 7), Counter32()).setUnits('s').setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleLifetime.setStatus('current')
gtModulePower = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gtModulePower.setStatus('current')
gtModuleMode = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleMode.setStatus('current')
gtModuleStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleStatus.setStatus('current')
gtModuleSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleSlot.setStatus('deprecated')
gtModuleFWIDUploaded = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtModuleFWIDUploaded.setStatus('current')
gtModuleReboot = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 3, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("running", 0), ("reboot", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gtModuleReboot.setStatus('current')
gtNumCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtNumCapabilities.setStatus('current')
gtCapabilitiesTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5), )
if mibBuilder.loadTexts: gtCapabilitiesTable.setStatus('current')
gtCapabilitiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5, 1), ).setIndexNames((0, "WISI-GTMODULES-MIB", "gtModule"), (0, "WISI-GTMODULES-MIB", "gtChannel"), (0, "WISI-GTMODULES-MIB", "gtCapability"))
if mibBuilder.loadTexts: gtCapabilitiesEntry.setStatus('current')
gtChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4095)))
if mibBuilder.loadTexts: gtChannel.setStatus('current')
gtCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtCapability.setStatus('current')
gtInputsTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7), )
if mibBuilder.loadTexts: gtInputsTable.setStatus('current')
gtInputsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1), ).setIndexNames((0, "WISI-GTMODULES-MIB", "gtModule"), (0, "WISI-GTMODULES-MIB", "gtInputsTableIdx"))
if mibBuilder.loadTexts: gtInputsEntry.setStatus('current')
gtInputsTableIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: gtInputsTableIdx.setStatus('current')
gtInputChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtInputChannel.setStatus('current')
gtInputName = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gtInputName.setStatus('current')
gtOutputsTable = MibTable((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8), )
if mibBuilder.loadTexts: gtOutputsTable.setStatus('current')
gtOutputsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1), ).setIndexNames((0, "WISI-GTMODULES-MIB", "gtModule"), (0, "WISI-GTMODULES-MIB", "gtOutputsTableIdx"))
if mibBuilder.loadTexts: gtOutputsEntry.setStatus('current')
gtOutputsTableIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 256)))
if mibBuilder.loadTexts: gtOutputsTableIdx.setStatus('current')
gtOutputChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: gtOutputChannel.setStatus('current')
gtOutputName = MibTableColumn((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 1, 8, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: gtOutputName.setStatus('current')
gtModulesMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 1, 1)).setObjects(("WISI-GTMODULES-MIB", "gtModulesV1Group"), ("WISI-GTMODULES-MIB", "gtModulesSystemGroup"), ("WISI-GTMODULES-MIB", "gtModulesStatsGroup"), ("WISI-GTMODULES-MIB", "gtModulesTrapGroup"), ("WISI-GTMODULES-MIB", "gtModulesSetGroup"), ("WISI-GTMODULES-MIB", "gtModulesBasicNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtModulesMIBCompliance = gtModulesMIBCompliance.setStatus('current')
gtModulesV1Group = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 1)).setObjects(("WISI-GTMODULES-MIB", "gtThisModuleSlot"), ("WISI-GTMODULES-MIB", "gtNumModules"), ("WISI-GTMODULES-MIB", "gtModuleName"), ("WISI-GTMODULES-MIB", "gtModuleHWID"), ("WISI-GTMODULES-MIB", "gtModuleFWID"), ("WISI-GTMODULES-MIB", "gtModuleSerNo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtModulesV1Group = gtModulesV1Group.setStatus('current')
gtModulesSystemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 2)).setObjects(("WISI-GTMODULES-MIB", "gtThisModuleSlot"), ("WISI-GTMODULES-MIB", "gtNumModules"), ("WISI-GTMODULES-MIB", "gtModuleName"), ("WISI-GTMODULES-MIB", "gtModuleHWID"), ("WISI-GTMODULES-MIB", "gtModuleFWID"), ("WISI-GTMODULES-MIB", "gtModuleSerNo"), ("WISI-GTMODULES-MIB", "gtCapability"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtModulesSystemGroup = gtModulesSystemGroup.setStatus('current')
gtModulesStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 3)).setObjects(("WISI-GTMODULES-MIB", "gtNumModules"), ("WISI-GTMODULES-MIB", "gtModuleUptime"), ("WISI-GTMODULES-MIB", "gtModuleLifetime"), ("WISI-GTMODULES-MIB", "gtNumCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtModulesStatsGroup = gtModulesStatsGroup.setStatus('current')
gtModulesTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 4))
gtModulesSetGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 5))
gtModulesBasicNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 7465, 20, 2, 9, 1, 2, 2, 2, 6)).setObjects(("WISI-GTMODULES-MIB", "gtModulesNotifyPlugin"), ("WISI-GTMODULES-MIB", "gtModulesNotifyPlugout"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    gtModulesBasicNotificationsGroup = gtModulesBasicNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("WISI-GTMODULES-MIB", gtModulesObjects=gtModulesObjects, gtModule=gtModule, gtModuleMode=gtModuleMode, gtOutputsTableIdx=gtOutputsTableIdx, gtCapability=gtCapability, gtOutputsTable=gtOutputsTable, gtModulesNotifyPlugin=gtModulesNotifyPlugin, gtCapabilitiesTable=gtCapabilitiesTable, gtCapabilitiesEntry=gtCapabilitiesEntry, gtModulesMIB=gtModulesMIB, gtInputName=gtInputName, gtThisModuleSlot=gtThisModuleSlot, gtOutputChannel=gtOutputChannel, gtModulePower=gtModulePower, gtModulesTable=gtModulesTable, gtModuleUptime=gtModuleUptime, gtModulesNotifyRedundancyClear=gtModulesNotifyRedundancyClear, gtNumModules=gtNumModules, gtOutputsEntry=gtOutputsEntry, gtModuleSerNo=gtModuleSerNo, gtInputsTable=gtInputsTable, gtModulesEntry=gtModulesEntry, gtChannel=gtChannel, gtNumCapabilities=gtNumCapabilities, gtModulesNotifyFailure=gtModulesNotifyFailure, gtModuleHWID=gtModuleHWID, gtModuleStatus=gtModuleStatus, gtModulesSystemGroup=gtModulesSystemGroup, gtModuleReboot=gtModuleReboot, gtModulesConformance=gtModulesConformance, gtModulesBasicNotificationsGroup=gtModulesBasicNotificationsGroup, gtModulesGroups=gtModulesGroups, gtModulesCompliances=gtModulesCompliances, gtOutputName=gtOutputName, gtModuleLifetime=gtModuleLifetime, gtInputChannel=gtInputChannel, gtModuleFWID=gtModuleFWID, gtModulesV1Group=gtModulesV1Group, gtModulesTrapGroup=gtModulesTrapGroup, gtInputsEntry=gtInputsEntry, gtModulesMIBCompliance=gtModulesMIBCompliance, gtModulesNotifyPlugout=gtModulesNotifyPlugout, gtModulesNotifyRedundancy=gtModulesNotifyRedundancy, gtModulesStatsGroup=gtModulesStatsGroup, gtInputsTableIdx=gtInputsTableIdx, PYSNMP_MODULE_ID=gtModulesMIB, gtModuleFWIDUploaded=gtModuleFWIDUploaded, gtModulesNotifications=gtModulesNotifications, gtModulesSetGroup=gtModulesSetGroup, gtModuleSlot=gtModuleSlot, gtModulesNotifyFailureClear=gtModulesNotifyFailureClear, gtModuleName=gtModuleName)
