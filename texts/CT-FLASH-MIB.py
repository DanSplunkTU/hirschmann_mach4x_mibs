#
# PySNMP MIB module CT-FLASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FLASH-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:06 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ctFlash, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFlash")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, ObjectIdentity, IpAddress, Gauge32, MibIdentifier, TimeTicks, iso, Unsigned32, Integer32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier", "TimeTicks", "iso", "Unsigned32", "Integer32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
flashStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1))
flashFile = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2))
flashCmd = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3))
flashVolumeStatusTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1), )
if mibBuilder.loadTexts: flashVolumeStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: flashVolumeStatusTable.setDescription('This table contains status information on each flash volume.')
flashVolumeStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1), ).setIndexNames((0, "CT-FLASH-MIB", "flashVolume"))
if mibBuilder.loadTexts: flashVolumeStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: flashVolumeStatusEntry.setDescription('Information on a particular volume.')
flashVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashVolume.setStatus('mandatory')
if mibBuilder.loadTexts: flashVolume.setDescription('Uniquely defines a volume.')
flashVolFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashVolFiles.setStatus('mandatory')
if mibBuilder.loadTexts: flashVolFiles.setDescription('The flash filing system status contains the number of\n                files currently in the volume.')
flashVolSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashVolSpace.setStatus('mandatory')
if mibBuilder.loadTexts: flashVolSpace.setDescription('This object returns the approximate amount of remaining \n                  storage space, in bytes, in the flash filing system.')
flashFileTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1), )
if mibBuilder.loadTexts: flashFileTable.setStatus('mandatory')
if mibBuilder.loadTexts: flashFileTable.setDescription('Describes each file in a flash file system volume.')
flashFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1), ).setIndexNames((0, "CT-FLASH-MIB", "flashVolume"), (0, "CT-FLASH-MIB", "flashFileID"))
if mibBuilder.loadTexts: flashFileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: flashFileEntry.setDescription('Describes a particular file.')
flashFileID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFileID.setStatus('mandatory')
if mibBuilder.loadTexts: flashFileID.setDescription('This object contains a volume-unique file id associated with\n                each file.')
flashFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFilename.setStatus('mandatory')
if mibBuilder.loadTexts: flashFilename.setDescription('This object contains the filename of the current file.')
flashFileVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFileVersion.setStatus('mandatory')
if mibBuilder.loadTexts: flashFileVersion.setDescription("This object contains the file version number of the current\n                  file in the form 'XX.XX.XX', where 'X' is in the range 0-9.")
flashFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("intelHex", 1), ("intelHexCompressed", 2), ("iEEE695", 3), ("eLF", 4), ("table", 5), ("dLL", 6), ("bOOT", 7), ("binary", 8), ("binaryCompressed", 9), ("taggedData", 10), ("package", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFileType.setStatus('mandatory')
if mibBuilder.loadTexts: flashFileType.setDescription('This object contains the file type defined for the file.')
flashFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFileSize.setStatus('mandatory')
if mibBuilder.loadTexts: flashFileSize.setDescription('This object contains the size, in bytes, currently allocated\n                  to the file.')
flashCmdPath = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdPath.setStatus('mandatory')
if mibBuilder.loadTexts: flashCmdPath.setDescription('Filename requested of the server for a TFTP download\n                or upload.')
flashCmdNetAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdNetAddress.setStatus('mandatory')
if mibBuilder.loadTexts: flashCmdNetAddress.setDescription('IP address of the TFTP server to use with a flash file\n                download or upload operation. If an IP address is not\n                specified, the operation will default to the IP address\n                 associated with the runtime TFTP download.')
flashCmdVolume = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdVolume.setStatus('mandatory')
if mibBuilder.loadTexts: flashCmdVolume.setDescription('Flash volume to contain the file created during a\n                download operation.')
flashCmdOperation = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("install", 1), ("download", 2), ("upload", 3), ("cleanup", 4), ("delete", 5), ("none", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdOperation.setStatus('mandatory')
if mibBuilder.loadTexts: flashCmdOperation.setDescription('Operation to perform on the specified flash file.\n                Download and upload operations require that the network.\n                pathname, filename, version, type, and volume be specified.\n                Cleanup does not require any additional information.')
flashCmdStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("idle", 1), ("other", 2), ("flashVerifyServer", 3), ("flashCleanup", 4), ("downLoadActive", 5), ("upLoadActive", 6), ("completeError", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashCmdStatus.setStatus('mandatory')
if mibBuilder.loadTexts: flashCmdStatus.setDescription('Status of the download or upload operation. The idle(1)\n                status indicates no operation is in progress. The \n                downLoadActive(3) or upLoadActive(4) indicate a file \n                transfer in progress. The completeError(5) status indicates\n                that a file transfer was started but an error was detected.')
flashCmdError = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("oK", 1), ("deleteFailed", 2), ("fileSystem", 3), ("tFTPerror", 4), ("corruptFile", 5), ("dupFlashName", 6), ("noFlashFile", 7), ("flashAlloc", 8), ("maxFiles", 9), ("invalidName", 10), ("protocolErr", 11), ("serverLost", 12), ("noNetFile", 13), ("noNetAccess", 14), ("netDiskFull", 15), ("dupNetFile", 16), ("parseError", 17), ("invalidType", 18), ("invalidCmd", 19), ("invalidModId", 20), ("noServerIP", 21), ("socketError", 22), ("blockSequence", 23), ("bufferError", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashCmdError.setStatus('mandatory')
if mibBuilder.loadTexts: flashCmdError.setDescription('If the value of flashCmdStatus is completeError(5), then\n                this object describes the nature of the error.')
flashCmdFile = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdFile.setStatus('mandatory')
if mibBuilder.loadTexts: flashCmdFile.setDescription('Flash filename to perform the specified operation.')
flashCmdVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdVersion.setStatus('mandatory')
if mibBuilder.loadTexts: flashCmdVersion.setDescription("Flash file version to perform the specified operation\n                in the form 'XX.XX.XX' where 'X' is in the range 0-9.")
flashCmdType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("intelHex", 1), ("intelHexCompressed", 2), ("iEEE695", 3), ("eLF", 4), ("table", 5), ("dLL", 6), ("bOOT", 7), ("binary", 8), ("binaryCompressed", 9), ("taggedData", 10), ("package", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdType.setStatus('mandatory')
if mibBuilder.loadTexts: flashCmdType.setDescription('File type to specify with a flash file created during\n                a download operation.')
flashCmdSize = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdSize.setStatus('mandatory')
if mibBuilder.loadTexts: flashCmdSize.setDescription('Size of the download file. This value allows the flash\n                filing system to initialize an appropriate amount of \n                flash memory prior to the TFTP transfer, preventing a\n                time-out condition during a transfer.')
flashBlockCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashBlockCount.setStatus('mandatory')
if mibBuilder.loadTexts: flashBlockCount.setDescription('Current TFTP block count of an active session. If no\n                TFTP transfer is in progress, zero is returned.')
mibBuilder.exportSymbols("CT-FLASH-MIB", flashCmdOperation=flashCmdOperation, flashCmdVersion=flashCmdVersion, flashVolumeStatusTable=flashVolumeStatusTable, flashCmdFile=flashCmdFile, flashCmdVolume=flashCmdVolume, flashCmdPath=flashCmdPath, flashVolSpace=flashVolSpace, flashCmdStatus=flashCmdStatus, flashVolume=flashVolume, flashCmdNetAddress=flashCmdNetAddress, flashCmdSize=flashCmdSize, flashVolumeStatusEntry=flashVolumeStatusEntry, flashFileID=flashFileID, flashFileSize=flashFileSize, flashVolFiles=flashVolFiles, flashCmdError=flashCmdError, flashFilename=flashFilename, flashCmd=flashCmd, flashBlockCount=flashBlockCount, flashFileType=flashFileType, flashStatus=flashStatus, flashFileTable=flashFileTable, flashFile=flashFile, flashFileVersion=flashFileVersion, flashCmdType=flashCmdType, flashFileEntry=flashFileEntry)
