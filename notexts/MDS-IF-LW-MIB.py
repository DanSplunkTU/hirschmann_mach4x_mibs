#
# PySNMP MIB module MDS-IF-LW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-IF-LW-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:22:30 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mdsInterfaces, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsInterfaces")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, Counter32, IpAddress, Unsigned32, MibIdentifier, Bits, NotificationType, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, ObjectIdentity, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier", "Bits", "NotificationType", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "ObjectIdentity", "ModuleIdentity")
TextualConvention, MacAddress, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString", "TruthValue")
mdsIfLwMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6))
mdsIfLwMIB.setRevisions(('2018-09-13 00:00',))
if mibBuilder.loadTexts: mdsIfLwMIB.setLastUpdated('201809130000Z')
if mibBuilder.loadTexts: mdsIfLwMIB.setOrganization('GE MDS LLC http://www.gemds.com')
mIfLwMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1))
mIfLwConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 1))
mIfLwStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2))
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class LinkStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("initializing", 0), ("scanning", 1), ("negotiating", 2), ("authenticating", 3), ("associated", 4), ("disassociated", 5))

class InitStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("off", 0), ("initializing", 1), ("discovering", 2), ("reprogramming", 3), ("configuring", 4), ("complete", 5), ("error", 6))

class DeviceModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("remote", 0), ("accessPoint", 1), ("storeAndForward", 2), ("test", 3))

class ModulationModeType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))
    namedValues = NamedValues(("qpsk25", 2), ("qpsk50", 3), ("qpsk75", 4), ("qam16r50", 5), ("qam16r75", 6))

class AlarmFlags(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("notCalibrated", 23), ("temperature", 0))

