#
# PySNMP MIB module LIEBERT-GP-NOTIFICATIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-NOTIFY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:47:52 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
lgpConditionDescr, lgpConditionTableRef, lgpConditionTime, lgpConditionId, lgpConditionTableRowRef = mibBuilder.importSymbols("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionDescr", "lgpConditionTableRef", "lgpConditionTime", "lgpConditionId", "lgpConditionTableRowRef")
lgpNotifications, liebertNotificationsModuleReg = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "lgpNotifications", "liebertNotificationsModuleReg")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Counter64, NotificationType, Bits, ObjectIdentity, TimeTicks, Gauge32, IpAddress, Counter32, Unsigned32, ModuleIdentity, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Bits", "ObjectIdentity", "TimeTicks", "Gauge32", "IpAddress", "Counter32", "Unsigned32", "ModuleIdentity", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
liebertGlobalProductsNotificationsModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 4, 1))
liebertGlobalProductsNotificationsModule.setRevisions(('2008-07-02 00:00', '2008-05-15 00:00', '2008-01-10 00:00', '2006-08-15 00:00', '2006-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: liebertGlobalProductsNotificationsModule.setRevisionsDescriptions(('   o Added Notifications for PDU devices (power on/off).  \n       o Added lgpEventParameters branch for defining notification payload \n         that specifically identifies objects that are contained in tables.\n       o Added new varbind to the lgpEventConditionEntryAdded and\n         lgpEventConditionEntryRemoved notifications.\n       o Fixed minor SMIv2 warnings and issues\n   ', '   o Added Notifications for PDU devices (power on/off).  \n       o Added lgpEventParameters branch for defining notification payload \n         that specifically identifies objects that are contained in tables.\n       o Added new varbind to the lgpEventConditionEntryAdded and\n         lgpEventConditionEntryRemoved notifications.\n       o Fixed minor SMIv2 warnings and issues\n   ', 'Modified contact email address and deprecated both:\n      o lgpEventAgentFirmwareUpdateSuccessful\n      o lgpEventAgentFirmwareCorrupt\n    which were moved to the LIEBERT-GP-AGENT-MIB document.', 'Added events for firmware update successful and for firmware corrupt.', 'Added support for Liebert DS Unit.',))
if mibBuilder.loadTexts: liebertGlobalProductsNotificationsModule.setLastUpdated('200807020000Z')
if mibBuilder.loadTexts: liebertGlobalProductsNotificationsModule.setOrganization('Liebert Corporation')
if mibBuilder.loadTexts: liebertGlobalProductsNotificationsModule.setContactInfo('Contact:   Technical Support\n\n      Postal:\n      Liebert Corporation\n      1050 Dearborn Drive\n      P.O. Box 29186\n      Columbus OH, 43229\n      US\n\n      Tel: +1 (800) 222-5877\n\n      E-mail: liebert.monitoring@vertivco.com\n      Web:    www.vertivco.com\n\n      Author:  Craig S. Ward')
if mibBuilder.loadTexts: liebertGlobalProductsNotificationsModule.setDescription("The MIB module used to register Liebert SNMP OIDs.\n\n      Copyright 2000-2008 Liebert Corporation. All rights reserved.\n      Reproduction of this document is authorized on the condition\n      that the forgoing copyright notice is included.\n\n      This Specification is supplied 'AS IS' and Liebert Corporation\n      makes no warranty, either express or implied, as to the use,\n      operation, condition, or performance of the Specification.")
lgpEventNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0))
if mibBuilder.loadTexts: lgpEventNotifications.setStatus('current')
if mibBuilder.loadTexts: lgpEventNotifications.setDescription('Notifications for Liebert Global Products.')
lgpEventParameters = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10))
if mibBuilder.loadTexts: lgpEventParameters.setStatus('current')
if mibBuilder.loadTexts: lgpEventParameters.setDescription('This sub tree describes various parameters/data that are carried\n         in the payload of some notifications.')
lgpEventParmTableRef = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10, 5), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpEventParmTableRef.setStatus('current')
if mibBuilder.loadTexts: lgpEventParmTableRef.setDescription("This object will be included as a varbind in some\n             lgpEventNotifications.  It is a reference to a table object in \n             the MIB.  The value of this object will be the OID of a table \n             that the object that the notification applies to is defined.\n             The notification containing this object will also contain \n             a varbind 'lgpEventParmTableRowRef' that will specify which \n             instance (row) in the table the object is defined in.\n\n             Example:\n               NOTIFICATION: lgpEventConditionEntryAdded\n               varbind: lgpConditionId          6\n               varbind: lgpConditionDescr       lgpConditionRcpBranchBreakerOpen\n               varbind: lgpConditionTime        393884848\n               varbind: lgpEventParmTableRef    lgpPduRbTable\n               varbind: lgpEventParmTableRowRef lgpPduRbEntryId.1.4\n\n             In the above example the breaker opened for a Receptacle branch.\n             The specific receptacle branch is specified by the additional\n             varbind (lgpEventParmTableRowRef).  In this case the notification\n             is for the 4th receptacle branch on the 1st PDU in the PDU cluster.\n            ")
lgpEventParmTableRowRef = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 10, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpEventParmTableRowRef.setStatus('current')
if mibBuilder.loadTexts: lgpEventParmTableRowRef.setDescription('This is a reference to the intersection of a row and column (cell)\n             in the table specified by the companion varbind \n             (lgpEventParmTableRef) in this notification.  The row in the\n             table where this cell exists represents the object that this\n             notification applies to.\n\n             Example:\n               NOTIFICATION: lgpEventRcpPowerStateChangeOff\n               varbind: sysUpTime               393885975\n               varbind: lgpEventParmTableRef    lgpPduRcpTable\n               varbind: lgpEventParmTableRowRef lgpPduRcpEntryId.2.4.5\n\n             In the above example the power state changed for a Receptacle.\n\n             The table containing the definition of the receptacle\n             (lgpPduRcpTable) is given by the varbind (lgpEventParmTableRef)\n\n             The specific receptacle is specified by the varbind\n             (lgpEventParmTableRowRef).  In this case the notification\n             is for the 5th receptacle on the 4th receptacle branch on the \n             2nd PDU in the PDU cluster.\n\n             If one wanted to retrieve the user assigned label for this \n             receptacle the OID would be: lgpPduRcpEntryUsrLabel.2.4.5\n            ')
lgpEventConditionEntryAdded = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 1)).setObjects(("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionId"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionDescr"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTime"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRef"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRowRef"))
if mibBuilder.loadTexts: lgpEventConditionEntryAdded.setStatus('current')
if mibBuilder.loadTexts: lgpEventConditionEntryAdded.setDescription('This notification is sent each time a condition is inserted into the\n        conditions table.')
lgpEventConditionEntryRemoved = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 2)).setObjects(("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionId"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionDescr"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTime"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRef"), ("LIEBERT-GP-CONDITIONS-MIB", "lgpConditionTableRowRef"))
if mibBuilder.loadTexts: lgpEventConditionEntryRemoved.setStatus('current')
if mibBuilder.loadTexts: lgpEventConditionEntryRemoved.setDescription('This notification is sent each time a condition is removed from the\n        conditions table.')
lgpEventLowBatteryWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 3)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventLowBatteryWarning.setStatus('current')
if mibBuilder.loadTexts: lgpEventLowBatteryWarning.setDescription("The battery's remaining charge is less than or equal to the agent's\n        configured low threshold 'lgpPwrConfigLowBatteryWarningTime'.")
lgpEventLoadTransferedToBypass = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 4)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventLoadTransferedToBypass.setStatus('current')
if mibBuilder.loadTexts: lgpEventLoadTransferedToBypass.setDescription('The device has transferred the load to the bypass source.')
lgpEventInternalFault = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 5)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventInternalFault.setStatus('current')
if mibBuilder.loadTexts: lgpEventInternalFault.setDescription('The device has reported an internal fault.')
lgpEventBatteryTestFailed = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 6)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventBatteryTestFailed.setStatus('current')
if mibBuilder.loadTexts: lgpEventBatteryTestFailed.setDescription('The device has reported a battery self-test failure.')
lgpEventOutputOverload = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 7)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventOutputOverload.setStatus('current')
if mibBuilder.loadTexts: lgpEventOutputOverload.setDescription('The device has reported an output overload condition.')
lgpEventEstablishedPowerRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 8)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventEstablishedPowerRedundancy.setStatus('current')
if mibBuilder.loadTexts: lgpEventEstablishedPowerRedundancy.setDescription('The device has transitioned to the user defined redundant state.')
lgpEventLostPowerRedundancy = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 9)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventLostPowerRedundancy.setStatus('current')
if mibBuilder.loadTexts: lgpEventLostPowerRedundancy.setDescription('The device as transitioned to a non-redundant power state as defined\n        by the user configured threshold.')
lgpEventPowerModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 10)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventPowerModuleFailure.setStatus('current')
if mibBuilder.loadTexts: lgpEventPowerModuleFailure.setDescription('Device power module failure.')
lgpEventBatteryModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 11)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventBatteryModuleFailure.setStatus('current')
if mibBuilder.loadTexts: lgpEventBatteryModuleFailure.setDescription('Device battery module failure.')
lgpEventControlModuleFailure = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 12)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventControlModuleFailure.setStatus('current')
if mibBuilder.loadTexts: lgpEventControlModuleFailure.setDescription('Device control module failure.')
lgpEventPowerModuleWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 13)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventPowerModuleWarning.setStatus('current')
if mibBuilder.loadTexts: lgpEventPowerModuleWarning.setDescription('Device power module warning.')
lgpEventBatteryModuleWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 14)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventBatteryModuleWarning.setStatus('current')
if mibBuilder.loadTexts: lgpEventBatteryModuleWarning.setDescription('Device battery module warning.')
lgpEventControlModuleWarning = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 15)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventControlModuleWarning.setStatus('current')
if mibBuilder.loadTexts: lgpEventControlModuleWarning.setDescription('Device control module warning.')
lgpEventAgentFirmwareUpdateSuccessful = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 16)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventAgentFirmwareUpdateSuccessful.setStatus('deprecated')
if mibBuilder.loadTexts: lgpEventAgentFirmwareUpdateSuccessful.setDescription('The firmware update to the agent card has completed successfully.\n\n        This element has been relocated to lgpAgentFirmwareUpdateSuccessful\n        in the LIEBERT-GP-AGENT-MIB document.')
lgpEventAgentFirmwareCorrupt = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 17)).setObjects(("SNMPv2-MIB", "sysUpTime"))
if mibBuilder.loadTexts: lgpEventAgentFirmwareCorrupt.setStatus('deprecated')
if mibBuilder.loadTexts: lgpEventAgentFirmwareCorrupt.setDescription('The firmware update to the agent card has failed and the firmware is\n        now corrupt.\n\n        This element has been relocated to lgpAgentFirmwareCorrupt\n        in the LIEBERT-GP-AGENT-MIB document.')
lgpEventConfigModified = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 18)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventConfigModified.setStatus('current')
if mibBuilder.loadTexts: lgpEventConfigModified.setDescription('Configuration for the referenced PDU has been modified.')
lgpEventModuleAdded = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 19)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventModuleAdded.setStatus('current')
if mibBuilder.loadTexts: lgpEventModuleAdded.setDescription('A hot-swappable module has been added to the object specified by the \n         lgpEventParmTableRef and lgpEventParmTableRowRef.')
lgpEventModuleRemoved = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 20)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventModuleRemoved.setStatus('current')
if mibBuilder.loadTexts: lgpEventModuleRemoved.setDescription('A hot-swappable module has been removed from the object specified by \n         the lgpEventParmTableRef and lgpEventParmTableRowRef.')
lgpEventRcpPowerStateChangeOn = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 21)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpPowerStateChangeOn.setStatus('current')
if mibBuilder.loadTexts: lgpEventRcpPowerStateChangeOn.setDescription("Receptacle's power state has been changed from OFF to ON.")
lgpEventRcpPowerStateChangeOff = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 22)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpPowerStateChangeOff.setStatus('current')
if mibBuilder.loadTexts: lgpEventRcpPowerStateChangeOff.setDescription("Receptacle's power state has been changed from ON to OFF.")
lgpEventRcpLoadAdded = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 23)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpLoadAdded.setStatus('current')
if mibBuilder.loadTexts: lgpEventRcpLoadAdded.setDescription("The receptacle's load started drawing power. This notification \n        is asserted when the receptacle power is ON and the associated load \n        was previously not drawing power but is now drawing power. \n        This event is not asserted as a result of turning the \n        receptacle power ON.")
lgpEventRcpLoadRemoved = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 3, 0, 24)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRef"), ("LIEBERT-GP-NOTIFICATIONS-MIB", "lgpEventParmTableRowRef"))
if mibBuilder.loadTexts: lgpEventRcpLoadRemoved.setStatus('current')
if mibBuilder.loadTexts: lgpEventRcpLoadRemoved.setDescription("The receptacle's load stopped drawing power. This notification \n        is asserted when the receptacle power is ON and the associated load \n        was previously drawing power but is now no longer drawing power. \n        This event is not asserted as a result of turning the \n        receptacle power OFF.")
mibBuilder.exportSymbols("LIEBERT-GP-NOTIFICATIONS-MIB", lgpEventParmTableRowRef=lgpEventParmTableRowRef, lgpEventControlModuleFailure=lgpEventControlModuleFailure, lgpEventAgentFirmwareUpdateSuccessful=lgpEventAgentFirmwareUpdateSuccessful, lgpEventRcpPowerStateChangeOff=lgpEventRcpPowerStateChangeOff, lgpEventPowerModuleFailure=lgpEventPowerModuleFailure, lgpEventConditionEntryRemoved=lgpEventConditionEntryRemoved, lgpEventLowBatteryWarning=lgpEventLowBatteryWarning, lgpEventBatteryModuleWarning=lgpEventBatteryModuleWarning, PYSNMP_MODULE_ID=liebertGlobalProductsNotificationsModule, lgpEventRcpPowerStateChangeOn=lgpEventRcpPowerStateChangeOn, lgpEventOutputOverload=lgpEventOutputOverload, lgpEventConfigModified=lgpEventConfigModified, lgpEventLoadTransferedToBypass=lgpEventLoadTransferedToBypass, lgpEventEstablishedPowerRedundancy=lgpEventEstablishedPowerRedundancy, lgpEventLostPowerRedundancy=lgpEventLostPowerRedundancy, liebertGlobalProductsNotificationsModule=liebertGlobalProductsNotificationsModule, lgpEventBatteryTestFailed=lgpEventBatteryTestFailed, lgpEventBatteryModuleFailure=lgpEventBatteryModuleFailure, lgpEventRcpLoadRemoved=lgpEventRcpLoadRemoved, lgpEventParameters=lgpEventParameters, lgpEventInternalFault=lgpEventInternalFault, lgpEventRcpLoadAdded=lgpEventRcpLoadAdded, lgpEventPowerModuleWarning=lgpEventPowerModuleWarning, lgpEventConditionEntryAdded=lgpEventConditionEntryAdded, lgpEventAgentFirmwareCorrupt=lgpEventAgentFirmwareCorrupt, lgpEventNotifications=lgpEventNotifications, lgpEventModuleRemoved=lgpEventModuleRemoved, lgpEventParmTableRef=lgpEventParmTableRef, lgpEventModuleAdded=lgpEventModuleAdded, lgpEventControlModuleWarning=lgpEventControlModuleWarning)
