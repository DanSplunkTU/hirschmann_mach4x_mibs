#
# PySNMP MIB module COLUBRIS-DEVICE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-DEVICE-MIB.my
# Produced by pysmi-1.1.3 at Sun Nov 28 20:18:39 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisNotificationEnable, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisNotificationEnable")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Counter64, IpAddress, Gauge32, Unsigned32, TimeTicks, Bits, ModuleIdentity, NotificationType, Integer32, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "IpAddress", "Gauge32", "Unsigned32", "TimeTicks", "Bits", "ModuleIdentity", "NotificationType", "Integer32", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
colubrisDeviceMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 23))
if mibBuilder.loadTexts: colubrisDeviceMIB.setLastUpdated('200609050000Z')
if mibBuilder.loadTexts: colubrisDeviceMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisDeviceMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisDeviceMIB.setDescription('Colubris Device MIB.')
colubrisDeviceMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1))
coDeviceConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1))
coDeviceDiscoveryGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2))
coDeviceInformationGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3))
coDeviceStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4))
coDeviceStateChangeNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 1), ColubrisNotificationEnable().clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDeviceStateChangeNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDeviceStateChangeNotificationEnabled.setDescription('Specifies if the coDeviceStateChangeNotification notification\n                 is generated.')
coDeviceAuthorizationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 2), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDeviceAuthorizationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDeviceAuthorizationFailureNotificationEnabled.setDescription('Specifies if the coDeviceAuthorizationFailureNotification\n                 notification is generated.')
coDeviceSecurityFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 3), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDeviceSecurityFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDeviceSecurityFailureNotificationEnabled.setDescription('Specifies if the coDeviceSecurityFailureNotification\n                 notification is generated.')
coDeviceFirmwareFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 4), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDeviceFirmwareFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDeviceFirmwareFailureNotificationEnabled.setDescription('Specifies if the coDeviceFirmwareFailureNotification\n                 notification is generated.')
coDeviceConfigurationFailureNotificationEnabled = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 1, 5), ColubrisNotificationEnable().clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: coDeviceConfigurationFailureNotificationEnabled.setStatus('current')
if mibBuilder.loadTexts: coDeviceConfigurationFailureNotificationEnabled.setDescription('Specifies if the coDeviceConfigurationFailureNotification\n                 notification is generated.')
coDeviceDiscoveryTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceDiscoveryTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceDiscoveryTable.setDescription('Device discovery attributes.')
coDeviceDiscoveryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"))
if mibBuilder.loadTexts: coDeviceDiscoveryEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceDiscoveryEntry.setDescription('An entry in the coDeviceDiscoveryTable.\n                 coDevDisIndex - Uniquely identifies a device on the\n                                 MultiService Controller.')
coDevDisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevDisIndex.setStatus('current')
if mibBuilder.loadTexts: coDevDisIndex.setDescription('Specifies the index of the device.')
coDevDisSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisSerialNumber.setStatus('current')
if mibBuilder.loadTexts: coDevDisSerialNumber.setDescription('Device serial number.')
coDevDisMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisMacAddress.setStatus('current')
if mibBuilder.loadTexts: coDevDisMacAddress.setDescription('Ethernet MAC address of the device.')
coDevDisIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisIpAddress.setStatus('current')
if mibBuilder.loadTexts: coDevDisIpAddress.setDescription('IP address of the device.')
coDevDisState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("disconnected", 1), ("authorized", 2), ("join", 3), ("firmware", 4), ("security", 5), ("configuration", 6), ("running", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisState.setStatus('current')
if mibBuilder.loadTexts: coDevDisState.setDescription('Device operational state.')
coDevDisSystemName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisSystemName.setStatus('current')
if mibBuilder.loadTexts: coDevDisSystemName.setDescription('Name assigned to the device by the configuration tool.')
coDevDisLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisLocation.setStatus('current')
if mibBuilder.loadTexts: coDevDisLocation.setDescription('Location assigned to the device by the configuration tool.')
coDevDisContact = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisContact.setStatus('current')
if mibBuilder.loadTexts: coDevDisContact.setDescription('Contact assigned to the device by the configuration tool.')
coDevDisGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisGroupName.setStatus('current')
if mibBuilder.loadTexts: coDevDisGroupName.setDescription('Identifies the group that the device belongs to.')
coDevDisConnectionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 2, 1, 1, 10), Counter32()).setUnits('minutes').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevDisConnectionTime.setStatus('current')
if mibBuilder.loadTexts: coDevDisConnectionTime.setDescription('Elapsed time in minutes since the device was last authorized.')
coDeviceInfoTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1), )
if mibBuilder.loadTexts: coDeviceInfoTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceInfoTable.setDescription('Device information attributes.')
coDeviceInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1), )
coDeviceDiscoveryEntry.registerAugmentions(("COLUBRIS-DEVICE-MIB", "coDeviceInfoEntry"))
coDeviceInfoEntry.setIndexNames(*coDeviceDiscoveryEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceInfoEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceInfoEntry.setDescription('An entry in the coDeviceInfoTable.\n                 coDevDisIndex - Uniquely identifies a device on the\n                                 MultiService Controller.')
coDevInfoProductType = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevInfoProductType.setStatus('current')
if mibBuilder.loadTexts: coDevInfoProductType.setDescription('Refer to a Colubris product inside colubrisProductsMIB.')
coDevInfoProductName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevInfoProductName.setStatus('current')
if mibBuilder.loadTexts: coDevInfoProductName.setDescription('Colubris Networks product name for the device.')
coDevInfoFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevInfoFirmwareRevision.setStatus('current')
if mibBuilder.loadTexts: coDevInfoFirmwareRevision.setDescription('Revision number of the device firmware.')
coDevInfoBootRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevInfoBootRevision.setStatus('current')
if mibBuilder.loadTexts: coDevInfoBootRevision.setDescription('Revision number of the device boot loader.')
coDevInfoHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 3, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevInfoHardwareRevision.setStatus('current')
if mibBuilder.loadTexts: coDevInfoHardwareRevision.setDescription('Revision number of the system hardware.')
coDeviceStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1), )
if mibBuilder.loadTexts: coDeviceStatusTable.setStatus('current')
if mibBuilder.loadTexts: coDeviceStatusTable.setDescription('Device status attributes.')
coDeviceStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1), )
coDeviceDiscoveryEntry.registerAugmentions(("COLUBRIS-DEVICE-MIB", "coDeviceStatusEntry"))
coDeviceStatusEntry.setIndexNames(*coDeviceDiscoveryEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceStatusEntry.setStatus('current')
if mibBuilder.loadTexts: coDeviceStatusEntry.setDescription('An entry in the coDeviceStatusTable.\n                 coDevDisIndex - Uniquely identifies a device on the\n                                 MultiService Controller.')
coDevStUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 1), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStUpTime.setStatus('current')
if mibBuilder.loadTexts: coDevStUpTime.setDescription('Time elapsed after the device powered up.')
coDevStLoadAverage1Min = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStLoadAverage1Min.setStatus('current')
if mibBuilder.loadTexts: coDevStLoadAverage1Min.setDescription('Average number of processes running during the last minute.')
coDevStLoadAverage5Min = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStLoadAverage5Min.setStatus('current')
if mibBuilder.loadTexts: coDevStLoadAverage5Min.setDescription('Average number of processes running during the last 5 minutes.')
coDevStLoadAverage15Min = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStLoadAverage15Min.setStatus('current')
if mibBuilder.loadTexts: coDevStLoadAverage15Min.setDescription('Average number of processes running during the last 15 minutes.')
coDevStCpuUseNow = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 5), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStCpuUseNow.setStatus('current')
if mibBuilder.loadTexts: coDevStCpuUseNow.setDescription('Current CPU usage.')
coDevStCpuUse5Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 6), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStCpuUse5Sec.setStatus('current')
if mibBuilder.loadTexts: coDevStCpuUse5Sec.setDescription('Average CPU usage during the last 5 seconds.')
coDevStCpuUse10Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 7), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStCpuUse10Sec.setStatus('current')
if mibBuilder.loadTexts: coDevStCpuUse10Sec.setDescription('Average CPU usage during the last 10 seconds.')
coDevStCpuUse20Sec = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 8), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStCpuUse20Sec.setStatus('current')
if mibBuilder.loadTexts: coDevStCpuUse20Sec.setDescription('Average CPU usage during the last 20 seconds.')
coDevStRamTotal = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 9), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStRamTotal.setStatus('current')
if mibBuilder.loadTexts: coDevStRamTotal.setDescription('Total system RAM.')
coDevStRamFree = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 10), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStRamFree.setStatus('current')
if mibBuilder.loadTexts: coDevStRamFree.setDescription('Available system RAM.')
coDevStRamBuffer = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 11), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStRamBuffer.setStatus('current')
if mibBuilder.loadTexts: coDevStRamBuffer.setDescription('Memory used by the buffers.')
coDevStRamCached = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 12), Unsigned32()).setUnits('Kb').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStRamCached.setStatus('current')
if mibBuilder.loadTexts: coDevStRamCached.setDescription('Memory used by the system cache.')
coDevStStorageUsePermanent = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 13), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStStorageUsePermanent.setStatus('current')
if mibBuilder.loadTexts: coDevStStorageUsePermanent.setDescription('Percentage of the permanent storage in use.')
coDevStStorageUseTemporary = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 23, 1, 4, 1, 1, 14), Unsigned32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevStStorageUseTemporary.setStatus('current')
if mibBuilder.loadTexts: coDevStStorageUseTemporary.setDescription('Percentage of the temporary storage in use.')
colubrisDeviceMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2))
colubrisDeviceMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0))
coDeviceStateChangeNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 1)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
if mibBuilder.loadTexts: coDeviceStateChangeNotification.setStatus('current')
if mibBuilder.loadTexts: coDeviceStateChangeNotification.setDescription('A coDeviceStateChangeNotification trap signifies that the\n                 SNMP entity has detected a device state change.')
coDeviceAuthorizationFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 2)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
if mibBuilder.loadTexts: coDeviceAuthorizationFailureNotification.setStatus('current')
if mibBuilder.loadTexts: coDeviceAuthorizationFailureNotification.setDescription('A coDeviceAuthorizationFailureNotification trap\n                 signifies that the SNMP entity has detected a device\n                 authentication failure.')
coDeviceSecurityFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 3)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
if mibBuilder.loadTexts: coDeviceSecurityFailureNotification.setStatus('current')
if mibBuilder.loadTexts: coDeviceSecurityFailureNotification.setDescription('A coDeviceSecurityFailureNotification trap signifies\n                 that the SNMP entity has detected a device connection\n                 failure.')
coDeviceFirmwareFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 4)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
if mibBuilder.loadTexts: coDeviceFirmwareFailureNotification.setStatus('current')
if mibBuilder.loadTexts: coDeviceFirmwareFailureNotification.setDescription('A coDeviceFirmwareFailureNotification trap signifies\n                 that the SNMP entity has detected a device firmware\n                 failure.')
coDeviceConfigurationFailureNotification = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 23, 2, 0, 5)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"))
if mibBuilder.loadTexts: coDeviceConfigurationFailureNotification.setStatus('current')
if mibBuilder.loadTexts: coDeviceConfigurationFailureNotification.setDescription('A coDeviceConfigurationFailureNotification trap\n                 signifies that the SNMP entity has detected a device\n                 configuration failure.')
colubrisDeviceMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3))
colubrisDeviceMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 1))
colubrisDeviceMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2))
colubrisDeviceMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 1, 1)).setObjects(("COLUBRIS-DEVICE-MIB", "colubrisDeviceConfigMIBGroup"), ("COLUBRIS-DEVICE-MIB", "colubrisDeviceDiscoveryMIBGroup"), ("COLUBRIS-DEVICE-MIB", "colubrisDeviceInformationMIBGroup"), ("COLUBRIS-DEVICE-MIB", "colubrisDeviceStatusMIBGroup"), ("COLUBRIS-DEVICE-MIB", "colubrisDeviceNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceMIBCompliance = colubrisDeviceMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceMIBCompliance.setDescription('The compliance statement for the Device MIB.')
colubrisDeviceConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 1)).setObjects(("COLUBRIS-DEVICE-MIB", "coDeviceStateChangeNotificationEnabled"), ("COLUBRIS-DEVICE-MIB", "coDeviceAuthorizationFailureNotificationEnabled"), ("COLUBRIS-DEVICE-MIB", "coDeviceSecurityFailureNotificationEnabled"), ("COLUBRIS-DEVICE-MIB", "coDeviceFirmwareFailureNotificationEnabled"), ("COLUBRIS-DEVICE-MIB", "coDeviceConfigurationFailureNotificationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceConfigMIBGroup = colubrisDeviceConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceConfigMIBGroup.setDescription('A collection of configuration objects.')
colubrisDeviceDiscoveryMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 2)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevDisSerialNumber"), ("COLUBRIS-DEVICE-MIB", "coDevDisMacAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisIpAddress"), ("COLUBRIS-DEVICE-MIB", "coDevDisState"), ("COLUBRIS-DEVICE-MIB", "coDevDisSystemName"), ("COLUBRIS-DEVICE-MIB", "coDevDisLocation"), ("COLUBRIS-DEVICE-MIB", "coDevDisContact"), ("COLUBRIS-DEVICE-MIB", "coDevDisGroupName"), ("COLUBRIS-DEVICE-MIB", "coDevDisConnectionTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceDiscoveryMIBGroup = colubrisDeviceDiscoveryMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceDiscoveryMIBGroup.setDescription('A collection of objects for Device\n                 discovery status.')
colubrisDeviceInformationMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 3)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevInfoProductType"), ("COLUBRIS-DEVICE-MIB", "coDevInfoProductName"), ("COLUBRIS-DEVICE-MIB", "coDevInfoFirmwareRevision"), ("COLUBRIS-DEVICE-MIB", "coDevInfoBootRevision"), ("COLUBRIS-DEVICE-MIB", "coDevInfoHardwareRevision"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceInformationMIBGroup = colubrisDeviceInformationMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceInformationMIBGroup.setDescription('A collection of objects for device\n                 configuration items.')
colubrisDeviceStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 4)).setObjects(("COLUBRIS-DEVICE-MIB", "coDevStUpTime"), ("COLUBRIS-DEVICE-MIB", "coDevStLoadAverage1Min"), ("COLUBRIS-DEVICE-MIB", "coDevStLoadAverage5Min"), ("COLUBRIS-DEVICE-MIB", "coDevStLoadAverage15Min"), ("COLUBRIS-DEVICE-MIB", "coDevStCpuUseNow"), ("COLUBRIS-DEVICE-MIB", "coDevStCpuUse5Sec"), ("COLUBRIS-DEVICE-MIB", "coDevStCpuUse10Sec"), ("COLUBRIS-DEVICE-MIB", "coDevStCpuUse20Sec"), ("COLUBRIS-DEVICE-MIB", "coDevStRamTotal"), ("COLUBRIS-DEVICE-MIB", "coDevStRamFree"), ("COLUBRIS-DEVICE-MIB", "coDevStRamBuffer"), ("COLUBRIS-DEVICE-MIB", "coDevStRamCached"), ("COLUBRIS-DEVICE-MIB", "coDevStStorageUsePermanent"), ("COLUBRIS-DEVICE-MIB", "coDevStStorageUseTemporary"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceStatusMIBGroup = colubrisDeviceStatusMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceStatusMIBGroup.setDescription('A collection of objects for device\n                 status.')
colubrisDeviceNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 23, 3, 2, 5)).setObjects(("COLUBRIS-DEVICE-MIB", "coDeviceStateChangeNotification"), ("COLUBRIS-DEVICE-MIB", "coDeviceAuthorizationFailureNotification"), ("COLUBRIS-DEVICE-MIB", "coDeviceSecurityFailureNotification"), ("COLUBRIS-DEVICE-MIB", "coDeviceFirmwareFailureNotification"), ("COLUBRIS-DEVICE-MIB", "coDeviceConfigurationFailureNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceNotificationGroup = colubrisDeviceNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisDeviceNotificationGroup.setDescription('A collection of supported device notifications.')
mibBuilder.exportSymbols("COLUBRIS-DEVICE-MIB", colubrisDeviceMIBObjects=colubrisDeviceMIBObjects, colubrisDeviceInformationMIBGroup=colubrisDeviceInformationMIBGroup, coDevStLoadAverage5Min=coDevStLoadAverage5Min, coDevStStorageUseTemporary=coDevStStorageUseTemporary, coDeviceInformationGroup=coDeviceInformationGroup, coDevDisIndex=coDevDisIndex, coDeviceStateChangeNotification=coDeviceStateChangeNotification, coDevDisMacAddress=coDevDisMacAddress, coDeviceConfigurationFailureNotification=coDeviceConfigurationFailureNotification, coDeviceInfoTable=coDeviceInfoTable, coDeviceStatusGroup=coDeviceStatusGroup, coDevDisLocation=coDevDisLocation, coDeviceFirmwareFailureNotification=coDeviceFirmwareFailureNotification, coDevStCpuUse10Sec=coDevStCpuUse10Sec, colubrisDeviceMIBGroups=colubrisDeviceMIBGroups, coDevDisGroupName=coDevDisGroupName, colubrisDeviceMIBCompliances=colubrisDeviceMIBCompliances, coDeviceStateChangeNotificationEnabled=coDeviceStateChangeNotificationEnabled, coDevInfoHardwareRevision=coDevInfoHardwareRevision, coDevInfoProductName=coDevInfoProductName, colubrisDeviceConfigMIBGroup=colubrisDeviceConfigMIBGroup, coDevDisConnectionTime=coDevDisConnectionTime, coDevStUpTime=coDevStUpTime, coDeviceConfigGroup=coDeviceConfigGroup, coDeviceDiscoveryEntry=coDeviceDiscoveryEntry, coDevInfoProductType=coDevInfoProductType, coDevStRamCached=coDevStRamCached, colubrisDeviceMIBNotifications=colubrisDeviceMIBNotifications, coDevDisSerialNumber=coDevDisSerialNumber, coDeviceStatusEntry=coDeviceStatusEntry, coDeviceAuthorizationFailureNotification=coDeviceAuthorizationFailureNotification, colubrisDeviceDiscoveryMIBGroup=colubrisDeviceDiscoveryMIBGroup, colubrisDeviceMIB=colubrisDeviceMIB, coDevDisState=coDevDisState, coDeviceFirmwareFailureNotificationEnabled=coDeviceFirmwareFailureNotificationEnabled, coDevInfoBootRevision=coDevInfoBootRevision, coDevStCpuUse5Sec=coDevStCpuUse5Sec, coDevStCpuUse20Sec=coDevStCpuUse20Sec, coDevStRamFree=coDevStRamFree, coDevDisIpAddress=coDevDisIpAddress, coDeviceInfoEntry=coDeviceInfoEntry, coDeviceDiscoveryTable=coDeviceDiscoveryTable, colubrisDeviceMIBCompliance=colubrisDeviceMIBCompliance, colubrisDeviceMIBNotificationPrefix=colubrisDeviceMIBNotificationPrefix, coDeviceSecurityFailureNotificationEnabled=coDeviceSecurityFailureNotificationEnabled, coDeviceSecurityFailureNotification=coDeviceSecurityFailureNotification, colubrisDeviceNotificationGroup=colubrisDeviceNotificationGroup, colubrisDeviceStatusMIBGroup=colubrisDeviceStatusMIBGroup, coDeviceAuthorizationFailureNotificationEnabled=coDeviceAuthorizationFailureNotificationEnabled, coDeviceDiscoveryGroup=coDeviceDiscoveryGroup, coDevInfoFirmwareRevision=coDevInfoFirmwareRevision, colubrisDeviceMIBConformance=colubrisDeviceMIBConformance, coDevStRamBuffer=coDevStRamBuffer, PYSNMP_MODULE_ID=colubrisDeviceMIB, coDevDisSystemName=coDevDisSystemName, coDeviceStatusTable=coDeviceStatusTable, coDevStLoadAverage1Min=coDevStLoadAverage1Min, coDeviceConfigurationFailureNotificationEnabled=coDeviceConfigurationFailureNotificationEnabled, coDevDisContact=coDevDisContact, coDevStLoadAverage15Min=coDevStLoadAverage15Min, coDevStRamTotal=coDevStRamTotal, coDevStStorageUsePermanent=coDevStStorageUsePermanent, coDevStCpuUseNow=coDevStCpuUseNow)
