#
# PySNMP MIB module F3-ELMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-ELMI-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:03 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
PerfCounter64, OperationalState = mibBuilder.importSymbols("CM-COMMON-MIB", "PerfCounter64", "OperationalState")
shelfIndex, slotIndex, neIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "shelfIndex", "slotIndex", "neIndex")
cmEthernetNetPortIndex, cmFlowIndex, cmEthernetAccPortIndex = mibBuilder.importSymbols("CM-FACILITY-MIB", "cmEthernetNetPortIndex", "cmFlowIndex", "cmEthernetAccPortIndex")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Gauge32, Integer32, Bits, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, NotificationType, ObjectIdentity, IpAddress, MibIdentifier, Counter32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "Bits", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "NotificationType", "ObjectIdentity", "IpAddress", "MibIdentifier", "Counter32", "Counter64")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
f3ElmiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20))
f3ElmiMIB.setRevisions(('2012-05-18 00:00',))
if mibBuilder.loadTexts: f3ElmiMIB.setLastUpdated('201205180000Z')
if mibBuilder.loadTexts: f3ElmiMIB.setOrganization('ADVA Optical Networking')
f3ElmiConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1))
f3ElmiStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2))
f3ElmiConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3))
class ELMIEvcStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("inactive", 2), ("partiallyActive", 3))

class ELMIEvcType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pointToPoint", 1), ("pointToMultipoint", 2))

