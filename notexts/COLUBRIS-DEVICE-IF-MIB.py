#
# PySNMP MIB module COLUBRIS-DEVICE-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-DEVICE-IF-MIB.my
# Produced by pysmi-1.1.8 at Sat Jan 15 18:07:38 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
coDevDisIndex, = mibBuilder.importSymbols("COLUBRIS-DEVICE-MIB", "coDevDisIndex")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Counter32, Bits, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, MibIdentifier, TimeTicks, Gauge32, Counter64, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter32", "Bits", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "MibIdentifier", "TimeTicks", "Gauge32", "Counter64", "NotificationType", "Integer32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
colubrisDeviceIfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 24))
if mibBuilder.loadTexts: colubrisDeviceIfMIB.setLastUpdated('200607050000Z')
if mibBuilder.loadTexts: colubrisDeviceIfMIB.setOrganization('Colubris Networks, Inc.')
colubrisDeviceIfMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1))
coDeviceIfStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1))
coDeviceIfStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2))
coDeviceIfStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1), )
if mibBuilder.loadTexts: coDeviceIfStatusTable.setStatus('current')
coDeviceIfStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-IF-MIB", "coDevIfStaIfIndex"))
if mibBuilder.loadTexts: coDeviceIfStatusEntry.setStatus('current')
coDevIfStaIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevIfStaIfIndex.setStatus('current')
coDevIfStaFriendlyInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaFriendlyInterfaceName.setStatus('current')
coDevIfStaType = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("other", 1), ("ethernet", 2), ("l2vlan", 3), ("bridge", 4), ("ieee80211", 5), ("ieee80211Wds", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaType.setStatus('current')
coDevIfStaVLAN = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4094))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaVLAN.setStatus('current')
coDevIfStaIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaIpAddress.setStatus('current')
coDevIfStaNetworkMask = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaNetworkMask.setStatus('current')
coDevIfStaMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 7), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaMACAddress.setStatus('current')
coDevIfStaState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStaState.setStatus('current')
coDeviceIfStatsTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceIfStatsTable.setStatus('current')
coDeviceIfStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1), )
coDeviceIfStatusEntry.registerAugmentions(("COLUBRIS-DEVICE-IF-MIB", "coDeviceIfStatsEntry"))
coDeviceIfStatsEntry.setIndexNames(*coDeviceIfStatusEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceIfStatsEntry.setStatus('current')
coDevIfStsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsRxBytes.setStatus('current')
coDevIfStsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsRxPackets.setStatus('current')
coDevIfStsRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsRxErrors.setStatus('current')
coDevIfStsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsTxBytes.setStatus('current')
coDevIfStsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsTxPackets.setStatus('current')
coDevIfStsTxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 24, 1, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevIfStsTxErrors.setStatus('current')
colubrisDeviceIfMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 2))
colubrisDeviceIfMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 2, 0))
colubrisDeviceIfMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3))
colubrisDeviceIfMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 1))
colubrisDeviceIfMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2))
colubrisDeviceIfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 1, 1)).setObjects(("COLUBRIS-DEVICE-IF-MIB", "colubrisDeviceIfStatusMIBGroup"), ("COLUBRIS-DEVICE-IF-MIB", "colubrisDeviceIfStatsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceIfMIBCompliance = colubrisDeviceIfMIBCompliance.setStatus('current')
colubrisDeviceIfStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2, 1)).setObjects(("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaFriendlyInterfaceName"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaType"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaVLAN"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaIpAddress"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaNetworkMask"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaMACAddress"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStaState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceIfStatusMIBGroup = colubrisDeviceIfStatusMIBGroup.setStatus('current')
colubrisDeviceIfStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 24, 3, 2, 2)).setObjects(("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsRxBytes"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsRxPackets"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsRxErrors"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsTxBytes"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsTxPackets"), ("COLUBRIS-DEVICE-IF-MIB", "coDevIfStsTxErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceIfStatsMIBGroup = colubrisDeviceIfStatsMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-DEVICE-IF-MIB", coDevIfStsTxErrors=coDevIfStsTxErrors, coDevIfStaFriendlyInterfaceName=coDevIfStaFriendlyInterfaceName, coDeviceIfStatusTable=coDeviceIfStatusTable, coDeviceIfStatusGroup=coDeviceIfStatusGroup, coDevIfStsTxPackets=coDevIfStsTxPackets, coDeviceIfStatusEntry=coDeviceIfStatusEntry, coDevIfStsRxBytes=coDevIfStsRxBytes, coDevIfStsRxErrors=coDevIfStsRxErrors, colubrisDeviceIfMIBGroups=colubrisDeviceIfMIBGroups, coDevIfStsRxPackets=coDevIfStsRxPackets, coDevIfStaState=coDevIfStaState, colubrisDeviceIfMIBCompliances=colubrisDeviceIfMIBCompliances, coDeviceIfStatsTable=coDeviceIfStatsTable, PYSNMP_MODULE_ID=colubrisDeviceIfMIB, colubrisDeviceIfMIBNotifications=colubrisDeviceIfMIBNotifications, coDeviceIfStatsEntry=coDeviceIfStatsEntry, coDevIfStaIfIndex=coDevIfStaIfIndex, colubrisDeviceIfStatsMIBGroup=colubrisDeviceIfStatsMIBGroup, coDevIfStaMACAddress=coDevIfStaMACAddress, colubrisDeviceIfStatusMIBGroup=colubrisDeviceIfStatusMIBGroup, coDevIfStaType=coDevIfStaType, colubrisDeviceIfMIBObjects=colubrisDeviceIfMIBObjects, coDevIfStaVLAN=coDevIfStaVLAN, colubrisDeviceIfMIBConformance=colubrisDeviceIfMIBConformance, coDeviceIfStatsGroup=coDeviceIfStatsGroup, coDevIfStsTxBytes=coDevIfStsTxBytes, colubrisDeviceIfMIBNotificationPrefix=colubrisDeviceIfMIBNotificationPrefix, colubrisDeviceIfMIB=colubrisDeviceIfMIB, coDevIfStaIpAddress=coDevIfStaIpAddress, colubrisDeviceIfMIBCompliance=colubrisDeviceIfMIBCompliance, coDevIfStaNetworkMask=coDevIfStaNetworkMask)
