#
# PySNMP MIB module EXAGRID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exagrid/EXAGRID-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:12 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
InternationalDisplayString, = mibBuilder.importSymbols("HOST-RESOURCES-MIB", "InternationalDisplayString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibIdentifier, IpAddress, enterprises, Integer32, iso, NotificationType, Bits, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "IpAddress", "enterprises", "Integer32", "iso", "NotificationType", "Bits", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
exagrid = MibIdentifier((1, 3, 6, 1, 4, 1, 14941))
exagridTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 1))
egEventParams = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 2))
exagridProductLines = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3))
exagridExX000Series = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1))
exagridExX000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 0))
exagridEx1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 1))
exagridEx2000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 2))
exagridEx3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 3))
exagridEx4000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 4))
exagridEx5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 5))
exagridExGW = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 6))
exagridEx10000E = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 10))
exagridEx1T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 11))
exagridEx2T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 12))
exagridEx3T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 13))
exagridEx4T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 14))
exagridEx5T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 15))
exagridEx7T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 16))
exagridEx9T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 19))
exagridEx7S = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 26))
exagridEx9S = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 29))
exagridEx1T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 31))
exagridEx2T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 32))
exagridEx3T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 33))
exagridEx4T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 34))
exagridEx5T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 35))
exagridEx7T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 36))
exagridEx7S2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 46))
exagridEx10T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 110))
exagridEx13T = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 113))
exagridEx10S = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 210))
exagridEx13S = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 213))
exagridEx10T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 310))
exagridEx13T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 313))
exagridEx21T2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 321))
exagridEx10S2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 410))
exagridEx13S2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 413))
exagridEx21S2012A = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 3, 1, 421))
exagridServerData = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4))
exagridLandingSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 1))
exagridRetentionSpace = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 2))
exagridDeduplicationRatio = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 3))
exagridPendingDeduplication = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 4))
exagridPendingReplication = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 5))
exagridServerStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 14941, 4, 6))
egLandingSpaceConfiguredWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egLandingSpaceConfiguredWholeGigabytes.setStatus('mandatory')
egLandingSpaceConfiguredFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egLandingSpaceConfiguredFractionalGigabytes.setStatus('mandatory')
egLandingSpaceAvailableWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egLandingSpaceAvailableWholeGigabytes.setStatus('mandatory')
egLandingSpaceAvailableFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egLandingSpaceAvailableFractionalGigabytes.setStatus('mandatory')
egRetentionSpaceConfiguredWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 2, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egRetentionSpaceConfiguredWholeGigabytes.setStatus('mandatory')
egRetentionSpaceConfiguredFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 2, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egRetentionSpaceConfiguredFractionalGigabytes.setStatus('mandatory')
egRetentionSpaceAvailableWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 2, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egRetentionSpaceAvailableWholeGigabytes.setStatus('mandatory')
egRetentionSpaceAvailableFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 2, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egRetentionSpaceAvailableFractionalGigabytes.setStatus('mandatory')
egBackupDataAvailableWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 3, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egBackupDataAvailableWholeGigabytes.setStatus('mandatory')
egBackupDataAvailableFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 3, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egBackupDataAvailableFractionalGigabytes.setStatus('mandatory')
egBackupDataSpaceConsumedWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 3, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egBackupDataSpaceConsumedWholeGigabytes.setStatus('mandatory')
egBackupDataSpaceConsumedFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 3, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egBackupDataSpaceConsumedFractionalGigabytes.setStatus('mandatory')
egPendingDeduplicationWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 4, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingDeduplicationWholeGigabytes.setStatus('mandatory')
egPendingDeduplicationFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 4, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingDeduplicationFractionalGigabytes.setStatus('mandatory')
egPendingDeduplicationAge = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 4, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingDeduplicationAge.setStatus('mandatory')
egPendingReplicationWholeGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 5, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingReplicationWholeGigabytes.setStatus('mandatory')
egPendingReplicationFractionalGigabytes = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 5, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingReplicationFractionalGigabytes.setStatus('mandatory')
egPendingReplicationAge = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 5, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egPendingReplicationAge.setStatus('mandatory')
egServerAlarmState = MibScalar((1, 3, 6, 1, 4, 1, 14941, 4, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: egServerAlarmState.setStatus('mandatory')
egEventParamsName = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsName.setStatus('mandatory')
egEventParamsId = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsId.setStatus('mandatory')
egEventParamsCreateTime = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsCreateTime.setStatus('mandatory')
egEventParamsCreateTimeRaw = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsCreateTimeRaw.setStatus('mandatory')
egEventParamsGridName = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsGridName.setStatus('mandatory')
egEventParamsSiteName = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsSiteName.setStatus('mandatory')
egEventParamsSiteId = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsSiteId.setStatus('mandatory')
egEventParamsSeverity = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsSeverity.setStatus('mandatory')
egEventParamsDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDeviceName.setStatus('mandatory')
egEventParamsDeviceId = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDeviceId.setStatus('mandatory')
egEventParamsDeviceSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDeviceSerialNumber.setStatus('mandatory')
egEventParamsDeviceIp = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDeviceIp.setStatus('mandatory')
egEventParamsDupCount = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDupCount.setStatus('mandatory')
egEventParamsText = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsText.setStatus('mandatory')
egEventParamsDetail = MibScalar((1, 3, 6, 1, 4, 1, 14941, 2, 15), InternationalDisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: egEventParamsDetail.setStatus('mandatory')
egTrap = NotificationType((1, 3, 6, 1, 4, 1, 14941, 1) + (0,1)).setObjects(("EXAGRID-MIB", "egEventParamsName"), ("EXAGRID-MIB", "egEventParamsId"), ("EXAGRID-MIB", "egEventParamsCreateTime"), ("EXAGRID-MIB", "egEventParamsCreateTimeRaw"), ("EXAGRID-MIB", "egEventParamsGridName"), ("EXAGRID-MIB", "egEventParamsSiteName"), ("EXAGRID-MIB", "egEventParamsSiteId"), ("EXAGRID-MIB", "egEventParamsSeverity"), ("EXAGRID-MIB", "egEventParamsDeviceName"), ("EXAGRID-MIB", "egEventParamsDeviceId"), ("EXAGRID-MIB", "egEventParamsDeviceIp"), ("EXAGRID-MIB", "egEventParamsDeviceSerialNumber"), ("EXAGRID-MIB", "egEventParamsDupCount"), ("EXAGRID-MIB", "egEventParamsText"), ("EXAGRID-MIB", "egEventParamsDetail"))
mibBuilder.exportSymbols("EXAGRID-MIB", exagridServerStatus=exagridServerStatus, exagridEx2T=exagridEx2T, exagridEx5T2012A=exagridEx5T2012A, exagridEx7T2012A=exagridEx7T2012A, egEventParamsDetail=egEventParamsDetail, exagridRetentionSpace=exagridRetentionSpace, egEventParamsDeviceSerialNumber=egEventParamsDeviceSerialNumber, exagridEx13S=exagridEx13S, egBackupDataSpaceConsumedFractionalGigabytes=egBackupDataSpaceConsumedFractionalGigabytes, egTrap=egTrap, exagridEx1000=exagridEx1000, exagridEx7S2012A=exagridEx7S2012A, exagridEx3000=exagridEx3000, exagridServerData=exagridServerData, egEventParamsSeverity=egEventParamsSeverity, egEventParamsDeviceId=egEventParamsDeviceId, exagridEx5T=exagridEx5T, exagridExGW=exagridExGW, egPendingDeduplicationFractionalGigabytes=egPendingDeduplicationFractionalGigabytes, exagridEx21S2012A=exagridEx21S2012A, egEventParamsSiteName=egEventParamsSiteName, egLandingSpaceAvailableWholeGigabytes=egLandingSpaceAvailableWholeGigabytes, egEventParams=egEventParams, exagridEx7S=exagridEx7S, egServerAlarmState=egServerAlarmState, exagridPendingDeduplication=exagridPendingDeduplication, exagridEx2000=exagridEx2000, egRetentionSpaceAvailableFractionalGigabytes=egRetentionSpaceAvailableFractionalGigabytes, exagridEx4T=exagridEx4T, exagridExX000Series=exagridExX000Series, egPendingReplicationAge=egPendingReplicationAge, exagridEx9T=exagridEx9T, egBackupDataAvailableWholeGigabytes=egBackupDataAvailableWholeGigabytes, exagridExX000=exagridExX000, exagridPendingReplication=exagridPendingReplication, egEventParamsDeviceName=egEventParamsDeviceName, egEventParamsText=egEventParamsText, exagridEx21T2012A=exagridEx21T2012A, exagridEx13S2012A=exagridEx13S2012A, exagridEx4000=exagridEx4000, exagridProductLines=exagridProductLines, egEventParamsName=egEventParamsName, exagridEx1T2012A=exagridEx1T2012A, egPendingDeduplicationWholeGigabytes=egPendingDeduplicationWholeGigabytes, egEventParamsDeviceIp=egEventParamsDeviceIp, exagridEx4T2012A=exagridEx4T2012A, exagridEx3T=exagridEx3T, egEventParamsCreateTimeRaw=egEventParamsCreateTimeRaw, exagridEx1T=exagridEx1T, egEventParamsSiteId=egEventParamsSiteId, egPendingReplicationWholeGigabytes=egPendingReplicationWholeGigabytes, exagridEx13T=exagridEx13T, exagridEx2T2012A=exagridEx2T2012A, exagridEx7T=exagridEx7T, egLandingSpaceConfiguredWholeGigabytes=egLandingSpaceConfiguredWholeGigabytes, exagridTraps=exagridTraps, egLandingSpaceConfiguredFractionalGigabytes=egLandingSpaceConfiguredFractionalGigabytes, exagridDeduplicationRatio=exagridDeduplicationRatio, exagrid=exagrid, exagridEx13T2012A=exagridEx13T2012A, egLandingSpaceAvailableFractionalGigabytes=egLandingSpaceAvailableFractionalGigabytes, exagridEx9S=exagridEx9S, exagridEx10S2012A=exagridEx10S2012A, exagridEx5000=exagridEx5000, egEventParamsGridName=egEventParamsGridName, egEventParamsId=egEventParamsId, egEventParamsCreateTime=egEventParamsCreateTime, exagridEx10S=exagridEx10S, egPendingReplicationFractionalGigabytes=egPendingReplicationFractionalGigabytes, egRetentionSpaceConfiguredFractionalGigabytes=egRetentionSpaceConfiguredFractionalGigabytes, exagridEx10T=exagridEx10T, exagridEx10T2012A=exagridEx10T2012A, egBackupDataAvailableFractionalGigabytes=egBackupDataAvailableFractionalGigabytes, egPendingDeduplicationAge=egPendingDeduplicationAge, egRetentionSpaceAvailableWholeGigabytes=egRetentionSpaceAvailableWholeGigabytes, exagridEx10000E=exagridEx10000E, egEventParamsDupCount=egEventParamsDupCount, exagridEx3T2012A=exagridEx3T2012A, egBackupDataSpaceConsumedWholeGigabytes=egBackupDataSpaceConsumedWholeGigabytes, egRetentionSpaceConfiguredWholeGigabytes=egRetentionSpaceConfiguredWholeGigabytes, exagridLandingSpace=exagridLandingSpace)
