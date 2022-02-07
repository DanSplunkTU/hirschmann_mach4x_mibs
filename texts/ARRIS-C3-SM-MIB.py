#
# PySNMP MIB module ARRIS-C3-SM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-C3-SM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:39 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
cmtsC3, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsC3")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, Gauge32, Counter64, Bits, ModuleIdentity, MibIdentifier, NotificationType, iso, TimeTicks, Integer32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "Gauge32", "Counter64", "Bits", "ModuleIdentity", "MibIdentifier", "NotificationType", "iso", "TimeTicks", "Integer32", "enterprises")
TruthValue, DisplayString, DateAndTime, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "DateAndTime", "TextualConvention")
cmtsC3SMMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4))
if mibBuilder.loadTexts: cmtsC3SMMIB.setLastUpdated('200311250000Z')
if mibBuilder.loadTexts: cmtsC3SMMIB.setOrganization('Arris International')
if mibBuilder.loadTexts: cmtsC3SMMIB.setContactInfo('   Network Management\n                Postal: Arris International.\n                        4400 Cork Airport Business Park\n                        Cork Airport, Kinsale Road\n                        Cork, Ireland.\n                Tel:    +353 21 7305 800\n                Fax:    +353 21 4321 972')
if mibBuilder.loadTexts: cmtsC3SMMIB.setDescription('This MIB manages the System Manager\n            software on the Arris CMTS C3')
dcxSMObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1))
dcxSMBootGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1))
dcxSMBootDevice = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("nfs", 1), ("tftp", 2), ("ftp", 3), ("diskAlternative", 4), ("diskCurrent", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMBootDevice.setStatus('current')
if mibBuilder.loadTexts: dcxSMBootDevice.setDescription('Specify device CMTS will by default boot from')
dcxSMBootHostname = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMBootHostname.setStatus('current')
if mibBuilder.loadTexts: dcxSMBootHostname.setDescription('Ip address of tftp, nfs, ftp server,\n            ignored when booting from flash disk')
dcxSMBootUsername = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMBootUsername.setStatus('current')
if mibBuilder.loadTexts: dcxSMBootUsername.setDescription('User name for tftp, ftp, nfs server,\n                ignored when booting from flash disk')
dcxSMBootPassword = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMBootPassword.setStatus('current')
if mibBuilder.loadTexts: dcxSMBootPassword.setDescription('User password for tftp, ftp, nfs server,\n            ignored when booting from flash disk')
dcxSMBootPath = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMBootPath.setStatus('current')
if mibBuilder.loadTexts: dcxSMBootPath.setDescription('Boot path for image file on tftp,\n            ftp, nfs server, ignored when \n            booting from flash disk')
dcxSMEnetMgmtInterface = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("outOfBand", 0), ("inBand", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMEnetMgmtInterface.setStatus('current')
if mibBuilder.loadTexts: dcxSMEnetMgmtInterface.setDescription('Specify Cmts management interface')
dcxSMRebootAction = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("nil", 1), ("rebootNow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMRebootAction.setStatus('current')
if mibBuilder.loadTexts: dcxSMRebootAction.setDescription('Force a reboot of the CMTS')
dcxSMConfigFileBootGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2))
dcxSMConfigFileBootDevice = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("nfs", 1), ("tftp", 2), ("ftp", 3), ("diskAlternative", 4), ("diskCurrent", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMConfigFileBootDevice.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileBootDevice.setDescription("Specify device from which CMTS\n            will read it's configuration")
dcxSMConfigFileBootHostname = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMConfigFileBootHostname.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileBootHostname.setDescription('Ip address of tftp, nfs, ftp server, \n            ignored when using flash disk')
dcxSMConfigFileBootUsername = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMConfigFileBootUsername.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileBootUsername.setDescription('User name for tftp, ftp server,\n            ignored when using flash disk')
dcxSMConfigFileBootPassword = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMConfigFileBootPassword.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileBootPassword.setDescription('User password for tftp, ftp server,\n            ignored when using flash disk')
dcxSMConfigFileBootPath = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 2, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMConfigFileBootPath.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileBootPath.setDescription('Boot path for image file on tftp,\n            ftp server, ignored when using flash disk')
dcxSMDownloadGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3))
dcxSMDownloadDevice = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nfs", 1), ("tftp", 2), ("ftp", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMDownloadDevice.setStatus('current')
if mibBuilder.loadTexts: dcxSMDownloadDevice.setDescription('Specify device CMTS will by download from')
dcxSMDownloadHostname = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMDownloadHostname.setStatus('current')
if mibBuilder.loadTexts: dcxSMDownloadHostname.setDescription('download ip address')
dcxSMDownloadUsername = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMDownloadUsername.setStatus('current')
if mibBuilder.loadTexts: dcxSMDownloadUsername.setDescription('download user name')
dcxSMDownloadPassword = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMDownloadPassword.setStatus('current')
if mibBuilder.loadTexts: dcxSMDownloadPassword.setDescription('download user password')
dcxSMDownloadPath = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMDownloadPath.setStatus('current')
if mibBuilder.loadTexts: dcxSMDownloadPath.setDescription('Boot path for image file on tftp, ftp')
dcxSMDownloadControl = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("abort", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMDownloadControl.setStatus('current')
if mibBuilder.loadTexts: dcxSMDownloadControl.setDescription('Begin downloading by setting to start(1)\n            abort a current download with abort(2)\n            downloaded image will not become active\n            until it made current in the softwareList\n            group')
dcxSMDownloadStatus = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("inprogress", 2), ("finished", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxSMDownloadStatus.setStatus('current')
if mibBuilder.loadTexts: dcxSMDownloadStatus.setDescription('none(1) indicates no images has been downloaded\n            since the CMTS rebooted, inprogress indicates there\n            is an active download occuring, finished(3) indicates\n            the download is complete and may be activated in the\n            SoftwareList group')
dcxSMTrapGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4))
dcxSMDiskInserted = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 1)).setObjects(("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion"))
if mibBuilder.loadTexts: dcxSMDiskInserted.setStatus('current')
if mibBuilder.loadTexts: dcxSMDiskInserted.setDescription('disk inserted. Severity is WARNING')
dcxSMDiskRemoved = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 2)).setObjects(("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion"))
if mibBuilder.loadTexts: dcxSMDiskRemoved.setStatus('current')
if mibBuilder.loadTexts: dcxSMDiskRemoved.setDescription('disk removed. Severity is ERROR.')
dcxSMDiskFailed = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 3)).setObjects(("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion"))
if mibBuilder.loadTexts: dcxSMDiskFailed.setStatus('current')
if mibBuilder.loadTexts: dcxSMDiskFailed.setDescription('disk failed. Severity is ERROR.')
dcxSMConfigChecksumChanged = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 4)).setObjects(("ARRIS-C3-SM-MIB", "dcxSMConfigFileDesc"))
if mibBuilder.loadTexts: dcxSMConfigChecksumChanged.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigChecksumChanged.setDescription('Config file checksum is different compared to the \n            config file used to initialize the cmts. Severity\n                is WARNING.')
dcxSMImageChecksumChanged = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 5)).setObjects(("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion"))
if mibBuilder.loadTexts: dcxSMImageChecksumChanged.setStatus('current')
if mibBuilder.loadTexts: dcxSMImageChecksumChanged.setDescription('Config image checksum is different compared to the\n            image used to boot the cmts. Severity is WARNING.')
dcxSMImageDownloadFailed = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 6)).setObjects(("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion"))
if mibBuilder.loadTexts: dcxSMImageDownloadFailed.setStatus('current')
if mibBuilder.loadTexts: dcxSMImageDownloadFailed.setDescription('An error occured while downloading the image file.\n            Severity is ERROR.')
dcxSMImageBootFailed = NotificationType((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 4, 7)).setObjects(("ARRIS-C3-SM-MIB", "dcxSMSoftwareVersion"))
if mibBuilder.loadTexts: dcxSMImageBootFailed.setStatus('current')
if mibBuilder.loadTexts: dcxSMImageBootFailed.setDescription('An error occured while booting.\n            Severity is ERROR.')
dcxSMConfigFileGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5))
dcxSMConfigFileTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1), )
if mibBuilder.loadTexts: dcxSMConfigFileTable.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileTable.setDescription('Table of config files installed on CMTS flash disk')
dcxSMConfigFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1), ).setIndexNames((0, "ARRIS-C3-SM-MIB", "dcxSMConfigFileIndex"))
if mibBuilder.loadTexts: dcxSMConfigFileEntry.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileEntry.setDescription('.')
dcxSMConfigFileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: dcxSMConfigFileIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileIndex.setDescription('index')
dcxSMConfigFileDate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxSMConfigFileDate.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileDate.setDescription('Date Config file last modified')
dcxSMConfigFileDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMConfigFileDesc.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileDesc.setDescription('Description of config file')
dcxSMConfigFileChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxSMConfigFileChecksum.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileChecksum.setDescription('checksum')
dcxSMConfigFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxSMConfigFileSize.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileSize.setDescription('file size')
dcxSMConfigFileStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("curconfig", 1), ("alt", 2), ("inactive", 3), ("deleted", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMConfigFileStatus.setStatus('current')
if mibBuilder.loadTexts: dcxSMConfigFileStatus.setDescription('Status of config file may be currrent, alt or inactive\n            current -> alt allowed config files swapped\n            alt -> current allowed config files swapped\n            inactive -> current allowed config files swapped\n            inactive -> alt allowed config files swapped\n            current -> inactive not allowed\n            alt -> inactive not allowed\n            deleted -> inactive only change allowed on deleted\n            deleted files remain available until the cmts is rebooted')
dcxSMSoftwareListGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6))
dcxSMSoftwareListTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1), )
if mibBuilder.loadTexts: dcxSMSoftwareListTable.setStatus('current')
if mibBuilder.loadTexts: dcxSMSoftwareListTable.setDescription('Table of images installed on CMTS flash disk')
dcxSMSoftwareListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1), ).setIndexNames((0, "ARRIS-C3-SM-MIB", "dcxSMSoftwareIndex"))
if mibBuilder.loadTexts: dcxSMSoftwareListEntry.setStatus('current')
if mibBuilder.loadTexts: dcxSMSoftwareListEntry.setDescription('.')
dcxSMSoftwareIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: dcxSMSoftwareIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSMSoftwareIndex.setDescription('image index')
dcxSMSoftwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxSMSoftwareVersion.setStatus('current')
if mibBuilder.loadTexts: dcxSMSoftwareVersion.setDescription('image version')
dcxSMSoftwareDate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxSMSoftwareDate.setStatus('current')
if mibBuilder.loadTexts: dcxSMSoftwareDate.setDescription('Date image created')
dcxSMSoftwareDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMSoftwareDesc.setStatus('current')
if mibBuilder.loadTexts: dcxSMSoftwareDesc.setDescription('Description of image')
dcxSMSoftwareChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxSMSoftwareChecksum.setStatus('current')
if mibBuilder.loadTexts: dcxSMSoftwareChecksum.setDescription('checksum')
dcxSMSoftwareSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxSMSoftwareSize.setStatus('current')
if mibBuilder.loadTexts: dcxSMSoftwareSize.setDescription('file size')
dcxSMSoftwareStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("curimage", 1), ("alt", 2), ("inactive", 3), ("deleted", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMSoftwareStatus.setStatus('current')
if mibBuilder.loadTexts: dcxSMSoftwareStatus.setDescription('Status of software may be currrent, alt or inactive\n            current -> alt allowed software swapped\n            alt -> current allowed software swapped\n            inactive -> current allowed config files swapped\n            inactive -> alt allowed softwares swapped\n            current -> inactive not allowed\n            alt -> inactive not allowed\n            deleted -> inactive only change allowed on deleted\n            deleted files remain available until the cmts is rebooted')
dcxSMMiscUserManagementGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7))
dcxSMMiscUserTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1), )
if mibBuilder.loadTexts: dcxSMMiscUserTable.setStatus('current')
if mibBuilder.loadTexts: dcxSMMiscUserTable.setDescription('Table of CLI accounts')
dcxSMMiscUserListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1), ).setIndexNames((0, "ARRIS-C3-SM-MIB", "dcxSMMiscUserIndex"))
if mibBuilder.loadTexts: dcxSMMiscUserListEntry.setStatus('current')
if mibBuilder.loadTexts: dcxSMMiscUserListEntry.setDescription('.')
dcxSMMiscUserIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 5)))
if mibBuilder.loadTexts: dcxSMMiscUserIndex.setStatus('current')
if mibBuilder.loadTexts: dcxSMMiscUserIndex.setDescription('user index')
dcxSMMiscUserLoginName = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMMiscUserLoginName.setStatus('current')
if mibBuilder.loadTexts: dcxSMMiscUserLoginName.setDescription('Login user name')
dcxSMMiscUserLoginPwd = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMMiscUserLoginPwd.setStatus('current')
if mibBuilder.loadTexts: dcxSMMiscUserLoginPwd.setDescription('Login user password')
dcxSMMiscUserEnablePwd = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMMiscUserEnablePwd.setStatus('current')
if mibBuilder.loadTexts: dcxSMMiscUserEnablePwd.setDescription('Login user name password to enter priviledged mode')
dcxSMMiscUserEnableSecretePwd = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMMiscUserEnableSecretePwd.setStatus('current')
if mibBuilder.loadTexts: dcxSMMiscUserEnableSecretePwd.setDescription('Login user enable secret password to enter priviledged mode')
dcxSMMiscUserWorkMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 7, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("usermode", 1), ("priviledgedmode", 2), ("globalconfiguremode", 3), ("lineconfmode", 4), ("ethernetconfmode", 5), ("cableconfmode", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxSMMiscUserWorkMode.setStatus('current')
if mibBuilder.loadTexts: dcxSMMiscUserWorkMode.setDescription('Login user config mode')
dcxIpdrGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 8))
dcxIpdrEnable = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 8, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxIpdrEnable.setStatus('current')
if mibBuilder.loadTexts: dcxIpdrEnable.setDescription('Enable or disable Ipdr')
dcxIpdrFileName = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 8, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxIpdrFileName.setStatus('current')
if mibBuilder.loadTexts: dcxIpdrFileName.setDescription('Ipdr file name on the ftp server. Can not be changed\n                while the collection system is retrieving or deleting\n                the exisiting file or if the CMTS is building the current\n                Ipdr file.')
dcxIpdrUserLoginName = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 8, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxIpdrUserLoginName.setStatus('current')
if mibBuilder.loadTexts: dcxIpdrUserLoginName.setDescription("Ftp server login name for accessing Ipdr file. If\n            set to 'anonymous', any non-zero length password\n            will be accepted.")
dcxIpdrUserLoginPwd = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 1, 8, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxIpdrUserLoginPwd.setStatus('current')
if mibBuilder.loadTexts: dcxIpdrUserLoginPwd.setDescription("Ftp server login password for accessing Ipdr file.\n            If dcxIpdrUserLoginName is 'anonymous', any non-zero\n            length password will be accepted.")
dcxDxmObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2))
dcxDxmStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1))
dcxDxmStatusIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxDxmStatusIpAddress.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusIpAddress.setDescription('Specifies the IP address of the DoxMonitor managing this DoxController')
dcxDxmStatusPort = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxDxmStatusPort.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusPort.setDescription('Specifies the TCP/UDP Port us to connect to the appropriate DoxMonitor')
dcxDxmStatusEnable = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxDxmStatusEnable.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusEnable.setDescription('Specifies whether the DoxController should register with the specified DoxMonitor')
dcxDxmStatusCmtsId = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusCmtsId.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusCmtsId.setDescription('Specifies whether the DoxController should register with the specified DoxMonitor')
dcxDxmStatusRole = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("primary", 2), ("standby", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusRole.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusRole.setDescription("describes the DoxController's role in the DoxMonitor redundancy cluster, it is\n             a Primary or Standby CMTS")
dcxDxmStatusState = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("standalone", 1), ("active", 2), ("inactive", 3), ("passive", 4), ("restored", 5), ("failed", 6), ("replacement", 7), ("restoring", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusState.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusState.setDescription('Specifies the current state of the DoxController')
dcxDxmStatusLastConfigRetrieval = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusLastConfigRetrieval.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusLastConfigRetrieval.setDescription('Specifies when the startup-configuration was last retrieved from this DoxController')
dcxDxmStatusLastConfigChange = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 8), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusLastConfigChange.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusLastConfigChange.setDescription('Specifies when the startup-configuration was last changed on this DoxController')
dcxDxmStatusConfigRetrievalCount = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusConfigRetrievalCount.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusConfigRetrievalCount.setDescription('The total number of times the DoxController has responded to a Config Retrieval Request')
dcxDxmStatusHeartbeatCount = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusHeartbeatCount.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusHeartbeatCount.setDescription('The total number of times the DoxController has responded to a Heartbeat Request')
dcxDxmStatusNotifAddCmCount = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusNotifAddCmCount.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusNotifAddCmCount.setDescription('The total number of times the DoxController has generated an AddCableModem Notification')
dcxDxmStatusNotifDelCmCount = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusNotifDelCmCount.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusNotifDelCmCount.setDescription('The total number of times the DoxController has generated an DeleteCableModem Notification')
dcxDxmStatusNotifAddCpeCount = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusNotifAddCpeCount.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusNotifAddCpeCount.setDescription('The total number of times the DoxController has generated an AddCpe Notification')
dcxDxmStatusNotifDelCpeCount = MibScalar((1, 3, 6, 1, 4, 1, 4115, 1, 4, 3, 4, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxDxmStatusNotifDelCpeCount.setStatus('current')
if mibBuilder.loadTexts: dcxDxmStatusNotifDelCpeCount.setDescription('The total number of times the DoxController has generated a DeleteCpe Notification')
mibBuilder.exportSymbols("ARRIS-C3-SM-MIB", dcxSMRebootAction=dcxSMRebootAction, dcxSMConfigFileBootHostname=dcxSMConfigFileBootHostname, dcxSMImageDownloadFailed=dcxSMImageDownloadFailed, dcxSMConfigFileDesc=dcxSMConfigFileDesc, dcxSMDownloadUsername=dcxSMDownloadUsername, dcxSMMiscUserManagementGroup=dcxSMMiscUserManagementGroup, dcxSMMiscUserWorkMode=dcxSMMiscUserWorkMode, dcxSMSoftwareChecksum=dcxSMSoftwareChecksum, dcxSMConfigFileBootGroup=dcxSMConfigFileBootGroup, dcxSMDownloadPassword=dcxSMDownloadPassword, dcxSMMiscUserLoginName=dcxSMMiscUserLoginName, dcxSMConfigFileBootDevice=dcxSMConfigFileBootDevice, dcxSMImageBootFailed=dcxSMImageBootFailed, dcxIpdrUserLoginPwd=dcxIpdrUserLoginPwd, dcxSMConfigFileIndex=dcxSMConfigFileIndex, dcxSMSoftwareListEntry=dcxSMSoftwareListEntry, dcxDxmStatusRole=dcxDxmStatusRole, dcxSMSoftwareIndex=dcxSMSoftwareIndex, dcxSMDownloadPath=dcxSMDownloadPath, dcxSMSoftwareDesc=dcxSMSoftwareDesc, dcxSMImageChecksumChanged=dcxSMImageChecksumChanged, dcxDxmStatusNotifDelCpeCount=dcxDxmStatusNotifDelCpeCount, dcxSMBootPath=dcxSMBootPath, dcxSMConfigFileBootPath=dcxSMConfigFileBootPath, dcxSMDownloadControl=dcxSMDownloadControl, dcxSMDownloadHostname=dcxSMDownloadHostname, dcxIpdrFileName=dcxIpdrFileName, dcxSMDownloadStatus=dcxSMDownloadStatus, cmtsC3SMMIB=cmtsC3SMMIB, dcxDxmStatusCmtsId=dcxDxmStatusCmtsId, dcxSMSoftwareStatus=dcxSMSoftwareStatus, dcxDxmStatusIpAddress=dcxDxmStatusIpAddress, dcxSMMiscUserEnableSecretePwd=dcxSMMiscUserEnableSecretePwd, dcxSMObjects=dcxSMObjects, dcxSMMiscUserIndex=dcxSMMiscUserIndex, dcxSMDownloadGroup=dcxSMDownloadGroup, dcxSMDiskFailed=dcxSMDiskFailed, dcxSMMiscUserEnablePwd=dcxSMMiscUserEnablePwd, dcxDxmStatusHeartbeatCount=dcxDxmStatusHeartbeatCount, dcxSMConfigFileBootUsername=dcxSMConfigFileBootUsername, dcxDxmObjects=dcxDxmObjects, dcxDxmStatusPort=dcxDxmStatusPort, dcxSMConfigFileGroup=dcxSMConfigFileGroup, dcxSMConfigFileBootPassword=dcxSMConfigFileBootPassword, dcxDxmStatusLastConfigChange=dcxDxmStatusLastConfigChange, dcxSMDiskInserted=dcxSMDiskInserted, dcxDxmStatusEnable=dcxDxmStatusEnable, dcxSMSoftwareDate=dcxSMSoftwareDate, dcxIpdrUserLoginName=dcxIpdrUserLoginName, dcxSMBootGroup=dcxSMBootGroup, dcxSMConfigChecksumChanged=dcxSMConfigChecksumChanged, dcxDxmStatusNotifAddCmCount=dcxDxmStatusNotifAddCmCount, dcxDxmStatusConfigRetrievalCount=dcxDxmStatusConfigRetrievalCount, dcxSMConfigFileChecksum=dcxSMConfigFileChecksum, dcxSMTrapGroup=dcxSMTrapGroup, dcxSMMiscUserLoginPwd=dcxSMMiscUserLoginPwd, dcxSMBootPassword=dcxSMBootPassword, dcxSMEnetMgmtInterface=dcxSMEnetMgmtInterface, dcxSMConfigFileSize=dcxSMConfigFileSize, dcxSMConfigFileTable=dcxSMConfigFileTable, dcxSMConfigFileStatus=dcxSMConfigFileStatus, dcxSMBootUsername=dcxSMBootUsername, dcxDxmStatusNotifDelCmCount=dcxDxmStatusNotifDelCmCount, dcxSMSoftwareSize=dcxSMSoftwareSize, dcxSMDownloadDevice=dcxSMDownloadDevice, dcxDxmStatusLastConfigRetrieval=dcxDxmStatusLastConfigRetrieval, dcxSMBootHostname=dcxSMBootHostname, dcxSMMiscUserListEntry=dcxSMMiscUserListEntry, dcxDxmStatusGroup=dcxDxmStatusGroup, dcxIpdrGroup=dcxIpdrGroup, dcxSMSoftwareListTable=dcxSMSoftwareListTable, dcxSMBootDevice=dcxSMBootDevice, dcxDxmStatusNotifAddCpeCount=dcxDxmStatusNotifAddCpeCount, dcxSMMiscUserTable=dcxSMMiscUserTable, dcxSMSoftwareVersion=dcxSMSoftwareVersion, dcxIpdrEnable=dcxIpdrEnable, dcxSMDiskRemoved=dcxSMDiskRemoved, dcxDxmStatusState=dcxDxmStatusState, dcxSMConfigFileDate=dcxSMConfigFileDate, dcxSMSoftwareListGroup=dcxSMSoftwareListGroup, PYSNMP_MODULE_ID=cmtsC3SMMIB, dcxSMConfigFileEntry=dcxSMConfigFileEntry)
