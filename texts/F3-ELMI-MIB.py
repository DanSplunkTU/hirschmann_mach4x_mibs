#
# PySNMP MIB module F3-ELMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-ELMI-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:14 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
PerfCounter64, OperationalState = mibBuilder.importSymbols("CM-COMMON-MIB", "PerfCounter64", "OperationalState")
shelfIndex, neIndex, slotIndex = mibBuilder.importSymbols("CM-ENTITY-MIB", "shelfIndex", "neIndex", "slotIndex")
cmEthernetNetPortIndex, cmFlowIndex, cmEthernetAccPortIndex = mibBuilder.importSymbols("CM-FACILITY-MIB", "cmEthernetNetPortIndex", "cmFlowIndex", "cmEthernetAccPortIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
ObjectIdentity, Bits, Unsigned32, ModuleIdentity, Counter64, Gauge32, NotificationType, TimeTicks, Integer32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Unsigned32", "ModuleIdentity", "Counter64", "Gauge32", "NotificationType", "TimeTicks", "Integer32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso", "MibIdentifier")
TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString")
f3ElmiMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20))
f3ElmiMIB.setRevisions(('2012-05-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f3ElmiMIB.setRevisionsDescriptions(('\n          Notes from release 201205180000Z\n            (i)Initial Version.',))
if mibBuilder.loadTexts: f3ElmiMIB.setLastUpdated('201205180000Z')
if mibBuilder.loadTexts: f3ElmiMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: f3ElmiMIB.setContactInfo('        Raghav Trivedi\n                     ADVA Optical Networking, Inc.\n                Tel: +1 972 759-1239\n             E-mail: rtrivedi@advaoptical.com\n             Postal: 2301 N. Greenville Ave. #300\n                     Richardson, TX USA 75082')
if mibBuilder.loadTexts: f3ElmiMIB.setDescription('This module defines the ELMI MIB definitions used by \n             the F3 (FSP150CM/CC) product lines.  \n             Copyright (C) ADVA Optical Networking.')
f3ElmiConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1))
f3ElmiStatsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2))
f3ElmiConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3))
class ELMIEvcStatus(TextualConvention, Integer32):
    description = 'Describes the E-LMI EVC status sent in Status messages'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("active", 1), ("inactive", 2), ("partiallyActive", 3))

class ELMIEvcType(TextualConvention, Integer32):
    description = 'Describes the E-LMI EVC type sent in Status messages'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("pointToPoint", 1), ("pointToMultipoint", 2))

