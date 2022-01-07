#
# PySNMP MIB module VEEAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/veeam/VEEAM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:41:03 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, IpAddress, TimeTicks, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, NotificationType, ObjectIdentity, Unsigned32, NotificationType, Counter32, Integer32, Gauge32, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "IpAddress", "TimeTicks", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "NotificationType", "ObjectIdentity", "Unsigned32", "NotificationType", "Counter32", "Integer32", "Gauge32", "iso", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
veeam = MibIdentifier((1, 3, 6, 1, 4, 1, 31023))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 31023, 1))
backup = MibIdentifier((1, 3, 6, 1, 4, 1, 31023, 1, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1))
onBackupJobCompleted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,1)).setObjects(("VEEAM-MIB", "backupJobId"), ("VEEAM-MIB", "backupJobName"), ("VEEAM-MIB", "backupJobResult"), ("VEEAM-MIB", "backupJobComment"))
onVmBackupCompleted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,2)).setObjects(("VEEAM-MIB", "backupJobName"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "sourceHostName"), ("VEEAM-MIB", "vmBackupResult"), ("VEEAM-MIB", "vmBackupComment"))
onLinuxFLRMountStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,3)).setObjects(("VEEAM-MIB", "sessionId"), ("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"))
onLinuxFLRCopyToStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,4)).setObjects(("VEEAM-MIB", "sessionId"), ("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "targetHost"), ("VEEAM-MIB", "targetDir"))
onLinuxFLRToOriginalStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,5)).setObjects(("VEEAM-MIB", "sessionId"), ("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"))
onLinuxFLRCopyToFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,6)).setObjects(("VEEAM-MIB", "sessionId"), ("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "transferStatus"), ("VEEAM-MIB", "transferTime"), ("VEEAM-MIB", "transferFileList"), ("VEEAM-MIB", "notTransferFileList"), ("VEEAM-MIB", "targetHost"), ("VEEAM-MIB", "targetDir"), ("VEEAM-MIB", "csvReportFilePath"))
onLinuxFLRToOriginalFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,7)).setObjects(("VEEAM-MIB", "sessionId"), ("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "transferStatus"), ("VEEAM-MIB", "transferTime"), ("VEEAM-MIB", "transferFileList"), ("VEEAM-MIB", "notTransferFileList"), ("VEEAM-MIB", "csvReportFilePath"))
onWinFLRMountStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,8)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "mountServerName"))
onWinFLRToOriginalStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,9)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"))
onWinFLRCopyToStarted = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,10)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "targetDir"))
onWinFLRToOriginalFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,11)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "transferStatus"), ("VEEAM-MIB", "transferFileList"), ("VEEAM-MIB", "notTransferFileList"), ("VEEAM-MIB", "csvReportFilePath"))
onWinFLRCopyToFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,12)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "transferStatus"), ("VEEAM-MIB", "transferFileList"), ("VEEAM-MIB", "notTransferFileList"), ("VEEAM-MIB", "targetDir"), ("VEEAM-MIB", "csvReportFilePath"))
onWebDownloadStart = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,13)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointCreationTime"))
onWebDownloadFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,14)).setObjects(("VEEAM-MIB", "initiatorName"), ("VEEAM-MIB", "initiatorSid"), ("VEEAM-MIB", "vmRestorePointId"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "vmRestorePointCreationTime"), ("VEEAM-MIB", "transferStatus"), ("VEEAM-MIB", "transferFileList"), ("VEEAM-MIB", "notTransferFileList"))
onSobrOffloadFinished = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,15)).setObjects(("VEEAM-MIB", "repositoryId"), ("VEEAM-MIB", "repositoryName"), ("VEEAM-MIB", "repositoryStatus"), ("VEEAM-MIB", "extentStatusList"))
onCdpRpoReport = NotificationType((1, 3, 6, 1, 4, 1, 31023, 1, 1, 1) + (0,16)).setObjects(("VEEAM-MIB", "cdpPolicyName"), ("VEEAM-MIB", "cdpRpoStatus"), ("VEEAM-MIB", "vmName"), ("VEEAM-MIB", "cdpSla"), ("VEEAM-MIB", "cdpRpoThreshold"), ("VEEAM-MIB", "cdpMaxDelay"))
backupJobId = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 101), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupJobId.setStatus('mandatory')
backupJobName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 102), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupJobName.setStatus('mandatory')
backupJobResult = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 103), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupJobResult.setStatus('mandatory')
backupJobComment = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 104), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: backupJobComment.setStatus('mandatory')
vmName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 105), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmName.setStatus('mandatory')
sourceHostName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 106), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sourceHostName.setStatus('mandatory')
vmBackupResult = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 107), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmBackupResult.setStatus('mandatory')
vmBackupComment = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 108), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmBackupComment.setStatus('mandatory')
sessionId = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 109), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sessionId.setStatus('mandatory')
initiatorName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 110), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: initiatorName.setStatus('mandatory')
initiatorSid = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 111), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: initiatorSid.setStatus('mandatory')
vmRestorePointId = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 112), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmRestorePointId.setStatus('mandatory')
vmRestorePointCreationTime = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 113), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vmRestorePointCreationTime.setStatus('mandatory')
targetHost = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 114), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: targetHost.setStatus('mandatory')
targetDir = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 115), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: targetDir.setStatus('mandatory')
transferStatus = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 116), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transferStatus.setStatus('mandatory')
transferTime = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 117), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transferTime.setStatus('mandatory')
transferFileList = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 118), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: transferFileList.setStatus('mandatory')
notTransferFileList = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 119), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: notTransferFileList.setStatus('mandatory')
mountServerName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 120), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mountServerName.setStatus('mandatory')
repositoryId = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 121), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: repositoryId.setStatus('mandatory')
repositoryName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 122), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: repositoryName.setStatus('mandatory')
repositoryStatus = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 123), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: repositoryStatus.setStatus('mandatory')
extentStatusList = MibTable((1, 3, 6, 1, 4, 1, 31023, 1, 1, 124), ).setMaxAccess("readonly")
if mibBuilder.loadTexts: extentStatusList.setStatus('mandatory')
extentStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 31023, 1, 1, 124, 1), ).setMaxAccess("readonly").setIndexNames((0, "VEEAM-MIB", "extentName"))
if mibBuilder.loadTexts: extentStatusEntry.setStatus('mandatory')
extentName = MibTableColumn((1, 3, 6, 1, 4, 1, 31023, 1, 1, 124, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extentName.setStatus('mandatory')
extentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 31023, 1, 1, 124, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extentStatus.setStatus('mandatory')
csvReportFilePath = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 125), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: csvReportFilePath.setStatus('mandatory')
cdpPolicyName = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 126), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpPolicyName.setStatus('mandatory')
cdpRpoStatus = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 127), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpRpoStatus.setStatus('mandatory')
cdpSla = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 128), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpSla.setStatus('mandatory')
cdpRpoThreshold = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 129), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpRpoThreshold.setStatus('mandatory')
cdpMaxDelay = MibScalar((1, 3, 6, 1, 4, 1, 31023, 1, 1, 130), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cdpMaxDelay.setStatus('mandatory')
mibBuilder.exportSymbols("VEEAM-MIB", products=products, backupJobName=backupJobName, onWinFLRCopyToStarted=onWinFLRCopyToStarted, onWinFLRCopyToFinished=onWinFLRCopyToFinished, onBackupJobCompleted=onBackupJobCompleted, mountServerName=mountServerName, cdpSla=cdpSla, targetDir=targetDir, veeam=veeam, onWinFLRMountStarted=onWinFLRMountStarted, targetHost=targetHost, onWinFLRToOriginalStarted=onWinFLRToOriginalStarted, backup=backup, cdpPolicyName=cdpPolicyName, extentStatusList=extentStatusList, onVmBackupCompleted=onVmBackupCompleted, vmRestorePointCreationTime=vmRestorePointCreationTime, initiatorSid=initiatorSid, repositoryStatus=repositoryStatus, cdpRpoStatus=cdpRpoStatus, notTransferFileList=notTransferFileList, backupJobComment=backupJobComment, onLinuxFLRCopyToFinished=onLinuxFLRCopyToFinished, onLinuxFLRToOriginalStarted=onLinuxFLRToOriginalStarted, transferTime=transferTime, onLinuxFLRToOriginalFinished=onLinuxFLRToOriginalFinished, vmName=vmName, vmBackupComment=vmBackupComment, traps=traps, cdpRpoThreshold=cdpRpoThreshold, onWebDownloadFinished=onWebDownloadFinished, sessionId=sessionId, backupJobResult=backupJobResult, transferStatus=transferStatus, onCdpRpoReport=onCdpRpoReport, onWinFLRToOriginalFinished=onWinFLRToOriginalFinished, vmRestorePointId=vmRestorePointId, transferFileList=transferFileList, repositoryName=repositoryName, extentName=extentName, csvReportFilePath=csvReportFilePath, sourceHostName=sourceHostName, extentStatus=extentStatus, repositoryId=repositoryId, extentStatusEntry=extentStatusEntry, backupJobId=backupJobId, cdpMaxDelay=cdpMaxDelay, onLinuxFLRMountStarted=onLinuxFLRMountStarted, onLinuxFLRCopyToStarted=onLinuxFLRCopyToStarted, initiatorName=initiatorName, vmBackupResult=vmBackupResult, onSobrOffloadFinished=onSobrOffloadFinished, onWebDownloadStart=onWebDownloadStart)
