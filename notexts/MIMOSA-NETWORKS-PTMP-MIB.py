#
# PySNMP MIB module MIMOSA-NETWORKS-PTMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-NETWORKS-PTMP-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:40:56 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
DecimalTwo, Mimosa5GHzFrequency, Mimosa5GHzChannelNumber, DecimalOne = mibBuilder.importSymbols("MIMOSA-MIB-TC", "DecimalTwo", "Mimosa5GHzFrequency", "Mimosa5GHzChannelNumber", "DecimalOne")
mimosaWireless, mimosaConformanceGroup = mibBuilder.importSymbols("MIMOSA-NETWORKS-BASE-MIB", "mimosaWireless", "mimosaConformanceGroup")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, iso, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, ModuleIdentity, Integer32, Counter64, IpAddress, Counter32, MibIdentifier, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "ModuleIdentity", "Integer32", "Counter64", "IpAddress", "Counter32", "MibIdentifier", "NotificationType", "ObjectIdentity")
TextualConvention, DisplayString, TimeStamp, MacAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TimeStamp", "MacAddress", "TruthValue")
mimosaPtmp = ModuleIdentity((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9))
mimosaPtmp.setRevisions(('2017-04-05 00:00',))
if mibBuilder.loadTexts: mimosaPtmp.setLastUpdated('201704050000Z')
if mibBuilder.loadTexts: mimosaPtmp.setOrganization('Mimosa Networks')
mimosaPtmpSsid = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1))
mimosaPtmpLinkInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 2))
mimosaPtmpChannelPower = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3))
mimosaPtmpApStats = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4))
mimosaPtmpClientInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5))
mimosaPtmpClientStats = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6))
mimosaPtmpMgmtInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7))
mimosaPtmpSsidTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1), )
if mibBuilder.loadTexts: mimosaPtmpSsidTable.setStatus('current')
mimosaPtmpSsidEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidIndex"))
if mibBuilder.loadTexts: mimosaPtmpSsidEntry.setStatus('current')
mimosaPtmpSsidIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 24)))
if mibBuilder.loadTexts: mimosaPtmpSsidIndex.setStatus('current')
mimosaPtmpSsidName = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpSsidName.setStatus('current')
mimosaPtmpSsidType = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("hotspot", 0), ("cpe", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpSsidType.setStatus('current')
mimosaPtmpSsidEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpSsidEnabled.setStatus('current')
mimosaPtmpSsidBroadcastEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpSsidBroadcastEnabled.setStatus('current')
mimosaPtmpSsidIsolationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 1, 1, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpSsidIsolationEnabled.setStatus('current')
mimosaPtmpWirelessMode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("srs", 1), ("wifiinterop", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpWirelessMode.setStatus('current')
mimosaPtmpWirelessGender = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("a", 1), ("b", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpWirelessGender.setStatus('current')
mimosaPtmpWirelessTrafficSplit = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpWirelessTrafficSplit.setStatus('current')
mimosaPtmpWirelessWindowLength = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpWirelessWindowLength.setStatus('current')
mimosaPtmpAutoChannelEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpAutoChannelEnabled.setStatus('current')
mimosaPtmpAntennaGain = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpAntennaGain.setStatus('current')
mimosaPtmpChannelPowerTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3), )
if mibBuilder.loadTexts: mimosaPtmpChannelPowerTable.setStatus('current')
mimosaPtmpChannelPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrRadioIndex"))
if mibBuilder.loadTexts: mimosaPtmpChannelPowerEntry.setStatus('current')
mimosaPtmpChPwrRadioIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: mimosaPtmpChPwrRadioIndex.setStatus('current')
mimosaPtmpChPwrRadioName = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrRadioName.setStatus('current')
mimosaPtmpChPwrCntrFreqCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 3), Mimosa5GHzFrequency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrCntrFreqCfg.setStatus('current')
mimosaPtmpChPwrPrimChannelCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 4), Mimosa5GHzChannelNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrPrimChannelCfg.setStatus('current')
mimosaPtmpChPwrChWidthCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrChWidthCfg.setStatus('current')
mimosaPtmpChPwrTxPowerCfg = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrTxPowerCfg.setStatus('current')
mimosaPtmpChPwrCntrFreqCur = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 7), Mimosa5GHzFrequency()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrCntrFreqCur.setStatus('current')
mimosaPtmpChPwrPrimChannelCur = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 8), Mimosa5GHzChannelNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrPrimChannelCur.setStatus('current')
mimosaPtmpChPwrChWidthCur = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrChWidthCur.setStatus('current')
mimosaPtmpChPwrTxPowerCur = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrTxPowerCur.setStatus('current')
mimosaPtmpChPwrAgcMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("manual", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrAgcMode.setStatus('current')
mimosaPtmpChPwrMinRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 3, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-90, -10))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChPwrMinRxPower.setStatus('current')
mimosaPtmpChannelExclusionTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 4), )
if mibBuilder.loadTexts: mimosaPtmpChannelExclusionTable.setStatus('current')
mimosaPtmpChannelExclusionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 4, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChannelExclusionIndex"))
if mibBuilder.loadTexts: mimosaPtmpChannelExclusionEntry.setStatus('current')
mimosaPtmpChannelExclusionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: mimosaPtmpChannelExclusionIndex.setStatus('current')
mimosaPtmpChannelExclusionStart = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 4, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChannelExclusionStart.setStatus('current')
mimosaPtmpChannelExclusionEnd = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 3, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpChannelExclusionEnd.setStatus('current')
mimosaPtmpApStatsRxBytes = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpApStatsRxBytes.setStatus('current')
mimosaPtmpApStatsTxBytes = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpApStatsTxBytes.setStatus('current')
mimosaPtmpApStatsRxPkts = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpApStatsRxPkts.setStatus('current')
mimosaPtmpApStatsTxPkts = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpApStatsTxPkts.setStatus('current')
mimosaPtmpApStatsTxPer = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpApStatsTxPer.setStatus('current')
mimosaPtmpApStatsLastUpdated = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 4, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpApStatsLastUpdated.setStatus('current')
mimosaPtmpClientInfoTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1), )
if mibBuilder.loadTexts: mimosaPtmpClientInfoTable.setStatus('current')
mimosaPtmpClientInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientInfoIndex"))
if mibBuilder.loadTexts: mimosaPtmpClientInfoEntry.setStatus('current')
mimosaPtmpClientInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: mimosaPtmpClientInfoIndex.setStatus('current')
mimosaPtmpClientInfoMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientInfoMacAddress.setStatus('current')
mimosaPtmpClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientName.setStatus('current')
mimosaPtmpClientFWVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientFWVersion.setStatus('current')
mimosaPtmpClientIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientIPAddress.setStatus('current')
mimosaPtmpClientAssociatedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 6), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientAssociatedTime.setStatus('current')
mimosaPtmpClientPlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientPlanName.setStatus('current')
mimosaPtmpClientUlCommitted = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientUlCommitted.setStatus('current')
mimosaPtmpClientUlPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientUlPeak.setStatus('current')
mimosaPtmpClientDlCommitted = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientDlCommitted.setStatus('current')
mimosaPtmpClientDlPeak = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientDlPeak.setStatus('current')
mimosaPtmpClientInfoLastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 5, 1, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientInfoLastUpdated.setStatus('current')
mimosaPtmpClientStatsTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1), )
if mibBuilder.loadTexts: mimosaPtmpClientStatsTable.setStatus('current')
mimosaPtmpClientStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientStatsIndex"))
if mibBuilder.loadTexts: mimosaPtmpClientStatsEntry.setStatus('current')
mimosaPtmpClientStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: mimosaPtmpClientStatsIndex.setStatus('current')
mimosaPtmpClientStatsMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientStatsMacAddress.setStatus('current')
mimosaPtmpClientAssocBW = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientAssocBW.setStatus('current')
mimosaPtmpClientRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientRxBytes.setStatus('current')
mimosaPtmpClientTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientTxBytes.setStatus('current')
mimosaPtmpClientRxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientRxPkts.setStatus('current')
mimosaPtmpClientTxPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientTxPkts.setStatus('current')
mimosaPtmpClientRxPhyRate = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientRxPhyRate.setStatus('current')
mimosaPtmpClientTxPhyRate = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientTxPhyRate.setStatus('current')
mimosaPtmpClientTxAvgPer = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 10), DecimalTwo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientTxAvgPer.setStatus('current')
mimosaPtmpClientRssiAvg = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 11), DecimalOne()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientRssiAvg.setStatus('current')
mimosaPtmpClientStatsLastUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 6, 1, 1, 12), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpClientStatsLastUpdated.setStatus('current')
mimosaPtmpMgmtIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpMgmtIpAddress.setStatus('current')
mimosaPtmpMgmtIpNetmask = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpMgmtIpNetmask.setStatus('current')
mimosaPtmpMgmtIpGateway = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpMgmtIpGateway.setStatus('current')
mimosaPtmpMgmtIpMode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(4, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpMgmtIpMode.setStatus('current')
mimosaPtmpMgmtPrimaryDNS = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpMgmtPrimaryDNS.setStatus('current')
mimosaPtmpMgmtSecondaryDNS = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpMgmtSecondaryDNS.setStatus('current')
mimosaPtmpMgmtVlanStatus = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpMgmtVlanStatus.setStatus('current')
mimosaPtmpMgmtVlanId = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpMgmtVlanId.setStatus('current')
mimosaPtmpMgmtVlanPassthrough = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disable", 0), ("enable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpMgmtVlanPassthrough.setStatus('current')
mimosaPtmpMgmtEthernetMac = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 9, 7, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPtmpMgmtEthernetMac.setStatus('current')
mimosaPtmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2))
mimosaPtmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 1))
mimosaPtmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2))
mimosaPtmpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 1, 1)).setObjects(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidGroup"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpLinkInfoGroup"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChannelPowerGroup"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsGroup"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientStatsGroup"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientInfoGroup"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaPtmpCompliance = mimosaPtmpCompliance.setStatus('current')
mimosaPtmpSsidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 1)).setObjects(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidName"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidType"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidEnabled"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidBroadcastEnabled"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpSsidIsolationEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaPtmpSsidGroup = mimosaPtmpSsidGroup.setStatus('current')
mimosaPtmpLinkInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 2)).setObjects(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpWirelessMode"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpWirelessGender"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpWirelessTrafficSplit"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpWirelessWindowLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaPtmpLinkInfoGroup = mimosaPtmpLinkInfoGroup.setStatus('current')
mimosaPtmpChannelPowerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 3)).setObjects(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpAutoChannelEnabled"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpAntennaGain"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrRadioName"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrCntrFreqCfg"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrPrimChannelCfg"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrChWidthCfg"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrTxPowerCfg"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrCntrFreqCur"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrPrimChannelCur"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrChWidthCur"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrTxPowerCur"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrAgcMode"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChPwrMinRxPower"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChannelExclusionStart"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpChannelExclusionEnd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaPtmpChannelPowerGroup = mimosaPtmpChannelPowerGroup.setStatus('current')
mimosaPtmpApStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 4)).setObjects(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsRxBytes"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsTxBytes"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsRxPkts"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsTxPkts"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsTxPer"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpApStatsLastUpdated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaPtmpApStatsGroup = mimosaPtmpApStatsGroup.setStatus('current')
mimosaPtmpClientInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 5)).setObjects(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientName"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientFWVersion"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientIPAddress"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientAssociatedTime"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientPlanName"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientUlCommitted"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientUlPeak"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientDlCommitted"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientDlPeak"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientInfoLastUpdated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaPtmpClientInfoGroup = mimosaPtmpClientInfoGroup.setStatus('current')
mimosaPtmpClientStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 6)).setObjects(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientStatsMacAddress"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientAssocBW"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientRxBytes"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientRxPkts"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientTxPkts"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientRssiAvg"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientRxPhyRate"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientTxAvgPer"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientTxPhyRate"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientTxBytes"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpClientStatsLastUpdated"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaPtmpClientStatsGroup = mimosaPtmpClientStatsGroup.setStatus('current')
mimosaPtmpMgmtInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43356, 2, 4, 2, 2, 7)).setObjects(("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtIpAddress"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtIpNetmask"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtIpGateway"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtIpMode"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtPrimaryDNS"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtSecondaryDNS"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtVlanStatus"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtVlanId"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtVlanPassthrough"), ("MIMOSA-NETWORKS-PTMP-MIB", "mimosaPtmpMgmtEthernetMac"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaPtmpMgmtInfoGroup = mimosaPtmpMgmtInfoGroup.setStatus('current')
mibBuilder.exportSymbols("MIMOSA-NETWORKS-PTMP-MIB", mimosaPtmpMgmtInfo=mimosaPtmpMgmtInfo, mimosaPtmpClientDlCommitted=mimosaPtmpClientDlCommitted, mimosaPtmpChPwrMinRxPower=mimosaPtmpChPwrMinRxPower, PYSNMP_MODULE_ID=mimosaPtmp, mimosaPtmpChPwrChWidthCur=mimosaPtmpChPwrChWidthCur, mimosaPtmpChPwrPrimChannelCur=mimosaPtmpChPwrPrimChannelCur, mimosaPtmp=mimosaPtmp, mimosaPtmpClientTxPhyRate=mimosaPtmpClientTxPhyRate, mimosaPtmpChannelPowerEntry=mimosaPtmpChannelPowerEntry, mimosaPtmpSsidEnabled=mimosaPtmpSsidEnabled, mimosaPtmpMgmtIpAddress=mimosaPtmpMgmtIpAddress, mimosaPtmpChPwrPrimChannelCfg=mimosaPtmpChPwrPrimChannelCfg, mimosaPtmpMgmtVlanId=mimosaPtmpMgmtVlanId, mimosaPtmpClientInfoTable=mimosaPtmpClientInfoTable, mimosaPtmpChPwrTxPowerCfg=mimosaPtmpChPwrTxPowerCfg, mimosaPtmpApStatsGroup=mimosaPtmpApStatsGroup, mimosaPtmpChannelExclusionTable=mimosaPtmpChannelExclusionTable, mimosaPtmpClientUlPeak=mimosaPtmpClientUlPeak, mimosaPtmpApStatsTxBytes=mimosaPtmpApStatsTxBytes, mimosaPtmpChannelExclusionEntry=mimosaPtmpChannelExclusionEntry, mimosaPtmpChPwrCntrFreqCur=mimosaPtmpChPwrCntrFreqCur, mimosaPtmpChannelPowerTable=mimosaPtmpChannelPowerTable, mimosaPtmpSsidName=mimosaPtmpSsidName, mimosaPtmpSsidEntry=mimosaPtmpSsidEntry, mimosaPtmpSsid=mimosaPtmpSsid, mimosaPtmpWirelessMode=mimosaPtmpWirelessMode, mimosaPtmpChPwrTxPowerCur=mimosaPtmpChPwrTxPowerCur, mimosaPtmpApStatsLastUpdated=mimosaPtmpApStatsLastUpdated, mimosaPtmpChPwrAgcMode=mimosaPtmpChPwrAgcMode, mimosaPtmpClientRxPkts=mimosaPtmpClientRxPkts, mimosaPtmpClientPlanName=mimosaPtmpClientPlanName, mimosaPtmpMgmtIpGateway=mimosaPtmpMgmtIpGateway, mimosaPtmpCompliance=mimosaPtmpCompliance, mimosaPtmpClientStatsMacAddress=mimosaPtmpClientStatsMacAddress, mimosaPtmpChannelExclusionStart=mimosaPtmpChannelExclusionStart, mimosaPtmpConformance=mimosaPtmpConformance, mimosaPtmpClientStatsGroup=mimosaPtmpClientStatsGroup, mimosaPtmpClientDlPeak=mimosaPtmpClientDlPeak, mimosaPtmpClientTxBytes=mimosaPtmpClientTxBytes, mimosaPtmpMgmtIpMode=mimosaPtmpMgmtIpMode, mimosaPtmpCompliances=mimosaPtmpCompliances, mimosaPtmpClientAssocBW=mimosaPtmpClientAssocBW, mimosaPtmpMgmtInfoGroup=mimosaPtmpMgmtInfoGroup, mimosaPtmpMgmtIpNetmask=mimosaPtmpMgmtIpNetmask, mimosaPtmpChPwrRadioName=mimosaPtmpChPwrRadioName, mimosaPtmpApStatsRxBytes=mimosaPtmpApStatsRxBytes, mimosaPtmpWirelessTrafficSplit=mimosaPtmpWirelessTrafficSplit, mimosaPtmpClientStatsEntry=mimosaPtmpClientStatsEntry, mimosaPtmpWirelessWindowLength=mimosaPtmpWirelessWindowLength, mimosaPtmpChannelExclusionEnd=mimosaPtmpChannelExclusionEnd, mimosaPtmpClientInfoMacAddress=mimosaPtmpClientInfoMacAddress, mimosaPtmpClientRxPhyRate=mimosaPtmpClientRxPhyRate, mimosaPtmpClientInfoEntry=mimosaPtmpClientInfoEntry, mimosaPtmpApStatsTxPkts=mimosaPtmpApStatsTxPkts, mimosaPtmpAntennaGain=mimosaPtmpAntennaGain, mimosaPtmpChannelPowerGroup=mimosaPtmpChannelPowerGroup, mimosaPtmpSsidGroup=mimosaPtmpSsidGroup, mimosaPtmpMgmtVlanPassthrough=mimosaPtmpMgmtVlanPassthrough, mimosaPtmpChPwrCntrFreqCfg=mimosaPtmpChPwrCntrFreqCfg, mimosaPtmpWirelessGender=mimosaPtmpWirelessGender, mimosaPtmpClientInfoIndex=mimosaPtmpClientInfoIndex, mimosaPtmpClientUlCommitted=mimosaPtmpClientUlCommitted, mimosaPtmpClientTxPkts=mimosaPtmpClientTxPkts, mimosaPtmpGroups=mimosaPtmpGroups, mimosaPtmpClientStats=mimosaPtmpClientStats, mimosaPtmpChannelExclusionIndex=mimosaPtmpChannelExclusionIndex, mimosaPtmpApStatsTxPer=mimosaPtmpApStatsTxPer, mimosaPtmpLinkInfo=mimosaPtmpLinkInfo, mimosaPtmpSsidIsolationEnabled=mimosaPtmpSsidIsolationEnabled, mimosaPtmpChannelPower=mimosaPtmpChannelPower, mimosaPtmpClientFWVersion=mimosaPtmpClientFWVersion, mimosaPtmpClientStatsTable=mimosaPtmpClientStatsTable, mimosaPtmpClientInfo=mimosaPtmpClientInfo, mimosaPtmpClientRssiAvg=mimosaPtmpClientRssiAvg, mimosaPtmpApStatsRxPkts=mimosaPtmpApStatsRxPkts, mimosaPtmpSsidType=mimosaPtmpSsidType, mimosaPtmpClientStatsLastUpdated=mimosaPtmpClientStatsLastUpdated, mimosaPtmpMgmtPrimaryDNS=mimosaPtmpMgmtPrimaryDNS, mimosaPtmpAutoChannelEnabled=mimosaPtmpAutoChannelEnabled, mimosaPtmpClientInfoLastUpdated=mimosaPtmpClientInfoLastUpdated, mimosaPtmpMgmtVlanStatus=mimosaPtmpMgmtVlanStatus, mimosaPtmpLinkInfoGroup=mimosaPtmpLinkInfoGroup, mimosaPtmpSsidTable=mimosaPtmpSsidTable, mimosaPtmpMgmtEthernetMac=mimosaPtmpMgmtEthernetMac, mimosaPtmpClientInfoGroup=mimosaPtmpClientInfoGroup, mimosaPtmpClientRxBytes=mimosaPtmpClientRxBytes, mimosaPtmpSsidIndex=mimosaPtmpSsidIndex, mimosaPtmpChPwrRadioIndex=mimosaPtmpChPwrRadioIndex, mimosaPtmpSsidBroadcastEnabled=mimosaPtmpSsidBroadcastEnabled, mimosaPtmpMgmtSecondaryDNS=mimosaPtmpMgmtSecondaryDNS, mimosaPtmpChPwrChWidthCfg=mimosaPtmpChPwrChWidthCfg, mimosaPtmpClientAssociatedTime=mimosaPtmpClientAssociatedTime, mimosaPtmpClientIPAddress=mimosaPtmpClientIPAddress, mimosaPtmpApStats=mimosaPtmpApStats, mimosaPtmpClientTxAvgPer=mimosaPtmpClientTxAvgPer, mimosaPtmpClientStatsIndex=mimosaPtmpClientStatsIndex, mimosaPtmpClientName=mimosaPtmpClientName)
