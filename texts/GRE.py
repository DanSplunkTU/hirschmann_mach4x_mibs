#
# PySNMP MIB module GRE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/GRE
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
greMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11))
greInfo = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1))
if mibBuilder.loadTexts: greInfo.setLastUpdated('201502110000Z')
if mibBuilder.loadTexts: greInfo.setOrganization('PEPLINK')
if mibBuilder.loadTexts: greInfo.setContactInfo('')
if mibBuilder.loadTexts: greInfo.setDescription('MIB module for GRE.')
greStatusTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1), )
if mibBuilder.loadTexts: greStatusTable.setStatus('current')
if mibBuilder.loadTexts: greStatusTable.setDescription('GRE status table')
greStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1), ).setIndexNames((0, "GRE", "greStatusId"))
if mibBuilder.loadTexts: greStatusEntry.setStatus('current')
if mibBuilder.loadTexts: greStatusEntry.setDescription('An entry in the greStatusTable')
greStatusId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusId.setStatus('current')
if mibBuilder.loadTexts: greStatusId.setDescription('GRE ID.')
greStatusProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusProfileName.setStatus('current')
if mibBuilder.loadTexts: greStatusProfileName.setDescription('GRE profile name.')
greStatusConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("disconnected", 0), ("connected", 1), ("connecting", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusConnectionState.setStatus('current')
if mibBuilder.loadTexts: greStatusConnectionState.setDescription('GRE connection state.')
greStatusLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusLocalIpAddress.setStatus('current')
if mibBuilder.loadTexts: greStatusLocalIpAddress.setDescription('GRE local IP.')
greStatusRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusRemoteIpAddress.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteIpAddress.setDescription('GRE remote IP.')
greStatusTunnelLocalIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusTunnelLocalIpAddress.setStatus('current')
if mibBuilder.loadTexts: greStatusTunnelLocalIpAddress.setDescription('GRE tunnel local IP.')
greStatusTunnelRemoteIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusTunnelRemoteIpAddress.setStatus('current')
if mibBuilder.loadTexts: greStatusTunnelRemoteIpAddress.setDescription('GRE tunnel remote IP.')
greStatusRemoteNetworkTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2), )
if mibBuilder.loadTexts: greStatusRemoteNetworkTable.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteNetworkTable.setDescription('GRE status remote network table')
greStatusRemoteNetworkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1), ).setIndexNames((0, "GRE", "greStatusId"), (0, "GRE", "greStatusRemoteNetworkId"))
if mibBuilder.loadTexts: greStatusRemoteNetworkEntry.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteNetworkEntry.setDescription('An entry in the greStatusRemoteNetworkTable')
greStatusRemoteNetworkId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusRemoteNetworkId.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteNetworkId.setDescription('GRE remote network ID.')
greStatusRemoteNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusRemoteNetwork.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteNetwork.setDescription('GRE remote network IP.')
greStatusRemoteSubnet = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 11, 1, 2, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: greStatusRemoteSubnet.setStatus('current')
if mibBuilder.loadTexts: greStatusRemoteSubnet.setDescription('GRE remote network subnet.')
mibBuilder.exportSymbols("GRE", productMib=productMib, greStatusRemoteNetworkId=greStatusRemoteNetworkId, greStatusTunnelRemoteIpAddress=greStatusTunnelRemoteIpAddress, peplink=peplink, greStatusId=greStatusId, greStatusRemoteNetwork=greStatusRemoteNetwork, greStatusTable=greStatusTable, greStatusLocalIpAddress=greStatusLocalIpAddress, greStatusTunnelLocalIpAddress=greStatusTunnelLocalIpAddress, greStatusRemoteSubnet=greStatusRemoteSubnet, greStatusConnectionState=greStatusConnectionState, greInfo=greInfo, greStatusProfileName=greStatusProfileName, greStatusRemoteNetworkEntry=greStatusRemoteNetworkEntry, greStatusRemoteIpAddress=greStatusRemoteIpAddress, generalMib=generalMib, greStatusRemoteNetworkTable=greStatusRemoteNetworkTable, PYSNMP_MODULE_ID=greInfo, greMib=greMib, greStatusEntry=greStatusEntry)