f3AccPortElmiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1), )
if mibBuilder.loadTexts: f3AccPortElmiConfigTable.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiConfigTable.setDescription('A list of entries corresponding to the Access Port related\n        ELMI Configuration.')
f3AccPortElmiConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"), (0, "F3-ELMI-MIB", "f3AccPortElmiConfigIndex"))
if mibBuilder.loadTexts: f3AccPortElmiConfigEntry.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiConfigEntry.setDescription('An entry containing information applicable to a particular\n           Access Port ELMI Configuration Entity.')
f3AccPortElmiConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: f3AccPortElmiConfigIndex.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiConfigIndex.setDescription('Unique index value associated with the Access Port ELMI Configuration.')
f3AccPortElmiConfigEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3AccPortElmiConfigEnabled.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiConfigEnabled.setDescription('This object allows SNMP management entities to enable/disable ELMI \n          on the Access Port.')
f3AccPortElmiConfigOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 3), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiConfigOperationalState.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiConfigOperationalState.setDescription('This object represents the Operational State of the ELMI state machine \n             on the Access Port.')
f3AccPortElmiConfigN393StatusCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3AccPortElmiConfigN393StatusCounter.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiConfigN393StatusCounter.setDescription('This object allows specification of maximum number of consecutive errors,\n            after which ELMI is declared as not operational.')
f3AccPortElmiConfigT392PollVerificationTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 30), )).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3AccPortElmiConfigT392PollVerificationTimer.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiConfigT392PollVerificationTimer.setDescription('This object provides the Poll Verification Timer in seconds.  Value of\n             0 will be used to disable the timer.')
f3AccPortElmiConfigAsyncStatusEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3AccPortElmiConfigAsyncStatusEnabled.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiConfigAsyncStatusEnabled.setDescription('This object allows configuration of the capability to generate and\n             send Asynchronous Status.')
f3AccPortElmiConfigMinAsyncMessageInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3AccPortElmiConfigMinAsyncMessageInterval.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiConfigMinAsyncMessageInterval.setDescription('This object allows configuration of the minimum time interval between\n             asynchronouos status messages, in seconds.')
f3NetPortElmiConfigTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2), )
if mibBuilder.loadTexts: f3NetPortElmiConfigTable.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiConfigTable.setDescription('A list of entries corresponding to the Access Port related\n        ELMI Configuration.')
f3NetPortElmiConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"), (0, "F3-ELMI-MIB", "f3NetPortElmiConfigIndex"))
if mibBuilder.loadTexts: f3NetPortElmiConfigEntry.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiConfigEntry.setDescription('An entry containing information applicable to a particular\n           Access Port ELMI Configuration Entity.')
f3NetPortElmiConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: f3NetPortElmiConfigIndex.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiConfigIndex.setDescription('Unique index value associated with the Network Port ELMI Configuration.')
f3NetPortElmiConfigEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortElmiConfigEnabled.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiConfigEnabled.setDescription('This object allows SNMP management entities to enable/disable ELMI \n          on the Network Port.')
f3NetPortElmiConfigOperationalState = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 3), OperationalState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiConfigOperationalState.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiConfigOperationalState.setDescription('This object represents the Operational State of the ELMI state machine \n             on the Network Port.')
f3NetPortElmiConfigN393StatusCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 10)).clone(4)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortElmiConfigN393StatusCounter.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiConfigN393StatusCounter.setDescription('This object allows specification of maximum number of consecutive errors,\n            after which ELMI is declared as not operational.')
f3NetPortElmiConfigT392PollVerificationTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 30), )).clone(15)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortElmiConfigT392PollVerificationTimer.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiConfigT392PollVerificationTimer.setDescription('This object provides the Poll Verification Timer in seconds.  Value of\n             0 will be used to disable the timer.')
f3NetPortElmiConfigAsyncStatusEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortElmiConfigAsyncStatusEnabled.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiConfigAsyncStatusEnabled.setDescription('This object allows configuration of the capability to generate and\n             send Asynchronous Status.')
f3NetPortElmiConfigMinAsyncMessageInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3)).clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3NetPortElmiConfigMinAsyncMessageInterval.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiConfigMinAsyncMessageInterval.setDescription('This object allows configuration of the minimum time interval between\n             asynchronouos status messages, in seconds.')
f3AccPortElmiStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1), )
if mibBuilder.loadTexts: f3AccPortElmiStatsTable.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsTable.setDescription('A list of entries corresponding to the Access Port related\n        ELMI Statistics.')
f3AccPortElmiStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"), (0, "F3-ELMI-MIB", "f3AccPortElmiConfigIndex"), (0, "F3-ELMI-MIB", "f3AccPortElmiStatsIndex"))
if mibBuilder.loadTexts: f3AccPortElmiStatsEntry.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsEntry.setDescription('An entry containing information applicable to a particular\n           Access Port ELMI Statistics Entity.')
f3AccPortElmiStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: f3AccPortElmiStatsIndex.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsIndex.setDescription('Unique index value associated with the Access Port ELMI Statistics.')
f3AccPortElmiStatsLastFullStatusSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsLastFullStatusSent.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsLastFullStatusSent.setDescription('This object provides number of hours, minutes, seconds since last full\n          status report was sent.')
f3AccPortElmiStatsLastStatusCheckSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsLastStatusCheckSent.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsLastStatusCheckSent.setDescription('This object provides number of hours, minutes, seconds since last \n          status check was sent.')
f3AccPortElmiStatsLastFullStatusReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsLastFullStatusReceived.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsLastFullStatusReceived.setDescription('This object provides number of hours, minutes, seconds since last \n          status check was received.')
f3AccPortElmiStatsLastStatusCheckReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsLastStatusCheckReceived.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsLastStatusCheckReceived.setDescription('This object provides number of hours, minutes, seconds since last \n          status check was received.')
f3AccPortElmiStatsInvalidProtocolVersionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 6), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsInvalidProtocolVersionFrames.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsInvalidProtocolVersionFrames.setDescription('This object provides the number of invalid protocol version frames.')
f3AccPortElmiStatsInvalidMessageTypeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 7), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsInvalidMessageTypeFrames.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsInvalidMessageTypeFrames.setDescription('This object provides the number of invalid message type frames.')
f3AccPortElmiStatsOutOfSequenceIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 8), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsOutOfSequenceIEFrames.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsOutOfSequenceIEFrames.setDescription('This object provides the number of ELMI frames received with one or\n          more Information Elements out of sequence.')
f3AccPortElmiStatsDuplicateIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 9), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsDuplicateIEFrames.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsDuplicateIEFrames.setDescription('This object provides the number of ELMI frames received with one or\n          more duplicate Information Elements.')
f3AccPortElmiStatsMissingMandatoryIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 10), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsMissingMandatoryIEFrames.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsMissingMandatoryIEFrames.setDescription('This object provides the number of ELMI frames received with one or\n          more missing mandatory Information Elements.')
f3AccPortElmiStatsErroredMandatoryIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 11), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsErroredMandatoryIEFrames.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsErroredMandatoryIEFrames.setDescription('This object provides the number of ELMI frames received with one or\n          more errors in mandatory Information Elements.')
f3AccPortElmiStatsUnexpectedIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 12), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsUnexpectedIEFrames.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsUnexpectedIEFrames.setDescription('This object provides the number of ELMI frames received with one or\n          more unexpected Information Elements.')
f3AccPortElmiStatsPVTExpirations = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 13), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3AccPortElmiStatsPVTExpirations.setStatus('current')
if mibBuilder.loadTexts: f3AccPortElmiStatsPVTExpirations.setDescription('This object provides the number of times the Protocol Verification Timer(t392)\n          has expired.')
f3NetPortElmiStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2), )
if mibBuilder.loadTexts: f3NetPortElmiStatsTable.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsTable.setDescription('A list of entries corresponding to the Access Port related\n        ELMI Statistics.')
f3NetPortElmiStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"), (0, "F3-ELMI-MIB", "f3NetPortElmiConfigIndex"), (0, "F3-ELMI-MIB", "f3NetPortElmiStatsIndex"))
if mibBuilder.loadTexts: f3NetPortElmiStatsEntry.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsEntry.setDescription('An entry containing information applicable to a particular\n           Access Port ELMI Statistics Entity.')
f3NetPortElmiStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: f3NetPortElmiStatsIndex.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsIndex.setDescription('Unique index value associated with the Access Port ELMI Statistics.')
f3NetPortElmiStatsLastFullStatusSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 2), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsLastFullStatusSent.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsLastFullStatusSent.setDescription('This object provides number of hours, minutes, seconds since last full\n          status report was sent.')
f3NetPortElmiStatsLastStatusCheckSent = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsLastStatusCheckSent.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsLastStatusCheckSent.setDescription('This object provides number of hours, minutes, seconds since last \n          status check was sent.')
f3NetPortElmiStatsLastFullStatusReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsLastFullStatusReceived.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsLastFullStatusReceived.setDescription('This object provides number of hours, minutes, seconds since last \n          status check was received.')
f3NetPortElmiStatsLastStatusCheckReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsLastStatusCheckReceived.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsLastStatusCheckReceived.setDescription('This object provides number of hours, minutes, seconds since last \n          status check was received.')
f3NetPortElmiStatsInvalidProtocolVersionFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 6), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsInvalidProtocolVersionFrames.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsInvalidProtocolVersionFrames.setDescription('This object provides the number of invalid protocol version frames.')
f3NetPortElmiStatsInvalidMessageTypeFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 7), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsInvalidMessageTypeFrames.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsInvalidMessageTypeFrames.setDescription('This object provides the number of invalid message type frames.')
f3NetPortElmiStatsOutOfSequenceIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 8), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsOutOfSequenceIEFrames.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsOutOfSequenceIEFrames.setDescription('This object provides the number of ELMI frames received with one or\n          more Information Elements out of sequence.')
f3NetPortElmiStatsDuplicateIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 9), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsDuplicateIEFrames.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsDuplicateIEFrames.setDescription('This object provides the number of ELMI frames received with one or\n          more duplicate Information Elements.')
f3NetPortElmiStatsMissingMandatoryIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 10), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsMissingMandatoryIEFrames.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsMissingMandatoryIEFrames.setDescription('This object provides the number of ELMI frames received with one or\n          more missing mandatory Information Elements.')
f3NetPortElmiStatsErroredMandatoryIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 11), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsErroredMandatoryIEFrames.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsErroredMandatoryIEFrames.setDescription('This object provides the number of ELMI frames received with one or\n          more errors in mandatory Information Elements.')
f3NetPortElmiStatsUnexpectedIEFrames = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 12), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsUnexpectedIEFrames.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsUnexpectedIEFrames.setDescription('This object provides the number of ELMI frames received with one or\n          more unexpected Information Elements.')
f3NetPortElmiStatsPVTExpirations = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 13), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3NetPortElmiStatsPVTExpirations.setStatus('current')
if mibBuilder.loadTexts: f3NetPortElmiStatsPVTExpirations.setDescription('This object provides the number of times the Protocol Verification Timer(t392)\n          has expired.')
f3ElmiEvcStatusInfoTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3), )
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoTable.setStatus('current')
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoTable.setDescription('A list of entries corresponding to ELMI EVC Status.')
f3ElmiEvcStatusInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1), ).setIndexNames((0, "CM-ENTITY-MIB", "neIndex"), (0, "CM-ENTITY-MIB", "shelfIndex"), (0, "CM-ENTITY-MIB", "slotIndex"), (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"), (0, "CM-FACILITY-MIB", "cmFlowIndex"))
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEntry.setStatus('current')
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEntry.setDescription('An entry containing information about EVC Status information\n           transmitted in the last E-LMI STATUS Message.')
f3ElmiEvcStatusInfoEvcID = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcID.setStatus('current')
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcID.setDescription('This object represents unique EVC Identifier within the System. \n          This value is sent in the E-LMI Status Message as EVC Reference ID.')
f3ElmiEvcStatusInfoEvcFlowID = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcFlowID.setStatus('current')
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcFlowID.setDescription('This object represents EVC Identifier derived from \n          cmFlowCircuitName of the Flow. \n          This value is sent in the E-LMI Status Message as EVC ID.')
f3ElmiEvcStatusInfoEvcStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 3), ELMIEvcStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcStatus.setStatus('current')
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcStatus.setDescription('This object represents E-LMI EVC Status')
f3ElmiEvcStatusInfoEvcType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 4), ELMIEvcType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcType.setStatus('current')
if mibBuilder.loadTexts: f3ElmiEvcStatusInfoEvcType.setDescription('This object represents E-LMI EVC Type')
f3ElmiCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 1))
f3ElmiGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 2))
f3ElmiCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 1, 1)).setObjects(("F3-ELMI-MIB", "f3ElmiConfigGroup"), ("F3-ELMI-MIB", "f3ElmiStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ElmiCompliance = f3ElmiCompliance.setStatus('current')
if mibBuilder.loadTexts: f3ElmiCompliance.setDescription('Describes the requirements for conformance to the F3 ELMI \n             group.')
f3ElmiConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 2, 1)).setObjects(("F3-ELMI-MIB", "f3AccPortElmiConfigEnabled"), ("F3-ELMI-MIB", "f3AccPortElmiConfigOperationalState"), ("F3-ELMI-MIB", "f3AccPortElmiConfigN393StatusCounter"), ("F3-ELMI-MIB", "f3AccPortElmiConfigT392PollVerificationTimer"), ("F3-ELMI-MIB", "f3AccPortElmiConfigAsyncStatusEnabled"), ("F3-ELMI-MIB", "f3AccPortElmiConfigMinAsyncMessageInterval"), ("F3-ELMI-MIB", "f3NetPortElmiConfigEnabled"), ("F3-ELMI-MIB", "f3NetPortElmiConfigOperationalState"), ("F3-ELMI-MIB", "f3NetPortElmiConfigN393StatusCounter"), ("F3-ELMI-MIB", "f3NetPortElmiConfigT392PollVerificationTimer"), ("F3-ELMI-MIB", "f3NetPortElmiConfigAsyncStatusEnabled"), ("F3-ELMI-MIB", "f3NetPortElmiConfigMinAsyncMessageInterval"), ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcID"), ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcFlowID"), ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcStatus"), ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ElmiConfigGroup = f3ElmiConfigGroup.setStatus('current')
if mibBuilder.loadTexts: f3ElmiConfigGroup.setDescription('A collection of objects used to manage the F3 ELMI Configuration data.')
f3ElmiStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 2, 2)).setObjects(("F3-ELMI-MIB", "f3AccPortElmiStatsLastFullStatusSent"), ("F3-ELMI-MIB", "f3AccPortElmiStatsLastStatusCheckSent"), ("F3-ELMI-MIB", "f3AccPortElmiStatsLastFullStatusReceived"), ("F3-ELMI-MIB", "f3AccPortElmiStatsLastStatusCheckReceived"), ("F3-ELMI-MIB", "f3AccPortElmiStatsInvalidProtocolVersionFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsInvalidMessageTypeFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsOutOfSequenceIEFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsDuplicateIEFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsMissingMandatoryIEFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsErroredMandatoryIEFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsUnexpectedIEFrames"), ("F3-ELMI-MIB", "f3AccPortElmiStatsPVTExpirations"), ("F3-ELMI-MIB", "f3NetPortElmiStatsLastFullStatusSent"), ("F3-ELMI-MIB", "f3NetPortElmiStatsLastStatusCheckSent"), ("F3-ELMI-MIB", "f3NetPortElmiStatsLastFullStatusReceived"), ("F3-ELMI-MIB", "f3NetPortElmiStatsLastStatusCheckReceived"), ("F3-ELMI-MIB", "f3NetPortElmiStatsInvalidProtocolVersionFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsInvalidMessageTypeFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsOutOfSequenceIEFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsDuplicateIEFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsMissingMandatoryIEFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsErroredMandatoryIEFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsUnexpectedIEFrames"), ("F3-ELMI-MIB", "f3NetPortElmiStatsPVTExpirations"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3ElmiStatsGroup = f3ElmiStatsGroup.setStatus('current')
if mibBuilder.loadTexts: f3ElmiStatsGroup.setDescription('A collection of objects used to manage the F3 ELMI Configuration data.')
mibBuilder.exportSymbols("F3-ELMI-MIB", f3NetPortElmiConfigTable=f3NetPortElmiConfigTable, f3AccPortElmiStatsLastStatusCheckReceived=f3AccPortElmiStatsLastStatusCheckReceived, f3AccPortElmiConfigMinAsyncMessageInterval=f3AccPortElmiConfigMinAsyncMessageInterval, f3NetPortElmiConfigMinAsyncMessageInterval=f3NetPortElmiConfigMinAsyncMessageInterval, f3AccPortElmiConfigEntry=f3AccPortElmiConfigEntry, f3ElmiEvcStatusInfoTable=f3ElmiEvcStatusInfoTable, f3ElmiEvcStatusInfoEvcID=f3ElmiEvcStatusInfoEvcID, f3NetPortElmiStatsInvalidProtocolVersionFrames=f3NetPortElmiStatsInvalidProtocolVersionFrames, f3AccPortElmiConfigTable=f3AccPortElmiConfigTable, f3AccPortElmiStatsLastStatusCheckSent=f3AccPortElmiStatsLastStatusCheckSent, ELMIEvcStatus=ELMIEvcStatus, f3NetPortElmiConfigT392PollVerificationTimer=f3NetPortElmiConfigT392PollVerificationTimer, f3NetPortElmiConfigAsyncStatusEnabled=f3NetPortElmiConfigAsyncStatusEnabled, f3AccPortElmiStatsOutOfSequenceIEFrames=f3AccPortElmiStatsOutOfSequenceIEFrames, f3ElmiConformance=f3ElmiConformance, f3AccPortElmiConfigT392PollVerificationTimer=f3AccPortElmiConfigT392PollVerificationTimer, f3AccPortElmiStatsUnexpectedIEFrames=f3AccPortElmiStatsUnexpectedIEFrames, f3AccPortElmiConfigIndex=f3AccPortElmiConfigIndex, f3AccPortElmiStatsErroredMandatoryIEFrames=f3AccPortElmiStatsErroredMandatoryIEFrames, f3AccPortElmiStatsTable=f3AccPortElmiStatsTable, f3ElmiCompliances=f3ElmiCompliances, f3NetPortElmiConfigEnabled=f3NetPortElmiConfigEnabled, f3NetPortElmiConfigIndex=f3NetPortElmiConfigIndex, f3AccPortElmiConfigAsyncStatusEnabled=f3AccPortElmiConfigAsyncStatusEnabled, f3NetPortElmiStatsOutOfSequenceIEFrames=f3NetPortElmiStatsOutOfSequenceIEFrames, f3ElmiGroups=f3ElmiGroups, f3ElmiConfigGroup=f3ElmiConfigGroup, f3NetPortElmiStatsErroredMandatoryIEFrames=f3NetPortElmiStatsErroredMandatoryIEFrames, f3NetPortElmiConfigEntry=f3NetPortElmiConfigEntry, f3AccPortElmiConfigN393StatusCounter=f3AccPortElmiConfigN393StatusCounter, f3AccPortElmiStatsLastFullStatusReceived=f3AccPortElmiStatsLastFullStatusReceived, f3NetPortElmiStatsTable=f3NetPortElmiStatsTable, ELMIEvcType=ELMIEvcType, f3ElmiMIB=f3ElmiMIB, f3NetPortElmiStatsInvalidMessageTypeFrames=f3NetPortElmiStatsInvalidMessageTypeFrames, f3NetPortElmiStatsPVTExpirations=f3NetPortElmiStatsPVTExpirations, f3ElmiCompliance=f3ElmiCompliance, f3ElmiEvcStatusInfoEvcStatus=f3ElmiEvcStatusInfoEvcStatus, f3NetPortElmiStatsDuplicateIEFrames=f3NetPortElmiStatsDuplicateIEFrames, f3NetPortElmiStatsMissingMandatoryIEFrames=f3NetPortElmiStatsMissingMandatoryIEFrames, f3NetPortElmiStatsLastStatusCheckSent=f3NetPortElmiStatsLastStatusCheckSent, f3ElmiEvcStatusInfoEntry=f3ElmiEvcStatusInfoEntry, f3NetPortElmiStatsLastFullStatusReceived=f3NetPortElmiStatsLastFullStatusReceived, f3NetPortElmiStatsIndex=f3NetPortElmiStatsIndex, f3ElmiEvcStatusInfoEvcFlowID=f3ElmiEvcStatusInfoEvcFlowID, f3AccPortElmiStatsIndex=f3AccPortElmiStatsIndex, f3AccPortElmiStatsInvalidMessageTypeFrames=f3AccPortElmiStatsInvalidMessageTypeFrames, f3NetPortElmiStatsLastFullStatusSent=f3NetPortElmiStatsLastFullStatusSent, f3NetPortElmiStatsLastStatusCheckReceived=f3NetPortElmiStatsLastStatusCheckReceived, f3ElmiStatsGroup=f3ElmiStatsGroup, f3NetPortElmiStatsEntry=f3NetPortElmiStatsEntry, f3ElmiStatsObjects=f3ElmiStatsObjects, f3NetPortElmiConfigOperationalState=f3NetPortElmiConfigOperationalState, f3AccPortElmiStatsMissingMandatoryIEFrames=f3AccPortElmiStatsMissingMandatoryIEFrames, f3AccPortElmiConfigEnabled=f3AccPortElmiConfigEnabled, f3AccPortElmiStatsEntry=f3AccPortElmiStatsEntry, f3NetPortElmiConfigN393StatusCounter=f3NetPortElmiConfigN393StatusCounter, f3AccPortElmiStatsLastFullStatusSent=f3AccPortElmiStatsLastFullStatusSent, PYSNMP_MODULE_ID=f3ElmiMIB, f3AccPortElmiConfigOperationalState=f3AccPortElmiConfigOperationalState, f3AccPortElmiStatsDuplicateIEFrames=f3AccPortElmiStatsDuplicateIEFrames, f3NetPortElmiStatsUnexpectedIEFrames=f3NetPortElmiStatsUnexpectedIEFrames, f3AccPortElmiStatsInvalidProtocolVersionFrames=f3AccPortElmiStatsInvalidProtocolVersionFrames, f3ElmiEvcStatusInfoEvcType=f3ElmiEvcStatusInfoEvcType, f3AccPortElmiStatsPVTExpirations=f3AccPortElmiStatsPVTExpirations, f3ElmiConfigObjects=f3ElmiConfigObjects)
