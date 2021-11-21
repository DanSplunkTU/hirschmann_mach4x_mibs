#
# PySNMP MIB module IPV6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:25:42 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
Ipv6IfIndexOrZero, Ipv6AddressPrefix, Ipv6IfIndex, Ipv6Address, Ipv6AddressIfIdentifier = mibBuilder.importSymbols("IPV6-TC", "Ipv6IfIndexOrZero", "Ipv6AddressPrefix", "Ipv6IfIndex", "Ipv6Address", "Ipv6AddressIfIdentifier")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
mib_2, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Gauge32, Bits, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, NotificationType, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Gauge32", "Bits", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "Integer32", "Counter64")
DisplayString, TimeStamp, RowPointer, PhysAddress, TextualConvention, VariablePointer, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TimeStamp", "RowPointer", "PhysAddress", "TextualConvention", "VariablePointer", "TruthValue")
ipv6MIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 55))
ipv6MIB.setRevisions(('2017-02-22 00:00', '1998-02-05 21:55',))
if mibBuilder.loadTexts: ipv6MIB.setLastUpdated('201702220000Z')
if mibBuilder.loadTexts: ipv6MIB.setOrganization('IETF IPv6 Working Group')
ipv6MIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 1))
ipv6Forwarding = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("forwarding", 1), ("notForwarding", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6Forwarding.setStatus('obsolete')
ipv6DefaultHopLimit = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6DefaultHopLimit.setStatus('obsolete')
ipv6Interfaces = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6Interfaces.setStatus('obsolete')
ipv6IfTableLastChange = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfTableLastChange.setStatus('obsolete')
ipv6IfTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 5), )
if mibBuilder.loadTexts: ipv6IfTable.setStatus('obsolete')
ipv6IfEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 5, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"))
if mibBuilder.loadTexts: ipv6IfEntry.setStatus('obsolete')
ipv6IfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 1), Ipv6IfIndex())
if mibBuilder.loadTexts: ipv6IfIndex.setStatus('obsolete')
ipv6IfDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6IfDescr.setStatus('obsolete')
ipv6IfLowerLayer = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 3), VariablePointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfLowerLayer.setStatus('obsolete')
ipv6IfEffectiveMtu = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 4), Unsigned32()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfEffectiveMtu.setStatus('obsolete')
ipv6IfReasmMaxSize = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfReasmMaxSize.setStatus('obsolete')
ipv6IfIdentifier = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 6), Ipv6AddressIfIdentifier()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6IfIdentifier.setStatus('obsolete')
ipv6IfIdentifierLength = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64))).setUnits('bits').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6IfIdentifierLength.setStatus('obsolete')
ipv6IfPhysicalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 8), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfPhysicalAddress.setStatus('obsolete')
ipv6IfAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6IfAdminStatus.setStatus('obsolete')
ipv6IfOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("noIfIdentifier", 3), ("unknown", 4), ("notPresent", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfOperStatus.setStatus('obsolete')
ipv6IfLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 11), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfLastChange.setStatus('obsolete')
ipv6IfStatsTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 6), )
if mibBuilder.loadTexts: ipv6IfStatsTable.setStatus('obsolete')
ipv6IfStatsEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 6, 1), )
ipv6IfEntry.registerAugmentions(("IPV6-MIB", "ipv6IfStatsEntry"))
ipv6IfStatsEntry.setIndexNames(*ipv6IfEntry.getIndexNames())
if mibBuilder.loadTexts: ipv6IfStatsEntry.setStatus('obsolete')
ipv6IfStatsInReceives = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInReceives.setStatus('obsolete')
ipv6IfStatsInHdrErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInHdrErrors.setStatus('obsolete')
ipv6IfStatsInTooBigErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInTooBigErrors.setStatus('obsolete')
ipv6IfStatsInNoRoutes = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInNoRoutes.setStatus('obsolete')
ipv6IfStatsInAddrErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInAddrErrors.setStatus('obsolete')
ipv6IfStatsInUnknownProtos = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInUnknownProtos.setStatus('obsolete')
ipv6IfStatsInTruncatedPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInTruncatedPkts.setStatus('obsolete')
ipv6IfStatsInDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInDiscards.setStatus('obsolete')
ipv6IfStatsInDelivers = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInDelivers.setStatus('obsolete')
ipv6IfStatsOutForwDatagrams = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutForwDatagrams.setStatus('obsolete')
ipv6IfStatsOutRequests = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutRequests.setStatus('obsolete')
ipv6IfStatsOutDiscards = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutDiscards.setStatus('obsolete')
ipv6IfStatsOutFragOKs = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutFragOKs.setStatus('obsolete')
ipv6IfStatsOutFragFails = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutFragFails.setStatus('obsolete')
ipv6IfStatsOutFragCreates = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutFragCreates.setStatus('obsolete')
ipv6IfStatsReasmReqds = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsReasmReqds.setStatus('obsolete')
ipv6IfStatsReasmOKs = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsReasmOKs.setStatus('obsolete')
ipv6IfStatsReasmFails = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsReasmFails.setStatus('obsolete')
ipv6IfStatsInMcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsInMcastPkts.setStatus('obsolete')
ipv6IfStatsOutMcastPkts = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfStatsOutMcastPkts.setStatus('obsolete')
ipv6AddrPrefixTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 7), )
if mibBuilder.loadTexts: ipv6AddrPrefixTable.setStatus('obsolete')
ipv6AddrPrefixEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 7, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"), (0, "IPV6-MIB", "ipv6AddrPrefix"), (0, "IPV6-MIB", "ipv6AddrPrefixLength"))
if mibBuilder.loadTexts: ipv6AddrPrefixEntry.setStatus('obsolete')
ipv6AddrPrefix = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 1), Ipv6AddressPrefix())
if mibBuilder.loadTexts: ipv6AddrPrefix.setStatus('obsolete')
ipv6AddrPrefixLength = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setUnits('bits')
if mibBuilder.loadTexts: ipv6AddrPrefixLength.setStatus('obsolete')
ipv6AddrPrefixOnLinkFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrPrefixOnLinkFlag.setStatus('obsolete')
ipv6AddrPrefixAutonomousFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrPrefixAutonomousFlag.setStatus('obsolete')
ipv6AddrPrefixAdvPreferredLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 5), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrPrefixAdvPreferredLifetime.setStatus('obsolete')
ipv6AddrPrefixAdvValidLifetime = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 6), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrPrefixAdvValidLifetime.setStatus('obsolete')
ipv6AddrTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 8), )
if mibBuilder.loadTexts: ipv6AddrTable.setStatus('obsolete')
ipv6AddrEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 8, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"), (0, "IPV6-MIB", "ipv6AddrAddress"))
if mibBuilder.loadTexts: ipv6AddrEntry.setStatus('obsolete')
ipv6AddrAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6AddrAddress.setStatus('obsolete')
ipv6AddrPfxLength = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setUnits('bits').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrPfxLength.setStatus('obsolete')
ipv6AddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("stateless", 1), ("stateful", 2), ("unknown", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrType.setStatus('obsolete')
ipv6AddrAnycastFlag = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrAnycastFlag.setStatus('obsolete')
ipv6AddrStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("preferred", 1), ("deprecated", 2), ("invalid", 3), ("inaccessible", 4), ("unknown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6AddrStatus.setStatus('obsolete')
ipv6RouteNumber = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteNumber.setStatus('obsolete')
ipv6DiscardedRoutes = MibScalar((1, 3, 6, 1, 2, 1, 55, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6DiscardedRoutes.setStatus('obsolete')
ipv6RouteTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 11), )
if mibBuilder.loadTexts: ipv6RouteTable.setStatus('obsolete')
ipv6RouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 11, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6RouteDest"), (0, "IPV6-MIB", "ipv6RoutePfxLength"), (0, "IPV6-MIB", "ipv6RouteIndex"))
if mibBuilder.loadTexts: ipv6RouteEntry.setStatus('obsolete')
ipv6RouteDest = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6RouteDest.setStatus('obsolete')
ipv6RoutePfxLength = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setUnits('bits')
if mibBuilder.loadTexts: ipv6RoutePfxLength.setStatus('obsolete')
ipv6RouteIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 3), Unsigned32())
if mibBuilder.loadTexts: ipv6RouteIndex.setStatus('obsolete')
ipv6RouteIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 4), Ipv6IfIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteIfIndex.setStatus('obsolete')
ipv6RouteNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 5), Ipv6Address()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteNextHop.setStatus('obsolete')
ipv6RouteType = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("discard", 2), ("local", 3), ("remote", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteType.setStatus('obsolete')
ipv6RouteProtocol = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("ndisc", 4), ("rip", 5), ("ospf", 6), ("bgp", 7), ("idrp", 8), ("igrp", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteProtocol.setStatus('obsolete')
ipv6RoutePolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RoutePolicy.setStatus('obsolete')
ipv6RouteAge = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 9), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteAge.setStatus('obsolete')
ipv6RouteNextHopRDI = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteNextHopRDI.setStatus('obsolete')
ipv6RouteMetric = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteMetric.setStatus('obsolete')
ipv6RouteWeight = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteWeight.setStatus('obsolete')
ipv6RouteInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 13), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6RouteInfo.setStatus('obsolete')
ipv6RouteValid = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 14), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6RouteValid.setStatus('obsolete')
ipv6NetToMediaTable = MibTable((1, 3, 6, 1, 2, 1, 55, 1, 12), )
if mibBuilder.loadTexts: ipv6NetToMediaTable.setStatus('obsolete')
ipv6NetToMediaEntry = MibTableRow((1, 3, 6, 1, 2, 1, 55, 1, 12, 1), ).setIndexNames((0, "IPV6-MIB", "ipv6IfIndex"), (0, "IPV6-MIB", "ipv6NetToMediaNetAddress"))
if mibBuilder.loadTexts: ipv6NetToMediaEntry.setStatus('obsolete')
ipv6NetToMediaNetAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: ipv6NetToMediaNetAddress.setStatus('obsolete')
ipv6NetToMediaPhysAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6NetToMediaPhysAddress.setStatus('obsolete')
ipv6NetToMediaType = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("dynamic", 2), ("static", 3), ("local", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6NetToMediaType.setStatus('obsolete')
ipv6IfNetToMediaState = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("reachable", 1), ("stale", 2), ("delay", 3), ("probe", 4), ("invalid", 5), ("unknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfNetToMediaState.setStatus('obsolete')
ipv6IfNetToMediaLastUpdated = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 5), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfNetToMediaLastUpdated.setStatus('obsolete')
ipv6NetToMediaValid = MibTableColumn((1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ipv6NetToMediaValid.setStatus('obsolete')
ipv6Notifications = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 2))
ipv6NotificationPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 2, 0))
ipv6IfStateChange = NotificationType((1, 3, 6, 1, 2, 1, 55, 2, 0, 1)).setObjects(("IPV6-MIB", "ipv6IfDescr"), ("IPV6-MIB", "ipv6IfOperStatus"))
if mibBuilder.loadTexts: ipv6IfStateChange.setStatus('obsolete')
ipv6Conformance = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 3))
ipv6Compliances = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 3, 1))
ipv6Groups = MibIdentifier((1, 3, 6, 1, 2, 1, 55, 3, 2))
ipv6Compliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 55, 3, 1, 1)).setObjects(("IPV6-MIB", "ipv6GeneralGroup"), ("IPV6-MIB", "ipv6NotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6Compliance = ipv6Compliance.setStatus('obsolete')
ipv6GeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 55, 3, 2, 1)).setObjects(("IPV6-MIB", "ipv6Forwarding"), ("IPV6-MIB", "ipv6DefaultHopLimit"), ("IPV6-MIB", "ipv6Interfaces"), ("IPV6-MIB", "ipv6IfTableLastChange"), ("IPV6-MIB", "ipv6IfDescr"), ("IPV6-MIB", "ipv6IfLowerLayer"), ("IPV6-MIB", "ipv6IfEffectiveMtu"), ("IPV6-MIB", "ipv6IfReasmMaxSize"), ("IPV6-MIB", "ipv6IfIdentifier"), ("IPV6-MIB", "ipv6IfIdentifierLength"), ("IPV6-MIB", "ipv6IfPhysicalAddress"), ("IPV6-MIB", "ipv6IfAdminStatus"), ("IPV6-MIB", "ipv6IfOperStatus"), ("IPV6-MIB", "ipv6IfLastChange"), ("IPV6-MIB", "ipv6IfStatsInReceives"), ("IPV6-MIB", "ipv6IfStatsInHdrErrors"), ("IPV6-MIB", "ipv6IfStatsInTooBigErrors"), ("IPV6-MIB", "ipv6IfStatsInNoRoutes"), ("IPV6-MIB", "ipv6IfStatsInAddrErrors"), ("IPV6-MIB", "ipv6IfStatsInUnknownProtos"), ("IPV6-MIB", "ipv6IfStatsInTruncatedPkts"), ("IPV6-MIB", "ipv6IfStatsInDiscards"), ("IPV6-MIB", "ipv6IfStatsInDelivers"), ("IPV6-MIB", "ipv6IfStatsOutForwDatagrams"), ("IPV6-MIB", "ipv6IfStatsOutRequests"), ("IPV6-MIB", "ipv6IfStatsOutDiscards"), ("IPV6-MIB", "ipv6IfStatsOutFragOKs"), ("IPV6-MIB", "ipv6IfStatsOutFragFails"), ("IPV6-MIB", "ipv6IfStatsOutFragCreates"), ("IPV6-MIB", "ipv6IfStatsReasmReqds"), ("IPV6-MIB", "ipv6IfStatsReasmOKs"), ("IPV6-MIB", "ipv6IfStatsReasmFails"), ("IPV6-MIB", "ipv6IfStatsInMcastPkts"), ("IPV6-MIB", "ipv6IfStatsOutMcastPkts"), ("IPV6-MIB", "ipv6AddrPrefixOnLinkFlag"), ("IPV6-MIB", "ipv6AddrPrefixAutonomousFlag"), ("IPV6-MIB", "ipv6AddrPrefixAdvPreferredLifetime"), ("IPV6-MIB", "ipv6AddrPrefixAdvValidLifetime"), ("IPV6-MIB", "ipv6AddrPfxLength"), ("IPV6-MIB", "ipv6AddrType"), ("IPV6-MIB", "ipv6AddrAnycastFlag"), ("IPV6-MIB", "ipv6AddrStatus"), ("IPV6-MIB", "ipv6RouteNumber"), ("IPV6-MIB", "ipv6DiscardedRoutes"), ("IPV6-MIB", "ipv6RouteIfIndex"), ("IPV6-MIB", "ipv6RouteNextHop"), ("IPV6-MIB", "ipv6RouteType"), ("IPV6-MIB", "ipv6RouteProtocol"), ("IPV6-MIB", "ipv6RoutePolicy"), ("IPV6-MIB", "ipv6RouteAge"), ("IPV6-MIB", "ipv6RouteNextHopRDI"), ("IPV6-MIB", "ipv6RouteMetric"), ("IPV6-MIB", "ipv6RouteWeight"), ("IPV6-MIB", "ipv6RouteInfo"), ("IPV6-MIB", "ipv6RouteValid"), ("IPV6-MIB", "ipv6NetToMediaPhysAddress"), ("IPV6-MIB", "ipv6NetToMediaType"), ("IPV6-MIB", "ipv6IfNetToMediaState"), ("IPV6-MIB", "ipv6IfNetToMediaLastUpdated"), ("IPV6-MIB", "ipv6NetToMediaValid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6GeneralGroup = ipv6GeneralGroup.setStatus('obsolete')
ipv6NotificationGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 55, 3, 2, 2)).setObjects(("IPV6-MIB", "ipv6IfStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6NotificationGroup = ipv6NotificationGroup.setStatus('obsolete')
mibBuilder.exportSymbols("IPV6-MIB", ipv6RouteNextHop=ipv6RouteNextHop, ipv6IfStatsInTruncatedPkts=ipv6IfStatsInTruncatedPkts, ipv6RouteNextHopRDI=ipv6RouteNextHopRDI, ipv6RouteMetric=ipv6RouteMetric, ipv6IfStatsOutForwDatagrams=ipv6IfStatsOutForwDatagrams, ipv6IfStatsInDiscards=ipv6IfStatsInDiscards, ipv6IfStatsOutMcastPkts=ipv6IfStatsOutMcastPkts, ipv6AddrPrefixOnLinkFlag=ipv6AddrPrefixOnLinkFlag, ipv6NetToMediaPhysAddress=ipv6NetToMediaPhysAddress, ipv6AddrPrefixAdvPreferredLifetime=ipv6AddrPrefixAdvPreferredLifetime, ipv6IfLastChange=ipv6IfLastChange, ipv6NetToMediaNetAddress=ipv6NetToMediaNetAddress, ipv6IfPhysicalAddress=ipv6IfPhysicalAddress, ipv6IfStatsInDelivers=ipv6IfStatsInDelivers, ipv6AddrPrefixAutonomousFlag=ipv6AddrPrefixAutonomousFlag, ipv6NetToMediaTable=ipv6NetToMediaTable, ipv6IfIdentifierLength=ipv6IfIdentifierLength, ipv6AddrAddress=ipv6AddrAddress, ipv6NotificationPrefix=ipv6NotificationPrefix, ipv6IfStatsOutDiscards=ipv6IfStatsOutDiscards, ipv6NetToMediaEntry=ipv6NetToMediaEntry, ipv6RouteIfIndex=ipv6RouteIfIndex, ipv6RouteWeight=ipv6RouteWeight, ipv6RouteType=ipv6RouteType, ipv6RouteDest=ipv6RouteDest, ipv6IfStatsInHdrErrors=ipv6IfStatsInHdrErrors, ipv6MIB=ipv6MIB, ipv6Groups=ipv6Groups, ipv6AddrPrefixEntry=ipv6AddrPrefixEntry, ipv6AddrAnycastFlag=ipv6AddrAnycastFlag, ipv6AddrType=ipv6AddrType, ipv6AddrPfxLength=ipv6AddrPfxLength, ipv6Forwarding=ipv6Forwarding, ipv6IfStatsOutFragCreates=ipv6IfStatsOutFragCreates, ipv6IfIndex=ipv6IfIndex, ipv6RouteAge=ipv6RouteAge, ipv6IfStateChange=ipv6IfStateChange, ipv6IfStatsReasmOKs=ipv6IfStatsReasmOKs, ipv6NotificationGroup=ipv6NotificationGroup, ipv6Interfaces=ipv6Interfaces, ipv6AddrTable=ipv6AddrTable, ipv6Conformance=ipv6Conformance, ipv6MIBObjects=ipv6MIBObjects, ipv6NetToMediaValid=ipv6NetToMediaValid, ipv6GeneralGroup=ipv6GeneralGroup, ipv6DefaultHopLimit=ipv6DefaultHopLimit, ipv6IfDescr=ipv6IfDescr, ipv6AddrEntry=ipv6AddrEntry, ipv6RouteInfo=ipv6RouteInfo, ipv6RoutePolicy=ipv6RoutePolicy, ipv6IfLowerLayer=ipv6IfLowerLayer, ipv6Compliance=ipv6Compliance, ipv6RouteNumber=ipv6RouteNumber, ipv6IfTableLastChange=ipv6IfTableLastChange, ipv6DiscardedRoutes=ipv6DiscardedRoutes, ipv6IfStatsOutRequests=ipv6IfStatsOutRequests, ipv6AddrPrefixAdvValidLifetime=ipv6AddrPrefixAdvValidLifetime, PYSNMP_MODULE_ID=ipv6MIB, ipv6RoutePfxLength=ipv6RoutePfxLength, ipv6IfOperStatus=ipv6IfOperStatus, ipv6NetToMediaType=ipv6NetToMediaType, ipv6IfNetToMediaState=ipv6IfNetToMediaState, ipv6IfNetToMediaLastUpdated=ipv6IfNetToMediaLastUpdated, ipv6RouteIndex=ipv6RouteIndex, ipv6IfEntry=ipv6IfEntry, ipv6IfStatsOutFragOKs=ipv6IfStatsOutFragOKs, ipv6AddrPrefixLength=ipv6AddrPrefixLength, ipv6IfReasmMaxSize=ipv6IfReasmMaxSize, ipv6IfStatsInTooBigErrors=ipv6IfStatsInTooBigErrors, ipv6RouteTable=ipv6RouteTable, ipv6Compliances=ipv6Compliances, ipv6RouteEntry=ipv6RouteEntry, ipv6RouteProtocol=ipv6RouteProtocol, ipv6IfStatsInAddrErrors=ipv6IfStatsInAddrErrors, ipv6IfStatsOutFragFails=ipv6IfStatsOutFragFails, ipv6IfEffectiveMtu=ipv6IfEffectiveMtu, ipv6IfIdentifier=ipv6IfIdentifier, ipv6IfStatsInMcastPkts=ipv6IfStatsInMcastPkts, ipv6AddrPrefix=ipv6AddrPrefix, ipv6IfStatsReasmFails=ipv6IfStatsReasmFails, ipv6IfAdminStatus=ipv6IfAdminStatus, ipv6IfStatsInUnknownProtos=ipv6IfStatsInUnknownProtos, ipv6Notifications=ipv6Notifications, ipv6AddrStatus=ipv6AddrStatus, ipv6IfTable=ipv6IfTable, ipv6IfStatsEntry=ipv6IfStatsEntry, ipv6IfStatsReasmReqds=ipv6IfStatsReasmReqds, ipv6IfStatsTable=ipv6IfStatsTable, ipv6RouteValid=ipv6RouteValid, ipv6IfStatsInNoRoutes=ipv6IfStatsInNoRoutes, ipv6AddrPrefixTable=ipv6AddrPrefixTable, ipv6IfStatsInReceives=ipv6IfStatsInReceives)
