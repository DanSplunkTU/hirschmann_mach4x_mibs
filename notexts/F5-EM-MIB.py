#
# PySNMP MIB module F5-EM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/f5/F5-EM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:02:36 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
LongDisplayString, bigipCompliances, f5, bigipGroups = mibBuilder.importSymbols("F5-BIGIP-COMMON-MIB", "LongDisplayString", "bigipCompliances", "f5", "bigipGroups")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, ModuleIdentity, Gauge32, Counter64, iso, Bits, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, enterprises, Integer32, Counter32, Opaque, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "Gauge32", "Counter64", "iso", "Bits", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "enterprises", "Integer32", "Counter32", "Opaque", "ObjectIdentity")
DisplayString, MacAddress, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention", "DateAndTime")
enterpriseManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 3375, 3))
if mibBuilder.loadTexts: enterpriseManagement.setLastUpdated('201202072039Z')
if mibBuilder.loadTexts: enterpriseManagement.setOrganization('F5 Networks, Inc.')
emDevices = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 1))
emDeviceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 2))
emImages = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 3))
emArchives = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 4))
emGlobals = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 5))
emAlert = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 6))
emAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0))
emAlertObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 6, 1))
emAlertConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 0))
emDeviceList = MibIdentifier((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1))
deviceNumber = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceNumber.setStatus('current')
deviceEntryTable = MibTable((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2), )
if mibBuilder.loadTexts: deviceEntryTable.setStatus('current')
deviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1), ).setIndexNames((0, "F5-EM-MIB", "deviceName"))
if mibBuilder.loadTexts: deviceEntry.setStatus('current')
deviceName = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceName.setStatus('current')
deviceAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceAddressType.setStatus('current')
deviceAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceAddress.setStatus('current')
groupNumber = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupNumber.setStatus('current')
groupEntryTable = MibTable((1, 3, 6, 1, 4, 1, 3375, 3, 2, 2), )
if mibBuilder.loadTexts: groupEntryTable.setStatus('current')
groupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3375, 3, 2, 2, 1), ).setIndexNames((0, "F5-EM-MIB", "groupName"))
if mibBuilder.loadTexts: groupEntry.setStatus('current')
groupName = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 2, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupName.setStatus('current')
groupDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: groupDescription.setStatus('current')
imageNumber = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imageNumber.setStatus('current')
imageEntryTable = MibTable((1, 3, 6, 1, 4, 1, 3375, 3, 3, 2), )
if mibBuilder.loadTexts: imageEntryTable.setStatus('current')
imageEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3375, 3, 3, 2, 1), ).setIndexNames((0, "F5-EM-MIB", "imageVersion"))
if mibBuilder.loadTexts: imageEntry.setStatus('current')
imageVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 3, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imageVersion.setStatus('current')
imageDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 3, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: imageDescription.setStatus('current')
archiveNumber = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 4, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveNumber.setStatus('obsolete')
archiveEntryTable = MibTable((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2), )
if mibBuilder.loadTexts: archiveEntryTable.setStatus('obsolete')
archiveEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1), ).setIndexNames((0, "F5-EM-MIB", "archiveSourceDevice"))
if mibBuilder.loadTexts: archiveEntry.setStatus('obsolete')
archiveSourceDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveSourceDevice.setStatus('obsolete')
archiveProduct = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveProduct.setStatus('obsolete')
archiveVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveVersion.setStatus('obsolete')
archiveTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveTimeStamp.setStatus('obsolete')
archiveFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveFilename.setStatus('obsolete')
archiveDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 3375, 3, 4, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: archiveDescription.setStatus('obsolete')
emMaxConcurrentUpdates = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 5, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: emMaxConcurrentUpdates.setStatus('obsolete')
emRefreshInterval = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: emRefreshInterval.setStatus('obsolete')
emVersion = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 5, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: emVersion.setStatus('obsolete')
emAlertObjMsg = MibScalar((1, 3, 6, 1, 4, 1, 3375, 3, 6, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: emAlertObjMsg.setStatus('current')
emDeviceUnreachable = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 1)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceUnreachable.setStatus('current')
emSoftwareInstallComplete = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 2)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emSoftwareInstallComplete.setStatus('current')
emSoftwareInstallFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 3)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emSoftwareInstallFailed.setStatus('current')
emDeviceClockSkew = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 4)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceClockSkew.setStatus('current')
emDiskUsage = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 5)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDiskUsage.setStatus('current')
emMemoryUsage = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 6)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emMemoryUsage.setStatus('current')
emHotfixInstallComplete = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 7)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emHotfixInstallComplete.setStatus('current')
emHotfixInstallFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 8)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emHotfixInstallFailed.setStatus('current')
emCpuUsage = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 9)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emCpuUsage.setStatus('current')
emCertificateExpiration = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 10)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emCertificateExpiration.setStatus('current')
emScheduledArchiveFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 11)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emScheduledArchiveFailed.setStatus('current')
emDeviceActiveMode = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 12)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceActiveMode.setStatus('current')
emDeviceStandbyMode = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 13)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceStandbyMode.setStatus('current')
emDeviceConfigSync = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 14)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceConfigSync.setStatus('current')
emRaidDriveFailureDetected = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 15)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emRaidDriveFailureDetected.setStatus('current')
emRaidDriveRebuildComplete = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 16)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emRaidDriveRebuildComplete.setStatus('current')
emHaSyncFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 19)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emHaSyncFailed.setStatus('current')
emASMSigInstallComplete = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 20)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emASMSigInstallComplete.setStatus('current')
emASMSigInstallFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 21)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emASMSigInstallFailed.setStatus('current')
emASMSigUpdateAvailable = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 22)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emASMSigUpdateAvailable.setStatus('current')
emASMSigUpdateFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 23)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emASMSigUpdateFailed.setStatus('current')
emPerformanceStorageDays = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 25)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emPerformanceStorageDays.setStatus('current')
emPerformanceStorageCap = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 26)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emPerformanceStorageCap.setStatus('current')
emPerformanceThreshold = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 27)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emPerformanceThreshold.setStatus('current')
emSchedBackupFailed = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 28)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emSchedBackupFailed.setStatus('current')
emStatsCollectionRateCap = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 29)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emStatsCollectionRateCap.setStatus('current')
emDeviceOfflineMode = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 30)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceOfflineMode.setStatus('current')
emDeviceForcedOfflineMode = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 31)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceForcedOfflineMode.setStatus('current')
emServiceContractExpiry = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 32)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emServiceContractExpiry.setStatus('current')
emStatsDBConnectivityLost = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 33)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emStatsDBConnectivityLost.setStatus('current')
emGatherServiceContractFailure = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 34)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emGatherServiceContractFailure.setStatus('current')
emDeviceImpaired = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 35)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceImpaired.setStatus('current')
emStatsDBConnectivityRestored = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 36)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emStatsDBConnectivityRestored.setStatus('current')
emDeviceConfigSettingChanged = NotificationType((1, 3, 6, 1, 4, 1, 3375, 3, 6, 0, 0, 1)).setObjects(("F5-EM-MIB", "emAlertObjMsg"))
if mibBuilder.loadTexts: emDeviceConfigSettingChanged.setStatus('obsolete')
mibBuilder.exportSymbols("F5-EM-MIB", groupName=groupName, enterpriseManagement=enterpriseManagement, imageNumber=imageNumber, emDevices=emDevices, emPerformanceStorageDays=emPerformanceStorageDays, emAlertObjMsg=emAlertObjMsg, emRaidDriveRebuildComplete=emRaidDriveRebuildComplete, emScheduledArchiveFailed=emScheduledArchiveFailed, emGlobals=emGlobals, archiveSourceDevice=archiveSourceDevice, imageEntry=imageEntry, deviceAddress=deviceAddress, emHotfixInstallComplete=emHotfixInstallComplete, emCertificateExpiration=emCertificateExpiration, emRaidDriveFailureDetected=emRaidDriveFailureDetected, emASMSigInstallFailed=emASMSigInstallFailed, emSchedBackupFailed=emSchedBackupFailed, emImages=emImages, emAlerts=emAlerts, archiveDescription=archiveDescription, groupNumber=groupNumber, emMaxConcurrentUpdates=emMaxConcurrentUpdates, emAlertConfigObjects=emAlertConfigObjects, emDeviceConfigSettingChanged=emDeviceConfigSettingChanged, emSoftwareInstallFailed=emSoftwareInstallFailed, emDeviceOfflineMode=emDeviceOfflineMode, emStatsDBConnectivityRestored=emStatsDBConnectivityRestored, imageEntryTable=imageEntryTable, emASMSigInstallComplete=emASMSigInstallComplete, emStatsCollectionRateCap=emStatsCollectionRateCap, emAlertObjects=emAlertObjects, emVersion=emVersion, emAlert=emAlert, emServiceContractExpiry=emServiceContractExpiry, emSoftwareInstallComplete=emSoftwareInstallComplete, emDeviceActiveMode=emDeviceActiveMode, emPerformanceThreshold=emPerformanceThreshold, emDeviceForcedOfflineMode=emDeviceForcedOfflineMode, emStatsDBConnectivityLost=emStatsDBConnectivityLost, emGatherServiceContractFailure=emGatherServiceContractFailure, emDeviceImpaired=emDeviceImpaired, deviceName=deviceName, emHotfixInstallFailed=emHotfixInstallFailed, emHaSyncFailed=emHaSyncFailed, emDeviceStandbyMode=emDeviceStandbyMode, emDeviceList=emDeviceList, emASMSigUpdateAvailable=emASMSigUpdateAvailable, groupEntry=groupEntry, emDiskUsage=emDiskUsage, archiveProduct=archiveProduct, archiveNumber=archiveNumber, emASMSigUpdateFailed=emASMSigUpdateFailed, emDeviceGroups=emDeviceGroups, deviceEntryTable=deviceEntryTable, archiveTimeStamp=archiveTimeStamp, archiveFilename=archiveFilename, emDeviceClockSkew=emDeviceClockSkew, groupEntryTable=groupEntryTable, groupDescription=groupDescription, PYSNMP_MODULE_ID=enterpriseManagement, emCpuUsage=emCpuUsage, imageDescription=imageDescription, deviceEntry=deviceEntry, archiveEntryTable=archiveEntryTable, emRefreshInterval=emRefreshInterval, imageVersion=imageVersion, emDeviceConfigSync=emDeviceConfigSync, archiveEntry=archiveEntry, emPerformanceStorageCap=emPerformanceStorageCap, emArchives=emArchives, deviceAddressType=deviceAddressType, emDeviceUnreachable=emDeviceUnreachable, emMemoryUsage=emMemoryUsage, archiveVersion=archiveVersion, deviceNumber=deviceNumber)
