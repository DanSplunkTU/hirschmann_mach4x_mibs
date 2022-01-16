#
# PySNMP MIB module SL-ALS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-ALS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:42:23 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PerfIntervalCount, PerfTotalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfTotalCount", "PerfCurrentCount")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Integer32, Counter64, ModuleIdentity, IpAddress, NotificationType, MibIdentifier, Gauge32, Counter32, ObjectIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Integer32", "Counter64", "ModuleIdentity", "IpAddress", "NotificationType", "MibIdentifier", "Gauge32", "Counter32", "ObjectIdentity", "TimeTicks", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
slAlsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 12))
if mibBuilder.loadTexts: slAlsMib.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slAlsMib.setOrganization('PacketLight Networks Ltd.')
slAlsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1))
slAlsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 12, 2))
slAlsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1), )
if mibBuilder.loadTexts: slAlsConfigTable.setStatus('current')
slAlsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: slAlsConfigEntry.setStatus('current')
slAlsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsMode.setStatus('current')
slAlsLosDeclareTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ms500", 1), ("ms550", 2), ("ms600", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsLosDeclareTime.setStatus('current')
slAlsTestPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("s80", 1), ("s90", 2), ("s100", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsTestPulseTime.setStatus('current')
slAlsManualPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ms1750", 1), ("ms2000", 2), ("ms2250", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsManualPulseTime.setStatus('current')
slAlsAutomaticPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ms1750", 1), ("ms2000", 2), ("ms2250", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsAutomaticPulseTime.setStatus('current')
slAlsAutomaticDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsAutomaticDelayTime.setStatus('current')
slAlsLaserTestActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("activate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsLaserTestActivate.setStatus('current')
slAlsLaserManualActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("activate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsLaserManualActivate.setStatus('current')
slAlsOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slAlsOperStatus.setStatus('current')
slAlsResetParams = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCounters", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsResetParams.setStatus('current')
slAlsStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 12, 2, 1)).setObjects(("IF-MIB", "ifIndex"), ("SL-ALS-MIB", "slAlsOperStatus"))
if mibBuilder.loadTexts: slAlsStatusChangeTrap.setStatus('current')
mibBuilder.exportSymbols("SL-ALS-MIB", slAlsTestPulseTime=slAlsTestPulseTime, slAlsTraps=slAlsTraps, slAlsMib=slAlsMib, slAlsConfig=slAlsConfig, slAlsResetParams=slAlsResetParams, slAlsLosDeclareTime=slAlsLosDeclareTime, slAlsAutomaticPulseTime=slAlsAutomaticPulseTime, slAlsConfigEntry=slAlsConfigEntry, PYSNMP_MODULE_ID=slAlsMib, slAlsMode=slAlsMode, slAlsLaserManualActivate=slAlsLaserManualActivate, slAlsStatusChangeTrap=slAlsStatusChangeTrap, slAlsConfigTable=slAlsConfigTable, slAlsLaserTestActivate=slAlsLaserTestActivate, slAlsAutomaticDelayTime=slAlsAutomaticDelayTime, slAlsOperStatus=slAlsOperStatus, slAlsManualPulseTime=slAlsManualPulseTime)
