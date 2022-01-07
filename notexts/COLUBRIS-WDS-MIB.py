#
# PySNMP MIB module COLUBRIS-WDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-WDS-MIB.my
# Produced by pysmi-1.1.8 at Fri Jan  7 16:25:15 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Counter64, Integer32, Unsigned32, ModuleIdentity, Counter32, NotificationType, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Integer32", "Unsigned32", "ModuleIdentity", "Counter32", "NotificationType", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "MibIdentifier", "TimeTicks")
TruthValue, MacAddress, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "MacAddress", "DisplayString", "TextualConvention")
colubrisWdsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 33))
if mibBuilder.loadTexts: colubrisWdsMIB.setLastUpdated('200801040000Z')
if mibBuilder.loadTexts: colubrisWdsMIB.setOrganization('Colubris Networks, Inc.')
colubrisWdsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1))
coWDSInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 1))
coWDSRadioGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2))
coWDSGroupGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3))
coWDSLinkGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4))
coWDSNetworkScanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5))
coWDSNumberOfGroup = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSNumberOfGroup.setStatus('current')
coWDSDynamicModeImplemented = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSDynamicModeImplemented.setStatus('current')
coWDSRadioTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2, 1), )
if mibBuilder.loadTexts: coWDSRadioTable.setStatus('current')
coWDSRadioEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2, 1, 1), ).setIndexNames((0, "COLUBRIS-WDS-MIB", "coWDSRadioIndex"))
if mibBuilder.loadTexts: coWDSRadioEntry.setStatus('current')
coWDSRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)))
if mibBuilder.loadTexts: coWDSRadioIndex.setStatus('current')
coWDSRadioAckDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2, 1, 1, 2), Unsigned32()).setUnits('km').setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSRadioAckDistance.setStatus('current')
coWDSRadioQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("disabled", 1), ("vlan", 2), ("veryHigh", 3), ("high", 4), ("normal", 5), ("low", 6), ("diffSrv", 7), ("tos", 8), ("ipQos", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSRadioQoS.setStatus('current')
coWDSGroupTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1), )
if mibBuilder.loadTexts: coWDSGroupTable.setStatus('current')
coWDSGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1), ).setIndexNames((0, "COLUBRIS-WDS-MIB", "coWDSGroupIndex"))
if mibBuilder.loadTexts: coWDSGroupEntry.setStatus('current')
coWDSGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: coWDSGroupIndex.setStatus('current')
coWDSGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSGroupName.setStatus('current')
coWDSGroupState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSGroupState.setStatus('current')
coWDSGroupSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("tkip", 3), ("aes", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSGroupSecurity.setStatus('current')
coWDSGroupAddressing = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("static", 1), ("dynamic", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSGroupAddressing.setStatus('current')
coWDSGroupStaticMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 6), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSGroupStaticMacAddress.setStatus('current')
coWDSGroupDynamicMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("none", 0), ("master", 1), ("slave", 2), ("alternateMaster", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSGroupDynamicMode.setStatus('current')
coWDSGroupDynamicGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 3, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSGroupDynamicGroupId.setStatus('current')
coWDSLinkTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1), )
if mibBuilder.loadTexts: coWDSLinkTable.setStatus('current')
coWDSLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1), ).setIndexNames((0, "COLUBRIS-WDS-MIB", "coWDSGroupIndex"), (0, "COLUBRIS-WDS-MIB", "coWDSLinkIndex"))
if mibBuilder.loadTexts: coWDSLinkEntry.setStatus('current')
coWDSLinkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 54)))
if mibBuilder.loadTexts: coWDSLinkIndex.setStatus('current')
coWDSLinkState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("acquiring", 2), ("inactive", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkState.setStatus('current')
coWDSLinkRadio = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkRadio.setStatus('current')
coWDSLinkPeerMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkPeerMacAddress.setStatus('current')
coWDSLinkMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkMaster.setStatus('current')
coWDSLinkAuthorized = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkAuthorized.setStatus('current')
coWDSLinkEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("tkip", 3), ("aes", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkEncryption.setStatus('current')
coWDSLinkIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkIdleTime.setStatus('current')
coWDSLinkSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 92))).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkSNR.setStatus('current')
coWDSLinkTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 10), Unsigned32()).setUnits('500Kb/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkTxRate.setStatus('current')
coWDSLinkRxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 11), Unsigned32()).setUnits('500Kb/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkRxRate.setStatus('current')
coWDSLinkIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkIfIndex.setStatus('current')
coWDSLinkHT = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkHT.setStatus('current')
coWDSLinkTxMCS = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkTxMCS.setStatus('current')
coWDSLinkRxMCS = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkRxMCS.setStatus('current')
coWDSLinkSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 16), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkSignal.setStatus('current')
coWDSLinkNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 4, 1, 1, 17), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSLinkNoise.setStatus('current')
coWDSNetworkScanTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1), )
if mibBuilder.loadTexts: coWDSNetworkScanTable.setStatus('current')
coWDSNetworkScanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1), ).setIndexNames((0, "COLUBRIS-WDS-MIB", "coWDSScanRadioIndex"), (0, "COLUBRIS-WDS-MIB", "coWDSScanPeerIndex"))
if mibBuilder.loadTexts: coWDSNetworkScanEntry.setStatus('current')
coWDSScanRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)))
if mibBuilder.loadTexts: coWDSScanRadioIndex.setStatus('current')
coWDSScanPeerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: coWDSScanPeerIndex.setStatus('current')
coWDSScanGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSScanGroupId.setStatus('current')
coWDSScanPeerMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSScanPeerMacAddress.setStatus('current')
coWDSScanChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 199))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSScanChannel.setStatus('current')
coWDSScanSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 92))).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSScanSNR.setStatus('current')
coWDSScanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("master", 1), ("slave", 2), ("alternateMaster", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSScanMode.setStatus('current')
coWDSScanAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 33, 1, 5, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coWDSScanAvailable.setStatus('current')
colubrisWdsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 33, 2))
colubrisWdsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 1))
colubrisWdsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2))
colubrisWdsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 1, 1)).setObjects(("COLUBRIS-WDS-MIB", "colubrisWDSInfoMIBGroup"), ("COLUBRIS-WDS-MIB", "colubrisWDSRadioMIBGroup"), ("COLUBRIS-WDS-MIB", "colubrisWDSGroupMIBGroup"), ("COLUBRIS-WDS-MIB", "colubrisWDSLinkMIBGroup"), ("COLUBRIS-WDS-MIB", "colubrisWDSScanMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisWdsMIBCompliance = colubrisWdsMIBCompliance.setStatus('current')
colubrisWDSInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2, 1)).setObjects(("COLUBRIS-WDS-MIB", "coWDSNumberOfGroup"), ("COLUBRIS-WDS-MIB", "coWDSDynamicModeImplemented"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisWDSInfoMIBGroup = colubrisWDSInfoMIBGroup.setStatus('current')
colubrisWDSRadioMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2, 2)).setObjects(("COLUBRIS-WDS-MIB", "coWDSRadioAckDistance"), ("COLUBRIS-WDS-MIB", "coWDSRadioQoS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisWDSRadioMIBGroup = colubrisWDSRadioMIBGroup.setStatus('current')
colubrisWDSGroupMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2, 3)).setObjects(("COLUBRIS-WDS-MIB", "coWDSGroupName"), ("COLUBRIS-WDS-MIB", "coWDSGroupState"), ("COLUBRIS-WDS-MIB", "coWDSGroupSecurity"), ("COLUBRIS-WDS-MIB", "coWDSGroupAddressing"), ("COLUBRIS-WDS-MIB", "coWDSGroupStaticMacAddress"), ("COLUBRIS-WDS-MIB", "coWDSGroupDynamicMode"), ("COLUBRIS-WDS-MIB", "coWDSGroupDynamicGroupId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisWDSGroupMIBGroup = colubrisWDSGroupMIBGroup.setStatus('current')
colubrisWDSLinkMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2, 4)).setObjects(("COLUBRIS-WDS-MIB", "coWDSLinkState"), ("COLUBRIS-WDS-MIB", "coWDSLinkRadio"), ("COLUBRIS-WDS-MIB", "coWDSLinkPeerMacAddress"), ("COLUBRIS-WDS-MIB", "coWDSLinkMaster"), ("COLUBRIS-WDS-MIB", "coWDSLinkAuthorized"), ("COLUBRIS-WDS-MIB", "coWDSLinkEncryption"), ("COLUBRIS-WDS-MIB", "coWDSLinkIdleTime"), ("COLUBRIS-WDS-MIB", "coWDSLinkSNR"), ("COLUBRIS-WDS-MIB", "coWDSLinkTxRate"), ("COLUBRIS-WDS-MIB", "coWDSLinkRxRate"), ("COLUBRIS-WDS-MIB", "coWDSLinkIfIndex"), ("COLUBRIS-WDS-MIB", "coWDSLinkHT"), ("COLUBRIS-WDS-MIB", "coWDSLinkTxMCS"), ("COLUBRIS-WDS-MIB", "coWDSLinkRxMCS"), ("COLUBRIS-WDS-MIB", "coWDSLinkSignal"), ("COLUBRIS-WDS-MIB", "coWDSLinkNoise"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisWDSLinkMIBGroup = colubrisWDSLinkMIBGroup.setStatus('current')
colubrisWDSScanMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 33, 2, 2, 5)).setObjects(("COLUBRIS-WDS-MIB", "coWDSScanGroupId"), ("COLUBRIS-WDS-MIB", "coWDSScanPeerMacAddress"), ("COLUBRIS-WDS-MIB", "coWDSScanChannel"), ("COLUBRIS-WDS-MIB", "coWDSScanSNR"), ("COLUBRIS-WDS-MIB", "coWDSScanMode"), ("COLUBRIS-WDS-MIB", "coWDSScanAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisWDSScanMIBGroup = colubrisWDSScanMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-WDS-MIB", colubrisWDSLinkMIBGroup=colubrisWDSLinkMIBGroup, coWDSRadioTable=coWDSRadioTable, coWDSDynamicModeImplemented=coWDSDynamicModeImplemented, coWDSLinkRxRate=coWDSLinkRxRate, colubrisWDSGroupMIBGroup=colubrisWDSGroupMIBGroup, coWDSLinkHT=coWDSLinkHT, coWDSScanPeerIndex=coWDSScanPeerIndex, colubrisWdsMIBCompliance=colubrisWdsMIBCompliance, colubrisWdsMIB=colubrisWdsMIB, coWDSLinkTxMCS=coWDSLinkTxMCS, coWDSLinkNoise=coWDSLinkNoise, coWDSLinkTable=coWDSLinkTable, coWDSScanAvailable=coWDSScanAvailable, coWDSRadioEntry=coWDSRadioEntry, coWDSRadioIndex=coWDSRadioIndex, coWDSRadioQoS=coWDSRadioQoS, coWDSLinkSNR=coWDSLinkSNR, coWDSRadioAckDistance=coWDSRadioAckDistance, coWDSScanGroupId=coWDSScanGroupId, coWDSLinkRadio=coWDSLinkRadio, colubrisWdsMIBGroups=colubrisWdsMIBGroups, colubrisWdsMIBObjects=colubrisWdsMIBObjects, coWDSGroupDynamicMode=coWDSGroupDynamicMode, coWDSScanRadioIndex=coWDSScanRadioIndex, colubrisWdsMIBConformance=colubrisWdsMIBConformance, coWDSGroupIndex=coWDSGroupIndex, coWDSNumberOfGroup=coWDSNumberOfGroup, coWDSGroupGroup=coWDSGroupGroup, coWDSGroupDynamicGroupId=coWDSGroupDynamicGroupId, colubrisWDSRadioMIBGroup=colubrisWDSRadioMIBGroup, coWDSLinkTxRate=coWDSLinkTxRate, coWDSGroupAddressing=coWDSGroupAddressing, coWDSGroupName=coWDSGroupName, coWDSLinkPeerMacAddress=coWDSLinkPeerMacAddress, coWDSNetworkScanEntry=coWDSNetworkScanEntry, coWDSRadioGroup=coWDSRadioGroup, coWDSScanPeerMacAddress=coWDSScanPeerMacAddress, coWDSScanChannel=coWDSScanChannel, coWDSLinkState=coWDSLinkState, coWDSGroupState=coWDSGroupState, coWDSLinkSignal=coWDSLinkSignal, coWDSLinkIfIndex=coWDSLinkIfIndex, coWDSGroupEntry=coWDSGroupEntry, coWDSInfoGroup=coWDSInfoGroup, coWDSLinkIndex=coWDSLinkIndex, coWDSGroupTable=coWDSGroupTable, PYSNMP_MODULE_ID=colubrisWdsMIB, coWDSGroupSecurity=coWDSGroupSecurity, coWDSNetworkScanTable=coWDSNetworkScanTable, coWDSNetworkScanGroup=coWDSNetworkScanGroup, colubrisWDSScanMIBGroup=colubrisWDSScanMIBGroup, coWDSLinkEncryption=coWDSLinkEncryption, coWDSLinkEntry=coWDSLinkEntry, colubrisWdsMIBCompliances=colubrisWdsMIBCompliances, coWDSLinkMaster=coWDSLinkMaster, coWDSLinkGroup=coWDSLinkGroup, coWDSLinkIdleTime=coWDSLinkIdleTime, coWDSGroupStaticMacAddress=coWDSGroupStaticMacAddress, coWDSLinkAuthorized=coWDSLinkAuthorized, coWDSScanSNR=coWDSScanSNR, coWDSScanMode=coWDSScanMode, coWDSLinkRxMCS=coWDSLinkRxMCS, colubrisWDSInfoMIBGroup=colubrisWDSInfoMIBGroup)
