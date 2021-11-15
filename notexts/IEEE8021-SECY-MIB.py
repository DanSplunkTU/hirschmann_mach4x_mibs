#
# PySNMP MIB module IEEE8021-SECY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-SECY-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:22 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Integer32, Counter32, Counter64, TimeTicks, ObjectIdentity, NotificationType, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Integer32", "Counter32", "Counter64", "TimeTicks", "ObjectIdentity", "NotificationType", "Gauge32")
RowPointer, TruthValue, DisplayString, TimeStamp, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "TruthValue", "DisplayString", "TimeStamp", "TextualConvention", "RowStatus")
ieee8021SecyMIB = ModuleIdentity((1, 0, 8802, 1, 1, 3))
ieee8021SecyMIB.setRevisions(('2006-01-10 00:00',))
if mibBuilder.loadTexts: ieee8021SecyMIB.setLastUpdated('200601100000Z')
if mibBuilder.loadTexts: ieee8021SecyMIB.setOrganization('IEEE 802.1 Working Group')
secyMIBNotifications = MibIdentifier((1, 0, 8802, 1, 1, 3, 0))
secyMIBObjects = MibIdentifier((1, 0, 8802, 1, 1, 3, 1))
secyMIBConformance = MibIdentifier((1, 0, 8802, 1, 1, 3, 2))
class SecySCI(TextualConvention, OctetString):
    reference = 'IEEE 802.1AE Clause 7.1.2, 10.7.1 and figure 7.7'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(8, 8)
    fixedLength = 8

class SecyAN(TextualConvention, Unsigned32):
    reference = 'IEEE 802.1AE Clause 8.1.3 and figure 7.7'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 3)

