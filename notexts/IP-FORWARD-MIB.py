#
# PySNMP MIB module IP-FORWARD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/IP-FORWARD-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:32 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
IANAipRouteProtocol, = mibBuilder.importSymbols("IANA-RTPROTO-MIB", "IANAipRouteProtocol")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
InetAutonomousSystemNumber, InetAddressType, InetAddressPrefixLength, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAutonomousSystemNumber", "InetAddressType", "InetAddressPrefixLength", "InetAddress")
ip, = mibBuilder.importSymbols("IP-MIB", "ip")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Unsigned32, ModuleIdentity, iso, MibIdentifier, Counter32, NotificationType, Bits, TimeTicks, Counter64, ObjectIdentity, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ModuleIdentity", "iso", "MibIdentifier", "Counter32", "NotificationType", "Bits", "TimeTicks", "Counter64", "ObjectIdentity", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ipForward = ModuleIdentity((1, 3, 6, 1, 2, 1, 4, 24))
ipForward.setRevisions(('2006-02-01 00:00', '1996-09-19 00:00', '1992-07-02 21:56',))
if mibBuilder.loadTexts: ipForward.setLastUpdated('200602010000Z')
if mibBuilder.loadTexts: ipForward.setOrganization('IETF IPv6 Working Group http://www.ietf.org/html.charters/ipv6-charter.html')
inetCidrRouteNumber = MibScalar((1, 3, 6, 1, 2, 1, 4, 24, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetCidrRouteNumber.setStatus('current')
inetCidrRouteDiscards = MibScalar((1, 3, 6, 1, 2, 1, 4, 24, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetCidrRouteDiscards.setStatus('current')
inetCidrRouteTable = MibTable((1, 3, 6, 1, 2, 1, 4, 24, 7), )
if mibBuilder.loadTexts: inetCidrRouteTable.setStatus('current')
inetCidrRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 24, 7, 1), ).setIndexNames((0, "IP-FORWARD-MIB", "inetCidrRouteDestType"), (0, "IP-FORWARD-MIB", "inetCidrRouteDest"), (0, "IP-FORWARD-MIB", "inetCidrRoutePfxLen"), (0, "IP-FORWARD-MIB", "inetCidrRoutePolicy"), (0, "IP-FORWARD-MIB", "inetCidrRouteNextHopType"), (0, "IP-FORWARD-MIB", "inetCidrRouteNextHop"))
if mibBuilder.loadTexts: inetCidrRouteEntry.setStatus('current')
inetCidrRouteDestType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 1), InetAddressType())
if mibBuilder.loadTexts: inetCidrRouteDestType.setStatus('current')
inetCidrRouteDest = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 2), InetAddress())
if mibBuilder.loadTexts: inetCidrRouteDest.setStatus('current')
inetCidrRoutePfxLen = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 3), InetAddressPrefixLength())
if mibBuilder.loadTexts: inetCidrRoutePfxLen.setStatus('current')
inetCidrRoutePolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 4), ObjectIdentifier())
if mibBuilder.loadTexts: inetCidrRoutePolicy.setStatus('current')
inetCidrRouteNextHopType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 5), InetAddressType())
if mibBuilder.loadTexts: inetCidrRouteNextHopType.setStatus('current')
inetCidrRouteNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 6), InetAddress())
if mibBuilder.loadTexts: inetCidrRouteNextHop.setStatus('current')
inetCidrRouteIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 7), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteIfIndex.setStatus('current')
inetCidrRouteType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("reject", 2), ("local", 3), ("remote", 4), ("blackhole", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteType.setStatus('current')
inetCidrRouteProto = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 9), IANAipRouteProtocol()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetCidrRouteProto.setStatus('current')
inetCidrRouteAge = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: inetCidrRouteAge.setStatus('current')
inetCidrRouteNextHopAS = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 11), InetAutonomousSystemNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteNextHopAS.setStatus('current')
inetCidrRouteMetric1 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 12), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteMetric1.setStatus('current')
inetCidrRouteMetric2 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 13), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteMetric2.setStatus('current')
inetCidrRouteMetric3 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 14), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteMetric3.setStatus('current')
inetCidrRouteMetric4 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 15), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteMetric4.setStatus('current')
inetCidrRouteMetric5 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 16), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteMetric5.setStatus('current')
inetCidrRouteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 7, 1, 17), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: inetCidrRouteStatus.setStatus('current')
ipForwardConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 24, 5))
ipForwardGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 24, 5, 1))
ipForwardCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 4, 24, 5, 2))
ipForwardFullCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 3)).setObjects(("IP-FORWARD-MIB", "inetForwardCidrRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipForwardFullCompliance = ipForwardFullCompliance.setStatus('current')
ipForwardReadOnlyCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 4)).setObjects(("IP-FORWARD-MIB", "inetForwardCidrRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipForwardReadOnlyCompliance = ipForwardReadOnlyCompliance.setStatus('current')
inetForwardCidrRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 4)).setObjects(("IP-FORWARD-MIB", "inetCidrRouteDiscards"), ("IP-FORWARD-MIB", "inetCidrRouteIfIndex"), ("IP-FORWARD-MIB", "inetCidrRouteType"), ("IP-FORWARD-MIB", "inetCidrRouteProto"), ("IP-FORWARD-MIB", "inetCidrRouteAge"), ("IP-FORWARD-MIB", "inetCidrRouteNextHopAS"), ("IP-FORWARD-MIB", "inetCidrRouteMetric1"), ("IP-FORWARD-MIB", "inetCidrRouteMetric2"), ("IP-FORWARD-MIB", "inetCidrRouteMetric3"), ("IP-FORWARD-MIB", "inetCidrRouteMetric4"), ("IP-FORWARD-MIB", "inetCidrRouteMetric5"), ("IP-FORWARD-MIB", "inetCidrRouteStatus"), ("IP-FORWARD-MIB", "inetCidrRouteNumber"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    inetForwardCidrRouteGroup = inetForwardCidrRouteGroup.setStatus('current')
ipCidrRouteNumber = MibScalar((1, 3, 6, 1, 2, 1, 4, 24, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteNumber.setStatus('deprecated')
ipCidrRouteTable = MibTable((1, 3, 6, 1, 2, 1, 4, 24, 4), )
if mibBuilder.loadTexts: ipCidrRouteTable.setStatus('deprecated')
ipCidrRouteEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 24, 4, 1), ).setIndexNames((0, "IP-FORWARD-MIB", "ipCidrRouteDest"), (0, "IP-FORWARD-MIB", "ipCidrRouteMask"), (0, "IP-FORWARD-MIB", "ipCidrRouteTos"), (0, "IP-FORWARD-MIB", "ipCidrRouteNextHop"))
if mibBuilder.loadTexts: ipCidrRouteEntry.setStatus('deprecated')
ipCidrRouteDest = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteDest.setStatus('deprecated')
ipCidrRouteMask = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteMask.setStatus('deprecated')
ipCidrRouteTos = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteTos.setStatus('deprecated')
ipCidrRouteNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteNextHop.setStatus('deprecated')
ipCidrRouteIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteIfIndex.setStatus('deprecated')
ipCidrRouteType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("reject", 2), ("local", 3), ("remote", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteType.setStatus('deprecated')
ipCidrRouteProto = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("isIs", 9), ("esIs", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15), ("ciscoEigrp", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteProto.setStatus('deprecated')
ipCidrRouteAge = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipCidrRouteAge.setStatus('deprecated')
ipCidrRouteInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 9), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteInfo.setStatus('deprecated')
ipCidrRouteNextHopAS = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteNextHopAS.setStatus('deprecated')
ipCidrRouteMetric1 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 11), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteMetric1.setStatus('deprecated')
ipCidrRouteMetric2 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 12), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteMetric2.setStatus('deprecated')
ipCidrRouteMetric3 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 13), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteMetric3.setStatus('deprecated')
ipCidrRouteMetric4 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 14), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteMetric4.setStatus('deprecated')
ipCidrRouteMetric5 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 15), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteMetric5.setStatus('deprecated')
ipCidrRouteStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 4, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipCidrRouteStatus.setStatus('deprecated')
ipForwardCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 1)).setObjects(("IP-FORWARD-MIB", "ipForwardCidrRouteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipForwardCompliance = ipForwardCompliance.setStatus('deprecated')
ipForwardCidrRouteGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 3)).setObjects(("IP-FORWARD-MIB", "ipCidrRouteNumber"), ("IP-FORWARD-MIB", "ipCidrRouteDest"), ("IP-FORWARD-MIB", "ipCidrRouteMask"), ("IP-FORWARD-MIB", "ipCidrRouteTos"), ("IP-FORWARD-MIB", "ipCidrRouteNextHop"), ("IP-FORWARD-MIB", "ipCidrRouteIfIndex"), ("IP-FORWARD-MIB", "ipCidrRouteType"), ("IP-FORWARD-MIB", "ipCidrRouteProto"), ("IP-FORWARD-MIB", "ipCidrRouteAge"), ("IP-FORWARD-MIB", "ipCidrRouteInfo"), ("IP-FORWARD-MIB", "ipCidrRouteNextHopAS"), ("IP-FORWARD-MIB", "ipCidrRouteMetric1"), ("IP-FORWARD-MIB", "ipCidrRouteMetric2"), ("IP-FORWARD-MIB", "ipCidrRouteMetric3"), ("IP-FORWARD-MIB", "ipCidrRouteMetric4"), ("IP-FORWARD-MIB", "ipCidrRouteMetric5"), ("IP-FORWARD-MIB", "ipCidrRouteStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipForwardCidrRouteGroup = ipForwardCidrRouteGroup.setStatus('deprecated')
ipForwardNumber = MibScalar((1, 3, 6, 1, 2, 1, 4, 24, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardNumber.setStatus('obsolete')
ipForwardTable = MibTable((1, 3, 6, 1, 2, 1, 4, 24, 2), )
if mibBuilder.loadTexts: ipForwardTable.setStatus('obsolete')
ipForwardEntry = MibTableRow((1, 3, 6, 1, 2, 1, 4, 24, 2, 1), ).setIndexNames((0, "IP-FORWARD-MIB", "ipForwardDest"), (0, "IP-FORWARD-MIB", "ipForwardProto"), (0, "IP-FORWARD-MIB", "ipForwardPolicy"), (0, "IP-FORWARD-MIB", "ipForwardNextHop"))
if mibBuilder.loadTexts: ipForwardEntry.setStatus('obsolete')
ipForwardDest = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardDest.setStatus('obsolete')
ipForwardMask = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 2), IpAddress().clone(hexValue="00000000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMask.setStatus('obsolete')
ipForwardPolicy = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardPolicy.setStatus('obsolete')
ipForwardNextHop = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardNextHop.setStatus('obsolete')
ipForwardIfIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardIfIndex.setStatus('obsolete')
ipForwardType = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("invalid", 2), ("local", 3), ("remote", 4))).clone('invalid')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardType.setStatus('obsolete')
ipForwardProto = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15))).clone(namedValues=NamedValues(("other", 1), ("local", 2), ("netmgmt", 3), ("icmp", 4), ("egp", 5), ("ggp", 6), ("hello", 7), ("rip", 8), ("is-is", 9), ("es-is", 10), ("ciscoIgrp", 11), ("bbnSpfIgp", 12), ("ospf", 13), ("bgp", 14), ("idpr", 15)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardProto.setStatus('obsolete')
ipForwardAge = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipForwardAge.setStatus('obsolete')
ipForwardInfo = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 9), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardInfo.setStatus('obsolete')
ipForwardNextHopAS = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 10), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardNextHopAS.setStatus('obsolete')
ipForwardMetric1 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 11), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMetric1.setStatus('obsolete')
ipForwardMetric2 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 12), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMetric2.setStatus('obsolete')
ipForwardMetric3 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 13), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMetric3.setStatus('obsolete')
ipForwardMetric4 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 14), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMetric4.setStatus('obsolete')
ipForwardMetric5 = MibTableColumn((1, 3, 6, 1, 2, 1, 4, 24, 2, 1, 15), Integer32().clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipForwardMetric5.setStatus('obsolete')
ipForwardOldCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 4, 24, 5, 2, 2)).setObjects(("IP-FORWARD-MIB", "ipForwardMultiPathGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipForwardOldCompliance = ipForwardOldCompliance.setStatus('obsolete')
ipForwardMultiPathGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 4, 24, 5, 1, 2)).setObjects(("IP-FORWARD-MIB", "ipForwardNumber"), ("IP-FORWARD-MIB", "ipForwardDest"), ("IP-FORWARD-MIB", "ipForwardMask"), ("IP-FORWARD-MIB", "ipForwardPolicy"), ("IP-FORWARD-MIB", "ipForwardNextHop"), ("IP-FORWARD-MIB", "ipForwardIfIndex"), ("IP-FORWARD-MIB", "ipForwardType"), ("IP-FORWARD-MIB", "ipForwardProto"), ("IP-FORWARD-MIB", "ipForwardAge"), ("IP-FORWARD-MIB", "ipForwardInfo"), ("IP-FORWARD-MIB", "ipForwardNextHopAS"), ("IP-FORWARD-MIB", "ipForwardMetric1"), ("IP-FORWARD-MIB", "ipForwardMetric2"), ("IP-FORWARD-MIB", "ipForwardMetric3"), ("IP-FORWARD-MIB", "ipForwardMetric4"), ("IP-FORWARD-MIB", "ipForwardMetric5"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipForwardMultiPathGroup = ipForwardMultiPathGroup.setStatus('obsolete')
mibBuilder.exportSymbols("IP-FORWARD-MIB", inetCidrRouteDestType=inetCidrRouteDestType, inetCidrRouteMetric3=inetCidrRouteMetric3, ipForward=ipForward, ipCidrRouteMask=ipCidrRouteMask, ipForwardIfIndex=ipForwardIfIndex, ipCidrRouteMetric2=ipCidrRouteMetric2, inetCidrRouteNumber=inetCidrRouteNumber, ipForwardNextHopAS=ipForwardNextHopAS, ipForwardCompliance=ipForwardCompliance, ipForwardMetric2=ipForwardMetric2, ipForwardFullCompliance=ipForwardFullCompliance, inetForwardCidrRouteGroup=inetForwardCidrRouteGroup, ipForwardReadOnlyCompliance=ipForwardReadOnlyCompliance, ipForwardMultiPathGroup=ipForwardMultiPathGroup, PYSNMP_MODULE_ID=ipForward, ipCidrRouteTos=ipCidrRouteTos, ipForwardTable=ipForwardTable, ipCidrRouteInfo=ipCidrRouteInfo, inetCidrRouteMetric1=inetCidrRouteMetric1, inetCidrRouteNextHopAS=inetCidrRouteNextHopAS, ipForwardMetric5=ipForwardMetric5, ipCidrRouteNextHopAS=ipCidrRouteNextHopAS, ipForwardMetric1=ipForwardMetric1, inetCidrRouteNextHop=inetCidrRouteNextHop, ipCidrRouteNextHop=ipCidrRouteNextHop, ipCidrRouteMetric3=ipCidrRouteMetric3, ipForwardType=ipForwardType, ipForwardProto=ipForwardProto, ipForwardInfo=ipForwardInfo, ipCidrRouteTable=ipCidrRouteTable, inetCidrRouteDiscards=inetCidrRouteDiscards, inetCidrRouteMetric4=inetCidrRouteMetric4, ipCidrRouteMetric1=ipCidrRouteMetric1, inetCidrRoutePolicy=inetCidrRoutePolicy, ipForwardConformance=ipForwardConformance, ipCidrRouteStatus=ipCidrRouteStatus, inetCidrRoutePfxLen=inetCidrRoutePfxLen, ipForwardGroups=ipForwardGroups, ipForwardMetric3=ipForwardMetric3, inetCidrRouteTable=inetCidrRouteTable, inetCidrRouteEntry=inetCidrRouteEntry, inetCidrRouteProto=inetCidrRouteProto, inetCidrRouteAge=inetCidrRouteAge, inetCidrRouteNextHopType=inetCidrRouteNextHopType, ipCidrRouteIfIndex=ipCidrRouteIfIndex, ipForwardPolicy=ipForwardPolicy, ipCidrRouteMetric4=ipCidrRouteMetric4, ipForwardMetric4=ipForwardMetric4, ipForwardCompliances=ipForwardCompliances, ipForwardCidrRouteGroup=ipForwardCidrRouteGroup, inetCidrRouteType=inetCidrRouteType, ipForwardEntry=ipForwardEntry, ipForwardNextHop=ipForwardNextHop, ipCidrRouteDest=ipCidrRouteDest, inetCidrRouteMetric2=inetCidrRouteMetric2, ipCidrRouteMetric5=ipCidrRouteMetric5, ipForwardNumber=ipForwardNumber, ipForwardDest=ipForwardDest, inetCidrRouteDest=inetCidrRouteDest, ipCidrRouteEntry=ipCidrRouteEntry, inetCidrRouteIfIndex=inetCidrRouteIfIndex, ipCidrRouteProto=ipCidrRouteProto, ipForwardMask=ipForwardMask, inetCidrRouteStatus=inetCidrRouteStatus, ipForwardAge=ipForwardAge, ipForwardOldCompliance=ipForwardOldCompliance, inetCidrRouteMetric5=inetCidrRouteMetric5, ipCidrRouteType=ipCidrRouteType, ipCidrRouteNumber=ipCidrRouteNumber, ipCidrRouteAge=ipCidrRouteAge)
