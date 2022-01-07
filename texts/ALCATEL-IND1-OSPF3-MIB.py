#
# PySNMP MIB module ALCATEL-IND1-OSPF3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nokia/aos7/ALCATEL-IND1-OSPF3-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:32:37 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
routingIND1Ospf3, = mibBuilder.importSymbols("ALCATEL-IND1-BASE", "routingIND1Ospf3")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
Ipv6IfIndexOrZero, Ipv6Address = mibBuilder.importSymbols("IPV6-TC", "Ipv6IfIndexOrZero", "Ipv6Address")
ospfv3IfEntry, ospfv3AreaEntry = mibBuilder.importSymbols("OSPFV3-MIB", "ospfv3IfEntry", "ospfv3AreaEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, iso, Bits, Gauge32, TimeTicks, Counter32, ObjectIdentity, MibIdentifier, ModuleIdentity, Integer32, Counter64, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "iso", "Bits", "Gauge32", "TimeTicks", "Counter32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Integer32", "Counter64", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
alcatelIND1OSPF3MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1))
alcatelIND1OSPF3MIB.setRevisions(('2014-10-06 00:00', '2007-04-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: alcatelIND1OSPF3MIB.setRevisionsDescriptions(('Added alaOspf3RouteTable.', 'The latest version of this MIB Module.',))
if mibBuilder.loadTexts: alcatelIND1OSPF3MIB.setLastUpdated('201410060000Z')
if mibBuilder.loadTexts: alcatelIND1OSPF3MIB.setOrganization('Alcatel-Lucent')
if mibBuilder.loadTexts: alcatelIND1OSPF3MIB.setContactInfo('Please consult with Customer Service to ensure the most appropriate\n         version of this document is used with the products in question:\n\n                    Alcatel-Lucent, Enterprise Solutions Division\n                   (Formerly Alcatel Internetworking, Incorporated)\n                           26801 West Agoura Road\n                        Agoura Hills, CA  91301-5122\n                          United States Of America\n\n        Telephone:               North America  +1 800 995 2696\n                                 Latin America  +1 877 919 9526\n                                 Europe         +31 23 556 0100\n                                 Asia           +65 394 7933\n                                 All Other      +1 818 878 4507\n\n        Electronic Mail:         support@ind.alcatel.com\n        World Wide Web:          http://alcatel-lucent.com/wps/portal/enterprise\n        File Transfer Protocol:  ftp://ftp.ind.alcatel.com/pub/products/mibs')
if mibBuilder.loadTexts: alcatelIND1OSPF3MIB.setDescription('This module describes an authoritative enterprise-specific Simple\n         Network Management Protocol (SNMP) Management Information Base (MIB):\n\n             This proprietary MIB contains management information for\n             the configuration of OSPFv3 global configuration parameters.\n\n         The right to make changes in specification and other information\n         contained in this document without prior notice is reserved.\n\n         No liability shall be assumed for any incidental, indirect, special, o\nr\n         consequential damages whatsoever arising from or related to this\n         document or the information contained herein.\n\n         Vendors, end-users, and other interested parties are granted\n         non-exclusive license to use this specification in connection with\n         management of the products for which it is intended to be used.\n\n                     Copyright (C) 1995-2003 Alcatel-Lucent\n                         ALL RIGHTS RESERVED WORLDWIDE')
alcatelIND1OSPF3MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1))
alaProtocolOspf3 = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1))
alaOspf3OrigRouteTag = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3OrigRouteTag.setStatus('current')
if mibBuilder.loadTexts: alaOspf3OrigRouteTag.setDescription('Route tag that is originated with ASEs')
alaOspf3TimerSpfDelay = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(5)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3TimerSpfDelay.setStatus('current')
if mibBuilder.loadTexts: alaOspf3TimerSpfDelay.setDescription('Delay (in seconds) between topology change and SPF run')
alaOspf3TimerSpfHold = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3TimerSpfHold.setStatus('current')
if mibBuilder.loadTexts: alaOspf3TimerSpfHold.setDescription('Delay (in seconds) between subsequent SPF executions')
alaOspf3RestartHelperSupport = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3RestartHelperSupport.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RestartHelperSupport.setDescription('This router can be a helper to another restarting router')
alaOspf3RestartStrictLsaChecking = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3RestartStrictLsaChecking.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RestartStrictLsaChecking.setDescription('Will changed LSA result in restart termination')
alaOspf3RestartInitiate = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3RestartInitiate.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RestartInitiate.setDescription('Start a graceful restart')
alaOspf3MTUCheck = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3MTUCheck.setStatus('current')
if mibBuilder.loadTexts: alaOspf3MTUCheck.setDescription('Verify the MTU of a neighbor matches our own.')
alaOspf3RouteTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8), )
if mibBuilder.loadTexts: alaOspf3RouteTable.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RouteTable.setDescription('OSPF3 Routing table. This table contains\n       an entry for each valid OSPF unicast route that\n       can be used for packet forwarding determination.\n       It is for display purposes only.')
alaOspf3RouteEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1), ).setIndexNames((0, "ALCATEL-IND1-OSPF3-MIB", "alaOspf3RouteDest"), (0, "ALCATEL-IND1-OSPF3-MIB", "alaOspf3RoutePfxLength"), (0, "ALCATEL-IND1-OSPF3-MIB", "alaOspf3RouteNextHop"), (0, "ALCATEL-IND1-OSPF3-MIB", "alaOspf3RouteIfIndex"))
if mibBuilder.loadTexts: alaOspf3RouteEntry.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RouteEntry.setDescription('A routing entry.')
alaOspf3RouteDest = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 1), Ipv6Address())
if mibBuilder.loadTexts: alaOspf3RouteDest.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RouteDest.setDescription('The destination IPv6 address of this route.')
alaOspf3RoutePfxLength = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 128))).setUnits('bits')
if mibBuilder.loadTexts: alaOspf3RoutePfxLength.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RoutePfxLength.setDescription('Indicates the prefix length of the destination\n        address.')
alaOspf3RouteNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 3), Ipv6Address())
if mibBuilder.loadTexts: alaOspf3RouteNextHop.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RouteNextHop.setDescription("On remote routes, the address of the next\n        system en route;  otherwise, ::0\n        ('00000000000000000000000000000000'H in ASN.1\n        string representation).")
alaOspf3RouteIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 4), Ipv6IfIndexOrZero())
if mibBuilder.loadTexts: alaOspf3RouteIfIndex.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RouteIfIndex.setDescription('The index value which uniquely identifies the local\n        interface through which the next hop of this\n        route should be reached.')
alaOspf3RouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("host", 1), ("other", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3RouteType.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RouteType.setDescription('The type of this route.')
alaOspf3RoutePathType = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("intraArea", 1), ("interArea", 2), ("externalType1", 3), ("externalType2", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3RoutePathType.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RoutePathType.setDescription('The routing metric path type for this route.')
alaOspf3RouteMetric1 = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3RouteMetric1.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RouteMetric1.setDescription('The primary routing metric for this route.')
alaOspf3RouteMetric2 = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 8, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3RouteMetric2.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RouteMetric2.setDescription("An alternate routing metric for this route. It's 0\n         for internal routes. For an external route, it's the metric\n         to reach the ASBR that announced the external route.")
alaOspf3BfdStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3BfdStatus.setStatus('current')
if mibBuilder.loadTexts: alaOspf3BfdStatus.setDescription('Enables or disables bfd  for OSPF protocol')
alaOspf3BfdAllInterfaceStatus = MibScalar((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: alaOspf3BfdAllInterfaceStatus.setStatus('current')
if mibBuilder.loadTexts: alaOspf3BfdAllInterfaceStatus.setDescription('Enables or disables bfd for all OSPF interfaces')
alaOspf3IfAugTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 11), )
if mibBuilder.loadTexts: alaOspf3IfAugTable.setStatus('current')
if mibBuilder.loadTexts: alaOspf3IfAugTable.setDescription('Expansion for ospf3IfTable')
alaOspf3IfAugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 11, 1), )
ospfv3IfEntry.registerAugmentions(("ALCATEL-IND1-OSPF3-MIB", "alaOspf3IfAugEntry"))
alaOspf3IfAugEntry.setIndexNames(*ospfv3IfEntry.getIndexNames())
if mibBuilder.loadTexts: alaOspf3IfAugEntry.setStatus('current')
if mibBuilder.loadTexts: alaOspf3IfAugEntry.setDescription('An entry of alaOspf3IfAugTable')
alaOspf3IfBfdStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 11, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaOspf3IfBfdStatus.setStatus('current')
if mibBuilder.loadTexts: alaOspf3IfBfdStatus.setDescription('Enables/Disables OSP3F for a BFD interface')
alaOspf3IfBfdDrsOnly = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 11, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: alaOspf3IfBfdDrsOnly.setStatus('current')
if mibBuilder.loadTexts: alaOspf3IfBfdDrsOnly.setDescription('Enables/Disables Drs Only option for a BFD interface')
alaOspf3AreaAugTable = MibTable((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12), )
if mibBuilder.loadTexts: alaOspf3AreaAugTable.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaAugTable.setDescription('This table extends the ofpv3 area table and it is used to \n        display very granular LSA Counts, Host and Interface counts')
alaOspf3AreaAugEntry = MibTableRow((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1), )
ospfv3AreaEntry.registerAugmentions(("ALCATEL-IND1-OSPF3-MIB", "alaOspf3AreaAugEntry"))
alaOspf3AreaAugEntry.setIndexNames(*ospfv3AreaEntry.getIndexNames())
if mibBuilder.loadTexts: alaOspf3AreaAugEntry.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaAugEntry.setDescription('An entry of alaOspf3AreaAugTable')
alaOspf3AreaRouterLsaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3AreaRouterLsaCount.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaRouterLsaCount.setDescription('This object indicates the Router LSA Count.')
alaOspf3AreaNetworkLsaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3AreaNetworkLsaCount.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaNetworkLsaCount.setDescription('This object indicates the Network LSA Count.')
alaOspf3AreaIntraAreaPrefixLsaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3AreaIntraAreaPrefixLsaCount.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaIntraAreaPrefixLsaCount.setDescription('This object indicates the Intra Area LSA Count.')
alaOspf3AreaInterAreaPrefixLsaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3AreaInterAreaPrefixLsaCount.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaInterAreaPrefixLsaCount.setDescription('This object indicates the Inter area LSA Count.')
alaOspf3AreaInterAreaRouterLsaCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3AreaInterAreaRouterLsaCount.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaInterAreaRouterLsaCount.setDescription('This object indicates the inter area Router LSA Count.')
alaOspf3AreaHostCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3AreaHostCount.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaHostCount.setDescription('This object indicates the host count.')
alaOspf3AreaInterfaceCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3AreaInterfaceCount.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaInterfaceCount.setDescription('This object indicates the Interface count.')
alaOspf3AreaSummarizationRangeCount = MibTableColumn((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 1, 1, 12, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alaOspf3AreaSummarizationRangeCount.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaSummarizationRangeCount.setDescription('This object indicates the summarization range count.')
alcatelIND1OSPF3MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2))
alcatelIND1OSPF3MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 1))
alcatelIND1OSPF3MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 2))
alcatelIND1OSPF3MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 1, 1)).setObjects(("ALCATEL-IND1-OSPF3-MIB", "alaOSPF3ConfigMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alcatelIND1OSPF3MIBCompliance = alcatelIND1OSPF3MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: alcatelIND1OSPF3MIBCompliance.setDescription('The compliance statement for OSPFv3\n             and implementing the ALCATEL-IND1-OSPF3 MIB.')
alaOSPF3ConfigMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 2, 1)).setObjects(("ALCATEL-IND1-OSPF3-MIB", "alaOspf3OrigRouteTag"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3TimerSpfDelay"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3TimerSpfHold"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartHelperSupport"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartStrictLsaChecking"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RestartInitiate"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3MTUCheck"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaOSPF3ConfigMIBGroup = alaOSPF3ConfigMIBGroup.setStatus('current')
if mibBuilder.loadTexts: alaOSPF3ConfigMIBGroup.setDescription('A collection of objects to support management of OSPF3.')
alaOspf3RouteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 2, 2)).setObjects(("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RouteType"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RoutePathType"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RouteMetric1"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3RouteMetric2"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3BfdStatus"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3BfdAllInterfaceStatus"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3IfBfdDrsOnly"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3IfBfdStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaOspf3RouteGroup = alaOspf3RouteGroup.setStatus('current')
if mibBuilder.loadTexts: alaOspf3RouteGroup.setDescription('Collection of objects for management of Network Route.')
alaOspf3AreaGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 13, 1, 2, 2, 3)).setObjects(("ALCATEL-IND1-OSPF3-MIB", "alaOspf3AreaRouterLsaCount"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3AreaNetworkLsaCount"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3AreaIntraAreaPrefixLsaCount"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3AreaInterAreaPrefixLsaCount"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3AreaInterAreaRouterLsaCount"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3AreaHostCount"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3AreaInterfaceCount"), ("ALCATEL-IND1-OSPF3-MIB", "alaOspf3AreaSummarizationRangeCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    alaOspf3AreaGroup = alaOspf3AreaGroup.setStatus('current')
if mibBuilder.loadTexts: alaOspf3AreaGroup.setDescription('Collection of objects for management of Router LSAs.')
mibBuilder.exportSymbols("ALCATEL-IND1-OSPF3-MIB", alaOspf3RouteType=alaOspf3RouteType, alaOspf3TimerSpfHold=alaOspf3TimerSpfHold, alaOspf3MTUCheck=alaOspf3MTUCheck, alaOspf3RoutePathType=alaOspf3RoutePathType, alaOspf3AreaHostCount=alaOspf3AreaHostCount, alcatelIND1OSPF3MIBCompliance=alcatelIND1OSPF3MIBCompliance, alaOSPF3ConfigMIBGroup=alaOSPF3ConfigMIBGroup, alaOspf3RestartStrictLsaChecking=alaOspf3RestartStrictLsaChecking, alaOspf3RestartHelperSupport=alaOspf3RestartHelperSupport, alaOspf3IfBfdStatus=alaOspf3IfBfdStatus, alaOspf3RouteNextHop=alaOspf3RouteNextHop, alaOspf3BfdStatus=alaOspf3BfdStatus, alaOspf3TimerSpfDelay=alaOspf3TimerSpfDelay, alaOspf3AreaIntraAreaPrefixLsaCount=alaOspf3AreaIntraAreaPrefixLsaCount, alaOspf3RouteEntry=alaOspf3RouteEntry, alaOspf3AreaAugEntry=alaOspf3AreaAugEntry, alaOspf3RouteIfIndex=alaOspf3RouteIfIndex, alcatelIND1OSPF3MIB=alcatelIND1OSPF3MIB, alaOspf3IfAugEntry=alaOspf3IfAugEntry, alaOspf3IfBfdDrsOnly=alaOspf3IfBfdDrsOnly, alcatelIND1OSPF3MIBGroups=alcatelIND1OSPF3MIBGroups, alaOspf3AreaGroup=alaOspf3AreaGroup, alaOspf3OrigRouteTag=alaOspf3OrigRouteTag, alaOspf3RouteGroup=alaOspf3RouteGroup, alaOspf3RouteMetric2=alaOspf3RouteMetric2, alaOspf3RouteDest=alaOspf3RouteDest, alaOspf3AreaAugTable=alaOspf3AreaAugTable, alaOspf3AreaInterAreaPrefixLsaCount=alaOspf3AreaInterAreaPrefixLsaCount, alaOspf3IfAugTable=alaOspf3IfAugTable, alcatelIND1OSPF3MIBObjects=alcatelIND1OSPF3MIBObjects, alaOspf3AreaNetworkLsaCount=alaOspf3AreaNetworkLsaCount, alcatelIND1OSPF3MIBCompliances=alcatelIND1OSPF3MIBCompliances, PYSNMP_MODULE_ID=alcatelIND1OSPF3MIB, alaOspf3BfdAllInterfaceStatus=alaOspf3BfdAllInterfaceStatus, alaOspf3AreaInterfaceCount=alaOspf3AreaInterfaceCount, alaOspf3RestartInitiate=alaOspf3RestartInitiate, alaOspf3RouteMetric1=alaOspf3RouteMetric1, alaOspf3AreaRouterLsaCount=alaOspf3AreaRouterLsaCount, alaOspf3AreaInterAreaRouterLsaCount=alaOspf3AreaInterAreaRouterLsaCount, alaOspf3AreaSummarizationRangeCount=alaOspf3AreaSummarizationRangeCount, alcatelIND1OSPF3MIBConformance=alcatelIND1OSPF3MIBConformance, alaOspf3RoutePfxLength=alaOspf3RoutePfxLength, alaOspf3RouteTable=alaOspf3RouteTable, alaProtocolOspf3=alaProtocolOspf3)
