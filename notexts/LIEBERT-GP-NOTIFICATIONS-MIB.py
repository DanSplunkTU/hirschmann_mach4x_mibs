#
# PySNMP MIB module LIEBERT-GP-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-NOTIFY-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:17:17 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
lgpConditionTableRowRef, lgpConditionTableRef, lgpConditionDescr, lgpConditionTime, lgpConditionId = mibBuilder.importSymbols("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRowRef", "lgpConditionTableRef", "lgpConditionDescr", "lgpConditionTime", "lgpConditionId")
liebertNotificationsModuleReg, lgpNotifications = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "liebertNotificationsModuleReg", "lgpNotifications")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
iso, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Integer32, Gauge32, ModuleIdentity, Counter64, MibIdentifier, Counter32, IpAddress, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Integer32", "Gauge32", "ModuleIdentity", "Counter64", "MibIdentifier", "Counter32", "IpAddress", "Bits", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
liebertGlobalProductsNotificationsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 4, 1))
liebertGlobalProductsNotificationsModule.setRevisions(('2008-07-02 00:00', '2008-05-15 00:00', '2008-01-10 00:00', '2006-08-15 00:00', '2006-02-22 00:00',))
if mibBuilder.loadTexts: liebertGlobalProductsNotificationsModule.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: liebertGlobalProductsNotificationsModule.setOrganization('Liebert Corporation')
lgpEventNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0))
if mibBuilder.loadTexts: lgpEventNotifications.setStatus('current')
lgpEventParameters = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10))
if mibBuilder.loadTexts: lgpEventParameters.setStatus('current')
lgpEventParmTableRef = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpEventParmTableRef.setStatus('current')
lgpEventParmTableRowRef = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpEventParmTableRowRef.setStatus('current')
lgpEventConditionEntryAdded = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 1)).setObjects(("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionId"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionDescr"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTime"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRef"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRowRef"))
if mibBuilder.loadTexts: lgpEventConditionEntryAdded.setStatus('current')
lgpEventConditionEntryRemoved = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 2)).setObjects(("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionId"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionDescr"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTime"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRef"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRowRef"))
if mibBuilder.loadTexts: lgpEventConditionEntryRemoved.setStatus('current')
lgpEventLowBatteryWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 3)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventLowBatteryWarning.setStatus('current')
lgpEventLoadTransferedToBypass = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 4)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventLoadTransferedToBypass.setStatus('current')
lgpEventInternalFault = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 5)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventInternalFault.setStatus('current')
lgpEventBatteryTestFailed = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 6)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventBatteryTestFailed.setStatus('current')
lgpEventOutputOverload = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 7)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventOutputOverload.setStatus('current')
lgpEventEstablishedPowerRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 8)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventEstablishedPowerRedundancy.setStatus('current')
lgpEventLostPowerRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 9)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventLostPowerRedundancy.setStatus('current')
lgpEventPowerModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 10)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventPowerModuleFailure.setStatus('current')
lgpEventBatteryModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 11)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventBatteryModuleFailure.setStatus('current')
lgpEventControlModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 12)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventControlModuleFailure.setStatus('current')
lgpEventPowerModuleWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 13)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventPowerModuleWarning.setStatus('current')
lgpEventBatteryModuleWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 14)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventBatteryModuleWarning.setStatus('current')
lgpEventControlModuleWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 15)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventControlModuleWarning.setStatus('current')
lgpEventAgentFirmwareUpdateSuccessful = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 16)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventAgentFirmwareUpdateSuccessful.setStatus('deprecated')
lgpEventAgentFirmwareCorrupt = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 17)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventAgentFirmwareCorrupt.setStatus('deprecated')
lgpEventConfigModified = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 18)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventConfigModified.setStatus('current')
lgpEventModuleAdded = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 19)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventModuleAdded.setStatus('current')
lgpEventModuleRemoved = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 20)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventModuleRemoved.setStatus('current')
lgpEventRcpPowerStateChangeOn = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 21)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpPowerStateChangeOn.setStatus('current')
lgpEventRcpPowerStateChangeOff = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 22)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpPowerStateChangeOff.setStatus('current')
lgpEventRcpLoadAdded = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 23)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpLoadAdded.setStatus('current')
lgpEventRcpLoadRemoved = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 24)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpLoadRemoved.setStatus('current')
mibBuilder.exportSymbols("LIEBERT-GP-NOTIFICATIONS-MIB", lgpEventControlModuleFailure=lgpEventControlModuleFailure, lgpEventBatteryTestFailed=lgpEventBatteryTestFailed, lgpEventParmTableRef=lgpEventParmTableRef, lgpEventConditionEntryRemoved=lgpEventConditionEntryRemoved, lgpEventLoadTransferedToBypass=lgpEventLoadTransferedToBypass, lgpEventConditionEntryAdded=lgpEventConditionEntryAdded, lgpEventBatteryModuleWarning=lgpEventBatteryModuleWarning, lgpEventPowerModuleFailure=lgpEventPowerModuleFailure, lgpEventRcpPowerStateChangeOn=lgpEventRcpPowerStateChangeOn, lgpEventInternalFault=lgpEventInternalFault, lgpEventPowerModuleWarning=lgpEventPowerModuleWarning, PYSNMP_MODULE_ID=liebertGlobalProductsNotificationsModule, liebertGlobalProductsNotificationsModule=liebertGlobalProductsNotificationsModule, lgpEventModuleRemoved=lgpEventModuleRemoved, lgpEventLostPowerRedundancy=lgpEventLostPowerRedundancy, lgpEventParameters=lgpEventParameters, lgpEventParmTableRowRef=lgpEventParmTableRowRef, lgpEventAgentFirmwareUpdateSuccessful=lgpEventAgentFirmwareUpdateSuccessful, lgpEventNotifications=lgpEventNotifications, lgpEventRcpPowerStateChangeOff=lgpEventRcpPowerStateChangeOff, lgpEventRcpLoadAdded=lgpEventRcpLoadAdded, lgpEventLowBatteryWarning=lgpEventLowBatteryWarning, lgpEventOutputOverload=lgpEventOutputOverload, lgpEventControlModuleWarning=lgpEventControlModuleWarning, lgpEventModuleAdded=lgpEventModuleAdded, lgpEventConfigModified=lgpEventConfigModified, lgpEventRcpLoadRemoved=lgpEventRcpLoadRemoved, lgpEventBatteryModuleFailure=lgpEventBatteryModuleFailure, lgpEventAgentFirmwareCorrupt=lgpEventAgentFirmwareCorrupt, lgpEventEstablishedPowerRedundancy=lgpEventEstablishedPowerRedundancy)
