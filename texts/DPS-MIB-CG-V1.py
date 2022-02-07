#
# PySNMP MIB module DPS-MIB-CG-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dpstelecom/DPS-MIB-CG-V1
# Produced by pysmi-1.1.8 at Mon Feb  7 16:11:14 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Counter64, MibIdentifier, Counter32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, iso, Bits, Integer32, Unsigned32, enterprises, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter64", "MibIdentifier", "Counter32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "iso", "Bits", "Integer32", "Unsigned32", "enterprises", "TimeTicks", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
dpsCellguard = ModuleIdentity((1, 3, 6, 1, 4, 1, 2682, 2))
dpsCellguard.setRevisions(('2013-10-18 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: dpsCellguard.setRevisionsDescriptions(('First Revision (CTS)',))
if mibBuilder.loadTexts: dpsCellguard.setLastUpdated('201310181200Z')
if mibBuilder.loadTexts: dpsCellguard.setOrganization('DPS Telecom')
if mibBuilder.loadTexts: dpsCellguard.setContactInfo('DPS Support Team \n\t\t\tWeb \thttp://dpstele.com/support\n\t\t\tE-Mail \tsupport@dpstele.com\n\t\t\tPhone\t(559)454-1600')
if mibBuilder.loadTexts: dpsCellguard.setDescription('MIB for Cellguard BSM support on DPS Products')
dpsInc = MibIdentifier((1, 3, 6, 1, 4, 1, 2682))
cgStringChannels = MibTable((1, 3, 6, 1, 4, 1, 2682, 2, 1), )
if mibBuilder.loadTexts: cgStringChannels.setStatus('current')
if mibBuilder.loadTexts: cgStringChannels.setDescription('Holds information on Cellguard battery strings.')
cgStringEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1), ).setIndexNames((0, "DPS-MIB-CG-V1", "cgStrNumber"))
if mibBuilder.loadTexts: cgStringEntry.setStatus('current')
if mibBuilder.loadTexts: cgStringEntry.setDescription('Information about a particular string.')
cgStrNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrNumber.setStatus('current')
if mibBuilder.loadTexts: cgStrNumber.setDescription('String number (1-6)')
cgStrEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrEnabled.setStatus('current')
if mibBuilder.loadTexts: cgStrEnabled.setDescription('Enable status of string')
cgStrStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrStatus.setStatus('current')
if mibBuilder.loadTexts: cgStrStatus.setDescription('The alarm status of the string.')
cgStrVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrVoltage.setStatus('current')
if mibBuilder.loadTexts: cgStrVoltage.setDescription('The voltage measurement of the string.')
cgStrCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrCurrent.setStatus('current')
if mibBuilder.loadTexts: cgStrCurrent.setDescription('The current measurement of the string.')
cgStrTempA = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrTempA.setStatus('current')
if mibBuilder.loadTexts: cgStrTempA.setDescription('Temperature sensor A measurement.')
cgStrTempB = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrTempB.setStatus('current')
if mibBuilder.loadTexts: cgStrTempB.setDescription('Temperature sensor B measurement.')
cgStrConductance = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrConductance.setStatus('current')
if mibBuilder.loadTexts: cgStrConductance.setDescription('The average conductance measurement of the string.')
cgStrLife = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrLife.setStatus('current')
if mibBuilder.loadTexts: cgStrLife.setDescription('The average battery capacity of the string.')
cgBatteryChannels = MibTable((1, 3, 6, 1, 4, 1, 2682, 2, 2), )
if mibBuilder.loadTexts: cgBatteryChannels.setStatus('current')
if mibBuilder.loadTexts: cgBatteryChannels.setDescription('Holds information on batteries.')
cgBatteryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1), ).setIndexNames((0, "DPS-MIB-CG-V1", "cgStringNumber"), (0, "DPS-MIB-CG-V1", "cgBatteryNumber"))
if mibBuilder.loadTexts: cgBatteryEntry.setStatus('current')
if mibBuilder.loadTexts: cgBatteryEntry.setDescription('Information about a particular battery.')
cgStringNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStringNumber.setStatus('current')
if mibBuilder.loadTexts: cgStringNumber.setDescription('String number (1-6)')
cgBatteryNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 240))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgBatteryNumber.setStatus('current')
if mibBuilder.loadTexts: cgBatteryNumber.setDescription('Battery number (1-240)')
cgStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStatus.setStatus('current')
if mibBuilder.loadTexts: cgStatus.setDescription('The alarm status of the battery.')
cgVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgVoltage.setStatus('current')
if mibBuilder.loadTexts: cgVoltage.setDescription('The voltage measurement of the battery.')
cgTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgTemperature.setStatus('current')
if mibBuilder.loadTexts: cgTemperature.setDescription('The temperature measurement of the battery.')
cgStrapResist = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgStrapResist.setStatus('current')
if mibBuilder.loadTexts: cgStrapResist.setDescription('The strap resistance measurement.')
cgConductance = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgConductance.setStatus('current')
if mibBuilder.loadTexts: cgConductance.setDescription('The conductance measurement of the battery.')
cgBatteryLife = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 2, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cgBatteryLife.setStatus('current')
if mibBuilder.loadTexts: cgBatteryLife.setDescription('The capacity of the battery.')
cellguardTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 2, 8000))
cgAlarmTrap = NotificationType((1, 3, 6, 1, 4, 1, 2682, 2, 8000, 1))
if mibBuilder.loadTexts: cgAlarmTrap.setStatus('current')
if mibBuilder.loadTexts: cgAlarmTrap.setDescription('Alarm info from Cellguard system.')
cgTrapType = MibScalar((1, 3, 6, 1, 4, 1, 2682, 2, 8000, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 0), ("voltage", 1), ("current", 2), ("temperature", 3), ("strapResistance", 4), ("life", 5), ("conductance", 6))))
if mibBuilder.loadTexts: cgTrapType.setStatus('current')
if mibBuilder.loadTexts: cgTrapType.setDescription('Trap threshold type.')
cgTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 2682, 2, 8000, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noAlarm", 0), ("minorUnder", 1), ("minorOver", 2), ("majorUnder", 3), ("majorOver", 4), ("notDetected", 5))))
if mibBuilder.loadTexts: cgTrapStatus.setStatus('current')
if mibBuilder.loadTexts: cgTrapStatus.setDescription('Trap threshold status.')
cgTrapValue = MibScalar((1, 3, 6, 1, 4, 1, 2682, 2, 8000, 4), DisplayString())
if mibBuilder.loadTexts: cgTrapValue.setStatus('current')
if mibBuilder.loadTexts: cgTrapValue.setDescription('Trap most recent measurement reading.')
mibBuilder.exportSymbols("DPS-MIB-CG-V1", cgStrVoltage=cgStrVoltage, cgTrapType=cgTrapType, cgBatteryLife=cgBatteryLife, cgStrTempA=cgStrTempA, cgStringChannels=cgStringChannels, cgBatteryChannels=cgBatteryChannels, cgStringNumber=cgStringNumber, cgTrapStatus=cgTrapStatus, cgStrEnabled=cgStrEnabled, dpsInc=dpsInc, cgStrNumber=cgStrNumber, cgAlarmTrap=cgAlarmTrap, cgStrStatus=cgStrStatus, cgStatus=cgStatus, cgTrapValue=cgTrapValue, cgConductance=cgConductance, cgStrConductance=cgStrConductance, cellguardTrap=cellguardTrap, cgBatteryEntry=cgBatteryEntry, dpsCellguard=dpsCellguard, cgStrapResist=cgStrapResist, PYSNMP_MODULE_ID=dpsCellguard, cgVoltage=cgVoltage, cgTemperature=cgTemperature, cgStrLife=cgStrLife, cgStrCurrent=cgStrCurrent, cgStringEntry=cgStringEntry, cgStrTempB=cgStrTempB, cgBatteryNumber=cgBatteryNumber)
