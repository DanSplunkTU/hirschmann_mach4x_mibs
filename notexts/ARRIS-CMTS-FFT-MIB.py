#
# PySNMP MIB module ARRIS-CMTS-FFT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arris/ARRIS-CMTS-FFT-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:54 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
cmtsCommon, = mibBuilder.importSymbols("ARRIS-MIB", "cmtsCommon")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, Counter32, MibIdentifier, Integer32, iso, TimeTicks, enterprises, NotificationType, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "Counter32", "MibIdentifier", "Integer32", "iso", "TimeTicks", "enterprises", "NotificationType", "Unsigned32", "IpAddress")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
cmtsFftMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1))
if mibBuilder.loadTexts: cmtsFftMIB.setLastUpdated('200402270000Z')
if mibBuilder.loadTexts: cmtsFftMIB.setOrganization('Arris International')
dcxFftObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1))
dcxFftUpstreamChannelTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1), )
if mibBuilder.loadTexts: dcxFftUpstreamChannelTable.setStatus('current')
dcxFftUpstreamChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: dcxFftUpstreamChannelEntry.setStatus('current')
dcxFftSize = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 1), Unsigned32().clone(2048)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftSize.setStatus('current')
dcxFftSampleRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("adcRate", 1), ("halfAdcRate", 2), ("quarterAdcRate", 3), ("quadrupleSymbolRate", 4))).clone('halfAdcRate')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftSampleRate.setStatus('current')
dcxFftCentreFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 3), Integer32().clone(40960000)).setUnits('hertz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftCentreFrequency.setStatus('current')
dcxFftWindowing = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("rectangular", 1), ("hanning", 2), ("hamming", 3), ("blackman", 4), ("blackmanHarris", 5))).clone('blackmanHarris')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftWindowing.setStatus('current')
dcxFftLogAveragingTimeConstant = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftLogAveragingTimeConstant.setStatus('current')
dcxFftOutputFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("raw", 1), ("fftIQ", 2), ("fftPower", 3), ("fftAmplitude", 4))).clone('fftAmplitude')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftOutputFormat.setStatus('current')
dcxFftOperatingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("baseSpectrum", 1), ("burstSpectrum", 2), ("periodicSpectrum", 3))).clone('baseSpectrum')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftOperatingMode.setStatus('current')
dcxFftIdleInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 8), Unsigned32().clone(50000)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftIdleInterval.setStatus('current')
dcxFftBurstSid = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 16383)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftBurstSid.setStatus('current')
dcxFftBurstIUC = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftBurstIUC.setStatus('current')
dcxFftLogicalChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 3)).clone(-1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftLogicalChannel.setStatus('current')
dcxFftTriggerCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftTriggerCount.setStatus('current')
dcxFftEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 13), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftEnable.setStatus('current')
dcxFftApplyConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 14), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dcxFftApplyConfig.setStatus('current')
dcxFftInProgress = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFftInProgress.setStatus('current')
dcxFftCurrentTriggers = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFftCurrentTriggers.setStatus('current')
class DcxFftPayloadBuffer(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

dcxFftPayloadTable = MibTable((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 2), )
if mibBuilder.loadTexts: dcxFftPayloadTable.setStatus('current')
dcxFftPayloadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "ARRIS-CMTS-FFT-MIB", "dcxFftPayloadIndex"))
if mibBuilder.loadTexts: dcxFftPayloadEntry.setStatus('current')
dcxFftPayloadIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: dcxFftPayloadIndex.setStatus('current')
dcxFftPayloadData = MibTableColumn((1, 3, 6, 1, 4, 1, 4115, 1, 4, 5, 1, 1, 2, 1, 2), DcxFftPayloadBuffer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dcxFftPayloadData.setStatus('current')
mibBuilder.exportSymbols("ARRIS-CMTS-FFT-MIB", dcxFftOperatingMode=dcxFftOperatingMode, dcxFftUpstreamChannelEntry=dcxFftUpstreamChannelEntry, dcxFftBurstIUC=dcxFftBurstIUC, dcxFftObjects=dcxFftObjects, dcxFftInProgress=dcxFftInProgress, dcxFftPayloadData=dcxFftPayloadData, dcxFftApplyConfig=dcxFftApplyConfig, dcxFftSampleRate=dcxFftSampleRate, dcxFftIdleInterval=dcxFftIdleInterval, dcxFftWindowing=dcxFftWindowing, dcxFftSize=dcxFftSize, dcxFftPayloadTable=dcxFftPayloadTable, dcxFftTriggerCount=dcxFftTriggerCount, cmtsFftMIB=cmtsFftMIB, dcxFftPayloadEntry=dcxFftPayloadEntry, dcxFftCurrentTriggers=dcxFftCurrentTriggers, dcxFftCentreFrequency=dcxFftCentreFrequency, dcxFftBurstSid=dcxFftBurstSid, dcxFftUpstreamChannelTable=dcxFftUpstreamChannelTable, dcxFftLogicalChannel=dcxFftLogicalChannel, DcxFftPayloadBuffer=DcxFftPayloadBuffer, dcxFftEnable=dcxFftEnable, dcxFftPayloadIndex=dcxFftPayloadIndex, dcxFftLogAveragingTimeConstant=dcxFftLogAveragingTimeConstant, PYSNMP_MODULE_ID=cmtsFftMIB, dcxFftOutputFormat=dcxFftOutputFormat)
