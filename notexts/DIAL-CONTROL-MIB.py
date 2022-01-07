#
# PySNMP MIB module DIAL-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DIAL-CONTROL-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
InterfaceIndex, InterfaceIndexOrZero, ifOperStatus, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "InterfaceIndexOrZero", "ifOperStatus", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, transmission, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
TextualConvention, TimeStamp, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "RowStatus", "DisplayString")
dialControlMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 21))
if mibBuilder.loadTexts: dialControlMib.setLastUpdated('9609231544Z')
if mibBuilder.loadTexts: dialControlMib.setOrganization('IETF ISDN Working Group')
class AbsoluteCounter32(TextualConvention, Gauge32):
    status = 'current'

dialControlMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 1))
dialCtlConfiguration = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 1, 1))
dialCtlAcceptMode = MibScalar((1, 3, 6, 1, 2, 1, 10, 21, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("acceptNone", 1), ("acceptAll", 2), ("acceptKnown", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialCtlAcceptMode.setStatus('current')
dialCtlTrapEnable = MibScalar((1, 3, 6, 1, 2, 1, 10, 21, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dialCtlTrapEnable.setStatus('current')
dialCtlPeer = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 1, 2))
dialCtlPeerCfgTable = MibTable((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1), )
if mibBuilder.loadTexts: dialCtlPeerCfgTable.setStatus('current')
dialCtlPeerCfgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1), ).setIndexNames((0, "DIAL-CONTROL-MIB", "dialCtlPeerCfgId"), (0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dialCtlPeerCfgEntry.setStatus('current')
dialCtlPeerCfgId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: dialCtlPeerCfgId.setStatus('current')
dialCtlPeerCfgIfType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 2), IANAifType().clone('other')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgIfType.setStatus('current')
dialCtlPeerCfgLowerIf = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgLowerIf.setStatus('current')
dialCtlPeerCfgOriginateAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgOriginateAddress.setStatus('current')
dialCtlPeerCfgAnswerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgAnswerAddress.setStatus('current')
dialCtlPeerCfgSubAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgSubAddress.setStatus('current')
dialCtlPeerCfgClosedUserGroup = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgClosedUserGroup.setStatus('current')
dialCtlPeerCfgSpeed = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgSpeed.setStatus('current')
dialCtlPeerCfgInfoType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), ("fax", 10))).clone('other')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgInfoType.setStatus('current')
dialCtlPeerCfgPermission = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("originate", 1), ("answer", 2), ("both", 3), ("callback", 4), ("none", 5))).clone('both')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgPermission.setStatus('current')
dialCtlPeerCfgInactivityTimer = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgInactivityTimer.setStatus('current')
dialCtlPeerCfgMinDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgMinDuration.setStatus('current')
dialCtlPeerCfgMaxDuration = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgMaxDuration.setStatus('current')
dialCtlPeerCfgCarrierDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgCarrierDelay.setStatus('current')
dialCtlPeerCfgCallRetries = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgCallRetries.setStatus('current')
dialCtlPeerCfgRetryDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 16), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgRetryDelay.setStatus('current')
dialCtlPeerCfgFailureDelay = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgFailureDelay.setStatus('current')
dialCtlPeerCfgTrapEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgTrapEnable.setStatus('current')
dialCtlPeerCfgStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dialCtlPeerCfgStatus.setStatus('current')
dialCtlPeerStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2), )
if mibBuilder.loadTexts: dialCtlPeerStatsTable.setStatus('current')
dialCtlPeerStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1), )
dialCtlPeerCfgEntry.registerAugmentions(("DIAL-CONTROL-MIB", "dialCtlPeerStatsEntry"))
dialCtlPeerStatsEntry.setIndexNames(*dialCtlPeerCfgEntry.getIndexNames())
if mibBuilder.loadTexts: dialCtlPeerStatsEntry.setStatus('current')
dialCtlPeerStatsConnectTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 1), AbsoluteCounter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlPeerStatsConnectTime.setStatus('current')
dialCtlPeerStatsChargedUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 2), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlPeerStatsChargedUnits.setStatus('current')
dialCtlPeerStatsSuccessCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 3), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlPeerStatsSuccessCalls.setStatus('current')
dialCtlPeerStatsFailCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 4), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlPeerStatsFailCalls.setStatus('current')
dialCtlPeerStatsAcceptCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 5), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlPeerStatsAcceptCalls.setStatus('current')
dialCtlPeerStatsRefuseCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 6), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlPeerStatsRefuseCalls.setStatus('current')
dialCtlPeerStatsLastDisconnectCause = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlPeerStatsLastDisconnectCause.setStatus('current')
dialCtlPeerStatsLastDisconnectText = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlPeerStatsLastDisconnectText.setStatus('current')
dialCtlPeerStatsLastSetupTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dialCtlPeerStatsLastSetupTime.setStatus('current')
callActive = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 1, 3))
callActiveTable = MibTable((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1), )
if mibBuilder.loadTexts: callActiveTable.setStatus('current')
callActiveEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1), ).setIndexNames((0, "DIAL-CONTROL-MIB", "callActiveSetupTime"), (0, "DIAL-CONTROL-MIB", "callActiveIndex"))
if mibBuilder.loadTexts: callActiveEntry.setStatus('current')
callActiveSetupTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 1), TimeStamp())
if mibBuilder.loadTexts: callActiveSetupTime.setStatus('current')
callActiveIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: callActiveIndex.setStatus('current')
callActivePeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActivePeerAddress.setStatus('current')
callActivePeerSubAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActivePeerSubAddress.setStatus('current')
callActivePeerId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActivePeerId.setStatus('current')
callActivePeerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActivePeerIfIndex.setStatus('current')
callActiveLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActiveLogicalIfIndex.setStatus('current')
callActiveConnectTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActiveConnectTime.setStatus('current')
callActiveCallState = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("connecting", 2), ("connected", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActiveCallState.setStatus('current')
callActiveCallOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("originate", 1), ("answer", 2), ("callback", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActiveCallOrigin.setStatus('current')
callActiveChargedUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 11), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActiveChargedUnits.setStatus('current')
callActiveInfoType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), ("fax", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActiveInfoType.setStatus('current')
callActiveTransmitPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 13), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActiveTransmitPackets.setStatus('current')
callActiveTransmitBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 14), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActiveTransmitBytes.setStatus('current')
callActiveReceivePackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 15), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActiveReceivePackets.setStatus('current')
callActiveReceiveBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 16), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callActiveReceiveBytes.setStatus('current')
callHistory = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 1, 4))
callHistoryTableMaxLength = MibScalar((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: callHistoryTableMaxLength.setStatus('current')
callHistoryRetainTimer = MibScalar((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('minutes').setMaxAccess("readwrite")
if mibBuilder.loadTexts: callHistoryRetainTimer.setStatus('current')
callHistoryTable = MibTable((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3), )
if mibBuilder.loadTexts: callHistoryTable.setStatus('current')
callHistoryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1), ).setIndexNames((0, "DIAL-CONTROL-MIB", "callActiveSetupTime"), (0, "DIAL-CONTROL-MIB", "callActiveIndex"))
if mibBuilder.loadTexts: callHistoryEntry.setStatus('current')
callHistoryPeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryPeerAddress.setStatus('current')
callHistoryPeerSubAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryPeerSubAddress.setStatus('current')
callHistoryPeerId = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryPeerId.setStatus('current')
callHistoryPeerIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryPeerIfIndex.setStatus('current')
callHistoryLogicalIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 5), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryLogicalIfIndex.setStatus('current')
callHistoryDisconnectCause = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryDisconnectCause.setStatus('current')
callHistoryDisconnectText = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryDisconnectText.setStatus('current')
callHistoryConnectTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryConnectTime.setStatus('current')
callHistoryDisconnectTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryDisconnectTime.setStatus('current')
callHistoryCallOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("originate", 1), ("answer", 2), ("callback", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryCallOrigin.setStatus('current')
callHistoryChargedUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 11), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryChargedUnits.setStatus('current')
callHistoryInfoType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("other", 1), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9), ("fax", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryInfoType.setStatus('current')
callHistoryTransmitPackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 13), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryTransmitPackets.setStatus('current')
callHistoryTransmitBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 14), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryTransmitBytes.setStatus('current')
callHistoryReceivePackets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 15), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryReceivePackets.setStatus('current')
callHistoryReceiveBytes = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 16), AbsoluteCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: callHistoryReceiveBytes.setStatus('current')
dialControlMibTrapPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 2))
dialControlMibTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 2, 0))
dialCtlPeerCallInformation = NotificationType((1, 3, 6, 1, 2, 1, 10, 21, 2, 0, 1)).setObjects(("DIAL-CONTROL-MIB", "callHistoryPeerId"), ("DIAL-CONTROL-MIB", "callHistoryPeerIfIndex"), ("DIAL-CONTROL-MIB", "callHistoryLogicalIfIndex"), ("IF-MIB", "ifOperStatus"), ("DIAL-CONTROL-MIB", "callHistoryPeerAddress"), ("DIAL-CONTROL-MIB", "callHistoryPeerSubAddress"), ("DIAL-CONTROL-MIB", "callHistoryDisconnectCause"), ("DIAL-CONTROL-MIB", "callHistoryConnectTime"), ("DIAL-CONTROL-MIB", "callHistoryDisconnectTime"), ("DIAL-CONTROL-MIB", "callHistoryInfoType"), ("DIAL-CONTROL-MIB", "callHistoryCallOrigin"))
if mibBuilder.loadTexts: dialCtlPeerCallInformation.setStatus('current')
dialCtlPeerCallSetup = NotificationType((1, 3, 6, 1, 2, 1, 10, 21, 2, 0, 2)).setObjects(("DIAL-CONTROL-MIB", "callActivePeerId"), ("DIAL-CONTROL-MIB", "callActivePeerIfIndex"), ("DIAL-CONTROL-MIB", "callActiveLogicalIfIndex"), ("IF-MIB", "ifOperStatus"), ("DIAL-CONTROL-MIB", "callActivePeerAddress"), ("DIAL-CONTROL-MIB", "callActivePeerSubAddress"), ("DIAL-CONTROL-MIB", "callActiveInfoType"), ("DIAL-CONTROL-MIB", "callActiveCallOrigin"))
if mibBuilder.loadTexts: dialCtlPeerCallSetup.setStatus('current')
dialControlMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 3))
dialControlMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 3, 1))
dialControlMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 21, 3, 2))
dialControlMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 21, 3, 1, 1)).setObjects(("DIAL-CONTROL-MIB", "dialControlGroup"), ("DIAL-CONTROL-MIB", "callActiveGroup"), ("DIAL-CONTROL-MIB", "callHistoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dialControlMibCompliance = dialControlMibCompliance.setStatus('current')
dialControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 1)).setObjects(("DIAL-CONTROL-MIB", "dialCtlAcceptMode"), ("DIAL-CONTROL-MIB", "dialCtlTrapEnable"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgIfType"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgLowerIf"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgOriginateAddress"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgAnswerAddress"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgSubAddress"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgClosedUserGroup"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgSpeed"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgInfoType"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgPermission"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgInactivityTimer"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgMinDuration"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgMaxDuration"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgCarrierDelay"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgCallRetries"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgRetryDelay"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgFailureDelay"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgTrapEnable"), ("DIAL-CONTROL-MIB", "dialCtlPeerCfgStatus"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsConnectTime"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsChargedUnits"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsSuccessCalls"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsFailCalls"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsAcceptCalls"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsRefuseCalls"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsLastDisconnectCause"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsLastDisconnectText"), ("DIAL-CONTROL-MIB", "dialCtlPeerStatsLastSetupTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dialControlGroup = dialControlGroup.setStatus('current')
callActiveGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 2)).setObjects(("DIAL-CONTROL-MIB", "callActivePeerAddress"), ("DIAL-CONTROL-MIB", "callActivePeerSubAddress"), ("DIAL-CONTROL-MIB", "callActivePeerId"), ("DIAL-CONTROL-MIB", "callActivePeerIfIndex"), ("DIAL-CONTROL-MIB", "callActiveLogicalIfIndex"), ("DIAL-CONTROL-MIB", "callActiveConnectTime"), ("DIAL-CONTROL-MIB", "callActiveCallState"), ("DIAL-CONTROL-MIB", "callActiveCallOrigin"), ("DIAL-CONTROL-MIB", "callActiveChargedUnits"), ("DIAL-CONTROL-MIB", "callActiveInfoType"), ("DIAL-CONTROL-MIB", "callActiveTransmitPackets"), ("DIAL-CONTROL-MIB", "callActiveTransmitBytes"), ("DIAL-CONTROL-MIB", "callActiveReceivePackets"), ("DIAL-CONTROL-MIB", "callActiveReceiveBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    callActiveGroup = callActiveGroup.setStatus('current')
callHistoryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 3)).setObjects(("DIAL-CONTROL-MIB", "callHistoryTableMaxLength"), ("DIAL-CONTROL-MIB", "callHistoryRetainTimer"), ("DIAL-CONTROL-MIB", "callHistoryPeerAddress"), ("DIAL-CONTROL-MIB", "callHistoryPeerSubAddress"), ("DIAL-CONTROL-MIB", "callHistoryPeerId"), ("DIAL-CONTROL-MIB", "callHistoryPeerIfIndex"), ("DIAL-CONTROL-MIB", "callHistoryLogicalIfIndex"), ("DIAL-CONTROL-MIB", "callHistoryDisconnectCause"), ("DIAL-CONTROL-MIB", "callHistoryDisconnectText"), ("DIAL-CONTROL-MIB", "callHistoryConnectTime"), ("DIAL-CONTROL-MIB", "callHistoryDisconnectTime"), ("DIAL-CONTROL-MIB", "callHistoryCallOrigin"), ("DIAL-CONTROL-MIB", "callHistoryChargedUnits"), ("DIAL-CONTROL-MIB", "callHistoryInfoType"), ("DIAL-CONTROL-MIB", "callHistoryTransmitPackets"), ("DIAL-CONTROL-MIB", "callHistoryTransmitBytes"), ("DIAL-CONTROL-MIB", "callHistoryReceivePackets"), ("DIAL-CONTROL-MIB", "callHistoryReceiveBytes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    callHistoryGroup = callHistoryGroup.setStatus('current')
mibBuilder.exportSymbols("DIAL-CONTROL-MIB", dialCtlPeerStatsConnectTime=dialCtlPeerStatsConnectTime, dialCtlPeerCallSetup=dialCtlPeerCallSetup, PYSNMP_MODULE_ID=dialControlMib, dialCtlPeerStatsRefuseCalls=dialCtlPeerStatsRefuseCalls, callHistoryTransmitBytes=callHistoryTransmitBytes, callHistoryReceivePackets=callHistoryReceivePackets, dialCtlPeerCfgCarrierDelay=dialCtlPeerCfgCarrierDelay, callActiveTable=callActiveTable, callActivePeerIfIndex=callActivePeerIfIndex, callActiveGroup=callActiveGroup, dialCtlPeerCfgSubAddress=dialCtlPeerCfgSubAddress, dialCtlPeerStatsLastSetupTime=dialCtlPeerStatsLastSetupTime, dialCtlPeerCfgClosedUserGroup=dialCtlPeerCfgClosedUserGroup, dialControlMib=dialControlMib, dialCtlPeerCfgLowerIf=dialCtlPeerCfgLowerIf, callActive=callActive, dialCtlPeerCfgInactivityTimer=dialCtlPeerCfgInactivityTimer, dialCtlPeerCfgPermission=dialCtlPeerCfgPermission, dialControlMibGroups=dialControlMibGroups, callActiveSetupTime=callActiveSetupTime, callActivePeerSubAddress=callActivePeerSubAddress, callActiveTransmitPackets=callActiveTransmitPackets, dialCtlPeerCfgAnswerAddress=dialCtlPeerCfgAnswerAddress, dialControlMibTraps=dialControlMibTraps, dialCtlPeerCfgStatus=dialCtlPeerCfgStatus, dialCtlPeerStatsAcceptCalls=dialCtlPeerStatsAcceptCalls, callHistoryChargedUnits=callHistoryChargedUnits, dialCtlPeerStatsSuccessCalls=dialCtlPeerStatsSuccessCalls, callHistoryCallOrigin=callHistoryCallOrigin, dialCtlPeerStatsTable=dialCtlPeerStatsTable, dialCtlPeerCfgMinDuration=dialCtlPeerCfgMinDuration, callActiveReceiveBytes=callActiveReceiveBytes, callActiveTransmitBytes=callActiveTransmitBytes, callActiveCallState=callActiveCallState, callHistoryPeerIfIndex=callHistoryPeerIfIndex, dialCtlPeer=dialCtlPeer, dialCtlPeerCfgTrapEnable=dialCtlPeerCfgTrapEnable, dialControlMibConformance=dialControlMibConformance, callHistoryDisconnectCause=callHistoryDisconnectCause, callHistoryPeerId=callHistoryPeerId, dialControlMibObjects=dialControlMibObjects, callHistory=callHistory, dialCtlAcceptMode=dialCtlAcceptMode, dialCtlPeerCfgId=dialCtlPeerCfgId, callHistoryConnectTime=callHistoryConnectTime, dialCtlPeerStatsEntry=dialCtlPeerStatsEntry, callActivePeerAddress=callActivePeerAddress, dialCtlPeerCfgEntry=dialCtlPeerCfgEntry, callActiveReceivePackets=callActiveReceivePackets, callHistoryTransmitPackets=callHistoryTransmitPackets, dialCtlPeerCfgIfType=dialCtlPeerCfgIfType, callActiveInfoType=callActiveInfoType, callHistoryRetainTimer=callHistoryRetainTimer, dialCtlPeerCallInformation=dialCtlPeerCallInformation, callActiveLogicalIfIndex=callActiveLogicalIfIndex, dialControlMibCompliances=dialControlMibCompliances, callHistoryTableMaxLength=callHistoryTableMaxLength, AbsoluteCounter32=AbsoluteCounter32, dialCtlPeerCfgCallRetries=dialCtlPeerCfgCallRetries, dialCtlPeerCfgRetryDelay=dialCtlPeerCfgRetryDelay, callHistoryReceiveBytes=callHistoryReceiveBytes, callHistoryInfoType=callHistoryInfoType, callActiveConnectTime=callActiveConnectTime, dialControlMibTrapPrefix=dialControlMibTrapPrefix, callHistoryDisconnectTime=callHistoryDisconnectTime, callHistoryTable=callHistoryTable, dialCtlPeerCfgOriginateAddress=dialCtlPeerCfgOriginateAddress, callHistoryPeerAddress=callHistoryPeerAddress, dialCtlPeerStatsChargedUnits=dialCtlPeerStatsChargedUnits, callHistoryLogicalIfIndex=callHistoryLogicalIfIndex, dialCtlConfiguration=dialCtlConfiguration, callHistoryPeerSubAddress=callHistoryPeerSubAddress, dialControlGroup=dialControlGroup, dialCtlPeerCfgTable=dialCtlPeerCfgTable, callActiveIndex=callActiveIndex, dialCtlTrapEnable=dialCtlTrapEnable, callActiveEntry=callActiveEntry, callActivePeerId=callActivePeerId, callHistoryGroup=callHistoryGroup, dialCtlPeerStatsLastDisconnectCause=dialCtlPeerStatsLastDisconnectCause, dialCtlPeerCfgFailureDelay=dialCtlPeerCfgFailureDelay, dialControlMibCompliance=dialControlMibCompliance, dialCtlPeerStatsLastDisconnectText=dialCtlPeerStatsLastDisconnectText, callActiveCallOrigin=callActiveCallOrigin, callActiveChargedUnits=callActiveChargedUnits, callHistoryDisconnectText=callHistoryDisconnectText, dialCtlPeerStatsFailCalls=dialCtlPeerStatsFailCalls, dialCtlPeerCfgInfoType=dialCtlPeerCfgInfoType, dialCtlPeerCfgSpeed=dialCtlPeerCfgSpeed, dialCtlPeerCfgMaxDuration=dialCtlPeerCfgMaxDuration, callHistoryEntry=callHistoryEntry)
