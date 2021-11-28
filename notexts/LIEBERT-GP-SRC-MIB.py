#
# PySNMP MIB module LIEBERT-GP-SRC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-SRC-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:31:06 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
lgpSrc, liebertSrcModuleReg = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "lgpSrc", "liebertSrcModuleReg")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Counter32, Counter64, Bits, TimeTicks, Unsigned32, iso, IpAddress, ModuleIdentity, NotificationType, ObjectIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Bits", "TimeTicks", "Unsigned32", "iso", "IpAddress", "ModuleIdentity", "NotificationType", "ObjectIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
liebertGlobalProductsSrcModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 12, 1))
liebertGlobalProductsSrcModule.setRevisions(('2017-11-10 00:00', '2017-10-16 00:00', '2017-08-18 00:00',))
if mibBuilder.loadTexts: liebertGlobalProductsSrcModule.setLastUpdated('201711100000Z')
if mibBuilder.loadTexts: liebertGlobalProductsSrcModule.setOrganization('Liebert Corporation')
lgpSrcTable = MibTable((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1), )
if mibBuilder.loadTexts: lgpSrcTable.setStatus('current')
lgpSrcEntry = MibTableRow((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1), ).setIndexNames((0, "LIEBERT-GP-SRC-MIB", "lgpSrcDevId"))
if mibBuilder.loadTexts: lgpSrcEntry.setStatus('current')
lgpSrcDevId = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSrcDevId.setStatus('current')
lgpSrcDevAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSrcDevAddress.setStatus('current')
lgpSrcDevState = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("enabled", 1), ("standbyOffline", 2), ("unavailableOffline", 3), ("absent", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSrcDevState.setStatus('current')
lgpSrcDevTemperatureDegF = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSrcDevTemperatureDegF.setStatus('current')
lgpSrcDevTemperatureSetpointDegF = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureSetpointDegF.setStatus('current')
lgpSrcDevTemperatureDegC = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSrcDevTemperatureDegC.setStatus('current')
lgpSrcDevTemperatureSetpointDegC = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureSetpointDegC.setStatus('current')
lgpSrcDevFanSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 2147483647))).clone(namedValues=NamedValues(("low", 1), ("middle", 2), ("high", 3), ("auto", 4), ("unknown", 2147483647)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevFanSpeed.setStatus('current')
lgpSrcDevPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2147483647))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("unknown", 2147483647)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevPowerStatus.setStatus('current')
lgpSrcDevOperatingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 2147483647))).clone(namedValues=NamedValues(("cooling", 0), ("dehumidify", 1), ("fan", 2), ("ai", 3), ("heating", 4), ("unknown", 2147483647)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevOperatingMode.setStatus('current')
lgpSrcDevTemperatureHighThresholdDegF = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setUnits('degrees Fahrenheit').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureHighThresholdDegF.setStatus('current')
lgpSrcDevTemperatureLowThresholdDegF = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setUnits('degrees Fahrenheit').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureLowThresholdDegF.setStatus('current')
lgpSrcDevTemperatureHighThresholdDegC = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureHighThresholdDegC.setStatus('current')
lgpSrcDevTemperatureLowThresholdDegC = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 10, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2147483647))).clone(namedValues=NamedValues(("unknown", 2147483647)))).setUnits('degrees Celsius').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSrcDevTemperatureLowThresholdDegC.setStatus('current')
mibBuilder.exportSymbols("LIEBERT-GP-SRC-MIB", PYSNMP_MODULE_ID=liebertGlobalProductsSrcModule, lgpSrcDevTemperatureHighThresholdDegC=lgpSrcDevTemperatureHighThresholdDegC, lgpSrcDevTemperatureSetpointDegC=lgpSrcDevTemperatureSetpointDegC, lgpSrcEntry=lgpSrcEntry, lgpSrcDevAddress=lgpSrcDevAddress, liebertGlobalProductsSrcModule=liebertGlobalProductsSrcModule, lgpSrcDevTemperatureHighThresholdDegF=lgpSrcDevTemperatureHighThresholdDegF, lgpSrcDevTemperatureLowThresholdDegC=lgpSrcDevTemperatureLowThresholdDegC, lgpSrcDevTemperatureDegC=lgpSrcDevTemperatureDegC, lgpSrcDevPowerStatus=lgpSrcDevPowerStatus, lgpSrcDevTemperatureSetpointDegF=lgpSrcDevTemperatureSetpointDegF, lgpSrcDevState=lgpSrcDevState, lgpSrcDevFanSpeed=lgpSrcDevFanSpeed, lgpSrcDevId=lgpSrcDevId, lgpSrcDevOperatingMode=lgpSrcDevOperatingMode, lgpSrcDevTemperatureLowThresholdDegF=lgpSrcDevTemperatureLowThresholdDegF, lgpSrcTable=lgpSrcTable, lgpSrcDevTemperatureDegF=lgpSrcDevTemperatureDegF)
