#
# PySNMP MIB module PRVT-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-DHCP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:26 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, iso, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, NotificationType, Counter32, Counter64, MibIdentifier, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "NotificationType", "Counter32", "Counter64", "MibIdentifier", "IpAddress", "Bits")
TruthValue, MacAddress, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "TextualConvention", "RowStatus")
prvtDHCPMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 105))
prvtDHCPMib.setRevisions(('2005-02-16 00:00', '2003-05-06 00:00', '2002-05-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtDHCPMib.setRevisionsDescriptions(('Fixed spelling errors and changed the contact info.', 'Move to SMI-V2.', 'Initial version. This revision enables monitoring\nof the DHCP server status only.',))
if mibBuilder.loadTexts: prvtDHCPMib.setLastUpdated('200502160000Z')
if mibBuilder.loadTexts: prvtDHCPMib.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtDHCPMib.setContactInfo('BATM/Telco Systems Support team\nEmail:\nFor North America: techsupport@telco.com\nFor North Europe: support@batm.de, info@batm.de\nFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtDHCPMib.setDescription('DHCP')
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
if mibBuilder.loadTexts: dhcpStatusTotalNoOfDiscovers.setDescription('This variable indicates the number of\ndiscovery messages received')
dhcpStatusTotalNoOfRequests = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfRequests.setStatus('current')
if mibBuilder.loadTexts: dhcpStatusTotalNoOfRequests.setDescription('This variable indicates the number of\nrequests received')
dhcpStatusTotalNoOfReleases = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfReleases.setStatus('current')
if mibBuilder.loadTexts: dhcpStatusTotalNoOfReleases.setDescription('This variable indicates the number of\nreleases received')
dhcpStatusTotalNoOfOffers = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfOffers.setStatus('current')
if mibBuilder.loadTexts: dhcpStatusTotalNoOfOffers.setDescription('This variable indicates the number of\noffers sent')
dhcpStatusTotalNoOfAcks = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfAcks.setStatus('current')
if mibBuilder.loadTexts: dhcpStatusTotalNoOfAcks.setDescription('This variable indicates the number of\nACKs received')
dhcpStatusTotalNoOfNacks = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfNacks.setStatus('current')
if mibBuilder.loadTexts: dhcpStatusTotalNoOfNacks.setDescription('This variable indicates the number of\nNACKs received')
dhcpStatusTotalNoOfDeclines = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatusTotalNoOfDeclines.setStatus('current')
if mibBuilder.loadTexts: dhcpStatusTotalNoOfDeclines.setDescription('This variable indicates the number of\ndeclines')
dhcpRangeTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1), )
if mibBuilder.loadTexts: dhcpRangeTable.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeTable.setDescription('A list of ranges maintained by the server')
dhcpRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpRangeStartIp"))
if mibBuilder.loadTexts: dhcpRangeEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeEntry.setDescription('This is the row corresponding to a range')
dhcpRangeStartIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeStartIp.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeStartIp.setDescription('This is the range start address ')
dhcpRangeStopIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeStopIp.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeStopIp.setDescription('This is the range stop address ')
dhcpRangeNoAddInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeNoAddInUse.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeNoAddInUse.setDescription('This is the number of addresses in use')
dhcpRangeNoAddFree = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeNoAddFree.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeNoAddFree.setDescription('This is the number of free addresses')
dhcpRangeCircuitID = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeCircuitID.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeCircuitID.setDescription('This is circuit-ID of that range ')
dhcpRangeCircuitIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("string", 1), ("hex", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeCircuitIDType.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeCircuitIDType.setDescription('This is circuit-ID type of that range ')
dhcpRangeRangeName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeRangeName.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeRangeName.setDescription('This is the range name ')
dhcpRangeSubnetIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeSubnetIp.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeSubnetIp.setDescription('This is the range start address ')
dhcpRangeSubnetName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRangeSubnetName.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeSubnetName.setDescription('Subnet name, related to the range')
dhcpRangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 2, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRangeRowStatus.setStatus('current')
if mibBuilder.loadTexts: dhcpRangeRowStatus.setDescription('Indicates the status of the row. Setting of this field to active enables range\ncreation')
dhcpSubnetTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1), )
if mibBuilder.loadTexts: dhcpSubnetTable.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetTable.setDescription('A list of subnets maintained by the server')
dhcpSubnetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpSubnetIp"))
if mibBuilder.loadTexts: dhcpSubnetEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetEntry.setDescription('This is the row corresponding to a single subnet')
dhcpSubnetIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpSubnetIp.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetIp.setDescription('This is the subnet IP address ')
dhcpSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpSubnetMask.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetMask.setDescription('This is the subnet netmask ')
dhcpSubnetName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpSubnetName.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetName.setDescription('This is the subnet name')
dhcpSubnetNoAddInUse = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetNoAddInUse.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetNoAddInUse.setDescription('This is the number of addresses in use')
dhcpSubnetNoAddFree = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpSubnetNoAddFree.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetNoAddFree.setDescription('This is the number of addresses that are free ')
dhcpSubnetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 3, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpSubnetRowStatus.setStatus('current')
if mibBuilder.loadTexts: dhcpSubnetRowStatus.setDescription('Indicates the status of the row. Setting of this field to active enables\nsubnet creation')
dhcpStaticHostsTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1), )
if mibBuilder.loadTexts: dhcpStaticHostsTable.setStatus('current')
if mibBuilder.loadTexts: dhcpStaticHostsTable.setDescription('A list of hosts with fixed IP addresses maintained by the server')
dhcpStaticHostsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpStaticHostIPAddress"))
if mibBuilder.loadTexts: dhcpStaticHostsEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpStaticHostsEntry.setDescription('This is the row, corresponding to a subnet')
dhcpStaticHostIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 1), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostIPAddress.setStatus('current')
if mibBuilder.loadTexts: dhcpStaticHostIPAddress.setDescription('This is the fixed IP address, reserved for this host')
dhcpStaticHostName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostName.setStatus('current')
if mibBuilder.loadTexts: dhcpStaticHostName.setDescription('This is the host name')
dhcpStaticHostConnected = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStaticHostConnected.setStatus('current')
if mibBuilder.loadTexts: dhcpStaticHostConnected.setDescription('This is the currently connected status of the host.\nThe value TRUE means that this host has requested this IP address')
dhcpStaticHostMACAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 4), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostMACAddr.setStatus('current')
if mibBuilder.loadTexts: dhcpStaticHostMACAddr.setDescription('This is the specified host MAC address ')
dhcpStaticHostFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 5), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostFilename.setStatus('current')
if mibBuilder.loadTexts: dhcpStaticHostFilename.setDescription('This is the host file name')
dhcpStaticHostBootpIP = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostBootpIP.setStatus('current')
if mibBuilder.loadTexts: dhcpStaticHostBootpIP.setDescription('This is the bootstrap server IP address for the current host')
dhcpStaticHostServer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostServer.setStatus('current')
if mibBuilder.loadTexts: dhcpStaticHostServer.setDescription('This is boot server name')
dhcpStatisHostSnoofPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpStatisHostSnoofPort.setStatus('current')
if mibBuilder.loadTexts: dhcpStatisHostSnoofPort.setDescription('This is the coresponding Snoof port if defined')
dhcpStaticHostRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 1, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpStaticHostRowStatus.setStatus('current')
if mibBuilder.loadTexts: dhcpStaticHostRowStatus.setDescription('Indicates the status of the row. Setting this field to active\nenables static host creation')
dhcpLeaseStateTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1), )
if mibBuilder.loadTexts: dhcpLeaseStateTable.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseStateTable.setDescription('A list of lease states')
dhcpLeaseStateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpLeaseIp"))
if mibBuilder.loadTexts: dhcpLeaseStateEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseStateEntry.setDescription('This is the row corresponding to a single lease')
dhcpLeaseIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseIp.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseIp.setDescription('This is the lease IP address ')
dhcpLeaseName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseName.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseName.setDescription('This is the lease name')
dhcpLeaseETime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseETime.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseETime.setDescription('Lease expiration time')
dhcpLeaseMac = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseMac.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseMac.setDescription('This is the lease MAC address ')
dhcpLeaseSnoofPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 4, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpLeaseSnoofPort.setStatus('current')
if mibBuilder.loadTexts: dhcpLeaseSnoofPort.setDescription('This is the corresponding Snoof port, if defined')
dhcpOptionsTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1), )
if mibBuilder.loadTexts: dhcpOptionsTable.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsTable.setDescription('A list of options set on the server')
dhcpOptionsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpOptionsSubnetIp"))
if mibBuilder.loadTexts: dhcpOptionsEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsEntry.setDescription('This is the row corresponding to a set of options')
dhcpOptionsSubnetIp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpOptionsSubnetIp.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsSubnetIp.setDescription('This is the subnet IP address ')
dhcpOptionsMaxLTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 2), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsMaxLTime.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsMaxLTime.setDescription('This is the max-lease-time option ')
dhcpOptionsDfltLTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 3), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDfltLTime.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsDfltLTime.setDescription('This is the default-lease-time option ')
dhcpOptionsRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsRouter.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsRouter.setDescription('This is the router option ')
dhcpOptionsBrcstAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsBrcstAddr.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsBrcstAddr.setDescription('This is the network broadcast address option ')
dhcpOptionsSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 6), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsSubnetMask.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsSubnetMask.setDescription('This is the network subnet mask option ')
dhcpOptionsDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 7), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDomainName.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsDomainName.setDescription('This is the domain-name option ')
dhcpOptionsMeritDump = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsMeritDump.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsMeritDump.setDescription('This is the merit-dump option ')
dhcpOptionsRootPath = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 9), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsRootPath.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsRootPath.setDescription('This is the root-path option ')
dhcpOptionsBootStSrv = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 10), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsBootStSrv.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsBootStSrv.setDescription('This is the bootstrap server IP address ')
dhcpOptionsBootFileName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 11), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsBootFileName.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsBootFileName.setDescription('This is the bootstrap filename option ')
dhcpOptionsDNSServer1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 12), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDNSServer1.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsDNSServer1.setDescription('This is the first DNS server option ')
dhcpOptionsDNSServer2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 13), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDNSServer2.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsDNSServer2.setDescription('This is the second DNS server option ')
dhcpOptionsDNSServer3 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 14), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDNSServer3.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsDNSServer3.setDescription('This is the third DNS server option ')
dhcpOptionsDNSServer4 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 15), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDNSServer4.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsDNSServer4.setDescription('This is the fourth DNS server option ')
dhcpOptionsDNSServer5 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 16), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsDNSServer5.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsDNSServer5.setDescription('This is the fifth DNS server option ')
dhcpOptionsLogServer1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 17), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsLogServer1.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsLogServer1.setDescription('This is the first log-server option ')
dhcpOptionsLogServer2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 18), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsLogServer2.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsLogServer2.setDescription('This is the second log-server option ')
dhcpOptionsLogServer3 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 19), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsLogServer3.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsLogServer3.setDescription('This is the third log-server option ')
dhcpOptionsLogServer4 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 20), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsLogServer4.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsLogServer4.setDescription('This is the fourth log-server option ')
dhcpOptionsLogServer5 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 21), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsLogServer5.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsLogServer5.setDescription('This is the fifth log-server option ')
dhcpOptionsWinsServer1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 22), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsWinsServer1.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsWinsServer1.setDescription('This is the first WINS server option ')
dhcpOptionsWinsServer2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 23), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsWinsServer2.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsWinsServer2.setDescription('This is the second WINS server option ')
dhcpOptionsWinsServer3 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 24), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsWinsServer3.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsWinsServer3.setDescription('This is the third WINS server option ')
dhcpOptionsWinsServer4 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 25), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsWinsServer4.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsWinsServer4.setDescription('This is the fourth WINS server option ')
dhcpOptionsWinsServer5 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 5, 1, 1, 26), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpOptionsWinsServer5.setStatus('current')
if mibBuilder.loadTexts: dhcpOptionsWinsServer5.setDescription('This is the fifth WINS server option ')
dhcpDBExpire = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 1), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpDBExpire.setStatus('current')
if mibBuilder.loadTexts: dhcpDBExpire.setDescription('Expire time for internal DHCP database ')
dhcpTFTPServer = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpTFTPServer.setStatus('current')
if mibBuilder.loadTexts: dhcpTFTPServer.setDescription('IP address of TFTP server to store the DHCP database remotely ')
dhcpFTPServer = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpFTPServer.setStatus('current')
if mibBuilder.loadTexts: dhcpFTPServer.setDescription('IP address of FTP server to store the DHCP database remotely ')
dhcpFTPServerUser = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpFTPServerUser.setStatus('current')
if mibBuilder.loadTexts: dhcpFTPServerUser.setDescription('Username for remote FTP server ')
dhcpFTPServerPass = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpFTPServerPass.setStatus('current')
if mibBuilder.loadTexts: dhcpFTPServerPass.setDescription('Password for remote FTP server ')
dhcpRemoteDBDelay = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 6), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpRemoteDBDelay.setStatus('current')
if mibBuilder.loadTexts: dhcpRemoteDBDelay.setDescription('Delay between consecutive database transfers to remote server ')
dhcpRemoteDBFilename = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 7), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpRemoteDBFilename.setStatus('current')
if mibBuilder.loadTexts: dhcpRemoteDBFilename.setDescription('IP Leases remote database filename')
dhcpUnknownCircuitIDPolicy = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("permit", 1), ("deny", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpUnknownCircuitIDPolicy.setStatus('current')
if mibBuilder.loadTexts: dhcpUnknownCircuitIDPolicy.setDescription('Unknown circuit-ID policy ')
dhcpEnableServer = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 8, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dhcpEnableServer.setStatus('current')
if mibBuilder.loadTexts: dhcpEnableServer.setDescription('Enable/disable DHCP server operation ')
dhcpPortTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1), )
if mibBuilder.loadTexts: dhcpPortTable.setStatus('current')
if mibBuilder.loadTexts: dhcpPortTable.setDescription('A list of DHCP settings related to ports ')
dhcpPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpPort"))
if mibBuilder.loadTexts: dhcpPortEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpPortEntry.setDescription('These are the physical port settings.')
dhcpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpPort.setStatus('current')
if mibBuilder.loadTexts: dhcpPort.setDescription('This is the port number.')
dhcpMaxPortIP = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 2), Counter32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpMaxPortIP.setStatus('current')
if mibBuilder.loadTexts: dhcpMaxPortIP.setDescription('This is the maximum IP addresses to be given via the current port.')
dhcpPortSnoof = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpPortSnoof.setStatus('current')
if mibBuilder.loadTexts: dhcpPortSnoof.setDescription('This is a check for enabling/disabling Snoof on the current port.')
dhcpPortServiceEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 6, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpPortServiceEnable.setStatus('current')
if mibBuilder.loadTexts: dhcpPortServiceEnable.setDescription('This is a check for enabling/disabling DHCP service on the current port.')
dhcpVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1), )
if mibBuilder.loadTexts: dhcpVlanTable.setStatus('current')
if mibBuilder.loadTexts: dhcpVlanTable.setDescription('A list of DHCP VLAN settings.')
dhcpVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpVlanID"))
if mibBuilder.loadTexts: dhcpVlanEntry.setStatus('current')
if mibBuilder.loadTexts: dhcpVlanEntry.setDescription('This is the row corresponding to a single VLAN setting.')
dhcpVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpVlanID.setStatus('current')
if mibBuilder.loadTexts: dhcpVlanID.setDescription('This is the VLAN ID.')
dhcpVlanEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 7, 1, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpVlanEnable.setStatus('current')
if mibBuilder.loadTexts: dhcpVlanEnable.setDescription('This is enable/disable DHCP service status per VLAN.')
dhcpRRTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1), )
if mibBuilder.loadTexts: dhcpRRTable.setStatus('current')
if mibBuilder.loadTexts: dhcpRRTable.setDescription('A list of DHCP round-robin settings.')
dhcpRREntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1, 1), ).setIndexNames((0, "PRVT-DHCP-MIB", "dhcpRRif"))
if mibBuilder.loadTexts: dhcpRREntry.setStatus('current')
if mibBuilder.loadTexts: dhcpRREntry.setDescription('This is the row corresponding to single VLAN setting.')
dhcpRRif = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dhcpRRif.setStatus('current')
if mibBuilder.loadTexts: dhcpRRif.setDescription('This is the IP interface name.')
dhcpRREnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 105, 1, 9, 1, 1, 2), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dhcpRREnable.setStatus('current')
if mibBuilder.loadTexts: dhcpRREnable.setDescription('This is enable/disable DHCP round-robin feature per interface.')
mibBuilder.exportSymbols("PRVT-DHCP-MIB", dhcpStatusTotalNoOfNacks=dhcpStatusTotalNoOfNacks, dhcpOptionsWinsServer5=dhcpOptionsWinsServer5, dhcpOptionsDNSServer3=dhcpOptionsDNSServer3, dhcpStaticHostsTable=dhcpStaticHostsTable, dhcpPortSnoof=dhcpPortSnoof, prvtDHCPNotifications=prvtDHCPNotifications, dhcpOptionsDNSServer5=dhcpOptionsDNSServer5, dhcpOptionsDfltLTime=dhcpOptionsDfltLTime, dhcpUnknownCircuitIDPolicy=dhcpUnknownCircuitIDPolicy, dhcpOptionsDomainName=dhcpOptionsDomainName, dhcpStatusTotalNoOfOffers=dhcpStatusTotalNoOfOffers, dhcpFTPServerUser=dhcpFTPServerUser, dhcpOptionsEntry=dhcpOptionsEntry, dhcpRangeStopIp=dhcpRangeStopIp, dhcpRemoteDBFilename=dhcpRemoteDBFilename, dhcpStaticHostMACAddr=dhcpStaticHostMACAddr, dhcpRangeStartIp=dhcpRangeStartIp, dhcpOptionsWinsServer1=dhcpOptionsWinsServer1, dhcpPackets=dhcpPackets, dhcpOptionsDNSServer2=dhcpOptionsDNSServer2, dhcpPorts=dhcpPorts, dhcpLeaseIp=dhcpLeaseIp, dhcpVlanID=dhcpVlanID, dhcpRREnable=dhcpRREnable, dhcpSubnetIp=dhcpSubnetIp, dhcpPort=dhcpPort, prvtDHCPObjects=prvtDHCPObjects, dhcpLeaseStateEntry=dhcpLeaseStateEntry, dhcpMiscSettings=dhcpMiscSettings, dhcpPortServiceEnable=dhcpPortServiceEnable, dhcpOptionsSubnetMask=dhcpOptionsSubnetMask, dhcpStaticHostConnected=dhcpStaticHostConnected, dhcpOptionsLogServer3=dhcpOptionsLogServer3, dhcpSubnetMask=dhcpSubnetMask, dhcpDBExpire=dhcpDBExpire, dhcpStatusTotalNoOfRequests=dhcpStatusTotalNoOfRequests, dhcpEnableServer=dhcpEnableServer, dhcpVlanTable=dhcpVlanTable, dhcpPortEntry=dhcpPortEntry, dhcpLeaseETime=dhcpLeaseETime, dhcpStaticHostIPAddress=dhcpStaticHostIPAddress, dhcpSubnetEntry=dhcpSubnetEntry, dhcpLeaseStateTable=dhcpLeaseStateTable, dhcpRangeSubnetName=dhcpRangeSubnetName, dhcpRangeNoAddFree=dhcpRangeNoAddFree, dhcpOptionsMaxLTime=dhcpOptionsMaxLTime, dhcpOptionsLogServer4=dhcpOptionsLogServer4, dhcpStatusTotalNoOfReleases=dhcpStatusTotalNoOfReleases, dhcpRREntry=dhcpRREntry, dhcpStatusTotalNoOfDeclines=dhcpStatusTotalNoOfDeclines, dhcpOptionsBootStSrv=dhcpOptionsBootStSrv, dhcpTFTPServer=dhcpTFTPServer, dhcpOptionsLogServer2=dhcpOptionsLogServer2, dhcpStatisHostSnoofPort=dhcpStatisHostSnoofPort, dhcpRangeEntry=dhcpRangeEntry, dhcpStatusTotalNoOfAcks=dhcpStatusTotalNoOfAcks, dhcpLeaseMac=dhcpLeaseMac, prvtDHCPMib=prvtDHCPMib, dhcpOptionsWinsServer3=dhcpOptionsWinsServer3, dhcpRangeRangeName=dhcpRangeRangeName, dhcpOptionsDNSServer1=dhcpOptionsDNSServer1, dhcpOptionsWinsServer2=dhcpOptionsWinsServer2, dhcpStaticHostRowStatus=dhcpStaticHostRowStatus, dhcpStaticHostFilename=dhcpStaticHostFilename, dhcpOptionsLogServer5=dhcpOptionsLogServer5, dhcpMaxPortIP=dhcpMaxPortIP, dhcpSubnetName=dhcpSubnetName, dhcpOptionsMeritDump=dhcpOptionsMeritDump, dhcpLeaseSnoofPort=dhcpLeaseSnoofPort, dhcpOptionsWinsServer4=dhcpOptionsWinsServer4, dhcpOptionsLogServer1=dhcpOptionsLogServer1, dhcpOptionsSubnetIp=dhcpOptionsSubnetIp, dhcpDynamicHosts=dhcpDynamicHosts, dhcpStaticHostsEntry=dhcpStaticHostsEntry, dhcpSubnetNoAddFree=dhcpSubnetNoAddFree, dhcpVlanEntry=dhcpVlanEntry, dhcpStaticHosts=dhcpStaticHosts, dhcpPortTable=dhcpPortTable, dhcpStaticHostServer=dhcpStaticHostServer, dhcpLeaseName=dhcpLeaseName, dhcpOptionsRouter=dhcpOptionsRouter, dhcpVlans=dhcpVlans, dhcpSubnetRowStatus=dhcpSubnetRowStatus, PYSNMP_MODULE_ID=prvtDHCPMib, dhcpOptionsTable=dhcpOptionsTable, dhcpOptionsDNSServer4=dhcpOptionsDNSServer4, dhcpOptionsBrcstAddr=dhcpOptionsBrcstAddr, dhcpStaticHostName=dhcpStaticHostName, dhcpRangeCircuitIDType=dhcpRangeCircuitIDType, dhcpRRSettings=dhcpRRSettings, dhcpRangeTable=dhcpRangeTable, dhcpSubnetNoAddInUse=dhcpSubnetNoAddInUse, dhcpOptionsRootPath=dhcpOptionsRootPath, dhcpSubnets=dhcpSubnets, dhcpRangeSubnetIp=dhcpRangeSubnetIp, dhcpOptions=dhcpOptions, dhcpRangeCircuitID=dhcpRangeCircuitID, dhcpVlanEnable=dhcpVlanEnable, dhcpSubnetTable=dhcpSubnetTable, dhcpRangeNoAddInUse=dhcpRangeNoAddInUse, dhcpHosts=dhcpHosts, dhcpStaticHostBootpIP=dhcpStaticHostBootpIP, dhcpRRif=dhcpRRif, dhcpRanges=dhcpRanges, dhcpStatusTotalNoOfDiscovers=dhcpStatusTotalNoOfDiscovers, dhcpRangeRowStatus=dhcpRangeRowStatus, dhcpRRTable=dhcpRRTable, dhcpFTPServerPass=dhcpFTPServerPass, dhcpRemoteDBDelay=dhcpRemoteDBDelay, dhcpFTPServer=dhcpFTPServer, dhcpOptionsBootFileName=dhcpOptionsBootFileName)
