#
# PySNMP MIB module PPP-LCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/PPP-LCP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, transmission, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ppp = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23))
pppLcp = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1))
pppLink = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 1))
pppLqr = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 2))
pppTests = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3))
pppLinkStatusTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1), )
if mibBuilder.loadTexts: pppLinkStatusTable.setStatus('mandatory')
pppLinkStatusEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppLinkStatusEntry.setStatus('mandatory')
pppLinkStatusPhysicalIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusPhysicalIndex.setStatus('mandatory')
pppLinkStatusBadAddresses = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusBadAddresses.setStatus('mandatory')
pppLinkStatusBadControls = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusBadControls.setStatus('mandatory')
pppLinkStatusPacketTooLongs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusPacketTooLongs.setStatus('mandatory')
pppLinkStatusBadFCSs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusBadFCSs.setStatus('mandatory')
pppLinkStatusLocalMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusLocalMRU.setStatus('mandatory')
pppLinkStatusRemoteMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusRemoteMRU.setStatus('mandatory')
pppLinkStatusLocalToPeerACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusLocalToPeerACCMap.setStatus('mandatory')
pppLinkStatusPeerToLocalACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusPeerToLocalACCMap.setStatus('mandatory')
pppLinkStatusLocalToRemoteProtocolCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusLocalToRemoteProtocolCompression.setStatus('mandatory')
pppLinkStatusRemoteToLocalProtocolCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusRemoteToLocalProtocolCompression.setStatus('mandatory')
pppLinkStatusLocalToRemoteACCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusLocalToRemoteACCompression.setStatus('mandatory')
pppLinkStatusRemoteToLocalACCompression = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusRemoteToLocalACCompression.setStatus('mandatory')
pppLinkStatusTransmitFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusTransmitFcsSize.setStatus('mandatory')
pppLinkStatusReceiveFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLinkStatusReceiveFcsSize.setStatus('mandatory')
pppLinkConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2), )
if mibBuilder.loadTexts: pppLinkConfigTable.setStatus('mandatory')
pppLinkConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppLinkConfigEntry.setStatus('mandatory')
pppLinkConfigInitialMRU = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)).clone(1500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLinkConfigInitialMRU.setStatus('mandatory')
pppLinkConfigReceiveACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4).clone(hexValue="ffffffff")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLinkConfigReceiveACCMap.setStatus('mandatory')
pppLinkConfigTransmitACCMap = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(4, 4)).setFixedLength(4).clone(hexValue="ffffffff")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLinkConfigTransmitACCMap.setStatus('mandatory')
pppLinkConfigMagicNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2))).clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLinkConfigMagicNumber.setStatus('mandatory')
pppLinkConfigFcsSize = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128)).clone(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLinkConfigFcsSize.setStatus('mandatory')
pppLqrTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1), )
if mibBuilder.loadTexts: pppLqrTable.setStatus('mandatory')
pppLqrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppLqrEntry.setStatus('mandatory')
pppLqrQuality = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("good", 1), ("bad", 2), ("not-determined", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrQuality.setStatus('mandatory')
pppLqrInGoodOctets = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrInGoodOctets.setStatus('mandatory')
pppLqrLocalPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrLocalPeriod.setStatus('mandatory')
pppLqrRemotePeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrRemotePeriod.setStatus('mandatory')
pppLqrOutLQRs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrOutLQRs.setStatus('mandatory')
pppLqrInLQRs = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrInLQRs.setStatus('mandatory')
pppLqrConfigTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2), )
if mibBuilder.loadTexts: pppLqrConfigTable.setStatus('mandatory')
pppLqrConfigEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppLqrConfigEntry.setStatus('mandatory')
pppLqrConfigPeriod = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLqrConfigPeriod.setStatus('mandatory')
pppLqrConfigStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pppLqrConfigStatus.setStatus('mandatory')
pppLqrExtnsTable = MibTable((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3), )
if mibBuilder.loadTexts: pppLqrExtnsTable.setStatus('mandatory')
pppLqrExtnsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pppLqrExtnsEntry.setStatus('mandatory')
pppLqrExtnsLastReceivedLqrPacket = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 23, 1, 2, 3, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(68, 68)).setFixedLength(68)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pppLqrExtnsLastReceivedLqrPacket.setStatus('mandatory')
pppEchoTest = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3, 1))
pppDiscardTest = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 23, 1, 3, 2))
mibBuilder.exportSymbols("PPP-LCP-MIB", pppLqrRemotePeriod=pppLqrRemotePeriod, pppLqrInGoodOctets=pppLqrInGoodOctets, pppLinkStatusLocalMRU=pppLinkStatusLocalMRU, pppLinkStatusReceiveFcsSize=pppLinkStatusReceiveFcsSize, pppLinkStatusRemoteToLocalACCompression=pppLinkStatusRemoteToLocalACCompression, pppLinkStatusEntry=pppLinkStatusEntry, pppLqrConfigStatus=pppLqrConfigStatus, pppLinkStatusBadAddresses=pppLinkStatusBadAddresses, pppLinkConfigReceiveACCMap=pppLinkConfigReceiveACCMap, pppLqr=pppLqr, pppLinkStatusBadControls=pppLinkStatusBadControls, pppLcp=pppLcp, pppDiscardTest=pppDiscardTest, pppLinkConfigTable=pppLinkConfigTable, pppLinkConfigFcsSize=pppLinkConfigFcsSize, pppLqrTable=pppLqrTable, ppp=ppp, pppLinkStatusLocalToPeerACCMap=pppLinkStatusLocalToPeerACCMap, pppLinkStatusRemoteMRU=pppLinkStatusRemoteMRU, pppLinkConfigEntry=pppLinkConfigEntry, pppLqrExtnsLastReceivedLqrPacket=pppLqrExtnsLastReceivedLqrPacket, pppLqrExtnsTable=pppLqrExtnsTable, pppLinkConfigTransmitACCMap=pppLinkConfigTransmitACCMap, pppLinkStatusBadFCSs=pppLinkStatusBadFCSs, pppLinkStatusPhysicalIndex=pppLinkStatusPhysicalIndex, pppLqrOutLQRs=pppLqrOutLQRs, pppLqrExtnsEntry=pppLqrExtnsEntry, pppTests=pppTests, pppLinkStatusTransmitFcsSize=pppLinkStatusTransmitFcsSize, pppLink=pppLink, pppLqrLocalPeriod=pppLqrLocalPeriod, pppLqrConfigPeriod=pppLqrConfigPeriod, pppLinkStatusPeerToLocalACCMap=pppLinkStatusPeerToLocalACCMap, pppLinkStatusLocalToRemoteProtocolCompression=pppLinkStatusLocalToRemoteProtocolCompression, pppLinkConfigInitialMRU=pppLinkConfigInitialMRU, pppLqrEntry=pppLqrEntry, pppLinkStatusRemoteToLocalProtocolCompression=pppLinkStatusRemoteToLocalProtocolCompression, pppLinkStatusLocalToRemoteACCompression=pppLinkStatusLocalToRemoteACCompression, pppEchoTest=pppEchoTest, pppLqrInLQRs=pppLqrInLQRs, pppLinkStatusTable=pppLinkStatusTable, pppLqrConfigTable=pppLqrConfigTable, pppLqrConfigEntry=pppLqrConfigEntry, pppLqrQuality=pppLqrQuality, pppLinkConfigMagicNumber=pppLinkConfigMagicNumber, pppLinkStatusPacketTooLongs=pppLinkStatusPacketTooLongs)
