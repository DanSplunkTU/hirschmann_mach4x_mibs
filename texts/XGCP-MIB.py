#
# PySNMP MIB module XGCP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/XGCP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:49 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Counter64, Unsigned32, ModuleIdentity, Counter32, NotificationType, TimeTicks, IpAddress, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, experimental, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Unsigned32", "ModuleIdentity", "Counter32", "NotificationType", "TimeTicks", "IpAddress", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "experimental", "iso", "Gauge32")
TextualConvention, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString")
xgcpMIB = ModuleIdentity((1, 3, 6, 1, 3, 90))
xgcpMIB.setRevisions(('1999-02-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: xgcpMIB.setRevisionsDescriptions(('This is initial version of XGCP MIB.',))
if mibBuilder.loadTexts: xgcpMIB.setLastUpdated('9902170000Z')
if mibBuilder.loadTexts: xgcpMIB.setOrganization('Will submit this new XGCP-MIB to IETF-DRAFT')
if mibBuilder.loadTexts: xgcpMIB.setContactInfo('        Dinh D. Nguyen \n\n             Postal: Cisco Systems, Inc.\n                     170 West Tasman Drive\n                     San Jose, CA  95134-1706\n                     US\n\n             Phone:  +1 408 525 1624\n             Email:  dinhn@cisco.com\n\n                     Rick N. Chen \n\n             Postal: Cisco Systems, Inc.\n                     170 West Tasman Drive\n                     San Jose, CA  95134-1706\n                     US\n\n             Phone:  +1 408 525 6367\n             Email:  richen@cisco.com')
if mibBuilder.loadTexts: xgcpMIB.setDescription('The MIB module for managing XGCP implementations.')
xgcpObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1))
xgcpCoreObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1, 1))
xgcpExtensionObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1, 2))
xgcpPackageObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1, 3))
xgcpVoiceQualityObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1, 4))
xgcpDefaultMGCObjects = MibIdentifier((1, 3, 6, 1, 3, 90, 1, 5))
xgcpInBadVersions = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 1), Counter32()).setUnits('messages').setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpInBadVersions.setStatus('current')
if mibBuilder.loadTexts: xgcpInBadVersions.setDescription('The total number of incoming messages which were delivered to\n         the protocol entity and were for an unsupported protocol \n         version.\n        ')
xgcpRequestTimeOut = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpRequestTimeOut.setStatus('current')
if mibBuilder.loadTexts: xgcpRequestTimeOut.setDescription('The request timeout is used to determine the timeout value used\n         for retransmitting unacknowledged message.\n\t It is the responsibility of the requesting entity to provide\n\t suitable timeouts for all outstanding commands, and to retry\n\t commands when timeouts exceeded.\n\n\t The default value of this object is 500 milliseconds.\n    \t')
xgcpRequestRetries = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpRequestRetries.setStatus('current')
if mibBuilder.loadTexts: xgcpRequestRetries.setDescription('This object specifies the number of retries for a request that\n         exceeds timeout. \n\t It is the responsibility of the requesting entity to provide\n\t suitable timeouts for all outstanding commands, and to retry\n\t when times out.\n\n\t The default value of this object is 3.\n        ')
xgcpAdminStatus = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("gracefulDown", 3))).clone('down')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpAdminStatus.setStatus('current')
if mibBuilder.loadTexts: xgcpAdminStatus.setDescription('The desired state of the protocol entity. \n\n\t The possible admin status are:\n\t     up - bring up protocol entity administratively  \n\t     down - bring down protocol entity adiministratively \n\t     gracefulDown - gracefully shut down protocol entity \n                                 administratively. \n\n \t A graceful shutdown indicates that the protocol \n\t will be taken out of service after the restart  \n\t delay timer timeouts or all connections are torn down.\n\n         When in graceDown, the xgcpOperStatus goes from up to \n         down via shutDownInProgress. \n\n         If there is no connection or restart delay timer \n         timeouts then xgcpOperStatus moves from \n         shutDownInProgress to down.\n        ')
xgcpOperStatus = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("shutDownInProgress", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpOperStatus.setStatus('current')
if mibBuilder.loadTexts: xgcpOperStatus.setDescription("This object indicates the current operational\n         status of the protocol entity.    \n\n\t The possible operating status are:\n\t     up - protocol up \n\t     down - protocol down \n \t     shutDownInProgress - Shut down in progress.\n\n\t The operating status - shutDownInProgress indicates \n         that the Media Gateway is in a transition state from \n         up to down. This state happens when resources are in \n         the process of being cleaned up and new resource \n         can't be allocated. \n\t")
xgcpUnRecognizedPackets = MibScalar((1, 3, 6, 1, 3, 90, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpUnRecognizedPackets.setStatus('current')
if mibBuilder.loadTexts: xgcpUnRecognizedPackets.setDescription(' This refers to the count of unrecognized packets  \n          since reset.\n        ')
xgcpMsgStatTable = MibTable((1, 3, 6, 1, 3, 90, 1, 1, 7), )
if mibBuilder.loadTexts: xgcpMsgStatTable.setStatus('current')
if mibBuilder.loadTexts: xgcpMsgStatTable.setDescription('This table contains XGCP statistics information since reset.\n         XGCP statistics are kept in this table, with each \n         table entry containing the statistics of XGCP that \n         communicates with a Media Gateway Controller (MGC) at \n         a specific IP address of the MGC.\n\n         Each table entry is composed of the following information:  \n\n         1) Messages successfully received/transmitted per IP device \n         2) Messages failed to be received/transmitted per IP device\n\n\t')
xgcpMsgStatEntry = MibTableRow((1, 3, 6, 1, 3, 90, 1, 1, 7, 1), ).setIndexNames((0, "XGCP-MIB", "xgcpIPAddress"))
if mibBuilder.loadTexts: xgcpMsgStatEntry.setStatus('current')
if mibBuilder.loadTexts: xgcpMsgStatEntry.setDescription('The row of the xgcpMsgStatTable contains \n         information about XGCP message statistics per IP address\n         of the Media Gateway Controller.\n         An entry is created when a request messge with new IP \n         address is received from Medida Gateway Controller. \n         When the table is full, an entry is deleted if it is \n         LRU (Least Recently Used). \n\t')
xgcpIPAddress = MibTableColumn((1, 3, 6, 1, 3, 90, 1, 1, 7, 1, 1), IpAddress())
if mibBuilder.loadTexts: xgcpIPAddress.setStatus('current')
if mibBuilder.loadTexts: xgcpIPAddress.setDescription(' This object specifies the IP address of the  \n          Media Gateway Controller.\n        ')
xgcpSuccessMessages = MibTableColumn((1, 3, 6, 1, 3, 90, 1, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpSuccessMessages.setStatus('current')
if mibBuilder.loadTexts: xgcpSuccessMessages.setDescription('This object specifies the count of successful messages\n         that communicate with the Media Gateway Controller on \n         that IP address.\n\n         Successful messages apply to both transmit and \n         receive messages.                             \n\n           Transmit: Positive ACK is received from the Media  \n                     Gateway Controller\n\n           Receive: Positive ACK is sent to the Media Gateway \n                    Controller. This implies that the format  \n                    of the message is correct and the request\n                    can be fulfilled.\n\n        ')
xgcpFailMessages = MibTableColumn((1, 3, 6, 1, 3, 90, 1, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpFailMessages.setStatus('current')
if mibBuilder.loadTexts: xgcpFailMessages.setDescription('This object specifies the count of failed  messages\n         that communicate with the Media Gateway Controller on \n         that IP address.\n\n         Failed messages apply to both transmit and receive\n         messages. \n\n           Transmit: Either NAK is received from the MGC or message\n                     times out waiting for ACK.   \n           Receive:  Format of the received message is bad or\n                     the request can not be fulfilled.   \n        ')
xgcpRestartInProgressMWD = MibScalar((1, 3, 6, 1, 3, 90, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600000))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpRestartInProgressMWD.setReference(' Media Gateway Control Protocol (MGCP),\n           version 0.1 draft, Feb 1, 1999 : Section 4.3.4 \n         ')
if mibBuilder.loadTexts: xgcpRestartInProgressMWD.setStatus('current')
if mibBuilder.loadTexts: xgcpRestartInProgressMWD.setDescription('The maximum waiting delay (MWD) timeout value is used for the\n         Media Gateway to send the Restart In Progress to the Media  \n         Gateway Controller.\n\n         The default value of this object is chosen in an \n         implementation-dependent manner by the MGCP functionality \n         based on the call volume of the system.\n    \t')
xgcpRestartDelay = MibScalar((1, 3, 6, 1, 3, 90, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 600))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpRestartDelay.setReference(' Media Gateway Control Protocol (MGCP),\n           version 0.1 draft, Feb 1, 1999 : Section 4.3.4 \n         ')
if mibBuilder.loadTexts: xgcpRestartDelay.setStatus('current')
if mibBuilder.loadTexts: xgcpRestartDelay.setDescription('This object specifies the Restart Delay Timeout for \n         the restart process.\n         The purpose of setting the restart timer before sending\n         the Restart In Progress notification to the media gateway\n         controller is to avoid the network congestion\n         during the critical period of service restoration.\n\n\t The default value of this object is 0.\n    \t')
xgcpMGCCfgAddress = MibScalar((1, 3, 6, 1, 3, 90, 1, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpMGCCfgAddress.setStatus('current')
if mibBuilder.loadTexts: xgcpMGCCfgAddress.setDescription('This object is used to configure either the domain \n         name or the IP address of the Default Media Gateway \n         Controller in standard dot notation.     \n\n         The complete address of a default MGC is cmposed of  \n         IP address/Domain Name and UDP port.\n        \n         xgcpMGCCfgaddress specifies address of the default Media \n         Gateway Controller to which RSIP(RestartInProgress) message \n         is sent whenever system starts up or line goes up.\n\n         If DNS name is entered and the IP address is found,\n         MG will send RSIP to the desired MGC. If no IP address is  \n         found or no such DNS name exists, no RSIP will be sent.\n\n         If IP address is entered, MG will send RSIP to that address.\n\n         If there is no response, it could be that the network is down \n         or user misconfigures the address (IP address, Domain Name or\n         UDP port number)\n\t')
xgcpMGCCfgUDPPort = MibScalar((1, 3, 6, 1, 3, 90, 1, 5, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1025, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpMGCCfgUDPPort.setStatus('current')
if mibBuilder.loadTexts: xgcpMGCCfgUDPPort.setDescription('This object is used to configure the UDP port\n         of the Media Gateway Controller.\n\n         The UDP port is used together with xgcpMGCCfgAddress to  \n         specify the destination address of the default Media \n         Gateway Controller to which RSIP message is sent when\n         system starts up or line goes up.\n          \n\t')
xgcpMGCCfgConnStatus = MibScalar((1, 3, 6, 1, 3, 90, 1, 5, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("connected", 2), ("connecting", 3), ("unknownName", 4), ("noResponse", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpMGCCfgConnStatus.setStatus('current')
if mibBuilder.loadTexts: xgcpMGCCfgConnStatus.setDescription('This object is used to specify the connection status   \n         of the Default Media Gateway Controller.\n\n         When sending RSIP to default Media Gateway Controller,\n         there could be the following status:\n   \n         unknown - undefined stauts. \n         connected - RSIP sent and response to it is received.  \n         connecting -  RSIP is sent and waiting for response.\n         unknownName - no domain name/ip address is found \n                      when checking the DNS for the domain name \n                      entered in xgcpMGCCfgAddress. No RSIP \n                      message is sent.\n         noResponse - timeout on RSIP message. \n        \n\n         The possible casues for no response on RSIP message:          \n\n         1) Address(IP Address/Domain Name and UDP) for the default \n            MGC is correct but MGC in not up or network is down.\n         2) MGC is up but at a different address (IP Address/\n            Domain Name)\n         3) MGC is up and at the same address(IP address/\n            Domain Name) but wrong UDP port.\n         4) MGC is down and address is wrong. \n\t')
xgcpMGCCfgTimeStamp = MibScalar((1, 3, 6, 1, 3, 90, 1, 5, 4), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: xgcpMGCCfgTimeStamp.setStatus('current')
if mibBuilder.loadTexts: xgcpMGCCfgTimeStamp.setDescription('This object contains the time stamp of \n         state transition of xgcpMGCCfgConnStatus.\n\t')
xgcpCapabilityPackageTable = MibTable((1, 3, 6, 1, 3, 90, 1, 3, 1), )
if mibBuilder.loadTexts: xgcpCapabilityPackageTable.setStatus('current')
if mibBuilder.loadTexts: xgcpCapabilityPackageTable.setDescription('This table contains XGCP capability packages.\n         The Capability Package table - This table is \n         used to specify the availability of the packages.\n\n         The Capabality Package Name is used as the \n         index for the table.\n\n         Each entry contains a CapabilityPackageEnable \n         object. It is used to enable/disable a package \n         on the Media Gateway.  \n        ')
xgcpCapabilityPackageEntry = MibTableRow((1, 3, 6, 1, 3, 90, 1, 3, 1, 1), ).setIndexNames((1, "XGCP-MIB", "xgcpCapabilityPackageName"))
if mibBuilder.loadTexts: xgcpCapabilityPackageEntry.setStatus('current')
if mibBuilder.loadTexts: xgcpCapabilityPackageEntry.setDescription('The entry specifies the availability of the XGCP         \n         package.\n         Each entry is created when the MGCP software \n         detects a new package. The entry goes away  \n         only if the package is removed.\n        ')
xgcpCapabilityPackageName = MibTableColumn((1, 3, 6, 1, 3, 90, 1, 3, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64)))
if mibBuilder.loadTexts: xgcpCapabilityPackageName.setReference(' Media Gateway Control Protocol (MGCP),\n           version 0.1 draft, Feb 1, 1999 : Section 6.1\n         ')
if mibBuilder.loadTexts: xgcpCapabilityPackageName.setStatus('current')
if mibBuilder.loadTexts: xgcpCapabilityPackageName.setDescription(' This object specifies the Name of the\n          Capability Package. \n\n          The list of basic packages includes the following:\n\n               _________________________________________\n              | Package                      |   name  |\n              |______________________________|_________|\n              | Generic Media Package        |   G     |\n              | DTMF package                 |   D     |\n              | MF Package                   |   M     |\n              | Trunk Package                |   T     |\n              | Line Package                 |   L     |\n              | Handset Package              |   H     |\n              | RTP Package                  |   R     |\n              | Netwark Access Server Package|   N     |\n              | Announcement Server Package  |   A     |\n              | Script Package               |   S     |\n              |______________________________|_________|\n         ')
xgcpCapabilityPackageEnable = MibTableColumn((1, 3, 6, 1, 3, 90, 1, 3, 1, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpCapabilityPackageEnable.setStatus('current')
if mibBuilder.loadTexts: xgcpCapabilityPackageEnable.setDescription(' This object eables/disables the Package Capability \n        ')
xgcpDefaultPackage = MibScalar((1, 3, 6, 1, 3, 90, 1, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpDefaultPackage.setReference(' Media Gateway Control Protocol (MGCP),\n           version 0.1 draft, Feb 1, 1998 : Section 2.1.6\n         ')
if mibBuilder.loadTexts: xgcpDefaultPackage.setStatus('current')
if mibBuilder.loadTexts: xgcpDefaultPackage.setDescription(' This object contains the default package name for\n          the MGCP/SGCP protocol and it should have the\n          same value as xgcpCapabilityPackageName. \n        ')
xgcpLowerBoundForPacketLoss = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpLowerBoundForPacketLoss.setStatus('current')
if mibBuilder.loadTexts: xgcpLowerBoundForPacketLoss.setDescription('This object specifies the lower bound for voice\n         quality packet loss per 100,000 packets. Voice quality \n         packet loss may happen due to network congestion or due\n         to network overload.\n\n         When packet loss(number of packet per 100,000) is high \n         enough to reach lower bound(e.g. 1500) and then higher \n         bound(e.g. 2500) the first time, a MGCP/SGCP Notify \n         message is sent to the Media Gateway Controller. \n   \n         Subsequent hits of the higher bound results in a \n         MGCP/SGCP Notify message being sent to the Media Gateway \n         Controller only after the lower bound is hit.\n\n\n           |                Ntfy \n           |    Ntfy  Ntfy   |        Ntfy\n           |     |     |     v         |\n           |     v     v      *   *    v\n           +     * *   *     * * * *   *     <---  higher bound\n           |    *   * * *  *    *   * * *\n           +   *     *   *           *   *   <---- lower bound\n           |  *                           *\n           | *                             * \n           |*\n           +------------------------------------ \n\n\t The default value of this object is 1000.\n        ')
xgcpHigherBoundForPacketLoss = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5000, 25000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpHigherBoundForPacketLoss.setStatus('current')
if mibBuilder.loadTexts: xgcpHigherBoundForPacketLoss.setDescription('This object specifies the higher bound for voice quality \n         packet loss per 100,000 packets. Voice quality packet loss \n         may happen due to network congestion or due to network \n         overload.\n\n\t The default value of this object is 10,000.\n        ')
xgcpLowerBoundForJitter = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(4, 60))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpLowerBoundForJitter.setStatus('current')
if mibBuilder.loadTexts: xgcpLowerBoundForJitter.setDescription('This object is the lower bound for Quality Alert for \n         Jitter.\n\n         Jitter is an estimate of the statistical variance of the RTP \n         data packet interval-rival time measured in milliseconds and \n         expressed as an unsigned integer.\n\n         When jitter(milliseconds) is long enough to reach lower \n         bound(e.g.30 ) and then higher bound(e.g. 150) the first \n         time, a MGCP/SGCP Notify message is sent to the Media \n         Gateway Controller. \n   \n         Subsequent hits of the higher bound results in a \n         MGCP/SGCP Notify message being sent to the Media Gateway \n         Controller only after the lower bound is hit.\n\n\t The default value of this object is 30.\n        ')
xgcpHigherBoundForJitter = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 200))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpHigherBoundForJitter.setStatus('current')
if mibBuilder.loadTexts: xgcpHigherBoundForJitter.setDescription('This object is the higher bound for Quality Alert for \n         Jitter.\n\n         Jitter is an estimate of the statistical variance of the RTP \n         data packet interval-rival time measured in milliseconds and \n         expressed as an unsigned integer.\n\n\t The default value of this object is 150.\n        ')
xgcpLowerBoundForLatency = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(125, 200))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpLowerBoundForLatency.setStatus('current')
if mibBuilder.loadTexts: xgcpLowerBoundForLatency.setDescription('This object is the higher bound for Quality Alert for \n\t latency.  \n\n\t QA latency is an estimate of the network delay, expressed \n         in milliseconds. This is the average value of the difference \n         between the Network Time Protocol (NTP) timestamp indicated \n         by the senders of the RTCP messages and the NTP timestamp \n         of the receivers, measured when these messages are received. \n\n         When latency (milliseconds) is long enough to reach lower \n         bound (e.g.150 ) and then higher bound(e.g. 300) the first \n         time, a MGCP/SGCP Notify message is sent to the Media \n         Gateway Controller. \n   \n         Subsequent hits of the higher bound results in a \n         MGCP/SGCP Notify message being sent to the Media Gateway \n         Controller only after the lower bound is hit.\n\n\t The default value of this object is 150.\n        ')
xgcpHigherBoundForLatency = MibScalar((1, 3, 6, 1, 3, 90, 1, 4, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(250, 400))).setUnits('milliseconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: xgcpHigherBoundForLatency.setStatus('current')
if mibBuilder.loadTexts: xgcpHigherBoundForLatency.setDescription('This object is the higher bound for Quality Alert for \n\t latency.  \n\n\t QA latency is an estimate of the network delay, expressed \n         in milliseconds. This is the average value of the difference \n         between the NTP timestamp indicated by the senders of the \n\t RTCP messages and the NTP timestamp of the receivers, \n         measured when these messages are received. \n\n\n\t The default value of this object is 300.\n        ')
xgcpNotificationPrefix = MibIdentifier((1, 3, 6, 1, 3, 90, 2))
xgcpNotifications = MibIdentifier((1, 3, 6, 1, 3, 90, 2, 0))
xgcpUpDownNotification = NotificationType((1, 3, 6, 1, 3, 90, 2, 0, 1)).setObjects(("XGCP-MIB", "xgcpOperStatus"))
if mibBuilder.loadTexts: xgcpUpDownNotification.setStatus('current')
if mibBuilder.loadTexts: xgcpUpDownNotification.setDescription('This notification is sent when the protocol status changes  \n             between up and down.\n\n             The following information is returned:\n                   xgcpOperStatus -> Current operational status of XGCP \n\n\t    ')
xgcpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 90, 3))
xgcpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 90, 3, 1))
xgcpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 90, 3, 2))
xgcpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 90, 3, 1, 1)).setObjects(("XGCP-MIB", "xgcpCoreGroup"), ("XGCP-MIB", "xgcpExtensionGroup"), ("XGCP-MIB", "xgcpPackageGroup"), ("XGCP-MIB", "xgcpVoiceQualityGroup"), ("XGCP-MIB", "xgcpDefaultMGCGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpMIBCompliance = xgcpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: xgcpMIBCompliance.setDescription('The compliance statement for the SNMPv2 entities \n             which implement XGCP.')
xgcpCoreGroup = ObjectGroup((1, 3, 6, 1, 3, 90, 3, 2, 1)).setObjects(("XGCP-MIB", "xgcpInBadVersions"), ("XGCP-MIB", "xgcpRequestTimeOut"), ("XGCP-MIB", "xgcpRequestRetries"), ("XGCP-MIB", "xgcpAdminStatus"), ("XGCP-MIB", "xgcpOperStatus"), ("XGCP-MIB", "xgcpUnRecognizedPackets"), ("XGCP-MIB", "xgcpSuccessMessages"), ("XGCP-MIB", "xgcpFailMessages"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpCoreGroup = xgcpCoreGroup.setStatus('current')
if mibBuilder.loadTexts: xgcpCoreGroup.setDescription('This group contains core objects for SGCP/MGCP on the  \n             Media Gateway Controller and the Media Gateway.\n             ')
xgcpExtensionGroup = ObjectGroup((1, 3, 6, 1, 3, 90, 3, 2, 2)).setObjects(("XGCP-MIB", "xgcpRestartInProgressMWD"), ("XGCP-MIB", "xgcpRestartDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpExtensionGroup = xgcpExtensionGroup.setStatus('current')
if mibBuilder.loadTexts: xgcpExtensionGroup.setDescription('This group contains extension objects for MGCP on \n             the Media Gateway.\n             ')
xgcpPackageGroup = ObjectGroup((1, 3, 6, 1, 3, 90, 3, 2, 3)).setObjects(("XGCP-MIB", "xgcpCapabilityPackageEnable"), ("XGCP-MIB", "xgcpDefaultPackage"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpPackageGroup = xgcpPackageGroup.setStatus('current')
if mibBuilder.loadTexts: xgcpPackageGroup.setDescription('This group contains package objects for MGCP on\n             the Media Gateway or the Media Gateway Controller.\n            ')
xgcpVoiceQualityGroup = ObjectGroup((1, 3, 6, 1, 3, 90, 3, 2, 4)).setObjects(("XGCP-MIB", "xgcpLowerBoundForPacketLoss"), ("XGCP-MIB", "xgcpHigherBoundForPacketLoss"), ("XGCP-MIB", "xgcpLowerBoundForJitter"), ("XGCP-MIB", "xgcpHigherBoundForJitter"), ("XGCP-MIB", "xgcpLowerBoundForLatency"), ("XGCP-MIB", "xgcpHigherBoundForLatency"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpVoiceQualityGroup = xgcpVoiceQualityGroup.setStatus('current')
if mibBuilder.loadTexts: xgcpVoiceQualityGroup.setDescription('This group contains voice quality objects for  \n             the Media Gateway .')
xgcpDefaultMGCGroup = ObjectGroup((1, 3, 6, 1, 3, 90, 3, 2, 5)).setObjects(("XGCP-MIB", "xgcpMGCCfgAddress"), ("XGCP-MIB", "xgcpMGCCfgUDPPort"), ("XGCP-MIB", "xgcpMGCCfgConnStatus"), ("XGCP-MIB", "xgcpMGCCfgTimeStamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xgcpDefaultMGCGroup = xgcpDefaultMGCGroup.setStatus('current')
if mibBuilder.loadTexts: xgcpDefaultMGCGroup.setDescription('This group contains address objects for default \n             Media Gateway Controller.\n             ')
mibBuilder.exportSymbols("XGCP-MIB", xgcpMsgStatTable=xgcpMsgStatTable, xgcpMGCCfgAddress=xgcpMGCCfgAddress, xgcpHigherBoundForPacketLoss=xgcpHigherBoundForPacketLoss, xgcpHigherBoundForJitter=xgcpHigherBoundForJitter, xgcpMIB=xgcpMIB, xgcpLowerBoundForPacketLoss=xgcpLowerBoundForPacketLoss, xgcpIPAddress=xgcpIPAddress, xgcpInBadVersions=xgcpInBadVersions, xgcpLowerBoundForJitter=xgcpLowerBoundForJitter, xgcpDefaultMGCObjects=xgcpDefaultMGCObjects, xgcpMGCCfgTimeStamp=xgcpMGCCfgTimeStamp, xgcpAdminStatus=xgcpAdminStatus, xgcpFailMessages=xgcpFailMessages, xgcpCoreObjects=xgcpCoreObjects, xgcpCapabilityPackageTable=xgcpCapabilityPackageTable, xgcpSuccessMessages=xgcpSuccessMessages, xgcpExtensionGroup=xgcpExtensionGroup, xgcpCapabilityPackageName=xgcpCapabilityPackageName, xgcpDefaultPackage=xgcpDefaultPackage, xgcpRestartInProgressMWD=xgcpRestartInProgressMWD, xgcpVoiceQualityObjects=xgcpVoiceQualityObjects, PYSNMP_MODULE_ID=xgcpMIB, xgcpOperStatus=xgcpOperStatus, xgcpNotificationPrefix=xgcpNotificationPrefix, xgcpNotifications=xgcpNotifications, xgcpMGCCfgConnStatus=xgcpMGCCfgConnStatus, xgcpCoreGroup=xgcpCoreGroup, xgcpUpDownNotification=xgcpUpDownNotification, xgcpPackageGroup=xgcpPackageGroup, xgcpRestartDelay=xgcpRestartDelay, xgcpCapabilityPackageEnable=xgcpCapabilityPackageEnable, xgcpObjects=xgcpObjects, xgcpLowerBoundForLatency=xgcpLowerBoundForLatency, xgcpMIBCompliances=xgcpMIBCompliances, xgcpMIBConformance=xgcpMIBConformance, xgcpMIBCompliance=xgcpMIBCompliance, xgcpUnRecognizedPackets=xgcpUnRecognizedPackets, xgcpVoiceQualityGroup=xgcpVoiceQualityGroup, xgcpHigherBoundForLatency=xgcpHigherBoundForLatency, xgcpRequestRetries=xgcpRequestRetries, xgcpCapabilityPackageEntry=xgcpCapabilityPackageEntry, xgcpExtensionObjects=xgcpExtensionObjects, xgcpPackageObjects=xgcpPackageObjects, xgcpMIBGroups=xgcpMIBGroups, xgcpRequestTimeOut=xgcpRequestTimeOut, xgcpMGCCfgUDPPort=xgcpMGCCfgUDPPort, xgcpDefaultMGCGroup=xgcpDefaultMGCGroup, xgcpMsgStatEntry=xgcpMsgStatEntry)
