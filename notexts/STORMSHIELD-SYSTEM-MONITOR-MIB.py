#
# PySNMP MIB module STORMSHIELD-SYSTEM-MONITOR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/stormshield/STORMSHIELD-SYSTEM-MONITOR-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:18:47 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Integer32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, IpAddress, MibIdentifier, TimeTicks, Counter32, NotificationType, Bits, ObjectIdentity, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "IpAddress", "MibIdentifier", "TimeTicks", "Counter32", "NotificationType", "Bits", "ObjectIdentity", "Unsigned32", "iso")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
stormshieldMIB, = mibBuilder.importSymbols("STORMSHIELD-SMI-MIB", "stormshieldMIB")
snsSystemMonitor = ModuleIdentity((1, 3, 6, 1, 4, 1, 11256, 1, 10))
snsSystemMonitor.setRevisions(('2017-02-20 00:00',))
if mibBuilder.loadTexts: snsSystemMonitor.setLastUpdated('201702200000Z')
if mibBuilder.loadTexts: snsSystemMonitor.setOrganization('Stormshield')
snsDate = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 10, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDate.setStatus('current')
snsUptime = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 10, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsUptime.setStatus('current')
snsMem = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 10, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsMem.setStatus('current')
snsStatTime = MibScalar((1, 3, 6, 1, 4, 1, 11256, 1, 10, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsStatTime.setStatus('current')
snsDiskTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5), )
if mibBuilder.loadTexts: snsDiskTable.setStatus('current')
snsDiskEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1), ).setIndexNames((0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsDiskEntryIndex"))
if mibBuilder.loadTexts: snsDiskEntry.setStatus('current')
snsDiskEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntryIndex.setStatus('current')
snsDiskEntryDiskName = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntryDiskName.setStatus('current')
snsDiskEntrySmartResult = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntrySmartResult.setStatus('current')
snsDiskEntryIsRaid = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntryIsRaid.setStatus('current')
snsDiskEntryRaidStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntryRaidStatus.setStatus('current')
snsDiskEntryPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsDiskEntryPosition.setStatus('current')
snsPowerSupplyTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 10, 6), )
if mibBuilder.loadTexts: snsPowerSupplyTable.setStatus('current')
snsPowerSupplyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 10, 6, 1), ).setIndexNames((0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsPowerSupplyIndex"))
if mibBuilder.loadTexts: snsPowerSupplyEntry.setStatus('current')
snsPowerSupplyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: snsPowerSupplyIndex.setStatus('current')
snsPowerSupplyPowered = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 6, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsPowerSupplyPowered.setStatus('current')
snsCpuTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 10, 7), )
if mibBuilder.loadTexts: snsCpuTable.setStatus('current')
snsCpuEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 10, 7, 1), ).setIndexNames((0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsCpuIndex"))
if mibBuilder.loadTexts: snsCpuEntry.setStatus('current')
snsCpuIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: snsCpuIndex.setStatus('current')
snsCpuTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 7, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsCpuTemp.setStatus('current')
snsBypassTable = MibTable((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8), )
if mibBuilder.loadTexts: snsBypassTable.setStatus('current')
snsBypassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1), ).setIndexNames((0, "STORMSHIELD-SYSTEM-MONITOR-MIB", "snsBypassIndex"))
if mibBuilder.loadTexts: snsBypassEntry.setStatus('current')
snsBypassIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: snsBypassIndex.setStatus('current')
snsBypassI2CAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsBypassI2CAddress.setStatus('current')
snsBypassSystemOff = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsBypassSystemOff.setStatus('current')
snsBypassJustOn = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsBypassJustOn.setStatus('current')
snsBypassRunTime = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsBypassRunTime.setStatus('current')
snsBypassWatchdog = MibTableColumn((1, 3, 6, 1, 4, 1, 11256, 1, 10, 8, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: snsBypassWatchdog.setStatus('current')
mibBuilder.exportSymbols("STORMSHIELD-SYSTEM-MONITOR-MIB", snsBypassWatchdog=snsBypassWatchdog, snsDiskEntryIndex=snsDiskEntryIndex, snsDiskEntryPosition=snsDiskEntryPosition, snsPowerSupplyEntry=snsPowerSupplyEntry, snsCpuIndex=snsCpuIndex, snsUptime=snsUptime, snsDiskTable=snsDiskTable, snsDate=snsDate, snsSystemMonitor=snsSystemMonitor, snsDiskEntryDiskName=snsDiskEntryDiskName, snsPowerSupplyIndex=snsPowerSupplyIndex, snsBypassTable=snsBypassTable, snsBypassJustOn=snsBypassJustOn, snsDiskEntryRaidStatus=snsDiskEntryRaidStatus, snsCpuTemp=snsCpuTemp, snsPowerSupplyTable=snsPowerSupplyTable, snsBypassRunTime=snsBypassRunTime, snsCpuTable=snsCpuTable, snsMem=snsMem, snsPowerSupplyPowered=snsPowerSupplyPowered, snsBypassI2CAddress=snsBypassI2CAddress, snsBypassSystemOff=snsBypassSystemOff, snsStatTime=snsStatTime, snsDiskEntrySmartResult=snsDiskEntrySmartResult, snsBypassIndex=snsBypassIndex, snsDiskEntryIsRaid=snsDiskEntryIsRaid, snsBypassEntry=snsBypassEntry, snsDiskEntry=snsDiskEntry, PYSNMP_MODULE_ID=snsSystemMonitor, snsCpuEntry=snsCpuEntry)
