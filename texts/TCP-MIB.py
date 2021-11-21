#
# PySNMP MIB module TCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/TCP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:25:48 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
InetAddressType, InetAddress, InetPortNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress", "InetPortNumber")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
mib_2, ModuleIdentity, Counter32, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, NotificationType, Unsigned32, Counter64, Integer32, TimeTicks, IpAddress, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "mib-2", "ModuleIdentity", "Counter32", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "NotificationType", "Unsigned32", "Counter64", "Integer32", "TimeTicks", "IpAddress", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
tcpMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 49))
tcpMIB.setRevisions(('2005-02-18 00:00', '1994-11-01 00:00', '1991-03-31 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tcpMIB.setRevisionsDescriptions(('IP version neutral revision, published as RFC 4022.', 'Initial SMIv2 version, published as RFC 2012.', 'The initial revision of this MIB module was part of\n            MIB-II.',))
if mibBuilder.loadTexts: tcpMIB.setLastUpdated('200502180000Z')
if mibBuilder.loadTexts: tcpMIB.setOrganization('IETF IPv6 MIB Revision Team\n            http://www.ietf.org/html.charters/ipv6-charter.html')
if mibBuilder.loadTexts: tcpMIB.setContactInfo('Rajiv Raghunarayan (editor)\n\n            Cisco Systems Inc.\n            170 West Tasman Drive\n            San Jose, CA 95134\n\n            Phone: +1 408 853 9612\n            Email: <raraghun@cisco.com>\n\n            Send comments to <ipv6@ietf.org>')
if mibBuilder.loadTexts: tcpMIB.setDescription('The MIB module for managing TCP implementations.\n\n            Copyright (C) The Internet Society (2005). This version\n            of this MIB module is a part of RFC 4022; see the RFC\n            itself for full legal notices.')
tcp = MibIdentifier((1, 3, 6, 1, 2, 1, 6))
tcpRtoAlgorithm = MibScalar((1, 3, 6, 1, 2, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("other", 1), ("constant", 2), ("rsre", 3), ("vanj", 4), ("rfc2988", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRtoAlgorithm.setStatus('current')
if mibBuilder.loadTexts: tcpRtoAlgorithm.setDescription('The algorithm used to determine the timeout value used for\n            retransmitting unacknowledged octets.')
tcpRtoMin = MibScalar((1, 3, 6, 1, 2, 1, 6, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRtoMin.setStatus('current')
if mibBuilder.loadTexts: tcpRtoMin.setDescription('The minimum value permitted by a TCP implementation for\n            the retransmission timeout, measured in milliseconds.\n            More refined semantics for objects of this type depend\n            on the algorithm used to determine the retransmission\n            timeout; in particular, the IETF standard algorithm\n            rfc2988(5) provides a minimum value.')
tcpRtoMax = MibScalar((1, 3, 6, 1, 2, 1, 6, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('milliseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRtoMax.setStatus('current')
if mibBuilder.loadTexts: tcpRtoMax.setDescription('The maximum value permitted by a TCP implementation for\n            the retransmission timeout, measured in milliseconds.\n            More refined semantics for objects of this type depend\n            on the algorithm used to determine the retransmission\n            timeout; in particular, the IETF standard algorithm\n            rfc2988(5) provides an upper bound (as part of an\n            adaptive backoff algorithm).')
tcpMaxConn = MibScalar((1, 3, 6, 1, 2, 1, 6, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 2147483647), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpMaxConn.setStatus('current')
if mibBuilder.loadTexts: tcpMaxConn.setDescription('The limit on the total number of TCP connections the entity\n            can support.  In entities where the maximum number of\n            connections is dynamic, this object should contain the\n            value -1.')
tcpActiveOpens = MibScalar((1, 3, 6, 1, 2, 1, 6, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpActiveOpens.setStatus('current')
if mibBuilder.loadTexts: tcpActiveOpens.setDescription('The number of times that TCP connections have made a direct\n            transition to the SYN-SENT state from the CLOSED state.\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpPassiveOpens = MibScalar((1, 3, 6, 1, 2, 1, 6, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpPassiveOpens.setStatus('current')
if mibBuilder.loadTexts: tcpPassiveOpens.setDescription('The number of times TCP connections have made a direct\n            transition to the SYN-RCVD state from the LISTEN state.\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpAttemptFails = MibScalar((1, 3, 6, 1, 2, 1, 6, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpAttemptFails.setStatus('current')
if mibBuilder.loadTexts: tcpAttemptFails.setDescription('The number of times that TCP connections have made a direct\n            transition to the CLOSED state from either the SYN-SENT\n            state or the SYN-RCVD state, plus the number of times that\n            TCP connections have made a direct transition to the\n            LISTEN state from the SYN-RCVD state.\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpEstabResets = MibScalar((1, 3, 6, 1, 2, 1, 6, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpEstabResets.setStatus('current')
if mibBuilder.loadTexts: tcpEstabResets.setDescription('The number of times that TCP connections have made a direct\n            transition to the CLOSED state from either the ESTABLISHED\n            state or the CLOSE-WAIT state.\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpCurrEstab = MibScalar((1, 3, 6, 1, 2, 1, 6, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpCurrEstab.setStatus('current')
if mibBuilder.loadTexts: tcpCurrEstab.setDescription('The number of TCP connections for which the current state\n            is either ESTABLISHED or CLOSE-WAIT.')
tcpInSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpInSegs.setStatus('current')
if mibBuilder.loadTexts: tcpInSegs.setDescription('The total number of segments received, including those\n            received in error.  This count includes segments received\n            on currently established connections.\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpOutSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpOutSegs.setStatus('current')
if mibBuilder.loadTexts: tcpOutSegs.setDescription('The total number of segments sent, including those on\n            current connections but excluding those containing only\n            retransmitted octets.\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpRetransSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpRetransSegs.setStatus('current')
if mibBuilder.loadTexts: tcpRetransSegs.setDescription('The total number of segments retransmitted; that is, the\n            number of TCP segments transmitted containing one or more\n            previously transmitted octets.\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpInErrs = MibScalar((1, 3, 6, 1, 2, 1, 6, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpInErrs.setStatus('current')
if mibBuilder.loadTexts: tcpInErrs.setDescription('The total number of segments received in error (e.g., bad\n            TCP checksums).\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpOutRsts = MibScalar((1, 3, 6, 1, 2, 1, 6, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpOutRsts.setStatus('current')
if mibBuilder.loadTexts: tcpOutRsts.setDescription('The number of TCP segments sent containing the RST flag.\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpHCInSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 17), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpHCInSegs.setStatus('current')
if mibBuilder.loadTexts: tcpHCInSegs.setDescription('The total number of segments received, including those\n            received in error.  This count includes segments received\n\n            on currently established connections.  This object is\n            the 64-bit equivalent of tcpInSegs.\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpHCOutSegs = MibScalar((1, 3, 6, 1, 2, 1, 6, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpHCOutSegs.setStatus('current')
if mibBuilder.loadTexts: tcpHCOutSegs.setDescription('The total number of segments sent, including those on\n            current connections but excluding those containing only\n            retransmitted octets.  This object is the 64-bit\n            equivalent of tcpOutSegs.\n\n            Discontinuities in the value of this counter are\n            indicated via discontinuities in the value of sysUpTime.')
tcpConnectionTable = MibTable((1, 3, 6, 1, 2, 1, 6, 19), )
if mibBuilder.loadTexts: tcpConnectionTable.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionTable.setDescription('A table containing information about existing TCP\n            connections.  Note that unlike earlier TCP MIBs, there\n            is a separate table for connections in the LISTEN state.')
tcpConnectionEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 19, 1), ).setIndexNames((0, "TCP-MIB", "tcpConnectionLocalAddressType"), (0, "TCP-MIB", "tcpConnectionLocalAddress"), (0, "TCP-MIB", "tcpConnectionLocalPort"), (0, "TCP-MIB", "tcpConnectionRemAddressType"), (0, "TCP-MIB", "tcpConnectionRemAddress"), (0, "TCP-MIB", "tcpConnectionRemPort"))
if mibBuilder.loadTexts: tcpConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionEntry.setDescription('A conceptual row of the tcpConnectionTable containing\n            information about a particular current TCP connection.\n            Each row of this table is transient in that it ceases to\n            exist when (or soon after) the connection makes the\n            transition to the CLOSED state.')
tcpConnectionLocalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 1), InetAddressType())
if mibBuilder.loadTexts: tcpConnectionLocalAddressType.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionLocalAddressType.setDescription('The address type of tcpConnectionLocalAddress.')
tcpConnectionLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 2), InetAddress())
if mibBuilder.loadTexts: tcpConnectionLocalAddress.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionLocalAddress.setDescription('The local IP address for this TCP connection.  The type\n            of this address is determined by the value of\n            tcpConnectionLocalAddressType.\n\n            As this object is used in the index for the\n            tcpConnectionTable, implementors should be\n            careful not to create entries that would result in OIDs\n            with more than 128 subidentifiers; otherwise the information\n            cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3.')
tcpConnectionLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: tcpConnectionLocalPort.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionLocalPort.setDescription('The local port number for this TCP connection.')
tcpConnectionRemAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 4), InetAddressType())
if mibBuilder.loadTexts: tcpConnectionRemAddressType.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionRemAddressType.setDescription('The address type of tcpConnectionRemAddress.')
tcpConnectionRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 5), InetAddress())
if mibBuilder.loadTexts: tcpConnectionRemAddress.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionRemAddress.setDescription('The remote IP address for this TCP connection.  The type\n            of this address is determined by the value of\n            tcpConnectionRemAddressType.\n\n            As this object is used in the index for the\n            tcpConnectionTable, implementors should be\n            careful not to create entries that would result in OIDs\n            with more than 128 subidentifiers; otherwise the information\n            cannot be accessed by using SNMPv1, SNMPv2c, or SNMPv3.')
tcpConnectionRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 6), InetPortNumber())
if mibBuilder.loadTexts: tcpConnectionRemPort.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionRemPort.setDescription('The remote port number for this TCP connection.')
tcpConnectionState = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpConnectionState.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionState.setDescription("The state of this TCP connection.\n\n            The value listen(2) is included only for parallelism to the\n            old tcpConnTable and should not be used.  A connection in\n            LISTEN state should be present in the tcpListenerTable.\n\n            The only value that may be set by a management station is\n            deleteTCB(12).  Accordingly, it is appropriate for an agent\n            to return a `badValue' response if a management station\n            attempts to set this object to any other value.\n\n            If a management station sets this object to the value\n            deleteTCB(12), then the TCB (as defined in [RFC793]) of\n            the corresponding connection on the managed node is\n            deleted, resulting in immediate termination of the\n            connection.\n\n            As an implementation-specific option, a RST segment may be\n            sent from the managed node to the other TCP endpoint (note,\n            however, that RST segments are not sent reliably).")
tcpConnectionProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 19, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnectionProcess.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionProcess.setDescription("The system's process ID for the process associated with\n            this connection, or zero if there is no such process.  This\n            value is expected to be the same as HOST-RESOURCES-MIB::\n            hrSWRunIndex or SYSAPPL-MIB::sysApplElmtRunIndex for some\n            row in the appropriate tables.")
tcpListenerTable = MibTable((1, 3, 6, 1, 2, 1, 6, 20), )
if mibBuilder.loadTexts: tcpListenerTable.setStatus('current')
if mibBuilder.loadTexts: tcpListenerTable.setDescription("A table containing information about TCP listeners.  A\n            listening application can be represented in three\n            possible ways:\n\n            1. An application that is willing to accept both IPv4 and\n               IPv6 datagrams is represented by\n\n               a tcpListenerLocalAddressType of unknown (0) and\n               a tcpListenerLocalAddress of ''h (a zero-length\n               octet-string).\n\n            2. An application that is willing to accept only IPv4 or\n               IPv6 datagrams is represented by a\n               tcpListenerLocalAddressType of the appropriate address\n               type and a tcpListenerLocalAddress of '0.0.0.0' or '::'\n               respectively.\n\n            3. An application that is listening for data destined\n               only to a specific IP address, but from any remote\n               system, is represented by a tcpListenerLocalAddressType\n               of an appropriate address type, with\n               tcpListenerLocalAddress as the specific local address.\n\n            NOTE: The address type in this table represents the\n            address type used for the communication, irrespective\n            of the higher-layer abstraction.  For example, an\n            application using IPv6 'sockets' to communicate via\n            IPv4 between ::ffff:10.0.0.1 and ::ffff:10.0.0.2 would\n            use InetAddressType ipv4(1)).")
tcpListenerEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 20, 1), ).setIndexNames((0, "TCP-MIB", "tcpListenerLocalAddressType"), (0, "TCP-MIB", "tcpListenerLocalAddress"), (0, "TCP-MIB", "tcpListenerLocalPort"))
if mibBuilder.loadTexts: tcpListenerEntry.setStatus('current')
if mibBuilder.loadTexts: tcpListenerEntry.setDescription('A conceptual row of the tcpListenerTable containing\n            information about a particular TCP listener.')
tcpListenerLocalAddressType = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 1), InetAddressType())
if mibBuilder.loadTexts: tcpListenerLocalAddressType.setStatus('current')
if mibBuilder.loadTexts: tcpListenerLocalAddressType.setDescription('The address type of tcpListenerLocalAddress.  The value\n            should be unknown (0) if connection initiations to all\n            local IP addresses are accepted.')
tcpListenerLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 2), InetAddress())
if mibBuilder.loadTexts: tcpListenerLocalAddress.setStatus('current')
if mibBuilder.loadTexts: tcpListenerLocalAddress.setDescription("The local IP address for this TCP connection.\n\n            The value of this object can be represented in three\n            possible ways, depending on the characteristics of the\n            listening application:\n\n            1. For an application willing to accept both IPv4 and\n               IPv6 datagrams, the value of this object must be\n               ''h (a zero-length octet-string), with the value\n               of the corresponding tcpListenerLocalAddressType\n               object being unknown (0).\n\n            2. For an application willing to accept only IPv4 or\n               IPv6 datagrams, the value of this object must be\n               '0.0.0.0' or '::' respectively, with\n               tcpListenerLocalAddressType representing the\n               appropriate address type.\n\n            3. For an application which is listening for data\n               destined only to a specific IP address, the value\n               of this object is the specific local address, with\n               tcpListenerLocalAddressType representing the\n               appropriate address type.\n\n            As this object is used in the index for the\n            tcpListenerTable, implementors should be\n            careful not to create entries that would result in OIDs\n            with more than 128 subidentifiers; otherwise the information\n            cannot be accessed, using SNMPv1, SNMPv2c, or SNMPv3.")
tcpListenerLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 3), InetPortNumber())
if mibBuilder.loadTexts: tcpListenerLocalPort.setStatus('current')
if mibBuilder.loadTexts: tcpListenerLocalPort.setDescription('The local port number for this TCP connection.')
tcpListenerProcess = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 20, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpListenerProcess.setStatus('current')
if mibBuilder.loadTexts: tcpListenerProcess.setDescription("The system's process ID for the process associated with\n            this listener, or zero if there is no such process.  This\n            value is expected to be the same as HOST-RESOURCES-MIB::\n            hrSWRunIndex or SYSAPPL-MIB::sysApplElmtRunIndex for some\n            row in the appropriate tables.")
tcpConnTable = MibTable((1, 3, 6, 1, 2, 1, 6, 13), )
if mibBuilder.loadTexts: tcpConnTable.setStatus('deprecated')
if mibBuilder.loadTexts: tcpConnTable.setDescription('A table containing information about existing IPv4-specific\n            TCP connections or listeners.  This table has been\n            deprecated in favor of the version neutral\n            tcpConnectionTable.')
tcpConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 6, 13, 1), ).setIndexNames((0, "TCP-MIB", "tcpConnLocalAddress"), (0, "TCP-MIB", "tcpConnLocalPort"), (0, "TCP-MIB", "tcpConnRemAddress"), (0, "TCP-MIB", "tcpConnRemPort"))
if mibBuilder.loadTexts: tcpConnEntry.setStatus('deprecated')
if mibBuilder.loadTexts: tcpConnEntry.setDescription('A conceptual row of the tcpConnTable containing information\n            about a particular current IPv4 TCP connection.  Each row\n            of this table is transient in that it ceases to exist when\n            (or soon after) the connection makes the transition to the\n            CLOSED state.')
tcpConnState = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))).clone(namedValues=NamedValues(("closed", 1), ("listen", 2), ("synSent", 3), ("synReceived", 4), ("established", 5), ("finWait1", 6), ("finWait2", 7), ("closeWait", 8), ("lastAck", 9), ("closing", 10), ("timeWait", 11), ("deleteTCB", 12)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tcpConnState.setStatus('deprecated')
if mibBuilder.loadTexts: tcpConnState.setDescription("The state of this TCP connection.\n\n            The only value that may be set by a management station is\n            deleteTCB(12).  Accordingly, it is appropriate for an agent\n            to return a `badValue' response if a management station\n            attempts to set this object to any other value.\n\n            If a management station sets this object to the value\n            deleteTCB(12), then the TCB (as defined in [RFC793]) of\n            the corresponding connection on the managed node is\n            deleted, resulting in immediate termination of the\n            connection.\n\n            As an implementation-specific option, a RST segment may be\n            sent from the managed node to the other TCP endpoint (note,\n            however, that RST segments are not sent reliably).")
tcpConnLocalAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnLocalAddress.setStatus('deprecated')
if mibBuilder.loadTexts: tcpConnLocalAddress.setDescription('The local IP address for this TCP connection.  In the case\n            of a connection in the listen state willing to\n            accept connections for any IP interface associated with the\n            node, the value 0.0.0.0 is used.')
tcpConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnLocalPort.setStatus('deprecated')
if mibBuilder.loadTexts: tcpConnLocalPort.setDescription('The local port number for this TCP connection.')
tcpConnRemAddress = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnRemAddress.setStatus('deprecated')
if mibBuilder.loadTexts: tcpConnRemAddress.setDescription('The remote IP address for this TCP connection.')
tcpConnRemPort = MibTableColumn((1, 3, 6, 1, 2, 1, 6, 13, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tcpConnRemPort.setStatus('deprecated')
if mibBuilder.loadTexts: tcpConnRemPort.setDescription('The remote port number for this TCP connection.')
tcpMIBConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 49, 2))
tcpMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 49, 2, 1))
tcpMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 49, 2, 2))
tcpMIBCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 49, 2, 1, 2)).setObjects(("TCP-MIB", "tcpBaseGroup"), ("TCP-MIB", "tcpConnectionGroup"), ("TCP-MIB", "tcpListenerGroup"), ("TCP-MIB", "tcpHCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpMIBCompliance2 = tcpMIBCompliance2.setStatus('current')
if mibBuilder.loadTexts: tcpMIBCompliance2.setDescription('The compliance statement for systems that implement TCP.\n\n            A number of INDEX objects cannot be\n            represented in the form of OBJECT clauses in SMIv2 but\n            have the following compliance requirements,\n            expressed in OBJECT clause form in this description\n            clause:\n\n            -- OBJECT      tcpConnectionLocalAddressType\n            -- SYNTAX      InetAddressType { ipv4(1), ipv6(2) }\n            -- DESCRIPTION\n            --     This MIB requires support for only global IPv4\n\n            --     and IPv6 address types.\n            --\n            -- OBJECT      tcpConnectionRemAddressType\n            -- SYNTAX      InetAddressType { ipv4(1), ipv6(2) }\n            -- DESCRIPTION\n            --     This MIB requires support for only global IPv4\n            --     and IPv6 address types.\n            --\n            -- OBJECT      tcpListenerLocalAddressType\n            -- SYNTAX      InetAddressType { unknown(0), ipv4(1),\n            --                               ipv6(2) }\n            -- DESCRIPTION\n            --     This MIB requires support for only global IPv4\n            --     and IPv6 address types.  The type unknown also\n            --     needs to be supported to identify a special\n            --     case in the listener table: a listen using\n            --     both IPv4 and IPv6 addresses on the device.\n            --\n           ')
tcpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 49, 2, 1, 1)).setObjects(("TCP-MIB", "tcpGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpMIBCompliance = tcpMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: tcpMIBCompliance.setDescription('The compliance statement for IPv4-only systems that\n            implement TCP.  In order to be IP version independent, this\n            compliance statement is deprecated in favor of\n            tcpMIBCompliance2.  However, agents are still encouraged\n            to implement these objects in order to interoperate with\n            the deployed base of managers.')
tcpGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 1)).setObjects(("TCP-MIB", "tcpRtoAlgorithm"), ("TCP-MIB", "tcpRtoMin"), ("TCP-MIB", "tcpRtoMax"), ("TCP-MIB", "tcpMaxConn"), ("TCP-MIB", "tcpActiveOpens"), ("TCP-MIB", "tcpPassiveOpens"), ("TCP-MIB", "tcpAttemptFails"), ("TCP-MIB", "tcpEstabResets"), ("TCP-MIB", "tcpCurrEstab"), ("TCP-MIB", "tcpInSegs"), ("TCP-MIB", "tcpOutSegs"), ("TCP-MIB", "tcpRetransSegs"), ("TCP-MIB", "tcpConnState"), ("TCP-MIB", "tcpConnLocalAddress"), ("TCP-MIB", "tcpConnLocalPort"), ("TCP-MIB", "tcpConnRemAddress"), ("TCP-MIB", "tcpConnRemPort"), ("TCP-MIB", "tcpInErrs"), ("TCP-MIB", "tcpOutRsts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpGroup = tcpGroup.setStatus('deprecated')
if mibBuilder.loadTexts: tcpGroup.setDescription('The tcp group of objects providing for management of TCP\n            entities.')
tcpBaseGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 2)).setObjects(("TCP-MIB", "tcpRtoAlgorithm"), ("TCP-MIB", "tcpRtoMin"), ("TCP-MIB", "tcpRtoMax"), ("TCP-MIB", "tcpMaxConn"), ("TCP-MIB", "tcpActiveOpens"), ("TCP-MIB", "tcpPassiveOpens"), ("TCP-MIB", "tcpAttemptFails"), ("TCP-MIB", "tcpEstabResets"), ("TCP-MIB", "tcpCurrEstab"), ("TCP-MIB", "tcpInSegs"), ("TCP-MIB", "tcpOutSegs"), ("TCP-MIB", "tcpRetransSegs"), ("TCP-MIB", "tcpInErrs"), ("TCP-MIB", "tcpOutRsts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpBaseGroup = tcpBaseGroup.setStatus('current')
if mibBuilder.loadTexts: tcpBaseGroup.setDescription('The group of counters common to TCP entities.')
tcpConnectionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 3)).setObjects(("TCP-MIB", "tcpConnectionState"), ("TCP-MIB", "tcpConnectionProcess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpConnectionGroup = tcpConnectionGroup.setStatus('current')
if mibBuilder.loadTexts: tcpConnectionGroup.setDescription('The group provides general information about TCP\n            connections.')
tcpListenerGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 4)).setObjects(("TCP-MIB", "tcpListenerProcess"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpListenerGroup = tcpListenerGroup.setStatus('current')
if mibBuilder.loadTexts: tcpListenerGroup.setDescription('This group has objects providing general information about\n            TCP listeners.')
tcpHCGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 49, 2, 2, 5)).setObjects(("TCP-MIB", "tcpHCInSegs"), ("TCP-MIB", "tcpHCOutSegs"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    tcpHCGroup = tcpHCGroup.setStatus('current')
if mibBuilder.loadTexts: tcpHCGroup.setDescription('The group of objects providing for counters of high speed\n            TCP implementations.')
mibBuilder.exportSymbols("TCP-MIB", tcpRtoAlgorithm=tcpRtoAlgorithm, tcpConnTable=tcpConnTable, tcpListenerProcess=tcpListenerProcess, tcpMIBGroups=tcpMIBGroups, tcpListenerLocalAddress=tcpListenerLocalAddress, PYSNMP_MODULE_ID=tcpMIB, tcpConnRemAddress=tcpConnRemAddress, tcpGroup=tcpGroup, tcpConnectionLocalAddressType=tcpConnectionLocalAddressType, tcp=tcp, tcpAttemptFails=tcpAttemptFails, tcpConnRemPort=tcpConnRemPort, tcpConnectionProcess=tcpConnectionProcess, tcpEstabResets=tcpEstabResets, tcpCurrEstab=tcpCurrEstab, tcpConnectionLocalAddress=tcpConnectionLocalAddress, tcpConnEntry=tcpConnEntry, tcpConnectionGroup=tcpConnectionGroup, tcpConnectionRemAddress=tcpConnectionRemAddress, tcpMIBCompliance=tcpMIBCompliance, tcpConnectionTable=tcpConnectionTable, tcpHCInSegs=tcpHCInSegs, tcpConnectionEntry=tcpConnectionEntry, tcpListenerLocalPort=tcpListenerLocalPort, tcpConnState=tcpConnState, tcpHCOutSegs=tcpHCOutSegs, tcpListenerEntry=tcpListenerEntry, tcpInSegs=tcpInSegs, tcpRetransSegs=tcpRetransSegs, tcpConnectionRemAddressType=tcpConnectionRemAddressType, tcpBaseGroup=tcpBaseGroup, tcpRtoMax=tcpRtoMax, tcpMIB=tcpMIB, tcpRtoMin=tcpRtoMin, tcpActiveOpens=tcpActiveOpens, tcpHCGroup=tcpHCGroup, tcpMIBCompliances=tcpMIBCompliances, tcpConnectionRemPort=tcpConnectionRemPort, tcpConnLocalPort=tcpConnLocalPort, tcpMaxConn=tcpMaxConn, tcpConnectionLocalPort=tcpConnectionLocalPort, tcpInErrs=tcpInErrs, tcpConnLocalAddress=tcpConnLocalAddress, tcpMIBConformance=tcpMIBConformance, tcpConnectionState=tcpConnectionState, tcpPassiveOpens=tcpPassiveOpens, tcpMIBCompliance2=tcpMIBCompliance2, tcpListenerGroup=tcpListenerGroup, tcpListenerLocalAddressType=tcpListenerLocalAddressType, tcpListenerTable=tcpListenerTable, tcpOutSegs=tcpOutSegs, tcpOutRsts=tcpOutRsts)
