#
# PySNMP MIB module CELLULAR (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/peplink/CELLULAR
# Produced by pysmi-1.1.8 at Mon Feb  7 16:18:10 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, enterprises, NotificationType, Gauge32, ObjectIdentity, iso, Unsigned32, Counter32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "enterprises", "NotificationType", "Gauge32", "ObjectIdentity", "iso", "Unsigned32", "Counter32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Integer32", "Bits")
TextualConvention, RowStatus, TruthValue, DisplayString, MacAddress = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString", "MacAddress")
peplink = MibIdentifier((1, 3, 6, 1, 4, 1, 23695))
productMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200))
generalMib = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1))
cellularMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12))
if mibBuilder.loadTexts: cellularMib.setLastUpdated('201805071200Z')
if mibBuilder.loadTexts: cellularMib.setOrganization('PEPLINK')
cellularSignalInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1))
cellularSignalInfoTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1), )
if mibBuilder.loadTexts: cellularSignalInfoTable.setStatus('current')
cellularSignalInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1), ).setIndexNames((0, "CELLULAR", "cellularSignalInfoId"))
if mibBuilder.loadTexts: cellularSignalInfoEntry.setStatus('current')
cellularSignalInfoId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalInfoId.setStatus('current')
cellularSignalInfoWanId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalInfoWanId.setStatus('current')
cellularSignalRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 3), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalRssi.setStatus('current')
cellularSignalSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 4), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalSnr.setStatus('current')
cellularSignalSinr = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 5), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalSinr.setStatus('current')
cellularSignalEcio = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 6), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalEcio.setStatus('current')
cellularSignalRsrp = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 7), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalRsrp.setStatus('current')
cellularSignalRsrq = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 8), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularSignalRsrq.setStatus('current')
cellularNetworkType = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularNetworkType.setStatus('current')
cellularBand = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularBand.setStatus('current')
cellularLac = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularLac.setStatus('current')
cellularTac = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularTac.setStatus('current')
cellularENodeBId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularENodeBId.setStatus('current')
cellularIdentityInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2))
cellularIdentityInfoTable = MibTable((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1), )
if mibBuilder.loadTexts: cellularIdentityInfoTable.setStatus('current')
cellularIdentityInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1, 1), ).setIndexNames((0, "CELLULAR", "cellularIdentityInfoId"))
if mibBuilder.loadTexts: cellularIdentityInfoEntry.setStatus('current')
cellularIdentityInfoId = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularIdentityInfoId.setStatus('current')
cellularIdentityInfoImei = MibTableColumn((1, 3, 6, 1, 4, 1, 23695, 200, 1, 12, 2, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cellularIdentityInfoImei.setStatus('current')
mibBuilder.exportSymbols("CELLULAR", cellularENodeBId=cellularENodeBId, cellularIdentityInfoImei=cellularIdentityInfoImei, cellularSignalRssi=cellularSignalRssi, cellularMib=cellularMib, cellularSignalInfoWanId=cellularSignalInfoWanId, cellularIdentityInfo=cellularIdentityInfo, cellularIdentityInfoId=cellularIdentityInfoId, cellularSignalEcio=cellularSignalEcio, PYSNMP_MODULE_ID=cellularMib, cellularSignalRsrp=cellularSignalRsrp, cellularSignalInfoId=cellularSignalInfoId, cellularBand=cellularBand, cellularSignalSinr=cellularSignalSinr, productMib=productMib, peplink=peplink, cellularSignalInfoEntry=cellularSignalInfoEntry, cellularSignalInfo=cellularSignalInfo, cellularSignalRsrq=cellularSignalRsrq, cellularTac=cellularTac, cellularIdentityInfoEntry=cellularIdentityInfoEntry, cellularSignalSnr=cellularSignalSnr, generalMib=generalMib, cellularIdentityInfoTable=cellularIdentityInfoTable, cellularSignalInfoTable=cellularSignalInfoTable, cellularLac=cellularLac, cellularNetworkType=cellularNetworkType)
