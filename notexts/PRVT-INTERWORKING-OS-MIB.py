#
# PySNMP MIB module PRVT-INTERWORKING-OS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-INTERWORKING-OS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
prvt_products, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "prvt-products")
usmUserSecurityName, = mibBuilder.importSymbols("SNMP-USER-BASED-SM-MIB", "usmUserSecurityName")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, NotificationType, Gauge32, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "MacAddress")
prvtInterworkOsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 111, 1))
prvtInterworkOsMib.setRevisions(('2008-04-09 00:00', '2008-03-31 00:00', '2008-01-01 00:00', '2005-02-16 00:00', '2004-12-20 00:00', '2004-03-10 00:00', '2003-05-08 00:00', '2002-12-12 00:00', '2002-11-26 00:00', '2002-11-17 00:00', '2001-04-19 00:00', '2001-03-19 00:00',))
if mibBuilder.loadTexts: prvtInterworkOsMib.setLastUpdated('200804090000Z')
if mibBuilder.loadTexts: prvtInterworkOsMib.setOrganization('BATM Advanced Communication')
software = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111))
prvtInterworkOsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0))
version = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1))
option = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 2))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3))
cpu = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4))
prvtInterworkOsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 5))
bootVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootVersionNumber.setStatus('current')
bootVersionDate = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootVersionDate.setStatus('current')
bootVersionString = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bootVersionString.setStatus('current')
oSversionNumber = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oSversionNumber.setStatus('current')
oSversionDate = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oSversionDate.setStatus('current')
oSversionString = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oSversionString.setStatus('current')
appletVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appletVersionNumber.setStatus('current')
appletVersionDate = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: appletVersionDate.setStatus('current')
optionInstalled = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 2, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: optionInstalled.setStatus('current')
managementConnectivity = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1))
managementConnectivityMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managementConnectivityMACAddr.setStatus('current')
managementConnectivityIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementConnectivityIpAddress.setStatus('current')
managementConnectivityIPNetMask = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementConnectivityIPNetMask.setStatus('current')
managementIPGateAddress = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementIPGateAddress.setStatus('current')
managementSerialBaud = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("baud2400", 1), ("baud9600", 2), ("baud19200", 3), ("baud38400", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementSerialBaud.setStatus('current')
managementLoad = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2))
managementLoadTftpServerAddress = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementLoadTftpServerAddress.setStatus('current')
managementLoadFileName = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementLoadFileName.setStatus('current')
managementLoadType = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("application", 1), ("boot", 2), ("configuration", 3), ("java", 4), ("vdsl-E2", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementLoadType.setStatus('current')
managementLoadExecute = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noop", 1), ("download", 2), ("upload", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementLoadExecute.setStatus('current')
managementLoadExecuteStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("not-started", 1), ("in-progress", 2), ("success", 3), ("error-connection", 4), ("error-filename", 5), ("error-fault", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: managementLoadExecuteStatus.setStatus('current')
managementMisc = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3))
managementMiscSaveToNvm = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("save", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementMiscSaveToNvm.setStatus('current')
managementMiscReset = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("noop", 1), ("reset", 2), ("reset-to-defaults", 3), ("save-and-reset", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementMiscReset.setStatus('current')
managementMiscReload = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noop", 1), ("save-and-reload", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementMiscReload.setStatus('current')
managementMiscReloadInTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementMiscReloadInTime.setStatus('current')
managementMiscReloadAtTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementMiscReloadAtTime.setStatus('current')
managementMiscReloadSaveInTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementMiscReloadSaveInTime.setStatus('current')
managementMiscReloadSaveAtTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 3, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementMiscReloadSaveAtTime.setStatus('current')
managementLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 4))
managementOptionSupportStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31))).clone(namedValues=NamedValues(("reserved0", 0), ("reserved1", 1), ("reserved2", 2), ("reserved3", 3), ("reserved4", 4), ("reserved5", 5), ("reserved6", 6), ("reserved7", 7), ("reserved8", 8), ("reserved9", 9), ("licNotSpecified", 10), ("licBasic", 11), ("licML", 12), ("licAdvML", 13), ("reserved14", 14), ("reserved15", 15), ("reserved16", 16), ("reserved17", 17), ("reserved18", 18), ("reserved19", 19), ("reserved20", 20), ("reserved21", 21), ("reserved22", 22), ("reserved23", 23), ("reserved24", 24), ("reserved25", 25), ("reserved26", 26), ("reserved27", 27), ("reserved28", 28), ("reserved29", 29), ("reserved30", 30), ("reserved31", 31)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: managementOptionSupportStatus.setStatus('current')
managementOptionSupportKey = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 4, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managementOptionSupportKey.setStatus('current')
managementOptionSupportAddress = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 4, 3), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: managementOptionSupportAddress.setStatus('current')
managementOptionSupportL3Capable = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 4, 4), TruthValue().clone('true')).setMaxAccess("readonly")
if mibBuilder.loadTexts: managementOptionSupportL3Capable.setStatus('current')
prvtBootConfigUpgrade = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5))
prvtBootUpgradeSrcURI = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtBootUpgradeSrcURI.setStatus('current')
prvtBootApplicationNameURI = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtBootApplicationNameURI.setStatus('current')
prvtBootConfigURI = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtBootConfigURI.setStatus('current')
prvtBootUpgradeCmd = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("ready", 1), ("apply", 2), ("applyExec", 3))).clone('ready')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtBootUpgradeCmd.setStatus('current')
prvtBootOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("ready", 1), ("notReady", 2), ("upgradeInProgress", 3))).clone('ready')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtBootOperStatus.setStatus('current')
prvtBootErrorCondition = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 3, 5, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))).clone(namedValues=NamedValues(("noError", 0), ("genericError", 1), ("copyFailed", 2), ("downloadFailed", 3), ("freeSpaceError", 4), ("validationFailed", 5), ("backupFailed", 6), ("inProgressError", 7), ("consistencyError", 8), ("fileSystemError", 9), ("profileNameError", 10), ("profileError", 11), ("fileNameError", 12), ("pathError", 13), ("zFileError", 14), ("cannotFindFile", 15), ("defApplicationProfileError", 16), ("configProfileError", 17), ("bootDevProfileError", 18), ("ftpServerProfileError", 19), ("ftpUserProfileError", 20), ("ftpPassProfileError", 21))).clone('noError')).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtBootErrorCondition.setStatus('current')
cpuMonitoring = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 1))
cpuMonitoringStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cpuMonitoringStatus.setStatus('current')
cpuMonitoringUtilization = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuMonitoringUtilization.setStatus('current')
cpuRedundancy = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2))
cpuHwRedundancySupport = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuHwRedundancySupport.setStatus('current')
cpuRedundancyTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2), )
if mibBuilder.loadTexts: cpuRedundancyTable.setStatus('current')
cpuRedundancyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1), ).setIndexNames((0, "PRVT-INTERWORKING-OS-MIB", "cpuId"))
if mibBuilder.loadTexts: cpuRedundancyEntry.setStatus('current')
cpuId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)))
if mibBuilder.loadTexts: cpuId.setStatus('current')
cpuName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuName.setStatus('current')
cpuStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("standby", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuStatus.setStatus('current')
cpuRedundancySupport = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuRedundancySupport.setStatus('current')
cpuSWVersionString = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuSWVersionString.setStatus('current')
cpuHW = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 3))
cpuRAMsize = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 4, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cpuRAMsize.setStatus('current')
imageCrcCheckFailed = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0, 1)).setObjects(("PRVT-INTERWORKING-OS-MIB", "managementLoadTftpServerAddress"), ("PRVT-INTERWORKING-OS-MIB", "managementLoadFileName"))
if mibBuilder.loadTexts: imageCrcCheckFailed.setStatus('current')
configurationLoadFailed = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0, 2)).setObjects(("PRVT-INTERWORKING-OS-MIB", "managementLoadTftpServerAddress"), ("PRVT-INTERWORKING-OS-MIB", "managementLoadFileName"))
if mibBuilder.loadTexts: configurationLoadFailed.setStatus('current')
unauthorizedAccessViaCLI = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0, 3))
if mibBuilder.loadTexts: unauthorizedAccessViaCLI.setStatus('current')
snmpSetExecuted = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0, 4)).setObjects(("SNMP-USER-BASED-SM-MIB", "usmUserSecurityName"))
if mibBuilder.loadTexts: snmpSetExecuted.setStatus('current')
managementOptionSupportChanged = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 111, 1, 0, 5)).setObjects(("PRVT-INTERWORKING-OS-MIB", "managementOptionSupportStatus"), ("PRVT-INTERWORKING-OS-MIB", "managementOptionSupportAddress"))
if mibBuilder.loadTexts: managementOptionSupportChanged.setStatus('current')
mibBuilder.exportSymbols("PRVT-INTERWORKING-OS-MIB", snmpSetExecuted=snmpSetExecuted, management=management, managementConnectivityIpAddress=managementConnectivityIpAddress, prvtBootUpgradeCmd=prvtBootUpgradeCmd, PYSNMP_MODULE_ID=prvtInterworkOsMib, managementConnectivityIPNetMask=managementConnectivityIPNetMask, prvtBootApplicationNameURI=prvtBootApplicationNameURI, cpuRedundancy=cpuRedundancy, managementOptionSupportL3Capable=managementOptionSupportL3Capable, cpuStatus=cpuStatus, version=version, managementOptionSupportStatus=managementOptionSupportStatus, cpuName=cpuName, managementConnectivityMACAddr=managementConnectivityMACAddr, prvtBootConfigUpgrade=prvtBootConfigUpgrade, bootVersionNumber=bootVersionNumber, managementLoadExecuteStatus=managementLoadExecuteStatus, managementLicense=managementLicense, appletVersionNumber=appletVersionNumber, cpuMonitoring=cpuMonitoring, oSversionDate=oSversionDate, managementMiscSaveToNvm=managementMiscSaveToNvm, managementOptionSupportAddress=managementOptionSupportAddress, managementMiscReload=managementMiscReload, managementIPGateAddress=managementIPGateAddress, managementLoadTftpServerAddress=managementLoadTftpServerAddress, cpuMonitoringUtilization=cpuMonitoringUtilization, managementMiscReloadAtTime=managementMiscReloadAtTime, cpuRedundancyTable=cpuRedundancyTable, cpuId=cpuId, cpuSWVersionString=cpuSWVersionString, managementMiscReset=managementMiscReset, cpuHW=cpuHW, managementOptionSupportKey=managementOptionSupportKey, prvtInterworkOsMib=prvtInterworkOsMib, managementLoadFileName=managementLoadFileName, imageCrcCheckFailed=imageCrcCheckFailed, appletVersionDate=appletVersionDate, cpuMonitoringStatus=cpuMonitoringStatus, managementMiscReloadInTime=managementMiscReloadInTime, prvtBootConfigURI=prvtBootConfigURI, cpuHwRedundancySupport=cpuHwRedundancySupport, managementLoadExecute=managementLoadExecute, managementMisc=managementMisc, prvtBootErrorCondition=prvtBootErrorCondition, oSversionString=oSversionString, cpu=cpu, managementMiscReloadSaveAtTime=managementMiscReloadSaveAtTime, cpuRedundancyEntry=cpuRedundancyEntry, managementOptionSupportChanged=managementOptionSupportChanged, prvtInterworkOsConformance=prvtInterworkOsConformance, optionInstalled=optionInstalled, managementLoadType=managementLoadType, cpuRAMsize=cpuRAMsize, unauthorizedAccessViaCLI=unauthorizedAccessViaCLI, managementSerialBaud=managementSerialBaud, prvtBootOperStatus=prvtBootOperStatus, managementMiscReloadSaveInTime=managementMiscReloadSaveInTime, prvtBootUpgradeSrcURI=prvtBootUpgradeSrcURI, bootVersionDate=bootVersionDate, configurationLoadFailed=configurationLoadFailed, prvtInterworkOsNotifications=prvtInterworkOsNotifications, cpuRedundancySupport=cpuRedundancySupport, managementConnectivity=managementConnectivity, option=option, managementLoad=managementLoad, oSversionNumber=oSversionNumber, bootVersionString=bootVersionString, software=software)
