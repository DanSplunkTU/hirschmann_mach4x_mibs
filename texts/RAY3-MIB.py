#
# PySNMP MIB module RAY3-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ray/RAY3-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:43:40 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
Bits, NotificationType, mib_2, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, IpAddress, Integer32, Counter64, iso, ObjectIdentity, enterprises, Unsigned32, ModuleIdentity, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "mib-2", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "IpAddress", "Integer32", "Counter64", "iso", "ObjectIdentity", "enterprises", "Unsigned32", "ModuleIdentity", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "DateAndTime")
racom = ModuleIdentity((1, 3, 6, 1, 4, 1, 33555))
racom.setRevisions(('2019-10-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: racom.setRevisionsDescriptions(('Latest version of this MIB module',))
if mibBuilder.loadTexts: racom.setLastUpdated('201910210000Z')
if mibBuilder.loadTexts: racom.setOrganization('Racom s.r.o')
if mibBuilder.loadTexts: racom.setContactInfo('Racom s.r.o\n\t\t\tMirova 1283\n\t\t\t592 31 Nove Mesto na Morave\n\t\t\tCzech Republic\n\t\t\tTel: +420 722 937 522\n\t\t\tE-mail: racom@racom.eu')
if mibBuilder.loadTexts: racom.setDescription('The MIB module defines management objects for RAy product series. Revision 201909200000Z.')
class Tenths(TextualConvention, Integer32):
    description = 'Numeric 32-bit type with 0.1 precision without subtyping.'
    status = 'current'
    displayHint = 'd-1'

class Hundredths(TextualConvention, Integer32):
    description = 'Numeric 32-bit type with 0.01 precision without subtyping.'
    status = 'current'
    displayHint = 'd-2'

class Thousandths(TextualConvention, Integer32):
    description = 'Numeric 32-bit type with 0.001 precision without subtyping.'
    status = 'current'
    displayHint = 'd-3'

class DisplayStringRaw(TextualConvention, OctetString):
    description = 'Unlimited display string - UTF8 encoding.'
    status = 'current'
    displayHint = '1t'

class PhysAddressRaw(TextualConvention, OctetString):
    description = 'Unlimited physic address - hexadecimal encoding for each octet.'
    status = 'current'
    displayHint = '1x'

class ServiceState(TextualConvention, Integer32):
    description = 'System service or device state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2))

class AlarmState(TextualConvention, Integer32):
    description = 'Alarm status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("na", 0), ("up", 1), ("down", 2), ("ack", 3))

class OptionSetting(TextualConvention, Integer32):
    description = 'Setting of some options.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("na", 0), ("on", 1), ("off", 2))

class ModulationList(TextualConvention, Integer32):
    description = 'Radio channel modulations numerical list'
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
if mibBuilder.loadTexts: productName.setDescription('Product name.')
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
if mibBuilder.loadTexts: serialNumber.setDescription('Product serial number.')
unitType = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 1, 3), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: unitType.setStatus('current')
if mibBuilder.loadTexts: unitType.setDescription('Station type (L or H).')
deviceName = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 2, 1), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: deviceName.setStatus('current')
if mibBuilder.loadTexts: deviceName.setDescription('Station name.')
swVer = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 2, 2), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVer.setStatus('current')
if mibBuilder.loadTexts: swVer.setDescription('Firmware version.')
swVerRadio = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 2, 3), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: swVerRadio.setStatus('current')
if mibBuilder.loadTexts: swVerRadio.setDescription('Radio firmware version.')
systemStatus = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("ok", 1), ("warning", 2), ("alarm", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemStatus.setStatus('current')
if mibBuilder.loadTexts: systemStatus.setDescription('Unit status.')
peerNumber = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: peerNumber.setStatus('current')
if mibBuilder.loadTexts: peerNumber.setDescription('Peer station serial number.')
securePeerMode = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 7), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: securePeerMode.setStatus('current')
if mibBuilder.loadTexts: securePeerMode.setDescription('Secure peer mode.')
lineStatusII = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("na", 0), ("setup", 1), ("single", 2), ("connecting", 3), ("authorizing", 4), ("ok", 5), ("analyzer", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lineStatusII.setStatus('current')
if mibBuilder.loadTexts: lineStatusII.setDescription('Radio link status.')
eth1Link = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 9), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eth1Link.setStatus('current')
if mibBuilder.loadTexts: eth1Link.setDescription('Ethernet 1 link status.')
eth2Link = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 3, 10), ServiceState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eth2Link.setStatus('current')
if mibBuilder.loadTexts: eth2Link.setDescription('Ethernet 2 link status.')
temperatureModem = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 1), Hundredths().subtype(subtypeSpec=ValueRangeConstraint(-10000, 10000))).setUnits('deg C').setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureModem.setStatus('current')
if mibBuilder.loadTexts: temperatureModem.setDescription('Modem temperature in hundredths of Celsius.')
temperatureRadio = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 2), Hundredths().subtype(subtypeSpec=ValueRangeConstraint(-10000, 10000))).setUnits('deg C').setMaxAccess("readonly")
if mibBuilder.loadTexts: temperatureRadio.setStatus('current')
if mibBuilder.loadTexts: temperatureRadio.setDescription('Radio temperature in hundredths of Celsius.')
voltageUnit = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 3), Tenths().subtype(subtypeSpec=ValueRangeConstraint(0, 1000))).setUnits('V').setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageUnit.setStatus('current')
if mibBuilder.loadTexts: voltageUnit.setDescription('Power supply voltage in tenths of Volts (V).')
voltageSource = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 4, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("aux", 1), ("poe", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: voltageSource.setStatus('current')
if mibBuilder.loadTexts: voltageSource.setDescription('Source of supply voltage.')
useCpu = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 5, 1), Integer32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: useCpu.setStatus('current')
if mibBuilder.loadTexts: useCpu.setDescription('System use CPU in %.')
useMemory = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 5, 2), Integer32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: useMemory.setStatus('current')
if mibBuilder.loadTexts: useMemory.setDescription('System use memory in %.')
useLogStorage = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 5, 3), Integer32()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: useLogStorage.setStatus('current')
if mibBuilder.loadTexts: useLogStorage.setDescription('Use storage for log in %.')
sshd = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("on", 1), ("onlykey", 2), ("off", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sshd.setStatus('current')
if mibBuilder.loadTexts: sshd.setDescription('Management interface: SSH.')
telnetd = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 2), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: telnetd.setStatus('current')
if mibBuilder.loadTexts: telnetd.setDescription('Management interface: Telnet.')
httpd = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 3), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: httpd.setStatus('current')
if mibBuilder.loadTexts: httpd.setDescription('Management interface: HTTP.')
ip = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ip.setStatus('current')
if mibBuilder.loadTexts: ip.setDescription('Management interface: IP address.')
mac = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 5), PhysAddressRaw()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mac.setStatus('current')
if mibBuilder.loadTexts: mac.setDescription('Management interface: MAC address.')
managementVlan = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 6), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managementVlan.setStatus('current')
if mibBuilder.loadTexts: managementVlan.setDescription('Management interface: VLAN on/off.')
managementVlanId = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: managementVlanId.setStatus('current')
if mibBuilder.loadTexts: managementVlanId.setDescription('Management interface: VLAN ID.')
wifiHAP = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 6, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("disabled", 1), ("enabled-on-air-link-loss", 2), ("force-enabled", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wifiHAP.setStatus('current')
if mibBuilder.loadTexts: wifiHAP.setDescription('Management interface: WiFi Host Access Point.')
alarmTemperature = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 1), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmTemperature.setStatus('current')
if mibBuilder.loadTexts: alarmTemperature.setDescription('Temperature alarm state.')
alarmVoltageLow = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 2), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmVoltageLow.setStatus('current')
if mibBuilder.loadTexts: alarmVoltageLow.setDescription('Low voltage alarm state.')
alarmVoltageHigh = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 3), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmVoltageHigh.setStatus('current')
if mibBuilder.loadTexts: alarmVoltageHigh.setDescription('High voltage alarm state.')
alarmRss = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 4), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmRss.setStatus('current')
if mibBuilder.loadTexts: alarmRss.setDescription('RSS alarm state.')
alarmBer = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 6), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmBer.setStatus('current')
if mibBuilder.loadTexts: alarmBer.setDescription('BER alarm state.')
alarmPeerDisconnected = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 7), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmPeerDisconnected.setStatus('current')
if mibBuilder.loadTexts: alarmPeerDisconnected.setDescription('Peer disconnect alarm state.')
alarmEth1Down = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 8), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmEth1Down.setStatus('current')
if mibBuilder.loadTexts: alarmEth1Down.setDescription('Ethernet 1 Link Down alarm state.')
alarmEth2Down = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 9), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmEth2Down.setStatus('current')
if mibBuilder.loadTexts: alarmEth2Down.setDescription('Ethernet 2 Link Down alarm state.')
alarmNetBitrate = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 11), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmNetBitrate.setStatus('current')
if mibBuilder.loadTexts: alarmNetBitrate.setDescription('Air Speed below Limit alarm state.')
alarmWifiOn = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 12), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmWifiOn.setStatus('current')
if mibBuilder.loadTexts: alarmWifiOn.setDescription('WiFi Host Access Point on.')
alarmMse = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 1, 8, 13), AlarmState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarmMse.setStatus('current')
if mibBuilder.loadTexts: alarmMse.setDescription('MSE alarm state.')
ifRadio = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1))
ifEth = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2))
rxChannel = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 1), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxChannel.setStatus('current')
if mibBuilder.loadTexts: rxChannel.setDescription('Receiver channel ID.')
txChannel = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 2), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: txChannel.setStatus('current')
if mibBuilder.loadTexts: txChannel.setDescription('Transceiver channel ID.')
rxFreq = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 3), Gauge32()).setUnits('kHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: rxFreq.setStatus('current')
if mibBuilder.loadTexts: rxFreq.setDescription('Receiver frequency in kHz.')
txFreq = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 4), Gauge32()).setUnits('kHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: txFreq.setStatus('current')
if mibBuilder.loadTexts: txFreq.setDescription('Transceiver frequency in kHz.')
rxModulation = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 5), DisplayStringRaw()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxModulation.setStatus('current')
if mibBuilder.loadTexts: rxModulation.setDescription('Rx modulation text ID.')
txModulation = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 6), DisplayStringRaw()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txModulation.setStatus('current')
if mibBuilder.loadTexts: txModulation.setDescription('Tx modulation text ID.')
rxModulationIndex = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 7), ModulationList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rxModulationIndex.setStatus('current')
if mibBuilder.loadTexts: rxModulationIndex.setDescription('Rx modulation index.')
txModulationIndex = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 8), ModulationList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: txModulationIndex.setStatus('current')
if mibBuilder.loadTexts: txModulationIndex.setDescription('Tx modulation index.')
matching = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 11), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: matching.setStatus('current')
if mibBuilder.loadTexts: matching.setDescription('Channel matching.')
rfPowerConfigured = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 12), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: rfPowerConfigured.setStatus('current')
if mibBuilder.loadTexts: rfPowerConfigured.setDescription('Configured RF Power in dBm.')
netBitrate = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 13), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: netBitrate.setStatus('current')
if mibBuilder.loadTexts: netBitrate.setDescription('Current net bitrate in kbps.')
maxNetBitrate = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 14), Integer32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: maxNetBitrate.setStatus('current')
if mibBuilder.loadTexts: maxNetBitrate.setDescription('Maximum net bitrate in Mbps.')
txBandwidthKHz = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 15), Integer32()).setUnits('kHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: txBandwidthKHz.setStatus('current')
if mibBuilder.loadTexts: txBandwidthKHz.setDescription('Radio Tx channel bandwidth in kHz.')
channelArrangement = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("accp", 1), ("acap", 2), ("ccdp", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelArrangement.setStatus('current')
if mibBuilder.loadTexts: channelArrangement.setDescription('Channel arrangement.')
rfPowerCurrent = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 17), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: rfPowerCurrent.setStatus('current')
if mibBuilder.loadTexts: rfPowerCurrent.setDescription('Current RF Power in dBm.')
acm = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 18), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acm.setStatus('current')
if mibBuilder.loadTexts: acm.setDescription('ACM option.')
atpc = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 19), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atpc.setStatus('current')
if mibBuilder.loadTexts: atpc.setDescription('ATPC option.')
frequencyTable = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 20), DisplayStringRaw().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: frequencyTable.setStatus('current')
if mibBuilder.loadTexts: frequencyTable.setDescription('Current frequency table name.')
rxBandwidthKHz = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 2, 1, 21), Integer32()).setUnits('kHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: rxBandwidthKHz.setStatus('current')
if mibBuilder.loadTexts: rxBandwidthKHz.setDescription('Radio Rx channel bandwidth in kHz.')
ifEthTable = MibTable((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1), )
if mibBuilder.loadTexts: ifEthTable.setStatus('current')
if mibBuilder.loadTexts: ifEthTable.setDescription('List of Ethernet interfaces.')
ifEthEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1), ).setIndexNames((0, "RAY3-MIB", "speed"))
if mibBuilder.loadTexts: ifEthEntry.setStatus('current')
if mibBuilder.loadTexts: ifEthEntry.setDescription('Ethernet interface entry.')
speed = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1000000000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: speed.setStatus('current')
if mibBuilder.loadTexts: speed.setDescription('Ethernet speed.')
duplex = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("full", 1), ("half", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: duplex.setStatus('current')
if mibBuilder.loadTexts: duplex.setDescription('Ethernet duplex.')
mdix = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("na", 0), ("mdi", 1), ("mdi-x", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mdix.setStatus('current')
if mibBuilder.loadTexts: mdix.setDescription('Ethernet MDI-X / MDI.')
autonego = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 4), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: autonego.setStatus('current')
if mibBuilder.loadTexts: autonego.setDescription('Ethernet autonego.')
flowControl = MibTableColumn((1, 3, 6, 1, 4, 1, 33555, 4, 2, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("na", 0), ("off", 1), ("on", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: flowControl.setStatus('current')
if mibBuilder.loadTexts: flowControl.setDescription('Ethernet flow control.')
radio = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2))
ethernet = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 3, 3))
rss = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 1), Tenths().subtype(subtypeSpec=ValueRangeConstraint(-1000, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rss.setStatus('current')
if mibBuilder.loadTexts: rss.setDescription('Receiving RSS indicator in tenths of dBm.')
timeAllConnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 5), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeAllConnect.setStatus('current')
if mibBuilder.loadTexts: timeAllConnect.setDescription('Overall link uptime.')
timeAllDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeAllDisconnect.setStatus('current')
if mibBuilder.loadTexts: timeAllDisconnect.setDescription('Overall link downtime.')
timeMaxDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: timeMaxDisconnect.setStatus('current')
if mibBuilder.loadTexts: timeMaxDisconnect.setDescription('The longest drop (disconnecting).')
numDisconnect = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: numDisconnect.setStatus('current')
if mibBuilder.loadTexts: numDisconnect.setDescription('Number of drops (disconnecting).')
reliability = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 9), Thousandths().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readonly")
if mibBuilder.loadTexts: reliability.setStatus('current')
if mibBuilder.loadTexts: reliability.setDescription('Reliability in thousandths of %.')
linkUptime = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: linkUptime.setStatus('current')
if mibBuilder.loadTexts: linkUptime.setDescription('Current radio link uptime.')
ber = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ber.setStatus('current')
if mibBuilder.loadTexts: ber.setDescription('Bit Error Rate (BER) multiplied by 10^9.')
mse = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 2, 12), Tenths().subtype(subtypeSpec=ValueRangeConstraint(-500, 0))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mse.setStatus('current')
if mibBuilder.loadTexts: mse.setDescription('Receiving MSE indicator in thnths of dB.')
ethInThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 1), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: ethInThroughput.setStatus('current')
if mibBuilder.loadTexts: ethInThroughput.setDescription('Input Ethernet 1 data port throughput in kbps.')
ethOutThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 2), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: ethOutThroughput.setStatus('current')
if mibBuilder.loadTexts: ethOutThroughput.setDescription('Output Ethernet 1 data port throughput in kbps.')
eth2InThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 3), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: eth2InThroughput.setStatus('current')
if mibBuilder.loadTexts: eth2InThroughput.setDescription('Input Ethernet 2 data port throughput in kbps.')
eth2OutThroughput = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 3, 3, 4), Integer32()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: eth2OutThroughput.setStatus('current')
if mibBuilder.loadTexts: eth2OutThroughput.setDescription('Output Ethernet 2 data port throughput in kbps.')
egressQueue = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 4, 3))
speedGuard = MibScalar((1, 3, 6, 1, 4, 1, 33555, 4, 4, 3, 2), OptionSetting()).setMaxAccess("readonly")
if mibBuilder.loadTexts: speedGuard.setStatus('current')
if mibBuilder.loadTexts: speedGuard.setDescription('Speed guard feature on/off.')
ray3TrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0))
tr3TemperatureAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 1)).setObjects(("RAY3-MIB", "temperatureModem"), ("RAY3-MIB", "alarmTemperature"))
if mibBuilder.loadTexts: tr3TemperatureAlarm.setStatus('current')
if mibBuilder.loadTexts: tr3TemperatureAlarm.setDescription('Temperature exceeded the threshold.')
tr3VoltageLowAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 2)).setObjects(("RAY3-MIB", "voltageUnit"), ("RAY3-MIB", "alarmVoltageLow"))
if mibBuilder.loadTexts: tr3VoltageLowAlarm.setStatus('current')
if mibBuilder.loadTexts: tr3VoltageLowAlarm.setDescription('Supply voltage below minimal threshold.')
tr3VoltageHighAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 3)).setObjects(("RAY3-MIB", "voltageUnit"), ("RAY3-MIB", "alarmVoltageHigh"))
if mibBuilder.loadTexts: tr3VoltageHighAlarm.setStatus('current')
if mibBuilder.loadTexts: tr3VoltageHighAlarm.setDescription('Supply voltage above maximal threshold.')
tr3RssAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 4)).setObjects(("RAY3-MIB", "rss"), ("RAY3-MIB", "alarmRss"))
if mibBuilder.loadTexts: tr3RssAlarm.setStatus('current')
if mibBuilder.loadTexts: tr3RssAlarm.setDescription('RSS exceeded the threshold.')
tr3MseAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 5)).setObjects(("RAY3-MIB", "mse"), ("RAY3-MIB", "alarmMse"))
if mibBuilder.loadTexts: tr3MseAlarm.setStatus('current')
if mibBuilder.loadTexts: tr3MseAlarm.setDescription('MSE exceeded the threshold.')
tr3BerAlarm = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 6)).setObjects(("RAY3-MIB", "ber"), ("RAY3-MIB", "alarmBer"))
if mibBuilder.loadTexts: tr3BerAlarm.setStatus('current')
if mibBuilder.loadTexts: tr3BerAlarm.setDescription('BER exceeded the threshold.')
tr3AirDisconnect = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 7)).setObjects(("RAY3-MIB", "lineStatusII"), ("RAY3-MIB", "alarmPeerDisconnected"))
if mibBuilder.loadTexts: tr3AirDisconnect.setStatus('current')
if mibBuilder.loadTexts: tr3AirDisconnect.setDescription('Air line disconnected.')
tr3AirConnect = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 8)).setObjects(("RAY3-MIB", "lineStatusII"), ("RAY3-MIB", "alarmPeerDisconnected"))
if mibBuilder.loadTexts: tr3AirConnect.setStatus('current')
if mibBuilder.loadTexts: tr3AirConnect.setDescription('Air line connected after being disconnected.')
tr3Eth1LinkDown = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 9)).setObjects(("RAY3-MIB", "eth1Link"), ("RAY3-MIB", "alarmEth1Down"))
if mibBuilder.loadTexts: tr3Eth1LinkDown.setStatus('current')
if mibBuilder.loadTexts: tr3Eth1LinkDown.setDescription('Local station Ethernet 1 link Up/Down.')
tr3Eth21LinkDown = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 10)).setObjects(("RAY3-MIB", "eth2Link"), ("RAY3-MIB", "alarmEth2Down"))
if mibBuilder.loadTexts: tr3Eth21LinkDown.setStatus('current')
if mibBuilder.loadTexts: tr3Eth21LinkDown.setDescription('Local station Ethernet 2 link Up/Down.')
tr3NetBitrate = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 11)).setObjects(("RAY3-MIB", "netBitrate"), ("RAY3-MIB", "alarmNetBitrate"))
if mibBuilder.loadTexts: tr3NetBitrate.setStatus('current')
if mibBuilder.loadTexts: tr3NetBitrate.setDescription('Air speed below threshold.')
tr3WifiOn = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 12)).setObjects(("RAY3-MIB", "wifiHAP"), ("RAY3-MIB", "alarmWifiOn"))
if mibBuilder.loadTexts: tr3WifiOn.setStatus('current')
if mibBuilder.loadTexts: tr3WifiOn.setDescription('WiFi Host Access Point is on.')
tr3EventAirCapacity = NotificationType((1, 3, 6, 1, 4, 1, 33555, 4, 12, 0, 101)).setObjects(("RAY3-MIB", "netBitrate"))
if mibBuilder.loadTexts: tr3EventAirCapacity.setStatus('current')
if mibBuilder.loadTexts: tr3EventAirCapacity.setDescription('Air channel capacity changed.')
mibBuilder.exportSymbols("RAY3-MIB", acm=acm, rss=rss, timeMaxDisconnect=timeMaxDisconnect, tr3VoltageHighAlarm=tr3VoltageHighAlarm, speed=speed, flowControl=flowControl, DisplayStringRaw=DisplayStringRaw, voltageSource=voltageSource, swVerRadio=swVerRadio, txBandwidthKHz=txBandwidthKHz, access=access, temperatureRadio=temperatureRadio, txModulationIndex=txModulationIndex, tr3VoltageLowAlarm=tr3VoltageLowAlarm, ifEthEntry=ifEthEntry, tr3EventAirCapacity=tr3EventAirCapacity, managementVlan=managementVlan, AlarmState=AlarmState, autonego=autonego, ServiceState=ServiceState, alarmVoltageLow=alarmVoltageLow, telnetd=telnetd, alarmEth1Down=alarmEth1Down, tr3TemperatureAlarm=tr3TemperatureAlarm, Thousandths=Thousandths, unitType=unitType, alarmMse=alarmMse, tr3AirDisconnect=tr3AirDisconnect, alarmBer=alarmBer, system=system, lineStatusII=lineStatusII, frequencyTable=frequencyTable, deviceName=deviceName, alarmWifiOn=alarmWifiOn, ethernet=ethernet, ray3Traps=ray3Traps, txModulation=txModulation, mse=mse, product=product, useMemory=useMemory, rxModulation=rxModulation, reliability=reliability, securePeerMode=securePeerMode, status=status, tr3Eth1LinkDown=tr3Eth1LinkDown, alarmRss=alarmRss, swVer=swVer, alarmTemperature=alarmTemperature, info=info, eth1Link=eth1Link, sshd=sshd, station=station, ifRadio=ifRadio, interface=interface, chassis=chassis, timeAllDisconnect=timeAllDisconnect, speedGuard=speedGuard, alarmEth2Down=alarmEth2Down, tr3BerAlarm=tr3BerAlarm, useLogStorage=useLogStorage, alarm=alarm, httpd=httpd, txFreq=txFreq, voltageUnit=voltageUnit, OptionSetting=OptionSetting, channelArrangement=channelArrangement, useCpu=useCpu, matching=matching, rxBandwidthKHz=rxBandwidthKHz, switch=switch, alarmVoltageHigh=alarmVoltageHigh, Tenths=Tenths, ber=ber, atpc=atpc, alarmNetBitrate=alarmNetBitrate, netBitrate=netBitrate, statistic=statistic, maxNetBitrate=maxNetBitrate, tr3AirConnect=tr3AirConnect, egressQueue=egressQueue, serialNumber=serialNumber, ethOutThroughput=ethOutThroughput, radio=radio, systemStatus=systemStatus, rxChannel=rxChannel, tr3Eth21LinkDown=tr3Eth21LinkDown, tr3RssAlarm=tr3RssAlarm, PhysAddressRaw=PhysAddressRaw, rfPowerCurrent=rfPowerCurrent, txChannel=txChannel, numDisconnect=numDisconnect, rfPowerConfigured=rfPowerConfigured, linkUptime=linkUptime, alarmPeerDisconnected=alarmPeerDisconnected, rxFreq=rxFreq, eth2InThroughput=eth2InThroughput, eth2Link=eth2Link, mdix=mdix, ip=ip, ModulationList=ModulationList, ray3TrapsPrefix=ray3TrapsPrefix, ifEthTable=ifEthTable, duplex=duplex, ethInThroughput=ethInThroughput, tr3MseAlarm=tr3MseAlarm, timeAllConnect=timeAllConnect, ifEth=ifEth, mac=mac, productName=productName, Hundredths=Hundredths, racom=racom, ray3=ray3, wifiHAP=wifiHAP, tr3WifiOn=tr3WifiOn, temperatureModem=temperatureModem, PYSNMP_MODULE_ID=racom, rxModulationIndex=rxModulationIndex, tr3NetBitrate=tr3NetBitrate, managementVlanId=managementVlanId, eth2OutThroughput=eth2OutThroughput, peerNumber=peerNumber)
