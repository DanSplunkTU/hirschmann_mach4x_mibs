#
# PySNMP MIB module CT-FLASH-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CT-FLASH-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:16 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
ctFlash, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctFlash")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity, Counter32, NotificationType, Unsigned32, Integer32, iso, TimeTicks, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "Unsigned32", "Integer32", "iso", "TimeTicks", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
flashStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1))
flashFile = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2))
flashCmd = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3))
flashVolumeStatusTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1), )
if mibBuilder.loadTexts: flashVolumeStatusTable.setStatus('mandatory')
flashVolumeStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1), ).setIndexNames((0, "CT-FLASH-MIB", "flashVolume"))
if mibBuilder.loadTexts: flashVolumeStatusEntry.setStatus('mandatory')
flashVolume = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashVolume.setStatus('mandatory')
flashVolFiles = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashVolFiles.setStatus('mandatory')
flashVolSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashVolSpace.setStatus('mandatory')
flashFileTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1), )
if mibBuilder.loadTexts: flashFileTable.setStatus('mandatory')
flashFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1), ).setIndexNames((0, "CT-FLASH-MIB", "flashVolume"), (0, "CT-FLASH-MIB", "flashFileID"))
if mibBuilder.loadTexts: flashFileEntry.setStatus('mandatory')
flashFileID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFileID.setStatus('mandatory')
flashFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFilename.setStatus('mandatory')
flashFileVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFileVersion.setStatus('mandatory')
flashFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("intelHex", 1), ("intelHexCompressed", 2), ("iEEE695", 3), ("eLF", 4), ("table", 5), ("dLL", 6), ("bOOT", 7), ("binary", 8), ("binaryCompressed", 9), ("taggedData", 10), ("package", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFileType.setStatus('mandatory')
flashFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashFileSize.setStatus('mandatory')
flashCmdPath = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdPath.setStatus('mandatory')
flashCmdNetAddress = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdNetAddress.setStatus('mandatory')
flashCmdVolume = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdVolume.setStatus('mandatory')
flashCmdOperation = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("install", 1), ("download", 2), ("upload", 3), ("cleanup", 4), ("delete", 5), ("none", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdOperation.setStatus('mandatory')
flashCmdStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("idle", 1), ("other", 2), ("flashVerifyServer", 3), ("flashCleanup", 4), ("downLoadActive", 5), ("upLoadActive", 6), ("completeError", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashCmdStatus.setStatus('mandatory')
flashCmdError = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))).clone(namedValues=NamedValues(("oK", 1), ("deleteFailed", 2), ("fileSystem", 3), ("tFTPerror", 4), ("corruptFile", 5), ("dupFlashName", 6), ("noFlashFile", 7), ("flashAlloc", 8), ("maxFiles", 9), ("invalidName", 10), ("protocolErr", 11), ("serverLost", 12), ("noNetFile", 13), ("noNetAccess", 14), ("netDiskFull", 15), ("dupNetFile", 16), ("parseError", 17), ("invalidType", 18), ("invalidCmd", 19), ("invalidModId", 20), ("noServerIP", 21), ("socketError", 22), ("blockSequence", 23), ("bufferError", 24)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashCmdError.setStatus('mandatory')
flashCmdFile = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdFile.setStatus('mandatory')
flashCmdVersion = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdVersion.setStatus('mandatory')
flashCmdType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("intelHex", 1), ("intelHexCompressed", 2), ("iEEE695", 3), ("eLF", 4), ("table", 5), ("dLL", 6), ("bOOT", 7), ("binary", 8), ("binaryCompressed", 9), ("taggedData", 10), ("package", 11)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdType.setStatus('mandatory')
flashCmdSize = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: flashCmdSize.setStatus('mandatory')
flashBlockCount = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10, 3, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: flashBlockCount.setStatus('mandatory')
mibBuilder.exportSymbols("CT-FLASH-MIB", flashCmdType=flashCmdType, flashFileID=flashFileID, flashVolumeStatusTable=flashVolumeStatusTable, flashCmd=flashCmd, flashCmdVolume=flashCmdVolume, flashBlockCount=flashBlockCount, flashFileVersion=flashFileVersion, flashVolume=flashVolume, flashFileEntry=flashFileEntry, flashStatus=flashStatus, flashCmdPath=flashCmdPath, flashFileType=flashFileType, flashVolSpace=flashVolSpace, flashVolFiles=flashVolFiles, flashCmdVersion=flashCmdVersion, flashCmdSize=flashCmdSize, flashCmdNetAddress=flashCmdNetAddress, flashCmdStatus=flashCmdStatus, flashCmdError=flashCmdError, flashVolumeStatusEntry=flashVolumeStatusEntry, flashCmdFile=flashCmdFile, flashFile=flashFile, flashFilename=flashFilename, flashFileTable=flashFileTable, flashCmdOperation=flashCmdOperation, flashFileSize=flashFileSize)
