#
# PySNMP MIB module IB-DHCPONE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/infoblox/IB-DHCPONE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:10:52 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
IbString, ibDHCPOne, IbIpAddr = mibBuilder.importSymbols("IB-SMI-MIB", "IbString", "ibDHCPOne", "IbIpAddr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, NotificationType, TimeTicks, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, iso, ModuleIdentity, Counter64, IpAddress, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "NotificationType", "TimeTicks", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "iso", "ModuleIdentity", "Counter64", "IpAddress", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ibDhcpModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1))
ibDhcpModule.setRevisions(('2010-03-23 00:00', '2008-02-14 00:00', '2005-01-10 00:00', '2004-05-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ibDhcpModule.setRevisionsDescriptions(('Fixed smilint errors', 'change ibDHCPSubnetPercentUsed syntax', 'Added copyright', 'Creation of the MIB file',))
if mibBuilder.loadTexts: ibDhcpModule.setLastUpdated('201003230000Z')
if mibBuilder.loadTexts: ibDhcpModule.setOrganization('Infoblox')
if mibBuilder.loadTexts: ibDhcpModule.setContactInfo('See IB-SMI-MIB for information.')
if mibBuilder.loadTexts: ibDhcpModule.setDescription('This file defines the Infoblox DHCP One MIB.')
ibDHCPSubnetTable = MibTable((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1), )
if mibBuilder.loadTexts: ibDHCPSubnetTable.setStatus('current')
if mibBuilder.loadTexts: ibDHCPSubnetTable.setDescription('A table of DHCP Subnet statistics.')
ibDHCPSubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1), ).setIndexNames((0, "IB-DHCPONE-MIB", "ibDHCPSubnetNetworkAddress"))
if mibBuilder.loadTexts: ibDHCPSubnetEntry.setStatus('current')
if mibBuilder.loadTexts: ibDHCPSubnetEntry.setDescription('A conceptual row of the ibDHCPSubnetEntry containing \n                  info about a particular network using DHCP.')
ibDHCPSubnetNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 1), IbIpAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPSubnetNetworkAddress.setStatus('current')
if mibBuilder.loadTexts: ibDHCPSubnetNetworkAddress.setDescription('DHCP Subnet in IpAddress format. A subnetwork may have many \n                  ranges for lease.')
ibDHCPSubnetNetworkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 2), IbIpAddr()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPSubnetNetworkMask.setStatus('current')
if mibBuilder.loadTexts: ibDHCPSubnetNetworkMask.setDescription('DHCP Subnet mask in IpAddress format.')
ibDHCPSubnetPercentUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPSubnetPercentUsed.setStatus('current')
if mibBuilder.loadTexts: ibDHCPSubnetPercentUsed.setDescription('Percentage of dynamic DHCP address for subnet leased out at this \n                  time. Fixed addresses are always counted as leased for this\n                  calcuation if the fixed addresses are within ranges of leases.')
ibDHCPStatistics = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3))
ibDhcpTotalNoOfDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfDiscovers.setStatus('current')
if mibBuilder.loadTexts: ibDhcpTotalNoOfDiscovers.setDescription('This variable indicates the number of\n\t\t discovery messages received')
ibDhcpTotalNoOfRequests = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfRequests.setStatus('current')
if mibBuilder.loadTexts: ibDhcpTotalNoOfRequests.setDescription('This variable indicates the number of\n\t\t requests received')
ibDhcpTotalNoOfReleases = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfReleases.setStatus('current')
if mibBuilder.loadTexts: ibDhcpTotalNoOfReleases.setDescription('This variable indicates the number of\n\t\t releases received')
ibDhcpTotalNoOfOffers = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfOffers.setStatus('current')
if mibBuilder.loadTexts: ibDhcpTotalNoOfOffers.setDescription('This variable indicates the number of\n\t\t offers sent')
ibDhcpTotalNoOfAcks = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfAcks.setStatus('current')
if mibBuilder.loadTexts: ibDhcpTotalNoOfAcks.setDescription('This variable indicates the number of\n\t\t acks sent')
ibDhcpTotalNoOfNacks = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfNacks.setStatus('current')
if mibBuilder.loadTexts: ibDhcpTotalNoOfNacks.setDescription('This variable indicates the number of\n\t\t nacks sent')
ibDhcpTotalNoOfDeclines = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfDeclines.setStatus('current')
if mibBuilder.loadTexts: ibDhcpTotalNoOfDeclines.setDescription('This variable indicates the number of\n\t\t declines received')
ibDhcpTotalNoOfInforms = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfInforms.setStatus('current')
if mibBuilder.loadTexts: ibDhcpTotalNoOfInforms.setDescription('This variable indicates the number of\n\t\t informs received')
ibDhcpTotalNoOfOthers = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 3, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpTotalNoOfOthers.setStatus('current')
if mibBuilder.loadTexts: ibDhcpTotalNoOfOthers.setDescription('This variable indicates the number of\n\t\t other messages received')
ibDhcpDeferredQueueSize = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDhcpDeferredQueueSize.setStatus('current')
if mibBuilder.loadTexts: ibDhcpDeferredQueueSize.setDescription('The size of deferred dynamic DNS update queue')
ibDHCPDDNSStats = MibIdentifier((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5))
ibDHCPDDNSAvgLatency5 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency5.setStatus('current')
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency5.setDescription('Average Latencies (in microseconds) for DHCPD\n                  dynamic DNS updates during the last 5 minutes')
ibDHCPDDNSAvgLatency15 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency15.setStatus('current')
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency15.setDescription('Average Latencies (in microseconds) for DHCPD\n                  dynamic DNS updates during the last 15 minutes')
ibDHCPDDNSAvgLatency60 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency60.setStatus('current')
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency60.setDescription('Average Latencies (in microseconds) for DHCPD\n                  dynamic DNS updates during the last 60 minutes')
ibDHCPDDNSAvgLatency1440 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency1440.setStatus('current')
if mibBuilder.loadTexts: ibDHCPDDNSAvgLatency1440.setDescription('Average Latencies (in microseconds) for DHCPD\n                  dynamic DNS updates during the last 1 day')
ibDHCPDDNSTimeoutCount5 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount5.setStatus('current')
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount5.setDescription('The number of timeout DHCPD dynamic DDNS\n                  updates during the last 5 minutes')
ibDHCPDDNSTimeoutCount15 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount15.setStatus('current')
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount15.setDescription('The number of timeout DHCPD dynamic DDNS\n                  updates during the last 15 minutes')
ibDHCPDDNSTimeoutCount60 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount60.setStatus('current')
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount60.setDescription('The number of timeout DHCPD dynamic DDNS\n                  updates during the last 60 minutes')
ibDHCPDDNSTimeoutCount1440 = MibScalar((1, 3, 6, 1, 4, 1, 7779, 3, 1, 1, 4, 1, 5, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount1440.setStatus('current')
if mibBuilder.loadTexts: ibDHCPDDNSTimeoutCount1440.setDescription('The number of timeout DHCPD dynamic DDNS\n                  updates during the last 1 day')
mibBuilder.exportSymbols("IB-DHCPONE-MIB", ibDhcpTotalNoOfAcks=ibDhcpTotalNoOfAcks, ibDHCPDDNSTimeoutCount1440=ibDHCPDDNSTimeoutCount1440, PYSNMP_MODULE_ID=ibDhcpModule, ibDhcpDeferredQueueSize=ibDhcpDeferredQueueSize, ibDhcpTotalNoOfDiscovers=ibDhcpTotalNoOfDiscovers, ibDHCPSubnetNetworkAddress=ibDHCPSubnetNetworkAddress, ibDhcpModule=ibDhcpModule, ibDHCPDDNSAvgLatency5=ibDHCPDDNSAvgLatency5, ibDHCPSubnetTable=ibDHCPSubnetTable, ibDhcpTotalNoOfDeclines=ibDhcpTotalNoOfDeclines, ibDhcpTotalNoOfOthers=ibDhcpTotalNoOfOthers, ibDHCPDDNSAvgLatency1440=ibDHCPDDNSAvgLatency1440, ibDHCPSubnetNetworkMask=ibDHCPSubnetNetworkMask, ibDhcpTotalNoOfNacks=ibDhcpTotalNoOfNacks, ibDhcpTotalNoOfRequests=ibDhcpTotalNoOfRequests, ibDhcpTotalNoOfOffers=ibDhcpTotalNoOfOffers, ibDHCPDDNSAvgLatency15=ibDHCPDDNSAvgLatency15, ibDhcpTotalNoOfReleases=ibDhcpTotalNoOfReleases, ibDhcpTotalNoOfInforms=ibDhcpTotalNoOfInforms, ibDHCPDDNSAvgLatency60=ibDHCPDDNSAvgLatency60, ibDHCPDDNSTimeoutCount5=ibDHCPDDNSTimeoutCount5, ibDHCPDDNSStats=ibDHCPDDNSStats, ibDHCPDDNSTimeoutCount60=ibDHCPDDNSTimeoutCount60, ibDHCPSubnetPercentUsed=ibDHCPSubnetPercentUsed, ibDHCPStatistics=ibDHCPStatistics, ibDHCPSubnetEntry=ibDHCPSubnetEntry, ibDHCPDDNSTimeoutCount15=ibDHCPDDNSTimeoutCount15)
