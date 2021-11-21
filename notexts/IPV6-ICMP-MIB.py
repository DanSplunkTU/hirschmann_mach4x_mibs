#
# PySNMP MIB module IPV6-ICMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IPV6-ICMP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:25:42 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ipv6IfEntry, = mibBuilder.importSymbols("IPV6-MIB", "ipv6IfEntry")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
mib_2, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, Bits, Gauge32, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, NotificationType, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "Bits", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "NotificationType", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ipv6IcmpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 56))
ipv6IcmpMIB.setRevisions(('2017-02-22 00:00', '1998-01-08 21:55',))
if mibBuilder.loadTexts: ipv6IcmpMIB.setLastUpdated('201702220000Z')
if mibBuilder.loadTexts: ipv6IcmpMIB.setOrganization('IETF IPv6 Working Group')
ipv6IcmpMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 1))
ipv6IfIcmpTable = MibTable((1, 3, 6, 1, 2, 1, 56, 1, 1), )
if mibBuilder.loadTexts: ipv6IfIcmpTable.setStatus('obsolete')
ipv6IfIcmpEntry = MibTableRow((1, 3, 6, 1, 2, 1, 56, 1, 1, 1), )
ipv6IfEntry.registerAugmentions(("IPV6-ICMP-MIB", "ipv6IfIcmpEntry"))
ipv6IfIcmpEntry.setIndexNames(*ipv6IfEntry.getIndexNames())
if mibBuilder.loadTexts: ipv6IfIcmpEntry.setStatus('obsolete')
ipv6IfIcmpInMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInMsgs.setStatus('obsolete')
ipv6IfIcmpInErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInErrors.setStatus('obsolete')
ipv6IfIcmpInDestUnreachs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInDestUnreachs.setStatus('obsolete')
ipv6IfIcmpInAdminProhibs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInAdminProhibs.setStatus('obsolete')
ipv6IfIcmpInTimeExcds = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInTimeExcds.setStatus('obsolete')
ipv6IfIcmpInParmProblems = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInParmProblems.setStatus('obsolete')
ipv6IfIcmpInPktTooBigs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInPktTooBigs.setStatus('obsolete')
ipv6IfIcmpInEchos = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInEchos.setStatus('obsolete')
ipv6IfIcmpInEchoReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInEchoReplies.setStatus('obsolete')
ipv6IfIcmpInRouterSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInRouterSolicits.setStatus('obsolete')
ipv6IfIcmpInRouterAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInRouterAdvertisements.setStatus('obsolete')
ipv6IfIcmpInNeighborSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInNeighborSolicits.setStatus('obsolete')
ipv6IfIcmpInNeighborAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInNeighborAdvertisements.setStatus('obsolete')
ipv6IfIcmpInRedirects = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInRedirects.setStatus('obsolete')
ipv6IfIcmpInGroupMembQueries = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInGroupMembQueries.setStatus('obsolete')
ipv6IfIcmpInGroupMembResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInGroupMembResponses.setStatus('obsolete')
ipv6IfIcmpInGroupMembReductions = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpInGroupMembReductions.setStatus('obsolete')
ipv6IfIcmpOutMsgs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutMsgs.setStatus('obsolete')
ipv6IfIcmpOutErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutErrors.setStatus('obsolete')
ipv6IfIcmpOutDestUnreachs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutDestUnreachs.setStatus('obsolete')
ipv6IfIcmpOutAdminProhibs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutAdminProhibs.setStatus('obsolete')
ipv6IfIcmpOutTimeExcds = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutTimeExcds.setStatus('obsolete')
ipv6IfIcmpOutParmProblems = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutParmProblems.setStatus('obsolete')
ipv6IfIcmpOutPktTooBigs = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutPktTooBigs.setStatus('obsolete')
ipv6IfIcmpOutEchos = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutEchos.setStatus('obsolete')
ipv6IfIcmpOutEchoReplies = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutEchoReplies.setStatus('obsolete')
ipv6IfIcmpOutRouterSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutRouterSolicits.setStatus('obsolete')
ipv6IfIcmpOutRouterAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutRouterAdvertisements.setStatus('obsolete')
ipv6IfIcmpOutNeighborSolicits = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutNeighborSolicits.setStatus('obsolete')
ipv6IfIcmpOutNeighborAdvertisements = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutNeighborAdvertisements.setStatus('obsolete')
ipv6IfIcmpOutRedirects = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutRedirects.setStatus('obsolete')
ipv6IfIcmpOutGroupMembQueries = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutGroupMembQueries.setStatus('obsolete')
ipv6IfIcmpOutGroupMembResponses = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutGroupMembResponses.setStatus('obsolete')
ipv6IfIcmpOutGroupMembReductions = MibTableColumn((1, 3, 6, 1, 2, 1, 56, 1, 1, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipv6IfIcmpOutGroupMembReductions.setStatus('obsolete')
ipv6IcmpConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 2))
ipv6IcmpCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 2, 1))
ipv6IcmpGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 56, 2, 2))
ipv6IcmpCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 56, 2, 1, 1)).setObjects(("IPV6-ICMP-MIB", "ipv6IcmpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6IcmpCompliance = ipv6IcmpCompliance.setStatus('obsolete')
ipv6IcmpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 56, 2, 2, 1)).setObjects(("IPV6-ICMP-MIB", "ipv6IfIcmpInMsgs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInErrors"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInDestUnreachs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInAdminProhibs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInTimeExcds"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInParmProblems"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInPktTooBigs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInEchos"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInEchoReplies"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInRouterSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInRouterAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInNeighborSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInNeighborAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInRedirects"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembQueries"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembResponses"), ("IPV6-ICMP-MIB", "ipv6IfIcmpInGroupMembReductions"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutMsgs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutErrors"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutDestUnreachs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutAdminProhibs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutTimeExcds"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutParmProblems"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutPktTooBigs"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutEchos"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutEchoReplies"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRouterSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRouterAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutNeighborSolicits"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutNeighborAdvertisements"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutRedirects"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembQueries"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembResponses"), ("IPV6-ICMP-MIB", "ipv6IfIcmpOutGroupMembReductions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ipv6IcmpGroup = ipv6IcmpGroup.setStatus('obsolete')
mibBuilder.exportSymbols("IPV6-ICMP-MIB", ipv6IfIcmpInRedirects=ipv6IfIcmpInRedirects, ipv6IfIcmpOutDestUnreachs=ipv6IfIcmpOutDestUnreachs, ipv6IcmpMIB=ipv6IcmpMIB, ipv6IfIcmpInNeighborSolicits=ipv6IfIcmpInNeighborSolicits, ipv6IfIcmpOutParmProblems=ipv6IfIcmpOutParmProblems, ipv6IcmpCompliances=ipv6IcmpCompliances, ipv6IfIcmpInRouterAdvertisements=ipv6IfIcmpInRouterAdvertisements, ipv6IfIcmpOutNeighborSolicits=ipv6IfIcmpOutNeighborSolicits, ipv6IfIcmpInGroupMembResponses=ipv6IfIcmpInGroupMembResponses, ipv6IfIcmpInEchoReplies=ipv6IfIcmpInEchoReplies, ipv6IcmpGroups=ipv6IcmpGroups, ipv6IcmpGroup=ipv6IcmpGroup, ipv6IfIcmpInParmProblems=ipv6IfIcmpInParmProblems, ipv6IfIcmpInGroupMembQueries=ipv6IfIcmpInGroupMembQueries, ipv6IfIcmpOutEchos=ipv6IfIcmpOutEchos, ipv6IfIcmpOutGroupMembQueries=ipv6IfIcmpOutGroupMembQueries, ipv6IfIcmpOutGroupMembReductions=ipv6IfIcmpOutGroupMembReductions, ipv6IfIcmpOutNeighborAdvertisements=ipv6IfIcmpOutNeighborAdvertisements, ipv6IfIcmpOutRouterAdvertisements=ipv6IfIcmpOutRouterAdvertisements, ipv6IcmpMIBObjects=ipv6IcmpMIBObjects, ipv6IfIcmpInDestUnreachs=ipv6IfIcmpInDestUnreachs, ipv6IfIcmpOutErrors=ipv6IfIcmpOutErrors, ipv6IfIcmpInAdminProhibs=ipv6IfIcmpInAdminProhibs, ipv6IfIcmpInNeighborAdvertisements=ipv6IfIcmpInNeighborAdvertisements, ipv6IfIcmpInEchos=ipv6IfIcmpInEchos, ipv6IfIcmpInMsgs=ipv6IfIcmpInMsgs, ipv6IfIcmpInPktTooBigs=ipv6IfIcmpInPktTooBigs, ipv6IfIcmpOutGroupMembResponses=ipv6IfIcmpOutGroupMembResponses, ipv6IcmpConformance=ipv6IcmpConformance, ipv6IfIcmpOutTimeExcds=ipv6IfIcmpOutTimeExcds, ipv6IfIcmpOutEchoReplies=ipv6IfIcmpOutEchoReplies, ipv6IfIcmpInErrors=ipv6IfIcmpInErrors, ipv6IfIcmpOutAdminProhibs=ipv6IfIcmpOutAdminProhibs, ipv6IfIcmpOutPktTooBigs=ipv6IfIcmpOutPktTooBigs, ipv6IfIcmpInRouterSolicits=ipv6IfIcmpInRouterSolicits, ipv6IcmpCompliance=ipv6IcmpCompliance, ipv6IfIcmpInTimeExcds=ipv6IfIcmpInTimeExcds, ipv6IfIcmpOutRedirects=ipv6IfIcmpOutRedirects, ipv6IfIcmpEntry=ipv6IfIcmpEntry, ipv6IfIcmpOutMsgs=ipv6IfIcmpOutMsgs, ipv6IfIcmpTable=ipv6IfIcmpTable, PYSNMP_MODULE_ID=ipv6IcmpMIB, ipv6IfIcmpOutRouterSolicits=ipv6IfIcmpOutRouterSolicits, ipv6IfIcmpInGroupMembReductions=ipv6IfIcmpInGroupMembReductions)
