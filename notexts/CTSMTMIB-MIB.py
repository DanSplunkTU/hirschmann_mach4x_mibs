#
# PySNMP MIB module CTSMTMIB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTSMTMIB-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:05:33 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ctsmtmib, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctsmtmib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ModuleIdentity, IpAddress, ObjectIdentity, TimeTicks, Gauge32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ModuleIdentity", "IpAddress", "ObjectIdentity", "TimeTicks", "Gauge32", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ctsmtmibRingTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1), )
if mibBuilder.loadTexts: ctsmtmibRingTable.setStatus('mandatory')
ctsmtmibRingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1), ).setIndexNames((0, "CTSMTMIB-MIB", "ctsmtmibRingSmtIndex"), (0, "CTSMTMIB-MIB", "ctsmtmibRingMacIndex"), (0, "CTSMTMIB-MIB", "ctsmtmibRingNodeIndex"), (0, "CTSMTMIB-MIB", "ctsmtmibRingMacAddr"))
if mibBuilder.loadTexts: ctsmtmibRingEntry.setStatus('mandatory')
ctsmtmibRingSmtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingSmtIndex.setStatus('mandatory')
ctsmtmibRingMacIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingMacIndex.setStatus('mandatory')
ctsmtmibRingNodeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingNodeIndex.setStatus('mandatory')
ctsmtmibRingMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingMacAddr.setStatus('mandatory')
ctsmtmibRingUpStreamAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingUpStreamAddr.setStatus('mandatory')
ctsmtmibRingNodeClass = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("station", 1), ("concentrator", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingNodeClass.setStatus('mandatory')
ctsmtmibRingMacCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingMacCount.setStatus('mandatory')
ctsmtmibRingNonMasterCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingNonMasterCount.setStatus('mandatory')
ctsmtmibRingMasterCount = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingMasterCount.setStatus('mandatory')
ctsmtmibRingTopology = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingTopology.setStatus('mandatory')
ctsmtmibRingDuplicate = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibRingDuplicate.setStatus('mandatory')
ctsmtmibMacTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2), )
if mibBuilder.loadTexts: ctsmtmibMacTable.setStatus('mandatory')
ctsmtmibMacEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1), ).setIndexNames((0, "CTSMTMIB-MIB", "ctsmtmibMacSmtIndex"), (0, "CTSMTMIB-MIB", "ctsmtmibMacIndex"))
if mibBuilder.loadTexts: ctsmtmibMacEntry.setStatus('mandatory')
ctsmtmibMacSmtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacSmtIndex.setStatus('mandatory')
ctsmtmibMacIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacIndex.setStatus('mandatory')
ctsmtmibMacNifTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacNifTxCts.setStatus('mandatory')
ctsmtmibMacNifRxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacNifRxCts.setStatus('mandatory')
ctsmtmibMacSifTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacSifTxCts.setStatus('mandatory')
ctsmtmibMacSifRxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacSifRxCts.setStatus('mandatory')
ctsmtmibMacEcfTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacEcfTxCts.setStatus('mandatory')
ctsmtmibMacEcfRxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacEcfRxCts.setStatus('mandatory')
ctsmtmibMacPmfTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacPmfTxCts.setStatus('mandatory')
ctsmtmibMacPmfRxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacPmfRxCts.setStatus('mandatory')
ctsmtmibMacRdfTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacRdfTxCts.setStatus('mandatory')
ctsmtmibMacRdfRxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacRdfRxCts.setStatus('mandatory')
ctsmtmibMacRingOpCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacRingOpCts.setStatus('mandatory')
ctsmtmibMacTxCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacTxCts.setStatus('mandatory')
ctsmtmibMacRingMapUpdateCts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibMacRingMapUpdateCts.setStatus('mandatory')
ctsmtmibMacAutoNegotiation = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctsmtmibMacAutoNegotiation.setStatus('mandatory')
ctsmtmibAttachmentNumber = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentNumber.setStatus('mandatory')
ctsmtmibAttachmentTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4), )
if mibBuilder.loadTexts: ctsmtmibAttachmentTable.setStatus('mandatory')
ctsmtmibAttachmentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1), ).setIndexNames((0, "CTSMTMIB-MIB", "ctsmtmibAttachmentSMTIndex"), (0, "CTSMTMIB-MIB", "ctsmtmibAttachmentIndex"))
if mibBuilder.loadTexts: ctsmtmibAttachmentEntry.setStatus('mandatory')
ctsmtmibAttachmentSMTIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentSMTIndex.setStatus('mandatory')
ctsmtmibAttachmentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentIndex.setStatus('mandatory')
ctsmtmibAttachmentClass = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("single-attachment", 1), ("dual-attachment", 2), ("concentrator", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentClass.setStatus('mandatory')
ctsmtmibAttachmentOpticalBypassPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("true", 1), ("false", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentOpticalBypassPresent.setStatus('mandatory')
ctsmtmibAttachmentIMaxExpiration = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentIMaxExpiration.setStatus('mandatory')
ctsmtmibAttachmentInsertedStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("true", 1), ("false", 2), ("unimplemented", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibAttachmentInsertedStatus.setStatus('mandatory')
ctsmtmibAttachmentInsertPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("true", 1), ("false", 2), ("unimplemented", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctsmtmibAttachmentInsertPolicy.setStatus('mandatory')
ctsmtmibSMTTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5), )
if mibBuilder.loadTexts: ctsmtmibSMTTable.setStatus('mandatory')
ctsmtmibSMTEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1), ).setIndexNames((0, "CTSMTMIB-MIB", "ctsmtmibSmtIndex"))
if mibBuilder.loadTexts: ctsmtmibSMTEntry.setStatus('mandatory')
ctsmtmibSMTDualHomeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notDualHomed", 1), ("linkAorB", 2), ("linkAandB", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibSMTDualHomeStatus.setStatus('mandatory')
ctsmtmibSMTDualHomeWrpLEDStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('on')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctsmtmibSMTDualHomeWrpLEDStatus.setStatus('mandatory')
ctsmtmibSmtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2, 5, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctsmtmibSmtIndex.setStatus('mandatory')
mibBuilder.exportSymbols("CTSMTMIB-MIB", ctsmtmibRingNodeClass=ctsmtmibRingNodeClass, ctsmtmibMacTable=ctsmtmibMacTable, ctsmtmibMacSifRxCts=ctsmtmibMacSifRxCts, ctsmtmibRingEntry=ctsmtmibRingEntry, ctsmtmibSMTTable=ctsmtmibSMTTable, ctsmtmibRingDuplicate=ctsmtmibRingDuplicate, ctsmtmibSMTDualHomeWrpLEDStatus=ctsmtmibSMTDualHomeWrpLEDStatus, ctsmtmibMacPmfRxCts=ctsmtmibMacPmfRxCts, ctsmtmibRingNodeIndex=ctsmtmibRingNodeIndex, ctsmtmibSMTDualHomeStatus=ctsmtmibSMTDualHomeStatus, ctsmtmibMacSifTxCts=ctsmtmibMacSifTxCts, ctsmtmibSmtIndex=ctsmtmibSmtIndex, ctsmtmibRingNonMasterCount=ctsmtmibRingNonMasterCount, ctsmtmibRingMacCount=ctsmtmibRingMacCount, ctsmtmibRingMacAddr=ctsmtmibRingMacAddr, ctsmtmibMacRingOpCts=ctsmtmibMacRingOpCts, ctsmtmibMacSmtIndex=ctsmtmibMacSmtIndex, ctsmtmibRingUpStreamAddr=ctsmtmibRingUpStreamAddr, ctsmtmibMacNifTxCts=ctsmtmibMacNifTxCts, ctsmtmibRingSmtIndex=ctsmtmibRingSmtIndex, ctsmtmibMacPmfTxCts=ctsmtmibMacPmfTxCts, ctsmtmibAttachmentEntry=ctsmtmibAttachmentEntry, ctsmtmibAttachmentClass=ctsmtmibAttachmentClass, ctsmtmibMacEcfTxCts=ctsmtmibMacEcfTxCts, ctsmtmibAttachmentInsertPolicy=ctsmtmibAttachmentInsertPolicy, ctsmtmibMacAutoNegotiation=ctsmtmibMacAutoNegotiation, ctsmtmibAttachmentNumber=ctsmtmibAttachmentNumber, ctsmtmibRingMacIndex=ctsmtmibRingMacIndex, ctsmtmibMacTxCts=ctsmtmibMacTxCts, ctsmtmibAttachmentTable=ctsmtmibAttachmentTable, ctsmtmibMacRdfRxCts=ctsmtmibMacRdfRxCts, ctsmtmibRingTable=ctsmtmibRingTable, ctsmtmibMacRingMapUpdateCts=ctsmtmibMacRingMapUpdateCts, ctsmtmibSMTEntry=ctsmtmibSMTEntry, ctsmtmibMacEcfRxCts=ctsmtmibMacEcfRxCts, ctsmtmibAttachmentOpticalBypassPresent=ctsmtmibAttachmentOpticalBypassPresent, ctsmtmibMacRdfTxCts=ctsmtmibMacRdfTxCts, ctsmtmibMacIndex=ctsmtmibMacIndex, ctsmtmibAttachmentInsertedStatus=ctsmtmibAttachmentInsertedStatus, ctsmtmibAttachmentIndex=ctsmtmibAttachmentIndex, ctsmtmibRingTopology=ctsmtmibRingTopology, ctsmtmibRingMasterCount=ctsmtmibRingMasterCount, ctsmtmibAttachmentSMTIndex=ctsmtmibAttachmentSMTIndex, ctsmtmibMacNifRxCts=ctsmtmibMacNifRxCts, ctsmtmibAttachmentIMaxExpiration=ctsmtmibAttachmentIMaxExpiration, ctsmtmibMacEntry=ctsmtmibMacEntry)
