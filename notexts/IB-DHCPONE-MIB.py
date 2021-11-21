#
# PySNMP MIB module IB-DHCPONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DHCPONE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:27:58 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
IbIpAddr, ibDHCPOne, IbString = mibBuilder.importSymbols("IB-SMI-MIB", "IbIpAddr", "ibDHCPOne", "IbString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, IpAddress, iso, Counter32, Bits, MibIdentifier, NotificationType, enterprises, ModuleIdentity, Integer32, ObjectIdentity, TimeTicks, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "IpAddress", "iso", "Counter32", "Bits", "MibIdentifier", "NotificationType", "enterprises", "ModuleIdentity", "Integer32", "ObjectIdentity", "TimeTicks", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibDhcpModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1))
ibDhcpModule.setRevisions(('2010-03-23 00:00', '2008-02-14 00:00', '2005-01-10 00:00', '2004-05-21 00:00',))
if mibBuilder.loadTexts: ibDhcpModule.setLastUpdated('201003230000Z')
if mibBuilder.loadTexts: ibDhcpModule.setOrganization('Infoblox')
ibDHCPSubnetTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1), )
if mibBuilder.loadTexts: ibDHCPSubnetTable.setStatus('current')
ibDHCPSubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1), ).setIndexNames((0, "IB-DHCPONE-MIB", "ibDHCPSubnetNetworkAddress"))
if mibBuilder.loadTexts: ibDHCPSubnetEntry.setStatus('current')
ibDHCPSubnetNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 1), IbIpAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPSubnetNetworkAddress.setStatus('current')
ibDHCPSubnetNetworkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 2), IbIpAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPSubnetNetworkMask.setStatus('current')
ibDHCPSubnetPercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPSubnetPercentUsed.setStatus('current')
ibDHCPStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3))
ibDhcpTotalNoOfDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfDiscovers.setStatus('current')
ibDhcpTotalNoOfRequests = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfRequests.setStatus('current')
ibDhcpTotalNoOfReleases = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfReleases.setStatus('current')
ibDhcpTotalNoOfOffers = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfOffers.setStatus('current')
ibDhcpTotalNoOfAcks = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfAcks.setStatus('current')
ibDhcpTotalNoOfNacks = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfNacks.setStatus('current')
ibDhcpTotalNoOfDeclines = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfDeclines.setStatus('current')
ibDhcpTotalNoOfInforms = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfInforms.setStatus('current')
ibDhcpTotalNoOfOthers = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfOthers.setStatus('current')
ibDhcpDeferredQueueSize = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpDeferredQueueSize.setStatus('current')
ibDHCPDDNSStats = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5))
ibDHCPDDNSAvgLatency5 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency5.setStatus('current')
ibDHCPDDNSAvgLatency15 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency15.setStatus('current')
ibDHCPDDNSAvgLatency60 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency60.setStatus('current')
ibDHCPDDNSAvgLatency1440 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency1440.setStatus('current')
ibDHCPDDNSTimeoutCount5 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount5.setStatus('current')
ibDHCPDDNSTimeoutCount15 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount15.setStatus('current')
ibDHCPDDNSTimeoutCount60 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount60.setStatus('current')
ibDHCPDDNSTimeoutCount1440 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount1440.setStatus('current')
mibBuilder.exportSymbols("IB-DHCPONE-MIB", ibDhcpDeferredQueueSize=ibDhcpDeferredQueueSize, ibDHCPDDNSAvgLatency60=ibDHCPDDNSAvgLatency60, ibDhcpTotalNoOfInforms=ibDhcpTotalNoOfInforms, ibDHCPSubnetPercentUsed=ibDHCPSubnetPercentUsed, ibDHCPDDNSTimeoutCount5=ibDHCPDDNSTimeoutCount5, ibDhcpTotalNoOfReleases=ibDhcpTotalNoOfReleases, ibDHCPDDNSTimeoutCount60=ibDHCPDDNSTimeoutCount60, ibDHCPDDNSAvgLatency5=ibDHCPDDNSAvgLatency5, ibDHCPSubnetEntry=ibDHCPSubnetEntry, ibDHCPSubnetNetworkAddress=ibDHCPSubnetNetworkAddress, ibDHCPDDNSAvgLatency15=ibDHCPDDNSAvgLatency15, ibDHCPDDNSAvgLatency1440=ibDHCPDDNSAvgLatency1440, ibDhcpTotalNoOfRequests=ibDhcpTotalNoOfRequests, ibDHCPDDNSTimeoutCount1440=ibDHCPDDNSTimeoutCount1440, ibDHCPDDNSTimeoutCount15=ibDHCPDDNSTimeoutCount15, ibDHCPSubnetTable=ibDHCPSubnetTable, ibDhcpTotalNoOfNacks=ibDhcpTotalNoOfNacks, ibDhcpTotalNoOfDeclines=ibDhcpTotalNoOfDeclines, ibDHCPDDNSStats=ibDHCPDDNSStats, ibDhcpTotalNoOfOffers=ibDhcpTotalNoOfOffers, ibDHCPSubnetNetworkMask=ibDHCPSubnetNetworkMask, ibDhcpTotalNoOfDiscovers=ibDhcpTotalNoOfDiscovers, ibDhcpTotalNoOfOthers=ibDhcpTotalNoOfOthers, ibDHCPStatistics=ibDHCPStatistics, ibDhcpTotalNoOfAcks=ibDhcpTotalNoOfAcks, ibDhcpModule=ibDhcpModule, PYSNMP_MODULE_ID=ibDhcpModule)
