#
# PySNMP MIB module DPS-MIB-CG-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dpstelecom/DPS-MIB-CG-V1
# Produced by pysmi-1.1.8 at Sun Jan 16 00:35:41 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, NotificationType, TimeTicks, ObjectIdentity, Integer32, Gauge32, enterprises, Bits, iso, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "NotificationType", "TimeTicks", "ObjectIdentity", "Integer32", "Gauge32", "enterprises", "Bits", "iso", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dpsCellguard = ModuleIdentity((1, 3, 6, 1, 4, 1, 2682, 2))
dpsCellguard.setRevisions(('2013-10-18 12:00',))
if mibBuilder.loadTexts: dpsCellguard.setLastUpdated('201310181200Z')
if mibBuilder.loadTexts: dpsCellguard.setOrganization('DPS Telecom')
dpsInc = MibIdentifier((1, 3, 6, 1, 4, 1, 2682))
cgStringChannels = MibTable((1, 3, 6, 1, 4, 1, 2682, 2, 1), )
if mibBuilder.loadTexts: cgStringChannels.setStatus('current')
cgStringEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1), ).setIndexNames((0, "DPS-MIB-CG-V1", "cgStrNumber"))
if mibBuilder.loadTexts: cgStringEntry.setStatus('current')
cgStrNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrNumber.setStatus('current')
cgStrEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrEnabled.setStatus('current')
cgStrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrStatus.setStatus('current')
cgStrVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrVoltage.setStatus('current')
cgStrCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrCurrent.setStatus('current')
cgStrTempA = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrTempA.setStatus('current')
cgStrTempB = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrTempB.setStatus('current')
cgStrConductance = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrConductance.setStatus('current')
cgStrLife = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrLife.setStatus('current')
cgBatteryChannels = MibTable((1, 3, 6, 1, 4, 1, 2682, 2, 2), )
if mibBuilder.loadTexts: cgBatteryChannels.setStatus('current')
cgBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1), ).setIndexNames((0, "DPS-MIB-CG-V1", "cgStringNumber"), (0, "DPS-MIB-CG-V1", "cgBatteryNumber"))
if mibBuilder.loadTexts: cgBatteryEntry.setStatus('current')
cgStringNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStringNumber.setStatus('current')
cgBatteryNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgBatteryNumber.setStatus('current')
cgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStatus.setStatus('current')
cgVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgVoltage.setStatus('current')
cgTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgTemperature.setStatus('current')
cgStrapResist = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrapResist.setStatus('current')
cgConductance = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgConductance.setStatus('current')
cgBatteryLife = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgBatteryLife.setStatus('current')
cellguardTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 2, 8000))
cgAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 2682, 2, 8000, 1))
if mibBuilder.loadTexts: cgAlarmTrap.setStatus('current')
cgTrapType = MibScalar((1, 3, 6, 1, 4, 1, 2682, 2, 8000, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 0), ("voltage", 1), ("current", 2), ("temperature", 3), ("strapResistance", 4), ("life", 5), ("conductance", 6))))
if mibBuilder.loadTexts: cgTrapType.setStatus('current')
cgTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 2682, 2, 8000, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noAlarm", 0), ("minorUnder", 1), ("minorOver", 2), ("majorUnder", 3), ("majorOver", 4), ("notDetected", 5))))
if mibBuilder.loadTexts: cgTrapStatus.setStatus('current')
cgTrapValue = MibScalar((1, 3, 6, 1, 4, 1, 2682, 2, 8000, 4), DisplayString())
if mibBuilder.loadTexts: cgTrapValue.setStatus('current')
mibBuilder.exportSymbols("DPS-MIB-CG-V1", cgVoltage=cgVoltage, cgStrTempB=cgStrTempB, cgStrapResist=cgStrapResist, cgStatus=cgStatus, cellguardTrap=cellguardTrap, cgBatteryChannels=cgBatteryChannels, cgStrCurrent=cgStrCurrent, cgStringEntry=cgStringEntry, cgStrStatus=cgStrStatus, cgBatteryEntry=cgBatteryEntry, cgStringChannels=cgStringChannels, cgStrConductance=cgStrConductance, cgStringNumber=cgStringNumber, cgStrVoltage=cgStrVoltage, cgStrLife=cgStrLife, cgTrapValue=cgTrapValue, cgStrEnabled=cgStrEnabled, cgStrTempA=cgStrTempA, dpsCellguard=dpsCellguard, cgTrapType=cgTrapType, cgAlarmTrap=cgAlarmTrap, dpsInc=dpsInc, cgBatteryLife=cgBatteryLife, PYSNMP_MODULE_ID=dpsCellguard, cgStrNumber=cgStrNumber, cgConductance=cgConductance, cgTemperature=cgTemperature, cgBatteryNumber=cgBatteryNumber, cgTrapStatus=cgTrapStatus)
