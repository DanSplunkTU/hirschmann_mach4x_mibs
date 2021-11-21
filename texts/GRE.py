#
# PySNMP MIB module GRE (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/GRE
# Produced by pysmi-1.1.3 at Sun Nov 21 00:26:46 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, Unsigned32, ObjectIdentity, ModuleIdentity, IpAddress, Gauge32, iso, Counter32, TimeTicks, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, NotificationType, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "IpAddress", "Gauge32", "iso", "Counter32", "TimeTicks", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "NotificationType", "MibIdentifier", "Integer32")
TruthValue, RowStatus, TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "MacAddress", "DisplayString")
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
mibBuilder.exportSymbols("GRE", greStatusLocalIpAddress=greStatusLocalIpAddress, greStatusRemoteNetwork=greStatusRemoteNetwork, greStatusConnectionState=greStatusConnectionState, greStatusRemoteIpAddress=greStatusRemoteIpAddress, greMib=greMib, greStatusRemoteNetworkEntry=greStatusRemoteNetworkEntry, greStatusRemoteNetworkTable=greStatusRemoteNetworkTable, PYSNMP_MODULE_ID=greInfo, greInfo=greInfo, productMib=productMib, greStatusTable=greStatusTable, greStatusEntry=greStatusEntry, peplink=peplink, greStatusRemoteNetworkId=greStatusRemoteNetworkId, greStatusId=greStatusId, greStatusProfileName=greStatusProfileName, greStatusTunnelRemoteIpAddress=greStatusTunnelRemoteIpAddress, greStatusRemoteSubnet=greStatusRemoteSubnet, generalMib=generalMib, greStatusTunnelLocalIpAddress=greStatusTunnelLocalIpAddress)
