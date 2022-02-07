#
# PySNMP MIB module COLUBRIS-MAINTENANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-MAINTENANCE-MIB.my
# Produced by pysmi-1.1.8 at Mon Feb  7 16:13:23 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
systemFirmwareRevision, systemConfigurationVersion = mibBuilder.importSymbols("COLUBRIS-SYSTEM-MIB", "systemFirmwareRevision", "systemConfigurationVersion")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ModuleIdentity, Counter64, NotificationType, ObjectIdentity, iso, Unsigned32, Bits, Gauge32, IpAddress, TimeTicks, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Counter64", "NotificationType", "ObjectIdentity", "iso", "Unsigned32", "Bits", "Gauge32", "IpAddress", "TimeTicks", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
colubrisMaintenanceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 2))
if mibBuilder.loadTexts: colubrisMaintenanceMIB.setLastUpdated('200501170000Z')
if mibBuilder.loadTexts: colubrisMaintenanceMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisMaintenanceMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisMaintenanceMIB.setDescription('Colubris Networks Maintenance MIB.')
colubrisMaintenanceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1))
firmwareUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1))
configurationUpdate = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2))
certificate = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3))
firmwarePeriodicUpdate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwarePeriodicUpdate.setStatus('current')
if mibBuilder.loadTexts: firmwarePeriodicUpdate.setDescription("Specifies if firmware updates are automatically triggered \n                 on a periodic basis or not.\n                   'true': Automatically update the firmware based on\n                           the information specified in the\n                           firmwareUpdateDay and firmwareUpdateTime\n                           attributes. \n                   'false': No firmware update is triggered unless a request \n                            is specifically issude using the\n                            firmwareUpdateInitiate attribute.")
firmwareUpdateDay = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7), ("everyday", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateDay.setStatus('current')
if mibBuilder.loadTexts: firmwareUpdateDay.setDescription('When firmwarePeriodicUpdate is set to true, this attribute\n                 specifies the day that automatic updates will occur.')
firmwareUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateTime.setStatus('current')
if mibBuilder.loadTexts: firmwareUpdateTime.setDescription("When firmwarePeriodicUpdate is set to true, this attribute \n                 specifies the time of the day for an automatic firmware update.\n                 Specify the time in hours (00-23) and minutes (00-59) in the\n                 format HH:MM. The ':' character is mandatory between the fields.")
firmwareUpdateLocation = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateLocation.setStatus('current')
if mibBuilder.loadTexts: firmwareUpdateLocation.setDescription('Specifies the URL where the new firmware file is located. This is\n                 used when the firmware update is triggered manually or automatically\n                 on a periodic basis.')
firmwareUpdateInitiate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("update", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateInitiate.setStatus('current')
if mibBuilder.loadTexts: firmwareUpdateInitiate.setDescription("Triggers a firmware update using the firmware specified in the\n                 firmwareUpdateLocation attribute. Reading this attribute always\n                 returns 'idle'.")
firmwareUpdateNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 6), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: firmwareUpdateNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: firmwareUpdateNotificationEnabled.setDescription('Specifies if firmwareUpdateNotification notifications are\n                 generated.')
firmwareUpdateInfo = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 1, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: firmwareUpdateInfo.setStatus('current')
if mibBuilder.loadTexts: firmwareUpdateInfo.setDescription('Contains various information about the firmware update and is\n                 used with firmware update notifications to provide more \n                 detailed information.')
configurationPeriodicUpdate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationPeriodicUpdate.setStatus('current')
if mibBuilder.loadTexts: configurationPeriodicUpdate.setDescription("Specifies if configuration file updates are automatically triggered \n                 on a periodic basis or not.\n\n                   'true': Automatically update the configuration file based on\n                           the information specified in the\n                           configurationUpdateDay and configurationUpdateTime \n                           attributes. \n\n                   'false': No configuration file update is triggered unless a request \n                            is specifically issude using the\n                            configurationUpdateInitiate attribute.")
configurationUpdateDay = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("monday", 1), ("tuesday", 2), ("wednesday", 3), ("thursday", 4), ("friday", 5), ("saturday", 6), ("sunday", 7), ("everyday", 8)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateDay.setStatus('current')
if mibBuilder.loadTexts: configurationUpdateDay.setDescription('When configurationPeriodicUpdate is set to true, this attribute\n                 specifies the day that automatic updates will occur.')
configurationUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateTime.setStatus('current')
if mibBuilder.loadTexts: configurationUpdateTime.setDescription("When configurationPeriodicUpdateis set to true, this attribute \n                 specifies the time of the day for an automatic configuration file update.\n                 Specify the time in hours (00-23) and minutes (00-59) in the\n                 format HH:MM. The ':' character is mandatory between the fields.")
configurationUpdateLocation = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateLocation.setStatus('current')
if mibBuilder.loadTexts: configurationUpdateLocation.setDescription('Specifies the URL where the new configuration file is located. This is\n                 used when the update is triggered manually or automatically\n                 on a periodic basis.')
configurationUpdateInitiate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("update", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateInitiate.setStatus('current')
if mibBuilder.loadTexts: configurationUpdateInitiate.setDescription("Triggers a configuration file update using the configuration file\n                 specified in the configurationUpdateLocation attribute. Reading this \n                 attribute always returns 'idle'.")
configurationUpdateOperation = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("backup", 1), ("restore", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateOperation.setStatus('current')
if mibBuilder.loadTexts: configurationUpdateOperation.setDescription("Specifies the operation that is performed on the\n                 configuration file.\n\n                    'backup':  Saves the current device configuration into the file\n                               specified in the configurationUpdateLocation attribute.\n\n                    'restore':  Loads the file specified in the\n                                configurationUpdateLocation attribute into the device.")
configurationUpdateNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 7), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationUpdateNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: configurationUpdateNotificationEnabled.setDescription('Specifies if configurationUpdateNotification notifications are generated.')
configurationLocalUpdateNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 8), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationLocalUpdateNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: configurationLocalUpdateNotificationEnabled.setDescription('Specifies if configurationLocalUpdateNotification notifications\n                 are generated.')
configurationUpdateInfo = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: configurationUpdateInfo.setStatus('current')
if mibBuilder.loadTexts: configurationUpdateInfo.setDescription('Contains various information about the configuration update and is\n                 used with configuration update notifications to provide more \n                 detailed information.')
configurationFactoryDefaults = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("resetToFactoryDefaults", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationFactoryDefaults.setStatus('current')
if mibBuilder.loadTexts: configurationFactoryDefaults.setDescription("Resets the device configuration to Factory Default. \n                 Important: This will reset the community names and shut down all\n                 connections. Reading this object will always return 'idle'.")
configurationRestart = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 2, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("idle", 0), ("restart", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configurationRestart.setStatus('current')
if mibBuilder.loadTexts: configurationRestart.setDescription("Restarts the device.\n                 Important: This will shut down all connections. Reading this object\n\t\t     will always return 'idle'.")
certificateAboutToExpireNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 1), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: certificateAboutToExpireNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: certificateAboutToExpireNotificationEnabled.setDescription('Specifies if certificateAboutToExpireNotification notifications\n                 are generated.')
certificateExpiredNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: certificateExpiredNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: certificateExpiredNotificationEnabled.setDescription('Specifies if certificateExpiredNotification notifications are generated.')
certificateExpiryDate = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 2, 1, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: certificateExpiryDate.setStatus('current')
if mibBuilder.loadTexts: certificateExpiryDate.setDescription('Indicates the current expiry date of the certificate.')
colubrisMaintenanceMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2))
colubrisMaintenanceMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0))
firmwareUpdateNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 5)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInfo"), ("COLUBRIS-SYSTEM-MIB", "systemFirmwareRevision"))
if mibBuilder.loadTexts: firmwareUpdateNotification.setStatus('current')
if mibBuilder.loadTexts: firmwareUpdateNotification.setDescription('Sent when a firmware update was attempted from a remote\n                 server.')
configurationUpdateNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 1)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"), ("COLUBRIS-SYSTEM-MIB", "systemConfigurationVersion"))
if mibBuilder.loadTexts: configurationUpdateNotification.setStatus('current')
if mibBuilder.loadTexts: configurationUpdateNotification.setDescription('Sent when a configuration update was attempted from a remote\n                 server.')
configurationLocalUpdateNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 2)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"))
if mibBuilder.loadTexts: configurationLocalUpdateNotification.setStatus('current')
if mibBuilder.loadTexts: configurationLocalUpdateNotification.setDescription('Sent whenever the configuration changes.')
certificateAboutToExpireNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 3)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate"))
if mibBuilder.loadTexts: certificateAboutToExpireNotification.setStatus('current')
if mibBuilder.loadTexts: certificateAboutToExpireNotification.setDescription('Sent when a certificate is about to expire.')
certificateExpiredNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 2, 2, 0, 4)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate"))
if mibBuilder.loadTexts: certificateExpiredNotification.setStatus('current')
if mibBuilder.loadTexts: certificateExpiredNotification.setDescription('Sent when a certificate has expired.')
colubrisMaintenanceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3))
colubrisMaintenanceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 1))
colubrisMaintenanceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2))
colubrisMaintenanceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 1, 1)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "colubrisMaintenanceMIBGroup"), ("COLUBRIS-MAINTENANCE-MIB", "colubrisMaintenanceNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisMaintenanceMIBCompliance = colubrisMaintenanceMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisMaintenanceMIBCompliance.setDescription('The compliance statement for entities which implement\n                the Colubris Maintenance MIB.')
colubrisMaintenanceMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2, 1)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "firmwarePeriodicUpdate"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateDay"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateTime"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateLocation"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInitiate"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateInfo"), ("COLUBRIS-MAINTENANCE-MIB", "configurationPeriodicUpdate"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateDay"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateTime"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateLocation"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInitiate"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateOperation"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateInfo"), ("COLUBRIS-MAINTENANCE-MIB", "configurationFactoryDefaults"), ("COLUBRIS-MAINTENANCE-MIB", "configurationRestart"), ("COLUBRIS-MAINTENANCE-MIB", "configurationLocalUpdateNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "certificateAboutToExpireNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiredNotificationEnabled"), ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiryDate"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisMaintenanceMIBGroup = colubrisMaintenanceMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisMaintenanceMIBGroup.setDescription('A collection of objects providing the Maintenance MIB\n                 capability.')
colubrisMaintenanceNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 2, 3, 2, 2)).setObjects(("COLUBRIS-MAINTENANCE-MIB", "firmwareUpdateNotification"), ("COLUBRIS-MAINTENANCE-MIB", "configurationUpdateNotification"), ("COLUBRIS-MAINTENANCE-MIB", "configurationLocalUpdateNotification"), ("COLUBRIS-MAINTENANCE-MIB", "certificateAboutToExpireNotification"), ("COLUBRIS-MAINTENANCE-MIB", "certificateExpiredNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisMaintenanceNotificationGroup = colubrisMaintenanceNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisMaintenanceNotificationGroup.setDescription('A collection of supported notifications')
mibBuilder.exportSymbols("COLUBRIS-MAINTENANCE-MIB", firmwareUpdateInfo=firmwareUpdateInfo, colubrisMaintenanceNotificationGroup=colubrisMaintenanceNotificationGroup, PYSNMP_MODULE_ID=colubrisMaintenanceMIB, configurationUpdateLocation=configurationUpdateLocation, certificateAboutToExpireNotification=certificateAboutToExpireNotification, configurationPeriodicUpdate=configurationPeriodicUpdate, firmwareUpdateNotificationEnabled=firmwareUpdateNotificationEnabled, configurationRestart=configurationRestart, colubrisMaintenanceMIBNotifications=colubrisMaintenanceMIBNotifications, configurationUpdateNotification=configurationUpdateNotification, firmwarePeriodicUpdate=firmwarePeriodicUpdate, colubrisMaintenanceMIBNotificationPrefix=colubrisMaintenanceMIBNotificationPrefix, colubrisMaintenanceMIBCompliance=colubrisMaintenanceMIBCompliance, certificate=certificate, firmwareUpdateDay=firmwareUpdateDay, firmwareUpdateTime=firmwareUpdateTime, colubrisMaintenanceMIBCompliances=colubrisMaintenanceMIBCompliances, colubrisMaintenanceMIB=colubrisMaintenanceMIB, configurationFactoryDefaults=configurationFactoryDefaults, configurationUpdateInfo=configurationUpdateInfo, configurationUpdateNotificationEnabled=configurationUpdateNotificationEnabled, firmwareUpdateInitiate=firmwareUpdateInitiate, configurationLocalUpdateNotification=configurationLocalUpdateNotification, configurationUpdateTime=configurationUpdateTime, colubrisMaintenanceMIBObjects=colubrisMaintenanceMIBObjects, certificateExpiredNotificationEnabled=certificateExpiredNotificationEnabled, certificateExpiredNotification=certificateExpiredNotification, configurationUpdate=configurationUpdate, configurationLocalUpdateNotificationEnabled=configurationLocalUpdateNotificationEnabled, firmwareUpdateNotification=firmwareUpdateNotification, colubrisMaintenanceMIBGroup=colubrisMaintenanceMIBGroup, firmwareUpdate=firmwareUpdate, certificateExpiryDate=certificateExpiryDate, colubrisMaintenanceMIBConformance=colubrisMaintenanceMIBConformance, firmwareUpdateLocation=firmwareUpdateLocation, certificateAboutToExpireNotificationEnabled=certificateAboutToExpireNotificationEnabled, configurationUpdateInitiate=configurationUpdateInitiate, configurationUpdateOperation=configurationUpdateOperation, configurationUpdateDay=configurationUpdateDay, colubrisMaintenanceMIBGroups=colubrisMaintenanceMIBGroups)
