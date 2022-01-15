#
# PySNMP MIB module RTM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/RTM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
stratacom, = mibBuilder.importSymbols("CISCOWAN-SMI", "stratacom")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rtm = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 120))
trapsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 120, 1))
trapConfigTable = MibTable((1, 3, 6, 1, 4, 1, 351, 120, 1, 1), )
if mibBuilder.loadTexts: trapConfigTable.setStatus('mandatory')
trapConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1), ).setIndexNames((0, "RTM-MIB", "managerIPaddress"))
if mibBuilder.loadTexts: trapConfigEntry.setStatus('mandatory')
managerIPaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerIPaddress.setStatus('mandatory')
managerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerPortNumber.setStatus('mandatory')
managerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("addRow", 1), ("delRow", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: managerRowStatus.setStatus('mandatory')
readingTrapsFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: readingTrapsFlag.setStatus('mandatory')
nextTrapSeqNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nextTrapSeqNum.setStatus('mandatory')
managerNumOfValidEntries = MibScalar((1, 3, 6, 1, 4, 1, 351, 120, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: managerNumOfValidEntries.setStatus('mandatory')
lastSequenceNumber = MibScalar((1, 3, 6, 1, 4, 1, 351, 120, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lastSequenceNumber.setStatus('mandatory')
trapUploadTable = MibTable((1, 3, 6, 1, 4, 1, 351, 120, 1, 4), )
if mibBuilder.loadTexts: trapUploadTable.setStatus('mandatory')
trapUploadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1), ).setIndexNames((0, "RTM-MIB", "trapManagerIPaddress"))
if mibBuilder.loadTexts: trapUploadEntry.setStatus('mandatory')
trapManagerIPaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: trapManagerIPaddress.setStatus('mandatory')
trapSequenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapSequenceNum.setStatus('mandatory')
trapPduString = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapPduString.setStatus('mandatory')
endOfQueueFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: endOfQueueFlag.setStatus('mandatory')
recoverTrapTable = MibTable((1, 3, 6, 1, 4, 1, 351, 120, 1, 5), )
if mibBuilder.loadTexts: recoverTrapTable.setStatus('mandatory')
recoverTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1), ).setIndexNames((0, "RTM-MIB", "recoverTrapSequenceNum"))
if mibBuilder.loadTexts: recoverTrapEntry.setStatus('mandatory')
recoverTrapSequenceNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: recoverTrapSequenceNum.setStatus('mandatory')
recoverTrapPduString = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 120, 1, 5, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readonly")
if mibBuilder.loadTexts: recoverTrapPduString.setStatus('mandatory')
mibBuilder.exportSymbols("RTM-MIB", managerRowStatus=managerRowStatus, trapPduString=trapPduString, lastSequenceNumber=lastSequenceNumber, managerNumOfValidEntries=managerNumOfValidEntries, managerIPaddress=managerIPaddress, recoverTrapTable=recoverTrapTable, managerPortNumber=managerPortNumber, trapUploadTable=trapUploadTable, trapConfigEntry=trapConfigEntry, trapConfigTable=trapConfigTable, trapSequenceNum=trapSequenceNum, rtm=rtm, endOfQueueFlag=endOfQueueFlag, nextTrapSeqNum=nextTrapSeqNum, trapManagerIPaddress=trapManagerIPaddress, recoverTrapSequenceNum=recoverTrapSequenceNum, recoverTrapPduString=recoverTrapPduString, trapUploadEntry=trapUploadEntry, readingTrapsFlag=readingTrapsFlag, trapsConfig=trapsConfig, recoverTrapEntry=recoverTrapEntry)
