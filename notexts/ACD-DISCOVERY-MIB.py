#
# PySNMP MIB module ACD-DISCOVERY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-DISCOVERY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:15:15 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, Unsigned32, MibIdentifier, ModuleIdentity, iso, Integer32, IpAddress, TimeTicks, NotificationType, Gauge32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "MibIdentifier", "ModuleIdentity", "iso", "Integer32", "IpAddress", "TimeTicks", "NotificationType", "Gauge32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32")
TextualConvention, MacAddress, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DateAndTime", "DisplayString")
acdDiscovery = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 11))
acdDiscovery.setRevisions(('2011-11-01 01:00', '2008-10-01 01:00',))
if mibBuilder.loadTexts: acdDiscovery.setLastUpdated('201111010100Z')
if mibBuilder.loadTexts: acdDiscovery.setOrganization('Accedian Networks, Inc.')
acdDiscoveryNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 0))
acdDiscoveryMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1))
acdDiscoveryConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2))
acdDiscoveryInventory = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1))
acdDiscoveryInventoryTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1), )
if mibBuilder.loadTexts: acdDiscoveryInventoryTable.setStatus('current')
acdDiscoveryInventoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1), ).setIndexNames((0, "ACD-DISCOVERY-MIB", "acdDiscoveryIndex"))
if mibBuilder.loadTexts: acdDiscoveryInventoryEntry.setStatus('current')
acdDiscoveryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: acdDiscoveryIndex.setStatus('current')
acdDiscoveryMgmtIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryMgmtIpAddress.setStatus('current')
acdDiscoverySystemName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoverySystemName.setStatus('current')
acdDiscoverySystemDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoverySystemDesc.setStatus('current')
acdDiscoverySerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoverySerialNumber.setStatus('current')
acdDiscoveryLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryLastChange.setStatus('current')
acdDiscoveryDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryDomain.setStatus('current')
acdDiscoveryFirmware = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryFirmware.setStatus('current')
acdDiscoveryBaseMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 9), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryBaseMacAddress.setStatus('current')
acdDiscoveryInterfaceMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryInterfaceMacAddress.setStatus('current')
acdDiscoveryChassisIdSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryChassisIdSubtype.setStatus('current')
acdDiscoveryChassisId = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryChassisId.setStatus('current')
acdDiscoveryLocalPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryLocalPortId.setStatus('current')
acdDiscoveryRemotePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryRemotePortId.setStatus('current')
acdDiscoveryWebServerPort = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 15), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryWebServerPort.setStatus('current')
acdDiscoverySnmpAgentPort = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 16), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoverySnmpAgentPort.setStatus('current')
acdDiscoverySshPort = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoverySshPort.setStatus('current')
acdDiscoveryVlan1 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryVlan1.setStatus('current')
acdDiscoveryVlan2 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 1, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryVlan2.setStatus('current')
acdDiscoveryIpListTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2), )
if mibBuilder.loadTexts: acdDiscoveryIpListTable.setStatus('current')
acdDiscoveryIpListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2, 1), ).setIndexNames((0, "ACD-DISCOVERY-MIB", "acdDiscoveryIndex"), (0, "ACD-DISCOVERY-MIB", "acdDiscoveryIpListIndex"))
if mibBuilder.loadTexts: acdDiscoveryIpListEntry.setStatus('current')
acdDiscoveryIpListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: acdDiscoveryIpListIndex.setStatus('current')
acdDiscoveryIpListAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryIpListAddress.setStatus('current')
acdDiscoveryMacAddressListTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3), )
if mibBuilder.loadTexts: acdDiscoveryMacAddressListTable.setStatus('current')
acdDiscoveryMacAddressListEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1), ).setIndexNames((0, "ACD-DISCOVERY-MIB", "acdDiscoveryIndex"), (0, "ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListIndex"))
if mibBuilder.loadTexts: acdDiscoveryMacAddressListEntry.setStatus('current')
acdDiscoveryMacAddressListIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: acdDiscoveryMacAddressListIndex.setStatus('current')
acdDiscoveryMacAddressListSystemSlotId = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryMacAddressListSystemSlotId.setStatus('current')
acdDiscoveryMacAddressListPortId = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryMacAddressListPortId.setStatus('current')
acdDiscoveryMacAddressListPortName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryMacAddressListPortName.setStatus('current')
acdDiscoveryMacAddressListPortMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 11, 1, 1, 3, 1, 5), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDiscoveryMacAddressListPortMacAddress.setStatus('current')
acdDiscoveryCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 1))
acdDiscoveryGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2))
acdDiscoveryInventoryGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2, 1)).setObjects(("ACD-DISCOVERY-MIB", "acdDiscoveryMgmtIpAddress"), ("ACD-DISCOVERY-MIB", "acdDiscoverySystemName"), ("ACD-DISCOVERY-MIB", "acdDiscoverySystemDesc"), ("ACD-DISCOVERY-MIB", "acdDiscoverySerialNumber"), ("ACD-DISCOVERY-MIB", "acdDiscoveryLastChange"), ("ACD-DISCOVERY-MIB", "acdDiscoveryDomain"), ("ACD-DISCOVERY-MIB", "acdDiscoveryFirmware"), ("ACD-DISCOVERY-MIB", "acdDiscoveryBaseMacAddress"), ("ACD-DISCOVERY-MIB", "acdDiscoveryInterfaceMacAddress"), ("ACD-DISCOVERY-MIB", "acdDiscoveryChassisIdSubtype"), ("ACD-DISCOVERY-MIB", "acdDiscoveryChassisId"), ("ACD-DISCOVERY-MIB", "acdDiscoveryLocalPortId"), ("ACD-DISCOVERY-MIB", "acdDiscoveryRemotePortId"), ("ACD-DISCOVERY-MIB", "acdDiscoveryWebServerPort"), ("ACD-DISCOVERY-MIB", "acdDiscoverySnmpAgentPort"), ("ACD-DISCOVERY-MIB", "acdDiscoverySshPort"), ("ACD-DISCOVERY-MIB", "acdDiscoveryVlan1"), ("ACD-DISCOVERY-MIB", "acdDiscoveryVlan2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDiscoveryInventoryGroup = acdDiscoveryInventoryGroup.setStatus('current')
acdDiscoveryIpListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2, 2)).setObjects(("ACD-DISCOVERY-MIB", "acdDiscoveryIpListAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDiscoveryIpListGroup = acdDiscoveryIpListGroup.setStatus('current')
acdDiscoveryMacAddressListGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 2, 3)).setObjects(("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListSystemSlotId"), ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListPortId"), ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListPortName"), ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListPortMacAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDiscoveryMacAddressListGroup = acdDiscoveryMacAddressListGroup.setStatus('current')
acdDiscoveryCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 11, 2, 1, 1)).setObjects(("ACD-DISCOVERY-MIB", "acdDiscoveryInventoryGroup"), ("ACD-DISCOVERY-MIB", "acdDiscoveryIpListGroup"), ("ACD-DISCOVERY-MIB", "acdDiscoveryMacAddressListGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDiscoveryCompliance = acdDiscoveryCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-DISCOVERY-MIB", acdDiscoveryLastChange=acdDiscoveryLastChange, acdDiscoveryWebServerPort=acdDiscoveryWebServerPort, acdDiscoveryChassisIdSubtype=acdDiscoveryChassisIdSubtype, acdDiscoveryDomain=acdDiscoveryDomain, acdDiscoveryMacAddressListPortName=acdDiscoveryMacAddressListPortName, acdDiscoveryRemotePortId=acdDiscoveryRemotePortId, acdDiscoveryMgmtIpAddress=acdDiscoveryMgmtIpAddress, acdDiscoveryInventoryEntry=acdDiscoveryInventoryEntry, acdDiscoveryCompliances=acdDiscoveryCompliances, acdDiscoveryMacAddressListPortMacAddress=acdDiscoveryMacAddressListPortMacAddress, acdDiscoverySshPort=acdDiscoverySshPort, acdDiscoveryIpListIndex=acdDiscoveryIpListIndex, acdDiscoveryInventory=acdDiscoveryInventory, acdDiscoveryMacAddressListSystemSlotId=acdDiscoveryMacAddressListSystemSlotId, PYSNMP_MODULE_ID=acdDiscovery, acdDiscoverySystemDesc=acdDiscoverySystemDesc, acdDiscoveryMIBObjects=acdDiscoveryMIBObjects, acdDiscovery=acdDiscovery, acdDiscoveryLocalPortId=acdDiscoveryLocalPortId, acdDiscoverySerialNumber=acdDiscoverySerialNumber, acdDiscoveryFirmware=acdDiscoveryFirmware, acdDiscoveryInventoryTable=acdDiscoveryInventoryTable, acdDiscoveryVlan1=acdDiscoveryVlan1, acdDiscoveryCompliance=acdDiscoveryCompliance, acdDiscoveryMacAddressListTable=acdDiscoveryMacAddressListTable, acdDiscoveryVlan2=acdDiscoveryVlan2, acdDiscoveryMacAddressListEntry=acdDiscoveryMacAddressListEntry, acdDiscoverySnmpAgentPort=acdDiscoverySnmpAgentPort, acdDiscoveryMacAddressListPortId=acdDiscoveryMacAddressListPortId, acdDiscoveryIpListAddress=acdDiscoveryIpListAddress, acdDiscoveryIpListEntry=acdDiscoveryIpListEntry, acdDiscoveryInterfaceMacAddress=acdDiscoveryInterfaceMacAddress, acdDiscoveryBaseMacAddress=acdDiscoveryBaseMacAddress, acdDiscoveryInventoryGroup=acdDiscoveryInventoryGroup, acdDiscoveryChassisId=acdDiscoveryChassisId, acdDiscoveryMacAddressListIndex=acdDiscoveryMacAddressListIndex, acdDiscoveryIpListTable=acdDiscoveryIpListTable, acdDiscoveryIndex=acdDiscoveryIndex, acdDiscoveryMacAddressListGroup=acdDiscoveryMacAddressListGroup, acdDiscoveryGroups=acdDiscoveryGroups, acdDiscoveryIpListGroup=acdDiscoveryIpListGroup, acdDiscoveryConformance=acdDiscoveryConformance, acdDiscoverySystemName=acdDiscoverySystemName, acdDiscoveryNotifications=acdDiscoveryNotifications)
