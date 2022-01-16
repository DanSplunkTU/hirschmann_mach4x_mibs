#
# PySNMP MIB module BGP4-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/BGP4-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:36 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Counter32, Unsigned32, MibIdentifier, iso, ObjectIdentity, Bits, Gauge32, Integer32, IpAddress, ModuleIdentity, mib_2, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Counter32", "Unsigned32", "MibIdentifier", "iso", "ObjectIdentity", "Bits", "Gauge32", "Integer32", "IpAddress", "ModuleIdentity", "mib-2", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bgp = ModuleIdentity((1, 3, 6, 1, 2, 1, 15))
bgp.setRevisions(('2006-01-11 00:00', '1994-05-05 00:00', '1991-10-26 18:39',))
if mibBuilder.loadTexts: bgp.setLastUpdated('200601110000Z')
if mibBuilder.loadTexts: bgp.setOrganization('IETF IDR Working Group')
bgpVersion = MibScalar((1, 3, 6, 1, 2, 1, 15, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpVersion.setStatus('current')
bgpLocalAs = MibScalar((1, 3, 6, 1, 2, 1, 15, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpLocalAs.setStatus('current')
bgpPeerTable = MibTable((1, 3, 6, 1, 2, 1, 15, 3), )
if mibBuilder.loadTexts: bgpPeerTable.setStatus('current')
bgpPeerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 3, 1), ).setIndexNames((0, "BGP4-MIB", "bgpPeerRemoteAddr"))
if mibBuilder.loadTexts: bgpPeerEntry.setStatus('current')
bgpPeerIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerIdentifier.setStatus('current')
bgpPeerState = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("connect", 2), ("active", 3), ("opensent", 4), ("openconfirm", 5), ("established", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerState.setStatus('current')
bgpPeerAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("stop", 1), ("start", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bgpPeerAdminStatus.setStatus('current')
bgpPeerNegotiatedVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerNegotiatedVersion.setStatus('current')
bgpPeerLocalAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLocalAddr.setStatus('current')
bgpPeerLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLocalPort.setStatus('current')
bgpPeerRemoteAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemoteAddr.setStatus('current')
bgpPeerRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemotePort.setStatus('current')
bgpPeerRemoteAs = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerRemoteAs.setStatus('current')
bgpPeerInUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInUpdates.setStatus('current')
bgpPeerOutUpdates = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerOutUpdates.setStatus('current')
bgpPeerInTotalMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInTotalMessages.setStatus('current')
bgpPeerOutTotalMessages = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerOutTotalMessages.setStatus('current')
bgpPeerLastError = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerLastError.setStatus('current')
bgpPeerFsmEstablishedTransitions = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerFsmEstablishedTransitions.setStatus('current')
bgpPeerFsmEstablishedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 16), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerFsmEstablishedTime.setStatus('current')
bgpPeerConnectRetryInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 17), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bgpPeerConnectRetryInterval.setStatus('current')
bgpPeerHoldTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerHoldTime.setStatus('current')
bgpPeerKeepAlive = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), ))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerKeepAlive.setStatus('current')
bgpPeerHoldTimeConfigured = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bgpPeerHoldTimeConfigured.setStatus('current')
bgpPeerKeepAliveConfigured = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 21), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bgpPeerKeepAliveConfigured.setStatus('current')
bgpPeerMinASOriginationInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bgpPeerMinASOriginationInterval.setStatus('current')
bgpPeerMinRouteAdvertisementInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 23), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: bgpPeerMinRouteAdvertisementInterval.setStatus('current')
bgpPeerInUpdateElapsedTime = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 3, 1, 24), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPeerInUpdateElapsedTime.setStatus('current')
bgpIdentifier = MibScalar((1, 3, 6, 1, 2, 1, 15, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpIdentifier.setStatus('current')
bgpRcvdPathAttrTable = MibTable((1, 3, 6, 1, 2, 1, 15, 5), )
if mibBuilder.loadTexts: bgpRcvdPathAttrTable.setStatus('obsolete')
bgpPathAttrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 5, 1), ).setIndexNames((0, "BGP4-MIB", "bgpPathAttrDestNetwork"), (0, "BGP4-MIB", "bgpPathAttrPeer"))
if mibBuilder.loadTexts: bgpPathAttrEntry.setStatus('obsolete')
bgpPathAttrPeer = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrPeer.setStatus('obsolete')
bgpPathAttrDestNetwork = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrDestNetwork.setStatus('obsolete')
bgpPathAttrOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("igp", 1), ("egp", 2), ("incomplete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrOrigin.setStatus('obsolete')
bgpPathAttrASPath = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrASPath.setStatus('obsolete')
bgpPathAttrNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrNextHop.setStatus('obsolete')
bgpPathAttrInterASMetric = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgpPathAttrInterASMetric.setStatus('obsolete')
bgp4PathAttrTable = MibTable((1, 3, 6, 1, 2, 1, 15, 6), )
if mibBuilder.loadTexts: bgp4PathAttrTable.setStatus('current')
bgp4PathAttrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 15, 6, 1), ).setIndexNames((0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefix"), (0, "BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"), (0, "BGP4-MIB", "bgp4PathAttrPeer"))
if mibBuilder.loadTexts: bgp4PathAttrEntry.setStatus('current')
bgp4PathAttrPeer = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrPeer.setStatus('current')
bgp4PathAttrIpAddrPrefixLen = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrIpAddrPrefixLen.setStatus('current')
bgp4PathAttrIpAddrPrefix = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrIpAddrPrefix.setStatus('current')
bgp4PathAttrOrigin = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("igp", 1), ("egp", 2), ("incomplete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrOrigin.setStatus('current')
bgp4PathAttrASPathSegment = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrASPathSegment.setStatus('current')
bgp4PathAttrNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrNextHop.setStatus('current')
bgp4PathAttrMultiExitDisc = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrMultiExitDisc.setStatus('current')
bgp4PathAttrLocalPref = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrLocalPref.setStatus('current')
bgp4PathAttrAtomicAggregate = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("lessSpecificRouteNotSelected", 1), ("lessSpecificRouteSelected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrAtomicAggregate.setStatus('current')
bgp4PathAttrAggregatorAS = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrAggregatorAS.setStatus('current')
bgp4PathAttrAggregatorAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 11), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrAggregatorAddr.setStatus('current')
bgp4PathAttrCalcLocalPref = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrCalcLocalPref.setStatus('current')
bgp4PathAttrBest = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrBest.setStatus('current')
bgp4PathAttrUnknown = MibTableColumn((1, 3, 6, 1, 2, 1, 15, 6, 1, 14), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bgp4PathAttrUnknown.setStatus('current')
bgpNotification = MibIdentifier((1, 3, 6, 1, 2, 1, 15, 0))
bgpEstablishedNotification = NotificationType((1, 3, 6, 1, 2, 1, 15, 0, 1)).setObjects(("BGP4-MIB", "bgpPeerRemoteAddr"), ("BGP4-MIB", "bgpPeerLastError"), ("BGP4-MIB", "bgpPeerState"))
if mibBuilder.loadTexts: bgpEstablishedNotification.setStatus('current')
bgpBackwardTransNotification = NotificationType((1, 3, 6, 1, 2, 1, 15, 0, 2)).setObjects(("BGP4-MIB", "bgpPeerRemoteAddr"), ("BGP4-MIB", "bgpPeerLastError"), ("BGP4-MIB", "bgpPeerState"))
if mibBuilder.loadTexts: bgpBackwardTransNotification.setStatus('current')
bgpTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 15, 7))
bgpEstablished = NotificationType((1, 3, 6, 1, 2, 1, 15, 7, 1)).setObjects(("BGP4-MIB", "bgpPeerLastError"), ("BGP4-MIB", "bgpPeerState"))
if mibBuilder.loadTexts: bgpEstablished.setStatus('deprecated')
bgpBackwardTransition = NotificationType((1, 3, 6, 1, 2, 1, 15, 7, 2)).setObjects(("BGP4-MIB", "bgpPeerLastError"), ("BGP4-MIB", "bgpPeerState"))
if mibBuilder.loadTexts: bgpBackwardTransition.setStatus('deprecated')
bgp4MIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 15, 8))
bgp4MIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 15, 8, 1))
bgp4MIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 15, 8, 2))
bgp4MIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 15, 8, 1, 1)).setObjects(("BGP4-MIB", "bgp4MIBGlobalsGroup"), ("BGP4-MIB", "bgp4MIBPeerGroup"), ("BGP4-MIB", "bgp4MIBPathAttrGroup"), ("BGP4-MIB", "bgp4MIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgp4MIBCompliance = bgp4MIBCompliance.setStatus('current')
bgp4MIBDeprecatedCompliances = ModuleCompliance((1, 3, 6, 1, 2, 1, 15, 8, 1, 2)).setObjects(("BGP4-MIB", "bgp4MIBTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgp4MIBDeprecatedCompliances = bgp4MIBDeprecatedCompliances.setStatus('deprecated')
bgp4MIBObsoleteCompliances = ModuleCompliance((1, 3, 6, 1, 2, 1, 15, 8, 1, 3)).setObjects(("BGP4-MIB", "bgpRcvdPathAttrGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgp4MIBObsoleteCompliances = bgp4MIBObsoleteCompliances.setStatus('obsolete')
bgp4MIBGlobalsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 15, 8, 2, 1)).setObjects(("BGP4-MIB", "bgpVersion"), ("BGP4-MIB", "bgpLocalAs"), ("BGP4-MIB", "bgpIdentifier"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgp4MIBGlobalsGroup = bgp4MIBGlobalsGroup.setStatus('current')
bgp4MIBPeerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 15, 8, 2, 2)).setObjects(("BGP4-MIB", "bgpPeerIdentifier"), ("BGP4-MIB", "bgpPeerState"), ("BGP4-MIB", "bgpPeerAdminStatus"), ("BGP4-MIB", "bgpPeerNegotiatedVersion"), ("BGP4-MIB", "bgpPeerLocalAddr"), ("BGP4-MIB", "bgpPeerLocalPort"), ("BGP4-MIB", "bgpPeerRemoteAddr"), ("BGP4-MIB", "bgpPeerRemotePort"), ("BGP4-MIB", "bgpPeerRemoteAs"), ("BGP4-MIB", "bgpPeerInUpdates"), ("BGP4-MIB", "bgpPeerOutUpdates"), ("BGP4-MIB", "bgpPeerInTotalMessages"), ("BGP4-MIB", "bgpPeerOutTotalMessages"), ("BGP4-MIB", "bgpPeerLastError"), ("BGP4-MIB", "bgpPeerFsmEstablishedTransitions"), ("BGP4-MIB", "bgpPeerFsmEstablishedTime"), ("BGP4-MIB", "bgpPeerConnectRetryInterval"), ("BGP4-MIB", "bgpPeerHoldTime"), ("BGP4-MIB", "bgpPeerKeepAlive"), ("BGP4-MIB", "bgpPeerHoldTimeConfigured"), ("BGP4-MIB", "bgpPeerKeepAliveConfigured"), ("BGP4-MIB", "bgpPeerMinASOriginationInterval"), ("BGP4-MIB", "bgpPeerMinRouteAdvertisementInterval"), ("BGP4-MIB", "bgpPeerInUpdateElapsedTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgp4MIBPeerGroup = bgp4MIBPeerGroup.setStatus('current')
bgpRcvdPathAttrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 15, 8, 2, 3)).setObjects(("BGP4-MIB", "bgpPathAttrPeer"), ("BGP4-MIB", "bgpPathAttrDestNetwork"), ("BGP4-MIB", "bgpPathAttrOrigin"), ("BGP4-MIB", "bgpPathAttrASPath"), ("BGP4-MIB", "bgpPathAttrNextHop"), ("BGP4-MIB", "bgpPathAttrInterASMetric"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgpRcvdPathAttrGroup = bgpRcvdPathAttrGroup.setStatus('obsolete')
bgp4MIBPathAttrGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 15, 8, 2, 4)).setObjects(("BGP4-MIB", "bgp4PathAttrPeer"), ("BGP4-MIB", "bgp4PathAttrIpAddrPrefixLen"), ("BGP4-MIB", "bgp4PathAttrIpAddrPrefix"), ("BGP4-MIB", "bgp4PathAttrOrigin"), ("BGP4-MIB", "bgp4PathAttrASPathSegment"), ("BGP4-MIB", "bgp4PathAttrNextHop"), ("BGP4-MIB", "bgp4PathAttrMultiExitDisc"), ("BGP4-MIB", "bgp4PathAttrLocalPref"), ("BGP4-MIB", "bgp4PathAttrAtomicAggregate"), ("BGP4-MIB", "bgp4PathAttrAggregatorAS"), ("BGP4-MIB", "bgp4PathAttrAggregatorAddr"), ("BGP4-MIB", "bgp4PathAttrCalcLocalPref"), ("BGP4-MIB", "bgp4PathAttrBest"), ("BGP4-MIB", "bgp4PathAttrUnknown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgp4MIBPathAttrGroup = bgp4MIBPathAttrGroup.setStatus('current')
bgp4MIBTrapGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 15, 8, 2, 5)).setObjects(("BGP4-MIB", "bgpEstablished"), ("BGP4-MIB", "bgpBackwardTransition"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgp4MIBTrapGroup = bgp4MIBTrapGroup.setStatus('deprecated')
bgp4MIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 15, 8, 2, 6)).setObjects(("BGP4-MIB", "bgpEstablishedNotification"), ("BGP4-MIB", "bgpBackwardTransNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bgp4MIBNotificationGroup = bgp4MIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("BGP4-MIB", bgp4PathAttrPeer=bgp4PathAttrPeer, bgpEstablishedNotification=bgpEstablishedNotification, bgp4PathAttrUnknown=bgp4PathAttrUnknown, bgpPathAttrNextHop=bgpPathAttrNextHop, bgpPeerLocalAddr=bgpPeerLocalAddr, bgp4MIBTrapGroup=bgp4MIBTrapGroup, bgpEstablished=bgpEstablished, bgpLocalAs=bgpLocalAs, bgp4MIBNotificationGroup=bgp4MIBNotificationGroup, bgp=bgp, bgp4PathAttrNextHop=bgp4PathAttrNextHop, bgpIdentifier=bgpIdentifier, bgp4PathAttrASPathSegment=bgp4PathAttrASPathSegment, bgpPeerState=bgpPeerState, bgp4PathAttrEntry=bgp4PathAttrEntry, bgpNotification=bgpNotification, bgpPeerTable=bgpPeerTable, bgpPeerKeepAliveConfigured=bgpPeerKeepAliveConfigured, bgpPeerMinASOriginationInterval=bgpPeerMinASOriginationInterval, bgp4MIBCompliances=bgp4MIBCompliances, bgp4MIBConformance=bgp4MIBConformance, bgp4PathAttrLocalPref=bgp4PathAttrLocalPref, bgpPeerHoldTime=bgpPeerHoldTime, bgp4MIBPeerGroup=bgp4MIBPeerGroup, bgpPathAttrASPath=bgpPathAttrASPath, bgp4PathAttrAggregatorAddr=bgp4PathAttrAggregatorAddr, bgpPeerEntry=bgpPeerEntry, bgpPeerLocalPort=bgpPeerLocalPort, bgpPeerRemoteAddr=bgpPeerRemoteAddr, bgpRcvdPathAttrTable=bgpRcvdPathAttrTable, bgpBackwardTransNotification=bgpBackwardTransNotification, bgp4MIBCompliance=bgp4MIBCompliance, bgp4MIBDeprecatedCompliances=bgp4MIBDeprecatedCompliances, bgp4MIBGlobalsGroup=bgp4MIBGlobalsGroup, bgpPeerOutUpdates=bgpPeerOutUpdates, bgp4PathAttrAggregatorAS=bgp4PathAttrAggregatorAS, bgpPathAttrDestNetwork=bgpPathAttrDestNetwork, bgp4MIBGroups=bgp4MIBGroups, bgpRcvdPathAttrGroup=bgpRcvdPathAttrGroup, bgpPeerIdentifier=bgpPeerIdentifier, bgpPeerConnectRetryInterval=bgpPeerConnectRetryInterval, bgpPeerInTotalMessages=bgpPeerInTotalMessages, bgpPathAttrEntry=bgpPathAttrEntry, bgp4PathAttrTable=bgp4PathAttrTable, bgp4MIBPathAttrGroup=bgp4MIBPathAttrGroup, bgpPeerRemoteAs=bgpPeerRemoteAs, bgpTraps=bgpTraps, bgpPathAttrInterASMetric=bgpPathAttrInterASMetric, bgpPeerRemotePort=bgpPeerRemotePort, bgpBackwardTransition=bgpBackwardTransition, bgpPeerInUpdateElapsedTime=bgpPeerInUpdateElapsedTime, bgp4PathAttrOrigin=bgp4PathAttrOrigin, bgpPeerKeepAlive=bgpPeerKeepAlive, bgp4PathAttrAtomicAggregate=bgp4PathAttrAtomicAggregate, bgpPeerFsmEstablishedTime=bgpPeerFsmEstablishedTime, bgpPathAttrOrigin=bgpPathAttrOrigin, bgpPeerInUpdates=bgpPeerInUpdates, bgpPeerAdminStatus=bgpPeerAdminStatus, bgpPeerFsmEstablishedTransitions=bgpPeerFsmEstablishedTransitions, bgp4PathAttrIpAddrPrefix=bgp4PathAttrIpAddrPrefix, bgp4PathAttrBest=bgp4PathAttrBest, bgpPeerNegotiatedVersion=bgpPeerNegotiatedVersion, bgp4PathAttrCalcLocalPref=bgp4PathAttrCalcLocalPref, bgpPeerLastError=bgpPeerLastError, bgp4PathAttrIpAddrPrefixLen=bgp4PathAttrIpAddrPrefixLen, bgp4MIBObsoleteCompliances=bgp4MIBObsoleteCompliances, bgpPeerOutTotalMessages=bgpPeerOutTotalMessages, bgpPeerHoldTimeConfigured=bgpPeerHoldTimeConfigured, bgpVersion=bgpVersion, bgpPathAttrPeer=bgpPathAttrPeer, bgpPeerMinRouteAdvertisementInterval=bgpPeerMinRouteAdvertisementInterval, bgp4PathAttrMultiExitDisc=bgp4PathAttrMultiExitDisc, PYSNMP_MODULE_ID=bgp)
