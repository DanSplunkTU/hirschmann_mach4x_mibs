#
# PySNMP MIB module AT-DHCPSN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-DHCPSN-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:44:43 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Unsigned32, TimeTicks, Gauge32, MibIdentifier, Integer32, Counter64, Counter32, ModuleIdentity, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Unsigned32", "TimeTicks", "Gauge32", "MibIdentifier", "Integer32", "Counter64", "Counter32", "ModuleIdentity", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
atDhcpsn = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537))
atDhcpsn.setRevisions(('2010-09-07 00:00', '2010-06-14 04:45', '2010-02-09 01:30', '2009-12-10 01:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atDhcpsn.setRevisionsDescriptions(('Generic syntax tidy up', 'MIB revision history dates in descriptions updated.', 'This MIB file contains definitions of managed objects for DHCP\n                Snooping in AlliedWare Plus.', 'Initial Revision',))
if mibBuilder.loadTexts: atDhcpsn.setLastUpdated('201009070000Z')
if mibBuilder.loadTexts: atDhcpsn.setOrganization('Allied Telesis, Inc')
if mibBuilder.loadTexts: atDhcpsn.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atDhcpsn.setDescription('Added two more violation types for DHCP Snooping.')
atDhcpsnEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 0))
atDhcpsnTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 0, 1)).setObjects(("AT-DHCPSN-MIB", "atDhcpsnIfIndex"), ("AT-DHCPSN-MIB", "atDhcpsnVid"), ("AT-DHCPSN-MIB", "atDhcpsnSmac"), ("AT-DHCPSN-MIB", "atDhcpsnOpcode"), ("AT-DHCPSN-MIB", "atDhcpsnCiaddr"), ("AT-DHCPSN-MIB", "atDhcpsnYiaddr"), ("AT-DHCPSN-MIB", "atDhcpsnGiaddr"), ("AT-DHCPSN-MIB", "atDhcpsnSiaddr"), ("AT-DHCPSN-MIB", "atDhcpsnChaddr"), ("AT-DHCPSN-MIB", "atDhcpsnVioType"))
if mibBuilder.loadTexts: atDhcpsnTrap.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnTrap.setDescription('DHCP Snooping violation trap.')
atArpsecTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 0, 2)).setObjects(("AT-DHCPSN-MIB", "atArpsecIfIndex"), ("AT-DHCPSN-MIB", "atArpsecClientIP"), ("AT-DHCPSN-MIB", "atArpsecSrcMac"), ("AT-DHCPSN-MIB", "atArpsecVid"), ("AT-DHCPSN-MIB", "atArpsecVioType"))
if mibBuilder.loadTexts: atArpsecTrap.setStatus('current')
if mibBuilder.loadTexts: atArpsecTrap.setDescription('DHCP Snooping ARP Security violation trap.')
atDhcpsnVariablesTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1), )
if mibBuilder.loadTexts: atDhcpsnVariablesTable.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnVariablesTable.setDescription('This table contains rows of DHCP Snooping information.')
atDhcpsnVariablesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1), ).setIndexNames((0, "AT-DHCPSN-MIB", "atDhcpsnIfIndex"))
if mibBuilder.loadTexts: atDhcpsnVariablesEntry.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnVariablesEntry.setDescription('A set of parameters that describe the DHCP Snooping features.')
atDhcpsnIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnIfIndex.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnIfIndex.setDescription('Ifindex of the port that the packet was received on.')
atDhcpsnVid = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnVid.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnVid.setDescription('VLAN ID of the port that the packet was received on.')
atDhcpsnSmac = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnSmac.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnSmac.setDescription('Source MAC address of the packet that caused the trap.')
atDhcpsnOpcode = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bootpRequest", 1), ("bootpReply", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnOpcode.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnOpcode.setDescription('Opcode value of the BOOTP packet that caused the trap. Only\n                bootpRequest(1) or bootpReply(2) is valid.')
atDhcpsnCiaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnCiaddr.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnCiaddr.setDescription('Ciaddr value of the BOOTP packet that caused the trap.')
atDhcpsnYiaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnYiaddr.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnYiaddr.setDescription('Yiaddr value of the BOOTP packet that caused the trap.')
atDhcpsnGiaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnGiaddr.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnGiaddr.setDescription('Giaddr value of the BOOTP packet that caused the trap.')
atDhcpsnSiaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnSiaddr.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnSiaddr.setDescription('Siaddr value of the BOOTP packet that caused the trap.')
atDhcpsnChaddr = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnChaddr.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnChaddr.setDescription('Chaddr value of the BOOTP packet that caused the trap.')
atDhcpsnVioType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("invalidBootp", 1), ("invalidDhcpAck", 2), ("invalidDhcpRelDec", 3), ("invalidIp", 4), ("maxBindExceeded", 5), ("opt82InsertErr", 6), ("opt82RxInvalid", 7), ("opt82RxUntrusted", 8), ("opt82TxUntrusted", 9), ("replyRxUntrusted", 10), ("srcMacChaddrMismatch", 11), ("staticEntryExisted", 12), ("dbAddErr", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atDhcpsnVioType.setStatus('current')
if mibBuilder.loadTexts: atDhcpsnVioType.setDescription('The reason that the trap was generated. invalidBootp(1) indicates\n                that the received BOOTP packet was invalid. For example, it is\n                neither BootpRequest nor BootpReply. invalidDhcpAck(2) indicates\n                that the received DHCP ACK was invalid. invalidDhcpRelDec(3) indicates\n                the DHCP Release or Decline was invalid. invalidIp(4) indicates\n                that the received IP packet was invalid. maxBindExceeded(5) indicates\n                that if the entry was added, the maximum bindings configured for\n                the port would be exceeded. opt82InsertErr(6) indicates that the\n                insertion of Option 82 failed. opt82RxInvalid(7) indicates that\n                the received Option 82 information was invalid. opt82RxUntrusted(8)\n                indicates that Option 82 information was received on an untrusted\n                port. opt82TxUntrusted(9) indicates that Option 82 would have been\n                transmitted out an untrusted port. replyRxUntrusted(10) indicates\n                that a BOOTP Reply was received on an untrusted port.\n                srcMacChaddrMismatch(11) indicates that the source MAC address of\n                the packet did not match the BOOTP CHADDR of the packet.\n                staticEntryExisted(12) indicates that the static entry to be added\n                already exists. dbAddErr(13) indicates that adding an entry to the\n                database failed.')
atArpsecVariablesTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2), )
if mibBuilder.loadTexts: atArpsecVariablesTable.setStatus('current')
if mibBuilder.loadTexts: atArpsecVariablesTable.setDescription('This table contains rows of DHCP Snooping ARP Security information.')
atArpsecVariablesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1), ).setIndexNames((0, "AT-DHCPSN-MIB", "atArpsecIfIndex"))
if mibBuilder.loadTexts: atArpsecVariablesEntry.setStatus('current')
if mibBuilder.loadTexts: atArpsecVariablesEntry.setDescription('A set of parameters that describe the DHCP Snooping ARP Security features.')
atArpsecIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atArpsecIfIndex.setStatus('current')
if mibBuilder.loadTexts: atArpsecIfIndex.setDescription('Ifindex of the port that the ARP packet was received on.')
atArpsecClientIP = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atArpsecClientIP.setStatus('current')
if mibBuilder.loadTexts: atArpsecClientIP.setDescription('Source IP address of the ARP packet.')
atArpsecSrcMac = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atArpsecSrcMac.setStatus('current')
if mibBuilder.loadTexts: atArpsecSrcMac.setDescription('Source MAC address of the ARP packet.')
atArpsecVid = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atArpsecVid.setStatus('current')
if mibBuilder.loadTexts: atArpsecVid.setDescription('VLAN ID of the port that the ARP packet was received on.')
atArpsecVioType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 537, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("srcIpNotFound", 1), ("badVLAN", 2), ("badPort", 3), ("srcIpNotAllocated", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atArpsecVioType.setStatus('current')
if mibBuilder.loadTexts: atArpsecVioType.setDescription('The reason that the trap was generated. srcIpNotFound(1) indicates\n                that the Sender IP address of the ARP packet was not found in the\n                DHCP Snooping database. badVLAN(2) indicates that the VLAN of the\n                DHCP Snooping binding entry associated with the Sender IP address\n                of the ARP packet does not match the VLAN that the ARP packet was\n                received on. badPort(3) indicates that the port of the DHCP\n                Snooping binding entry associated with the Sender IP address of the\n                ARP packet does not match the port that the ARP packet was received\n                on. srcIpNotAllocated(4) indicates that the CHADDR of the DHCP\n                Snooping binding entry associated with the Sender IP address of\n                the ARP packet does not match the Source MAC and/or the ARP source\n                MAC of the ARP packet.')
mibBuilder.exportSymbols("AT-DHCPSN-MIB", PYSNMP_MODULE_ID=atDhcpsn, atDhcpsnSiaddr=atDhcpsnSiaddr, atDhcpsnVioType=atDhcpsnVioType, atArpsecTrap=atArpsecTrap, atDhcpsnOpcode=atDhcpsnOpcode, atArpsecIfIndex=atArpsecIfIndex, atArpsecSrcMac=atArpsecSrcMac, atDhcpsn=atDhcpsn, atArpsecVioType=atArpsecVioType, atDhcpsnSmac=atDhcpsnSmac, atDhcpsnEvents=atDhcpsnEvents, atDhcpsnYiaddr=atDhcpsnYiaddr, atArpsecClientIP=atArpsecClientIP, atDhcpsnIfIndex=atDhcpsnIfIndex, atDhcpsnVariablesTable=atDhcpsnVariablesTable, atArpsecVariablesTable=atArpsecVariablesTable, atDhcpsnTrap=atDhcpsnTrap, atDhcpsnCiaddr=atDhcpsnCiaddr, atDhcpsnChaddr=atDhcpsnChaddr, atDhcpsnVid=atDhcpsnVid, atArpsecVid=atArpsecVid, atArpsecVariablesEntry=atArpsecVariablesEntry, atDhcpsnVariablesEntry=atDhcpsnVariablesEntry, atDhcpsnGiaddr=atDhcpsnGiaddr)
