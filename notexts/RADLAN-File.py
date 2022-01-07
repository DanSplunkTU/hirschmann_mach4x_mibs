#
# PySNMP MIB module RADLAN-File (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltex/RADLAN-FILE
# Produced by pysmi-1.1.8 at Fri Jan  7 16:19:58 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, ObjectIdentity, Counter32, iso, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, IpAddress, Integer32, TimeTicks, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Counter32", "iso", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "IpAddress", "Integer32", "TimeTicks", "Counter64", "Gauge32")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
rlFile = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 96))
rlFile.setRevisions(('2013-04-01 00:00',))
if mibBuilder.loadTexts: rlFile.setLastUpdated('201304010000Z')
if mibBuilder.loadTexts: rlFile.setOrganization('Marvell Semiconductor, Inc.')
class FilePermission(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("read", 0), ("write", 1), ("execute", 2), ("dir", 3))

rlFileMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileMibVersion.setStatus('current')
rlFileTable = MibTable((1, 3, 6, 1, 4, 1, 89, 96, 2), )
if mibBuilder.loadTexts: rlFileTable.setStatus('current')
rlFileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 96, 2, 1), ).setIndexNames((1, "RADLAN-File", "rlFileName"))
if mibBuilder.loadTexts: rlFileEntry.setStatus('current')
rlFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileName.setStatus('current')
rlFilePermission = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 2), FilePermission()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFilePermission.setStatus('current')
rlFileSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileSize.setStatus('current')
rlFileModificationDate = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileModificationDate.setStatus('current')
rlFileModificationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileModificationTime.setStatus('current')
rlFileRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileRowStatus.setStatus('current')
rlFileFlashSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFlashSize.setStatus('current')
rlFileFullNormalizedName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 2, 1, 8), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFullNormalizedName.setStatus('current')
rlFileActionTable = MibTable((1, 3, 6, 1, 4, 1, 89, 96, 3), )
if mibBuilder.loadTexts: rlFileActionTable.setStatus('current')
rlFileActionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 96, 3, 1), ).setIndexNames((0, "RADLAN-File", "rlFileActionName"))
if mibBuilder.loadTexts: rlFileActionEntry.setStatus('current')
rlFileActionName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionName.setStatus('current')
rlFileActionNewName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 160))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionNewName.setStatus('current')
rlFileActionRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionRowStatus.setStatus('current')
rlFileActionCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 96, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("rename", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileActionCommand.setStatus('current')
rlFileTotalSizeOfFlash = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileTotalSizeOfFlash.setStatus('current')
rlFileFreeSizeOfFlash = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFreeSizeOfFlash.setStatus('current')
rlFileAuditingEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlFileAuditingEnable.setStatus('current')
rlFileTotalSizeOfUSB = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileTotalSizeOfUSB.setStatus('current')
rlFileFreeSizeOfUSB = MibScalar((1, 3, 6, 1, 4, 1, 89, 96, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlFileFreeSizeOfUSB.setStatus('current')
mibBuilder.exportSymbols("RADLAN-File", rlFileFreeSizeOfFlash=rlFileFreeSizeOfFlash, rlFileFullNormalizedName=rlFileFullNormalizedName, rlFileAuditingEnable=rlFileAuditingEnable, rlFilePermission=rlFilePermission, rlFileActionNewName=rlFileActionNewName, rlFile=rlFile, FilePermission=FilePermission, rlFileModificationDate=rlFileModificationDate, rlFileTotalSizeOfFlash=rlFileTotalSizeOfFlash, rlFileName=rlFileName, rlFileActionRowStatus=rlFileActionRowStatus, rlFileActionName=rlFileActionName, rlFileFlashSize=rlFileFlashSize, rlFileSize=rlFileSize, rlFileEntry=rlFileEntry, PYSNMP_MODULE_ID=rlFile, rlFileRowStatus=rlFileRowStatus, rlFileTable=rlFileTable, rlFileMibVersion=rlFileMibVersion, rlFileModificationTime=rlFileModificationTime, rlFileActionEntry=rlFileActionEntry, rlFileActionCommand=rlFileActionCommand, rlFileActionTable=rlFileActionTable, rlFileFreeSizeOfUSB=rlFileFreeSizeOfUSB, rlFileTotalSizeOfUSB=rlFileTotalSizeOfUSB)
