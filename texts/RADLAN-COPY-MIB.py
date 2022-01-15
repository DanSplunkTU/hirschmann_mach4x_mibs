#
# PySNMP MIB module RADLAN-COPY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-COPY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:17:50 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, Counter64, IpAddress, NotificationType, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, TimeTicks, Unsigned32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "Counter64", "IpAddress", "NotificationType", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "TimeTicks", "Unsigned32", "ModuleIdentity", "Bits")
RowStatus, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TruthValue", "TextualConvention")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlCopy = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 87))
rlCopy.setRevisions(('2006-02-02 00:00', '2003-09-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlCopy.setRevisionsDescriptions(('Added objects rlCopyMessagesTable and rlCopyMessagesTableRemoveEntries.', 'Initial version of this MIB.',))
if mibBuilder.loadTexts: rlCopy.setLastUpdated('200602020000Z')
if mibBuilder.loadTexts: rlCopy.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlCopy.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlCopy.setDescription('The private MIB module definition for file copy in Radlan devices.')
class RlCopyApplicationType(TextualConvention, Integer32):
    description = 'Specifies management application'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("mcli", 1), ("cli", 2), ("ewb", 3), ("nms", 4), ("initerm", 5), ("serial", 6))

class RlCopyLocationType(TextualConvention, Integer32):
    description = 'Specifies file location'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("local", 1), ("anotherUnit", 2), ("tftp", 3), ("xmodem", 4), ("scp", 5), ("serial", 6))

class RlCopyFileType(TextualConvention, Integer32):
    description = 'The File type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    namedValues = NamedValues(("other", 1), ("runningConfig", 2), ("startupConfig", 3), ("backupConfig", 4), ("runningMibConfig", 5), ("startupMibConfig", 6), ("backupMibConfig", 7), ("image", 8), ("boot", 9), ("null", 10))

rlCopyMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 87, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyMibVersion.setStatus('current')
if mibBuilder.loadTexts: rlCopyMibVersion.setDescription('Indicates the Copy support version. The current version is 1.')
rlCopyTable = MibTable((1, 3, 6, 1, 4, 1, 89, 87, 2), )
if mibBuilder.loadTexts: rlCopyTable.setStatus('current')
if mibBuilder.loadTexts: rlCopyTable.setDescription(' The (conceptual) table listing only one entry at a time\n          with parameters needed for configuration\n          of the file copy action.')
rlCopyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 87, 2, 1), ).setIndexNames((0, "RADLAN-COPY-MIB", "rlCopyIndex"))
if mibBuilder.loadTexts: rlCopyEntry.setStatus('current')
if mibBuilder.loadTexts: rlCopyEntry.setDescription(' An entry (conceptual row) in the CopyTable.')
rlCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyIndex.setStatus('current')
if mibBuilder.loadTexts: rlCopyIndex.setDescription('The row index in the table.')
rlCopyApplicationId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 2), RlCopyApplicationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyApplicationId.setStatus('current')
if mibBuilder.loadTexts: rlCopyApplicationId.setDescription('The applicatione activated this comand')
rlCopySourceLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 3), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceLocation.setStatus('current')
if mibBuilder.loadTexts: rlCopySourceLocation.setDescription('Source File Location')
rlCopySourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceIpAddress.setStatus('current')
if mibBuilder.loadTexts: rlCopySourceIpAddress.setDescription('The Ip address of the source remote host')
rlCopySourceUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceUnitNumber.setStatus('current')
if mibBuilder.loadTexts: rlCopySourceUnitNumber.setDescription('The unit number of the source unit')
rlCopySourceFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceFileName.setStatus('current')
if mibBuilder.loadTexts: rlCopySourceFileName.setDescription('The name of the source file.')
rlCopySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 7), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopySourceFileType.setStatus('current')
if mibBuilder.loadTexts: rlCopySourceFileType.setDescription('The type of the source file.')
rlCopyDestinationLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 8), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationLocation.setStatus('current')
if mibBuilder.loadTexts: rlCopyDestinationLocation.setDescription('Destination File Location')
rlCopyDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationIpAddress.setStatus('current')
if mibBuilder.loadTexts: rlCopyDestinationIpAddress.setDescription('The Ip address of the destination remote host')
rlCopyDestinationUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationUnitNumber.setStatus('current')
if mibBuilder.loadTexts: rlCopyDestinationUnitNumber.setDescription('The unit number of the destination unit,\n         value 257 means all units')
rlCopyDestinationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationFileName.setStatus('current')
if mibBuilder.loadTexts: rlCopyDestinationFileName.setDescription('The name of the destination file.')
rlCopyDestinationFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 12), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyDestinationFileType.setStatus('current')
if mibBuilder.loadTexts: rlCopyDestinationFileType.setDescription('The type of the destination file.')
rlCopyUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyUpTime.setStatus('current')
if mibBuilder.loadTexts: rlCopyUpTime.setDescription('The time elapsed since this entry was created.')
rlCopyOperationState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("uploadInProgress", 1), ("downloadInProgress", 2), ("copyFailed", 3), ("copyTimedout", 4), ("copyFinished", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyOperationState.setStatus('current')
if mibBuilder.loadTexts: rlCopyOperationState.setDescription('The state of the copy operation.')
rlCopyBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyBytesTransferred.setStatus('current')
if mibBuilder.loadTexts: rlCopyBytesTransferred.setDescription('The number of bytes that were transferred by the copy operation.')
rlCopyInBackground = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyInBackground.setStatus('current')
if mibBuilder.loadTexts: rlCopyInBackground.setDescription('When enabled the copy operation is done in the background.')
rlCopyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 17), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlCopyRowStatus.setDescription('It is used to insert or delete an entry')
rlCopyHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 2, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryIndex.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryIndex.setDescription('The index of the entry corresponding to this one in the\n         rlCopyHistoryTable (equals rlCopyHistoryHistoryIndex).\n         A value of 0 indicates that no history entry should be kept\n         for this copy operation.')
rlCopyFreeHistoryIndex = MibScalar((1, 3, 6, 1, 4, 1, 89, 87, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyFreeHistoryIndex.setStatus('current')
if mibBuilder.loadTexts: rlCopyFreeHistoryIndex.setDescription('Gives the next free index in the rlCopyHistoryTable (i.e., the next\n        available value for rlCopyHistoryHistoryIndex)')
rlCopyHistoryTable = MibTable((1, 3, 6, 1, 4, 1, 89, 87, 4), )
if mibBuilder.loadTexts: rlCopyHistoryTable.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryTable.setDescription(' The (conceptual) table listing only one entry at a time\n          with parameters needed for configuration\n          of the file copy action.')
rlCopyHistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 87, 4, 1), ).setIndexNames((0, "RADLAN-COPY-MIB", "rlCopyHistoryHistoryIndex"))
if mibBuilder.loadTexts: rlCopyHistoryEntry.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryEntry.setDescription(' An entry (conceptual row) in the rlCopyHistoryTable.')
rlCopyHistoryHistoryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryHistoryIndex.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryHistoryIndex.setDescription('The row index in the table.')
rlCopyHistoryApplicationId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 2), RlCopyApplicationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryApplicationId.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryApplicationId.setDescription('The application that activated this comand')
rlCopyHistorySourceLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 3), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceLocation.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistorySourceLocation.setDescription('Source File Location')
rlCopyHistorySourceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 4), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceIpAddress.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistorySourceIpAddress.setDescription('The IP address of the source remote host')
rlCopyHistorySourceUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceUnitNumber.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistorySourceUnitNumber.setDescription('The unit number of the source unit')
rlCopyHistorySourceFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 6), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceFileName.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistorySourceFileName.setDescription('The name of the source file.')
rlCopyHistorySourceFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 7), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistorySourceFileType.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistorySourceFileType.setDescription('The type of the source file.')
rlCopyHistoryDestinationLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 8), RlCopyLocationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationLocation.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryDestinationLocation.setDescription('Destination File Location')
rlCopyHistoryDestinationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationIpAddress.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryDestinationIpAddress.setDescription('The IP address of the destination remote host')
rlCopyHistoryDestinationUnitNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationUnitNumber.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryDestinationUnitNumber.setDescription('The unit number of the destination unit')
rlCopyHistoryDestinationFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationFileName.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryDestinationFileName.setDescription('The name of the destination file.')
rlCopyHistoryDestinationFileType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 12), RlCopyFileType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryDestinationFileType.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryDestinationFileType.setDescription('The type of the destination file.')
rlCopyHistoryUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryUpTime.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryUpTime.setDescription('The time elapsed since this entry was created.')
rlCopyHistoryOperationState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("uploadInProgress", 1), ("downloadInProgress", 2), ("copyFailed", 3), ("copyTimedout", 4), ("copyFinished", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryOperationState.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryOperationState.setDescription('The state of the copy operation.')
rlCopyHistoryBytesTransferred = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryBytesTransferred.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryBytesTransferred.setDescription('The number of bytes that were transferred by the copy operation.')
rlCopyHistoryInBackground = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryInBackground.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryInBackground.setDescription('When enabled the copy operation is done in the background.')
rlCopyHistoryRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 17), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyHistoryRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryRowStatus.setDescription('It is used delete an entry. No other operations are permitted since\n         the history table is populated and updated through the copy table only.')
rlCopyHistoryErrorMessage = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 4, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyHistoryErrorMessage.setStatus('current')
if mibBuilder.loadTexts: rlCopyHistoryErrorMessage.setDescription('Error message as a result of failed copy action.')
rlCopyAuditingEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 87, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyAuditingEnable.setStatus('current')
if mibBuilder.loadTexts: rlCopyAuditingEnable.setDescription('Controls whether SysLog messages\n         should be issued on file copy events')
rlCopyMessagesTable = MibTable((1, 3, 6, 1, 4, 1, 89, 87, 6), )
if mibBuilder.loadTexts: rlCopyMessagesTable.setStatus('current')
if mibBuilder.loadTexts: rlCopyMessagesTable.setDescription(' The table listing the messages issued during a COPY operation.')
rlCopyMessagesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 87, 6, 1), ).setIndexNames((0, "RADLAN-COPY-MIB", "rlCopyMessagesCopyIndex"), (0, "RADLAN-COPY-MIB", "rlCopyMessagesMessageIndex"))
if mibBuilder.loadTexts: rlCopyMessagesEntry.setStatus('current')
if mibBuilder.loadTexts: rlCopyMessagesEntry.setDescription(' An entry (conceptual row) in the rlCopyMessagesTable.')
rlCopyMessagesCopyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rlCopyMessagesCopyIndex.setStatus('current')
if mibBuilder.loadTexts: rlCopyMessagesCopyIndex.setDescription('The index of the copy operation whose messages are displayed.')
rlCopyMessagesMessageIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: rlCopyMessagesMessageIndex.setStatus('current')
if mibBuilder.loadTexts: rlCopyMessagesMessageIndex.setDescription('The index of the displayed message.')
rlCopyMessagesMessageText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlCopyMessagesMessageText.setStatus('current')
if mibBuilder.loadTexts: rlCopyMessagesMessageText.setDescription('The text of the message occurred in the copy operation.')
rlCopyMessagesStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 87, 6, 1, 4), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyMessagesStatus.setStatus('current')
if mibBuilder.loadTexts: rlCopyMessagesStatus.setDescription('Only destroy is supported.')
rlCopyMessagesTableRemoveEntries = MibScalar((1, 3, 6, 1, 4, 1, 89, 87, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlCopyMessagesTableRemoveEntries.setStatus('current')
if mibBuilder.loadTexts: rlCopyMessagesTableRemoveEntries.setDescription('Setting this object with value n will remove all entries associated\n         with copy operation represented by the value n from the rlCopyMessagesTable,\n         i.e. all the entries with rlCopyMessagesCopyIndex = n.')
mibBuilder.exportSymbols("RADLAN-COPY-MIB", rlCopyDestinationLocation=rlCopyDestinationLocation, rlCopyMessagesStatus=rlCopyMessagesStatus, rlCopyOperationState=rlCopyOperationState, rlCopySourceLocation=rlCopySourceLocation, rlCopy=rlCopy, rlCopyHistoryTable=rlCopyHistoryTable, rlCopyMessagesMessageText=rlCopyMessagesMessageText, rlCopyFreeHistoryIndex=rlCopyFreeHistoryIndex, rlCopySourceUnitNumber=rlCopySourceUnitNumber, rlCopyMessagesEntry=rlCopyMessagesEntry, RlCopyLocationType=RlCopyLocationType, rlCopyHistorySourceUnitNumber=rlCopyHistorySourceUnitNumber, rlCopyRowStatus=rlCopyRowStatus, RlCopyFileType=RlCopyFileType, rlCopySourceFileName=rlCopySourceFileName, rlCopyDestinationFileName=rlCopyDestinationFileName, rlCopyHistoryDestinationUnitNumber=rlCopyHistoryDestinationUnitNumber, rlCopyHistoryOperationState=rlCopyHistoryOperationState, rlCopyHistorySourceFileType=rlCopyHistorySourceFileType, rlCopyHistoryUpTime=rlCopyHistoryUpTime, rlCopyTable=rlCopyTable, rlCopyHistorySourceIpAddress=rlCopyHistorySourceIpAddress, rlCopyMessagesCopyIndex=rlCopyMessagesCopyIndex, PYSNMP_MODULE_ID=rlCopy, rlCopyHistoryIndex=rlCopyHistoryIndex, rlCopyAuditingEnable=rlCopyAuditingEnable, rlCopyMessagesTable=rlCopyMessagesTable, RlCopyApplicationType=RlCopyApplicationType, rlCopyHistoryInBackground=rlCopyHistoryInBackground, rlCopyHistoryErrorMessage=rlCopyHistoryErrorMessage, rlCopyMibVersion=rlCopyMibVersion, rlCopyHistorySourceFileName=rlCopyHistorySourceFileName, rlCopyHistoryDestinationIpAddress=rlCopyHistoryDestinationIpAddress, rlCopyEntry=rlCopyEntry, rlCopyUpTime=rlCopyUpTime, rlCopyInBackground=rlCopyInBackground, rlCopyHistoryBytesTransferred=rlCopyHistoryBytesTransferred, rlCopyHistorySourceLocation=rlCopyHistorySourceLocation, rlCopyApplicationId=rlCopyApplicationId, rlCopyHistoryHistoryIndex=rlCopyHistoryHistoryIndex, rlCopySourceFileType=rlCopySourceFileType, rlCopyHistoryEntry=rlCopyHistoryEntry, rlCopyHistoryDestinationLocation=rlCopyHistoryDestinationLocation, rlCopyHistoryDestinationFileType=rlCopyHistoryDestinationFileType, rlCopySourceIpAddress=rlCopySourceIpAddress, rlCopyBytesTransferred=rlCopyBytesTransferred, rlCopyMessagesMessageIndex=rlCopyMessagesMessageIndex, rlCopyHistoryRowStatus=rlCopyHistoryRowStatus, rlCopyDestinationFileType=rlCopyDestinationFileType, rlCopyIndex=rlCopyIndex, rlCopyDestinationIpAddress=rlCopyDestinationIpAddress, rlCopyHistoryApplicationId=rlCopyHistoryApplicationId, rlCopyHistoryDestinationFileName=rlCopyHistoryDestinationFileName, rlCopyMessagesTableRemoveEntries=rlCopyMessagesTableRemoveEntries, rlCopyDestinationUnitNumber=rlCopyDestinationUnitNumber)
