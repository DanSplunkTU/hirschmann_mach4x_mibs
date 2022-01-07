#
# PySNMP MIB module CELLULAR (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/CELLULAR
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
cellularMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12))
if mibBuilder.loadTexts: cellularMib.setLastUpdated('201805071200Z')
if mibBuilder.loadTexts: cellularMib.setOrganization('PEPLINK')
if mibBuilder.loadTexts: cellularMib.setContactInfo('')
if mibBuilder.loadTexts: cellularMib.setDescription('MIB module for CELLULAR.')
cellularSignalInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1))
cellularSignalInfoTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1), )
if mibBuilder.loadTexts: cellularSignalInfoTable.setStatus('current')
if mibBuilder.loadTexts: cellularSignalInfoTable.setDescription('Cellular signal info table')
cellularSignalInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1), ).setIndexNames((0, "CELLULAR", "cellularSignalInfoId"))
if mibBuilder.loadTexts: cellularSignalInfoEntry.setStatus('current')
if mibBuilder.loadTexts: cellularSignalInfoEntry.setDescription('An entry in the cellularSignalInfoTable')
cellularSignalInfoId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalInfoId.setStatus('current')
if mibBuilder.loadTexts: cellularSignalInfoId.setDescription('Cellular signal info ID.')
cellularSignalInfoWanId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalInfoWanId.setStatus('current')
if mibBuilder.loadTexts: cellularSignalInfoWanId.setDescription('Cellular signal info WAN ID.')
cellularSignalRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 3), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalRssi.setStatus('current')
if mibBuilder.loadTexts: cellularSignalRssi.setDescription('Cellular RSSI (units: dBm).\n                    Remark:\n                    If the value equals -9999, means signal strength\n                    not applicable in this cellular.')
cellularSignalSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 4), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalSnr.setStatus('current')
if mibBuilder.loadTexts: cellularSignalSnr.setDescription('Cellular SNR (units: dB).\n                    Remark:\n                    If the value equals -9999, means signal strength\n                    not applicable in this cellular.')
cellularSignalSinr = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 5), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalSinr.setStatus('current')
if mibBuilder.loadTexts: cellularSignalSinr.setDescription('Cellular SINR (units: dB).\n                    Remark:\n                    If the value equals -9999, means signal strength\n                    not applicable in this cellular.')
cellularSignalEcio = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 6), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalEcio.setStatus('current')
if mibBuilder.loadTexts: cellularSignalEcio.setDescription('Cellular Ec/Io (units: dB).\n                    Remark:\n                    If the value equals -9999, means signal strength\n                    not applicable in this cellular.')
cellularSignalRsrp = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 7), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalRsrp.setStatus('current')
if mibBuilder.loadTexts: cellularSignalRsrp.setDescription('Cellular RSRP (units: dBm).\n                    Remark:\n                    If the value equals -9999, means signal strength\n                    not applicable in this cellular.')
cellularSignalRsrq = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 8), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalRsrq.setStatus('current')
if mibBuilder.loadTexts: cellularSignalRsrq.setDescription('Cellular RSRQ (units: dB).\n                    Remark:\n                    If the value equals -9999, means signal strength\n                    not applicable in this cellular.')
cellularNetworkType = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularNetworkType.setStatus('current')
if mibBuilder.loadTexts: cellularNetworkType.setDescription('Cellular Network Type.')
cellularBand = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularBand.setStatus('current')
if mibBuilder.loadTexts: cellularBand.setDescription('Cellular Band.')
cellularLac = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularLac.setStatus('current')
if mibBuilder.loadTexts: cellularLac.setDescription('Cellular Location Area Code(LAC).\n                    Remark:\n                    If the value equals -1, means LAC not applicable in this cellular.')
cellularTac = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularTac.setStatus('current')
if mibBuilder.loadTexts: cellularTac.setDescription('Cellular Tracking Area Code(TAC).\n                    Remark:\n                    If the value equals -1, means TAC not applicable in this cellular.')
cellularENodeBId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularENodeBId.setStatus('current')
if mibBuilder.loadTexts: cellularENodeBId.setDescription('Cellular eNodeB ID.\n                    Remark:\n                    If the value equals -1, means eNodeB ID not applicable in this cellular.')
cellularIdentityInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2))
cellularIdentityInfoTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1), )
if mibBuilder.loadTexts: cellularIdentityInfoTable.setStatus('current')
if mibBuilder.loadTexts: cellularIdentityInfoTable.setDescription('Cellular identity info table')
cellularIdentityInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1, 1), ).setIndexNames((0, "CELLULAR", "cellularIdentityInfoId"))
if mibBuilder.loadTexts: cellularIdentityInfoEntry.setStatus('current')
if mibBuilder.loadTexts: cellularIdentityInfoEntry.setDescription('An entry in the cellularIdentityInfoTable')
cellularIdentityInfoId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularIdentityInfoId.setStatus('current')
if mibBuilder.loadTexts: cellularIdentityInfoId.setDescription('Cellular identity ID.')
cellularIdentityInfoImei = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularIdentityInfoImei.setStatus('current')
if mibBuilder.loadTexts: cellularIdentityInfoImei.setDescription('Cellular IMEI.')
mibBuilder.exportSymbols("CELLULAR", productMib=productMib, cellularTac=cellularTac, cellularIdentityInfoEntry=cellularIdentityInfoEntry, cellularNetworkType=cellularNetworkType, cellularIdentityInfoTable=cellularIdentityInfoTable, cellularIdentityInfo=cellularIdentityInfo, cellularIdentityInfoId=cellularIdentityInfoId, cellularIdentityInfoImei=cellularIdentityInfoImei, cellularSignalEcio=cellularSignalEcio, cellularLac=cellularLac, peplink=peplink, cellularMib=cellularMib, cellularSignalSnr=cellularSignalSnr, cellularSignalRsrq=cellularSignalRsrq, cellularSignalInfoTable=cellularSignalInfoTable, cellularSignalSinr=cellularSignalSinr, cellularBand=cellularBand, cellularSignalInfo=cellularSignalInfo, PYSNMP_MODULE_ID=cellularMib, generalMib=generalMib, cellularSignalRssi=cellularSignalRssi, cellularSignalInfoWanId=cellularSignalInfoWanId, cellularSignalInfoId=cellularSignalInfoId, cellularENodeBId=cellularENodeBId, cellularSignalRsrp=cellularSignalRsrp, cellularSignalInfoEntry=cellularSignalInfoEntry)
