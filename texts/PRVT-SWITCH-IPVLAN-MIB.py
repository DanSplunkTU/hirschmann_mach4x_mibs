#
# PySNMP MIB module PRVT-SWITCH-IPVLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-SWITCH-IPVLAN-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:48 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ipSwitch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "ipSwitch")
dot1qVlanIndex, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, IpAddress, Integer32, Counter32, Bits, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, TimeTicks, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "IpAddress", "Integer32", "Counter32", "Bits", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "TimeTicks", "NotificationType", "Unsigned32")
MacAddress, TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
prvtSwitchIpVLANMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 2))
prvtSwitchIpVLANMib.setRevisions(('2008-01-01 00:00', '2006-11-03 09:59', '2005-02-16 09:59', '2000-11-24 09:59',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtSwitchIpVLANMib.setRevisionsDescriptions(('Removed redefined OIDs in private vendor extension definitions.', 'Fixed Some generic object declarations (ACCESS to MAX-ACCESS)\nStatus set to current\nadded table for loopback interfaces', 'Fixed syntax errors and updated the contact info.', 'Initial version.',))
if mibBuilder.loadTexts: prvtSwitchIpVLANMib.setLastUpdated('200801010000Z')
if mibBuilder.loadTexts: prvtSwitchIpVLANMib.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtSwitchIpVLANMib.setContactInfo('BATM/Telco Systems Support team\n\t\t\t\tEmail: \n\t\t\t\tFor North America: techsupport@telco.com\n\t\t\t\tFor North Europe: support@batm.de, info@batm.de\n\t\t\t\tFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtSwitchIpVLANMib.setDescription('The IpVLAN MIB module that controls the assignment of IP subnets \n        to VLANs in L3 switches.')
ipInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1))
ipVLAN = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2))
ipInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1), )
if mibBuilder.loadTexts: ipInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: ipInterfaceTable.setDescription('This table controls the creation of IP interfaces (subnets).')
ipInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1), ).setIndexNames((0, "PRVT-SWITCH-IPVLAN-MIB", "ipInterfaceName"))
if mibBuilder.loadTexts: ipInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: ipInterfaceEntry.setDescription('')
ipInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipInterfaceName.setStatus('current')
if mibBuilder.loadTexts: ipInterfaceName.setDescription('This object identifies the name of the IP interface, serves as an \n        index to this table name, and can only be changed during row creation. \n        The name is the integer part of the interface name; sw1 will be 1, sw5 \n        will be 5 etc..')
ipInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: ipInterfaceIndex.setDescription('This object identifies the index of the IP interface. \n        This is the same index as ipAdEntIfIndex from MIB-II (ipAddrTable).')
ipInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pseudoInterface", 1), ("ipInterface", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipInterfaceType.setStatus('current')
if mibBuilder.loadTexts: ipInterfaceType.setDescription('This indicates a status of the IP interface. The value of this object \n        is determined by the IP address. If the IP address field is \n        empty (0.0.0.0) then this interface becomes a pseudo interface.')
ipInterfaceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipInterfaceIpAddress.setStatus('current')
if mibBuilder.loadTexts: ipInterfaceIpAddress.setDescription('This object has the value of the switch IP address in this subnet. \n\t    A value of 0.0.0.0 will make this interface a pseudo interface.')
ipInterfaceSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipInterfaceSubnetMask.setStatus('current')
if mibBuilder.loadTexts: ipInterfaceSubnetMask.setDescription('This object together with ipInterfaceIpAddress forms the IP \n\t    subnet, assigned to this IP interface. In case that ipInterfaceIpAddress \n\t    has the value of 0.0.0.0, this object will be ignored.')
ipInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 1, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: ipInterfaceRowStatus.setDescription('This object indicates that the row status, and enables the creation & \n\t    deletion of rows in this table. See SNMPv2-TC for more information.')
ipLoInterfaceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2), )
if mibBuilder.loadTexts: ipLoInterfaceTable.setStatus('current')
if mibBuilder.loadTexts: ipLoInterfaceTable.setDescription('This table controls the creation of IP LoopBack interfaces.')
ipLoInterfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1), ).setIndexNames((0, "PRVT-SWITCH-IPVLAN-MIB", "ipLoInterfaceName"))
if mibBuilder.loadTexts: ipLoInterfaceEntry.setStatus('current')
if mibBuilder.loadTexts: ipLoInterfaceEntry.setDescription('')
ipLoInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipLoInterfaceName.setStatus('current')
if mibBuilder.loadTexts: ipLoInterfaceName.setDescription('This object identifies the name of the IP interface, serves as an \n        index to this table name, and can only be changed during row creation. \n        The name is the integer part of the interface name; lo1 will be 1, lo5 \n        will be 5 etc..')
ipLoInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipLoInterfaceIndex.setStatus('current')
if mibBuilder.loadTexts: ipLoInterfaceIndex.setDescription('This object identifies the index of the IP interface. \n        This is the same index as ipAdEntIfIndex from MIB-II (ipAddrTable).')
ipLoInterfaceType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pseudoInterface", 1), ("ipInterface", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipLoInterfaceType.setStatus('current')
if mibBuilder.loadTexts: ipLoInterfaceType.setDescription('This indicates a status of the IP interface. The value of this object \n        is determined by the IP address. If the IP address field is \n        empty (0.0.0.0) then this interface becomes a pseudo interface.')
ipLoInterfaceIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 4), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipLoInterfaceIpAddress.setStatus('current')
if mibBuilder.loadTexts: ipLoInterfaceIpAddress.setDescription('This object has the value of the switch IP address in this subnet. \n\t    A value of 0.0.0.0 will make this interface a pseudo interface.')
ipLoInterfaceSubnetMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 5), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipLoInterfaceSubnetMask.setStatus('current')
if mibBuilder.loadTexts: ipLoInterfaceSubnetMask.setDescription('This object together with ipInterfaceIpAddress forms the IP \n\t    subnet, assigned to this IP interface. In case that ipInterfaceIpAddress \n\t    has the value of 0.0.0.0, this object will be ignored.')
ipLoInterfaceRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipLoInterfaceRowStatus.setStatus('current')
if mibBuilder.loadTexts: ipLoInterfaceRowStatus.setDescription('This object indicates that the row status, and enables the creation & \n\t    deletion of rows in this table. See SNMPv2-TC for more information.')
ipVLANTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 1), )
if mibBuilder.loadTexts: ipVLANTable.setStatus('current')
if mibBuilder.loadTexts: ipVLANTable.setDescription('This table extends the table dot1qVlanStaticTable from Q-BRIDGE-MIB. \n        It gives a connection between the IP Interface & the IP VLAN.')
ipVLANEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 1, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"), (0, "PRVT-SWITCH-IPVLAN-MIB", "ipInterfaceName"))
if mibBuilder.loadTexts: ipVLANEntry.setStatus('current')
if mibBuilder.loadTexts: ipVLANEntry.setDescription('')
ipVLANStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("attached", 1), ("detached", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipVLANStatus.setStatus('current')
if mibBuilder.loadTexts: ipVLANStatus.setDescription('This object shows the VLAN on which the interface in the index \n\t    of the entry is installed and vice versa. See SNMPv2-TC for \n\t    more information.')
ipPortMappingTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 2), )
if mibBuilder.loadTexts: ipPortMappingTable.setStatus('current')
if mibBuilder.loadTexts: ipPortMappingTable.setDescription('This table serves to map physical ports to SW interfaces in their 1:1 relationship. \n        This means that we can map only one SW interface on a ')
ipPortMappingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: ipPortMappingEntry.setStatus('current')
if mibBuilder.loadTexts: ipPortMappingEntry.setDescription('')
ipPortSwIface = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 2, 2, 2, 1, 1), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ipPortSwIface.setStatus('current')
if mibBuilder.loadTexts: ipPortSwIface.setDescription('This object shows the SW interfaces to which a particular port is mapped. If we\n\t    want to detach the port and delete the mapping we need to set the value 256 which \n\t    is an invalid index for a SW interface.')
mibBuilder.exportSymbols("PRVT-SWITCH-IPVLAN-MIB", ipLoInterfaceName=ipLoInterfaceName, ipInterfaceIpAddress=ipInterfaceIpAddress, ipLoInterfaceIndex=ipLoInterfaceIndex, ipLoInterfaceSubnetMask=ipLoInterfaceSubnetMask, ipPortMappingEntry=ipPortMappingEntry, ipPortMappingTable=ipPortMappingTable, ipVLANTable=ipVLANTable, ipInterfaceType=ipInterfaceType, ipInterface=ipInterface, ipInterfaceSubnetMask=ipInterfaceSubnetMask, ipVLAN=ipVLAN, ipLoInterfaceIpAddress=ipLoInterfaceIpAddress, ipLoInterfaceRowStatus=ipLoInterfaceRowStatus, ipPortSwIface=ipPortSwIface, ipInterfaceEntry=ipInterfaceEntry, ipInterfaceIndex=ipInterfaceIndex, ipInterfaceName=ipInterfaceName, prvtSwitchIpVLANMib=prvtSwitchIpVLANMib, ipLoInterfaceEntry=ipLoInterfaceEntry, ipVLANEntry=ipVLANEntry, ipInterfaceRowStatus=ipInterfaceRowStatus, ipVLANStatus=ipVLANStatus, ipLoInterfaceTable=ipLoInterfaceTable, ipLoInterfaceType=ipLoInterfaceType, PYSNMP_MODULE_ID=prvtSwitchIpVLANMib, ipInterfaceTable=ipInterfaceTable)
