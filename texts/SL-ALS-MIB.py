#
# PySNMP MIB module SL-ALS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-ALS-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:33:50 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, ifIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifIndex")
PerfIntervalCount, PerfTotalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfTotalCount", "PerfCurrentCount")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, IpAddress, iso, Counter64, Unsigned32, ModuleIdentity, Bits, TimeTicks, MibIdentifier, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "IpAddress", "iso", "Counter64", "Unsigned32", "ModuleIdentity", "Bits", "TimeTicks", "MibIdentifier", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Integer32")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
slAlsMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 12))
if mibBuilder.loadTexts: slAlsMib.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slAlsMib.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slAlsMib.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slAlsMib.setDescription('This MIB module describes the SiteLight ALS feature.')
slAlsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1))
slAlsTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 12, 2))
slAlsConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1), )
if mibBuilder.loadTexts: slAlsConfigTable.setStatus('current')
if mibBuilder.loadTexts: slAlsConfigTable.setDescription('The ALS configuration Table.')
slAlsConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: slAlsConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slAlsConfigEntry.setDescription('The entries exist for active optical inetfaces \n\t\tifType = 196. The objects in this table are \n\t\tused to configure the ALS algorithm.')
slAlsMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsMode.setStatus('current')
if mibBuilder.loadTexts: slAlsMode.setDescription("Enable/Disable the ALS algorithm.\n        When the Laser Admin Status is 'down' the ALS not operational.")
slAlsLosDeclareTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ms500", 1), ("ms550", 2), ("ms600", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsLosDeclareTime.setStatus('current')
if mibBuilder.loadTexts: slAlsLosDeclareTime.setDescription('Time to declare optical LOS present or clear: 550 +- 50 msec.')
slAlsTestPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("s80", 1), ("s90", 2), ("s100", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsTestPulseTime.setStatus('current')
if mibBuilder.loadTexts: slAlsTestPulseTime.setDescription('Manual restart for test Pulse time (in manual restart) - 90+-10 sec.')
slAlsManualPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ms1750", 1), ("ms2000", 2), ("ms2250", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsManualPulseTime.setStatus('current')
if mibBuilder.loadTexts: slAlsManualPulseTime.setDescription('Manual restart Pulse time (in manual mode) - 2+-0.25 sec.')
slAlsAutomaticPulseTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ms1750", 1), ("ms2000", 2), ("ms2250", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsAutomaticPulseTime.setStatus('current')
if mibBuilder.loadTexts: slAlsAutomaticPulseTime.setDescription('Automatic restart Pulse time (in automatic mode) - 2+-0.25 sec.')
slAlsAutomaticDelayTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(60, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsAutomaticDelayTime.setStatus('current')
if mibBuilder.loadTexts: slAlsAutomaticDelayTime.setDescription('In Automatic mode. The delay between two laser re-activations.')
slAlsLaserTestActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("activate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsLaserTestActivate.setStatus('current')
if mibBuilder.loadTexts: slAlsLaserTestActivate.setDescription('Activate the laser for test operation.')
slAlsLaserManualActivate = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("activate", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsLaserManualActivate.setStatus('current')
if mibBuilder.loadTexts: slAlsLaserManualActivate.setDescription('Activate the laser manual operation.')
slAlsOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slAlsOperStatus.setStatus('current')
if mibBuilder.loadTexts: slAlsOperStatus.setDescription("The operational status of the ALS algorithm.\n        When the Laser Admin Status is 'down' the ALS not operational.")
slAlsResetParams = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 12, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("resetCounters", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slAlsResetParams.setReference('ANSI T1.231-1997 clause 9.1.5.1.')
if mibBuilder.loadTexts: slAlsResetParams.setStatus('current')
if mibBuilder.loadTexts: slAlsResetParams.setDescription('Setting this variable to 1 will reset the ALS \n        parameters to the factory defaults.')
slAlsStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 12, 2, 1)).setObjects(("IF-MIB", "ifIndex"), ("SL-ALS-MIB", "slAlsOperStatus"))
if mibBuilder.loadTexts: slAlsStatusChangeTrap.setStatus('current')
if mibBuilder.loadTexts: slAlsStatusChangeTrap.setDescription('A slAlsStatusChangeTrap is sent when the TX laser status is changed.')
mibBuilder.exportSymbols("SL-ALS-MIB", slAlsMib=slAlsMib, slAlsTraps=slAlsTraps, slAlsConfigTable=slAlsConfigTable, slAlsManualPulseTime=slAlsManualPulseTime, slAlsConfigEntry=slAlsConfigEntry, slAlsTestPulseTime=slAlsTestPulseTime, slAlsMode=slAlsMode, slAlsConfig=slAlsConfig, slAlsAutomaticDelayTime=slAlsAutomaticDelayTime, slAlsAutomaticPulseTime=slAlsAutomaticPulseTime, slAlsLaserManualActivate=slAlsLaserManualActivate, slAlsLaserTestActivate=slAlsLaserTestActivate, PYSNMP_MODULE_ID=slAlsMib, slAlsLosDeclareTime=slAlsLosDeclareTime, slAlsOperStatus=slAlsOperStatus, slAlsResetParams=slAlsResetParams, slAlsStatusChangeTrap=slAlsStatusChangeTrap)
