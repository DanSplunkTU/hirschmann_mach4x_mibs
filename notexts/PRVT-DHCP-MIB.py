#
# PySNMP MIB module PRVT-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-DHCP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:22 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Integer32, Counter32, TimeTicks, ObjectIdentity, Gauge32, ModuleIdentity, Counter64, IpAddress, MibIdentifier, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Integer32", "Counter32", "TimeTicks", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Counter64", "IpAddress", "MibIdentifier", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
RowStatus, TextualConvention, DisplayString, MacAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString", "MacAddress", "TruthValue")
prvtDHCPMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 105))
prvtDHCPMib.setRevisions(('2005-02-16 00:00', '2003-05-06 00:00', '2002-05-30 00:00',))
if mibBuilder.loadTexts: prvtDHCPMib.setLastUpdated('200502160000Z')
if mibBuilder.loadTexts: prvtDHCPMib.setOrganization('BATM Advanced Communication')
prvtDHCPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1))
prvtDHCPNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 2))
dhcpPackets = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1))
dhcpRanges = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2))
dhcpSubnets = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3))
dhcpHosts = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4))
dhcpOptions = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5))
dhcpPorts = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6))
dhcpVlans = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7))
dhcpMiscSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8))
dhcpRRSettings = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9))
dhcpStaticHosts = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1))
dhcpDynamicHosts = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2))
dhcpStatusTotalNoOfDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfDiscovers.setStatus('current')
dhcpStatusTotalNoOfRequests = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfRequests.setStatus('current')
dhcpStatusTotalNoOfReleases = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfReleases.setStatus('current')
dhcpStatusTotalNoOfOffers = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfOffers.setStatus('current')
dhcpStatusTotalNoOfAcks = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfAcks.setStatus('current')
dhcpStatusTotalNoOfNacks = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfNacks.setStatus('current')
dhcpStatusTotalNoOfDeclines = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfDeclines.setStatus('current')
dhcpRangeTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1), )
if mibBuilder.loadTexts: dhcpRangeTable.setStatus('current')
dhcpRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpRangeStartIp"))
if mibBuilder.loadTexts: dhcpRangeEntry.setStatus('current')
dhcpRangeStartIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeStartIp.setStatus('current')
dhcpRangeStopIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeStopIp.setStatus('current')
dhcpRangeNoAddInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeNoAddInUse.setStatus('current')
dhcpRangeNoAddFree = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeNoAddFree.setStatus('current')
dhcpRangeCircuitID = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeCircuitID.setStatus('current')
dhcpRangeCircuitIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("string", 1), ("hex", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeCircuitIDType.setStatus('current')
dhcpRangeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeRangeName.setStatus('current')
dhcpRangeSubnetIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeSubnetIp.setStatus('current')
dhcpRangeSubnetName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeSubnetName.setStatus('current')
dhcpRangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeRowStatus.setStatus('current')
dhcpSubnetTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1), )
if mibBuilder.loadTexts: dhcpSubnetTable.setStatus('current')
dhcpSubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpSubnetIp"))
if mibBuilder.loadTexts: dhcpSubnetEntry.setStatus('current')
dhcpSubnetIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpSubnetIp.setStatus('current')
dhcpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpSubnetMask.setStatus('current')
dhcpSubnetName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpSubnetName.setStatus('current')
dhcpSubnetNoAddInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetNoAddInUse.setStatus('current')
dhcpSubnetNoAddFree = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetNoAddFree.setStatus('current')
dhcpSubnetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpSubnetRowStatus.setStatus('current')
dhcpStaticHostsTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1), )
if mibBuilder.loadTexts: dhcpStaticHostsTable.setStatus('current')
dhcpStaticHostsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpStaticHostIPAddress"))
if mibBuilder.loadTexts: dhcpStaticHostsEntry.setStatus('current')
dhcpStaticHostIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostIPAddress.setStatus('current')
dhcpStaticHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostName.setStatus('current')
dhcpStaticHostConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStaticHostConnected.setStatus('current')
dhcpStaticHostMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostMACAddr.setStatus('current')
dhcpStaticHostFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostFilename.setStatus('current')
dhcpStaticHostBootpIP = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostBootpIP.setStatus('current')
dhcpStaticHostServer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostServer.setStatus('current')
dhcpStatisHostSnoofPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatisHostSnoofPort.setStatus('current')
dhcpStaticHostRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostRowStatus.setStatus('current')
dhcpLeaseStateTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1), )
if mibBuilder.loadTexts: dhcpLeaseStateTable.setStatus('current')
dhcpLeaseStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpLeaseIp"))
if mibBuilder.loadTexts: dhcpLeaseStateEntry.setStatus('current')
dhcpLeaseIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseIp.setStatus('current')
dhcpLeaseName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseName.setStatus('current')
dhcpLeaseETime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseETime.setStatus('current')
dhcpLeaseMac = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseMac.setStatus('current')
dhcpLeaseSnoofPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseSnoofPort.setStatus('current')
dhcpOptionsTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1), )
if mibBuilder.loadTexts: dhcpOptionsTable.setStatus('current')
dhcpOptionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpOptionsSubnetIp"))
if mibBuilder.loadTexts: dhcpOptionsEntry.setStatus('current')
dhcpOptionsSubnetIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpOptionsSubnetIp.setStatus('current')
dhcpOptionsMaxLTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 2), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsMaxLTime.setStatus('current')
dhcpOptionsDfltLTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 3), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDfltLTime.setStatus('current')
dhcpOptionsRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsRouter.setStatus('current')
dhcpOptionsBrcstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsBrcstAddr.setStatus('current')
dhcpOptionsSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsSubnetMask.setStatus('current')
dhcpOptionsDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDomainName.setStatus('current')
dhcpOptionsMeritDump = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsMeritDump.setStatus('current')
dhcpOptionsRootPath = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 9), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsRootPath.setStatus('current')
dhcpOptionsBootStSrv = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsBootStSrv.setStatus('current')
dhcpOptionsBootFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 11), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsBootFileName.setStatus('current')
dhcpOptionsDNSServer1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 12), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDNSServer1.setStatus('current')
dhcpOptionsDNSServer2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 13), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDNSServer2.setStatus('current')
dhcpOptionsDNSServer3 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 14), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDNSServer3.setStatus('current')
dhcpOptionsDNSServer4 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 15), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDNSServer4.setStatus('current')
dhcpOptionsDNSServer5 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 16), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDNSServer5.setStatus('current')
dhcpOptionsLogServer1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 17), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsLogServer1.setStatus('current')
dhcpOptionsLogServer2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsLogServer2.setStatus('current')
dhcpOptionsLogServer3 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 19), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsLogServer3.setStatus('current')
dhcpOptionsLogServer4 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 20), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsLogServer4.setStatus('current')
dhcpOptionsLogServer5 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 21), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsLogServer5.setStatus('current')
dhcpOptionsWinsServer1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 22), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsWinsServer1.setStatus('current')
dhcpOptionsWinsServer2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 23), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsWinsServer2.setStatus('current')
dhcpOptionsWinsServer3 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 24), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsWinsServer3.setStatus('current')
dhcpOptionsWinsServer4 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 25), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsWinsServer4.setStatus('current')
dhcpOptionsWinsServer5 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 26), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsWinsServer5.setStatus('current')
dhcpDBExpire = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpDBExpire.setStatus('current')
dhcpTFTPServer = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpTFTPServer.setStatus('current')
dhcpFTPServer = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpFTPServer.setStatus('current')
dhcpFTPServerUser = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpFTPServerUser.setStatus('current')
dhcpFTPServerPass = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpFTPServerPass.setStatus('current')
dhcpRemoteDBDelay = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpRemoteDBDelay.setStatus('current')
dhcpRemoteDBFilename = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpRemoteDBFilename.setStatus('current')
dhcpUnknownCircuitIDPolicy = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpUnknownCircuitIDPolicy.setStatus('current')
dhcpEnableServer = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpEnableServer.setStatus('current')
dhcpPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1), )
if mibBuilder.loadTexts: dhcpPortTable.setStatus('current')
dhcpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpPort"))
if mibBuilder.loadTexts: dhcpPortEntry.setStatus('current')
dhcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPort.setStatus('current')
dhcpMaxPortIP = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 2), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpMaxPortIP.setStatus('current')
dhcpPortSnoof = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpPortSnoof.setStatus('current')
dhcpPortServiceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpPortServiceEnable.setStatus('current')
dhcpVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1), )
if mibBuilder.loadTexts: dhcpVlanTable.setStatus('current')
dhcpVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpVlanID"))
if mibBuilder.loadTexts: dhcpVlanEntry.setStatus('current')
dhcpVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpVlanID.setStatus('current')
dhcpVlanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpVlanEnable.setStatus('current')
dhcpRRTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1), )
if mibBuilder.loadTexts: dhcpRRTable.setStatus('current')
dhcpRREntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpRRif"))
if mibBuilder.loadTexts: dhcpRREntry.setStatus('current')
dhcpRRif = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRRif.setStatus('current')
dhcpRREnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRREnable.setStatus('current')
mibBuilder.exportSymbols("PRVT-DHCP-MIB", dhcpOptionsDfltLTime=dhcpOptionsDfltLTime, dhcpOptionsWinsServer5=dhcpOptionsWinsServer5, dhcpOptionsSubnetMask=dhcpOptionsSubnetMask, dhcpRRTable=dhcpRRTable, dhcpSubnetMask=dhcpSubnetMask, dhcpStatusTotalNoOfOffers=dhcpStatusTotalNoOfOffers, dhcpRREntry=dhcpRREntry, dhcpOptionsDomainName=dhcpOptionsDomainName, dhcpStaticHosts=dhcpStaticHosts, dhcpLeaseETime=dhcpLeaseETime, dhcpRangeStartIp=dhcpRangeStartIp, dhcpOptionsLogServer1=dhcpOptionsLogServer1, dhcpTFTPServer=dhcpTFTPServer, dhcpPortServiceEnable=dhcpPortServiceEnable, dhcpOptionsRouter=dhcpOptionsRouter, dhcpStatusTotalNoOfNacks=dhcpStatusTotalNoOfNacks, dhcpRREnable=dhcpRREnable, dhcpLeaseStateTable=dhcpLeaseStateTable, dhcpRRSettings=dhcpRRSettings, dhcpStaticHostsTable=dhcpStaticHostsTable, dhcpDBExpire=dhcpDBExpire, dhcpRangeEntry=dhcpRangeEntry, dhcpPortSnoof=dhcpPortSnoof, dhcpOptionsTable=dhcpOptionsTable, dhcpOptionsMaxLTime=dhcpOptionsMaxLTime, prvtDHCPMib=prvtDHCPMib, dhcpOptionsLogServer5=dhcpOptionsLogServer5, dhcpPorts=dhcpPorts, dhcpRangeStopIp=dhcpRangeStopIp, dhcpSubnetIp=dhcpSubnetIp, dhcpStatusTotalNoOfAcks=dhcpStatusTotalNoOfAcks, dhcpRangeSubnetIp=dhcpRangeSubnetIp, dhcpPackets=dhcpPackets, dhcpStatusTotalNoOfDeclines=dhcpStatusTotalNoOfDeclines, dhcpRangeSubnetName=dhcpRangeSubnetName, dhcpPortTable=dhcpPortTable, dhcpRRif=dhcpRRif, dhcpStatusTotalNoOfDiscovers=dhcpStatusTotalNoOfDiscovers, dhcpOptionsWinsServer3=dhcpOptionsWinsServer3, dhcpOptionsBootStSrv=dhcpOptionsBootStSrv, dhcpVlanEntry=dhcpVlanEntry, dhcpOptionsBootFileName=dhcpOptionsBootFileName, dhcpOptionsLogServer2=dhcpOptionsLogServer2, dhcpOptionsDNSServer2=dhcpOptionsDNSServer2, dhcpVlanID=dhcpVlanID, dhcpPortEntry=dhcpPortEntry, dhcpVlanEnable=dhcpVlanEnable, PYSNMP_MODULE_ID=prvtDHCPMib, dhcpSubnetRowStatus=dhcpSubnetRowStatus, dhcpOptionsEntry=dhcpOptionsEntry, dhcpFTPServer=dhcpFTPServer, dhcpOptionsWinsServer2=dhcpOptionsWinsServer2, dhcpOptions=dhcpOptions, dhcpOptionsDNSServer3=dhcpOptionsDNSServer3, dhcpOptionsDNSServer5=dhcpOptionsDNSServer5, prvtDHCPNotifications=prvtDHCPNotifications, dhcpRangeRowStatus=dhcpRangeRowStatus, dhcpRangeTable=dhcpRangeTable, dhcpUnknownCircuitIDPolicy=dhcpUnknownCircuitIDPolicy, dhcpDynamicHosts=dhcpDynamicHosts, dhcpStaticHostMACAddr=dhcpStaticHostMACAddr, dhcpLeaseStateEntry=dhcpLeaseStateEntry, dhcpRangeCircuitIDType=dhcpRangeCircuitIDType, dhcpOptionsWinsServer4=dhcpOptionsWinsServer4, dhcpSubnetNoAddInUse=dhcpSubnetNoAddInUse, dhcpOptionsLogServer4=dhcpOptionsLogServer4, dhcpLeaseName=dhcpLeaseName, dhcpVlans=dhcpVlans, dhcpStaticHostServer=dhcpStaticHostServer, dhcpRangeNoAddFree=dhcpRangeNoAddFree, dhcpHosts=dhcpHosts, dhcpStaticHostsEntry=dhcpStaticHostsEntry, dhcpMiscSettings=dhcpMiscSettings, dhcpSubnetTable=dhcpSubnetTable, dhcpOptionsSubnetIp=dhcpOptionsSubnetIp, dhcpOptionsRootPath=dhcpOptionsRootPath, dhcpEnableServer=dhcpEnableServer, dhcpRemoteDBFilename=dhcpRemoteDBFilename, dhcpRangeRangeName=dhcpRangeRangeName, dhcpStaticHostName=dhcpStaticHostName, dhcpSubnetNoAddFree=dhcpSubnetNoAddFree, dhcpStaticHostBootpIP=dhcpStaticHostBootpIP, dhcpStatisHostSnoofPort=dhcpStatisHostSnoofPort, dhcpStaticHostRowStatus=dhcpStaticHostRowStatus, dhcpOptionsDNSServer4=dhcpOptionsDNSServer4, dhcpFTPServerUser=dhcpFTPServerUser, dhcpOptionsWinsServer1=dhcpOptionsWinsServer1, dhcpRanges=dhcpRanges, dhcpSubnetEntry=dhcpSubnetEntry, dhcpRangeNoAddInUse=dhcpRangeNoAddInUse, dhcpFTPServerPass=dhcpFTPServerPass, dhcpRangeCircuitID=dhcpRangeCircuitID, dhcpStaticHostFilename=dhcpStaticHostFilename, dhcpOptionsLogServer3=dhcpOptionsLogServer3, prvtDHCPObjects=prvtDHCPObjects, dhcpVlanTable=dhcpVlanTable, dhcpOptionsBrcstAddr=dhcpOptionsBrcstAddr, dhcpOptionsMeritDump=dhcpOptionsMeritDump, dhcpStaticHostIPAddress=dhcpStaticHostIPAddress, dhcpStatusTotalNoOfRequests=dhcpStatusTotalNoOfRequests, dhcpSubnets=dhcpSubnets, dhcpLeaseIp=dhcpLeaseIp, dhcpLeaseSnoofPort=dhcpLeaseSnoofPort, dhcpRemoteDBDelay=dhcpRemoteDBDelay, dhcpStaticHostConnected=dhcpStaticHostConnected, dhcpOptionsDNSServer1=dhcpOptionsDNSServer1, dhcpStatusTotalNoOfReleases=dhcpStatusTotalNoOfReleases, dhcpSubnetName=dhcpSubnetName, dhcpMaxPortIP=dhcpMaxPortIP, dhcpPort=dhcpPort, dhcpLeaseMac=dhcpLeaseMac)
