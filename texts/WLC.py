#
# PySNMP MIB module WLC (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/WLC
# Produced by pysmi-1.1.8 at Sun Jan 16 00:42:40 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, enterprises, Counter32, Gauge32, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, iso, ObjectIdentity, Unsigned32, TimeTicks, IpAddress, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "enterprises", "Counter32", "Gauge32", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "iso", "ObjectIdentity", "Unsigned32", "TimeTicks", "IpAddress", "Counter64", "Integer32")
DisplayString, TextualConvention, MacAddress, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "MacAddress", "RowStatus", "TruthValue")
peplink = MibIdentifier((1, 3, 6, 1, 4, 1, 23695))
wlc = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 4))
if mibBuilder.loadTexts: wlc.setLastUpdated('2011081900Z')
if mibBuilder.loadTexts: wlc.setOrganization('PEPLINK')
if mibBuilder.loadTexts: wlc.setContactInfo('')
if mibBuilder.loadTexts: wlc.setDescription('MIB module for WLC.')
wlcSystemInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 4, 1))
wlcSystemBasicInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 4, 1, 1))
wlcApMgmtEnable = MibScalar((1, 3, 6, 1, 4, 1, 23695, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApMgmtEnable.setStatus('current')
if mibBuilder.loadTexts: wlcApMgmtEnable.setDescription('WLC AP Mangement Enable')
wlcRemoteApMgmtEnable = MibScalar((1, 3, 6, 1, 4, 1, 23695, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcRemoteApMgmtEnable.setStatus('current')
if mibBuilder.loadTexts: wlcRemoteApMgmtEnable.setDescription('WLC Remote AP Management Enable')
wlcMaxNumAp = MibScalar((1, 3, 6, 1, 4, 1, 23695, 4, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcMaxNumAp.setStatus('current')
if mibBuilder.loadTexts: wlcMaxNumAp.setDescription('WLC Maximum Number of Supported AP Licensed')
wlcNumApProfile = MibScalar((1, 3, 6, 1, 4, 1, 23695, 4, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNumApProfile.setStatus('current')
if mibBuilder.loadTexts: wlcNumApProfile.setDescription('WLC Number of AP Profile Created')
wlcNumWlanNetwork = MibScalar((1, 3, 6, 1, 4, 1, 23695, 4, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNumWlanNetwork.setStatus('current')
if mibBuilder.loadTexts: wlcNumWlanNetwork.setDescription('WLC Number of WLAN Network Created')
wlcNumApReg = MibScalar((1, 3, 6, 1, 4, 1, 23695, 4, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNumApReg.setStatus('current')
if mibBuilder.loadTexts: wlcNumApReg.setDescription('WLC Number of AP Registered')
wlcNumApOnline = MibScalar((1, 3, 6, 1, 4, 1, 23695, 4, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNumApOnline.setStatus('current')
if mibBuilder.loadTexts: wlcNumApOnline.setDescription('WLC Current Number of Online AP')
wlcNumAssocSta = MibScalar((1, 3, 6, 1, 4, 1, 23695, 4, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNumAssocSta.setStatus('current')
if mibBuilder.loadTexts: wlcNumAssocSta.setDescription('WLC Current Number of Associated WLAN Station')
wlcApMgmtInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 4, 2))
wlcApGroupInfoTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 4, 2, 1), )
if mibBuilder.loadTexts: wlcApGroupInfoTable.setStatus('current')
if mibBuilder.loadTexts: wlcApGroupInfoTable.setDescription('WLC AP Group Information Table')
wlcApGroupInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 4, 2, 1, 1), ).setIndexNames((0, "WLC", "wlcApGrpId"))
if mibBuilder.loadTexts: wlcApGroupInfoEntry.setStatus('current')
if mibBuilder.loadTexts: wlcApGroupInfoEntry.setDescription('An entry in the wlcApGroupInfoTable')
wlcApGrpId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpId.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpId.setDescription('WLC AP Group ID')
wlcApGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpName.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpName.setDescription('WLC AP Group Name')
wlcApGrpBand24WlanNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpBand24WlanNetwork.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpBand24WlanNetwork.setDescription('WLC Current Number of 2.4GHz Band WLAN Network')
wlcApGrpBand50WlanNetwork = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpBand50WlanNetwork.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpBand50WlanNetwork.setDescription('WLC Current Number of 5GHz Band WLAN Network')
wlcApGrpNumApReg = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpNumApReg.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpNumApReg.setDescription('WLC Number of Registered AP in this AP Group')
wlcApGrpNumApOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpNumApOnline.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpNumApOnline.setDescription('WLC Number of Online AP in this AP Group')
wlcApGrpNumAssocSta = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpNumAssocSta.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpNumAssocSta.setDescription('WLC Number of Associated WLAN Stations in this AP Group')
wlcApGrpMgmtVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpMgmtVlan.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpMgmtVlan.setDescription('WLC Managment VLAN ID of this AP Group')
wlcApGroupStatTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 4, 2, 2), )
if mibBuilder.loadTexts: wlcApGroupStatTable.setStatus('current')
if mibBuilder.loadTexts: wlcApGroupStatTable.setDescription('WLAN AP Group Statistics Table')
wlcApGroupStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 4, 2, 2, 1), ).setIndexNames((0, "WLC", "wlcApGrpId"), (0, "WLC", "wlcApGrpStatBand"))
if mibBuilder.loadTexts: wlcApGroupStatEntry.setStatus('current')
if mibBuilder.loadTexts: wlcApGroupStatEntry.setDescription('An entry in the wlcApGroupStatTable')
wlcApGrpStatName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpStatName.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpStatName.setDescription('WLC AP Group Name')
wlcApGrpStatBand = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("band24", 1), ("band50", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpStatBand.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpStatBand.setDescription('WLC AP Group Statistics of Frequency Band')
wlcApGrpStatNumTxPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpStatNumTxPkt.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpStatNumTxPkt.setDescription('WLC AP Group Number of Transmitted Packets')
wlcApGrpStatNumTxByte = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpStatNumTxByte.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpStatNumTxByte.setDescription('WLC AP Group Number of Transmitted Bytes')
wlcApGrpStatNumRxPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpStatNumRxPkt.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpStatNumRxPkt.setDescription('WLC AP Group Number of Received Packets')
wlcApGrpStatNumRxByte = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApGrpStatNumRxByte.setStatus('current')
if mibBuilder.loadTexts: wlcApGrpStatNumRxByte.setDescription('WLC AP Group Number of Received Bytes')
wlcWlanNetworkInfoTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 4, 2, 3), )
if mibBuilder.loadTexts: wlcWlanNetworkInfoTable.setStatus('current')
if mibBuilder.loadTexts: wlcWlanNetworkInfoTable.setDescription('WLC WLAN Network Information Table')
wlcWlanNetworkInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 4, 2, 3, 1), ).setIndexNames((0, "WLC", "wlcWlanNetworkId"))
if mibBuilder.loadTexts: wlcWlanNetworkInfoEntry.setStatus('current')
if mibBuilder.loadTexts: wlcWlanNetworkInfoEntry.setDescription('An entry in the wlcWlanNetworkInfoTable')
wlcWlanNetworkId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanNetworkId.setStatus('current')
if mibBuilder.loadTexts: wlcWlanNetworkId.setDescription('WLC WLAN Network ID')
wlcWlanEssid = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 3, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanEssid.setStatus('current')
if mibBuilder.loadTexts: wlcWlanEssid.setDescription('WLC WLAN Network ESSID')
wlcWlanSecMode = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("wep", 1), ("legacy8021x", 2), ("wpaMix", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanSecMode.setStatus('current')
if mibBuilder.loadTexts: wlcWlanSecMode.setDescription('WLC WLAN Network Security Mode')
wlcWlanNumApOnline = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanNumApOnline.setStatus('current')
if mibBuilder.loadTexts: wlcWlanNumApOnline.setDescription('WLC Current Number of Online AP in this WLAN Network')
wlcWlanNumAssocSta = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanNumAssocSta.setStatus('current')
if mibBuilder.loadTexts: wlcWlanNumAssocSta.setDescription('WLC Current Number of Associated Stations in this WLAN Network')
wlcWlanVlanPool = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 3, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanVlanPool.setStatus('current')
if mibBuilder.loadTexts: wlcWlanVlanPool.setDescription('WLC VLAN Pool Setting of this WLAN Network')
wlcWlanNetworkStatTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 4, 2, 4), )
if mibBuilder.loadTexts: wlcWlanNetworkStatTable.setStatus('current')
if mibBuilder.loadTexts: wlcWlanNetworkStatTable.setDescription('WLC WLAN Network Statistics Table')
wlcWlanNetworkStatEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 4, 2, 4, 1), ).setIndexNames((0, "WLC", "wlcWlanNetworkId"), (0, "WLC", "wlcWlanStatBand"))
if mibBuilder.loadTexts: wlcWlanNetworkStatEntry.setStatus('current')
if mibBuilder.loadTexts: wlcWlanNetworkStatEntry.setDescription('An entry in the wlcWlanNetworkInfoTable')
wlcWlanStatEssid = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 4, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanStatEssid.setStatus('current')
if mibBuilder.loadTexts: wlcWlanStatEssid.setDescription('WLC WLAN Network ESSID')
wlcWlanStatBand = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("band24", 1), ("band50", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanStatBand.setStatus('current')
if mibBuilder.loadTexts: wlcWlanStatBand.setDescription('WLC Statistics of WLAN Network in Frequency Band')
wlcWlanStatNumTxPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 4, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanStatNumTxPkt.setStatus('current')
if mibBuilder.loadTexts: wlcWlanStatNumTxPkt.setDescription('WLC WLAN Network Number of Transmitted Packets')
wlcWlanStatNumTxByte = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 4, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanStatNumTxByte.setStatus('current')
if mibBuilder.loadTexts: wlcWlanStatNumTxByte.setDescription('WLC WLAN Network Number of Transmitted Bytes')
wlcWlanStatNumRxPkt = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 4, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanStatNumRxPkt.setStatus('current')
if mibBuilder.loadTexts: wlcWlanStatNumRxPkt.setDescription('WLC WLAN Network Number of Received Packets')
wlcWlanStatNumRxByte = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 2, 4, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcWlanStatNumRxByte.setStatus('current')
if mibBuilder.loadTexts: wlcWlanStatNumRxByte.setDescription('WLC WLAN Network Number of Received Bytes')
wlcWlanNeighDeviceInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 4, 3))
wlcWlanNeighApTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1), )
if mibBuilder.loadTexts: wlcWlanNeighApTable.setStatus('current')
if mibBuilder.loadTexts: wlcWlanNeighApTable.setDescription('WLC Neighbor AP Table')
wlcWlanNeighApEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1, 1), ).setIndexNames((0, "WLC", "wlcNeighApBssid"))
if mibBuilder.loadTexts: wlcWlanNeighApEntry.setStatus('current')
if mibBuilder.loadTexts: wlcWlanNeighApEntry.setDescription('An entry in the wlcWlanNeighApTable')
wlcNeighApBssid = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNeighApBssid.setStatus('current')
if mibBuilder.loadTexts: wlcNeighApBssid.setDescription('WLC Neighbor AP BSSID')
wlcNeighApEssid = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNeighApEssid.setStatus('current')
if mibBuilder.loadTexts: wlcNeighApEssid.setDescription('WLC Neighbor AP ESSID')
wlcNeighApChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNeighApChannel.setStatus('current')
if mibBuilder.loadTexts: wlcNeighApChannel.setDescription('WLC Neighbor AP Channel')
wlcNeighApEncytMode = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("wep", 1), ("wpa", 2), ("wpa2", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNeighApEncytMode.setStatus('current')
if mibBuilder.loadTexts: wlcNeighApEncytMode.setDescription('WLC Neighbor AP Encryption Mode')
wlcNeighNumApSeen = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNeighNumApSeen.setStatus('current')
if mibBuilder.loadTexts: wlcNeighNumApSeen.setDescription('WLC Number of AP which can detect the Neighbor AP')
wlcNeighNearestAp = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNeighNearestAp.setStatus('current')
if mibBuilder.loadTexts: wlcNeighNearestAp.setDescription('WLC Nearest AP Serial Number')
wlcNeighNearestApRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNeighNearestApRssi.setStatus('current')
if mibBuilder.loadTexts: wlcNeighNearestApRssi.setDescription('WLC Neighbor Signal Strength received by the Nearest AP')
wlcNeighFurthestAp = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(12, 12)).setFixedLength(12)).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNeighFurthestAp.setStatus('current')
if mibBuilder.loadTexts: wlcNeighFurthestAp.setDescription('WLC Furthest AP Serial Number')
wlcNeighFurthestApRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 3, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcNeighFurthestApRssi.setStatus('current')
if mibBuilder.loadTexts: wlcNeighFurthestApRssi.setDescription('WLC Neighbor Signal Strength received by the Furthest AP')
wlcApInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 4, 4))
wlcApInfoTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1), )
if mibBuilder.loadTexts: wlcApInfoTable.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoTable.setDescription('WLAN Managed AP Information Table')
wlcApInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1, 1), ).setIndexNames((0, "WLC", "wlcApInfoApId"))
if mibBuilder.loadTexts: wlcApInfoEntry.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoEntry.setDescription('An entry in the wlcApInfoTable')
wlcApInfoApId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApInfoApId.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoApId.setDescription('WLC AP ID')
wlcApInfoApSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApInfoApSerialNumber.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoApSerialNumber.setDescription('WLC AP Serial Number')
wlcApInfoApName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApInfoApName.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoApName.setDescription('WLC AP Name')
wlcApInfoApModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApInfoApModelName.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoApModelName.setDescription('WLC AP Model Name')
wlcApInfoApFirmwareVer = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApInfoApFirmwareVer.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoApFirmwareVer.setDescription('WLC AP Firmare Version')
wlcApInfoApStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("offline", 0), ("online", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApInfoApStatus.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoApStatus.setDescription('WLC Current AP Status')
wlcApInfoApIp = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1, 1, 7), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApInfoApIp.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoApIp.setDescription('WLC Current AP Ip Address')
wlcApInfoApGrpID = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApInfoApGrpID.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoApGrpID.setDescription('WLC AP Configured AP Group ID')
wlcApInfoApGrpName = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 4, 4, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wlcApInfoApGrpName.setStatus('current')
if mibBuilder.loadTexts: wlcApInfoApGrpName.setDescription('WLC AP Configured AP Group Name')
mibBuilder.exportSymbols("WLC", wlcNeighNumApSeen=wlcNeighNumApSeen, wlcApInfoApName=wlcApInfoApName, peplink=peplink, wlcApInfoApFirmwareVer=wlcApInfoApFirmwareVer, wlcWlanStatNumTxPkt=wlcWlanStatNumTxPkt, wlcApInfoApGrpID=wlcApInfoApGrpID, wlcApGroupInfoEntry=wlcApGroupInfoEntry, wlcApGrpStatNumTxPkt=wlcApGrpStatNumTxPkt, wlcNumApOnline=wlcNumApOnline, wlcApGrpNumApOnline=wlcApGrpNumApOnline, wlcNeighNearestAp=wlcNeighNearestAp, wlcApGrpStatName=wlcApGrpStatName, wlcWlanNeighApTable=wlcWlanNeighApTable, wlcApGrpStatNumRxByte=wlcApGrpStatNumRxByte, wlcNeighApEssid=wlcNeighApEssid, wlcNeighApEncytMode=wlcNeighApEncytMode, wlcApInfoEntry=wlcApInfoEntry, wlcWlanNetworkInfoEntry=wlcWlanNetworkInfoEntry, wlcApInfoApIp=wlcApInfoApIp, wlcApInfoApSerialNumber=wlcApInfoApSerialNumber, wlcWlanNetworkStatEntry=wlcWlanNetworkStatEntry, wlcWlanNeighApEntry=wlcWlanNeighApEntry, wlcApGrpStatNumRxPkt=wlcApGrpStatNumRxPkt, wlcWlanStatBand=wlcWlanStatBand, wlcWlanNeighDeviceInfo=wlcWlanNeighDeviceInfo, wlcWlanNetworkInfoTable=wlcWlanNetworkInfoTable, wlcWlanVlanPool=wlcWlanVlanPool, wlcWlanEssid=wlcWlanEssid, wlcWlanStatNumRxByte=wlcWlanStatNumRxByte, wlcMaxNumAp=wlcMaxNumAp, wlcApInfoApGrpName=wlcApInfoApGrpName, wlcRemoteApMgmtEnable=wlcRemoteApMgmtEnable, wlcWlanStatEssid=wlcWlanStatEssid, wlcApGroupStatEntry=wlcApGroupStatEntry, wlcWlanStatNumRxPkt=wlcWlanStatNumRxPkt, wlcApGrpStatNumTxByte=wlcApGrpStatNumTxByte, wlcApMgmtEnable=wlcApMgmtEnable, wlcNumWlanNetwork=wlcNumWlanNetwork, wlcApGrpName=wlcApGrpName, wlcWlanSecMode=wlcWlanSecMode, wlcApMgmtInfo=wlcApMgmtInfo, wlcWlanNetworkStatTable=wlcWlanNetworkStatTable, wlcWlanNumApOnline=wlcWlanNumApOnline, wlcApGrpBand24WlanNetwork=wlcApGrpBand24WlanNetwork, wlcWlanStatNumTxByte=wlcWlanStatNumTxByte, wlcApInfoTable=wlcApInfoTable, wlcApGrpStatBand=wlcApGrpStatBand, wlcNeighFurthestAp=wlcNeighFurthestAp, wlcNeighNearestApRssi=wlcNeighNearestApRssi, wlcApInfoApId=wlcApInfoApId, wlcApGroupStatTable=wlcApGroupStatTable, wlcApGrpMgmtVlan=wlcApGrpMgmtVlan, wlcWlanNumAssocSta=wlcWlanNumAssocSta, wlcNeighApBssid=wlcNeighApBssid, wlcApInfoApStatus=wlcApInfoApStatus, wlcApInfo=wlcApInfo, wlcSystemBasicInfo=wlcSystemBasicInfo, wlcNumApProfile=wlcNumApProfile, PYSNMP_MODULE_ID=wlc, wlc=wlc, wlcApGrpId=wlcApGrpId, wlcNeighApChannel=wlcNeighApChannel, wlcNumApReg=wlcNumApReg, wlcApGroupInfoTable=wlcApGroupInfoTable, wlcNumAssocSta=wlcNumAssocSta, wlcWlanNetworkId=wlcWlanNetworkId, wlcApInfoApModelName=wlcApInfoApModelName, wlcSystemInfo=wlcSystemInfo, wlcApGrpBand50WlanNetwork=wlcApGrpBand50WlanNetwork, wlcApGrpNumApReg=wlcApGrpNumApReg, wlcNeighFurthestApRssi=wlcNeighFurthestApRssi, wlcApGrpNumAssocSta=wlcApGrpNumAssocSta)
