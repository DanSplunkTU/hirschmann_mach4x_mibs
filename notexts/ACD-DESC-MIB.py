#
# PySNMP MIB module ACD-DESC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-DESC-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:50:16 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
acdProducts, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdProducts")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Integer32, iso, Gauge32, TimeTicks, ObjectIdentity, IpAddress, MibIdentifier, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Integer32", "iso", "Gauge32", "TimeTicks", "ObjectIdentity", "IpAddress", "MibIdentifier", "NotificationType", "Counter32")
MacAddress, TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "TruthValue")
acdDesc = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 1, 1))
acdDesc.setRevisions(('2010-11-10 01:00', '2010-06-30 01:00', '2009-02-04 01:00', '2008-12-01 01:00', '2006-08-06 01:00',))
if mibBuilder.loadTexts: acdDesc.setLastUpdated('201011100100Z')
if mibBuilder.loadTexts: acdDesc.setOrganization('Accedian Networks, Inc.')
acdDescNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 1, 1, 0))
acdDescMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15))
acdDescConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1))
acdDescCommercialName = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCommercialName.setStatus('current')
acdDescMacBaseAddr = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 2), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescMacBaseAddr.setStatus('current')
acdDescIdentifier = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescIdentifier.setStatus('current')
acdDescFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescFirmwareVersion.setStatus('current')
acdDescHardwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescHardwareVersion.setStatus('current')
acdDescSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescSerialNumber.setStatus('current')
acdDescCpuUsageCurrent = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 20), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCpuUsageCurrent.setStatus('current')
acdDescCpuUsageAverage15 = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 21), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCpuUsageAverage15.setStatus('current')
acdDescCpuUsageAverage30 = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 22), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCpuUsageAverage30.setStatus('current')
acdDescCpuUsageAverage60 = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 23), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCpuUsageAverage60.setStatus('current')
acdDescCpuUsageAverage900 = MibScalar((1, 3, 6, 1, 4, 1, 22420, 1, 1, 24), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescCpuUsageAverage900.setStatus('current')
acdDescConnectorTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10), )
if mibBuilder.loadTexts: acdDescConnectorTable.setStatus('current')
acdDescConnectorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1), ).setIndexNames((0, "ACD-DESC-MIB", "acdDescConnectorID"))
if mibBuilder.loadTexts: acdDescConnectorEntry.setStatus('current')
acdDescConnectorID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: acdDescConnectorID.setStatus('current')
acdDescConnectorName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescConnectorName.setStatus('current')
acdDescConnectorType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("other", 1), ("rj45", 2), ("rj45S", 3), ("db9", 4), ("bnc", 5), ("fAUI", 6), ("mAUI", 7), ("fiberSC", 8), ("fiberMIC", 9), ("fiberST", 10), ("telco", 11), ("mtrj", 12), ("hssdc", 13), ("fiberLC", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescConnectorType.setStatus('current')
acdDescConnectorPoESupport = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 10, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescConnectorPoESupport.setStatus('current')
acdDescPwrTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11), )
if mibBuilder.loadTexts: acdDescPwrTable.setStatus('current')
acdDescPwrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1), ).setIndexNames((0, "ACD-DESC-MIB", "acdDescPwrID"))
if mibBuilder.loadTexts: acdDescPwrEntry.setStatus('current')
acdDescPwrID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: acdDescPwrID.setStatus('current')
acdDescPwrName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescPwrName.setStatus('current')
acdDescPwrType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("pwrplus5volts", 1), ("pwrminus48volts", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescPwrType.setStatus('current')
acdDescPwrPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 11, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescPwrPresent.setStatus('current')
acdDescTsTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12), )
if mibBuilder.loadTexts: acdDescTsTable.setStatus('current')
acdDescTsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1), ).setIndexNames((0, "ACD-DESC-MIB", "acdDescTsID"))
if mibBuilder.loadTexts: acdDescTsEntry.setStatus('current')
acdDescTsID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: acdDescTsID.setStatus('current')
acdDescTsCurrentTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescTsCurrentTemp.setStatus('current')
acdDescTsFirstThres = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescTsFirstThres.setStatus('current')
acdDescTsFisrtThresPass = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescTsFisrtThresPass.setStatus('current')
acdDescTsSecondThres = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescTsSecondThres.setStatus('current')
acdDescTsSecondThresPass = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 1, 1, 12, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdDescTsSecondThresPass.setStatus('current')
acdPowerLost = NotificationType((1, 3, 6, 1, 4, 1, 22420, 1, 1, 0, 1)).setObjects(("ACD-DESC-MIB", "acdDescCommercialName"), ("ACD-DESC-MIB", "acdDescMacBaseAddr"), ("ACD-DESC-MIB", "acdDescIdentifier"), ("ACD-DESC-MIB", "acdDescSerialNumber"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: acdPowerLost.setStatus('current')
acdDescCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 1))
acdDescGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2))
acdDescGenGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 1)).setObjects(("ACD-DESC-MIB", "acdDescCommercialName"), ("ACD-DESC-MIB", "acdDescMacBaseAddr"), ("ACD-DESC-MIB", "acdDescIdentifier"), ("ACD-DESC-MIB", "acdDescFirmwareVersion"), ("ACD-DESC-MIB", "acdDescHardwareVersion"), ("ACD-DESC-MIB", "acdDescSerialNumber"), ("ACD-DESC-MIB", "acdDescCpuUsageCurrent"), ("ACD-DESC-MIB", "acdDescCpuUsageAverage15"), ("ACD-DESC-MIB", "acdDescCpuUsageAverage30"), ("ACD-DESC-MIB", "acdDescCpuUsageAverage60"), ("ACD-DESC-MIB", "acdDescCpuUsageAverage900"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDescGenGroup = acdDescGenGroup.setStatus('current')
acdDescConnectorGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 2)).setObjects(("ACD-DESC-MIB", "acdDescConnectorName"), ("ACD-DESC-MIB", "acdDescConnectorType"), ("ACD-DESC-MIB", "acdDescConnectorPoESupport"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDescConnectorGroup = acdDescConnectorGroup.setStatus('current')
acdDescPwrGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 3)).setObjects(("ACD-DESC-MIB", "acdDescPwrName"), ("ACD-DESC-MIB", "acdDescPwrType"), ("ACD-DESC-MIB", "acdDescPwrPresent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDescPwrGroup = acdDescPwrGroup.setStatus('current')
acdDescTsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 4)).setObjects(("ACD-DESC-MIB", "acdDescTsCurrentTemp"), ("ACD-DESC-MIB", "acdDescTsFirstThres"), ("ACD-DESC-MIB", "acdDescTsFisrtThresPass"), ("ACD-DESC-MIB", "acdDescTsSecondThres"), ("ACD-DESC-MIB", "acdDescTsSecondThresPass"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDescTsGroup = acdDescTsGroup.setStatus('current')
acdDescNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 2, 5)).setObjects(("ACD-DESC-MIB", "acdPowerLost"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdDescNotificationsGroup = acdDescNotificationsGroup.setStatus('current')
acdAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 1, 1, 15, 1, 1, 1)).setObjects(("ACD-DESC-MIB", "acdDescGenGroup"), ("ACD-DESC-MIB", "acdDescConnectorGroup"), ("ACD-DESC-MIB", "acdDescPwrGroup"), ("ACD-DESC-MIB", "acdDescTsGroup"), ("ACD-DESC-MIB", "acdDescNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdAlarmCompliance = acdAlarmCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-DESC-MIB", acdDescTsFirstThres=acdDescTsFirstThres, acdDescTsSecondThres=acdDescTsSecondThres, acdDescGenGroup=acdDescGenGroup, acdDescConnectorType=acdDescConnectorType, acdDescCpuUsageAverage30=acdDescCpuUsageAverage30, acdDescTsTable=acdDescTsTable, acdDescPwrGroup=acdDescPwrGroup, acdDescCommercialName=acdDescCommercialName, acdDescPwrTable=acdDescPwrTable, acdDescCompliances=acdDescCompliances, PYSNMP_MODULE_ID=acdDesc, acdDescTsCurrentTemp=acdDescTsCurrentTemp, acdDescMIBObjects=acdDescMIBObjects, acdDescConnectorTable=acdDescConnectorTable, acdDescSerialNumber=acdDescSerialNumber, acdDescTsFisrtThresPass=acdDescTsFisrtThresPass, acdDescConnectorName=acdDescConnectorName, acdDescConnectorEntry=acdDescConnectorEntry, acdDescHardwareVersion=acdDescHardwareVersion, acdPowerLost=acdPowerLost, acdDesc=acdDesc, acdDescConnectorGroup=acdDescConnectorGroup, acdDescConnectorID=acdDescConnectorID, acdDescTsGroup=acdDescTsGroup, acdDescMacBaseAddr=acdDescMacBaseAddr, acdDescTsEntry=acdDescTsEntry, acdDescNotifications=acdDescNotifications, acdDescCpuUsageCurrent=acdDescCpuUsageCurrent, acdDescConnectorPoESupport=acdDescConnectorPoESupport, acdDescPwrType=acdDescPwrType, acdDescIdentifier=acdDescIdentifier, acdDescNotificationsGroup=acdDescNotificationsGroup, acdDescPwrEntry=acdDescPwrEntry, acdDescConformance=acdDescConformance, acdDescCpuUsageAverage15=acdDescCpuUsageAverage15, acdDescCpuUsageAverage60=acdDescCpuUsageAverage60, acdDescPwrName=acdDescPwrName, acdDescTsSecondThresPass=acdDescTsSecondThresPass, acdDescPwrPresent=acdDescPwrPresent, acdDescFirmwareVersion=acdDescFirmwareVersion, acdDescGroups=acdDescGroups, acdDescPwrID=acdDescPwrID, acdDescCpuUsageAverage900=acdDescCpuUsageAverage900, acdAlarmCompliance=acdAlarmCompliance, acdDescTsID=acdDescTsID)
