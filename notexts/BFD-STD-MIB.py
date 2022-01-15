#
# PySNMP MIB module BFD-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/BFD-STD-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
BfdMultiplierTC, BfdCtrlDestPortNumberTC, BfdIntervalTC, BfdCtrlSourcePortNumberTC, BfdSessIndexTC = mibBuilder.importSymbols("BFD-TC-STD-MIB", "BfdMultiplierTC", "BfdCtrlDestPortNumberTC", "BfdIntervalTC", "BfdCtrlSourcePortNumberTC", "BfdSessIndexTC")
IndexIntegerNextFree, = mibBuilder.importSymbols("DIFFSERV-DSCP-TC", "IndexIntegerNextFree")
IANAbfdSessAuthenticationTypeTC, IANAbfdDiagTC, IANAbfdSessAuthenticationKeyTC, IANAbfdSessOperModeTC, IANAbfdSessTypeTC, IANAbfdSessStateTC = mibBuilder.importSymbols("IANA-BFD-TC-STD-MIB", "IANAbfdSessAuthenticationTypeTC", "IANAbfdDiagTC", "IANAbfdSessAuthenticationKeyTC", "IANAbfdSessOperModeTC", "IANAbfdSessTypeTC", "IANAbfdSessStateTC")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, mib_2, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "mib-2", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
StorageType, DisplayString, TimeStamp, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "TimeStamp", "RowStatus", "TextualConvention", "TruthValue")
bfdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 222))
bfdMIB.setRevisions(('2014-08-12 00:00',))
if mibBuilder.loadTexts: bfdMIB.setLastUpdated('201408120000Z')
if mibBuilder.loadTexts: bfdMIB.setOrganization('IETF Bidirectional Forwarding Detection Working Group')
bfdNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 222, 0))
bfdObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 222, 1))
bfdConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 222, 2))
bfdScalarObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 222, 1, 1))
bfdAdminStatus = MibScalar((1, 3, 6, 1, 2, 1, 222, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("adminDown", 3), ("down", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdAdminStatus.setStatus('current')
bfdOperStatus = MibScalar((1, 3, 6, 1, 2, 1, 222, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("adminDown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdOperStatus.setStatus('current')
bfdNotificationsEnable = MibScalar((1, 3, 6, 1, 2, 1, 222, 1, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bfdNotificationsEnable.setStatus('current')
bfdSessIndexNext = MibScalar((1, 3, 6, 1, 2, 1, 222, 1, 1, 4), IndexIntegerNextFree().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessIndexNext.setStatus('current')
bfdSessTable = MibTable((1, 3, 6, 1, 2, 1, 222, 1, 2), )
if mibBuilder.loadTexts: bfdSessTable.setStatus('current')
bfdSessEntry = MibTableRow((1, 3, 6, 1, 2, 1, 222, 1, 2, 1), ).setIndexNames((0, "BFD-STD-MIB", "bfdSessIndex"))
if mibBuilder.loadTexts: bfdSessEntry.setStatus('current')
bfdSessIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 1), BfdSessIndexTC())
if mibBuilder.loadTexts: bfdSessIndex.setStatus('current')
bfdSessVersionNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessVersionNumber.setStatus('current')
bfdSessType = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 3), IANAbfdSessTypeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessType.setStatus('current')
bfdSessDiscriminator = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDiscriminator.setStatus('current')
bfdSessRemoteDiscr = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 5), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessRemoteDiscr.setStatus('current')
bfdSessDestinationUdpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 6), BfdCtrlDestPortNumberTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDestinationUdpPort.setStatus('current')
bfdSessSourceUdpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 7), BfdCtrlSourcePortNumberTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessSourceUdpPort.setStatus('current')
bfdSessEchoSourceUdpPort = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 8), InetPortNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessEchoSourceUdpPort.setStatus('current')
bfdSessAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("adminDown", 3), ("down", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAdminStatus.setStatus('current')
bfdSessOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("adminDown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessOperStatus.setStatus('current')
bfdSessState = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 11), IANAbfdSessStateTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessState.setStatus('current')
bfdSessRemoteHeardFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessRemoteHeardFlag.setStatus('current')
bfdSessDiag = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 13), IANAbfdDiagTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessDiag.setStatus('current')
bfdSessOperMode = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 14), IANAbfdSessOperModeTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessOperMode.setStatus('current')
bfdSessDemandModeDesiredFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 15), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDemandModeDesiredFlag.setStatus('current')
bfdSessControlPlaneIndepFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 16), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessControlPlaneIndepFlag.setStatus('current')
bfdSessMultipointFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 17), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessMultipointFlag.setStatus('current')
bfdSessInterface = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 18), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessInterface.setStatus('current')
bfdSessSrcAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 19), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessSrcAddrType.setStatus('current')
bfdSessSrcAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 20), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessSrcAddr.setStatus('current')
bfdSessDstAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 21), InetAddressType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDstAddrType.setStatus('current')
bfdSessDstAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 22), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDstAddr.setStatus('current')
bfdSessGTSM = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 23), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessGTSM.setStatus('current')
bfdSessGTSMTTL = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 24), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(255)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessGTSMTTL.setStatus('current')
bfdSessDesiredMinTxInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 25), BfdIntervalTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDesiredMinTxInterval.setStatus('current')
bfdSessReqMinRxInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 26), BfdIntervalTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessReqMinRxInterval.setStatus('current')
bfdSessReqMinEchoRxInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 27), BfdIntervalTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessReqMinEchoRxInterval.setStatus('current')
bfdSessDetectMult = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 28), BfdMultiplierTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessDetectMult.setStatus('current')
bfdSessNegotiatedInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 29), BfdIntervalTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessNegotiatedInterval.setStatus('current')
bfdSessNegotiatedEchoInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 30), BfdIntervalTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessNegotiatedEchoInterval.setStatus('current')
bfdSessNegotiatedDetectMult = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 31), BfdMultiplierTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessNegotiatedDetectMult.setStatus('current')
bfdSessAuthPresFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 32), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAuthPresFlag.setStatus('current')
bfdSessAuthenticationType = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 33), IANAbfdSessAuthenticationTypeTC().clone('noAuthentication')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAuthenticationType.setStatus('current')
bfdSessAuthenticationKeyID = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 34), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 255), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAuthenticationKeyID.setStatus('current')
bfdSessAuthenticationKey = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 35), IANAbfdSessAuthenticationKeyTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessAuthenticationKey.setStatus('current')
bfdSessStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 36), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessStorageType.setStatus('current')
bfdSessRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 2, 1, 37), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: bfdSessRowStatus.setStatus('current')
bfdSessPerfTable = MibTable((1, 3, 6, 1, 2, 1, 222, 1, 3), )
if mibBuilder.loadTexts: bfdSessPerfTable.setStatus('current')
bfdSessPerfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 222, 1, 3, 1), )
bfdSessEntry.registerAugmentions(("BFD-STD-MIB", "bfdSessPerfEntry"))
bfdSessPerfEntry.setIndexNames(*bfdSessEntry.getIndexNames())
if mibBuilder.loadTexts: bfdSessPerfEntry.setStatus('current')
bfdSessPerfCtrlPktIn = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfCtrlPktIn.setStatus('current')
bfdSessPerfCtrlPktOut = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfCtrlPktOut.setStatus('current')
bfdSessPerfCtrlPktDrop = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfCtrlPktDrop.setStatus('current')
bfdSessPerfCtrlPktDropLastTime = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfCtrlPktDropLastTime.setStatus('current')
bfdSessPerfEchoPktIn = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfEchoPktIn.setStatus('current')
bfdSessPerfEchoPktOut = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfEchoPktOut.setStatus('current')
bfdSessPerfEchoPktDrop = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfEchoPktDrop.setStatus('current')
bfdSessPerfEchoPktDropLastTime = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfEchoPktDropLastTime.setStatus('current')
bfdSessUpTime = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessUpTime.setStatus('current')
bfdSessPerfLastSessDownTime = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 10), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfLastSessDownTime.setStatus('current')
bfdSessPerfLastCommLostDiag = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 11), IANAbfdDiagTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfLastCommLostDiag.setStatus('current')
bfdSessPerfSessUpCount = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfSessUpCount.setStatus('current')
bfdSessPerfDiscTime = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 13), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfDiscTime.setStatus('current')
bfdSessPerfCtrlPktInHC = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfCtrlPktInHC.setStatus('current')
bfdSessPerfCtrlPktOutHC = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfCtrlPktOutHC.setStatus('current')
bfdSessPerfCtrlPktDropHC = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfCtrlPktDropHC.setStatus('current')
bfdSessPerfEchoPktInHC = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfEchoPktInHC.setStatus('current')
bfdSessPerfEchoPktOutHC = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfEchoPktOutHC.setStatus('current')
bfdSessPerfEchoPktDropHC = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 3, 1, 19), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessPerfEchoPktDropHC.setStatus('current')
bfdSessDiscMapTable = MibTable((1, 3, 6, 1, 2, 1, 222, 1, 4), )
if mibBuilder.loadTexts: bfdSessDiscMapTable.setStatus('current')
bfdSessDiscMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 222, 1, 4, 1), ).setIndexNames((0, "BFD-STD-MIB", "bfdSessDiscriminator"))
if mibBuilder.loadTexts: bfdSessDiscMapEntry.setStatus('current')
bfdSessDiscMapIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 4, 1, 1), BfdSessIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessDiscMapIndex.setStatus('current')
bfdSessIpMapTable = MibTable((1, 3, 6, 1, 2, 1, 222, 1, 5), )
if mibBuilder.loadTexts: bfdSessIpMapTable.setStatus('current')
bfdSessIpMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 222, 1, 5, 1), ).setIndexNames((0, "BFD-STD-MIB", "bfdSessInterface"), (0, "BFD-STD-MIB", "bfdSessSrcAddrType"), (0, "BFD-STD-MIB", "bfdSessSrcAddr"), (0, "BFD-STD-MIB", "bfdSessDstAddrType"), (0, "BFD-STD-MIB", "bfdSessDstAddr"))
if mibBuilder.loadTexts: bfdSessIpMapEntry.setStatus('current')
bfdSessIpMapIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 222, 1, 5, 1, 1), BfdSessIndexTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bfdSessIpMapIndex.setStatus('current')
bfdSessUp = NotificationType((1, 3, 6, 1, 2, 1, 222, 0, 1)).setObjects(("BFD-STD-MIB", "bfdSessDiag"), ("BFD-STD-MIB", "bfdSessDiag"))
if mibBuilder.loadTexts: bfdSessUp.setStatus('current')
bfdSessDown = NotificationType((1, 3, 6, 1, 2, 1, 222, 0, 2)).setObjects(("BFD-STD-MIB", "bfdSessDiag"), ("BFD-STD-MIB", "bfdSessDiag"))
if mibBuilder.loadTexts: bfdSessDown.setStatus('current')
bfdGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 222, 2, 1))
bfdCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 222, 2, 2))
bfdModuleFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 222, 2, 2, 1)).setObjects(("BFD-STD-MIB", "bfdSessionGroup"), ("BFD-STD-MIB", "bfdSessionReadOnlyGroup"), ("BFD-STD-MIB", "bfdSessionPerfGroup"), ("BFD-STD-MIB", "bfdNotificationGroup"), ("BFD-STD-MIB", "bfdSessionPerfHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdModuleFullCompliance = bfdModuleFullCompliance.setStatus('current')
bfdModuleReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 222, 2, 2, 2)).setObjects(("BFD-STD-MIB", "bfdSessionGroup"), ("BFD-STD-MIB", "bfdSessionReadOnlyGroup"), ("BFD-STD-MIB", "bfdSessionPerfGroup"), ("BFD-STD-MIB", "bfdNotificationGroup"), ("BFD-STD-MIB", "bfdSessionPerfHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdModuleReadOnlyCompliance = bfdModuleReadOnlyCompliance.setStatus('current')
bfdSessionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 222, 2, 1, 1)).setObjects(("BFD-STD-MIB", "bfdAdminStatus"), ("BFD-STD-MIB", "bfdOperStatus"), ("BFD-STD-MIB", "bfdNotificationsEnable"), ("BFD-STD-MIB", "bfdSessVersionNumber"), ("BFD-STD-MIB", "bfdSessType"), ("BFD-STD-MIB", "bfdSessIndexNext"), ("BFD-STD-MIB", "bfdSessDiscriminator"), ("BFD-STD-MIB", "bfdSessDestinationUdpPort"), ("BFD-STD-MIB", "bfdSessSourceUdpPort"), ("BFD-STD-MIB", "bfdSessEchoSourceUdpPort"), ("BFD-STD-MIB", "bfdSessAdminStatus"), ("BFD-STD-MIB", "bfdSessOperStatus"), ("BFD-STD-MIB", "bfdSessOperMode"), ("BFD-STD-MIB", "bfdSessDemandModeDesiredFlag"), ("BFD-STD-MIB", "bfdSessControlPlaneIndepFlag"), ("BFD-STD-MIB", "bfdSessMultipointFlag"), ("BFD-STD-MIB", "bfdSessInterface"), ("BFD-STD-MIB", "bfdSessSrcAddrType"), ("BFD-STD-MIB", "bfdSessSrcAddr"), ("BFD-STD-MIB", "bfdSessDstAddrType"), ("BFD-STD-MIB", "bfdSessDstAddr"), ("BFD-STD-MIB", "bfdSessGTSM"), ("BFD-STD-MIB", "bfdSessGTSMTTL"), ("BFD-STD-MIB", "bfdSessDesiredMinTxInterval"), ("BFD-STD-MIB", "bfdSessReqMinRxInterval"), ("BFD-STD-MIB", "bfdSessReqMinEchoRxInterval"), ("BFD-STD-MIB", "bfdSessDetectMult"), ("BFD-STD-MIB", "bfdSessAuthPresFlag"), ("BFD-STD-MIB", "bfdSessAuthenticationType"), ("BFD-STD-MIB", "bfdSessAuthenticationKeyID"), ("BFD-STD-MIB", "bfdSessAuthenticationKey"), ("BFD-STD-MIB", "bfdSessStorageType"), ("BFD-STD-MIB", "bfdSessRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdSessionGroup = bfdSessionGroup.setStatus('current')
bfdSessionReadOnlyGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 222, 2, 1, 2)).setObjects(("BFD-STD-MIB", "bfdSessRemoteDiscr"), ("BFD-STD-MIB", "bfdSessState"), ("BFD-STD-MIB", "bfdSessRemoteHeardFlag"), ("BFD-STD-MIB", "bfdSessDiag"), ("BFD-STD-MIB", "bfdSessNegotiatedInterval"), ("BFD-STD-MIB", "bfdSessNegotiatedEchoInterval"), ("BFD-STD-MIB", "bfdSessNegotiatedDetectMult"), ("BFD-STD-MIB", "bfdSessDiscMapIndex"), ("BFD-STD-MIB", "bfdSessIpMapIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdSessionReadOnlyGroup = bfdSessionReadOnlyGroup.setStatus('current')
bfdSessionPerfGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 222, 2, 1, 3)).setObjects(("BFD-STD-MIB", "bfdSessPerfCtrlPktIn"), ("BFD-STD-MIB", "bfdSessPerfCtrlPktOut"), ("BFD-STD-MIB", "bfdSessPerfCtrlPktDrop"), ("BFD-STD-MIB", "bfdSessPerfCtrlPktDropLastTime"), ("BFD-STD-MIB", "bfdSessPerfEchoPktIn"), ("BFD-STD-MIB", "bfdSessPerfEchoPktOut"), ("BFD-STD-MIB", "bfdSessPerfEchoPktDrop"), ("BFD-STD-MIB", "bfdSessPerfEchoPktDropLastTime"), ("BFD-STD-MIB", "bfdSessUpTime"), ("BFD-STD-MIB", "bfdSessPerfLastSessDownTime"), ("BFD-STD-MIB", "bfdSessPerfLastCommLostDiag"), ("BFD-STD-MIB", "bfdSessPerfSessUpCount"), ("BFD-STD-MIB", "bfdSessPerfDiscTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdSessionPerfGroup = bfdSessionPerfGroup.setStatus('current')
bfdSessionPerfHCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 222, 2, 1, 4)).setObjects(("BFD-STD-MIB", "bfdSessPerfCtrlPktInHC"), ("BFD-STD-MIB", "bfdSessPerfCtrlPktOutHC"), ("BFD-STD-MIB", "bfdSessPerfCtrlPktDropHC"), ("BFD-STD-MIB", "bfdSessPerfEchoPktInHC"), ("BFD-STD-MIB", "bfdSessPerfEchoPktOutHC"), ("BFD-STD-MIB", "bfdSessPerfEchoPktDropHC"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdSessionPerfHCGroup = bfdSessionPerfHCGroup.setStatus('current')
bfdNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 222, 2, 1, 5)).setObjects(("BFD-STD-MIB", "bfdSessUp"), ("BFD-STD-MIB", "bfdSessDown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bfdNotificationGroup = bfdNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("BFD-STD-MIB", bfdSessPerfEchoPktDropLastTime=bfdSessPerfEchoPktDropLastTime, bfdSessionGroup=bfdSessionGroup, bfdSessNegotiatedInterval=bfdSessNegotiatedInterval, bfdSessPerfEchoPktDrop=bfdSessPerfEchoPktDrop, bfdSessPerfEchoPktInHC=bfdSessPerfEchoPktInHC, bfdSessPerfCtrlPktDrop=bfdSessPerfCtrlPktDrop, bfdSessIpMapEntry=bfdSessIpMapEntry, bfdSessPerfEchoPktOut=bfdSessPerfEchoPktOut, bfdSessEchoSourceUdpPort=bfdSessEchoSourceUdpPort, bfdSessionPerfGroup=bfdSessionPerfGroup, bfdSessDiscMapEntry=bfdSessDiscMapEntry, bfdSessDstAddr=bfdSessDstAddr, bfdGroups=bfdGroups, bfdSessVersionNumber=bfdSessVersionNumber, bfdSessDown=bfdSessDown, bfdSessSrcAddr=bfdSessSrcAddr, bfdSessPerfEntry=bfdSessPerfEntry, bfdSessOperStatus=bfdSessOperStatus, bfdSessDiscMapIndex=bfdSessDiscMapIndex, bfdSessEntry=bfdSessEntry, bfdSessDiag=bfdSessDiag, bfdSessIpMapTable=bfdSessIpMapTable, bfdSessAuthenticationKey=bfdSessAuthenticationKey, bfdConformance=bfdConformance, bfdSessPerfCtrlPktInHC=bfdSessPerfCtrlPktInHC, bfdSessAdminStatus=bfdSessAdminStatus, bfdSessAuthPresFlag=bfdSessAuthPresFlag, bfdMIB=bfdMIB, bfdSessPerfEchoPktIn=bfdSessPerfEchoPktIn, bfdScalarObjects=bfdScalarObjects, bfdModuleReadOnlyCompliance=bfdModuleReadOnlyCompliance, bfdSessNegotiatedEchoInterval=bfdSessNegotiatedEchoInterval, bfdSessPerfTable=bfdSessPerfTable, bfdCompliances=bfdCompliances, bfdSessPerfCtrlPktOut=bfdSessPerfCtrlPktOut, bfdSessDiscriminator=bfdSessDiscriminator, bfdSessUpTime=bfdSessUpTime, bfdSessPerfLastCommLostDiag=bfdSessPerfLastCommLostDiag, bfdSessIndexNext=bfdSessIndexNext, bfdNotificationGroup=bfdNotificationGroup, bfdSessReqMinEchoRxInterval=bfdSessReqMinEchoRxInterval, bfdSessDetectMult=bfdSessDetectMult, bfdSessTable=bfdSessTable, bfdSessNegotiatedDetectMult=bfdSessNegotiatedDetectMult, bfdNotifications=bfdNotifications, bfdSessMultipointFlag=bfdSessMultipointFlag, bfdSessPerfCtrlPktOutHC=bfdSessPerfCtrlPktOutHC, bfdModuleFullCompliance=bfdModuleFullCompliance, bfdSessType=bfdSessType, bfdSessOperMode=bfdSessOperMode, bfdSessAuthenticationType=bfdSessAuthenticationType, bfdSessRemoteDiscr=bfdSessRemoteDiscr, bfdSessionReadOnlyGroup=bfdSessionReadOnlyGroup, bfdSessSourceUdpPort=bfdSessSourceUdpPort, bfdSessDesiredMinTxInterval=bfdSessDesiredMinTxInterval, bfdSessRowStatus=bfdSessRowStatus, bfdSessPerfSessUpCount=bfdSessPerfSessUpCount, bfdSessIpMapIndex=bfdSessIpMapIndex, bfdSessPerfEchoPktOutHC=bfdSessPerfEchoPktOutHC, bfdOperStatus=bfdOperStatus, bfdSessPerfEchoPktDropHC=bfdSessPerfEchoPktDropHC, bfdSessAuthenticationKeyID=bfdSessAuthenticationKeyID, bfdSessDemandModeDesiredFlag=bfdSessDemandModeDesiredFlag, bfdAdminStatus=bfdAdminStatus, bfdSessionPerfHCGroup=bfdSessionPerfHCGroup, bfdSessReqMinRxInterval=bfdSessReqMinRxInterval, bfdSessDstAddrType=bfdSessDstAddrType, bfdSessPerfCtrlPktDropHC=bfdSessPerfCtrlPktDropHC, bfdSessState=bfdSessState, bfdSessIndex=bfdSessIndex, bfdSessDiscMapTable=bfdSessDiscMapTable, bfdSessGTSM=bfdSessGTSM, bfdSessPerfLastSessDownTime=bfdSessPerfLastSessDownTime, bfdSessUp=bfdSessUp, bfdObjects=bfdObjects, bfdSessStorageType=bfdSessStorageType, bfdSessControlPlaneIndepFlag=bfdSessControlPlaneIndepFlag, bfdSessDestinationUdpPort=bfdSessDestinationUdpPort, bfdSessGTSMTTL=bfdSessGTSMTTL, PYSNMP_MODULE_ID=bfdMIB, bfdSessPerfCtrlPktIn=bfdSessPerfCtrlPktIn, bfdSessRemoteHeardFlag=bfdSessRemoteHeardFlag, bfdSessPerfDiscTime=bfdSessPerfDiscTime, bfdSessPerfCtrlPktDropLastTime=bfdSessPerfCtrlPktDropLastTime, bfdNotificationsEnable=bfdNotificationsEnable, bfdSessSrcAddrType=bfdSessSrcAddrType, bfdSessInterface=bfdSessInterface)
