#
# PySNMP MIB module COLUBRIS-MAINTENANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-MAINTENANCE-MIB.my
# Produced by pysmi-1.1.8 at Sun Jan 16 00:37:53 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
systemFirmwareRevision, systemConfigurationVersion = mibBuilder.importSymbols("COLUBRIS-SYSTEM-MIB", "systemFirmwareRevision", "systemConfigurationVersion")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, TimeTicks, NotificationType, Unsigned32, Counter64, iso, Integer32, IpAddress, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "TimeTicks", "NotificationType", "Unsigned32", "Counter64", "iso", "Integer32", "IpAddress", "Counter32")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
colubrisMaintenanceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 2))
if mibBuilder.loadTexts: colubrisMaintenanceMIB.setLastUpdated('200501170000Z')
if mibBuilder.loadTexts: colubrisMaintenanceMIB.setOrganization('Colubris Networks, Inc.')
colubrisMaintenanceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1))
firmwareUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1))
configurationUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2))
certificate = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3))
firmwarePeriodicUpdate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwarePeriodicUpdate.setStatus('current')
firmwareUpdateDay = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7), ("everyday", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateDay.setStatus('current')
firmwareUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateTime.setStatus('current')
firmwareUpdateLocation = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateLocation.setStatus('current')
firmwareUpdateInitiate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("update", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateInitiate.setStatus('current')
firmwareUpdateNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 6), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateNotificationEnabled.setStatus('current')
firmwareUpdateInfo = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: firmwareUpdateInfo.setStatus('current')
configurationPeriodicUpdate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationPeriodicUpdate.setStatus('current')
configurationUpdateDay = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7), ("everyday", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateDay.setStatus('current')
configurationUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateTime.setStatus('current')
configurationUpdateLocation = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateLocation.setStatus('current')
configurationUpdateInitiate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("update", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateInitiate.setStatus('current')
configurationUpdateOperation = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backup", 1), ("restore", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateOperation.setStatus('current')
configurationUpdateNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 7), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateNotificationEnabled.setStatus('current')
configurationLocalUpdateNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 8), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationLocalUpdateNotificationEnabled.setStatus('current')
configurationUpdateInfo = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: configurationUpdateInfo.setStatus('current')
configurationFactoryDefaults = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("resetToFactoryDefaults", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationFactoryDefaults.setStatus('current')
configurationRestart = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("restart", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationRestart.setStatus('current')
certificateAboutToExpireNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 1), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: certificateAboutToExpireNotificationEnabled.setStatus('current')
certificateExpiredNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: certificateExpiredNotificationEnabled.setStatus('current')
certificateExpiryDate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: certificateExpiryDate.setStatus('current')
colubrisMaintenanceMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2))
colubrisMaintenanceMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0))
firmwareUpdateNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 5)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInfo"), ("COLUBRIS-SYSTEM-MIB", "systemFirmwareRevision"))
if mibBuilder.loadTexts: firmwareUpdateNotification.setStatus('current')
configurationUpdateNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 1)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"), ("COLUBRIS-SYSTEM-MIB", "systemConfigurationVersion"))
if mibBuilder.loadTexts: configurationUpdateNotification.setStatus('current')
configurationLocalUpdateNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 2)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"))
if mibBuilder.loadTexts: configurationLocalUpdateNotification.setStatus('current')
certificateAboutToExpireNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 3)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate"))
if mibBuilder.loadTexts: certificateAboutToExpireNotification.setStatus('current')
certificateExpiredNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 4)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate"))
if mibBuilder.loadTexts: certificateExpiredNotification.setStatus('current')
colubrisMaintenanceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3))
colubrisMaintenanceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 1))
colubrisMaintenanceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2))
colubrisMaintenanceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 1, 1)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "colubrisMaintenanceMIBGroup"), ("COLUBRIS-MAINTENANCE-MIB", "colubrisMaintenanceNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisMaintenanceMIBCompliance = colubrisMaintenanceMIBCompliance.setStatus('current')
colubrisMaintenanceMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2, 1)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "firmwarePeriodicUpdate"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateDay"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateTime"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateLocation"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInitiate"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInfo"), ("COLUBRIS-MAINTENANCE-MIB", "configurationPeriodicUpdate"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateDay"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateTime"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateLocation"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInitiate"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateOperation"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"), ("COLUBRIS-MAINTENANCE-MIB", "configurationFactoryDefaults"), ("COLUBRIS-MAINTENANCE-MIB", "configurationRestart"), ("COLUBRIS-MAINTENANCE-MIB", "configurationLocalUpdateNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "certificateAboutToExpireNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiredNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisMaintenanceMIBGroup = colubrisMaintenanceMIBGroup.setStatus('current')
colubrisMaintenanceNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2, 2)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateNotification"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateNotification"), ("COLUBRIS-MAINTENANCE-MIB", "configurationLocalUpdateNotification"), ("COLUBRIS-MAINTENANCE-MIB", "certificateAboutToExpireNotification"), ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiredNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisMaintenanceNotificationGroup = colubrisMaintenanceNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-MAINTENANCE-MIB", configurationPeriodicUpdate=configurationPeriodicUpdate, configurationUpdateInfo=configurationUpdateInfo, certificateExpiryDate=certificateExpiryDate, configurationUpdateNotificationEnabled=configurationUpdateNotificationEnabled, colubrisMaintenanceMIBCompliances=colubrisMaintenanceMIBCompliances, configurationUpdateOperation=configurationUpdateOperation, firmwareUpdateNotificationEnabled=firmwareUpdateNotificationEnabled, configurationLocalUpdateNotification=configurationLocalUpdateNotification, certificateAboutToExpireNotification=certificateAboutToExpireNotification, configurationUpdateLocation=configurationUpdateLocation, certificateAboutToExpireNotificationEnabled=certificateAboutToExpireNotificationEnabled, certificateExpiredNotificationEnabled=certificateExpiredNotificationEnabled, firmwareUpdateInfo=firmwareUpdateInfo, colubrisMaintenanceMIBNotifications=colubrisMaintenanceMIBNotifications, PYSNMP_MODULE_ID=colubrisMaintenanceMIB, configurationUpdate=configurationUpdate, configurationFactoryDefaults=configurationFactoryDefaults, colubrisMaintenanceMIBGroup=colubrisMaintenanceMIBGroup, firmwarePeriodicUpdate=firmwarePeriodicUpdate, colubrisMaintenanceMIBObjects=colubrisMaintenanceMIBObjects, configurationLocalUpdateNotificationEnabled=configurationLocalUpdateNotificationEnabled, configurationRestart=configurationRestart, colubrisMaintenanceMIBNotificationPrefix=colubrisMaintenanceMIBNotificationPrefix, colubrisMaintenanceMIBCompliance=colubrisMaintenanceMIBCompliance, firmwareUpdateTime=firmwareUpdateTime, firmwareUpdateInitiate=firmwareUpdateInitiate, colubrisMaintenanceMIBConformance=colubrisMaintenanceMIBConformance, firmwareUpdateDay=firmwareUpdateDay, configurationUpdateInitiate=configurationUpdateInitiate, certificate=certificate, firmwareUpdate=firmwareUpdate, configurationUpdateDay=configurationUpdateDay, firmwareUpdateNotification=firmwareUpdateNotification, colubrisMaintenanceMIBGroups=colubrisMaintenanceMIBGroups, configurationUpdateNotification=configurationUpdateNotification, firmwareUpdateLocation=firmwareUpdateLocation, colubrisMaintenanceMIB=colubrisMaintenanceMIB, certificateExpiredNotification=certificateExpiredNotification, configurationUpdateTime=configurationUpdateTime, colubrisMaintenanceNotificationGroup=colubrisMaintenanceNotificationGroup)
