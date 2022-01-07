#
# PySNMP MIB module ExtendAirG2 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/exalt/ExtendAirG2
# Produced by pysmi-1.1.8 at Fri Jan  7 16:20:53 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
systemConfig, = mibBuilder.importSymbols("ExaltComProducts", "systemConfig")
BandwidthT, RadioTxPwr11gT, AcmBaseModulationT, ExaltEnableT, AcmPowerBoostEnableT, DiplexerConfigG2T, AcmTargetModulationT, ModulationT, RadioSourceT, AcmPolicyT, BuzTimeoutT = mibBuilder.importSymbols("ExaltComm", "BandwidthT", "RadioTxPwr11gT", "AcmBaseModulationT", "ExaltEnableT", "AcmPowerBoostEnableT", "DiplexerConfigG2T", "AcmTargetModulationT", "ModulationT", "RadioSourceT", "AcmPolicyT", "BuzTimeoutT")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter32, MibIdentifier, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Unsigned32, iso, TimeTicks, Gauge32, Integer32, ModuleIdentity, Bits, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibIdentifier", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Unsigned32", "iso", "TimeTicks", "Gauge32", "Integer32", "ModuleIdentity", "Bits", "NotificationType", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extendAirG2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57))
extendAirG2.setRevisions(('2013-04-26 10:21',))
if mibBuilder.loadTexts: extendAirG2.setLastUpdated('201304261021Z')
if mibBuilder.loadTexts: extendAirG2.setOrganization('Exalt')
extendAirG2TxPower = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 1), RadioTxPwr11gT()).setUnits('Tenths of dBm.').setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2TxPower.setStatus('current')
extendAirG2Bandwidth = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 2), BandwidthT()).setUnits('kHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2Bandwidth.setStatus('current')
extendAirG2Modulation = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 3), ModulationT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2Modulation.setStatus('current')
extendAirG2TXfrequency = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 9))).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2TXfrequency.setStatus('current')
extendAirG2RXfrequency = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 9))).setUnits('MHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2RXfrequency.setStatus('current')
extendAirG2DiplexerConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 6), DiplexerConfigG2T()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2DiplexerConfiguration.setStatus('current')
extendAirG2InsertionLoss = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 200))).setUnits('Hundredth dBm').setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2InsertionLoss.setStatus('current')
extendAirG2BuzTimeout = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 8), BuzTimeoutT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2BuzTimeout.setStatus('current')
extendAirG2AcmMode = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 9), ExaltEnableT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2AcmMode.setStatus('current')
extendAirG2AcmPolicy = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 10), AcmPolicyT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2AcmPolicy.setStatus('current')
extendAirG2AcmBaseModulation = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 11), AcmBaseModulationT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2AcmBaseModulation.setStatus('current')
extendAirG2AcmTargetModulation = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 12), AcmTargetModulationT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2AcmTargetModulation.setStatus('current')
extendAirG2AcmPowerBoostMode = MibScalar((1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 1, 57, 15), AcmPowerBoostEnableT()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: extendAirG2AcmPowerBoostMode.setStatus('current')
mibBuilder.exportSymbols("ExtendAirG2", extendAirG2AcmMode=extendAirG2AcmMode, extendAirG2AcmTargetModulation=extendAirG2AcmTargetModulation, extendAirG2RXfrequency=extendAirG2RXfrequency, extendAirG2AcmPolicy=extendAirG2AcmPolicy, extendAirG2Bandwidth=extendAirG2Bandwidth, extendAirG2Modulation=extendAirG2Modulation, PYSNMP_MODULE_ID=extendAirG2, extendAirG2TXfrequency=extendAirG2TXfrequency, extendAirG2DiplexerConfiguration=extendAirG2DiplexerConfiguration, extendAirG2InsertionLoss=extendAirG2InsertionLoss, extendAirG2AcmBaseModulation=extendAirG2AcmBaseModulation, extendAirG2BuzTimeout=extendAirG2BuzTimeout, extendAirG2AcmPowerBoostMode=extendAirG2AcmPowerBoostMode, extendAirG2=extendAirG2, extendAirG2TxPower=extendAirG2TxPower)