f3AccPortElmiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1), )
if mibBuilder.loadTexts: f3AccPortElmiConfigTable.setStatus('current')
f3AccPortElmiConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"), (0, "F3-ELMI-MIB", "f3AccPortElmiConfigIndex"))
if mibBuilder.loadTexts: f3AccPortElmiConfigEntry.setStatus('current')
f3AccPortElmiConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: f3AccPortElmiConfigIndex.setStatus('current')
f3AccPortElmiConfigEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3AccPortElmiConfigEnabled.setStatus('current')
f3AccPortElmiConfigOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 3), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiConfigOperationalState.setStatus('current')
f3AccPortElmiConfigN393StatusCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3AccPortElmiConfigN393StatusCounter.setStatus('current')
f3AccPortElmiConfigT392PollVerificationTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 30), )).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3AccPortElmiConfigT392PollVerificationTimer.setStatus('current')
f3AccPortElmiConfigAsyncStatusEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3AccPortElmiConfigAsyncStatusEnabled.setStatus('current')
f3AccPortElmiConfigMinAsyncMessageInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3AccPortElmiConfigMinAsyncMessageInterval.setStatus('current')
f3NetPortElmiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2), )
if mibBuilder.loadTexts: f3NetPortElmiConfigTable.setStatus('current')
f3NetPortElmiConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"), (0, "F3-ELMI-MIB", "f3NetPortElmiConfigIndex"))
if mibBuilder.loadTexts: f3NetPortElmiConfigEntry.setStatus('current')
f3NetPortElmiConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: f3NetPortElmiConfigIndex.setStatus('current')
f3NetPortElmiConfigEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortElmiConfigEnabled.setStatus('current')
f3NetPortElmiConfigOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 3), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiConfigOperationalState.setStatus('current')
f3NetPortElmiConfigN393StatusCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortElmiConfigN393StatusCounter.setStatus('current')
f3NetPortElmiConfigT392PollVerificationTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 30), )).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortElmiConfigT392PollVerificationTimer.setStatus('current')
f3NetPortElmiConfigAsyncStatusEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortElmiConfigAsyncStatusEnabled.setStatus('current')
f3NetPortElmiConfigMinAsyncMessageInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortElmiConfigMinAsyncMessageInterval.setStatus('current')
f3AccPortElmiStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1), )
if mibBuilder.loadTexts: f3AccPortElmiStatsTable.setStatus('current')
f3AccPortElmiStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"), (0, "F3-ELMI-MIB", "f3AccPortElmiConfigIndex"), (0, "F3-ELMI-MIB", "f3AccPortElmiStatsIndex"))
if mibBuilder.loadTexts: f3AccPortElmiStatsEntry.setStatus('current')
f3AccPortElmiStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: f3AccPortElmiStatsIndex.setStatus('current')
f3AccPortElmiStatsLastFullStatusSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsLastFullStatusSent.setStatus('current')
f3AccPortElmiStatsLastStatusCheckSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsLastStatusCheckSent.setStatus('current')
f3AccPortElmiStatsLastFullStatusReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsLastFullStatusReceived.setStatus('current')
f3AccPortElmiStatsLastStatusCheckReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsLastStatusCheckReceived.setStatus('current')
f3AccPortElmiStatsInvalidProtocolVersionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 6), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsInvalidProtocolVersionFrames.setStatus('current')
f3AccPortElmiStatsInvalidMessageTypeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 7), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsInvalidMessageTypeFrames.setStatus('current')
f3AccPortElmiStatsOutOfSequenceIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 8), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsOutOfSequenceIEFrames.setStatus('current')
f3AccPortElmiStatsDuplicateIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 9), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsDuplicateIEFrames.setStatus('current')
f3AccPortElmiStatsMissingMandatoryIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 10), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsMissingMandatoryIEFrames.setStatus('current')
f3AccPortElmiStatsErroredMandatoryIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 11), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsErroredMandatoryIEFrames.setStatus('current')
f3AccPortElmiStatsUnexpectedIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 12), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsUnexpectedIEFrames.setStatus('current')
f3AccPortElmiStatsPVTExpirations = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 13), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsPVTExpirations.setStatus('current')
f3NetPortElmiStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2), )
if mibBuilder.loadTexts: f3NetPortElmiStatsTable.setStatus('current')
f3NetPortElmiStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"), (0, "F3-ELMI-MIB", "f3NetPortElmiConfigIndex"), (0, "F3-ELMI-MIB", "f3NetPortElmiStatsIndex"))
if mibBuilder.loadTexts: f3NetPortElmiStatsEntry.setStatus('current')
f3NetPortElmiStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: f3NetPortElmiStatsIndex.setStatus('current')
f3NetPortElmiStatsLastFullStatusSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsLastFullStatusSent.setStatus('current')
f3NetPortElmiStatsLastStatusCheckSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsLastStatusCheckSent.setStatus('current')
f3NetPortElmiStatsLastFullStatusReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsLastFullStatusReceived.setStatus('current')
f3NetPortElmiStatsLastStatusCheckReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsLastStatusCheckReceived.setStatus('current')
f3NetPortElmiStatsInvalidProtocolVersionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 6), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsInvalidProtocolVersionFrames.setStatus('current')
f3NetPortElmiStatsInvalidMessageTypeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 7), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsInvalidMessageTypeFrames.setStatus('current')
f3NetPortElmiStatsOutOfSequenceIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 8), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsOutOfSequenceIEFrames.setStatus('current')
f3NetPortElmiStatsDuplicateIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 9), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsDuplicateIEFrames.setStatus('current')
f3NetPortElmiStatsMissingMandatoryIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 10), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsMissingMandatoryIEFrames.setStatus('current')
f3NetPortElmiStatsErroredMandatoryIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 11), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsErroredMandatoryIEFrames.setStatus('current')
f3NetPortElmiStatsUnexpectedIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 12), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsUnexpectedIEFrames.setStatus('current')
f3NetPortElmiStatsPVTExpirations = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 13), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsPVTExpirations.setStatus('current')
f3ElmiEvcStatusInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3), )
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoTable.setStatus('current')
f3ElmiEvcStatusInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"), (0, "CM-FACILITY-MIB", "cmFlowIndex"))
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEntry.setStatus('current')
f3ElmiEvcStatusInfoEvcID = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcID.setStatus('current')
f3ElmiEvcStatusInfoEvcFlowID = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcFlowID.setStatus('current')
f3ElmiEvcStatusInfoEvcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 3), ELMIEvcStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcStatus.setStatus('current')
f3ElmiEvcStatusInfoEvcType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 4), ELMIEvcType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcType.setStatus('current')
f3ElmiCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 1))
f3ElmiGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 2))
f3ElmiCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 1, 1)).setObjects(("F3-ELMI-MIB", "f3ElmiConfigGroup"), ("F3-ELMI-MIB", "f3ElmiStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ElmiCompliance = f3ElmiCompliance.setStatus('current')
f3ElmiConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 2, 1)).setObjects(("F3-ELMI-MIB", "f3AccPortElmiConfigEnabled"), ("F3-ELMI-MIB", "f3AccPortElmiConfigOperationalState"), ("F3-ELMI-MIB", "f3AccPortElmiConfigN393StatusCounter"), ("F3-ELMI-MIB", "f3AccPortElmiConfigT392PollVerificationTimer"), ("F3-ELMI-MIB", "f3AccPortElmiConfigAsyncStatusEnabled"), ("F3-ELMI-MIB", "f3AccPortElmiConfigMinAsyncMessageInterval"), ("F3-ELMI-MIB", "f3NetPortElmiConfigEnabled"), ("F3-ELMI-MIB", "f3NetPortElmiConfigOperationalState"), ("F3-ELMI-MIB", "f3NetPortElmiConfigN393StatusCounter"), ("F3-ELMI-MIB", "f3NetPortElmiConfigT392PollVerificationTimer"), ("F3-ELMI-MIB", "f3NetPortElmiConfigAsyncStatusEnabled"), ("F3-ELMI-MIB", "f3NetPortElmiConfigMinAsyncMessageInterval"), ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcID"), ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcFlowID"), ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcStatus"), ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ElmiConfigGroup = f3ElmiConfigGroup.setStatus('current')
f3ElmiStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 2, 2)).setObjects(("F3-ELMI-MIB", "f3AccPortElmiStatsLastFullStatusSent"), ("F3-ELMI-MIB", "f3AccPortElmiStatsLastStatusCheckSent"), ("F3-ELMI-MIB", "f3AccPortElmiStatsLastFullStatusReceived"), ("F3-ELMI-MIB", "f3AccPortElmiStatsLastStatusCheckReceived"), ("F3-ELMI-MIB", "f3AccPortElmiStatsInvalidProtocolVersionFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsInvalidMessageTypeFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsOutOfSequenceIEFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsDuplicateIEFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsMissingMandatoryIEFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsErroredMandatoryIEFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsUnexpectedIEFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsPVTExpirations"), ("F3-ELMI-MIB", "f3NetPortElmiStatsLastFullStatusSent"), ("F3-ELMI-MIB", "f3NetPortElmiStatsLastStatusCheckSent"), ("F3-ELMI-MIB", "f3NetPortElmiStatsLastFullStatusReceived"), ("F3-ELMI-MIB", "f3NetPortElmiStatsLastStatusCheckReceived"), ("F3-ELMI-MIB", "f3NetPortElmiStatsInvalidProtocolVersionFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsInvalidMessageTypeFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsOutOfSequenceIEFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsDuplicateIEFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsMissingMandatoryIEFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsErroredMandatoryIEFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsUnexpectedIEFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsPVTExpirations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ElmiStatsGroup = f3ElmiStatsGroup.setStatus('current')
mibBuilder.exportSymbols("F3-ELMI-MIB", f3NetPortElmiConfigAsyncStatusEnabled=f3NetPortElmiConfigAsyncStatusEnabled, f3NetPortElmiStatsInvalidProtocolVersionFrames=f3NetPortElmiStatsInvalidProtocolVersionFrames, f3AccPortElmiStatsErroredMandatoryIEFrames=f3AccPortElmiStatsErroredMandatoryIEFrames, f3NetPortElmiConfigMinAsyncMessageInterval=f3NetPortElmiConfigMinAsyncMessageInterval, f3NetPortElmiStatsIndex=f3NetPortElmiStatsIndex, f3AccPortElmiConfigT392PollVerificationTimer=f3AccPortElmiConfigT392PollVerificationTimer, f3ElmiEvcStatusInfoEvcID=f3ElmiEvcStatusInfoEvcID, f3ElmiEvcStatusInfoEvcFlowID=f3ElmiEvcStatusInfoEvcFlowID, f3NetPortElmiStatsLastStatusCheckSent=f3NetPortElmiStatsLastStatusCheckSent, f3NetPortElmiStatsDuplicateIEFrames=f3NetPortElmiStatsDuplicateIEFrames, ELMIEvcStatus=ELMIEvcStatus, f3ElmiEvcStatusInfoEntry=f3ElmiEvcStatusInfoEntry, f3ElmiConformance=f3ElmiConformance, PYSNMP_MODULE_ID=f3ElmiMIB, f3NetPortElmiStatsUnexpectedIEFrames=f3NetPortElmiStatsUnexpectedIEFrames, f3AccPortElmiStatsMissingMandatoryIEFrames=f3AccPortElmiStatsMissingMandatoryIEFrames, f3AccPortElmiStatsEntry=f3AccPortElmiStatsEntry, f3ElmiEvcStatusInfoEvcType=f3ElmiEvcStatusInfoEvcType, f3NetPortElmiConfigN393StatusCounter=f3NetPortElmiConfigN393StatusCounter, f3NetPortElmiStatsOutOfSequenceIEFrames=f3NetPortElmiStatsOutOfSequenceIEFrames, f3AccPortElmiStatsLastFullStatusSent=f3AccPortElmiStatsLastFullStatusSent, f3AccPortElmiConfigN393StatusCounter=f3AccPortElmiConfigN393StatusCounter, f3AccPortElmiStatsIndex=f3AccPortElmiStatsIndex, f3NetPortElmiStatsLastStatusCheckReceived=f3NetPortElmiStatsLastStatusCheckReceived, f3NetPortElmiStatsInvalidMessageTypeFrames=f3NetPortElmiStatsInvalidMessageTypeFrames, f3ElmiEvcStatusInfoTable=f3ElmiEvcStatusInfoTable, f3NetPortElmiConfigT392PollVerificationTimer=f3NetPortElmiConfigT392PollVerificationTimer, f3ElmiMIB=f3ElmiMIB, f3NetPortElmiStatsPVTExpirations=f3NetPortElmiStatsPVTExpirations, f3AccPortElmiConfigOperationalState=f3AccPortElmiConfigOperationalState, f3AccPortElmiConfigEntry=f3AccPortElmiConfigEntry, f3ElmiStatsObjects=f3ElmiStatsObjects, ELMIEvcType=ELMIEvcType, f3NetPortElmiConfigOperationalState=f3NetPortElmiConfigOperationalState, f3NetPortElmiConfigEnabled=f3NetPortElmiConfigEnabled, f3AccPortElmiStatsLastFullStatusReceived=f3AccPortElmiStatsLastFullStatusReceived, f3AccPortElmiStatsInvalidProtocolVersionFrames=f3AccPortElmiStatsInvalidProtocolVersionFrames, f3AccPortElmiStatsDuplicateIEFrames=f3AccPortElmiStatsDuplicateIEFrames, f3AccPortElmiStatsUnexpectedIEFrames=f3AccPortElmiStatsUnexpectedIEFrames, f3ElmiStatsGroup=f3ElmiStatsGroup, f3NetPortElmiStatsErroredMandatoryIEFrames=f3NetPortElmiStatsErroredMandatoryIEFrames, f3NetPortElmiStatsLastFullStatusReceived=f3NetPortElmiStatsLastFullStatusReceived, f3AccPortElmiConfigEnabled=f3AccPortElmiConfigEnabled, f3ElmiConfigObjects=f3ElmiConfigObjects, f3NetPortElmiStatsLastFullStatusSent=f3NetPortElmiStatsLastFullStatusSent, f3ElmiCompliance=f3ElmiCompliance, f3AccPortElmiStatsLastStatusCheckReceived=f3AccPortElmiStatsLastStatusCheckReceived, f3NetPortElmiStatsMissingMandatoryIEFrames=f3NetPortElmiStatsMissingMandatoryIEFrames, f3ElmiEvcStatusInfoEvcStatus=f3ElmiEvcStatusInfoEvcStatus, f3AccPortElmiConfigAsyncStatusEnabled=f3AccPortElmiConfigAsyncStatusEnabled, f3AccPortElmiStatsInvalidMessageTypeFrames=f3AccPortElmiStatsInvalidMessageTypeFrames, f3ElmiConfigGroup=f3ElmiConfigGroup, f3ElmiGroups=f3ElmiGroups, f3AccPortElmiStatsPVTExpirations=f3AccPortElmiStatsPVTExpirations, f3AccPortElmiConfigMinAsyncMessageInterval=f3AccPortElmiConfigMinAsyncMessageInterval, f3AccPortElmiStatsTable=f3AccPortElmiStatsTable, f3ElmiCompliances=f3ElmiCompliances, f3AccPortElmiStatsOutOfSequenceIEFrames=f3AccPortElmiStatsOutOfSequenceIEFrames, f3NetPortElmiConfigIndex=f3NetPortElmiConfigIndex, f3AccPortElmiConfigIndex=f3AccPortElmiConfigIndex, f3NetPortElmiStatsEntry=f3NetPortElmiStatsEntry, f3NetPortElmiStatsTable=f3NetPortElmiStatsTable, f3AccPortElmiConfigTable=f3AccPortElmiConfigTable, f3NetPortElmiConfigEntry=f3NetPortElmiConfigEntry, f3NetPortElmiConfigTable=f3NetPortElmiConfigTable, f3AccPortElmiStatsLastStatusCheckSent=f3AccPortElmiStatsLastStatusCheckSent)
