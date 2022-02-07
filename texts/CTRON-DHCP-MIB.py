#
# PySNMP MIB module CTRON-DHCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-DHCP-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:06 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
nwIpMibs, nwIpComponents, nwIpRouter, nwIpClientServices = mibBuilder.importSymbols("CTRON-IP-ROUTER-MIB", "nwIpMibs", "nwIpComponents", "nwIpRouter", "nwIpClientServices")
nwRtrProtoSuites, = mibBuilder.importSymbols("ROUTER-OIDS", "nwRtrProtoSuites")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter32, ObjectIdentity, IpAddress, Gauge32, MibIdentifier, TimeTicks, iso, Unsigned32, Integer32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier", "TimeTicks", "iso", "Unsigned32", "Integer32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits")
PhysAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TextualConvention")
ctDhcp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2))
ctDhcpServerStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1))
ctDhcpInterfaceConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2))
ctDhcpClientStatusTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3))
ctDhcpAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpAdminStatus.setDescription('This object is used to enable or disable the DHCP\n                        server function for the entire device.  This object \n                        must be set to enabled for the server to function on \n                        this device.')
ctDhcpOperStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpOperStatus.setDescription('Indicates the current operating status of the DHCP\n                        server function on this device.  The value of \n                        ctDhcpIfOperStatus for at least one interface must be \n                        set to enabled for this object to be enabled.')
ctDhcpDiscovers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpDiscovers.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpDiscovers.setDescription('This value is the number of discover messages \n                        received by the DHCP server since the last reset.')
ctDhcpOffers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOffers.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpOffers.setDescription('This value is the number of offer messages \n                        sent by the DHCP server since the last reset.')
ctDhcpRequests = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpRequests.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpRequests.setDescription('This value is the number of request messages \n                        received by the DHCP server since the last reset.')
ctDhcpDeclines = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpDeclines.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpDeclines.setDescription('This value is the number of decline messages \n                        received by the DHCP server since the last reset.')
ctDhcpReleases = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpReleases.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpReleases.setDescription('This value is the number of release messages \n                        received by the DHCP server since the last reset.')
ctDhcpAcks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpAcks.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpAcks.setDescription('This value is the number of ack messages \n                        sent by the DHCP server since the last reset.')
ctDhcpNaks = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpNaks.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpNaks.setDescription('This value is the number of nak messages \n                        sent by the DHCP server since the last reset.')
ctDhcpOtherServers = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpOtherServers.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpOtherServers.setDescription('This value is the number of messages \n                        received by the DHCP server since the last reset\n                        which were directed to other servers.')
ctDhcpProtocolErrors = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpProtocolErrors.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpProtocolErrors.setDescription('This value is the number of protocol errors detected \n                        by the DHCP server since the last reset.')
ctDhcpServerTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpServerTime.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpServerTime.setDescription('This value is the number of seconds that this DHCP \n                        server has been in operation since its non-volatile \n                        memory was last cleared.')
ctDhcpNoOfActiveClients = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpNoOfActiveClients.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpNoOfActiveClients.setDescription('This value is the number of clients who currently\n                        have network addresses assigned by this DHCP server.')
ctDhcpReclaimIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 1, 14), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpReclaimIP.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpReclaimIP.setDescription('This object is a method of reclaiming abandoned IP\n                        addresses.  The value reads as 0.0.0.0.  Writing to\n                        it with an IP address of a client on the active list\n                        will remove the entry from the list.  It is used to \n                        recover addresses with long leases from clients who\n                        have left the network without sending a release notice.')
ctDhcpServerIfTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1), )
if mibBuilder.loadTexts: ctDhcpServerIfTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpServerIfTable.setDescription("This table contains an entry for each port of a\n                        DHCP server which is eligible to perform DHCP functions. \n                        The table is indexed by ctDhcpIfIndex, which indicates\n                        the value of the MIB 2 ifindex which identifies the\n                        device's interface for which the entry exists.")
ctDhcpServerIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1), ).setIndexNames((0, "CTRON-DHCP-MIB", "ctDhcpIfIndex"))
if mibBuilder.loadTexts: ctDhcpServerIfEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpServerIfEntry.setDescription('A description of the configuration parameters for a\n                         single interface on the DHCP server.')
ctDhcpIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfIndex.setDescription('A unique value identifying an element in a sequence of\n                        entries which belong to the DHCP server interface list.  \n                        This value ranges from 1 to 2.')
ctDhcpIfAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfAdminStatus.setDescription('Used to enable and disable the DHCP functions on this\n                        interface only.  This object must be set to enabled for \n                        the DHCP functions to occur on this interface.')
ctDhcpIfOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("invalid-config", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfOperStatus.setDescription('Indicates the current operating status of the DHCP\n                        server function on this interface.')
ctDhcpIfServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfServerAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfServerAddress.setDescription('This is the IP address of the interface which\n                        is providing access to the DHCP server for clients\n                        which are connected to this network.')
ctDhcpIfNetworkAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfNetworkAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfNetworkAddress.setDescription('This is the IP subnet which is being served by\n                        this interface of the DHCP server.')
ctDhcpIfSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfSubnetMask.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfSubnetMask.setDescription('This is the subnet mask of the IP subnet which is \n                        being served by this interface of the DHCP server.')
ctDhcpIfLowestaddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfLowestaddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfLowestaddress.setDescription('This is the lowest numerical value of the IP address\n                        range that will be assigned to clients by this interface\n                        of the DHCP server.  Its value must be greater or equal \n                        to ctDhcpIfNetworkAddress and less than or equal to \n                        ctDhcpIfHighestAddress.')
ctDhcpIfHighestAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfHighestAddress.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfHighestAddress.setDescription('This is the highest numerical value of the IP address\n                        range that will be assigned to clients by this interface\n                        of the DHCP server.  Its value must be greater or equal\n                        to ctDhcpIfLowestaddress but remain within \n                        ctDhcpIfNetworkAddress.')
ctDhcpIfAddressesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfAddressesUsed.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfAddressesUsed.setDescription('This value is the number of clients which are currently \n                        using IP addresses assigned by this interface of the\n                        DHCP server.')
ctDhcpIfAddressesFree = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpIfAddressesFree.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfAddressesFree.setDescription('This value is the number of IP addresses that are \n                        currently available for distribution by this interface \n                        of the DHCP server.')
ctDhcpIfLeasePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfLeasePeriod.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfLeasePeriod.setDescription('This value is the time period for which an IP address\n                        assigned by this interface is valid.  The units are \n                        seconds.  A value of 0 signifys that the lease will \n                        never expire.')
ctDhcpIfDefaultGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 12), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDefaultGateway.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfDefaultGateway.setDescription('This value is an DHCP option that can be passed to a \n                        client by this interface if it is requested as part \n                        of the DHCP process.  This value is the IP address of \n                        the default gateway to be used by the client.')
ctDhcpIfDomainNameServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDomainNameServer.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfDomainNameServer.setDescription('This value is an DHCP option that can be passed to a \n                        client by this interface if it is requested as part \n                        of the DHCP process.  This value is the IP address of \n                        the domain name server to be used by the client.')
ctDhcpIfDomainName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 14), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfDomainName.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfDomainName.setDescription('This value is an DHCP option that can be passed to a \n                        client by this interface if it is requested as part \n                        of the DHCP process.  This value is the domain name \n                        to be used by the client.')
ctDhcpIfWINServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 2, 1, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDhcpIfWINServer.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpIfWINServer.setDescription('This value is an DHCP option that can be passed to a \n                        client by this interface if it is requested as part \n                        of the DHCP process.  This value is the IP address of \n                        the NetBIOS overTCP/IP name server to be used by the \n                        client.')
ctDhcpClientStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1), )
if mibBuilder.loadTexts: ctDhcpClientStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientStatsTable.setDescription('This table contains an entry for each DHCP client. The\n                        table is indexed by ctDhcpClientStatsID, which indicates\n                        an arbitrary order of entries.')
ctDhcpClientStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1), ).setIndexNames((0, "CTRON-DHCP-MIB", "ctDhcpClientStatsID"))
if mibBuilder.loadTexts: ctDhcpClientStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientStatsEntry.setDescription('A description of a single client, which could be on any\n                        of the subnets being served by participating interfaces.')
ctDhcpClientStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientStatsID.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientStatsID.setDescription('A unique value identifying an element in a sequence of\n                        active clients which have been given network addresses \n                        by this DHCP server.')
ctDhcpClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientName.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientName.setDescription('This is the name of the client as listed by the client\n                        in a DHCP request packet.')
ctDhcpClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientIP.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientIP.setDescription('This is the assigned IP address of the client during\n                        this active connection.')
ctDhcpClientID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpClientID.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpClientID.setDescription("This is the ID of the client as listed by the client\n                        in a DHCP request packet.  It is normally the client's\n                        Ethernet MAC address.")
ctDhcpEndOfLease = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 2, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDhcpEndOfLease.setStatus('mandatory')
if mibBuilder.loadTexts: ctDhcpEndOfLease.setDescription('This value is the time at which the lease of the IP\n                        address will expire.  The units are seconds and the\n                        value is relative to the same starting point as \n                        ctDhcpIfServerTime.')
mibBuilder.exportSymbols("CTRON-DHCP-MIB", ctDhcpOperStatus=ctDhcpOperStatus, ctDhcpServerIfTable=ctDhcpServerIfTable, ctDhcpRequests=ctDhcpRequests, ctDhcpNoOfActiveClients=ctDhcpNoOfActiveClients, ctDhcpClientStatsID=ctDhcpClientStatsID, ctDhcpIfLowestaddress=ctDhcpIfLowestaddress, ctDhcpIfNetworkAddress=ctDhcpIfNetworkAddress, ctDhcpIfHighestAddress=ctDhcpIfHighestAddress, ctDhcpClientName=ctDhcpClientName, ctDhcpIfIndex=ctDhcpIfIndex, ctDhcpClientIP=ctDhcpClientIP, ctDhcpOffers=ctDhcpOffers, ctDhcpIfWINServer=ctDhcpIfWINServer, ctDhcpServerTime=ctDhcpServerTime, ctDhcpIfDomainNameServer=ctDhcpIfDomainNameServer, ctDhcpDeclines=ctDhcpDeclines, ctDhcpClientStatsTable=ctDhcpClientStatsTable, ctDhcpIfAddressesUsed=ctDhcpIfAddressesUsed, ctDhcp=ctDhcp, ctDhcpServerIfEntry=ctDhcpServerIfEntry, ctDhcpAdminStatus=ctDhcpAdminStatus, ctDhcpIfDefaultGateway=ctDhcpIfDefaultGateway, ctDhcpClientID=ctDhcpClientID, ctDhcpInterfaceConfig=ctDhcpInterfaceConfig, ctDhcpOtherServers=ctDhcpOtherServers, ctDhcpClientStatsEntry=ctDhcpClientStatsEntry, ctDhcpReclaimIP=ctDhcpReclaimIP, ctDhcpIfLeasePeriod=ctDhcpIfLeasePeriod, ctDhcpServerStats=ctDhcpServerStats, ctDhcpIfAdminStatus=ctDhcpIfAdminStatus, ctDhcpIfAddressesFree=ctDhcpIfAddressesFree, ctDhcpNaks=ctDhcpNaks, ctDhcpIfDomainName=ctDhcpIfDomainName, ctDhcpEndOfLease=ctDhcpEndOfLease, ctDhcpIfSubnetMask=ctDhcpIfSubnetMask, ctDhcpProtocolErrors=ctDhcpProtocolErrors, ctDhcpReleases=ctDhcpReleases, ctDhcpAcks=ctDhcpAcks, ctDhcpClientStatusTable=ctDhcpClientStatusTable, ctDhcpIfServerAddress=ctDhcpIfServerAddress, ctDhcpDiscovers=ctDhcpDiscovers, ctDhcpIfOperStatus=ctDhcpIfOperStatus)
