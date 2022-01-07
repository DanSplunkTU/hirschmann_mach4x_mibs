#
# PySNMP MIB module IPSEC-VPN (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/IPSEC-VPN
# Produced by pysmi-1.1.8 at Fri Jan  7 16:34:25 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Counter64, ObjectIdentity, MibIdentifier, Gauge32, Counter32, Integer32, TimeTicks, NotificationType, Unsigned32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Counter64", "ObjectIdentity", "MibIdentifier", "Gauge32", "Counter32", "Integer32", "TimeTicks", "NotificationType", "Unsigned32", "enterprises")
DisplayString, TruthValue, MacAddress, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "TextualConvention", "RowStatus")
peplink = MibIdentifier((1, 3, 6, 1, 4, 1, 23695))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1))
ipsecVpnMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13))
if mibBuilder.loadTexts: ipsecVpnMib.setLastUpdated('201812181200Z')
if mibBuilder.loadTexts: ipsecVpnMib.setOrganization('PEPLINK')
if mibBuilder.loadTexts: ipsecVpnMib.setContactInfo('')
if mibBuilder.loadTexts: ipsecVpnMib.setDescription('MIB module for IPSEC-VPN.')
ipsecVpnStatusTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1), )
if mibBuilder.loadTexts: ipsecVpnStatusTable.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnStatusTable.setDescription('IPsec VPN status table')
ipsecVpnStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1), ).setIndexNames((0, "IPSEC-VPN", "ipsecVpnStatusId"))
if mibBuilder.loadTexts: ipsecVpnStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnStatusEntry.setDescription('An entry in the ipsecVpnStatusTable')
ipsecVpnStatusId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnStatusId.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnStatusId.setDescription('IPsec VPN status ID.')
ipsecVpnStatusProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnStatusProfileName.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnStatusProfileName.setDescription('IPsec VPN profile name.')
ipsecVpnStatusConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("standby", 0), ("connecting", 1), ("established", 2), ("partially-established", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnStatusConnectionState.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnStatusConnectionState.setDescription('IPsec VPN connection state.')
ipsecVpnStatusWanName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnStatusWanName.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnStatusWanName.setDescription('IPsec VPN WAN name.')
ipsecVpnRouteStatusTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2), )
if mibBuilder.loadTexts: ipsecVpnRouteStatusTable.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnRouteStatusTable.setDescription('IPsec VPN route status table')
ipsecVpnRouteStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1), ).setIndexNames((0, "IPSEC-VPN", "ipsecVpnStatusId"), (0, "IPSEC-VPN", "ipsecVpnRouteStatusId"))
if mibBuilder.loadTexts: ipsecVpnRouteStatusEntry.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnRouteStatusEntry.setDescription('An entry in the ipsecVpnRouteStatusTable')
ipsecVpnRouteStatusId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteStatusId.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnRouteStatusId.setDescription('IPsec VPN route status ID.')
ipsecVpnRouteState = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("down", 0), ("up", 1), ("standby", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteState.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnRouteState.setDescription('IPsec VPN route state.')
ipsecVpnRouteStatusLocalNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteStatusLocalNetwork.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnRouteStatusLocalNetwork.setDescription('IPsec VPN route local network.')
ipsecVpnRouteStatusLocalSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteStatusLocalSubnet.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnRouteStatusLocalSubnet.setDescription('IPsec VPN route local subnet.')
ipsecVpnRouteStatusRemoteNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteStatusRemoteNetwork.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnRouteStatusRemoteNetwork.setDescription('IPsec VPN route remote network.')
ipsecVpnRouteStatusRemoteSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 13, 2, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ipsecVpnRouteStatusRemoteSubnet.setStatus('current')
if mibBuilder.loadTexts: ipsecVpnRouteStatusRemoteSubnet.setDescription('IPsec VPN route remote subnet.')
mibBuilder.exportSymbols("IPSEC-VPN", ipsecVpnRouteStatusEntry=ipsecVpnRouteStatusEntry, productMib=productMib, ipsecVpnStatusConnectionState=ipsecVpnStatusConnectionState, peplink=peplink, ipsecVpnStatusId=ipsecVpnStatusId, ipsecVpnStatusEntry=ipsecVpnStatusEntry, ipsecVpnRouteState=ipsecVpnRouteState, ipsecVpnRouteStatusTable=ipsecVpnRouteStatusTable, ipsecVpnRouteStatusLocalNetwork=ipsecVpnRouteStatusLocalNetwork, ipsecVpnStatusProfileName=ipsecVpnStatusProfileName, ipsecVpnRouteStatusId=ipsecVpnRouteStatusId, ipsecVpnStatusTable=ipsecVpnStatusTable, ipsecVpnRouteStatusLocalSubnet=ipsecVpnRouteStatusLocalSubnet, ipsecVpnMib=ipsecVpnMib, ipsecVpnRouteStatusRemoteSubnet=ipsecVpnRouteStatusRemoteSubnet, generalMib=generalMib, ipsecVpnRouteStatusRemoteNetwork=ipsecVpnRouteStatusRemoteNetwork, PYSNMP_MODULE_ID=ipsecVpnMib, ipsecVpnStatusWanName=ipsecVpnStatusWanName)
