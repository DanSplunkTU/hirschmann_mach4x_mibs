#
# PySNMP MIB module RAY3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ray/RAY3-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:31:27 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
ModuleIdentity, mib_2, Integer32, Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, NotificationType, TimeTicks, Gauge32, enterprises, iso, ObjectIdentity, Counter32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "mib-2", "Integer32", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "NotificationType", "TimeTicks", "Gauge32", "enterprises", "iso", "ObjectIdentity", "Counter32", "Counter64", "IpAddress")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
racom = ModuleIdentity((1, 3, 6, 1, 4, 1, 33555))
racom.setRevisions(('2019-10-21 00:00',))
if mibBuilder.loadTexts: racom.setLastUpdated('201910210000Z')
if mibBuilder.loadTexts: racom.setOrganization('Racom s.r.o')
class Tenths(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-1'

class Hundredths(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-2'

class Thousandths(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd-3'

class DisplayStringRaw(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class PhysAddressRaw(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x'

class ServiceState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2))

class AlarmState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2), ("ack", 3))

class OptionSetting(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("on", 1), ("off", 2))

class ModulationList(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    namedValues = NamedValues(("na", 0), ("qpskS", 1), ("qpsk", 2), ("qam16", 3), ("qam32", 4), ("qam64", 5), ("qam128", 6), ("qam256", 7), ("qam512", 8), ("qam1024", 9), ("qam2048", 10), ("qam4096", 11))

ray3 = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4))
station = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 1))
interface = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 2))
statistic = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 3))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 4))
ray3Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 12))
product = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 1, 1))
info = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 1, 2))
status = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3))
chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 1, 4))
system = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 1, 5))
access = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6))
alarm = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8))
productName = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 1, 1), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: productName.setStatus('current')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
unitType = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 1, 3), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitType.setStatus('current')
deviceName = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 2, 1), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceName.setStatus('current')
swVer = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 2, 2), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVer.setStatus('current')
swVerRadio = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 2, 3), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVerRadio.setStatus('current')
systemStatus = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("ok", 1), ("warning", 2), ("alarm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemStatus.setStatus('current')
peerNumber = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: peerNumber.setStatus('current')
securePeerMode = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 7), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: securePeerMode.setStatus('current')
lineStatusII = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("na", 0), ("setup", 1), ("single", 2), ("connecting", 3), ("authorizing", 4), ("ok", 5), ("analyzer", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineStatusII.setStatus('current')
eth1Link = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 9), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eth1Link.setStatus('current')
eth2Link = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 10), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eth2Link.setStatus('current')
temperatureModem = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 1), Hundredths().subtype(subtypeSpec=ValueRangeConstraint(-10000, 10000))).setUnits('deg C').setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureModem.setStatus('current')
temperatureRadio = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 2), Hundredths().subtype(subtypeSpec=ValueRangeConstraint(-10000, 10000))).setUnits('deg C').setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureRadio.setStatus('current')
voltageUnit = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 3), Tenths().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setUnits('V').setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageUnit.setStatus('current')
voltageSource = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("aux", 1), ("poe", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageSource.setStatus('current')
useCpu = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 5, 1), Integer32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: useCpu.setStatus('current')
useMemory = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 5, 2), Integer32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: useMemory.setStatus('current')
useLogStorage = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 5, 3), Integer32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: useLogStorage.setStatus('current')
sshd = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("onlykey", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshd.setStatus('current')
telnetd = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 2), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telnetd.setStatus('current')
httpd = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 3), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: httpd.setStatus('current')
ip = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ip.setStatus('current')
mac = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 5), PhysAddressRaw()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mac.setStatus('current')
managementVlan = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 6), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managementVlan.setStatus('current')
managementVlanId = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managementVlanId.setStatus('current')
wifiHAP = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("disabled", 1), ("enabled-on-air-link-loss", 2), ("force-enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wifiHAP.setStatus('current')
alarmTemperature = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 1), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTemperature.setStatus('current')
alarmVoltageLow = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 2), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmVoltageLow.setStatus('current')
alarmVoltageHigh = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 3), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmVoltageHigh.setStatus('current')
alarmRss = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 4), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmRss.setStatus('current')
alarmBer = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 6), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmBer.setStatus('current')
alarmPeerDisconnected = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 7), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPeerDisconnected.setStatus('current')
alarmEth1Down = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 8), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmEth1Down.setStatus('current')
alarmEth2Down = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 9), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmEth2Down.setStatus('current')
alarmNetBitrate = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 11), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmNetBitrate.setStatus('current')
alarmWifiOn = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 12), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmWifiOn.setStatus('current')
alarmMse = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 13), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMse.setStatus('current')
ifRadio = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1))
ifEth = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2))
rxChannel = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 1), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxChannel.setStatus('current')
txChannel = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 2), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: txChannel.setStatus('current')
rxFreq = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 3), Gauge32()).setUnits('kHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFreq.setStatus('current')
txFreq = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 4), Gauge32()).setUnits('kHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: txFreq.setStatus('current')
rxModulation = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 5), DisplayStringRaw()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxModulation.setStatus('current')
txModulation = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 6), DisplayStringRaw()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txModulation.setStatus('current')
rxModulationIndex = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 7), ModulationList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxModulationIndex.setStatus('current')
txModulationIndex = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 8), ModulationList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txModulationIndex.setStatus('current')
matching = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 11), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matching.setStatus('current')
rfPowerConfigured = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 12), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: rfPowerConfigured.setStatus('current')
netBitrate = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 13), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: netBitrate.setStatus('current')
maxNetBitrate = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 14), Integer32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNetBitrate.setStatus('current')
txBandwidthKHz = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 15), Integer32()).setUnits('kHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: txBandwidthKHz.setStatus('current')
channelArrangement = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("accp", 1), ("acap", 2), ("ccdp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelArrangement.setStatus('current')
rfPowerCurrent = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 17), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: rfPowerCurrent.setStatus('current')
acm = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 18), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acm.setStatus('current')
atpc = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 19), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atpc.setStatus('current')
frequencyTable = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 20), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frequencyTable.setStatus('current')
rxBandwidthKHz = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 21), Integer32()).setUnits('kHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: rxBandwidthKHz.setStatus('current')
ifEthTable = MibTable((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1), )
if mibBuilder.loadTexts: ifEthTable.setStatus('current')
ifEthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1), ).setIndexNames((0, "RAY3-MIB", "speed"))
if mibBuilder.loadTexts: ifEthEntry.setStatus('current')
speed = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: speed.setStatus('current')
duplex = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("full", 1), ("half", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: duplex.setStatus('current')
mdix = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("mdi", 1), ("mdi-x", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdix.setStatus('current')
autonego = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 4), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: autonego.setStatus('current')
flowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("off", 1), ("on", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowControl.setStatus('current')
radio = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2))
ethernet = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 3, 3))
rss = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 1), Tenths().subtype(subtypeSpec=ValueRangeConstraint(-1000, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rss.setStatus('current')
timeAllConnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeAllConnect.setStatus('current')
timeAllDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeAllDisconnect.setStatus('current')
timeMaxDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeMaxDisconnect.setStatus('current')
numDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numDisconnect.setStatus('current')
reliability = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 9), Thousandths().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reliability.setStatus('current')
linkUptime = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkUptime.setStatus('current')
ber = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ber.setStatus('current')
mse = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 12), Tenths().subtype(subtypeSpec=ValueRangeConstraint(-500, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mse.setStatus('current')
ethInThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 1), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: ethInThroughput.setStatus('current')
ethOutThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 2), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: ethOutThroughput.setStatus('current')
eth2InThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 3), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: eth2InThroughput.setStatus('current')
eth2OutThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 4), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: eth2OutThroughput.setStatus('current')
egressQueue = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 4, 3))
speedGuard = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 4, 3, 2), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: speedGuard.setStatus('current')
ray3TrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0))
tr3TemperatureAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 1)).setObjects(("RAY3-MIB", "temperatureModem"), ("RAY3-MIB", "alarmTemperature"))
if mibBuilder.loadTexts: tr3TemperatureAlarm.setStatus('current')
tr3VoltageLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 2)).setObjects(("RAY3-MIB", "voltageUnit"), ("RAY3-MIB", "alarmVoltageLow"))
if mibBuilder.loadTexts: tr3VoltageLowAlarm.setStatus('current')
tr3VoltageHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 3)).setObjects(("RAY3-MIB", "voltageUnit"), ("RAY3-MIB", "alarmVoltageHigh"))
if mibBuilder.loadTexts: tr3VoltageHighAlarm.setStatus('current')
tr3RssAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 4)).setObjects(("RAY3-MIB", "rss"), ("RAY3-MIB", "alarmRss"))
if mibBuilder.loadTexts: tr3RssAlarm.setStatus('current')
tr3MseAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 5)).setObjects(("RAY3-MIB", "mse"), ("RAY3-MIB", "alarmMse"))
if mibBuilder.loadTexts: tr3MseAlarm.setStatus('current')
tr3BerAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 6)).setObjects(("RAY3-MIB", "ber"), ("RAY3-MIB", "alarmBer"))
if mibBuilder.loadTexts: tr3BerAlarm.setStatus('current')
tr3AirDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 7)).setObjects(("RAY3-MIB", "lineStatusII"), ("RAY3-MIB", "alarmPeerDisconnected"))
if mibBuilder.loadTexts: tr3AirDisconnect.setStatus('current')
tr3AirConnect = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 8)).setObjects(("RAY3-MIB", "lineStatusII"), ("RAY3-MIB", "alarmPeerDisconnected"))
if mibBuilder.loadTexts: tr3AirConnect.setStatus('current')
tr3Eth1LinkDown = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 9)).setObjects(("RAY3-MIB", "eth1Link"), ("RAY3-MIB", "alarmEth1Down"))
if mibBuilder.loadTexts: tr3Eth1LinkDown.setStatus('current')
tr3Eth21LinkDown = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 10)).setObjects(("RAY3-MIB", "eth2Link"), ("RAY3-MIB", "alarmEth2Down"))
if mibBuilder.loadTexts: tr3Eth21LinkDown.setStatus('current')
tr3NetBitrate = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 11)).setObjects(("RAY3-MIB", "netBitrate"), ("RAY3-MIB", "alarmNetBitrate"))
if mibBuilder.loadTexts: tr3NetBitrate.setStatus('current')
tr3WifiOn = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 12)).setObjects(("RAY3-MIB", "wifiHAP"), ("RAY3-MIB", "alarmWifiOn"))
if mibBuilder.loadTexts: tr3WifiOn.setStatus('current')
tr3EventAirCapacity = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 101)).setObjects(("RAY3-MIB", "netBitrate"))
if mibBuilder.loadTexts: tr3EventAirCapacity.setStatus('current')
mibBuilder.exportSymbols("RAY3-MIB", ModulationList=ModulationList, racom=racom, securePeerMode=securePeerMode, info=info, wifiHAP=wifiHAP, reliability=reliability, ifEthEntry=ifEthEntry, rxModulationIndex=rxModulationIndex, netBitrate=netBitrate, timeAllConnect=timeAllConnect, peerNumber=peerNumber, temperatureRadio=temperatureRadio, station=station, interface=interface, speedGuard=speedGuard, alarmWifiOn=alarmWifiOn, ip=ip, linkUptime=linkUptime, egressQueue=egressQueue, duplex=duplex, radio=radio, maxNetBitrate=maxNetBitrate, txChannel=txChannel, eth2OutThroughput=eth2OutThroughput, tr3WifiOn=tr3WifiOn, txModulation=txModulation, tr3AirDisconnect=tr3AirDisconnect, telnetd=telnetd, access=access, rxFreq=rxFreq, tr3VoltageLowAlarm=tr3VoltageLowAlarm, tr3RssAlarm=tr3RssAlarm, alarmPeerDisconnected=alarmPeerDisconnected, tr3NetBitrate=tr3NetBitrate, ray3TrapsPrefix=ray3TrapsPrefix, txModulationIndex=txModulationIndex, alarmRss=alarmRss, ifEth=ifEth, rfPowerCurrent=rfPowerCurrent, ethOutThroughput=ethOutThroughput, PYSNMP_MODULE_ID=racom, rss=rss, alarmEth2Down=alarmEth2Down, ifRadio=ifRadio, rxModulation=rxModulation, rxBandwidthKHz=rxBandwidthKHz, product=product, Thousandths=Thousandths, alarmVoltageHigh=alarmVoltageHigh, lineStatusII=lineStatusII, tr3TemperatureAlarm=tr3TemperatureAlarm, useMemory=useMemory, alarmBer=alarmBer, useCpu=useCpu, speed=speed, sshd=sshd, tr3MseAlarm=tr3MseAlarm, voltageSource=voltageSource, managementVlanId=managementVlanId, rfPowerConfigured=rfPowerConfigured, unitType=unitType, swVerRadio=swVerRadio, serialNumber=serialNumber, deviceName=deviceName, OptionSetting=OptionSetting, tr3VoltageHighAlarm=tr3VoltageHighAlarm, swVer=swVer, flowControl=flowControl, alarmMse=alarmMse, mse=mse, DisplayStringRaw=DisplayStringRaw, alarmNetBitrate=alarmNetBitrate, tr3AirConnect=tr3AirConnect, txBandwidthKHz=txBandwidthKHz, PhysAddressRaw=PhysAddressRaw, alarm=alarm, ServiceState=ServiceState, atpc=atpc, acm=acm, tr3Eth21LinkDown=tr3Eth21LinkDown, autonego=autonego, productName=productName, tr3EventAirCapacity=tr3EventAirCapacity, ber=ber, tr3Eth1LinkDown=tr3Eth1LinkDown, eth1Link=eth1Link, mdix=mdix, httpd=httpd, mac=mac, numDisconnect=numDisconnect, systemStatus=systemStatus, channelArrangement=channelArrangement, ray3Traps=ray3Traps, alarmEth1Down=alarmEth1Down, timeMaxDisconnect=timeMaxDisconnect, timeAllDisconnect=timeAllDisconnect, AlarmState=AlarmState, system=system, Hundredths=Hundredths, managementVlan=managementVlan, ethInThroughput=ethInThroughput, ifEthTable=ifEthTable, eth2InThroughput=eth2InThroughput, tr3BerAlarm=tr3BerAlarm, useLogStorage=useLogStorage, eth2Link=eth2Link, alarmVoltageLow=alarmVoltageLow, rxChannel=rxChannel, matching=matching, ray3=ray3, temperatureModem=temperatureModem, alarmTemperature=alarmTemperature, frequencyTable=frequencyTable, Tenths=Tenths, switch=switch, statistic=statistic, status=status, chassis=chassis, txFreq=txFreq, ethernet=ethernet, voltageUnit=voltageUnit)