secyMgmtMIBObjects = MibIdentifier((1, 0, 8802, 1, 1, 3, 1, 1))
secyStatsMIBObjects = MibIdentifier((1, 0, 8802, 1, 1, 3, 1, 2))
secyIfTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 1, 1), )
if mibBuilder.loadTexts: secyIfTable.setStatus('current')
secyIfEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"))
if mibBuilder.loadTexts: secyIfEntry.setStatus('current')
secyIfInterfaceIndex = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: secyIfInterfaceIndex.setStatus('current')
secyIfMaxPeerSCs = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 2), Unsigned32()).setUnits('security connections').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyIfMaxPeerSCs.setStatus('current')
secyIfRxMaxKeys = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 3), Unsigned32()).setUnits('keys').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyIfRxMaxKeys.setStatus('current')
secyIfTxMaxKeys = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 4), Unsigned32()).setUnits('keys').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyIfTxMaxKeys.setStatus('current')
secyIfProtectFramesEnable = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 5), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secyIfProtectFramesEnable.setStatus('current')
secyIfValidateFrames = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("check", 2), ("strict", 3))).clone('strict')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secyIfValidateFrames.setStatus('current')
secyIfReplayProtectEnable = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 7), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secyIfReplayProtectEnable.setStatus('current')
secyIfReplayProtectWindow = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 8), Unsigned32()).setUnits('Packets').setMaxAccess("readwrite")
if mibBuilder.loadTexts: secyIfReplayProtectWindow.setStatus('current')
secyIfCurrentCipherSuite = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secyIfCurrentCipherSuite.setStatus('current')
secyIfAdminPt2PtMAC = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forceTrue", 1), ("forceFalse", 2), ("auto", 3))).clone('auto')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secyIfAdminPt2PtMAC.setStatus('current')
secyIfOperPt2PtMAC = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyIfOperPt2PtMAC.setStatus('current')
secyIfIncludeSCIEnable = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 12), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secyIfIncludeSCIEnable.setStatus('current')
secyIfUseESEnable = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secyIfUseESEnable.setStatus('current')
secyIfUseSCBEnable = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secyIfUseSCBEnable.setStatus('current')
secyTxSCTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 1, 2), )
if mibBuilder.loadTexts: secyTxSCTable.setStatus('current')
secyTxSCEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 1, 2, 1), ).setIndexNames((0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"))
if mibBuilder.loadTexts: secyTxSCEntry.setStatus('current')
secyTxSCI = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 1), SecySCI()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCI.setStatus('current')
secyTxSCState = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inUse", 1), ("notInUse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCState.setStatus('current')
secyTxSCEncodingSA = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 3), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCEncodingSA.setStatus('current')
secyTxSCEncipheringSA = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 4), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCEncipheringSA.setStatus('current')
secyTxSCCreatedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCCreatedTime.setStatus('current')
secyTxSCStartedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCStartedTime.setStatus('current')
secyTxSCStoppedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 2, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCStoppedTime.setStatus('current')
secyTxSATable = MibTable((1, 0, 8802, 1, 1, 3, 1, 1, 3), )
if mibBuilder.loadTexts: secyTxSATable.setStatus('current')
secyTxSAEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 1, 3, 1), ).setIndexNames((0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"), (0, "IEEE8021-SECY-MIB", "secyTxSA"))
if mibBuilder.loadTexts: secyTxSAEntry.setStatus('current')
secyTxSA = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 1), SecyAN())
if mibBuilder.loadTexts: secyTxSA.setStatus('current')
secyTxSAState = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inUse", 1), ("notInUse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSAState.setStatus('current')
secyTxSANextPN = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSANextPN.setStatus('current')
secyTxSAConfidentiality = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSAConfidentiality.setStatus('current')
secyTxSASAKUnchanged = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSASAKUnchanged.setStatus('current')
secyTxSACreatedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSACreatedTime.setStatus('current')
secyTxSAStartedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSAStartedTime.setStatus('current')
secyTxSAStoppedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 3, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSAStoppedTime.setStatus('current')
secyRxSCTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 1, 4), )
if mibBuilder.loadTexts: secyRxSCTable.setStatus('current')
secyRxSCEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 1, 4, 1), ).setIndexNames((0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"), (0, "IEEE8021-SECY-MIB", "secyRxSCI"))
if mibBuilder.loadTexts: secyRxSCEntry.setStatus('current')
secyRxSCI = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 1), SecySCI())
if mibBuilder.loadTexts: secyRxSCI.setStatus('current')
secyRxSCState = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inUse", 1), ("notInUse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCState.setStatus('current')
secyRxSCCurrentSA = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 3), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCCurrentSA.setStatus('current')
secyRxSCCreatedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCCreatedTime.setStatus('current')
secyRxSCStartedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStartedTime.setStatus('current')
secyRxSCStoppedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 4, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStoppedTime.setStatus('current')
secyRxSATable = MibTable((1, 0, 8802, 1, 1, 3, 1, 1, 5), )
if mibBuilder.loadTexts: secyRxSATable.setStatus('current')
secyRxSAEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 1, 5, 1), ).setIndexNames((0, "IEEE8021-SECY-MIB", "secyIfInterfaceIndex"), (0, "IEEE8021-SECY-MIB", "secyRxSCI"), (0, "IEEE8021-SECY-MIB", "secyRxSA"))
if mibBuilder.loadTexts: secyRxSAEntry.setStatus('current')
secyRxSA = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 1), SecyAN())
if mibBuilder.loadTexts: secyRxSA.setStatus('current')
secyRxSAState = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("inUse", 1), ("notInUse", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSAState.setStatus('current')
secyRxSANextPN = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 3), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: secyRxSANextPN.setStatus('current')
secyRxSASAKUnchanged = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSASAKUnchanged.setStatus('current')
secyRxSACreatedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSACreatedTime.setStatus('current')
secyRxSAStartedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSAStartedTime.setStatus('current')
secyRxSAStoppedTime = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 5, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSAStoppedTime.setStatus('current')
secyCipherSuiteTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 1, 6), )
if mibBuilder.loadTexts: secyCipherSuiteTable.setStatus('current')
secyCipherSuiteEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 1, 6, 1), ).setIndexNames((0, "IEEE8021-SECY-MIB", "secyCipherSuiteIndex"))
if mibBuilder.loadTexts: secyCipherSuiteEntry.setStatus('current')
secyCipherSuiteIndex = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: secyCipherSuiteIndex.setStatus('current')
secyCipherSuiteId = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: secyCipherSuiteId.setStatus('current')
secyCipherSuiteName = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 128))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: secyCipherSuiteName.setStatus('current')
secyCipherSuiteCapability = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 4), Bits().clone(namedValues=NamedValues(("integrity", 0), ("confidentiality", 1), ("offsetConfidentiality", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: secyCipherSuiteCapability.setStatus('current')
secyCipherSuiteProtection = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 5), Bits().clone(namedValues=NamedValues(("integrity", 0), ("confidentiality", 1), ("offsetConfidentiality", 2))).clone(namedValues=NamedValues(("integrity", 0)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: secyCipherSuiteProtection.setStatus('current')
secyCipherSuiteProtectionOffset = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(30, 30), ValueRangeConstraint(50, 50), ))).setUnits('bytes').setMaxAccess("readcreate")
if mibBuilder.loadTexts: secyCipherSuiteProtectionOffset.setStatus('current')
secyCipherSuiteDataLengthChange = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 7), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: secyCipherSuiteDataLengthChange.setStatus('current')
secyCipherSuiteICVLength = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(8, 16))).setUnits('octets').setMaxAccess("readcreate")
if mibBuilder.loadTexts: secyCipherSuiteICVLength.setStatus('current')
secyCipherSuiteRowStatus = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 1, 6, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: secyCipherSuiteRowStatus.setStatus('current')
secyTxSAStatsTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 2, 1), )
if mibBuilder.loadTexts: secyTxSAStatsTable.setStatus('current')
secyTxSAStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 2, 1, 1), )
secyTxSAEntry.registerAugmentions(("IEEE8021-SECY-MIB", "secyTxSAStatsEntry"))
secyTxSAStatsEntry.setIndexNames(*secyTxSAEntry.getIndexNames())
if mibBuilder.loadTexts: secyTxSAStatsEntry.setStatus('current')
secyTxSAStatsProtectedPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 1), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSAStatsProtectedPkts.setStatus('current')
secyTxSAStatsEncryptedPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 1, 1, 2), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSAStatsEncryptedPkts.setStatus('current')
secyTxSCStatsTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 2, 2), )
if mibBuilder.loadTexts: secyTxSCStatsTable.setStatus('current')
secyTxSCStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 2, 2, 1), )
secyTxSCEntry.registerAugmentions(("IEEE8021-SECY-MIB", "secyTxSCStatsEntry"))
secyTxSCStatsEntry.setIndexNames(*secyTxSCEntry.getIndexNames())
if mibBuilder.loadTexts: secyTxSCStatsEntry.setStatus('current')
secyTxSCStatsProtectedPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 2, 1, 1), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCStatsProtectedPkts.setStatus('current')
secyTxSCStatsEncryptedPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 2, 1, 4), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCStatsEncryptedPkts.setStatus('current')
secyTxSCStatsOctetsProtected = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 2, 1, 10), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCStatsOctetsProtected.setStatus('current')
secyTxSCStatsOctetsEncrypted = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 2, 1, 11), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyTxSCStatsOctetsEncrypted.setStatus('current')
secyRxSAStatsTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 2, 3), )
if mibBuilder.loadTexts: secyRxSAStatsTable.setStatus('current')
secyRxSAStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 2, 3, 1), )
secyRxSAEntry.registerAugmentions(("IEEE8021-SECY-MIB", "secyRxSAStatsEntry"))
secyRxSAStatsEntry.setIndexNames(*secyRxSAEntry.getIndexNames())
if mibBuilder.loadTexts: secyRxSAStatsEntry.setStatus('current')
secyRxSAStatsUnusedSAPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 3, 1, 1), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSAStatsUnusedSAPkts.setStatus('current')
secyRxSAStatsNoUsingSAPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 3, 1, 4), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSAStatsNoUsingSAPkts.setStatus('current')
secyRxSAStatsNotValidPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 3, 1, 13), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSAStatsNotValidPkts.setStatus('current')
secyRxSAStatsInvalidPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 3, 1, 16), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSAStatsInvalidPkts.setStatus('current')
secyRxSAStatsOKPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 3, 1, 25), Counter32()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSAStatsOKPkts.setStatus('current')
secyRxSCStatsTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 2, 4), )
if mibBuilder.loadTexts: secyRxSCStatsTable.setStatus('current')
secyRxSCStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1), )
secyRxSCEntry.registerAugmentions(("IEEE8021-SECY-MIB", "secyRxSCStatsEntry"))
secyRxSCStatsEntry.setIndexNames(*secyRxSCEntry.getIndexNames())
if mibBuilder.loadTexts: secyRxSCStatsEntry.setStatus('current')
secyRxSCStatsUnusedSAPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 1), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStatsUnusedSAPkts.setStatus('current')
secyRxSCStatsNoUsingSAPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 2), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStatsNoUsingSAPkts.setStatus('current')
secyRxSCStatsLatePkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 3), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStatsLatePkts.setStatus('current')
secyRxSCStatsNotValidPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 4), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStatsNotValidPkts.setStatus('current')
secyRxSCStatsInvalidPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 5), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStatsInvalidPkts.setStatus('current')
secyRxSCStatsDelayedPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 6), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStatsDelayedPkts.setStatus('current')
secyRxSCStatsUncheckedPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 7), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStatsUncheckedPkts.setStatus('current')
secyRxSCStatsOKPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 8), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStatsOKPkts.setStatus('current')
secyRxSCStatsOctetsValidated = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 9), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStatsOctetsValidated.setStatus('current')
secyRxSCStatsOctetsDecrypted = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 4, 1, 10), Counter64()).setUnits('Octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyRxSCStatsOctetsDecrypted.setStatus('current')
secyStatsTable = MibTable((1, 0, 8802, 1, 1, 3, 1, 2, 5), )
if mibBuilder.loadTexts: secyStatsTable.setStatus('current')
secyStatsEntry = MibTableRow((1, 0, 8802, 1, 1, 3, 1, 2, 5, 1), )
secyIfEntry.registerAugmentions(("IEEE8021-SECY-MIB", "secyStatsEntry"))
secyStatsEntry.setIndexNames(*secyIfEntry.getIndexNames())
if mibBuilder.loadTexts: secyStatsEntry.setStatus('current')
secyStatsTxUntaggedPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 1), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyStatsTxUntaggedPkts.setStatus('current')
secyStatsTxTooLongPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 2), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyStatsTxTooLongPkts.setStatus('current')
secyStatsRxUntaggedPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 3), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyStatsRxUntaggedPkts.setStatus('current')
secyStatsRxNoTagPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 4), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyStatsRxNoTagPkts.setStatus('current')
secyStatsRxBadTagPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 5), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyStatsRxBadTagPkts.setStatus('current')
secyStatsRxUnknownSCIPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 6), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyStatsRxUnknownSCIPkts.setStatus('current')
secyStatsRxNoSCIPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 7), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyStatsRxNoSCIPkts.setStatus('current')
secyStatsRxOverrunPkts = MibTableColumn((1, 0, 8802, 1, 1, 3, 1, 2, 5, 1, 8), Counter64()).setUnits('Packets').setMaxAccess("readonly")
if mibBuilder.loadTexts: secyStatsRxOverrunPkts.setStatus('current')
secyMIBCompliances = MibIdentifier((1, 0, 8802, 1, 1, 3, 2, 1))
secyMIBGroups = MibIdentifier((1, 0, 8802, 1, 1, 3, 2, 2))
secyMIBCompliance = ModuleCompliance((1, 0, 8802, 1, 1, 3, 2, 1, 1)).setObjects(("IEEE8021-SECY-MIB", "secyIfCtrlGroup"), ("IEEE8021-SECY-MIB", "secyTxSCGroup"), ("IEEE8021-SECY-MIB", "secyTxSAGroup"), ("IEEE8021-SECY-MIB", "secyRxSCGroup"), ("IEEE8021-SECY-MIB", "secyRxSAGroup"), ("IEEE8021-SECY-MIB", "secyCipherSuiteGroup"), ("IEEE8021-SECY-MIB", "secyTxSAStatsGroup"), ("IEEE8021-SECY-MIB", "secyTxSCStatsGroup"), ("IEEE8021-SECY-MIB", "secyRxSAStatsGroup"), ("IEEE8021-SECY-MIB", "secyRxSCStatsGroup"), ("IEEE8021-SECY-MIB", "secyStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyMIBCompliance = secyMIBCompliance.setStatus('current')
secyIfCtrlGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 1)).setObjects(("IEEE8021-SECY-MIB", "secyIfMaxPeerSCs"), ("IEEE8021-SECY-MIB", "secyIfRxMaxKeys"), ("IEEE8021-SECY-MIB", "secyIfTxMaxKeys"), ("IEEE8021-SECY-MIB", "secyIfProtectFramesEnable"), ("IEEE8021-SECY-MIB", "secyIfValidateFrames"), ("IEEE8021-SECY-MIB", "secyIfReplayProtectEnable"), ("IEEE8021-SECY-MIB", "secyIfReplayProtectWindow"), ("IEEE8021-SECY-MIB", "secyIfCurrentCipherSuite"), ("IEEE8021-SECY-MIB", "secyIfAdminPt2PtMAC"), ("IEEE8021-SECY-MIB", "secyIfOperPt2PtMAC"), ("IEEE8021-SECY-MIB", "secyIfIncludeSCIEnable"), ("IEEE8021-SECY-MIB", "secyIfUseESEnable"), ("IEEE8021-SECY-MIB", "secyIfUseSCBEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyIfCtrlGroup = secyIfCtrlGroup.setStatus('current')
secyTxSCGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 2)).setObjects(("IEEE8021-SECY-MIB", "secyTxSCI"), ("IEEE8021-SECY-MIB", "secyTxSCState"), ("IEEE8021-SECY-MIB", "secyTxSCEncodingSA"), ("IEEE8021-SECY-MIB", "secyTxSCEncipheringSA"), ("IEEE8021-SECY-MIB", "secyTxSCCreatedTime"), ("IEEE8021-SECY-MIB", "secyTxSCStartedTime"), ("IEEE8021-SECY-MIB", "secyTxSCStoppedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyTxSCGroup = secyTxSCGroup.setStatus('current')
secyTxSAGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 3)).setObjects(("IEEE8021-SECY-MIB", "secyTxSAState"), ("IEEE8021-SECY-MIB", "secyTxSANextPN"), ("IEEE8021-SECY-MIB", "secyTxSAConfidentiality"), ("IEEE8021-SECY-MIB", "secyTxSASAKUnchanged"), ("IEEE8021-SECY-MIB", "secyTxSACreatedTime"), ("IEEE8021-SECY-MIB", "secyTxSAStartedTime"), ("IEEE8021-SECY-MIB", "secyTxSAStoppedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyTxSAGroup = secyTxSAGroup.setStatus('current')
secyRxSCGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 4)).setObjects(("IEEE8021-SECY-MIB", "secyRxSCState"), ("IEEE8021-SECY-MIB", "secyRxSCCurrentSA"), ("IEEE8021-SECY-MIB", "secyRxSCCreatedTime"), ("IEEE8021-SECY-MIB", "secyRxSCStartedTime"), ("IEEE8021-SECY-MIB", "secyRxSCStoppedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyRxSCGroup = secyRxSCGroup.setStatus('current')
secyRxSAGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 5)).setObjects(("IEEE8021-SECY-MIB", "secyRxSAState"), ("IEEE8021-SECY-MIB", "secyRxSANextPN"), ("IEEE8021-SECY-MIB", "secyRxSASAKUnchanged"), ("IEEE8021-SECY-MIB", "secyRxSACreatedTime"), ("IEEE8021-SECY-MIB", "secyRxSAStartedTime"), ("IEEE8021-SECY-MIB", "secyRxSAStoppedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyRxSAGroup = secyRxSAGroup.setStatus('current')
secyCipherSuiteGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 6)).setObjects(("IEEE8021-SECY-MIB", "secyCipherSuiteId"), ("IEEE8021-SECY-MIB", "secyCipherSuiteName"), ("IEEE8021-SECY-MIB", "secyCipherSuiteCapability"), ("IEEE8021-SECY-MIB", "secyCipherSuiteProtection"), ("IEEE8021-SECY-MIB", "secyCipherSuiteProtectionOffset"), ("IEEE8021-SECY-MIB", "secyCipherSuiteDataLengthChange"), ("IEEE8021-SECY-MIB", "secyCipherSuiteICVLength"), ("IEEE8021-SECY-MIB", "secyCipherSuiteRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyCipherSuiteGroup = secyCipherSuiteGroup.setStatus('current')
secyTxSAStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 7)).setObjects(("IEEE8021-SECY-MIB", "secyTxSAStatsProtectedPkts"), ("IEEE8021-SECY-MIB", "secyTxSAStatsEncryptedPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyTxSAStatsGroup = secyTxSAStatsGroup.setStatus('current')
secyRxSAStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 8)).setObjects(("IEEE8021-SECY-MIB", "secyRxSAStatsUnusedSAPkts"), ("IEEE8021-SECY-MIB", "secyRxSAStatsNoUsingSAPkts"), ("IEEE8021-SECY-MIB", "secyRxSAStatsNotValidPkts"), ("IEEE8021-SECY-MIB", "secyRxSAStatsInvalidPkts"), ("IEEE8021-SECY-MIB", "secyRxSAStatsOKPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyRxSAStatsGroup = secyRxSAStatsGroup.setStatus('current')
secyTxSCStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 9)).setObjects(("IEEE8021-SECY-MIB", "secyTxSCStatsProtectedPkts"), ("IEEE8021-SECY-MIB", "secyTxSCStatsEncryptedPkts"), ("IEEE8021-SECY-MIB", "secyTxSCStatsOctetsProtected"), ("IEEE8021-SECY-MIB", "secyTxSCStatsOctetsEncrypted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyTxSCStatsGroup = secyTxSCStatsGroup.setStatus('current')
secyRxSCStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 10)).setObjects(("IEEE8021-SECY-MIB", "secyRxSCStatsUnusedSAPkts"), ("IEEE8021-SECY-MIB", "secyRxSCStatsNoUsingSAPkts"), ("IEEE8021-SECY-MIB", "secyRxSCStatsLatePkts"), ("IEEE8021-SECY-MIB", "secyRxSCStatsNotValidPkts"), ("IEEE8021-SECY-MIB", "secyRxSCStatsInvalidPkts"), ("IEEE8021-SECY-MIB", "secyRxSCStatsDelayedPkts"), ("IEEE8021-SECY-MIB", "secyRxSCStatsUncheckedPkts"), ("IEEE8021-SECY-MIB", "secyRxSCStatsOKPkts"), ("IEEE8021-SECY-MIB", "secyRxSCStatsOctetsValidated"), ("IEEE8021-SECY-MIB", "secyRxSCStatsOctetsDecrypted"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyRxSCStatsGroup = secyRxSCStatsGroup.setStatus('current')
secyStatsGroup = ObjectGroup((1, 0, 8802, 1, 1, 3, 2, 2, 11)).setObjects(("IEEE8021-SECY-MIB", "secyStatsTxUntaggedPkts"), ("IEEE8021-SECY-MIB", "secyStatsTxTooLongPkts"), ("IEEE8021-SECY-MIB", "secyStatsRxUntaggedPkts"), ("IEEE8021-SECY-MIB", "secyStatsRxNoTagPkts"), ("IEEE8021-SECY-MIB", "secyStatsRxBadTagPkts"), ("IEEE8021-SECY-MIB", "secyStatsRxUnknownSCIPkts"), ("IEEE8021-SECY-MIB", "secyStatsRxNoSCIPkts"), ("IEEE8021-SECY-MIB", "secyStatsRxOverrunPkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    secyStatsGroup = secyStatsGroup.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-SECY-MIB", secyRxSAStatsGroup=secyRxSAStatsGroup, secyTxSCCreatedTime=secyTxSCCreatedTime, secyStatsRxOverrunPkts=secyStatsRxOverrunPkts, ieee8021SecyMIB=ieee8021SecyMIB, secyIfUseESEnable=secyIfUseESEnable, secyStatsTxUntaggedPkts=secyStatsTxUntaggedPkts, secyCipherSuiteTable=secyCipherSuiteTable, secyTxSAState=secyTxSAState, secyCipherSuiteProtectionOffset=secyCipherSuiteProtectionOffset, secyTxSCStartedTime=secyTxSCStartedTime, secyStatsMIBObjects=secyStatsMIBObjects, secyMIBCompliance=secyMIBCompliance, secyRxSCStatsNoUsingSAPkts=secyRxSCStatsNoUsingSAPkts, SecySCI=SecySCI, secyRxSASAKUnchanged=secyRxSASAKUnchanged, secyIfInterfaceIndex=secyIfInterfaceIndex, secyRxSAStatsTable=secyRxSAStatsTable, secyRxSCState=secyRxSCState, secyRxSCStatsEntry=secyRxSCStatsEntry, secyTxSCStoppedTime=secyTxSCStoppedTime, secyCipherSuiteIndex=secyCipherSuiteIndex, secyCipherSuiteCapability=secyCipherSuiteCapability, secyRxSAStoppedTime=secyRxSAStoppedTime, PYSNMP_MODULE_ID=ieee8021SecyMIB, secyTxSCStatsTable=secyTxSCStatsTable, secyRxSCStatsInvalidPkts=secyRxSCStatsInvalidPkts, secyIfMaxPeerSCs=secyIfMaxPeerSCs, secyTxSAStatsTable=secyTxSAStatsTable, secyTxSAStatsGroup=secyTxSAStatsGroup, secyCipherSuiteProtection=secyCipherSuiteProtection, secyRxSAGroup=secyRxSAGroup, secyIfAdminPt2PtMAC=secyIfAdminPt2PtMAC, secyMIBConformance=secyMIBConformance, secyIfReplayProtectEnable=secyIfReplayProtectEnable, secyIfCtrlGroup=secyIfCtrlGroup, secyTxSCStatsOctetsEncrypted=secyTxSCStatsOctetsEncrypted, secyCipherSuiteICVLength=secyCipherSuiteICVLength, secyMIBNotifications=secyMIBNotifications, secyCipherSuiteRowStatus=secyCipherSuiteRowStatus, secyTxSAGroup=secyTxSAGroup, secyIfTable=secyIfTable, secyStatsGroup=secyStatsGroup, secyRxSCStatsDelayedPkts=secyRxSCStatsDelayedPkts, secyTxSCStatsOctetsProtected=secyTxSCStatsOctetsProtected, secyTxSCStatsGroup=secyTxSCStatsGroup, secyTxSA=secyTxSA, secyIfTxMaxKeys=secyIfTxMaxKeys, secyIfReplayProtectWindow=secyIfReplayProtectWindow, secyTxSCEncodingSA=secyTxSCEncodingSA, secyIfValidateFrames=secyIfValidateFrames, secyStatsTable=secyStatsTable, secyTxSAStatsEntry=secyTxSAStatsEntry, secyRxSCStoppedTime=secyRxSCStoppedTime, secyTxSCEntry=secyTxSCEntry, secyCipherSuiteGroup=secyCipherSuiteGroup, secyRxSAStatsUnusedSAPkts=secyRxSAStatsUnusedSAPkts, secyStatsRxNoSCIPkts=secyStatsRxNoSCIPkts, secyCipherSuiteDataLengthChange=secyCipherSuiteDataLengthChange, secyTxSCStatsProtectedPkts=secyTxSCStatsProtectedPkts, secyIfIncludeSCIEnable=secyIfIncludeSCIEnable, secyMgmtMIBObjects=secyMgmtMIBObjects, secyRxSCStatsOctetsDecrypted=secyRxSCStatsOctetsDecrypted, secyTxSAStartedTime=secyTxSAStartedTime, secyRxSAStatsNotValidPkts=secyRxSAStatsNotValidPkts, secyIfCurrentCipherSuite=secyIfCurrentCipherSuite, secyRxSCStatsUnusedSAPkts=secyRxSCStatsUnusedSAPkts, secyTxSCI=secyTxSCI, secyIfRxMaxKeys=secyIfRxMaxKeys, secyRxSCGroup=secyRxSCGroup, secyRxSCCurrentSA=secyRxSCCurrentSA, secyRxSANextPN=secyRxSANextPN, secyTxSACreatedTime=secyTxSACreatedTime, secyRxSACreatedTime=secyRxSACreatedTime, secyStatsTxTooLongPkts=secyStatsTxTooLongPkts, secyRxSAEntry=secyRxSAEntry, secyRxSCStatsTable=secyRxSCStatsTable, secyRxSATable=secyRxSATable, secyRxSCStatsLatePkts=secyRxSCStatsLatePkts, SecyAN=SecyAN, secyIfEntry=secyIfEntry, secyTxSCTable=secyTxSCTable, secyRxSCStatsUncheckedPkts=secyRxSCStatsUncheckedPkts, secyRxSAStatsNoUsingSAPkts=secyRxSAStatsNoUsingSAPkts, secyRxSCEntry=secyRxSCEntry, secyRxSAState=secyRxSAState, secyStatsRxUnknownSCIPkts=secyStatsRxUnknownSCIPkts, secyRxSCStartedTime=secyRxSCStartedTime, secyIfProtectFramesEnable=secyIfProtectFramesEnable, secyCipherSuiteEntry=secyCipherSuiteEntry, secyRxSCCreatedTime=secyRxSCCreatedTime, secyIfOperPt2PtMAC=secyIfOperPt2PtMAC, secyRxSCStatsOKPkts=secyRxSCStatsOKPkts, secyStatsRxNoTagPkts=secyStatsRxNoTagPkts, secyMIBObjects=secyMIBObjects, secyRxSAStartedTime=secyRxSAStartedTime, secyTxSANextPN=secyTxSANextPN, secyTxSAConfidentiality=secyTxSAConfidentiality, secyTxSCStatsEntry=secyTxSCStatsEntry, secyTxSCStatsEncryptedPkts=secyTxSCStatsEncryptedPkts, secyMIBGroups=secyMIBGroups, secyTxSASAKUnchanged=secyTxSASAKUnchanged, secyTxSCEncipheringSA=secyTxSCEncipheringSA, secyRxSCStatsOctetsValidated=secyRxSCStatsOctetsValidated, secyTxSCState=secyTxSCState, secyRxSA=secyRxSA, secyTxSAStoppedTime=secyTxSAStoppedTime, secyMIBCompliances=secyMIBCompliances, secyRxSCStatsNotValidPkts=secyRxSCStatsNotValidPkts, secyRxSCI=secyRxSCI, secyCipherSuiteId=secyCipherSuiteId, secyCipherSuiteName=secyCipherSuiteName, secyTxSAStatsEncryptedPkts=secyTxSAStatsEncryptedPkts, secyRxSAStatsInvalidPkts=secyRxSAStatsInvalidPkts, secyStatsRxBadTagPkts=secyStatsRxBadTagPkts, secyTxSATable=secyTxSATable, secyRxSCStatsGroup=secyRxSCStatsGroup, secyStatsEntry=secyStatsEntry, secyRxSAStatsEntry=secyRxSAStatsEntry, secyStatsRxUntaggedPkts=secyStatsRxUntaggedPkts, secyTxSAEntry=secyTxSAEntry, secyIfUseSCBEnable=secyIfUseSCBEnable, secyRxSCTable=secyRxSCTable, secyTxSCGroup=secyTxSCGroup, secyRxSAStatsOKPkts=secyRxSAStatsOKPkts, secyTxSAStatsProtectedPkts=secyTxSAStatsProtectedPkts)