class FirmwareRevision(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'

class InetIpAddress(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class FrequencyType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class ChannelType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class FecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("disabled", 0), ("adaptiveGain", 1), ("lowGain", 2))

class RateType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

mIfLwStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1), )
if mibBuilder.loadTexts: mIfLwStatusTable.setStatus('current')
mIfLwStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mIfLwStatusEntry.setStatus('current')
mIfLwLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 1), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwLinkStatus.setStatus('current')
mIfLwInitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 2), InitStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwInitStatus.setStatus('current')
mIfLwCurrentDeviceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 3), DeviceModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwCurrentDeviceMode.setStatus('current')
mIfLwAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 4), AlarmFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwAlarms.setStatus('current')
mIfLwSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwSerialNumber.setStatus('current')
mIfLwFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 6), FirmwareRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwFirmwareRevision.setStatus('current')
mIfLwHardwareId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 7), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwHardwareId.setStatus('current')
mIfLwHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 8), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwHardwareRevision.setStatus('current')
mIfLwTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwTemperature.setStatus('current')
mIfLwApInfoApAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoApAddress.setStatus('current')
mIfLwApInfoIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 11), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoIpAddress.setStatus('current')
mIfLwApInfoConnectedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoConnectedTime.setStatus('current')
mIfLwApInfoRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoRssi.setStatus('current')
mIfLwApInfoSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoSnr.setStatus('current')
mIfLwApInfoMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 15), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwApInfoMod.setStatus('current')
mIfLwMacStatsTxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsTxSuccess.setStatus('current')
mIfLwMacStatsTxQueueFull = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsTxQueueFull.setStatus('current')
mIfLwMacStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsTxError.setStatus('current')
mIfLwMacStatsTxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsTxRetry.setStatus('current')
mIfLwMacStatsRxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsRxSuccess.setStatus('current')
mIfLwMacStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwMacStatsRxError.setStatus('current')
mIfLwModemStatsTxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwModemStatsTxSuccess.setStatus('current')
mIfLwModemStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwModemStatsTxError.setStatus('current')
mIfLwModemStatsRxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwModemStatsRxSuccess.setStatus('current')
mIfLwModemStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwModemStatsRxError.setStatus('current')
mIfLwLastRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwLastRssi.setStatus('current')
mIfLwLastSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 27), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwLastSnr.setStatus('current')
mIfLwLastMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 28), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwLastMod.setStatus('current')
mIfLwLastRate = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 29), RateType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwLastRate.setStatus('current')
mIfLwActiveNic = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 1, 1, 30), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwActiveNic.setStatus('current')
mIfLwStatusConnRemTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2), )
if mibBuilder.loadTexts: mIfLwStatusConnRemTable.setStatus('current')
mIfLwStatusConnRemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-LW-MIB", "mIfLwStatusConnRemAddress"))
if mibBuilder.loadTexts: mIfLwStatusConnRemEntry.setStatus('current')
mIfLwStatusConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemAddress.setStatus('current')
mIfLwStatusConnRemIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemIpAddress.setStatus('current')
mIfLwStatusConnRemTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemTimeToLive.setStatus('current')
mIfLwStatusConnRemLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 4), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemLinkStatus.setStatus('current')
mIfLwStatusConnRemNicId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 5), UnsignedShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemNicId.setStatus('current')
mIfLwStatusConnRemRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemRssi.setStatus('current')
mIfLwStatusConnRemSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemSnr.setStatus('current')
mIfLwStatusConnRemMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 8), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemMod.setStatus('current')
mIfLwStatusConnRemStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxPackets.setStatus('current')
mIfLwStatusConnRemStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxBytes.setStatus('current')
mIfLwStatusConnRemStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxPackets.setStatus('current')
mIfLwStatusConnRemStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxBytes.setStatus('current')
mIfLwStatusConnRemStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxError.setStatus('current')
mIfLwStatusConnRemStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxError.setStatus('current')
mIfLwStatusConnRemStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTxDrop.setStatus('current')
mIfLwStatusConnRemStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsRxDrop.setStatus('current')
mIfLwStatusConnRemStatsGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 17), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsGateway.setStatus('current')
mIfLwStatusConnRemStatsAllIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsAllIp.setStatus('current')
mIfLwStatusConnRemStatsName = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsName.setStatus('current')
mIfLwStatusConnRemStatsAlarmed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsAlarmed.setStatus('current')
mIfLwStatusConnRemStatsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsVersion.setStatus('current')
mIfLwStatusConnRemStatsTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsTemp.setStatus('current')
mIfLwStatusConnRemStatsDwnRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsDwnRssi.setStatus('current')
mIfLwStatusConnRemStatsDwnSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsDwnSnr.setStatus('current')
mIfLwStatusConnRemStatsDwnMod = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 2, 1, 25), ModulationModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusConnRemStatsDwnMod.setStatus('current')
mIfLwStatusEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3), )
if mibBuilder.loadTexts: mIfLwStatusEndpointTable.setStatus('current')
mIfLwStatusEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-LW-MIB", "mIfLwStatusEndpointAddress"))
if mibBuilder.loadTexts: mIfLwStatusEndpointEntry.setStatus('current')
mIfLwStatusEndpointAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointAddress.setStatus('current')
mIfLwStatusEndpointIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointIpAddress.setStatus('current')
mIfLwStatusEndpointTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointTimeToLive.setStatus('current')
mIfLwStatusEndpointRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointRemAddress.setStatus('current')
mIfLwStatusEndpointStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxPackets.setStatus('current')
mIfLwStatusEndpointStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxBytes.setStatus('current')
mIfLwStatusEndpointStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxPackets.setStatus('current')
mIfLwStatusEndpointStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxBytes.setStatus('current')
mIfLwStatusEndpointStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxError.setStatus('current')
mIfLwStatusEndpointStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxError.setStatus('current')
mIfLwStatusEndpointStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsTxDrop.setStatus('current')
mIfLwStatusEndpointStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 1, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfLwStatusEndpointStatsRxDrop.setStatus('current')
mdsIfLwMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3))
mdsIfLwMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 1))
mdsIfLwMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2))
mIfLwCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 1, 1)).setObjects(("MDS-IF-LW-MIB", "mIfLwStatusGroup"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemGroup"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLwCompliance = mIfLwCompliance.setStatus('current')
mIfLwStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2, 1)).setObjects(("MDS-IF-LW-MIB", "mIfLwLinkStatus"), ("MDS-IF-LW-MIB", "mIfLwInitStatus"), ("MDS-IF-LW-MIB", "mIfLwCurrentDeviceMode"), ("MDS-IF-LW-MIB", "mIfLwAlarms"), ("MDS-IF-LW-MIB", "mIfLwSerialNumber"), ("MDS-IF-LW-MIB", "mIfLwFirmwareRevision"), ("MDS-IF-LW-MIB", "mIfLwHardwareId"), ("MDS-IF-LW-MIB", "mIfLwHardwareRevision"), ("MDS-IF-LW-MIB", "mIfLwTemperature"), ("MDS-IF-LW-MIB", "mIfLwApInfoApAddress"), ("MDS-IF-LW-MIB", "mIfLwApInfoIpAddress"), ("MDS-IF-LW-MIB", "mIfLwApInfoConnectedTime"), ("MDS-IF-LW-MIB", "mIfLwApInfoRssi"), ("MDS-IF-LW-MIB", "mIfLwApInfoSnr"), ("MDS-IF-LW-MIB", "mIfLwApInfoMod"), ("MDS-IF-LW-MIB", "mIfLwMacStatsTxSuccess"), ("MDS-IF-LW-MIB", "mIfLwMacStatsTxQueueFull"), ("MDS-IF-LW-MIB", "mIfLwMacStatsTxError"), ("MDS-IF-LW-MIB", "mIfLwMacStatsTxRetry"), ("MDS-IF-LW-MIB", "mIfLwMacStatsRxSuccess"), ("MDS-IF-LW-MIB", "mIfLwMacStatsRxError"), ("MDS-IF-LW-MIB", "mIfLwModemStatsTxSuccess"), ("MDS-IF-LW-MIB", "mIfLwModemStatsTxError"), ("MDS-IF-LW-MIB", "mIfLwModemStatsRxSuccess"), ("MDS-IF-LW-MIB", "mIfLwModemStatsRxError"), ("MDS-IF-LW-MIB", "mIfLwLastRssi"), ("MDS-IF-LW-MIB", "mIfLwLastSnr"), ("MDS-IF-LW-MIB", "mIfLwLastMod"), ("MDS-IF-LW-MIB", "mIfLwLastRate"), ("MDS-IF-LW-MIB", "mIfLwActiveNic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLwStatusGroup = mIfLwStatusGroup.setStatus('current')
mIfLwStatusConnRemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2, 2)).setObjects(("MDS-IF-LW-MIB", "mIfLwStatusConnRemAddress"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemIpAddress"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemTimeToLive"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemLinkStatus"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemNicId"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemRssi"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemSnr"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemMod"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxPackets"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxBytes"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxPackets"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxBytes"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxError"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxError"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTxDrop"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsRxDrop"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsGateway"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsAllIp"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsName"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsAlarmed"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsVersion"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsTemp"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsDwnRssi"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsDwnSnr"), ("MDS-IF-LW-MIB", "mIfLwStatusConnRemStatsDwnMod"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLwStatusConnRemGroup = mIfLwStatusConnRemGroup.setStatus('current')
mIfLwStatusEndpointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 6, 3, 2, 3)).setObjects(("MDS-IF-LW-MIB", "mIfLwStatusEndpointAddress"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointIpAddress"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointTimeToLive"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointRemAddress"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxPackets"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxBytes"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxPackets"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxBytes"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxError"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxError"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsTxDrop"), ("MDS-IF-LW-MIB", "mIfLwStatusEndpointStatsRxDrop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfLwStatusEndpointGroup = mIfLwStatusEndpointGroup.setStatus('current')
mibBuilder.exportSymbols("MDS-IF-LW-MIB", mIfLwStatusEndpointStatsTxPackets=mIfLwStatusEndpointStatsTxPackets, mdsIfLwMIB=mdsIfLwMIB, mIfLwHardwareId=mIfLwHardwareId, mIfLwModemStatsTxSuccess=mIfLwModemStatsTxSuccess, mIfLwLastRate=mIfLwLastRate, mIfLwStatus=mIfLwStatus, mIfLwStatusEndpointGroup=mIfLwStatusEndpointGroup, mIfLwStatusConnRemRssi=mIfLwStatusConnRemRssi, UnsignedShort=UnsignedShort, mIfLwStatusConnRemStatsDwnMod=mIfLwStatusConnRemStatsDwnMod, mIfLwApInfoIpAddress=mIfLwApInfoIpAddress, mIfLwStatusConnRemStatsGateway=mIfLwStatusConnRemStatsGateway, mIfLwStatusEntry=mIfLwStatusEntry, mIfLwMacStatsRxSuccess=mIfLwMacStatsRxSuccess, mIfLwCompliance=mIfLwCompliance, mIfLwLastRssi=mIfLwLastRssi, mIfLwStatusEndpointStatsRxPackets=mIfLwStatusEndpointStatsRxPackets, mIfLwLastMod=mIfLwLastMod, mIfLwTemperature=mIfLwTemperature, mIfLwStatusEndpointEntry=mIfLwStatusEndpointEntry, mIfLwStatusEndpointStatsRxError=mIfLwStatusEndpointStatsRxError, mIfLwInitStatus=mIfLwInitStatus, mIfLwStatusConnRemGroup=mIfLwStatusConnRemGroup, mIfLwStatusEndpointStatsTxBytes=mIfLwStatusEndpointStatsTxBytes, mIfLwStatusEndpointStatsRxDrop=mIfLwStatusEndpointStatsRxDrop, ModulationModeType=ModulationModeType, mIfLwStatusTable=mIfLwStatusTable, mIfLwApInfoConnectedTime=mIfLwApInfoConnectedTime, mIfLwModemStatsRxSuccess=mIfLwModemStatsRxSuccess, mIfLwStatusConnRemStatsVersion=mIfLwStatusConnRemStatsVersion, PYSNMP_MODULE_ID=mdsIfLwMIB, mIfLwAlarms=mIfLwAlarms, mIfLwStatusConnRemTimeToLive=mIfLwStatusConnRemTimeToLive, mIfLwModemStatsRxError=mIfLwModemStatsRxError, mIfLwStatusConnRemIpAddress=mIfLwStatusConnRemIpAddress, mdsIfLwMIBConformance=mdsIfLwMIBConformance, mIfLwStatusConnRemStatsRxBytes=mIfLwStatusConnRemStatsRxBytes, FecType=FecType, mIfLwStatusConnRemStatsTxBytes=mIfLwStatusConnRemStatsTxBytes, mIfLwStatusConnRemLinkStatus=mIfLwStatusConnRemLinkStatus, mIfLwLinkStatus=mIfLwLinkStatus, mIfLwApInfoApAddress=mIfLwApInfoApAddress, mIfLwMacStatsTxError=mIfLwMacStatsTxError, mIfLwApInfoMod=mIfLwApInfoMod, mIfLwStatusConnRemNicId=mIfLwStatusConnRemNicId, mIfLwCurrentDeviceMode=mIfLwCurrentDeviceMode, mIfLwStatusEndpointIpAddress=mIfLwStatusEndpointIpAddress, mIfLwStatusConnRemStatsTxPackets=mIfLwStatusConnRemStatsTxPackets, ChannelType=ChannelType, mIfLwMacStatsTxRetry=mIfLwMacStatsTxRetry, DeviceModeType=DeviceModeType, mIfLwMIBObjects=mIfLwMIBObjects, mIfLwStatusConnRemMod=mIfLwStatusConnRemMod, mIfLwStatusEndpointTable=mIfLwStatusEndpointTable, mdsIfLwMIBGroups=mdsIfLwMIBGroups, mIfLwStatusEndpointStatsTxDrop=mIfLwStatusEndpointStatsTxDrop, mIfLwStatusEndpointRemAddress=mIfLwStatusEndpointRemAddress, mIfLwStatusConnRemStatsTxDrop=mIfLwStatusConnRemStatsTxDrop, mIfLwActiveNic=mIfLwActiveNic, mIfLwMacStatsRxError=mIfLwMacStatsRxError, mIfLwMacStatsTxQueueFull=mIfLwMacStatsTxQueueFull, mIfLwApInfoSnr=mIfLwApInfoSnr, mIfLwStatusConnRemStatsTemp=mIfLwStatusConnRemStatsTemp, mIfLwLastSnr=mIfLwLastSnr, mIfLwStatusGroup=mIfLwStatusGroup, mIfLwFirmwareRevision=mIfLwFirmwareRevision, mIfLwStatusConnRemStatsAlarmed=mIfLwStatusConnRemStatsAlarmed, RateType=RateType, AlarmFlags=AlarmFlags, mIfLwHardwareRevision=mIfLwHardwareRevision, mIfLwModemStatsTxError=mIfLwModemStatsTxError, mIfLwStatusConnRemStatsRxDrop=mIfLwStatusConnRemStatsRxDrop, mIfLwStatusConnRemStatsDwnRssi=mIfLwStatusConnRemStatsDwnRssi, mIfLwStatusConnRemTable=mIfLwStatusConnRemTable, LinkStatus=LinkStatus, mIfLwStatusConnRemStatsDwnSnr=mIfLwStatusConnRemStatsDwnSnr, mIfLwConfig=mIfLwConfig, InitStatus=InitStatus, mIfLwStatusConnRemEntry=mIfLwStatusConnRemEntry, mIfLwStatusConnRemStatsTxError=mIfLwStatusConnRemStatsTxError, mIfLwStatusConnRemStatsRxPackets=mIfLwStatusConnRemStatsRxPackets, mdsIfLwMIBCompliances=mdsIfLwMIBCompliances, mIfLwMacStatsTxSuccess=mIfLwMacStatsTxSuccess, mIfLwStatusConnRemStatsAllIp=mIfLwStatusConnRemStatsAllIp, mIfLwStatusConnRemStatsName=mIfLwStatusConnRemStatsName, FirmwareRevision=FirmwareRevision, FrequencyType=FrequencyType, InetIpAddress=InetIpAddress, mIfLwStatusConnRemAddress=mIfLwStatusConnRemAddress, UnsignedByte=UnsignedByte, mIfLwStatusConnRemSnr=mIfLwStatusConnRemSnr, mIfLwStatusEndpointTimeToLive=mIfLwStatusEndpointTimeToLive, mIfLwSerialNumber=mIfLwSerialNumber, mIfLwStatusEndpointStatsRxBytes=mIfLwStatusEndpointStatsRxBytes, mIfLwStatusEndpointStatsTxError=mIfLwStatusEndpointStatsTxError, mIfLwStatusEndpointAddress=mIfLwStatusEndpointAddress, mIfLwApInfoRssi=mIfLwApInfoRssi, mIfLwStatusConnRemStatsRxError=mIfLwStatusConnRemStatsRxError)
