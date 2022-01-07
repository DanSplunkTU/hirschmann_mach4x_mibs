#
# PySNMP MIB module IB-DHCPONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DHCPONE-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:27:41 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ibDHCPOne, IbString, IbIpAddr = mibBuilder.importSymbols("IB-SMI-MIB", "ibDHCPOne", "IbString", "IbIpAddr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, enterprises, ModuleIdentity, Unsigned32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, Integer32, ObjectIdentity, MibIdentifier, IpAddress, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "enterprises", "ModuleIdentity", "Unsigned32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "Integer32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter64", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
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
mibBuilder.exportSymbols("IB-DHCPONE-MIB", ibDHCPSubnetNetworkMask=ibDHCPSubnetNetworkMask, ibDHCPSubnetEntry=ibDHCPSubnetEntry, ibDhcpTotalNoOfDiscovers=ibDhcpTotalNoOfDiscovers, ibDhcpTotalNoOfAcks=ibDhcpTotalNoOfAcks, ibDHCPDDNSAvgLatency1440=ibDHCPDDNSAvgLatency1440, ibDHCPDDNSAvgLatency60=ibDHCPDDNSAvgLatency60, ibDhcpModule=ibDhcpModule, ibDHCPSubnetPercentUsed=ibDHCPSubnetPercentUsed, ibDHCPDDNSAvgLatency5=ibDHCPDDNSAvgLatency5, ibDHCPDDNSAvgLatency15=ibDHCPDDNSAvgLatency15, ibDHCPDDNSStats=ibDHCPDDNSStats, ibDhcpTotalNoOfDeclines=ibDhcpTotalNoOfDeclines, ibDHCPDDNSTimeoutCount60=ibDHCPDDNSTimeoutCount60, ibDhcpTotalNoOfOffers=ibDhcpTotalNoOfOffers, ibDhcpTotalNoOfReleases=ibDhcpTotalNoOfReleases, ibDhcpTotalNoOfOthers=ibDhcpTotalNoOfOthers, ibDhcpTotalNoOfNacks=ibDhcpTotalNoOfNacks, ibDHCPDDNSTimeoutCount15=ibDHCPDDNSTimeoutCount15, ibDHCPSubnetNetworkAddress=ibDHCPSubnetNetworkAddress, ibDHCPSubnetTable=ibDHCPSubnetTable, PYSNMP_MODULE_ID=ibDhcpModule, ibDhcpTotalNoOfInforms=ibDhcpTotalNoOfInforms, ibDhcpDeferredQueueSize=ibDhcpDeferredQueueSize, ibDHCPDDNSTimeoutCount1440=ibDHCPDDNSTimeoutCount1440, ibDHCPDDNSTimeoutCount5=ibDHCPDDNSTimeoutCount5, ibDhcpTotalNoOfRequests=ibDhcpTotalNoOfRequests, ibDHCPStatistics=ibDHCPStatistics)
