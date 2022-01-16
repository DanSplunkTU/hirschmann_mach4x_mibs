#
# PySNMP MIB module ACD-DISCOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-DISCOVERY-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:12 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, ObjectIdentity, TimeTicks, Gauge32, ModuleIdentity, Bits, iso, Integer32, Counter32, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "ObjectIdentity", "TimeTicks", "Gauge32", "ModuleIdentity", "Bits", "iso", "Integer32", "Counter32", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32")
MacAddress, TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "DateAndTime")
acdDiscovery = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 11))
acdDiscovery.setRevisions(('2011-11-01 01:00', '2008-10-01 01:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acdDiscovery.setRevisionsDescriptions(('Addition of MAC Address List table.', 'Initial version of MIB module ACD-DISCOVERY-MIB.',))
if mibBuilder.loadTexts: acdDiscovery.setLastUpdated('201111010100Z')
if mibBuilder.loadTexts: acdDiscovery.setOrganization('Accedian Networks, Inc.')
if mibBuilder.loadTexts: acdDiscovery.setContactInfo('Accedian Technical Assistance Center\n             Accedian Networks, Inc.\n             4878 Levy, suite 202\n             Saint-Laurent, Quebec Canada H4R 2P1\n             E-mail: support@accedian.com')
if mibBuilder.loadTexts: acdDiscovery.setDescription('The discovery inventory information for this Accedian Networks device.')
acdDiscoveryNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 0))
acdDiscoveryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1))
acdDiscoveryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2))
acdDiscoveryInventory = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1))
acdDiscoveryInventoryTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1), )
if mibBuilder.loadTexts: acdDiscoveryInventoryTable.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryInventoryTable.setDescription('Table of information on neighboring NIDs')
acdDiscoveryInventoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1), ).setIndexNames((0, "ACD-DISCOVERY-MIB", "acdDiscoveryIndex"))
if mibBuilder.loadTexts: acdDiscoveryInventoryEntry.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryInventoryEntry.setDescription('Inventory information.')
acdDiscoveryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: acdDiscoveryIndex.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryIndex.setDescription('The value of this object uniquely identifies this acdDiscovery\n        entry.')
acdDiscoveryMgmtIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryMgmtIpAddress.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryMgmtIpAddress.setDescription('The IP address of the management interface.')
acdDiscoverySystemName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoverySystemName.setStatus('current')
if mibBuilder.loadTexts: acdDiscoverySystemName.setDescription('An administratively-assigned name for this managed node.')
acdDiscoverySystemDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoverySystemDesc.setStatus('current')
if mibBuilder.loadTexts: acdDiscoverySystemDesc.setDescription('The system description.')
acdDiscoverySerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoverySerialNumber.setStatus('current')
if mibBuilder.loadTexts: acdDiscoverySerialNumber.setDescription('This is the serial number of the unit.')
acdDiscoveryLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryLastChange.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryLastChange.setDescription('Indicates the last time we received an information frame for the device.')
acdDiscoveryDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryDomain.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryDomain.setDescription('Indicates the discovery domain.')
acdDiscoveryFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryFirmware.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryFirmware.setDescription('The firmware version of the unit.')
acdDiscoveryBaseMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryBaseMacAddress.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryBaseMacAddress.setDescription('The base MAC address of the remote NID based on the last information\n         frame received from the device. If no information has been received,\n         this object shall be equal to six octets of zero.')
acdDiscoveryInterfaceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryInterfaceMacAddress.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryInterfaceMacAddress.setDescription('The management interface MAC address of the remote NID based on the\n         last information frame received from the device. If no information has\n         been received, this object shall be equal to six octets of zero.')
acdDiscoveryChassisIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryChassisIdSubtype.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryChassisIdSubtype.setDescription('The chassis ID subtype, as defined by IEEE 802.1AB.')
acdDiscoveryChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryChassisId.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryChassisId.setDescription('The chassis ID of the remote device.')
acdDiscoveryLocalPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryLocalPortId.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryLocalPortId.setDescription('This object identifies the port name where the advertisement frame was received.')
acdDiscoveryRemotePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryRemotePortId.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryRemotePortId.setDescription('This object identifies the advertisement port of the remote device.')
acdDiscoveryWebServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryWebServerPort.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryWebServerPort.setDescription('The web server port of the remote device.')
acdDiscoverySnmpAgentPort = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoverySnmpAgentPort.setStatus('current')
if mibBuilder.loadTexts: acdDiscoverySnmpAgentPort.setDescription('The SNMP agent port of the remote device. If 0, SNMP agent is disabled.')
acdDiscoverySshPort = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoverySshPort.setStatus('current')
if mibBuilder.loadTexts: acdDiscoverySshPort.setDescription('The SSH port of the remote device.')
acdDiscoveryVlan1 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryVlan1.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryVlan1.setDescription('The first VLAN on the remote device interface. No VLAN when this value is zero.')
acdDiscoveryVlan2 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryVlan2.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryVlan2.setDescription('The second VLAN on the remote device interface. No VLAN when this value is zero.')
acdDiscoveryIpListTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2), )
if mibBuilder.loadTexts: acdDiscoveryIpListTable.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryIpListTable.setDescription('This table contains all interfaces found on the remote device, excluding the\n        management interface, which was configured by a beacon frame.')
acdDiscoveryIpListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2, 1), ).setIndexNames((0, "ACD-DISCOVERY-MIB", "acdDiscoveryIndex"), (0, "ACD-DISCOVERY-MIB", "acdDiscoveryIpListIndex"))
if mibBuilder.loadTexts: acdDiscoveryIpListEntry.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryIpListEntry.setDescription('An entry consisting of the IP address of an interface on the remote device.')
acdDiscoveryIpListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: acdDiscoveryIpListIndex.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryIpListIndex.setDescription('Unique value for each row. Based on number of interface found.')
acdDiscoveryIpListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryIpListAddress.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryIpListAddress.setDescription('This is the IP address on one of the interfaces found on the remote NID.')
acdDiscoveryMacAddressListTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3), )
if mibBuilder.loadTexts: acdDiscoveryMacAddressListTable.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryMacAddressListTable.setDescription('This table contains MAC addresses of ports found on the remote device. Not\n         all port MAC addresses are necessary listed.')
acdDiscoveryMacAddressListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1), ).setIndexNames((0, "ACD-DISCOVERY-MIB", "acdDiscoveryIndex"), (0, "ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListIndex"))
if mibBuilder.loadTexts: acdDiscoveryMacAddressListEntry.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryMacAddressListEntry.setDescription('An entry consisting of the MAC address of a port on the remote device.')
acdDiscoveryMacAddressListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: acdDiscoveryMacAddressListIndex.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryMacAddressListIndex.setDescription('Unique value for each row. Based on number of port MAC addresses found.')
acdDiscoveryMacAddressListSystemSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryMacAddressListSystemSlotId.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryMacAddressListSystemSlotId.setDescription('System slot identifier of module on which the port is located. \n         Applies only to a MetroNODE module. Value is 0 for a MetroNID device.')
acdDiscoveryMacAddressListPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryMacAddressListPortId.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryMacAddressListPortId.setDescription('Port identifier.')
acdDiscoveryMacAddressListPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryMacAddressListPortName.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryMacAddressListPortName.setDescription('Port name.')
acdDiscoveryMacAddressListPortMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryMacAddressListPortMacAddress.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryMacAddressListPortMacAddress.setDescription('This is the MAC address of one of the ports found on the remote device.')
acdDiscoveryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 1))
acdDiscoveryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2))
acdDiscoveryInventoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2, 1)).setObjects(("ACD-DISCOVERY-MIB", "acdDiscoveryMgmtIpAddress"), ("ACD-DISCOVERY-MIB", "acdDiscoverySystemName"), ("ACD-DISCOVERY-MIB", "acdDiscoverySystemDesc"), ("ACD-DISCOVERY-MIB", "acdDiscoverySerialNumber"), ("ACD-DISCOVERY-MIB", "acdDiscoveryLastChange"), ("ACD-DISCOVERY-MIB", "acdDiscoveryDomain"), ("ACD-DISCOVERY-MIB", "acdDiscoveryFirmware"), ("ACD-DISCOVERY-MIB", "acdDiscoveryBaseMacAddress"), ("ACD-DISCOVERY-MIB", "acdDiscoveryInterfaceMacAddress"), ("ACD-DISCOVERY-MIB", "acdDiscoveryChassisIdSubtype"), ("ACD-DISCOVERY-MIB", "acdDiscoveryChassisId"), ("ACD-DISCOVERY-MIB", "acdDiscoveryLocalPortId"), ("ACD-DISCOVERY-MIB", "acdDiscoveryRemotePortId"), ("ACD-DISCOVERY-MIB", "acdDiscoveryWebServerPort"), ("ACD-DISCOVERY-MIB", "acdDiscoverySnmpAgentPort"), ("ACD-DISCOVERY-MIB", "acdDiscoverySshPort"), ("ACD-DISCOVERY-MIB", "acdDiscoveryVlan1"), ("ACD-DISCOVERY-MIB", "acdDiscoveryVlan2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDiscoveryInventoryGroup = acdDiscoveryInventoryGroup.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryInventoryGroup.setDescription('.')
acdDiscoveryIpListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2, 2)).setObjects(("ACD-DISCOVERY-MIB", "acdDiscoveryIpListAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDiscoveryIpListGroup = acdDiscoveryIpListGroup.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryIpListGroup.setDescription('.')
acdDiscoveryMacAddressListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2, 3)).setObjects(("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListSystemSlotId"), ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListPortId"), ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListPortName"), ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListPortMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDiscoveryMacAddressListGroup = acdDiscoveryMacAddressListGroup.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryMacAddressListGroup.setDescription('.')
acdDiscoveryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 1, 1)).setObjects(("ACD-DISCOVERY-MIB", "acdDiscoveryInventoryGroup"), ("ACD-DISCOVERY-MIB", "acdDiscoveryIpListGroup"), ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDiscoveryCompliance = acdDiscoveryCompliance.setStatus('current')
if mibBuilder.loadTexts: acdDiscoveryCompliance.setDescription('The compliance statement for support of the ACD-DISCOVERY-MIB module.')
mibBuilder.exportSymbols("ACD-DISCOVERY-MIB", acdDiscoveryRemotePortId=acdDiscoveryRemotePortId, acdDiscoveryCompliance=acdDiscoveryCompliance, acdDiscoveryMacAddressListEntry=acdDiscoveryMacAddressListEntry, acdDiscoveryMacAddressListPortMacAddress=acdDiscoveryMacAddressListPortMacAddress, PYSNMP_MODULE_ID=acdDiscovery, acdDiscoveryVlan2=acdDiscoveryVlan2, acdDiscoveryIpListAddress=acdDiscoveryIpListAddress, acdDiscovery=acdDiscovery, acdDiscoveryMacAddressListTable=acdDiscoveryMacAddressListTable, acdDiscoveryLastChange=acdDiscoveryLastChange, acdDiscoveryNotifications=acdDiscoveryNotifications, acdDiscoveryGroups=acdDiscoveryGroups, acdDiscoverySystemDesc=acdDiscoverySystemDesc, acdDiscoverySystemName=acdDiscoverySystemName, acdDiscoverySnmpAgentPort=acdDiscoverySnmpAgentPort, acdDiscoveryFirmware=acdDiscoveryFirmware, acdDiscoveryBaseMacAddress=acdDiscoveryBaseMacAddress, acdDiscoveryDomain=acdDiscoveryDomain, acdDiscoverySerialNumber=acdDiscoverySerialNumber, acdDiscoveryVlan1=acdDiscoveryVlan1, acdDiscoveryInterfaceMacAddress=acdDiscoveryInterfaceMacAddress, acdDiscoveryIpListEntry=acdDiscoveryIpListEntry, acdDiscoveryIpListIndex=acdDiscoveryIpListIndex, acdDiscoveryInventoryGroup=acdDiscoveryInventoryGroup, acdDiscoveryIpListGroup=acdDiscoveryIpListGroup, acdDiscoveryMacAddressListIndex=acdDiscoveryMacAddressListIndex, acdDiscoveryMIBObjects=acdDiscoveryMIBObjects, acdDiscoveryMacAddressListPortName=acdDiscoveryMacAddressListPortName, acdDiscoveryInventoryTable=acdDiscoveryInventoryTable, acdDiscoveryLocalPortId=acdDiscoveryLocalPortId, acdDiscoveryCompliances=acdDiscoveryCompliances, acdDiscoverySshPort=acdDiscoverySshPort, acdDiscoveryInventory=acdDiscoveryInventory, acdDiscoveryIpListTable=acdDiscoveryIpListTable, acdDiscoveryMacAddressListSystemSlotId=acdDiscoveryMacAddressListSystemSlotId, acdDiscoveryConformance=acdDiscoveryConformance, acdDiscoveryMacAddressListPortId=acdDiscoveryMacAddressListPortId, acdDiscoveryIndex=acdDiscoveryIndex, acdDiscoveryMgmtIpAddress=acdDiscoveryMgmtIpAddress, acdDiscoveryWebServerPort=acdDiscoveryWebServerPort, acdDiscoveryMacAddressListGroup=acdDiscoveryMacAddressListGroup, acdDiscoveryChassisIdSubtype=acdDiscoveryChassisIdSubtype, acdDiscoveryChassisId=acdDiscoveryChassisId, acdDiscoveryInventoryEntry=acdDiscoveryInventoryEntry)
