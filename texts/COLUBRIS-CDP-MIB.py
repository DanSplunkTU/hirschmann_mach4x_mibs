#
# PySNMP MIB module COLUBRIS-CDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-CDP-MIB.my
# Produced by pysmi-1.1.8 at Mon Feb  7 16:13:23 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Counter32, ModuleIdentity, Counter64, NotificationType, ObjectIdentity, iso, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, Integer32, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "Counter64", "NotificationType", "ObjectIdentity", "iso", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "Integer32", "MibIdentifier", "Unsigned32")
MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention")
colubrisCdpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 9))
if mibBuilder.loadTexts: colubrisCdpMIB.setLastUpdated('200402200000Z')
if mibBuilder.loadTexts: colubrisCdpMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisCdpMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisCdpMIB.setDescription('Colubris Networks CDP MIB.')
colubrisCdpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1))
coCdpCache = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1))
coCdpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 2))
coCdpCacheTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1), )
if mibBuilder.loadTexts: coCdpCacheTable.setStatus('current')
if mibBuilder.loadTexts: coCdpCacheTable.setDescription('The (conceptual) table containing the cached information\n                 obtained from CDP messages. In tabular form to allow\n                 multiple instances on an agent. This table applies to\n                 access controllers only.')
coCdpCacheEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-CDP-MIB", "coCdpCacheDeviceIndex"))
if mibBuilder.loadTexts: coCdpCacheEntry.setStatus('current')
if mibBuilder.loadTexts: coCdpCacheEntry.setDescription('An entry (conceptual row) in the coCdpCacheTable. A row\n                 contains the information received via CDP on one interface\n                 from one device.  Entries appear when a CDP advertisement is\n                 received from a neighbor device.\n                 coCdpCacheDeviceIndex - Uniquely identify a device inside the\n                                         CDP table.')
coCdpCacheDeviceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coCdpCacheDeviceIndex.setStatus('current')
if mibBuilder.loadTexts: coCdpCacheDeviceIndex.setDescription('A unique value for each device from which CDP messages\n                 are received.')
coCdpCacheLocalInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheLocalInterface.setStatus('current')
if mibBuilder.loadTexts: coCdpCacheLocalInterface.setDescription('Indicates the name of the interface that received the CDP message.')
coCdpCacheAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheAddress.setStatus('current')
if mibBuilder.loadTexts: coCdpCacheAddress.setDescription('Indicates the Ethernet address of the device that sent the CDP message.')
coCdpCacheDeviceId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheDeviceId.setStatus('current')
if mibBuilder.loadTexts: coCdpCacheDeviceId.setDescription('Indicates the Device-ID string as reported in the most recent CDP\n                 message. A zero-length string indicates that no Device-ID field (TLV) \n                 was reported in the most recent CDP message.')
coCdpCacheTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheTimeToLive.setStatus('current')
if mibBuilder.loadTexts: coCdpCacheTimeToLive.setDescription('Indicates the number of seconds to keep the remote device in the\n                 cache table after receiving the CDP message.')
coCdpCacheCapabilities = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheCapabilities.setStatus('current')
if mibBuilder.loadTexts: coCdpCacheCapabilities.setDescription("Indicates the device's functional capabilities as reported in the\n                 most recent CDP message. Possible values are:\n\n                   R - layer 3 router\n\n                   T - a layer 2 transparent bridge \n\n                   B - a layer 2 source-root bridge\n\n                   S - a layer 2 switch (non-spanning tree)\n\n                   r - a layer 3 (non routing) host\n\n                   I - does not forward IGMP Packets to non-routers\n\n                   H - a layer 1 repeater\n\n                 A zero-length string indicates no Capabilities field (TLV) was \n                 reported in the most recent CDP message.")
coCdpCacheVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCacheVersion.setStatus('current')
if mibBuilder.loadTexts: coCdpCacheVersion.setDescription('Indicates the Version string as reported in the most recent CDP\n                 message. A zero-length string indicates no Version field (TLV) \n                 was reported in the most recent CDP message.')
coCdpCachePlatform = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCachePlatform.setStatus('current')
if mibBuilder.loadTexts: coCdpCachePlatform.setDescription("Indicates the Device's Hardware Platform as reported in the most\n                 recent CDP message. A zero-length string indicates that no Platform\n                 field (TLV) was reported in the most recent CDP message.")
coCdpCachePortId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coCdpCachePortId.setStatus('current')
if mibBuilder.loadTexts: coCdpCachePortId.setDescription("Indicates the Port-ID string as reported in the most recent CDP\n                 message. This will typically be the value of the ifName\n                 object (e.g., 'Ethernet0'). A zero-length string indicates no \n                 Port-ID field (TLV) was reported in the most recent CDP message.")
coCdpGlobalMessageInterval = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 254)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdpGlobalMessageInterval.setStatus('current')
if mibBuilder.loadTexts: coCdpGlobalMessageInterval.setDescription('Specifies the interval at which CDP messages will be generated.')
coCdpGlobalHoldTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 9, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(10, 255)).clone(180)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: coCdpGlobalHoldTime.setStatus('current')
if mibBuilder.loadTexts: coCdpGlobalHoldTime.setDescription('Specifies the amount of time the receiving device holds CDP messages.')
colubrisCdpMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 2))
colubrisCdpMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 1))
colubrisCdpMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 2))
colubrisCdpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 1, 1)).setObjects(("COLUBRIS-CDP-MIB", "colubrisCdpMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisCdpMIBCompliance = colubrisCdpMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisCdpMIBCompliance.setDescription('The compliance statement for the CDP MIB.')
colubrisCdpMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 9, 2, 2, 1)).setObjects(("COLUBRIS-CDP-MIB", "coCdpCacheLocalInterface"), ("COLUBRIS-CDP-MIB", "coCdpCacheAddress"), ("COLUBRIS-CDP-MIB", "coCdpCacheDeviceId"), ("COLUBRIS-CDP-MIB", "coCdpCacheTimeToLive"), ("COLUBRIS-CDP-MIB", "coCdpCacheCapabilities"), ("COLUBRIS-CDP-MIB", "coCdpCacheVersion"), ("COLUBRIS-CDP-MIB", "coCdpCachePlatform"), ("COLUBRIS-CDP-MIB", "coCdpCachePortId"), ("COLUBRIS-CDP-MIB", "coCdpGlobalMessageInterval"), ("COLUBRIS-CDP-MIB", "coCdpGlobalHoldTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisCdpMIBGroup = colubrisCdpMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisCdpMIBGroup.setDescription('A collection of objects for use with CDP.')
mibBuilder.exportSymbols("COLUBRIS-CDP-MIB", coCdpGlobalHoldTime=coCdpGlobalHoldTime, coCdpCachePortId=coCdpCachePortId, coCdpCache=coCdpCache, coCdpGlobal=coCdpGlobal, coCdpGlobalMessageInterval=coCdpGlobalMessageInterval, colubrisCdpMIBCompliances=colubrisCdpMIBCompliances, PYSNMP_MODULE_ID=colubrisCdpMIB, coCdpCacheLocalInterface=coCdpCacheLocalInterface, colubrisCdpMIB=colubrisCdpMIB, coCdpCacheTimeToLive=coCdpCacheTimeToLive, coCdpCacheEntry=coCdpCacheEntry, colubrisCdpMIBGroups=colubrisCdpMIBGroups, coCdpCachePlatform=coCdpCachePlatform, coCdpCacheCapabilities=coCdpCacheCapabilities, colubrisCdpMIBConformance=colubrisCdpMIBConformance, colubrisCdpMIBGroup=colubrisCdpMIBGroup, colubrisCdpMIBObjects=colubrisCdpMIBObjects, colubrisCdpMIBCompliance=colubrisCdpMIBCompliance, coCdpCacheAddress=coCdpCacheAddress, coCdpCacheTable=coCdpCacheTable, coCdpCacheVersion=coCdpCacheVersion, coCdpCacheDeviceId=coCdpCacheDeviceId, coCdpCacheDeviceIndex=coCdpCacheDeviceIndex)
