#
# PySNMP MIB module RAPID-IPSEC-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-IPSEC-TUNNEL-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:51 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, Gauge32, ObjectIdentity, Unsigned32, enterprises, IpAddress, Integer32, Bits, MibIdentifier, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "Gauge32", "ObjectIdentity", "Unsigned32", "enterprises", "IpAddress", "Integer32", "Bits", "MibIdentifier", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
rsInfoModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 6))
rsInfoModule.setRevisions(('2001-04-20 12:00', '2002-11-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsInfoModule.setRevisionsDescriptions(('Initial revision.', 'Changed CONTACT-INFO.',))
if mibBuilder.loadTexts: rsInfoModule.setLastUpdated('0103061200Z')
if mibBuilder.loadTexts: rsInfoModule.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: rsInfoModule.setContactInfo('   Ella Yu\n                      WatchGuard Technologies, Inc.\n                      1841 Zanker Road\n                      San Jose, CA 95112\n                      USA\n\n                      408-519-4888\n                      ella.yu@watchguard.com ')
if mibBuilder.loadTexts: rsInfoModule.setDescription('The MIB module describes various tunnel objects\n            of RapidStream system.')
rsIpsecTunnelMIB = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 5))
if mibBuilder.loadTexts: rsIpsecTunnelMIB.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelMIB.setDescription('This is the base object identifier for all tunnel\n             branches.')
rsIpsecTunnel = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1))
if mibBuilder.loadTexts: rsIpsecTunnel.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnel.setDescription('This is the base object identifier for all \n            tunnel information.')
rsIpsecTunnelNum = MibScalar((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelNum.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelNum.setDescription('The total number of entries in the rsIpsecTunnelTable. ')
rsIpsecTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2), )
if mibBuilder.loadTexts: rsIpsecTunnelTable.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelTable.setDescription('This is the connection table describing all current\n             tunnels exist on this entity.')
rsIpsecTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1), ).setIndexNames((0, "RAPID-IPSEC-TUNNEL-MIB", "rsIpsecTunnelID"))
if mibBuilder.loadTexts: rsIpsecTunnelEntry.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelEntry.setDescription('An entry (conceptual row) containing the information on a\n             tunnel between two security gateways.')
rsIpsecTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelID.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelID.setDescription('The running index of this tunnel.')
rsIpsecTunnelLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelLocalAddr.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelLocalAddr.setDescription('The local IP address of the current tunnel.')
rsIpsecTunnelPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelPeerAddr.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelPeerAddr.setDescription('The remote IP address of the current tunnel.')
rsIpsecTunnelInSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelInSpi.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelInSpi.setDescription("The security parameters index of inbound  SA's within this \n             tunnel.")
rsIpsecTunnelOutSpi = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelOutSpi.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelOutSpi.setDescription("The security parameters index of outbound  SA's within this \n            tunnel.")
rsIpsecTunnelCreateTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelCreateTime.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelCreateTime.setDescription('The date and time when the tunnel is created.')
rsIpsecTunnelDeviceID = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelDeviceID.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelDeviceID.setDescription('The identifier of target device where the SA resides.')
rsIpsecTunnelEspEncryptAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("des", 2), ("three-des", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelEspEncryptAlg.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelEspEncryptAlg.setDescription("The encryption algorithm used in the tunnel. It's 0\n            if ESP is not used.")
rsIpsecTunnelEspAuthAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("md5", 2), ("sha", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelEspAuthAlg.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelEspAuthAlg.setDescription("The authentication algorithm used in the tunnel. It's\n            0 if ESP is not used.")
rsIpsecTunnelAhAuthAlg = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("md5", 2), ("sha", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelAhAuthAlg.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelAhAuthAlg.setDescription("The AH authentication algorithm used in the tunnel.\n            It's 0 if AH is not used.")
rsIpsecTunnelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("unknown", 0), ("tunnel", 1), ("transport", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelMode.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelMode.setDescription('The tunnel/transport mode of the tunnel.')
rsIpsecTunnelKeyMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("unknown", 0), ("manual", 1), ("auto-ike", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelKeyMode.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelKeyMode.setDescription('The key mode of the tunnel.')
rsIpsecTunnelLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 13), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelLifeTime.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelLifeTime.setDescription('The life time (in hundredths of a second) of the tunnel.')
rsIpsecTunnelLifeLength = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelLifeLength.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelLifeLength.setDescription('The maximum traffic in bytes that the tunnel is allowed to support.')
rsIpsecTunnelInSaBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelInSaBytes.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelInSaBytes.setDescription('Current active inbound SA bytes of the tunnel.')
rsIpsecTunnelOutSaBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelOutSaBytes.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelOutSaBytes.setDescription('Current active outbound SA bytes of the tunnel.')
rsIpsecTunnelAccSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelAccSecs.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelAccSecs.setDescription('The number of seconds that the tunnel has existed.')
rsIpsecTunnelSelectorProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4, 6, 8, 12, 17, 22, 29, 41, 43, 44, 46, 47, 50, 51, 58, 59, 60, 92, 98, 103, 255))).clone(namedValues=NamedValues(("any", 0), ("icmp", 1), ("igmp", 2), ("ipip", 4), ("tcp", 6), ("egp", 8), ("pup", 12), ("udp", 17), ("idp", 22), ("tp", 29), ("ipv6", 41), ("ipv6-routing", 43), ("ipv6-fragmentation", 44), ("rsvp", 46), ("gre", 47), ("esp", 50), ("ah", 51), ("icmpv6", 58), ("none", 59), ("dstopts", 60), ("mtp", 92), ("encap", 98), ("pim", 103), ("raw", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelSelectorProtocol.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelSelectorProtocol.setDescription('The ip protocol number that this SA selector carries, or\n            0 if it carries any protocol.')
rsIpsecTunnelSelectorRemoteIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 19), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ip-addr-single", 1), ("ip-addr-subnet", 2), ("ip-addr-range", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelSelectorRemoteIPType.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelSelectorRemoteIPType.setDescription('The type of remote IP address of the SA selector in \n            the entity.')
rsIpsecTunnelSelectorRemoteIPOne = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 20), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelSelectorRemoteIPOne.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelSelectorRemoteIPOne.setDescription("The first remote IP address of the SA selector in the entity.\n            It's IP address if remote IP of this selector only has one address.\n            It's IP address of subnet if the remote IP of this selector is IP subnet.\n            It's the start IP address if the remote IP of this selector \n            has a range of addresses.")
rsIpsecTunnelSelectorRemoteIPTwo = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 21), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelSelectorRemoteIPTwo.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelSelectorRemoteIPTwo.setDescription("The second remote IP address of the SA selector in the entity.\n            It's 0 if remote IP of this selector only has one address.\n            It's netmask of subnet if the remote IP of this selector is IP subnet.\n            It's the end IP address if the remote IP of this selector \n            has a range of addresses.")
rsIpsecTunnelSelectorRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelSelectorRemotePort.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelSelectorRemotePort.setDescription('The remote port used by this selector in the entity.')
rsIpsecTunnelSelectorLocalIPType = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ip-addr-single", 1), ("ip-addr-subnet", 2), ("ip-addr-range", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelSelectorLocalIPType.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelSelectorLocalIPType.setDescription('The type of local IP address of the SA selector in \n            the entity.')
rsIpsecTunnelSelectorLocalIPOne = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 24), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelSelectorLocalIPOne.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelSelectorLocalIPOne.setDescription("The first local IP address of the SA selector in the entity.\n            It's IP address if local IP of this selector only has one address.\n            It's IP address of subnet if the local IP of this selector is IP subnet.\n            It's the start IP address if the local IP of this selector \n             has a range of IP addresses.")
rsIpsecTunnelSelectorLocalIPTwo = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 25), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelSelectorLocalIPTwo.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelSelectorLocalIPTwo.setDescription("The second local IP address of the SA selector in the entity.\n            It's 0 if local IP of this selector only has one address.\n            It's netmask of subnet if the local IP of this selector is IP subnet.\n            It's the end IP address if the local IP of this selector \n            has a range of IP addresses.")
rsIpsecTunnelSelectorLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 26), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelSelectorLocalPort.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelSelectorLocalPort.setDescription('The local port used by this selector in the entity.')
rsIpsecTunnelNumRekey = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelNumRekey.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelNumRekey.setDescription('The number of rekeys of the tunnel.')
rsIpsecTunnelInKbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 28), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelInKbytes.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelInKbytes.setDescription('Total inbound traffic in Kbytes since the establish of\n            this tunnel.')
rsIpsecTunnelOutKbytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 29), Counter32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelOutKbytes.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelOutKbytes.setDescription('Total outound traffic in Kbytes since the establish of\n            this connection.')
rsIpsecTunnelInPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelInPackets.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelInPackets.setDescription('Total number of inbound packets since the establish of\n            this connection.')
rsIpsecTunnelOutPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelOutPackets.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelOutPackets.setDescription('Total number of outound packets since the establish of\n            this connection.')
rsIpsecTunnelInDecryptErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelInDecryptErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelInDecryptErrors.setDescription('Total number of packets discarded due to decryption\n            error since the establish of this connection.')
rsIpsecTunnelInAuthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 33), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelInAuthErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelInAuthErrors.setDescription('Total number of packets discarded due to authentication\n            error since the establish of this connection.')
rsIpsecTunnelInReplayErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 34), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelInReplayErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelInReplayErrors.setDescription('Total number of packets discarded due to replay\n            error since the establish of this connection.')
rsIpsecTunnelInOtherErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 35), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelInOtherErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelInOtherErrors.setDescription('The number of packets discarded  due to errors\n            other than decryption, authentication or replay errors. This\n            may include packets dropped due to a lack of receive\n            buffers, and may include packets dropped due to congestion\n            at the decryption element.')
rsIpsecTunnelOutDecryptErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 36), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelOutDecryptErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelOutDecryptErrors.setDescription('Total number of packets discarded due to decryption\n            error since the establish of this connection.')
rsIpsecTunnelOutAuthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 37), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelOutAuthErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelOutAuthErrors.setDescription('Total number of packets discarded due to authentication\n            error since the establish of this connection.')
rsIpsecTunnelOutReplayErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 38), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelOutReplayErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelOutReplayErrors.setDescription('Total number of packets discarded due to replay\n            error since the establish of this connection.')
rsIpsecTunnelOutOtherErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 39), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelOutOtherErrors.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelOutOtherErrors.setDescription('The number of packets discarded due to errors\n            other than decryption, authentication or replay errors. This\n            may include packets dropped due to a lack of receive\n            buffers, and may include packets dropped due to congestion\n            at the decryption element.')
rsIpsecTunnelUdpEncap = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelUdpEncap.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelUdpEncap.setDescription('Indicates whether if UDP encapsulated IPSec has been enabled.')
rsIpsecTunnelPeerUdpPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 41), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelPeerUdpPort.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelPeerUdpPort.setDescription("The peer's UDP port of current tunnel when UDP encapsulated IPSec\n             is enabled.")
rsIpsecTunnelOrigPeerAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 6, 5, 1, 2, 1, 42), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsIpsecTunnelOrigPeerAddr.setStatus('current')
if mibBuilder.loadTexts: rsIpsecTunnelOrigPeerAddr.setDescription('The original peer ip address of current tunnel when UDP encapsulated\n             IPSec is enabled')
mibBuilder.exportSymbols("RAPID-IPSEC-TUNNEL-MIB", rsIpsecTunnelSelectorRemoteIPOne=rsIpsecTunnelSelectorRemoteIPOne, rsIpsecTunnelSelectorLocalIPTwo=rsIpsecTunnelSelectorLocalIPTwo, rsIpsecTunnelEntry=rsIpsecTunnelEntry, rsIpsecTunnelOutDecryptErrors=rsIpsecTunnelOutDecryptErrors, rsIpsecTunnelSelectorRemoteIPType=rsIpsecTunnelSelectorRemoteIPType, rsIpsecTunnelOutOtherErrors=rsIpsecTunnelOutOtherErrors, rsIpsecTunnelPeerUdpPort=rsIpsecTunnelPeerUdpPort, PYSNMP_MODULE_ID=rsInfoModule, rsIpsecTunnelSelectorLocalIPType=rsIpsecTunnelSelectorLocalIPType, rsIpsecTunnelOutSpi=rsIpsecTunnelOutSpi, rsIpsecTunnel=rsIpsecTunnel, rsIpsecTunnelLifeLength=rsIpsecTunnelLifeLength, rsIpsecTunnelSelectorLocalPort=rsIpsecTunnelSelectorLocalPort, rsIpsecTunnelInDecryptErrors=rsIpsecTunnelInDecryptErrors, rsIpsecTunnelMode=rsIpsecTunnelMode, rsIpsecTunnelInSaBytes=rsIpsecTunnelInSaBytes, rsIpsecTunnelEspEncryptAlg=rsIpsecTunnelEspEncryptAlg, rsIpsecTunnelSelectorLocalIPOne=rsIpsecTunnelSelectorLocalIPOne, rsIpsecTunnelInOtherErrors=rsIpsecTunnelInOtherErrors, rsIpsecTunnelAccSecs=rsIpsecTunnelAccSecs, rsIpsecTunnelOutSaBytes=rsIpsecTunnelOutSaBytes, rsInfoModule=rsInfoModule, rsIpsecTunnelOutKbytes=rsIpsecTunnelOutKbytes, rsIpsecTunnelOutReplayErrors=rsIpsecTunnelOutReplayErrors, rsIpsecTunnelInSpi=rsIpsecTunnelInSpi, rsIpsecTunnelLocalAddr=rsIpsecTunnelLocalAddr, rsIpsecTunnelInPackets=rsIpsecTunnelInPackets, rsIpsecTunnelSelectorRemoteIPTwo=rsIpsecTunnelSelectorRemoteIPTwo, rsIpsecTunnelMIB=rsIpsecTunnelMIB, rsIpsecTunnelKeyMode=rsIpsecTunnelKeyMode, rsIpsecTunnelTable=rsIpsecTunnelTable, rsIpsecTunnelID=rsIpsecTunnelID, rsIpsecTunnelOutPackets=rsIpsecTunnelOutPackets, rsIpsecTunnelInAuthErrors=rsIpsecTunnelInAuthErrors, rsIpsecTunnelInReplayErrors=rsIpsecTunnelInReplayErrors, rsIpsecTunnelUdpEncap=rsIpsecTunnelUdpEncap, rsIpsecTunnelPeerAddr=rsIpsecTunnelPeerAddr, rsIpsecTunnelAhAuthAlg=rsIpsecTunnelAhAuthAlg, rsIpsecTunnelOrigPeerAddr=rsIpsecTunnelOrigPeerAddr, rsIpsecTunnelOutAuthErrors=rsIpsecTunnelOutAuthErrors, rsIpsecTunnelCreateTime=rsIpsecTunnelCreateTime, rsIpsecTunnelEspAuthAlg=rsIpsecTunnelEspAuthAlg, rsIpsecTunnelInKbytes=rsIpsecTunnelInKbytes, rsIpsecTunnelDeviceID=rsIpsecTunnelDeviceID, rsIpsecTunnelSelectorRemotePort=rsIpsecTunnelSelectorRemotePort, rsIpsecTunnelNumRekey=rsIpsecTunnelNumRekey, rsIpsecTunnelNum=rsIpsecTunnelNum, rsIpsecTunnelSelectorProtocol=rsIpsecTunnelSelectorProtocol, rsIpsecTunnelLifeTime=rsIpsecTunnelLifeTime)
