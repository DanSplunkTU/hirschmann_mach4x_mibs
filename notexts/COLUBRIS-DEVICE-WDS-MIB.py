#
# PySNMP MIB module COLUBRIS-DEVICE-WDS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-DEVICE-WDS-MIB.my
# Produced by pysmi-1.1.3 at Sun Nov 21 00:37:16 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
coDevDisIndex, = mibBuilder.importSymbols("COLUBRIS-DEVICE-MIB", "coDevDisIndex")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibIdentifier, iso, ObjectIdentity, Bits, TimeTicks, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, NotificationType, IpAddress, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "ObjectIdentity", "Bits", "TimeTicks", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "NotificationType", "IpAddress", "Gauge32", "Counter32")
DisplayString, TruthValue, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "MacAddress", "TextualConvention")
colubrisDeviceWdsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 34))
if mibBuilder.loadTexts: colubrisDeviceWdsMIB.setLastUpdated('200801040000Z')
if mibBuilder.loadTexts: colubrisDeviceWdsMIB.setOrganization('Colubris Networks, Inc.')
colubrisDeviceWdsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1))
coDeviceWDSInfoGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 2))
coDeviceWDSRadioGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3))
coDeviceWDSGroupGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4))
coDeviceWDSLinkGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5))
coDeviceWDSNetworkScanGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6))
coDeviceWdsInfoTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 2, 1), )
if mibBuilder.loadTexts: coDeviceWdsInfoTable.setStatus('current')
coDeviceWdsInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 2, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"))
if mibBuilder.loadTexts: coDeviceWdsInfoEntry.setStatus('current')
coDevWDSInfoMaxNumberOfGroup = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSInfoMaxNumberOfGroup.setStatus('current')
coDeviceWDSRadioTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3, 1), )
if mibBuilder.loadTexts: coDeviceWDSRadioTable.setStatus('current')
coDeviceWDSRadioEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSRadioIndex"))
if mibBuilder.loadTexts: coDeviceWDSRadioEntry.setStatus('current')
coDevWDSRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)))
if mibBuilder.loadTexts: coDevWDSRadioIndex.setStatus('current')
coDevWDSRadioAckDistance = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3, 1, 1, 2), Unsigned32()).setUnits('km').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSRadioAckDistance.setStatus('current')
coDevWDSRadioQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("disabled", 1), ("vlan", 2), ("veryHigh", 3), ("high", 4), ("normal", 5), ("low", 6), ("diffSrv", 7), ("tos", 8), ("ipQos", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSRadioQoS.setStatus('current')
coDeviceWDSGroupTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1), )
if mibBuilder.loadTexts: coDeviceWDSGroupTable.setStatus('current')
coDeviceWDSGroupEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupIndex"))
if mibBuilder.loadTexts: coDeviceWDSGroupEntry.setStatus('current')
coDevWDSGroupIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: coDevWDSGroupIndex.setStatus('current')
coDevWDSGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSGroupName.setStatus('current')
coDevWDSGroupState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("discovery", 1), ("negotiation", 2), ("acquisition", 3), ("locked", 4), ("shutdown", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSGroupState.setStatus('current')
coDevWDSGroupSecurity = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("tkip", 3), ("aes", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSGroupSecurity.setStatus('current')
coDevWDSGroupDynamicMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("master", 1), ("slave", 2), ("alternateMaster", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSGroupDynamicMode.setStatus('current')
coDevWDSGroupDynamicGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 4, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSGroupDynamicGroupId.setStatus('current')
coDeviceWDSLinkStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1), )
if mibBuilder.loadTexts: coDeviceWDSLinkStatusTable.setStatus('current')
coDeviceWDSLinkStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupIndex"), (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaIndex"))
if mibBuilder.loadTexts: coDeviceWDSLinkStatusEntry.setStatus('current')
coDevWDSLinkStaIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coDevWDSLinkStaIndex.setStatus('current')
coDevWDSLinkStaState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("down", 1), ("acquiring", 2), ("inactive", 3), ("active", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaState.setStatus('current')
coDevWDSLinkStaRadio = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaRadio.setStatus('current')
coDevWDSLinkStaPeerMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaPeerMacAddress.setStatus('current')
coDevWDSLinkStaMaster = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaMaster.setStatus('current')
coDevWDSLinkStaAuthorized = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaAuthorized.setStatus('current')
coDevWDSLinkStaEncryption = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("wep", 2), ("tkip", 3), ("aes", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaEncryption.setStatus('current')
coDevWDSLinkStaIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 8), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaIdleTime.setStatus('current')
coDevWDSLinkStaSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 92))).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaSNR.setStatus('current')
coDevWDSLinkStaTxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 10), Unsigned32()).setUnits('500Kb/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaTxRate.setStatus('current')
coDevWDSLinkStaRxRate = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 11), Unsigned32()).setUnits('500Kb/s').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaRxRate.setStatus('current')
coDevWDSLinkStaIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaIfIndex.setStatus('current')
coDevWDSLinkStaHT = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaHT.setStatus('current')
coDevWDSLinkStaTxMCS = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaTxMCS.setStatus('current')
coDevWDSLinkStaRxMCS = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaRxMCS.setStatus('current')
coDevWDSLinkStaSignal = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 16), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaSignal.setStatus('current')
coDevWDSLinkStaNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 1, 1, 17), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStaNoise.setStatus('current')
coDeviceWDSLinkStatsRatesTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2), )
if mibBuilder.loadTexts: coDeviceWDSLinkStatsRatesTable.setStatus('current')
coDeviceWDSLinkStatsRatesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1), )
coDeviceWDSLinkStatusEntry.registerAugmentions(("COLUBRIS-DEVICE-WDS-MIB", "coDeviceWDSLinkStatsRatesEntry"))
coDeviceWDSLinkStatsRatesEntry.setIndexNames(*coDeviceWDSLinkStatusEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceWDSLinkStatsRatesEntry.setStatus('current')
coDevWDSLinkStsPktsTxRate1 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate1.setStatus('current')
coDevWDSLinkStsPktsTxRate2 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate2.setStatus('current')
coDevWDSLinkStsPktsTxRate5dot5 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate5dot5.setStatus('current')
coDevWDSLinkStsPktsTxRate11 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate11.setStatus('current')
coDevWDSLinkStsPktsTxRate6 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate6.setStatus('current')
coDevWDSLinkStsPktsTxRate9 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate9.setStatus('current')
coDevWDSLinkStsPktsTxRate12 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate12.setStatus('current')
coDevWDSLinkStsPktsTxRate18 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate18.setStatus('current')
coDevWDSLinkStsPktsTxRate24 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate24.setStatus('current')
coDevWDSLinkStsPktsTxRate36 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate36.setStatus('current')
coDevWDSLinkStsPktsTxRate48 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate48.setStatus('current')
coDevWDSLinkStsPktsTxRate54 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxRate54.setStatus('current')
coDevWDSLinkStsPktsRxRate1 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate1.setStatus('current')
coDevWDSLinkStsPktsRxRate2 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate2.setStatus('current')
coDevWDSLinkStsPktsRxRate5dot5 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate5dot5.setStatus('current')
coDevWDSLinkStsPktsRxRate11 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate11.setStatus('current')
coDevWDSLinkStsPktsRxRate6 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate6.setStatus('current')
coDevWDSLinkStsPktsRxRate9 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate9.setStatus('current')
coDevWDSLinkStsPktsRxRate12 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate12.setStatus('current')
coDevWDSLinkStsPktsRxRate18 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate18.setStatus('current')
coDevWDSLinkStsPktsRxRate24 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate24.setStatus('current')
coDevWDSLinkStsPktsRxRate36 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate36.setStatus('current')
coDevWDSLinkStsPktsRxRate48 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate48.setStatus('current')
coDevWDSLinkStsPktsRxRate54 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 2, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxRate54.setStatus('current')
coDeviceWDSLinkStatsHTRatesTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3), )
if mibBuilder.loadTexts: coDeviceWDSLinkStatsHTRatesTable.setStatus('current')
coDeviceWDSLinkStatsHTRatesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1), )
coDeviceWDSLinkStatusEntry.registerAugmentions(("COLUBRIS-DEVICE-WDS-MIB", "coDeviceWDSLinkStatsHTRatesEntry"))
coDeviceWDSLinkStatsHTRatesEntry.setIndexNames(*coDeviceWDSLinkStatusEntry.getIndexNames())
if mibBuilder.loadTexts: coDeviceWDSLinkStatsHTRatesEntry.setStatus('current')
coDevWDSLinkStsPktsTxMCS0 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS0.setStatus('current')
coDevWDSLinkStsPktsTxMCS1 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS1.setStatus('current')
coDevWDSLinkStsPktsTxMCS2 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS2.setStatus('current')
coDevWDSLinkStsPktsTxMCS3 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS3.setStatus('current')
coDevWDSLinkStsPktsTxMCS4 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS4.setStatus('current')
coDevWDSLinkStsPktsTxMCS5 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS5.setStatus('current')
coDevWDSLinkStsPktsTxMCS6 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS6.setStatus('current')
coDevWDSLinkStsPktsTxMCS7 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS7.setStatus('current')
coDevWDSLinkStsPktsTxMCS8 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS8.setStatus('current')
coDevWDSLinkStsPktsTxMCS9 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS9.setStatus('current')
coDevWDSLinkStsPktsTxMCS10 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS10.setStatus('current')
coDevWDSLinkStsPktsTxMCS11 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 12), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS11.setStatus('current')
coDevWDSLinkStsPktsTxMCS12 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 13), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS12.setStatus('current')
coDevWDSLinkStsPktsTxMCS13 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 14), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS13.setStatus('current')
coDevWDSLinkStsPktsTxMCS14 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 15), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS14.setStatus('current')
coDevWDSLinkStsPktsTxMCS15 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsTxMCS15.setStatus('current')
coDevWDSLinkStsPktsRxMCS0 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 17), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS0.setStatus('current')
coDevWDSLinkStsPktsRxMCS1 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 18), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS1.setStatus('current')
coDevWDSLinkStsPktsRxMCS2 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 19), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS2.setStatus('current')
coDevWDSLinkStsPktsRxMCS3 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 20), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS3.setStatus('current')
coDevWDSLinkStsPktsRxMCS4 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 21), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS4.setStatus('current')
coDevWDSLinkStsPktsRxMCS5 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 22), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS5.setStatus('current')
coDevWDSLinkStsPktsRxMCS6 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 23), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS6.setStatus('current')
coDevWDSLinkStsPktsRxMCS7 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 24), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS7.setStatus('current')
coDevWDSLinkStsPktsRxMCS8 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 25), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS8.setStatus('current')
coDevWDSLinkStsPktsRxMCS9 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 26), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS9.setStatus('current')
coDevWDSLinkStsPktsRxMCS10 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 27), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS10.setStatus('current')
coDevWDSLinkStsPktsRxMCS11 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 28), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS11.setStatus('current')
coDevWDSLinkStsPktsRxMCS12 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 29), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS12.setStatus('current')
coDevWDSLinkStsPktsRxMCS13 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 30), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS13.setStatus('current')
coDevWDSLinkStsPktsRxMCS14 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 31), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS14.setStatus('current')
coDevWDSLinkStsPktsRxMCS15 = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 5, 3, 1, 32), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSLinkStsPktsRxMCS15.setStatus('current')
coDeviceWDSNetworkScanTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1), )
if mibBuilder.loadTexts: coDeviceWDSNetworkScanTable.setStatus('current')
coDeviceWDSNetworkScanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1), ).setIndexNames((0, "COLUBRIS-DEVICE-MIB", "coDevDisIndex"), (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanRadioIndex"), (0, "COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanPeerIndex"))
if mibBuilder.loadTexts: coDeviceWDSNetworkScanEntry.setStatus('current')
coDevWDSScanRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 3)))
if mibBuilder.loadTexts: coDevWDSScanRadioIndex.setStatus('current')
coDevWDSScanPeerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 100)))
if mibBuilder.loadTexts: coDevWDSScanPeerIndex.setStatus('current')
coDevWDSScanGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSScanGroupId.setStatus('current')
coDevWDSScanPeerMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSScanPeerMacAddress.setStatus('current')
coDevWDSScanChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 199))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSScanChannel.setStatus('current')
coDevWDSScanSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 92))).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSScanSNR.setStatus('current')
coDevWDSScanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("master", 1), ("slave", 2), ("alternateMaster", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSScanMode.setStatus('current')
coDevWDSScanAvailable = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 34, 1, 6, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coDevWDSScanAvailable.setStatus('current')
colubrisDeviceWdsMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 2))
colubrisDeviceWdsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 2, 0))
colubrisDeviceWdsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 3))
colubrisDeviceWdsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 1))
colubrisDeviceWdsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2))
colubrisDeviceWdsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 1, 1)).setObjects(("COLUBRIS-DEVICE-WDS-MIB", "colubrisDeviceWdsInfoMIBGroup"), ("COLUBRIS-DEVICE-WDS-MIB", "colubrisDeviceWdsRadioMIBGroup"), ("COLUBRIS-DEVICE-WDS-MIB", "colubrisDeviceWdsGroupMIBGroup"), ("COLUBRIS-DEVICE-WDS-MIB", "colubrisDeviceWdsLinkMIBGroup"), ("COLUBRIS-DEVICE-WDS-MIB", "colubrisDeviceWdsNetworkScanMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceWdsMIBCompliance = colubrisDeviceWdsMIBCompliance.setStatus('current')
colubrisDeviceWdsInfoMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2, 1)).setObjects(("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSInfoMaxNumberOfGroup"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceWdsInfoMIBGroup = colubrisDeviceWdsInfoMIBGroup.setStatus('current')
colubrisDeviceWdsRadioMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2, 2)).setObjects(("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSRadioAckDistance"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSRadioQoS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceWdsRadioMIBGroup = colubrisDeviceWdsRadioMIBGroup.setStatus('current')
colubrisDeviceWdsGroupMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2, 3)).setObjects(("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupName"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupState"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupSecurity"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupDynamicMode"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSGroupDynamicGroupId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceWdsGroupMIBGroup = colubrisDeviceWdsGroupMIBGroup.setStatus('current')
colubrisDeviceWdsLinkMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2, 4)).setObjects(("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaState"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaRadio"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaPeerMacAddress"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaMaster"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaAuthorized"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaEncryption"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaIdleTime"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaSNR"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaTxRate"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaRxRate"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaIfIndex"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaHT"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaTxMCS"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaRxMCS"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaSignal"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStaNoise"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate1"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate2"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate5dot5"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate11"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate6"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate9"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate12"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate18"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate24"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate36"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate48"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxRate54"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate1"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate2"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate5dot5"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate11"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate6"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate9"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate12"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate18"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate24"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate36"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate48"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxRate54"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS0"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS1"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS2"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS3"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS4"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS5"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS6"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS7"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS8"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS9"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS10"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS11"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS12"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS13"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS14"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsTxMCS15"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS0"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS1"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS2"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS3"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS4"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS5"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS6"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS7"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS8"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS9"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS10"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS11"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS12"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS13"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS14"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSLinkStsPktsRxMCS15"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceWdsLinkMIBGroup = colubrisDeviceWdsLinkMIBGroup.setStatus('current')
colubrisDeviceWdsNetworkScanMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 34, 3, 2, 5)).setObjects(("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanGroupId"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanPeerMacAddress"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanChannel"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanSNR"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanMode"), ("COLUBRIS-DEVICE-WDS-MIB", "coDevWDSScanAvailable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisDeviceWdsNetworkScanMIBGroup = colubrisDeviceWdsNetworkScanMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-DEVICE-WDS-MIB", coDevWDSLinkStsPktsTxMCS2=coDevWDSLinkStsPktsTxMCS2, coDevWDSLinkStaTxRate=coDevWDSLinkStaTxRate, coDevWDSLinkStsPktsRxMCS9=coDevWDSLinkStsPktsRxMCS9, coDevWDSLinkStsPktsTxMCS14=coDevWDSLinkStsPktsTxMCS14, coDeviceWDSNetworkScanEntry=coDeviceWDSNetworkScanEntry, coDeviceWDSInfoGroup=coDeviceWDSInfoGroup, coDevWDSLinkStaPeerMacAddress=coDevWDSLinkStaPeerMacAddress, coDevWDSLinkStsPktsRxMCS3=coDevWDSLinkStsPktsRxMCS3, coDevWDSRadioQoS=coDevWDSRadioQoS, coDevWDSLinkStsPktsTxMCS15=coDevWDSLinkStsPktsTxMCS15, coDevWDSLinkStsPktsRxRate5dot5=coDevWDSLinkStsPktsRxRate5dot5, coDevWDSLinkStsPktsRxMCS1=coDevWDSLinkStsPktsRxMCS1, coDevWDSLinkStsPktsTxRate5dot5=coDevWDSLinkStsPktsTxRate5dot5, coDevWDSLinkStsPktsRxMCS13=coDevWDSLinkStsPktsRxMCS13, colubrisDeviceWdsMIBGroups=colubrisDeviceWdsMIBGroups, coDevWDSLinkStsPktsTxMCS1=coDevWDSLinkStsPktsTxMCS1, coDevWDSLinkStsPktsRxMCS2=coDevWDSLinkStsPktsRxMCS2, colubrisDeviceWdsMIBConformance=colubrisDeviceWdsMIBConformance, colubrisDeviceWdsMIBCompliance=colubrisDeviceWdsMIBCompliance, coDevWDSLinkStsPktsTxRate11=coDevWDSLinkStsPktsTxRate11, coDevWDSLinkStsPktsRxMCS14=coDevWDSLinkStsPktsRxMCS14, colubrisDeviceWdsLinkMIBGroup=colubrisDeviceWdsLinkMIBGroup, coDevWDSLinkStsPktsRxRate24=coDevWDSLinkStsPktsRxRate24, PYSNMP_MODULE_ID=colubrisDeviceWdsMIB, coDevWDSScanPeerIndex=coDevWDSScanPeerIndex, coDevWDSLinkStsPktsTxRate48=coDevWDSLinkStsPktsTxRate48, coDevWDSLinkStsPktsTxMCS6=coDevWDSLinkStsPktsTxMCS6, coDeviceWDSRadioEntry=coDeviceWDSRadioEntry, coDevWDSLinkStsPktsRxMCS10=coDevWDSLinkStsPktsRxMCS10, coDeviceWdsInfoEntry=coDeviceWdsInfoEntry, coDeviceWDSLinkStatsRatesEntry=coDeviceWDSLinkStatsRatesEntry, coDeviceWDSLinkStatsHTRatesTable=coDeviceWDSLinkStatsHTRatesTable, colubrisDeviceWdsMIBCompliances=colubrisDeviceWdsMIBCompliances, coDeviceWDSLinkGroup=coDeviceWDSLinkGroup, coDevWDSLinkStaRxMCS=coDevWDSLinkStaRxMCS, coDevWDSLinkStsPktsTxMCS10=coDevWDSLinkStsPktsTxMCS10, coDevWDSLinkStsPktsRxRate18=coDevWDSLinkStsPktsRxRate18, coDevWDSRadioAckDistance=coDevWDSRadioAckDistance, coDeviceWDSLinkStatusEntry=coDeviceWDSLinkStatusEntry, coDevWDSLinkStsPktsRxMCS12=coDevWDSLinkStsPktsRxMCS12, coDevWDSLinkStsPktsRxRate11=coDevWDSLinkStsPktsRxRate11, coDevWDSGroupName=coDevWDSGroupName, coDevWDSScanPeerMacAddress=coDevWDSScanPeerMacAddress, coDevWDSLinkStsPktsTxMCS12=coDevWDSLinkStsPktsTxMCS12, coDevWDSLinkStsPktsTxMCS11=coDevWDSLinkStsPktsTxMCS11, coDeviceWDSGroupGroup=coDeviceWDSGroupGroup, coDevWDSGroupDynamicGroupId=coDevWDSGroupDynamicGroupId, coDevWDSScanSNR=coDevWDSScanSNR, coDevWDSLinkStsPktsTxRate36=coDevWDSLinkStsPktsTxRate36, coDevWDSLinkStsPktsRxRate12=coDevWDSLinkStsPktsRxRate12, coDevWDSLinkStaHT=coDevWDSLinkStaHT, coDevWDSLinkStsPktsRxMCS0=coDevWDSLinkStsPktsRxMCS0, coDevWDSLinkStsPktsRxRate48=coDevWDSLinkStsPktsRxRate48, coDeviceWDSNetworkScanGroup=coDeviceWDSNetworkScanGroup, coDevWDSGroupSecurity=coDevWDSGroupSecurity, colubrisDeviceWdsRadioMIBGroup=colubrisDeviceWdsRadioMIBGroup, coDevWDSLinkStaIndex=coDevWDSLinkStaIndex, coDevWDSLinkStaRxRate=coDevWDSLinkStaRxRate, coDevWDSLinkStsPktsTxRate12=coDevWDSLinkStsPktsTxRate12, colubrisDeviceWdsInfoMIBGroup=colubrisDeviceWdsInfoMIBGroup, coDevWDSLinkStaTxMCS=coDevWDSLinkStaTxMCS, coDevWDSInfoMaxNumberOfGroup=coDevWDSInfoMaxNumberOfGroup, coDevWDSLinkStaIfIndex=coDevWDSLinkStaIfIndex, coDevWDSLinkStsPktsTxMCS4=coDevWDSLinkStsPktsTxMCS4, colubrisDeviceWdsNetworkScanMIBGroup=colubrisDeviceWdsNetworkScanMIBGroup, coDeviceWDSLinkStatusTable=coDeviceWDSLinkStatusTable, coDevWDSLinkStsPktsRxRate2=coDevWDSLinkStsPktsRxRate2, coDevWDSLinkStsPktsTxMCS3=coDevWDSLinkStsPktsTxMCS3, coDevWDSLinkStsPktsRxRate6=coDevWDSLinkStsPktsRxRate6, coDevWDSLinkStsPktsTxMCS9=coDevWDSLinkStsPktsTxMCS9, coDeviceWDSNetworkScanTable=coDeviceWDSNetworkScanTable, coDevWDSLinkStaIdleTime=coDevWDSLinkStaIdleTime, coDeviceWDSGroupTable=coDeviceWDSGroupTable, coDevWDSLinkStaEncryption=coDevWDSLinkStaEncryption, coDevWDSLinkStsPktsRxMCS6=coDevWDSLinkStsPktsRxMCS6, coDevWDSLinkStsPktsTxMCS8=coDevWDSLinkStsPktsTxMCS8, coDevWDSScanMode=coDevWDSScanMode, coDevWDSLinkStsPktsRxMCS8=coDevWDSLinkStsPktsRxMCS8, coDevWDSLinkStsPktsTxRate6=coDevWDSLinkStsPktsTxRate6, coDevWDSLinkStaState=coDevWDSLinkStaState, coDevWDSLinkStaMaster=coDevWDSLinkStaMaster, coDevWDSGroupState=coDevWDSGroupState, coDevWDSLinkStsPktsRxRate9=coDevWDSLinkStsPktsRxRate9, coDevWDSLinkStaNoise=coDevWDSLinkStaNoise, coDevWDSLinkStsPktsTxRate24=coDevWDSLinkStsPktsTxRate24, coDevWDSLinkStaAuthorized=coDevWDSLinkStaAuthorized, colubrisDeviceWdsGroupMIBGroup=colubrisDeviceWdsGroupMIBGroup, coDevWDSLinkStsPktsRxMCS15=coDevWDSLinkStsPktsRxMCS15, coDevWDSLinkStsPktsRxMCS5=coDevWDSLinkStsPktsRxMCS5, colubrisDeviceWdsMIBNotificationPrefix=colubrisDeviceWdsMIBNotificationPrefix, coDeviceWDSLinkStatsHTRatesEntry=coDeviceWDSLinkStatsHTRatesEntry, colubrisDeviceWdsMIBObjects=colubrisDeviceWdsMIBObjects, coDevWDSScanRadioIndex=coDevWDSScanRadioIndex, coDevWDSScanAvailable=coDevWDSScanAvailable, coDevWDSScanGroupId=coDevWDSScanGroupId, coDevWDSLinkStsPktsTxMCS5=coDevWDSLinkStsPktsTxMCS5, coDevWDSLinkStsPktsTxRate54=coDevWDSLinkStsPktsTxRate54, colubrisDeviceWdsMIB=colubrisDeviceWdsMIB, coDevWDSGroupIndex=coDevWDSGroupIndex, coDeviceWDSRadioTable=coDeviceWDSRadioTable, coDeviceWdsInfoTable=coDeviceWdsInfoTable, coDevWDSLinkStsPktsRxRate36=coDevWDSLinkStsPktsRxRate36, coDevWDSLinkStsPktsTxMCS0=coDevWDSLinkStsPktsTxMCS0, coDevWDSLinkStsPktsTxMCS13=coDevWDSLinkStsPktsTxMCS13, coDevWDSLinkStsPktsTxMCS7=coDevWDSLinkStsPktsTxMCS7, coDevWDSLinkStaSignal=coDevWDSLinkStaSignal, coDevWDSRadioIndex=coDevWDSRadioIndex, coDevWDSLinkStsPktsRxRate54=coDevWDSLinkStsPktsRxRate54, coDeviceWDSGroupEntry=coDeviceWDSGroupEntry, coDevWDSLinkStaSNR=coDevWDSLinkStaSNR, colubrisDeviceWdsMIBNotifications=colubrisDeviceWdsMIBNotifications, coDevWDSLinkStsPktsRxRate1=coDevWDSLinkStsPktsRxRate1, coDevWDSLinkStaRadio=coDevWDSLinkStaRadio, coDevWDSLinkStsPktsRxMCS4=coDevWDSLinkStsPktsRxMCS4, coDevWDSLinkStsPktsTxRate2=coDevWDSLinkStsPktsTxRate2, coDeviceWDSLinkStatsRatesTable=coDeviceWDSLinkStatsRatesTable, coDevWDSLinkStsPktsTxRate9=coDevWDSLinkStsPktsTxRate9, coDevWDSGroupDynamicMode=coDevWDSGroupDynamicMode, coDeviceWDSRadioGroup=coDeviceWDSRadioGroup, coDevWDSLinkStsPktsTxRate1=coDevWDSLinkStsPktsTxRate1, coDevWDSLinkStsPktsRxMCS7=coDevWDSLinkStsPktsRxMCS7, coDevWDSLinkStsPktsTxRate18=coDevWDSLinkStsPktsTxRate18, coDevWDSScanChannel=coDevWDSScanChannel, coDevWDSLinkStsPktsRxMCS11=coDevWDSLinkStsPktsRxMCS11)
