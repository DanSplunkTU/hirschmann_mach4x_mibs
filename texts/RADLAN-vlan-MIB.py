#
# PySNMP MIB module RADLAN-vlan-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-vlan-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:20 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PortList, VlanIndex, dot1qVlanIndex = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "VlanIndex", "dot1qVlanIndex")
rnd, rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("RADLAN-MIB", "rnd", "rndErrorSeverity", "rndErrorDesc")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, Bits, IpAddress, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Gauge32, Counter32, iso, TimeTicks, MibIdentifier, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "Bits", "IpAddress", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Gauge32", "Counter32", "iso", "TimeTicks", "MibIdentifier", "Counter64")
RowStatus, TextualConvention, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "MacAddress", "DisplayString", "TruthValue")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
vlan = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 48))
vlan.setRevisions(('2004-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vlan.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: vlan.setLastUpdated('200404190000Z')
if mibBuilder.loadTexts: vlan.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: vlan.setContactInfo('radlan.com')
if mibBuilder.loadTexts: vlan.setDescription('The private MIB module definition for IP Multicast support in Radlan devices.')
vlanMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 48, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanMibVersion.setStatus('current')
if mibBuilder.loadTexts: vlanMibVersion.setDescription("MIB's version :\n           Version 2: the current VLAN MIB replaced the previous one;\n           Version 3: field vlanPortForbiddenEgressPort was added.\n           Version 4: dot1q and dot1v supported\n           Version 5: Private Edge Vlan\n                        vlanPrivateEdgeSupported\n                        vlanPrivateEdgeMibVersion\n                        vlanPrivateEdgeTable")
vlanMaxTableNumber = MibScalar((1, 3, 6, 1, 4, 1, 89, 48, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanMaxTableNumber.setStatus('current')
if mibBuilder.loadTexts: vlanMaxTableNumber.setDescription('Maximum number of VLAN Tables supported by the device.')
vlanNameTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 21), )
if mibBuilder.loadTexts: vlanNameTable.setStatus('current')
if mibBuilder.loadTexts: vlanNameTable.setDescription("This table translates Vlan name to Vlan's tag and ifindex")
vlanNameEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 21, 1), ).setIndexNames((0, "RADLAN-vlan-MIB", "vlanNameName"))
if mibBuilder.loadTexts: vlanNameEntry.setStatus('current')
if mibBuilder.loadTexts: vlanNameEntry.setDescription('The row definition for this table.')
vlanNameName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 21, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameName.setStatus('current')
if mibBuilder.loadTexts: vlanNameName.setDescription("The Vlan's name")
vlanNameTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 21, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameTag.setStatus('current')
if mibBuilder.loadTexts: vlanNameTag.setDescription("The Vlan's tag")
vlanNameIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 21, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanNameIfIndex.setStatus('current')
if mibBuilder.loadTexts: vlanNameIfIndex.setDescription("The Vlan's ifindex")
vlanPortModeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 22), )
if mibBuilder.loadTexts: vlanPortModeTable.setStatus('current')
if mibBuilder.loadTexts: vlanPortModeTable.setDescription('This table hold information on port status trunk or access')
vlanPortModeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 22, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vlanPortModeEntry.setStatus('current')
if mibBuilder.loadTexts: vlanPortModeEntry.setDescription('The row definition for this table.')
vlanPortModeState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 22, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPortModeState.setStatus('current')
if mibBuilder.loadTexts: vlanPortModeState.setDescription('The port state, 1 is generic cli')
vlanSendUnknownToAllPorts = MibScalar((1, 3, 6, 1, 4, 1, 89, 48, 27), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSendUnknownToAllPorts.setStatus('current')
if mibBuilder.loadTexts: vlanSendUnknownToAllPorts.setDescription('If a value of the parameter is true a frame with unknown\n         destination MAC address sent by the Layer 3 to a VLAN will be\n         sent to all ports of the VLAN.\n         If a value of the parameter is false a frame with unknown\n         destination MAC address sent by the Layer 3 to a VLAN will be\n         discarded.')
vlanDefaultSupported = MibScalar((1, 3, 6, 1, 4, 1, 89, 48, 29), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanDefaultSupported.setStatus('current')
if mibBuilder.loadTexts: vlanDefaultSupported.setDescription('supported or not default vlan.')
vlanDot1vSupported = MibScalar((1, 3, 6, 1, 4, 1, 89, 48, 31), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanDot1vSupported.setStatus('current')
if mibBuilder.loadTexts: vlanDot1vSupported.setDescription('802.1v standard for vlan per port and protocol.')
vlanDefaultEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 48, 32), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDefaultEnabled.setStatus('current')
if mibBuilder.loadTexts: vlanDefaultEnabled.setDescription('if supported default vlan , indicate enabled or disabled')
vlanSpecialTagTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 33), )
if mibBuilder.loadTexts: vlanSpecialTagTable.setStatus('current')
if mibBuilder.loadTexts: vlanSpecialTagTable.setDescription('special vlan tag used for this port')
vlanSpecialTagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 33, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vlanSpecialTagEntry.setStatus('current')
if mibBuilder.loadTexts: vlanSpecialTagEntry.setDescription(' entry of special tag')
vlanSpecialTagVID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 33, 1, 1), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpecialTagVID.setStatus('current')
if mibBuilder.loadTexts: vlanSpecialTagVID.setDescription('specify the special vlan tag .')
vlanSpecialTagStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 33, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpecialTagStatus.setStatus('current')
if mibBuilder.loadTexts: vlanSpecialTagStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
vlanSpecialTagCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 34), )
if mibBuilder.loadTexts: vlanSpecialTagCurrentTable.setStatus('current')
if mibBuilder.loadTexts: vlanSpecialTagCurrentTable.setDescription('special Current vlan tag used for this port')
vlanSpecialTagCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 34, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vlanSpecialTagCurrentEntry.setStatus('current')
if mibBuilder.loadTexts: vlanSpecialTagCurrentEntry.setDescription(' entry of Current special tag')
vlanSpecialTagCurrentVID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 34, 1, 1), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpecialTagCurrentVID.setStatus('current')
if mibBuilder.loadTexts: vlanSpecialTagCurrentVID.setDescription('specify the special vlan tag .')
vlanSpecialTagCurrentReserved = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 34, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpecialTagCurrentReserved.setStatus('current')
if mibBuilder.loadTexts: vlanSpecialTagCurrentReserved.setDescription('specify if the special vlan tag is reserved .')
vlanSpecialTagCurrentActive = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 34, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpecialTagCurrentActive.setStatus('current')
if mibBuilder.loadTexts: vlanSpecialTagCurrentActive.setDescription('specify if the special vlan tag is used .')
vlanPrivateEdgeSupported = MibScalar((1, 3, 6, 1, 4, 1, 89, 48, 35), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPrivateEdgeSupported.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeSupported.setDescription('is private edge supported.')
vlanPrivateEdgeVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 48, 36), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPrivateEdgeVersion.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeVersion.setDescription('private edge version.')
vlanPrivateEdgeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 37), )
if mibBuilder.loadTexts: vlanPrivateEdgeTable.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeTable.setDescription('table for pve port and uplink')
vlanPrivateEdgeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 37, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vlanPrivateEdgeEntry.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeEntry.setDescription(' entry of pve')
vlanPrivateEdgeUplink = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 37, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPrivateEdgeUplink.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeUplink.setDescription('specify the uplink port.')
vlanPrivateEdgeStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 37, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPrivateEdgeStatus.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
vlanDynamicVlanSupported = MibScalar((1, 3, 6, 1, 4, 1, 89, 48, 38), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanDynamicVlanSupported.setStatus('current')
if mibBuilder.loadTexts: vlanDynamicVlanSupported.setDescription('is DynamicVlanVlan supported.')
vlanDynamicVlanTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 39), )
if mibBuilder.loadTexts: vlanDynamicVlanTable.setStatus('current')
if mibBuilder.loadTexts: vlanDynamicVlanTable.setDescription('table for DynamicVlan')
vlanDynamicVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 39, 1), ).setIndexNames((0, "RADLAN-vlan-MIB", "vlanDynamicVlanMacAddress"))
if mibBuilder.loadTexts: vlanDynamicVlanEntry.setStatus('current')
if mibBuilder.loadTexts: vlanDynamicVlanEntry.setDescription(' entry of DynamicVlan')
vlanDynamicVlanMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 39, 1, 1), MacAddress())
if mibBuilder.loadTexts: vlanDynamicVlanMacAddress.setStatus('current')
if mibBuilder.loadTexts: vlanDynamicVlanMacAddress.setDescription('mac address ')
vlanDynamicVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 39, 1, 2), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDynamicVlanTag.setStatus('current')
if mibBuilder.loadTexts: vlanDynamicVlanTag.setDescription('vlan Tag')
vlanDynamicVlanStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 39, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanDynamicVlanStatus.setStatus('current')
if mibBuilder.loadTexts: vlanDynamicVlanStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
vlanPortModeExtTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 40), )
if mibBuilder.loadTexts: vlanPortModeExtTable.setStatus('current')
if mibBuilder.loadTexts: vlanPortModeExtTable.setDescription('This table hold information on port status trunk or access')
vlanPortModeExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 40, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vlanPortModeExtEntry.setStatus('current')
if mibBuilder.loadTexts: vlanPortModeExtEntry.setDescription('The row definition for this table.')
vlanPortModeExtState = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 40, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPortModeExtState.setStatus('current')
if mibBuilder.loadTexts: vlanPortModeExtState.setDescription('The ext')
vlanPortModeExtStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 40, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPortModeExtStatus.setStatus('current')
if mibBuilder.loadTexts: vlanPortModeExtStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
vlanPrivateSupported = MibScalar((1, 3, 6, 1, 4, 1, 89, 48, 41), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPrivateSupported.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateSupported.setDescription('is private vlan supported.')
vlanPrivateTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 42), )
if mibBuilder.loadTexts: vlanPrivateTable.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateTable.setDescription('table for PrivateVlan')
vlanPrivateEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 42, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: vlanPrivateEntry.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEntry.setDescription(' entry of PrivateVlan')
vlanPrivateIsolatedVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 42, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPrivateIsolatedVlanTag.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateIsolatedVlanTag.setDescription('vlan Tag')
vlanPrivateStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 42, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPrivateStatus.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
vlanPrivateCommunityTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 43), )
if mibBuilder.loadTexts: vlanPrivateCommunityTable.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateCommunityTable.setDescription('table for PrivateVlan')
vlanPrivateCommunityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 43, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"), (0, "RADLAN-vlan-MIB", "vlanPrivateCommunityVlanTag"))
if mibBuilder.loadTexts: vlanPrivateCommunityEntry.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateCommunityEntry.setDescription(' entry of PrivateVlan')
vlanPrivateCommunityVlanTag = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 43, 1, 1), VlanIndex())
if mibBuilder.loadTexts: vlanPrivateCommunityVlanTag.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateCommunityVlanTag.setDescription('vlan Tag')
vlanPrivateCommunityStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 43, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPrivateCommunityStatus.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateCommunityStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
vlanMulticastTvTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 44), )
if mibBuilder.loadTexts: vlanMulticastTvTable.setStatus('current')
if mibBuilder.loadTexts: vlanMulticastTvTable.setDescription(' multicast vlan used for this port')
vlanMulticastTvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 44, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vlanMulticastTvEntry.setStatus('current')
if mibBuilder.loadTexts: vlanMulticastTvEntry.setDescription(' entry of multicast tag')
vlanMulticastTvVID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 44, 1, 1), VlanIndex()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanMulticastTvVID.setStatus('current')
if mibBuilder.loadTexts: vlanMulticastTvVID.setDescription('specify the TV vlan tag, vlan must exist .')
vlanMulticastTvStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 44, 1, 2), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanMulticastTvStatus.setStatus('current')
if mibBuilder.loadTexts: vlanMulticastTvStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
vlanMacBaseVlanGroupTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 45), )
if mibBuilder.loadTexts: vlanMacBaseVlanGroupTable.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanGroupTable.setDescription('A table that contains mappings from Range of MAC\n         addresses to Group Identifiers used for\n         MAC-based VLAN Classification.')
vlanMacBaseVlanGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 45, 1), ).setIndexNames((0, "RADLAN-vlan-MIB", "vlanMacBaseVlanMacAddress"), (0, "RADLAN-vlan-MIB", "vlanMacBaseVlanMacMask"))
if mibBuilder.loadTexts: vlanMacBaseVlanGroupEntry.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanGroupEntry.setDescription('A mapping from a Range of MAC addresses to a\n         Group Identifier.')
vlanMacBaseVlanMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 1), MacAddress())
if mibBuilder.loadTexts: vlanMacBaseVlanMacAddress.setReference('IEEE 802.1v clause 8.6.2')
if mibBuilder.loadTexts: vlanMacBaseVlanMacAddress.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanMacAddress.setDescription('The base MAC address of the range.')
vlanMacBaseVlanMacMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(9, 48)))
if mibBuilder.loadTexts: vlanMacBaseVlanMacMask.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanMacMask.setDescription("The Mask of the range.\n        The mask determains the leading '1' bits of the mask (MSB).\n        48 means single HOST and 9 means the widest range.\n        The MASK is limited to 9 to avoid entring ranges including\n        multicast addresses.\n        ")
vlanMacBaseVlanGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanMacBaseVlanGroupId.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanGroupId.setDescription('Represents a group of ranges of MAC addresses\n         that are associated together when assigning a\n         VID to a frame.')
vlanMacBaseVlanGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 45, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanMacBaseVlanGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanGroupRowStatus.setDescription('This object indicates the status of this entry.')
vlanMacBaseVlanPortTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 46), )
if mibBuilder.loadTexts: vlanMacBaseVlanPortTable.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanPortTable.setDescription('A table that contains VID sets used for\n         MAC-based VLAN Classification.')
vlanMacBaseVlanPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 46, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "RADLAN-vlan-MIB", "vlanMacBaseVlanPortGroupId"))
if mibBuilder.loadTexts: vlanMacBaseVlanPortEntry.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanPortEntry.setDescription('A VID set for a port and group.')
vlanMacBaseVlanPortGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 46, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vlanMacBaseVlanPortGroupId.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanPortGroupId.setDescription('Designates a group of Ranges in the ranges\n         Group Database.')
vlanMacBaseVlanPortGroupVid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 46, 1, 2), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanMacBaseVlanPortGroupVid.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanPortGroupVid.setDescription('The VID associated with a group of range MAC addresses for\n         each port.')
vlanMacBaseVlanPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 46, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanMacBaseVlanPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: vlanMacBaseVlanPortRowStatus.setDescription('This object indicates the status of this entry.')
vlanPrivateEdgeGroupTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 47), )
if mibBuilder.loadTexts: vlanPrivateEdgeGroupTable.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeGroupTable.setDescription('table for pve port and uplink')
vlanPrivateEdgeGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 47, 1), ).setIndexNames((0, "RADLAN-vlan-MIB", "vlanPrivateEdgeGroupSource"))
if mibBuilder.loadTexts: vlanPrivateEdgeGroupEntry.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeGroupEntry.setDescription(' entry of pve')
vlanPrivateEdgeGroupSource = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 47, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPrivateEdgeGroupSource.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeGroupSource.setDescription('specify the uplink group.')
vlanPrivateEdgeGroupUplink = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 47, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPrivateEdgeGroupUplink.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeGroupUplink.setDescription('specify the uplink port.')
vlanPrivateEdgeGroupStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 47, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanPrivateEdgeGroupStatus.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeGroupStatus.setDescription('The row status variable, used according to\n       row installation and removal conventions.')
vlanPrivateEdgeGroupIfIndexTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 48), )
if mibBuilder.loadTexts: vlanPrivateEdgeGroupIfIndexTable.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeGroupIfIndexTable.setDescription('table for pve port and uplink')
vlanPrivateEdgeGroupIfIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 48, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: vlanPrivateEdgeGroupIfIndexEntry.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeGroupIfIndexEntry.setDescription(' entry of pve')
vlanPrivateEdgeGroupIfIndexID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 48, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPrivateEdgeGroupIfIndexID.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeGroupIfIndexID.setDescription('specify the ifIndex group id.')
vlanPrivateEdgeGroupIfIndexDomainID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 48, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanPrivateEdgeGroupIfIndexDomainID.setStatus('current')
if mibBuilder.loadTexts: vlanPrivateEdgeGroupIfIndexDomainID.setDescription('specify the ifIndex group id.')
vlanSubnetRangeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 49), )
if mibBuilder.loadTexts: vlanSubnetRangeTable.setReference('IEEE 802.1v clause 8.6.4')
if mibBuilder.loadTexts: vlanSubnetRangeTable.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetRangeTable.setDescription('A table that contains mappings from subnet\n                 range to Group Identifiers used for\n                 Port-and-subnet-based VLAN Classification.')
vlanSubnetRangeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 49, 1), ).setIndexNames((0, "RADLAN-vlan-MIB", "vlanSubnetRangeAddr"), (0, "RADLAN-vlan-MIB", "vlanSubnetRangeMask"))
if mibBuilder.loadTexts: vlanSubnetRangeEntry.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetRangeEntry.setDescription('A mapping from a subnet to a\n                        Group Identifier.')
vlanSubnetRangeAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSubnetRangeAddr.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetRangeAddr.setDescription('The IP address of the range ')
vlanSubnetRangeMask = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSubnetRangeMask.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetRangeMask.setDescription('The numbers of continuous ones in the mask ')
vlanSubnetRangeGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanSubnetRangeGroupId.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetRangeGroupId.setDescription('Represents a group of subnets that are associated\n                        together when assigning a VID to a frame.')
vlanSubnetRangeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 49, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanSubnetRangeRowStatus.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetRangeRowStatus.setDescription('This object indicates the status of this entry.')
vlanSubnetPortTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 50), )
if mibBuilder.loadTexts: vlanSubnetPortTable.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetPortTable.setDescription('A table that contains VID sets used for\n                        Port-and-subnet-based VLAN Classification.')
vlanSubnetPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 50, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "RADLAN-vlan-MIB", "vlanSubnetPortGroupId"))
if mibBuilder.loadTexts: vlanSubnetPortEntry.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetPortEntry.setDescription('A VID set for a port.')
vlanSubnetPortGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 50, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vlanSubnetPortGroupId.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetPortGroupId.setDescription('Designates a group of subnets in the\n                         Group Database.')
vlanSubnetPortGroupVid = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 50, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanSubnetPortGroupVid.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetPortGroupVid.setDescription('The VID associated with a group of subnets for\n                        each port.')
vlanSubnetPortRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 50, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanSubnetPortRowStatus.setStatus('current')
if mibBuilder.loadTexts: vlanSubnetPortRowStatus.setDescription('This object indicates the status of this entry.')
vlanTriplePlayTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 51), )
if mibBuilder.loadTexts: vlanTriplePlayTable.setStatus('current')
if mibBuilder.loadTexts: vlanTriplePlayTable.setDescription(' TriplePlay table, map CPE vlan to multicastTvVlan')
vlanTriplePlayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 51, 1), ).setIndexNames((0, "RADLAN-vlan-MIB", "vlanTriplePlayInnerVID"))
if mibBuilder.loadTexts: vlanTriplePlayEntry.setStatus('current')
if mibBuilder.loadTexts: vlanTriplePlayEntry.setDescription(' entry of TriplePlay table')
vlanTriplePlayInnerVID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 51, 1, 1), VlanIndex())
if mibBuilder.loadTexts: vlanTriplePlayInnerVID.setStatus('current')
if mibBuilder.loadTexts: vlanTriplePlayInnerVID.setDescription(' Specifies  the CPE inner vlan.')
vlanTriplePlayMulticastTvVID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 51, 1, 2), VlanIndex()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanTriplePlayMulticastTvVID.setStatus('current')
if mibBuilder.loadTexts: vlanTriplePlayMulticastTvVID.setDescription(' Specifies the multicast TV outer vlan.')
vlanTriplePlayRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 51, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vlanTriplePlayRowStatus.setStatus('current')
if mibBuilder.loadTexts: vlanTriplePlayRowStatus.setDescription('The row status variable, used according to\n       row creation and removal conventions.')
vlanTriplePlayMulticastTvTable = MibTable((1, 3, 6, 1, 4, 1, 89, 48, 52), )
if mibBuilder.loadTexts: vlanTriplePlayMulticastTvTable.setStatus('current')
if mibBuilder.loadTexts: vlanTriplePlayMulticastTvTable.setDescription(' TriplePlayMulticastTv table saves a list of ports for a certain multicastTvVlan')
vlanTriplePlayMulticatTvEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 48, 52, 1), ).setIndexNames((0, "RADLAN-vlan-MIB", "vlanTriplePlayMulticastTvMulticastTvVID"))
if mibBuilder.loadTexts: vlanTriplePlayMulticatTvEntry.setStatus('current')
if mibBuilder.loadTexts: vlanTriplePlayMulticatTvEntry.setDescription(' entry of triple play MulticastTv table')
vlanTriplePlayMulticastTvMulticastTvVID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 52, 1, 1), VlanIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanTriplePlayMulticastTvMulticastTvVID.setStatus('current')
if mibBuilder.loadTexts: vlanTriplePlayMulticastTvMulticastTvVID.setDescription('Specifies the multicast TV external vlan.')
vlanTriplePlayMulticastTvMulticastTvPortList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 48, 52, 1, 2), PortList()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanTriplePlayMulticastTvMulticastTvPortList.setStatus('current')
if mibBuilder.loadTexts: vlanTriplePlayMulticastTvMulticastTvPortList.setDescription('the multicast tv port list.')
mibBuilder.exportSymbols("RADLAN-vlan-MIB", vlanMacBaseVlanPortEntry=vlanMacBaseVlanPortEntry, vlanPrivateEdgeEntry=vlanPrivateEdgeEntry, vlanPrivateSupported=vlanPrivateSupported, vlanMulticastTvEntry=vlanMulticastTvEntry, vlanSendUnknownToAllPorts=vlanSendUnknownToAllPorts, vlanDynamicVlanTag=vlanDynamicVlanTag, vlanPrivateEdgeGroupStatus=vlanPrivateEdgeGroupStatus, PYSNMP_MODULE_ID=vlan, vlanSpecialTagStatus=vlanSpecialTagStatus, vlanTriplePlayMulticastTvTable=vlanTriplePlayMulticastTvTable, vlanPrivateTable=vlanPrivateTable, vlanTriplePlayMulticastTvVID=vlanTriplePlayMulticastTvVID, vlanTriplePlayMulticastTvMulticastTvVID=vlanTriplePlayMulticastTvMulticastTvVID, vlanMulticastTvStatus=vlanMulticastTvStatus, vlanSpecialTagCurrentReserved=vlanSpecialTagCurrentReserved, vlanSubnetPortGroupVid=vlanSubnetPortGroupVid, vlanTriplePlayInnerVID=vlanTriplePlayInnerVID, vlanPrivateEdgeSupported=vlanPrivateEdgeSupported, vlanPrivateEdgeUplink=vlanPrivateEdgeUplink, vlanMacBaseVlanPortGroupId=vlanMacBaseVlanPortGroupId, vlanMulticastTvVID=vlanMulticastTvVID, vlanTriplePlayRowStatus=vlanTriplePlayRowStatus, vlanMacBaseVlanGroupTable=vlanMacBaseVlanGroupTable, vlanSpecialTagCurrentActive=vlanSpecialTagCurrentActive, vlanPrivateIsolatedVlanTag=vlanPrivateIsolatedVlanTag, vlanPrivateEdgeGroupUplink=vlanPrivateEdgeGroupUplink, vlanSubnetRangeMask=vlanSubnetRangeMask, vlanPrivateEdgeGroupIfIndexDomainID=vlanPrivateEdgeGroupIfIndexDomainID, vlanPrivateEdgeGroupIfIndexTable=vlanPrivateEdgeGroupIfIndexTable, vlanPortModeExtStatus=vlanPortModeExtStatus, vlanSpecialTagCurrentTable=vlanSpecialTagCurrentTable, vlanSubnetRangeEntry=vlanSubnetRangeEntry, vlanSubnetPortRowStatus=vlanSubnetPortRowStatus, vlanSpecialTagTable=vlanSpecialTagTable, vlanMacBaseVlanPortRowStatus=vlanMacBaseVlanPortRowStatus, vlanMulticastTvTable=vlanMulticastTvTable, vlanPortModeExtTable=vlanPortModeExtTable, vlanSubnetPortGroupId=vlanSubnetPortGroupId, vlanPortModeState=vlanPortModeState, vlanMacBaseVlanMacMask=vlanMacBaseVlanMacMask, vlanPrivateEdgeGroupTable=vlanPrivateEdgeGroupTable, vlanDefaultSupported=vlanDefaultSupported, vlanDynamicVlanEntry=vlanDynamicVlanEntry, vlanPrivateStatus=vlanPrivateStatus, vlanDynamicVlanMacAddress=vlanDynamicVlanMacAddress, vlanPrivateCommunityEntry=vlanPrivateCommunityEntry, vlanNameTable=vlanNameTable, vlanTriplePlayMulticastTvMulticastTvPortList=vlanTriplePlayMulticastTvMulticastTvPortList, vlanSpecialTagCurrentVID=vlanSpecialTagCurrentVID, vlanSpecialTagCurrentEntry=vlanSpecialTagCurrentEntry, vlan=vlan, vlanNameName=vlanNameName, vlanDot1vSupported=vlanDot1vSupported, vlanPortModeExtEntry=vlanPortModeExtEntry, vlanPortModeEntry=vlanPortModeEntry, vlanMacBaseVlanPortTable=vlanMacBaseVlanPortTable, vlanSubnetRangeTable=vlanSubnetRangeTable, vlanDynamicVlanSupported=vlanDynamicVlanSupported, vlanTriplePlayMulticatTvEntry=vlanTriplePlayMulticatTvEntry, vlanSpecialTagEntry=vlanSpecialTagEntry, vlanNameIfIndex=vlanNameIfIndex, vlanDynamicVlanStatus=vlanDynamicVlanStatus, vlanPrivateEdgeGroupEntry=vlanPrivateEdgeGroupEntry, vlanPrivateEdgeGroupIfIndexID=vlanPrivateEdgeGroupIfIndexID, vlanMacBaseVlanGroupEntry=vlanMacBaseVlanGroupEntry, vlanTriplePlayTable=vlanTriplePlayTable, vlanSubnetRangeRowStatus=vlanSubnetRangeRowStatus, vlanPrivateEdgeStatus=vlanPrivateEdgeStatus, vlanPrivateEdgeVersion=vlanPrivateEdgeVersion, vlanSubnetPortEntry=vlanSubnetPortEntry, vlanDefaultEnabled=vlanDefaultEnabled, vlanNameEntry=vlanNameEntry, vlanPrivateCommunityTable=vlanPrivateCommunityTable, vlanSubnetRangeGroupId=vlanSubnetRangeGroupId, vlanPrivateCommunityStatus=vlanPrivateCommunityStatus, vlanPrivateEntry=vlanPrivateEntry, vlanMacBaseVlanGroupId=vlanMacBaseVlanGroupId, vlanMacBaseVlanPortGroupVid=vlanMacBaseVlanPortGroupVid, vlanSubnetRangeAddr=vlanSubnetRangeAddr, vlanPrivateEdgeTable=vlanPrivateEdgeTable, vlanPrivateCommunityVlanTag=vlanPrivateCommunityVlanTag, vlanTriplePlayEntry=vlanTriplePlayEntry, vlanPortModeTable=vlanPortModeTable, vlanMacBaseVlanMacAddress=vlanMacBaseVlanMacAddress, vlanMaxTableNumber=vlanMaxTableNumber, vlanPortModeExtState=vlanPortModeExtState, vlanSpecialTagVID=vlanSpecialTagVID, vlanMacBaseVlanGroupRowStatus=vlanMacBaseVlanGroupRowStatus, vlanMibVersion=vlanMibVersion, vlanPrivateEdgeGroupIfIndexEntry=vlanPrivateEdgeGroupIfIndexEntry, vlanDynamicVlanTable=vlanDynamicVlanTable, vlanSubnetPortTable=vlanSubnetPortTable, vlanPrivateEdgeGroupSource=vlanPrivateEdgeGroupSource, vlanNameTag=vlanNameTag)
