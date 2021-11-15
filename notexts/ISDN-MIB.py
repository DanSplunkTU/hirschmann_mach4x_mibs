#
# PySNMP MIB module ISDN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ISDN-MIB
# Produced by pysmi-1.1.0 at Mon Nov 15 18:46:22 2021
# On host fv-az77-248 platform Linux version 5.11.0-1020-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, ModuleIdentity, Bits, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, TimeTicks, Integer32, Gauge32, Counter64, transmission, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Bits", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "TimeTicks", "Integer32", "Gauge32", "Counter64", "transmission", "ObjectIdentity", "NotificationType")
TruthValue, DisplayString, TimeStamp, TextualConvention, RowStatus, TestAndIncr = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TimeStamp", "TextualConvention", "RowStatus", "TestAndIncr")
isdnMib = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 20))
if mibBuilder.loadTexts: isdnMib.setLastUpdated('9609231642Z')
if mibBuilder.loadTexts: isdnMib.setOrganization('IETF ISDN MIB Working Group')
class IsdnSignalingProtocol(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))
    namedValues = NamedValues(("other", 1), ("dss1", 2), ("etsi", 3), ("dass2", 4), ("ess4", 5), ("ess5", 6), ("dms100", 7), ("dms250", 8), ("ni1", 9), ("ni2", 10), ("ni3", 11), ("vn2", 12), ("vn3", 13), ("vn4", 14), ("vn6", 15), ("kdd", 16), ("ins64", 17), ("ins1500", 18), ("itr6", 19), ("cornet", 20), ("ts013", 21), ("ts014", 22), ("qsig", 23), ("swissnet2", 24), ("swissnet3", 25))

isdnMibObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1))
isdnBasicRateGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1, 1))
isdnBasicRateTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1), )
if mibBuilder.loadTexts: isdnBasicRateTable.setStatus('current')
isdnBasicRateEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: isdnBasicRateEntry.setStatus('current')
isdnBasicRateIfType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(75, 76))).clone(namedValues=NamedValues(("isdns", 75), ("isdnu", 76)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnBasicRateIfType.setStatus('current')
isdnBasicRateLineTopology = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pointToPoint", 1), ("pointToMultipoint", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnBasicRateLineTopology.setStatus('current')
isdnBasicRateIfMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("te", 1), ("nt", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnBasicRateIfMode.setStatus('current')
isdnBasicRateSignalMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnBasicRateSignalMode.setStatus('current')
isdnBearerGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1, 2))
isdnBearerTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1), )
if mibBuilder.loadTexts: isdnBearerTable.setStatus('current')
isdnBearerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: isdnBearerEntry.setStatus('current')
isdnBearerChannelType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dialup", 1), ("leased", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnBearerChannelType.setStatus('current')
isdnBearerOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("idle", 1), ("connecting", 2), ("connected", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerOperStatus.setStatus('current')
isdnBearerChannelNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerChannelNumber.setStatus('current')
isdnBearerPeerAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerPeerAddress.setStatus('current')
isdnBearerPeerSubAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerPeerSubAddress.setStatus('current')
isdnBearerCallOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("originate", 2), ("answer", 3), ("callback", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerCallOrigin.setStatus('current')
isdnBearerInfoType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unknown", 1), ("speech", 2), ("unrestrictedDigital", 3), ("unrestrictedDigital56", 4), ("restrictedDigital", 5), ("audio31", 6), ("audio7", 7), ("video", 8), ("packetSwitched", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerInfoType.setStatus('current')
isdnBearerMultirate = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerMultirate.setStatus('current')
isdnBearerCallSetupTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerCallSetupTime.setStatus('current')
isdnBearerCallConnectTime = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerCallConnectTime.setStatus('current')
isdnBearerChargedUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 2, 1, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnBearerChargedUnits.setStatus('current')
isdnSignalingGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1, 3))
isdnSignalingGetIndex = MibScalar((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnSignalingGetIndex.setStatus('current')
isdnSignalingTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2), )
if mibBuilder.loadTexts: isdnSignalingTable.setStatus('current')
isdnSignalingEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1), ).setIndexNames((0, "ISDN-MIB", "isdnSignalingIndex"))
if mibBuilder.loadTexts: isdnSignalingEntry.setStatus('current')
isdnSignalingIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: isdnSignalingIndex.setStatus('current')
isdnSignalingIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSignalingIfIndex.setStatus('current')
isdnSignalingProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 3), IsdnSignalingProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingProtocol.setStatus('current')
isdnSignalingCallingAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingCallingAddress.setStatus('current')
isdnSignalingSubAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingSubAddress.setStatus('current')
isdnSignalingBchannelCount = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingBchannelCount.setStatus('current')
isdnSignalingInfoTrapEnable = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingInfoTrapEnable.setStatus('current')
isdnSignalingStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 2, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnSignalingStatus.setStatus('current')
isdnSignalingStatsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3), )
if mibBuilder.loadTexts: isdnSignalingStatsTable.setStatus('current')
isdnSignalingStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1), )
isdnSignalingEntry.registerAugmentions(("ISDN-MIB", "isdnSignalingStatsEntry"))
isdnSignalingStatsEntry.setIndexNames(*isdnSignalingEntry.getIndexNames())
if mibBuilder.loadTexts: isdnSignalingStatsEntry.setStatus('current')
isdnSigStatsInCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSigStatsInCalls.setStatus('current')
isdnSigStatsInConnected = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSigStatsInConnected.setStatus('current')
isdnSigStatsOutCalls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSigStatsOutCalls.setStatus('current')
isdnSigStatsOutConnected = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSigStatsOutConnected.setStatus('current')
isdnSigStatsChargedUnits = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnSigStatsChargedUnits.setStatus('current')
isdnLapdTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4), )
if mibBuilder.loadTexts: isdnLapdTable.setStatus('current')
isdnLapdEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: isdnLapdEntry.setStatus('current')
isdnLapdPrimaryChannel = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnLapdPrimaryChannel.setStatus('current')
isdnLapdOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("inactive", 1), ("l1Active", 2), ("l2Active", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnLapdOperStatus.setStatus('current')
isdnLapdPeerSabme = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnLapdPeerSabme.setStatus('current')
isdnLapdRecvdFrmr = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 3, 4, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnLapdRecvdFrmr.setStatus('current')
isdnEndpointGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1, 4))
isdnEndpointGetIndex = MibScalar((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: isdnEndpointGetIndex.setStatus('current')
isdnEndpointTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2), )
if mibBuilder.loadTexts: isdnEndpointTable.setStatus('current')
isdnEndpointEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1), ).setIndexNames((0, "ISDN-MIB", "isdnEndpointIndex"))
if mibBuilder.loadTexts: isdnEndpointEntry.setStatus('current')
isdnEndpointIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: isdnEndpointIndex.setStatus('current')
isdnEndpointIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: isdnEndpointIfIndex.setStatus('current')
isdnEndpointIfType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 3), IANAifType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointIfType.setStatus('current')
isdnEndpointTeiType = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dynamic", 1), ("static", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointTeiType.setStatus('current')
isdnEndpointTeiValue = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointTeiValue.setStatus('current')
isdnEndpointSpid = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 6), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointSpid.setStatus('current')
isdnEndpointStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 4, 2, 1, 7), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnEndpointStatus.setStatus('current')
isdnDirectoryGroup = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 1, 5))
isdnDirectoryTable = MibTable((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1), )
if mibBuilder.loadTexts: isdnDirectoryTable.setStatus('current')
isdnDirectoryEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1), ).setIndexNames((0, "ISDN-MIB", "isdnDirectoryIndex"))
if mibBuilder.loadTexts: isdnDirectoryEntry.setStatus('current')
isdnDirectoryIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: isdnDirectoryIndex.setStatus('current')
isdnDirectoryNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnDirectoryNumber.setStatus('current')
isdnDirectorySigIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnDirectorySigIndex.setStatus('current')
isdnDirectoryStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 20, 1, 5, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: isdnDirectoryStatus.setStatus('current')
isdnMibTrapPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 2))
isdnMibTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 2, 0))
isdnMibCallInformation = NotificationType((1, 3, 6, 1, 2, 1, 10, 20, 2, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("ISDN-MIB", "isdnBearerOperStatus"), ("ISDN-MIB", "isdnBearerPeerAddress"), ("ISDN-MIB", "isdnBearerPeerSubAddress"), ("ISDN-MIB", "isdnBearerCallSetupTime"), ("ISDN-MIB", "isdnBearerInfoType"), ("ISDN-MIB", "isdnBearerCallOrigin"))
if mibBuilder.loadTexts: isdnMibCallInformation.setStatus('current')
isdnMibConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 3))
isdnMibCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 3, 1))
isdnMibGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 20, 3, 2))
isdnMibCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 20, 3, 1, 1)).setObjects(("ISDN-MIB", "isdnMibSignalingGroup"), ("ISDN-MIB", "isdnMibBearerGroup"), ("ISDN-MIB", "isdnMibBasicRateGroup"), ("ISDN-MIB", "isdnMibEndpointGroup"), ("ISDN-MIB", "isdnMibDirectoryGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isdnMibCompliance = isdnMibCompliance.setStatus('current')
isdnMibBasicRateGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 20, 3, 2, 1)).setObjects(("ISDN-MIB", "isdnBasicRateIfType"), ("ISDN-MIB", "isdnBasicRateLineTopology"), ("ISDN-MIB", "isdnBasicRateIfMode"), ("ISDN-MIB", "isdnBasicRateSignalMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isdnMibBasicRateGroup = isdnMibBasicRateGroup.setStatus('current')
isdnMibBearerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 20, 3, 2, 2)).setObjects(("ISDN-MIB", "isdnBearerChannelType"), ("ISDN-MIB", "isdnBearerOperStatus"), ("ISDN-MIB", "isdnBearerChannelNumber"), ("ISDN-MIB", "isdnBearerPeerAddress"), ("ISDN-MIB", "isdnBearerPeerSubAddress"), ("ISDN-MIB", "isdnBearerCallOrigin"), ("ISDN-MIB", "isdnBearerInfoType"), ("ISDN-MIB", "isdnBearerMultirate"), ("ISDN-MIB", "isdnBearerCallSetupTime"), ("ISDN-MIB", "isdnBearerCallConnectTime"), ("ISDN-MIB", "isdnBearerChargedUnits"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isdnMibBearerGroup = isdnMibBearerGroup.setStatus('current')
isdnMibSignalingGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 20, 3, 2, 3)).setObjects(("ISDN-MIB", "isdnSignalingGetIndex"), ("ISDN-MIB", "isdnSignalingIfIndex"), ("ISDN-MIB", "isdnSignalingProtocol"), ("ISDN-MIB", "isdnSignalingCallingAddress"), ("ISDN-MIB", "isdnSignalingSubAddress"), ("ISDN-MIB", "isdnSignalingBchannelCount"), ("ISDN-MIB", "isdnSignalingInfoTrapEnable"), ("ISDN-MIB", "isdnSignalingStatus"), ("ISDN-MIB", "isdnSigStatsInCalls"), ("ISDN-MIB", "isdnSigStatsInConnected"), ("ISDN-MIB", "isdnSigStatsOutCalls"), ("ISDN-MIB", "isdnSigStatsOutConnected"), ("ISDN-MIB", "isdnSigStatsChargedUnits"), ("ISDN-MIB", "isdnLapdPrimaryChannel"), ("ISDN-MIB", "isdnLapdOperStatus"), ("ISDN-MIB", "isdnLapdPeerSabme"), ("ISDN-MIB", "isdnLapdRecvdFrmr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isdnMibSignalingGroup = isdnMibSignalingGroup.setStatus('current')
isdnMibEndpointGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 20, 3, 2, 4)).setObjects(("ISDN-MIB", "isdnEndpointGetIndex"), ("ISDN-MIB", "isdnEndpointIfIndex"), ("ISDN-MIB", "isdnEndpointIfType"), ("ISDN-MIB", "isdnEndpointTeiType"), ("ISDN-MIB", "isdnEndpointTeiValue"), ("ISDN-MIB", "isdnEndpointSpid"), ("ISDN-MIB", "isdnEndpointStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isdnMibEndpointGroup = isdnMibEndpointGroup.setStatus('current')
isdnMibDirectoryGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 20, 3, 2, 5)).setObjects(("ISDN-MIB", "isdnDirectoryNumber"), ("ISDN-MIB", "isdnDirectorySigIndex"), ("ISDN-MIB", "isdnDirectoryStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    isdnMibDirectoryGroup = isdnMibDirectoryGroup.setStatus('current')
mibBuilder.exportSymbols("ISDN-MIB", IsdnSignalingProtocol=IsdnSignalingProtocol, isdnBasicRateTable=isdnBasicRateTable, isdnMib=isdnMib, isdnMibBearerGroup=isdnMibBearerGroup, isdnBearerCallSetupTime=isdnBearerCallSetupTime, isdnEndpointTeiType=isdnEndpointTeiType, isdnLapdPeerSabme=isdnLapdPeerSabme, isdnBearerCallConnectTime=isdnBearerCallConnectTime, isdnEndpointIfType=isdnEndpointIfType, isdnBasicRateIfType=isdnBasicRateIfType, isdnMibSignalingGroup=isdnMibSignalingGroup, isdnBearerCallOrigin=isdnBearerCallOrigin, PYSNMP_MODULE_ID=isdnMib, isdnMibTrapPrefix=isdnMibTrapPrefix, isdnSignalingIfIndex=isdnSignalingIfIndex, isdnDirectoryNumber=isdnDirectoryNumber, isdnBearerPeerSubAddress=isdnBearerPeerSubAddress, isdnDirectoryGroup=isdnDirectoryGroup, isdnMibBasicRateGroup=isdnMibBasicRateGroup, isdnMibGroups=isdnMibGroups, isdnBearerEntry=isdnBearerEntry, isdnEndpointTable=isdnEndpointTable, isdnLapdRecvdFrmr=isdnLapdRecvdFrmr, isdnSignalingStatsEntry=isdnSignalingStatsEntry, isdnEndpointIfIndex=isdnEndpointIfIndex, isdnSignalingIndex=isdnSignalingIndex, isdnDirectoryStatus=isdnDirectoryStatus, isdnSigStatsInConnected=isdnSigStatsInConnected, isdnSigStatsOutCalls=isdnSigStatsOutCalls, isdnBearerMultirate=isdnBearerMultirate, isdnSignalingStatsTable=isdnSignalingStatsTable, isdnMibConformance=isdnMibConformance, isdnSignalingSubAddress=isdnSignalingSubAddress, isdnEndpointGroup=isdnEndpointGroup, isdnSignalingGetIndex=isdnSignalingGetIndex, isdnMibCompliances=isdnMibCompliances, isdnLapdEntry=isdnLapdEntry, isdnBasicRateSignalMode=isdnBasicRateSignalMode, isdnBearerChannelNumber=isdnBearerChannelNumber, isdnSignalingTable=isdnSignalingTable, isdnBasicRateLineTopology=isdnBasicRateLineTopology, isdnEndpointGetIndex=isdnEndpointGetIndex, isdnBasicRateIfMode=isdnBasicRateIfMode, isdnEndpointSpid=isdnEndpointSpid, isdnSignalingProtocol=isdnSignalingProtocol, isdnMibTraps=isdnMibTraps, isdnSignalingStatus=isdnSignalingStatus, isdnDirectoryEntry=isdnDirectoryEntry, isdnBearerPeerAddress=isdnBearerPeerAddress, isdnBearerChannelType=isdnBearerChannelType, isdnEndpointStatus=isdnEndpointStatus, isdnSignalingInfoTrapEnable=isdnSignalingInfoTrapEnable, isdnDirectoryTable=isdnDirectoryTable, isdnSigStatsChargedUnits=isdnSigStatsChargedUnits, isdnLapdOperStatus=isdnLapdOperStatus, isdnMibEndpointGroup=isdnMibEndpointGroup, isdnBasicRateEntry=isdnBasicRateEntry, isdnMibCompliance=isdnMibCompliance, isdnMibCallInformation=isdnMibCallInformation, isdnDirectorySigIndex=isdnDirectorySigIndex, isdnEndpointTeiValue=isdnEndpointTeiValue, isdnSignalingBchannelCount=isdnSignalingBchannelCount, isdnBearerOperStatus=isdnBearerOperStatus, isdnLapdTable=isdnLapdTable, isdnSigStatsInCalls=isdnSigStatsInCalls, isdnSigStatsOutConnected=isdnSigStatsOutConnected, isdnEndpointEntry=isdnEndpointEntry, isdnBearerTable=isdnBearerTable, isdnLapdPrimaryChannel=isdnLapdPrimaryChannel, isdnEndpointIndex=isdnEndpointIndex, isdnSignalingGroup=isdnSignalingGroup, isdnMibObjects=isdnMibObjects, isdnSignalingCallingAddress=isdnSignalingCallingAddress, isdnBearerChargedUnits=isdnBearerChargedUnits, isdnBearerInfoType=isdnBearerInfoType, isdnBearerGroup=isdnBearerGroup, isdnDirectoryIndex=isdnDirectoryIndex, isdnSignalingEntry=isdnSignalingEntry, isdnMibDirectoryGroup=isdnMibDirectoryGroup, isdnBasicRateGroup=isdnBasicRateGroup)
