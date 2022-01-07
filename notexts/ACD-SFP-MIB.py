#
# PySNMP MIB module ACD-SFP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-SFP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:08:21 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, Gauge32, Bits, Unsigned32, TimeTicks, Counter32, Counter64, Integer32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Gauge32", "Bits", "Unsigned32", "TimeTicks", "Counter32", "Counter64", "Integer32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "NotificationType")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
acdSfp = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 4))
acdSfp.setRevisions(('2010-11-10 01:00', '2008-04-22 01:00', '2006-08-06 01:00',))
if mibBuilder.loadTexts: acdSfp.setLastUpdated('201011100100Z')
if mibBuilder.loadTexts: acdSfp.setOrganization('Accedian Networks, Inc.')
acdSfpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 4, 5))
acdSfpMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 4, 6))
acdSfpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 4, 7))
acdSfpInfoTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1), )
if mibBuilder.loadTexts: acdSfpInfoTable.setStatus('current')
acdSfpInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1), ).setIndexNames((0, "ACD-SFP-MIB", "acdSfpInfoID"))
if mibBuilder.loadTexts: acdSfpInfoEntry.setStatus('current')
acdSfpInfoID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSfpInfoID.setStatus('current')
acdSfpInfoConnIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoConnIdx.setStatus('current')
acdSfpInfoConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 32, 33))).clone(namedValues=NamedValues(("sfpSC", 1), ("sfpFC1COPPER", 2), ("sfpFC2COPPER", 3), ("sfpBNC", 4), ("sfpFCCOAX", 5), ("sfpFIBERJACK", 6), ("sfpLC", 7), ("sfpMTRJ", 8), ("sfpMU", 9), ("sfpSG", 10), ("sfpPIGTAIL", 11), ("sfpHSSDCII", 32), ("sfpCOPPERPIGTAIL", 33)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoConnType.setStatus('current')
acdSfpInfoVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoVendor.setStatus('current')
acdSfpInfoVendorOui = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(3, 3)).setFixedLength(3)).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoVendorOui.setStatus('current')
acdSfpInfoVendorPn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoVendorPn.setStatus('current')
acdSfpInfoVendorRev = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoVendorRev.setStatus('current')
acdSfpInfoWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoWavelength.setStatus('current')
acdSfpInfoSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoSerialNum.setStatus('current')
acdSfpInfoYear = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoYear.setStatus('current')
acdSfpInfoMonth = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoMonth.setStatus('current')
acdSfpInfoDay = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoDay.setStatus('current')
acdSfpInfoLot = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoLot.setStatus('current')
acdSfpInfoRev8472 = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("undefined", 0), ("rev93", 1), ("rev94", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoRev8472.setStatus('current')
acdSfpInfoPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoPresent.setStatus('current')
acdSfpInfoDiag = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoDiag.setStatus('current')
acdSfpInfoInternal = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoInternal.setStatus('current')
acdSfpInfoAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoAlm.setStatus('current')
acdSfpInfoIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoIdType.setStatus('current')
acdSfpInfoExtIdType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoExtIdType.setStatus('current')
acdSfpInfoTransCode = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 1, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 8)).setFixedLength(8)).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpInfoTransCode.setStatus('current')
acdSfpDiagTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2), )
if mibBuilder.loadTexts: acdSfpDiagTable.setStatus('current')
acdSfpDiagEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1), ).setIndexNames((0, "ACD-SFP-MIB", "acdSfpDiagID"))
if mibBuilder.loadTexts: acdSfpDiagEntry.setStatus('current')
acdSfpDiagID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSfpDiagID.setStatus('current')
acdSfpDiagConnIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpDiagConnIdx.setStatus('current')
acdSfpDiagTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpDiagTemp.setStatus('current')
acdSfpDiagVcc = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpDiagVcc.setStatus('current')
acdSfpDiagLbc = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpDiagLbc.setStatus('current')
acdSfpDiagTxPwr = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpDiagTxPwr.setStatus('current')
acdSfpDiagRxPwr = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpDiagRxPwr.setStatus('current')
acdSfpDiagTxPwrdBm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpDiagTxPwrdBm.setStatus('current')
acdSfpDiagRxPwrdBm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpDiagRxPwrdBm.setStatus('current')
acdSfpThreshTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3), )
if mibBuilder.loadTexts: acdSfpThreshTable.setStatus('current')
acdSfpThreshEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1), ).setIndexNames((0, "ACD-SFP-MIB", "acdSfpThreshID"))
if mibBuilder.loadTexts: acdSfpThreshEntry.setStatus('current')
acdSfpThreshID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSfpThreshID.setStatus('current')
acdSfpThreshConnIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshConnIdx.setStatus('current')
acdSfpThreshTempHighAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTempHighAlm.setStatus('current')
acdSfpThreshTempLowAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTempLowAlm.setStatus('current')
acdSfpThreshTempHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTempHighWarn.setStatus('current')
acdSfpThreshTempLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTempLowWarn.setStatus('current')
acdSfpThreshVccHighAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshVccHighAlm.setStatus('current')
acdSfpThreshVccLowAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshVccLowAlm.setStatus('current')
acdSfpThreshVccHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshVccHighWarn.setStatus('current')
acdSfpThreshVccLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshVccLowWarn.setStatus('current')
acdSfpThreshLbcHighAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshLbcHighAlm.setStatus('current')
acdSfpThreshLbcLowAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshLbcLowAlm.setStatus('current')
acdSfpThreshLbcHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshLbcHighWarn.setStatus('current')
acdSfpThreshLbcLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshLbcLowWarn.setStatus('current')
acdSfpThreshTxPwrHighAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTxPwrHighAlm.setStatus('current')
acdSfpThreshTxPwrLowAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTxPwrLowAlm.setStatus('current')
acdSfpThreshTxPwrHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTxPwrHighWarn.setStatus('current')
acdSfpThreshTxPwrLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTxPwrLowWarn.setStatus('current')
acdSfpThreshRxPwrHighAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshRxPwrHighAlm.setStatus('current')
acdSfpThreshRxPwrLowAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshRxPwrLowAlm.setStatus('current')
acdSfpThreshRxPwrHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshRxPwrHighWarn.setStatus('current')
acdSfpThreshRxPwrLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshRxPwrLowWarn.setStatus('current')
acdSfpThreshTxPwrHighAlmdBm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTxPwrHighAlmdBm.setStatus('current')
acdSfpThreshTxPwrLowAlmdBm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 24), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTxPwrLowAlmdBm.setStatus('current')
acdSfpThreshTxPwrHighWarndBm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTxPwrHighWarndBm.setStatus('current')
acdSfpThreshTxPwrLowWarndBm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 26), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshTxPwrLowWarndBm.setStatus('current')
acdSfpThreshRxPwrHighAlmdBm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 27), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshRxPwrHighAlmdBm.setStatus('current')
acdSfpThreshRxPwrLowAlmdBm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 28), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshRxPwrLowAlmdBm.setStatus('current')
acdSfpThreshRxPwrHighWarndBm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 29), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshRxPwrHighWarndBm.setStatus('current')
acdSfpThreshRxPwrLowWarndBm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 3, 1, 30), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshRxPwrLowWarndBm.setStatus('current')
acdSfpThreshStatusTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4), )
if mibBuilder.loadTexts: acdSfpThreshStatusTable.setStatus('current')
acdSfpThreshStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1), ).setIndexNames((0, "ACD-SFP-MIB", "acdSfpThreshStatusID"))
if mibBuilder.loadTexts: acdSfpThreshStatusEntry.setStatus('current')
acdSfpThreshStatusID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSfpThreshStatusID.setStatus('current')
acdSfpThreshStatusConnIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusConnIdx.setStatus('current')
acdSfpThreshStatusTempHighAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusTempHighAlm.setStatus('current')
acdSfpThreshStatusTempLowAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusTempLowAlm.setStatus('current')
acdSfpThreshStatusTempHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusTempHighWarn.setStatus('current')
acdSfpThreshStatusTempLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusTempLowWarn.setStatus('current')
acdSfpThreshStatusVccHighAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusVccHighAlm.setStatus('current')
acdSfpThreshStatusVccLowAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusVccLowAlm.setStatus('current')
acdSfpThreshStatusVccHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 9), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusVccHighWarn.setStatus('current')
acdSfpThreshStatusVccLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusVccLowWarn.setStatus('current')
acdSfpThreshStatusLbcHighAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusLbcHighAlm.setStatus('current')
acdSfpThreshStatusLbcLowAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusLbcLowAlm.setStatus('current')
acdSfpThreshStatusLbcHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusLbcHighWarn.setStatus('current')
acdSfpThreshStatusLbcLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusLbcLowWarn.setStatus('current')
acdSfpThreshStatusTxPwrHighAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusTxPwrHighAlm.setStatus('current')
acdSfpThreshStatusTxPwrLowAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusTxPwrLowAlm.setStatus('current')
acdSfpThreshStatusTxPwrHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 17), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusTxPwrHighWarn.setStatus('current')
acdSfpThreshStatusTxPwrLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusTxPwrLowWarn.setStatus('current')
acdSfpThreshStatusRxPwrHighAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusRxPwrHighAlm.setStatus('current')
acdSfpThreshStatusRxPwrLowAlm = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusRxPwrLowAlm.setStatus('current')
acdSfpThreshStatusRxPwrHighWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 21), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusRxPwrHighWarn.setStatus('current')
acdSfpThreshStatusRxPwrLowWarn = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 4, 4, 1, 22), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdSfpThreshStatusRxPwrLowWarn.setStatus('current')
acdSfpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 1))
acdSfpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 2))
acdSfpInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 2, 1)).setObjects(("ACD-SFP-MIB", "acdSfpInfoConnIdx"), ("ACD-SFP-MIB", "acdSfpInfoConnType"), ("ACD-SFP-MIB", "acdSfpInfoVendor"), ("ACD-SFP-MIB", "acdSfpInfoVendorOui"), ("ACD-SFP-MIB", "acdSfpInfoVendorPn"), ("ACD-SFP-MIB", "acdSfpInfoVendorRev"), ("ACD-SFP-MIB", "acdSfpInfoWavelength"), ("ACD-SFP-MIB", "acdSfpInfoSerialNum"), ("ACD-SFP-MIB", "acdSfpInfoYear"), ("ACD-SFP-MIB", "acdSfpInfoMonth"), ("ACD-SFP-MIB", "acdSfpInfoDay"), ("ACD-SFP-MIB", "acdSfpInfoLot"), ("ACD-SFP-MIB", "acdSfpInfoRev8472"), ("ACD-SFP-MIB", "acdSfpInfoPresent"), ("ACD-SFP-MIB", "acdSfpInfoDiag"), ("ACD-SFP-MIB", "acdSfpInfoInternal"), ("ACD-SFP-MIB", "acdSfpInfoAlm"), ("ACD-SFP-MIB", "acdSfpInfoIdType"), ("ACD-SFP-MIB", "acdSfpInfoExtIdType"), ("ACD-SFP-MIB", "acdSfpInfoTransCode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSfpInfoGroup = acdSfpInfoGroup.setStatus('current')
acdSfpDiagGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 2, 2)).setObjects(("ACD-SFP-MIB", "acdSfpDiagConnIdx"), ("ACD-SFP-MIB", "acdSfpDiagTemp"), ("ACD-SFP-MIB", "acdSfpDiagVcc"), ("ACD-SFP-MIB", "acdSfpDiagLbc"), ("ACD-SFP-MIB", "acdSfpDiagTxPwr"), ("ACD-SFP-MIB", "acdSfpDiagRxPwr"), ("ACD-SFP-MIB", "acdSfpDiagTxPwrdBm"), ("ACD-SFP-MIB", "acdSfpDiagRxPwrdBm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSfpDiagGroup = acdSfpDiagGroup.setStatus('current')
acdSfpThreshGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 2, 3)).setObjects(("ACD-SFP-MIB", "acdSfpThreshConnIdx"), ("ACD-SFP-MIB", "acdSfpThreshTempHighAlm"), ("ACD-SFP-MIB", "acdSfpThreshTempLowAlm"), ("ACD-SFP-MIB", "acdSfpThreshTempHighWarn"), ("ACD-SFP-MIB", "acdSfpThreshTempLowWarn"), ("ACD-SFP-MIB", "acdSfpThreshVccHighAlm"), ("ACD-SFP-MIB", "acdSfpThreshVccLowAlm"), ("ACD-SFP-MIB", "acdSfpThreshVccHighWarn"), ("ACD-SFP-MIB", "acdSfpThreshVccLowWarn"), ("ACD-SFP-MIB", "acdSfpThreshLbcHighAlm"), ("ACD-SFP-MIB", "acdSfpThreshLbcLowAlm"), ("ACD-SFP-MIB", "acdSfpThreshLbcHighWarn"), ("ACD-SFP-MIB", "acdSfpThreshLbcLowWarn"), ("ACD-SFP-MIB", "acdSfpThreshTxPwrHighAlm"), ("ACD-SFP-MIB", "acdSfpThreshTxPwrLowAlm"), ("ACD-SFP-MIB", "acdSfpThreshTxPwrHighWarn"), ("ACD-SFP-MIB", "acdSfpThreshTxPwrLowWarn"), ("ACD-SFP-MIB", "acdSfpThreshRxPwrHighAlm"), ("ACD-SFP-MIB", "acdSfpThreshRxPwrLowAlm"), ("ACD-SFP-MIB", "acdSfpThreshRxPwrHighWarn"), ("ACD-SFP-MIB", "acdSfpThreshRxPwrLowWarn"), ("ACD-SFP-MIB", "acdSfpThreshTxPwrHighAlmdBm"), ("ACD-SFP-MIB", "acdSfpThreshTxPwrLowAlmdBm"), ("ACD-SFP-MIB", "acdSfpThreshTxPwrHighWarndBm"), ("ACD-SFP-MIB", "acdSfpThreshTxPwrLowWarndBm"), ("ACD-SFP-MIB", "acdSfpThreshRxPwrHighAlmdBm"), ("ACD-SFP-MIB", "acdSfpThreshRxPwrLowAlmdBm"), ("ACD-SFP-MIB", "acdSfpThreshRxPwrHighWarndBm"), ("ACD-SFP-MIB", "acdSfpThreshRxPwrLowWarndBm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSfpThreshGroup = acdSfpThreshGroup.setStatus('current')
acdSfpThreshStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 2, 4)).setObjects(("ACD-SFP-MIB", "acdSfpThreshStatusConnIdx"), ("ACD-SFP-MIB", "acdSfpThreshStatusTempHighAlm"), ("ACD-SFP-MIB", "acdSfpThreshStatusTempLowAlm"), ("ACD-SFP-MIB", "acdSfpThreshStatusTempHighWarn"), ("ACD-SFP-MIB", "acdSfpThreshStatusTempLowWarn"), ("ACD-SFP-MIB", "acdSfpThreshStatusVccHighAlm"), ("ACD-SFP-MIB", "acdSfpThreshStatusVccLowAlm"), ("ACD-SFP-MIB", "acdSfpThreshStatusVccHighWarn"), ("ACD-SFP-MIB", "acdSfpThreshStatusVccLowWarn"), ("ACD-SFP-MIB", "acdSfpThreshStatusLbcHighAlm"), ("ACD-SFP-MIB", "acdSfpThreshStatusLbcLowAlm"), ("ACD-SFP-MIB", "acdSfpThreshStatusLbcHighWarn"), ("ACD-SFP-MIB", "acdSfpThreshStatusLbcLowWarn"), ("ACD-SFP-MIB", "acdSfpThreshStatusTxPwrHighAlm"), ("ACD-SFP-MIB", "acdSfpThreshStatusTxPwrLowAlm"), ("ACD-SFP-MIB", "acdSfpThreshStatusTxPwrHighWarn"), ("ACD-SFP-MIB", "acdSfpThreshStatusTxPwrLowWarn"), ("ACD-SFP-MIB", "acdSfpThreshStatusRxPwrHighAlm"), ("ACD-SFP-MIB", "acdSfpThreshStatusRxPwrLowAlm"), ("ACD-SFP-MIB", "acdSfpThreshStatusRxPwrHighWarn"), ("ACD-SFP-MIB", "acdSfpThreshStatusRxPwrLowWarn"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSfpThreshStatusGroup = acdSfpThreshStatusGroup.setStatus('current')
acdSfpCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 4, 7, 1, 1)).setObjects(("ACD-SFP-MIB", "acdSfpInfoGroup"), ("ACD-SFP-MIB", "acdSfpDiagGroup"), ("ACD-SFP-MIB", "acdSfpThreshGroup"), ("ACD-SFP-MIB", "acdSfpThreshStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSfpCompliance = acdSfpCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-SFP-MIB", acdSfpThreshTxPwrLowAlm=acdSfpThreshTxPwrLowAlm, acdSfpDiagEntry=acdSfpDiagEntry, acdSfpThreshTxPwrHighAlmdBm=acdSfpThreshTxPwrHighAlmdBm, acdSfpThreshStatusTempLowWarn=acdSfpThreshStatusTempLowWarn, acdSfpGroups=acdSfpGroups, acdSfpInfoYear=acdSfpInfoYear, acdSfpInfoConnType=acdSfpInfoConnType, acdSfpThreshVccHighAlm=acdSfpThreshVccHighAlm, acdSfpInfoVendorOui=acdSfpInfoVendorOui, acdSfpInfoGroup=acdSfpInfoGroup, acdSfpThreshStatusTempHighAlm=acdSfpThreshStatusTempHighAlm, acdSfpThreshStatusTxPwrHighAlm=acdSfpThreshStatusTxPwrHighAlm, acdSfpDiagTemp=acdSfpDiagTemp, acdSfpInfoExtIdType=acdSfpInfoExtIdType, acdSfpThreshTempLowAlm=acdSfpThreshTempLowAlm, acdSfpThreshTxPwrHighWarndBm=acdSfpThreshTxPwrHighWarndBm, acdSfpThreshStatusRxPwrHighAlm=acdSfpThreshStatusRxPwrHighAlm, acdSfpThreshRxPwrLowWarn=acdSfpThreshRxPwrLowWarn, acdSfpInfoMonth=acdSfpInfoMonth, acdSfpThreshStatusTempHighWarn=acdSfpThreshStatusTempHighWarn, acdSfpThreshStatusVccHighAlm=acdSfpThreshStatusVccHighAlm, acdSfpThreshStatusEntry=acdSfpThreshStatusEntry, acdSfpDiagTxPwr=acdSfpDiagTxPwr, acdSfpThreshRxPwrHighAlm=acdSfpThreshRxPwrHighAlm, acdSfpThreshStatusConnIdx=acdSfpThreshStatusConnIdx, acdSfpDiagGroup=acdSfpDiagGroup, acdSfpInfoConnIdx=acdSfpInfoConnIdx, acdSfpDiagLbc=acdSfpDiagLbc, PYSNMP_MODULE_ID=acdSfp, acdSfpThreshStatusVccLowWarn=acdSfpThreshStatusVccLowWarn, acdSfpInfoPresent=acdSfpInfoPresent, acdSfpInfoID=acdSfpInfoID, acdSfpInfoVendorPn=acdSfpInfoVendorPn, acdSfpDiagConnIdx=acdSfpDiagConnIdx, acdSfpDiagRxPwr=acdSfpDiagRxPwr, acdSfpNotifications=acdSfpNotifications, acdSfpInfoDiag=acdSfpInfoDiag, acdSfpThreshTempLowWarn=acdSfpThreshTempLowWarn, acdSfpThreshRxPwrHighWarndBm=acdSfpThreshRxPwrHighWarndBm, acdSfpThreshStatusTempLowAlm=acdSfpThreshStatusTempLowAlm, acdSfpInfoIdType=acdSfpInfoIdType, acdSfpThreshStatusLbcHighAlm=acdSfpThreshStatusLbcHighAlm, acdSfpDiagID=acdSfpDiagID, acdSfpThreshEntry=acdSfpThreshEntry, acdSfpThreshRxPwrLowAlmdBm=acdSfpThreshRxPwrLowAlmdBm, acdSfpThreshTxPwrHighWarn=acdSfpThreshTxPwrHighWarn, acdSfpDiagTable=acdSfpDiagTable, acdSfpThreshRxPwrHighAlmdBm=acdSfpThreshRxPwrHighAlmdBm, acdSfpThreshRxPwrLowWarndBm=acdSfpThreshRxPwrLowWarndBm, acdSfpThreshStatusLbcHighWarn=acdSfpThreshStatusLbcHighWarn, acdSfp=acdSfp, acdSfpThreshLbcHighAlm=acdSfpThreshLbcHighAlm, acdSfpThreshLbcHighWarn=acdSfpThreshLbcHighWarn, acdSfpThreshVccLowAlm=acdSfpThreshVccLowAlm, acdSfpInfoLot=acdSfpInfoLot, acdSfpCompliances=acdSfpCompliances, acdSfpInfoTransCode=acdSfpInfoTransCode, acdSfpThreshStatusRxPwrLowAlm=acdSfpThreshStatusRxPwrLowAlm, acdSfpDiagRxPwrdBm=acdSfpDiagRxPwrdBm, acdSfpThreshStatusVccLowAlm=acdSfpThreshStatusVccLowAlm, acdSfpDiagTxPwrdBm=acdSfpDiagTxPwrdBm, acdSfpThreshRxPwrLowAlm=acdSfpThreshRxPwrLowAlm, acdSfpThreshStatusVccHighWarn=acdSfpThreshStatusVccHighWarn, acdSfpInfoRev8472=acdSfpInfoRev8472, acdSfpThreshRxPwrHighWarn=acdSfpThreshRxPwrHighWarn, acdSfpInfoWavelength=acdSfpInfoWavelength, acdSfpThreshTxPwrHighAlm=acdSfpThreshTxPwrHighAlm, acdSfpThreshGroup=acdSfpThreshGroup, acdSfpThreshVccHighWarn=acdSfpThreshVccHighWarn, acdSfpThreshLbcLowAlm=acdSfpThreshLbcLowAlm, acdSfpThreshStatusTxPwrHighWarn=acdSfpThreshStatusTxPwrHighWarn, acdSfpInfoTable=acdSfpInfoTable, acdSfpCompliance=acdSfpCompliance, acdSfpThreshStatusTxPwrLowWarn=acdSfpThreshStatusTxPwrLowWarn, acdSfpMIBObjects=acdSfpMIBObjects, acdSfpThreshTempHighWarn=acdSfpThreshTempHighWarn, acdSfpThreshTable=acdSfpThreshTable, acdSfpInfoVendorRev=acdSfpInfoVendorRev, acdSfpThreshTxPwrLowWarndBm=acdSfpThreshTxPwrLowWarndBm, acdSfpThreshTempHighAlm=acdSfpThreshTempHighAlm, acdSfpInfoInternal=acdSfpInfoInternal, acdSfpInfoDay=acdSfpInfoDay, acdSfpDiagVcc=acdSfpDiagVcc, acdSfpInfoVendor=acdSfpInfoVendor, acdSfpThreshTxPwrLowWarn=acdSfpThreshTxPwrLowWarn, acdSfpThreshStatusLbcLowAlm=acdSfpThreshStatusLbcLowAlm, acdSfpThreshStatusRxPwrLowWarn=acdSfpThreshStatusRxPwrLowWarn, acdSfpConformance=acdSfpConformance, acdSfpThreshStatusLbcLowWarn=acdSfpThreshStatusLbcLowWarn, acdSfpInfoEntry=acdSfpInfoEntry, acdSfpThreshVccLowWarn=acdSfpThreshVccLowWarn, acdSfpThreshStatusTxPwrLowAlm=acdSfpThreshStatusTxPwrLowAlm, acdSfpThreshID=acdSfpThreshID, acdSfpThreshStatusTable=acdSfpThreshStatusTable, acdSfpThreshStatusGroup=acdSfpThreshStatusGroup, acdSfpThreshStatusID=acdSfpThreshStatusID, acdSfpThreshStatusRxPwrHighWarn=acdSfpThreshStatusRxPwrHighWarn, acdSfpInfoAlm=acdSfpInfoAlm, acdSfpThreshConnIdx=acdSfpThreshConnIdx, acdSfpThreshTxPwrLowAlmdBm=acdSfpThreshTxPwrLowAlmdBm, acdSfpInfoSerialNum=acdSfpInfoSerialNum, acdSfpThreshLbcLowWarn=acdSfpThreshLbcLowWarn)
