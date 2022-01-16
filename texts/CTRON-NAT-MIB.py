#
# PySNMP MIB module CTRON-NAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-NAT-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:36 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
nwIpClientServices, nwIpMibs, nwIpRouter, nwIpComponents = mibBuilder.importSymbols("CTRON-IP-ROUTER-MIB", "nwIpClientServices", "nwIpMibs", "nwIpRouter", "nwIpComponents")
nwRtrProtoSuites, = mibBuilder.importSymbols("ROUTER-OIDS", "nwRtrProtoSuites")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, iso, Counter64, Unsigned32, MibIdentifier, Counter32, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "iso", "Counter64", "Unsigned32", "MibIdentifier", "Counter32", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctNat = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1))
ctNatConfigGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1))
ctNatServerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2))
ctNatConnStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3))
ctNatPublicIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatPublicIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatPublicIfIndex.setDescription('This is the value of the MIB II ifindex which identifies \n                        the router port connected to the public network.')
ctNatPublicIP = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatPublicIP.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatPublicIP.setDescription('This is the IP address of the interface which\n                        is selected by ctNatPublicIfIndex.')
ctNatPublicMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatPublicMask.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatPublicMask.setDescription('This is the subnet mask of the interface which\n                        is selected by ctNatPublicIfIndex.')
ctNatMaxConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatMaxConn.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatMaxConn.setDescription('This is the value of the maximum number of simultaneous\n                        connections allowed, using the Network Address \n                        Translator application.  The default value is 200.  \n                        Acceptable values are from 40 to 1000.')
ctNatTcpTimeout = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatTcpTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatTcpTimeout.setDescription('This is the value in seconds after which an idle\n                        TCP connection will be deleted.  The default value\n                        is 300.  Acceptable values are from 60 to 3600.')
ctNatUdpTimeout = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatUdpTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatUdpTimeout.setDescription('This is the value in seconds after which an idle\n                        UDP connection will be deleted.  The default value\n                        is 120.  Acceptable values are from 60 to 3600.')
ctNatPktsL2I = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatPktsL2I.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatPktsL2I.setDescription('This is the number of packets which have been forwarded \n                        from the private network to the public network since the\n                        last reset.')
ctNatPktsI2L = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatPktsI2L.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatPktsI2L.setDescription('This is the number of packets which have been forwarded \n                        from the public network to the private network since the\n                        last reset.')
ctNatBytesL2I = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatBytesL2I.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatBytesL2I.setDescription('This is the number of bytes which have been forwarded \n                        from the private network to the public network since the\n                        last reset.')
ctNatBytesI2L = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatBytesI2L.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatBytesI2L.setDescription('This is the number of bytes which have been forwarded\n                        from the public network to the private network since the\n                        last reset.')
ctNatTcpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTcpConn.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatTcpConn.setDescription('This is the number of active TCP connections using\n                        the Network Address Translator application.')
ctNatUdpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatUdpConn.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatUdpConn.setDescription('This is the number of active UDP connections using\n                        the Network Address Translator application.')
ctNatIcmpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatIcmpConn.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatIcmpConn.setDescription('This is the number of active ICMP connections using\n                        the Network Address Translator application.')
ctNatRetries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatRetries.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatRetries.setDescription('This is the number of detected TCP retries in both\n                        directions since the last reset.')
ctNatBadSums = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatBadSums.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatBadSums.setDescription('This is the number of detected checksum errors in both\n                        directions since the last reset.')
ctNatTotalPkts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotalPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatTotalPkts.setDescription('This is the total number of packets by the application\n                        since the last reset.')
ctNatBadPkts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatBadPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatBadPkts.setDescription('This is the total number of packets detected with an \n                        invalid format since the last reset.')
ctNatResPkts = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatResPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatResPkts.setDescription('This is the total number of packets detected with a\n                        reserved address since the last reset.')
ctNatTotTcpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotTcpConn.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatTotTcpConn.setDescription('This is the number of TCP connections made\n                        using the Network Address Translator application\n                        since the last reset.')
ctNatTotUdpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotUdpConn.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatTotUdpConn.setDescription('This is the number of UDP connections made\n                        using the Network Address Translator application\n                        since the last reset.')
ctNatTotIcmpConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotIcmpConn.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatTotIcmpConn.setDescription('This is the number of ICMP connections made\n                        using the Network Address Translator application\n                        since the last reset.')
ctNatConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22), )
if mibBuilder.loadTexts: ctNatConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConfigTable.setDescription('Information describing the configuration parameters\n                        for each instance of NAT.')
ctNatConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1), ).setIndexNames((0, "CTRON-NAT-MIB", "ctNatConfigId"))
if mibBuilder.loadTexts: ctNatConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConfigEntry.setDescription('A description of a single server entry.')
ctNatConfigId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConfigId.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConfigId.setDescription('A unique value identifying an element in a sequence of\n                        groups which belong to the NAT configuration table.')
ctNatAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatAdminStatus.setDescription('Used to enable and disable the Network Address \n                        Translator method for this instance.  This object must \n                        be set to enabled for the translation to occur on \n                        ctNatLocalIfIndex.')
ctNatOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("invalid-config", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatOperStatus.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatOperStatus.setDescription('Indicates the current operating status of the Network \n                        Address Translator feature.')
ctNatLocalIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatLocalIfIndex.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatLocalIfIndex.setDescription('This is the value of the MIB II ifindex which identifies \n                        the router port connected to the private network.')
ctNatLocalIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatLocalIP.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatLocalIP.setDescription('This is the IP address of the interface which\n                        serves as the gateway for the private network.\n                        With ctNatLocalMask, it serves to define the subnet \n                        of the hosts on the network.  The preferred address \n                        is 192.168.254.254, part of the class C net reserved \n                        by RFC1597.')
ctNatLocalMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 1, 22, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatLocalMask.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatLocalMask.setDescription('This is the subnet mask of the interface which\n                        serves as the gateway for the private network.\n                        With ctNatLocalIP, it serves to define the subnet \n                        of the hosts on the network.  The preferred mask is\n                        255.255.255.0, part of the class C net reserved \n                        by RFC1597.')
ctNatTotServerEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotServerEntries.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatTotServerEntries.setDescription('This is the total number of server assignments.')
ctNatServerListTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2), )
if mibBuilder.loadTexts: ctNatServerListTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatServerListTable.setDescription('Information describing the configured parameters\n                        which designate a local device as a server.')
ctNatServerListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2, 1), ).setIndexNames((0, "CTRON-NAT-MIB", "ctNatServerId"))
if mibBuilder.loadTexts: ctNatServerListEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatServerListEntry.setDescription('A description of a single server entry.')
ctNatServerId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatServerId.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatServerId.setDescription('A unique value identifying an element in a sequence of\n                        groups which belong to the NAT Server List.  This value\n                        ranges from 1 to 16.')
ctNatProxyServer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 2, 2, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctNatProxyServer.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatProxyServer.setDescription('A description of a proxy server assignment.  The format\n                        is private IP address of the server, followed by the \n                        public port number, followed by the private port number, \n                        followed by the protocol to be handled by the server.  \n                        The fields are delimited by commas.  Each record must be \n                        31 chars or less.  Protocol choices are TCP and UDP.')
ctNatTotActiveConn = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatTotActiveConn.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatTotActiveConn.setDescription('This is the total number of active connections.')
ctNatConnStatsTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2), )
if mibBuilder.loadTexts: ctNatConnStatsTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsTable.setDescription('Information describing the configured parameters\n                        which designate a local device as a server.')
ctNatConnStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1), ).setIndexNames((0, "CTRON-NAT-MIB", "ctNatConnStatsID"))
if mibBuilder.loadTexts: ctNatConnStatsEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsEntry.setDescription('A description of a single server entry.')
ctNatConnStatsID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsID.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsID.setDescription('A unique value identifying an element in a sequence of\n                        active connections which belong to the NAT Connection\n                        Statistics Group.')
ctNatConnStatsForeignIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsForeignIP.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsForeignIP.setDescription('This is the IP address of the foreign host during\n                        this active connection.')
ctNatConnStatsLocalIP = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsLocalIP.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsLocalIP.setDescription('This is the IP address of the local host during\n                        this active connection.')
ctNatConnStatsPublicPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsPublicPort.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsPublicPort.setDescription('This is the port number addressed by an external \n                        device.  It is also substituted for the local port \n                        by NAT on outbound packets.')
ctNatConnStatsLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsLocalPort.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsLocalPort.setDescription("This is the local host's port for TCP or UDP\n                        for this active connection.")
ctNatConnStatsForeignPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsForeignPort.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsForeignPort.setDescription('This is the source port number used by the\n                        foreign host for this active connection.')
ctNatConnStatsOutgoingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsOutgoingPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsOutgoingPkts.setDescription('This is the number of packets that have been sent \n                        from the local net to the public net by this \n                        active connection.')
ctNatConnStatsOutgoingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsOutgoingBytes.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsOutgoingBytes.setDescription('This is the number of bytes that have been sent \n                        from the local net to the public net by this \n                        active connection.')
ctNatConnStatsIncomingPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsIncomingPkts.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsIncomingPkts.setDescription('This is the number of packets that have been sent from\n                        the public net to the local net by this active connection.')
ctNatConnStatsIncomingBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsIncomingBytes.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsIncomingBytes.setDescription('This is the number of bytes that have been sent from\n                        the public net to the local net by this active connection.')
ctNatConnStatsTimeSinceUse = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsTimeSinceUse.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsTimeSinceUse.setDescription('This is the time in seconds since the last packet \n                        was sent or received on this active connection.')
ctNatConnStatsProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsProtocol.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsProtocol.setDescription('This is the type of IP protocol used by this \n                        active connection.  Options are 1 = ICMP, 6 = TCP \n                        and 17 = UDP.')
ctNatConnStatsTCPSeq = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsTCPSeq.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsTCPSeq.setDescription('This is the last TCP sequence number of local host \n                        sent on this active connection.')
ctNatConnStatsTCPAck = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsTCPAck.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsTCPAck.setDescription('This is the last TCP acknowledgement number of \n                        local host sent on this active connection.')
ctNatConnStatsTCPState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsTCPState.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsTCPState.setDescription('This is the TCP connection state value on this \n                        active connection.')
ctNatConnStatsLocalRetrys = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsLocalRetrys.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsLocalRetrys.setDescription('This is the number of TCP retries by the local host \n                        on this active connection.')
ctNatConnStatsForeignRetrys = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsForeignRetrys.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsForeignRetrys.setDescription('This is the number of TCP retries by the foreign host \n                        on this active connection.')
ctNatConnStatsLocalChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsLocalChecksum.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsLocalChecksum.setDescription('This is the number of times checksum failed in a \n                        packet from the local host on this active connection.')
ctNatConnStatsForeignChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3, 1, 2, 12, 1, 3, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctNatConnStatsForeignChecksum.setStatus('mandatory')
if mibBuilder.loadTexts: ctNatConnStatsForeignChecksum.setDescription('This is the number of times checksum failed in a \n                        packet from the foreign host on this active connection.')
mibBuilder.exportSymbols("CTRON-NAT-MIB", ctNatConnStatsID=ctNatConnStatsID, ctNatBadPkts=ctNatBadPkts, ctNatConnStatsOutgoingPkts=ctNatConnStatsOutgoingPkts, ctNatPublicMask=ctNatPublicMask, ctNatConnStatsOutgoingBytes=ctNatConnStatsOutgoingBytes, ctNatConnStatsGroup=ctNatConnStatsGroup, ctNatConnStatsForeignRetrys=ctNatConnStatsForeignRetrys, ctNatConfigTable=ctNatConfigTable, ctNatLocalMask=ctNatLocalMask, ctNatLocalIP=ctNatLocalIP, ctNatConfigEntry=ctNatConfigEntry, ctNat=ctNat, ctNatConfigId=ctNatConfigId, ctNatServerGroup=ctNatServerGroup, ctNatConnStatsLocalChecksum=ctNatConnStatsLocalChecksum, ctNatPublicIfIndex=ctNatPublicIfIndex, ctNatTcpConn=ctNatTcpConn, ctNatTcpTimeout=ctNatTcpTimeout, ctNatConnStatsLocalIP=ctNatConnStatsLocalIP, ctNatPktsI2L=ctNatPktsI2L, ctNatTotTcpConn=ctNatTotTcpConn, ctNatIcmpConn=ctNatIcmpConn, ctNatOperStatus=ctNatOperStatus, ctNatConnStatsTCPAck=ctNatConnStatsTCPAck, ctNatAdminStatus=ctNatAdminStatus, ctNatLocalIfIndex=ctNatLocalIfIndex, ctNatMaxConn=ctNatMaxConn, ctNatConnStatsIncomingPkts=ctNatConnStatsIncomingPkts, ctNatConnStatsForeignPort=ctNatConnStatsForeignPort, ctNatConnStatsIncomingBytes=ctNatConnStatsIncomingBytes, ctNatPktsL2I=ctNatPktsL2I, ctNatBytesI2L=ctNatBytesI2L, ctNatProxyServer=ctNatProxyServer, ctNatBadSums=ctNatBadSums, ctNatTotIcmpConn=ctNatTotIcmpConn, ctNatResPkts=ctNatResPkts, ctNatServerListEntry=ctNatServerListEntry, ctNatTotActiveConn=ctNatTotActiveConn, ctNatConnStatsEntry=ctNatConnStatsEntry, ctNatConnStatsTimeSinceUse=ctNatConnStatsTimeSinceUse, ctNatTotalPkts=ctNatTotalPkts, ctNatConnStatsForeignIP=ctNatConnStatsForeignIP, ctNatTotServerEntries=ctNatTotServerEntries, ctNatConnStatsLocalRetrys=ctNatConnStatsLocalRetrys, ctNatUdpTimeout=ctNatUdpTimeout, ctNatConnStatsForeignChecksum=ctNatConnStatsForeignChecksum, ctNatServerId=ctNatServerId, ctNatBytesL2I=ctNatBytesL2I, ctNatConnStatsTCPSeq=ctNatConnStatsTCPSeq, ctNatConnStatsTable=ctNatConnStatsTable, ctNatTotUdpConn=ctNatTotUdpConn, ctNatUdpConn=ctNatUdpConn, ctNatConnStatsPublicPort=ctNatConnStatsPublicPort, ctNatConfigGroup=ctNatConfigGroup, ctNatConnStatsLocalPort=ctNatConnStatsLocalPort, ctNatConnStatsTCPState=ctNatConnStatsTCPState, ctNatConnStatsProtocol=ctNatConnStatsProtocol, ctNatRetries=ctNatRetries, ctNatPublicIP=ctNatPublicIP, ctNatServerListTable=ctNatServerListTable)
