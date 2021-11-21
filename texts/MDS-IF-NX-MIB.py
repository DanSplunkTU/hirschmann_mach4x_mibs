#
# PySNMP MIB module MDS-IF-NX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-IF-NX-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:38:22 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mdsInterfaces, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsInterfaces")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ObjectIdentity, NotificationType, Bits, Counter32, IpAddress, iso, MibIdentifier, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ModuleIdentity, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Bits", "Counter32", "IpAddress", "iso", "MibIdentifier", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ModuleIdentity", "Unsigned32", "Integer32")
MacAddress, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "DisplayString", "TextualConvention", "TruthValue")
mdsIfNxMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3))
mdsIfNxMIB.setRevisions(('2018-05-16 00:00', '2016-09-21 00:00', '2015-08-21 00:00', '2015-06-12 00:00', '2015-03-27 00:00', '2014-10-20 00:00', '2014-05-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsIfNxMIB.setRevisionsDescriptions(('Updated conformance statments based on smilint.', 'Added Error init status.', 'Added last packet parameters.', "Added 'disassociated' to LinkStatus.", 'Added test option for status', 'Removed hyphens from enumerations.', 'Initial version.',))
if mibBuilder.loadTexts: mdsIfNxMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsIfNxMIB.setOrganization('GE MDS LLC\n      http://www.gemds.com')
if mibBuilder.loadTexts: mdsIfNxMIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n       T 585-242-9600\n       F 585-242-9620\n\n       175 Science Parkway\n       Rochester, New York 14620\n       USA')
if mibBuilder.loadTexts: mdsIfNxMIB.setDescription('The MIB module to describe the 900 Mhz(NX) interface.')
mIfNxMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1))
mIfNxConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 1))
mIfNxStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2))
class UnsignedByte(TextualConvention, Unsigned32):
    description = 'xs:unsignedByte'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    description = 'xs:unsignedShort'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class LinkStatus(TextualConvention, Integer32):
    description = 'Link state'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("initializing", 0), ("scanning", 1), ("negotiating", 2), ("authenticating", 3), ("associated", 4), ("disassociated", 5))

class InitStatus(TextualConvention, Integer32):
    description = 'State of the NIC Initialization.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("off", 0), ("initializing", 1), ("discovering", 2), ("reprogramming", 3), ("configuring", 4), ("complete", 5), ("error", 6))

class DeviceModeType(TextualConvention, Integer32):
    description = 'Device Mode'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("remote", 0), ("accessPoint", 1), ("storeAndForward", 2), ("test", 3))

class ModemType(TextualConvention, Integer32):
    description = 'Modem type'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 10))
    namedValues = NamedValues(("e125kbps", 0), ("e250kbps", 1), ("e500kbps", 2), ("e1000kbps", 3), ("e1000Wkbps", 4), ("e1250kbps", 5), ("auto", 10))

class AlarmFlags(TextualConvention, Bits):
    description = 'Alarms'
    status = 'current'
    namedValues = NamedValues(("notCalibrated", 23), ("vswrFault", 16), ("temperature", 0))

class FirmwareRevision(TextualConvention, OctetString):
    description = 'Firmware revision'
    status = 'current'
    displayHint = '32a'

class InetIpAddress(TextualConvention, OctetString):
    description = 'IP Addres'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
mIfNxStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1), )
if mibBuilder.loadTexts: mIfNxStatusTable.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusTable.setDescription('This table contains status of NX interfaces. This table has \n         a sparse dependent relationship on the ifTable. For each entry in \n         this table, there exists an entry in the ifTable.')
mIfNxStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: mIfNxStatusEntry.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEntry.setDescription('Each entry contains status of a cellular interface.')
mIfNxLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 1), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxLinkStatus.setStatus('current')
if mibBuilder.loadTexts: mIfNxLinkStatus.setDescription('Link State.')
mIfNxInitStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 2), InitStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxInitStatus.setStatus('current')
if mibBuilder.loadTexts: mIfNxInitStatus.setDescription('State of the NIC Initialization.')
mIfNxCurrentModem = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 3), ModemType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxCurrentModem.setStatus('current')
if mibBuilder.loadTexts: mIfNxCurrentModem.setDescription('The current operating modem.')
mIfNxAlarms = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 4), AlarmFlags()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxAlarms.setStatus('current')
if mibBuilder.loadTexts: mIfNxAlarms.setDescription('The current NIC alarms.')
mIfNxSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxSerialNumber.setStatus('current')
if mibBuilder.loadTexts: mIfNxSerialNumber.setDescription('Serial Number.')
mIfNxFirmwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 6), FirmwareRevision()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxFirmwareRevision.setStatus('current')
if mibBuilder.loadTexts: mIfNxFirmwareRevision.setDescription('NIC Firmware Revision.')
mIfNxHardwareId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 7), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxHardwareId.setStatus('current')
if mibBuilder.loadTexts: mIfNxHardwareId.setDescription('The Hardware ID.')
mIfNxHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 8), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxHardwareRevision.setStatus('current')
if mibBuilder.loadTexts: mIfNxHardwareRevision.setDescription('The Hardware Revision.')
mIfNxTemperature = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxTemperature.setStatus('current')
if mibBuilder.loadTexts: mIfNxTemperature.setDescription('The transceiver temperature.')
mIfNxApInfoApAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 10), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxApInfoApAddress.setStatus('current')
if mibBuilder.loadTexts: mIfNxApInfoApAddress.setDescription('MAC address of access point this device is linked to.')
mIfNxApInfoIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 11), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxApInfoIpAddress.setStatus('current')
if mibBuilder.loadTexts: mIfNxApInfoIpAddress.setDescription('IP address of access point this device is linked to.')
mIfNxApInfoConnectedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxApInfoConnectedTime.setStatus('current')
if mibBuilder.loadTexts: mIfNxApInfoConnectedTime.setDescription('Time elapsed since link established.')
mIfNxApInfoAvgRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxApInfoAvgRssi.setStatus('current')
if mibBuilder.loadTexts: mIfNxApInfoAvgRssi.setDescription('Average received signal strength index.')
mIfNxApInfoAvgLqi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxApInfoAvgLqi.setStatus('current')
if mibBuilder.loadTexts: mIfNxApInfoAvgLqi.setDescription('Average link quality index.')
mIfNxMacStatsTxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxSuccess.setStatus('current')
if mibBuilder.loadTexts: mIfNxMacStatsTxSuccess.setDescription('Successful transmissions.')
mIfNxMacStatsTxFail = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxFail.setStatus('current')
if mibBuilder.loadTexts: mIfNxMacStatsTxFail.setDescription('Failed transmissions, TTL expired or retry count exceeded.')
mIfNxMacStatsTxQueueFull = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxQueueFull.setStatus('current')
if mibBuilder.loadTexts: mIfNxMacStatsTxQueueFull.setDescription('Failed transmissions, MAC queue full.')
mIfNxMacStatsTxNoSync = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 18), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxNoSync.setStatus('current')
if mibBuilder.loadTexts: mIfNxMacStatsTxNoSync.setDescription('Packets dropped because the MAC is not synchronized.')
mIfNxMacStatsTxNoAssoc = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 19), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxNoAssoc.setStatus('current')
if mibBuilder.loadTexts: mIfNxMacStatsTxNoAssoc.setDescription('Packets dropped because the MAC is not associated.')
mIfNxMacStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 20), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfNxMacStatsTxError.setDescription('Packets dropped for other reasons. Currently unused.')
mIfNxMacStatsTxRetry = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 21), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsTxRetry.setStatus('current')
if mibBuilder.loadTexts: mIfNxMacStatsTxRetry.setDescription('Re-transmission count due to to previously unsuccessful transmission.')
mIfNxMacStatsRxSuccess = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsRxSuccess.setStatus('current')
if mibBuilder.loadTexts: mIfNxMacStatsRxSuccess.setDescription('Valid packet received.')
mIfNxMacStatsSyncCheckError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 23), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsSyncCheckError.setStatus('current')
if mibBuilder.loadTexts: mIfNxMacStatsSyncCheckError.setDescription('Lost synchronization.')
mIfNxMacStatsSyncChange = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxMacStatsSyncChange.setStatus('current')
if mibBuilder.loadTexts: mIfNxMacStatsSyncChange.setDescription('Sychronization changed or forced drop.')
mIfNxCurrentDeviceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 25), DeviceModeType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxCurrentDeviceMode.setStatus('current')
if mibBuilder.loadTexts: mIfNxCurrentDeviceMode.setDescription('The current device mode.')
mIfNxLastRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 26), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxLastRssi.setStatus('current')
if mibBuilder.loadTexts: mIfNxLastRssi.setDescription('Average received signal strength index.')
mIfNxLastLqi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 27), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxLastLqi.setStatus('current')
if mibBuilder.loadTexts: mIfNxLastLqi.setDescription('Average link quality index.')
mIfNxLastChan = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 28), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxLastChan.setStatus('current')
if mibBuilder.loadTexts: mIfNxLastChan.setDescription('Average link quality index.')
mIfNxActiveNic = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 1, 1, 29), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxActiveNic.setStatus('current')
if mibBuilder.loadTexts: mIfNxActiveNic.setDescription('If the nic is active.')
mIfNxStatusConnRemTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2), )
if mibBuilder.loadTexts: mIfNxStatusConnRemTable.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemTable.setDescription('The list of connected remotes.')
mIfNxStatusConnRemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-NX-MIB", "mIfNxStatusConnRemAddress"))
if mibBuilder.loadTexts: mIfNxStatusConnRemEntry.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemEntry.setDescription('The connected remote status entry.')
mIfNxStatusConnRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemAddress.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemAddress.setDescription('Address of connected remote.')
mIfNxStatusConnRemIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemIpAddress.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemIpAddress.setDescription('Ip address of connected remote.')
mIfNxStatusConnRemTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemTimeToLive.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemTimeToLive.setDescription('Time left until this entry is aged out.')
mIfNxStatusConnRemLinkStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 4), LinkStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemLinkStatus.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemLinkStatus.setDescription('The status of the connection to a remote device.')
mIfNxStatusConnRemNicId = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 5), UnsignedShort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemNicId.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemNicId.setDescription('The RF connection identifier for the connected remote device.')
mIfNxStatusConnRemAvgRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemAvgRssi.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemAvgRssi.setDescription('Average received signal strength index.')
mIfNxStatusConnRemAvgLqi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemAvgLqi.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemAvgLqi.setDescription('Average link quality index.')
mIfNxStatusConnRemStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxPackets.setDescription('tx packets')
mIfNxStatusConnRemStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxBytes.setDescription('tx bytes')
mIfNxStatusConnRemStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxPackets.setDescription('rx packets')
mIfNxStatusConnRemStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxBytes.setDescription('rx bytes')
mIfNxStatusConnRemStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxError.setDescription('tx error')
mIfNxStatusConnRemStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxError.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxError.setDescription('rx error')
mIfNxStatusConnRemStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTxDrop.setDescription('tx drop')
mIfNxStatusConnRemStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsRxDrop.setDescription('rx drop')
mIfNxStatusConnRemAvgSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemAvgSnr.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemAvgSnr.setDescription('Average signal to noise ratio.')
mIfNxStatusConnRemStatsGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 17), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsGateway.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsGateway.setDescription('The mac address of the next hop')
mIfNxStatusConnRemStatsAllIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 18), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsAllIp.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsAllIp.setDescription('String version of all IP addresses')
mIfNxStatusConnRemStatsName = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 19), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsName.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsName.setDescription('System name')
mIfNxStatusConnRemStatsAlarmed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 20), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsAlarmed.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsAlarmed.setDescription('Is alarmed')
mIfNxStatusConnRemStatsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 21), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsVersion.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsVersion.setDescription('Host firmware version')
mIfNxStatusConnRemStatsTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTemp.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsTemp.setDescription('System temprature in celsius')
mIfNxStatusConnRemStatsDwnRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 23), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsDwnRssi.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsDwnRssi.setDescription('Downstream RSSI')
mIfNxStatusConnRemStatsDwnLqi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 24), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsDwnLqi.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsDwnLqi.setDescription('Downstream LQI')
mIfNxStatusConnRemStatsDwnSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 2, 1, 25), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsDwnSnr.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemStatsDwnSnr.setDescription('Downstream SNR')
mIfNxStatusEndpointTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3), )
if mibBuilder.loadTexts: mIfNxStatusEndpointTable.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointTable.setDescription('The list of endpoints.')
mIfNxStatusEndpointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-NX-MIB", "mIfNxStatusEndpointAddress"))
if mibBuilder.loadTexts: mIfNxStatusEndpointEntry.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointEntry.setDescription('The endpoint status entry.')
mIfNxStatusEndpointAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointAddress.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointAddress.setDescription('Address of endpoint.')
mIfNxStatusEndpointIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 2), InetIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointIpAddress.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointIpAddress.setDescription('Ip address of endpoint.')
mIfNxStatusEndpointTimeToLive = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointTimeToLive.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointTimeToLive.setDescription('Time left until this entry is aged out.')
mIfNxStatusEndpointRemAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointRemAddress.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointRemAddress.setDescription('The MAC address of the remote device servicing this endpoint.')
mIfNxStatusEndpointStatsTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxPackets.setDescription('tx packets')
mIfNxStatusEndpointStatsTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxBytes.setDescription('tx bytes')
mIfNxStatusEndpointStatsRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxPackets.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxPackets.setDescription('rx packets')
mIfNxStatusEndpointStatsRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxBytes.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxBytes.setDescription('rx bytes')
mIfNxStatusEndpointStatsTxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxError.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxError.setDescription('tx error')
mIfNxStatusEndpointStatsRxError = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxError.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxError.setDescription('rx error')
mIfNxStatusEndpointStatsTxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsTxDrop.setDescription('tx drop')
mIfNxStatusEndpointStatsRxDrop = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxDrop.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointStatsRxDrop.setDescription('rx drop')
mIfNxStatusActChanTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4), )
if mibBuilder.loadTexts: mIfNxStatusActChanTable.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusActChanTable.setDescription('The list of channels.')
mIfNxStatusActChanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "MDS-IF-NX-MIB", "mIfNxStatusActChanChannel"))
if mibBuilder.loadTexts: mIfNxStatusActChanEntry.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusActChanEntry.setDescription('The endpoint status entry.')
mIfNxStatusActChanChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 1), UnsignedByte()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusActChanChannel.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusActChanChannel.setDescription('Channel.')
mIfNxStatusActChanFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusActChanFrequency.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusActChanFrequency.setDescription('Frequency.')
mIfNxStatusActChanAvgRssi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusActChanAvgRssi.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusActChanAvgRssi.setDescription('Average received signal strength index.')
mIfNxStatusActChanAvgLqi = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 1, 2, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mIfNxStatusActChanAvgLqi.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusActChanAvgLqi.setDescription('Average link quality index.')
mdsIfNxMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3))
mdsIfNxMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 1))
mdsIfNxMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2))
mIfNxCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 1, 1)).setObjects(("MDS-IF-NX-MIB", "mIfNxStatusGroup"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemGroup"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointGroup"), ("MDS-IF-NX-MIB", "mIfNxStatusActChanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfNxCompliance = mIfNxCompliance.setStatus('current')
if mibBuilder.loadTexts: mIfNxCompliance.setDescription('The compliance statement for SNMP entities that \n            implement the MDS-IF-NX-MIB.')
mIfNxStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 1)).setObjects(("MDS-IF-NX-MIB", "mIfNxLinkStatus"), ("MDS-IF-NX-MIB", "mIfNxInitStatus"), ("MDS-IF-NX-MIB", "mIfNxCurrentModem"), ("MDS-IF-NX-MIB", "mIfNxAlarms"), ("MDS-IF-NX-MIB", "mIfNxSerialNumber"), ("MDS-IF-NX-MIB", "mIfNxFirmwareRevision"), ("MDS-IF-NX-MIB", "mIfNxHardwareId"), ("MDS-IF-NX-MIB", "mIfNxHardwareRevision"), ("MDS-IF-NX-MIB", "mIfNxTemperature"), ("MDS-IF-NX-MIB", "mIfNxApInfoApAddress"), ("MDS-IF-NX-MIB", "mIfNxApInfoIpAddress"), ("MDS-IF-NX-MIB", "mIfNxApInfoConnectedTime"), ("MDS-IF-NX-MIB", "mIfNxApInfoAvgRssi"), ("MDS-IF-NX-MIB", "mIfNxApInfoAvgLqi"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxSuccess"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxFail"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxQueueFull"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxNoSync"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxNoAssoc"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxError"), ("MDS-IF-NX-MIB", "mIfNxMacStatsTxRetry"), ("MDS-IF-NX-MIB", "mIfNxMacStatsRxSuccess"), ("MDS-IF-NX-MIB", "mIfNxMacStatsSyncCheckError"), ("MDS-IF-NX-MIB", "mIfNxMacStatsSyncChange"), ("MDS-IF-NX-MIB", "mIfNxCurrentDeviceMode"), ("MDS-IF-NX-MIB", "mIfNxLastRssi"), ("MDS-IF-NX-MIB", "mIfNxLastLqi"), ("MDS-IF-NX-MIB", "mIfNxLastChan"), ("MDS-IF-NX-MIB", "mIfNxActiveNic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfNxStatusGroup = mIfNxStatusGroup.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusGroup.setDescription('A collection of objects providing information about\n        common NX interface status.')
mIfNxStatusConnRemGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 2)).setObjects(("MDS-IF-NX-MIB", "mIfNxStatusConnRemAddress"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemIpAddress"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemTimeToLive"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemLinkStatus"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemNicId"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemAvgRssi"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemAvgLqi"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxPackets"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxBytes"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxPackets"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxBytes"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxError"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxError"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTxDrop"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsRxDrop"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemAvgSnr"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsGateway"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsAllIp"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsName"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsAlarmed"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsVersion"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsTemp"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsDwnRssi"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsDwnLqi"), ("MDS-IF-NX-MIB", "mIfNxStatusConnRemStatsDwnSnr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfNxStatusConnRemGroup = mIfNxStatusConnRemGroup.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusConnRemGroup.setDescription('A collection of objects providing information about\n        connected remotes status.')
mIfNxStatusEndpointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 3)).setObjects(("MDS-IF-NX-MIB", "mIfNxStatusEndpointAddress"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointIpAddress"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointTimeToLive"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointRemAddress"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxPackets"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxBytes"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxPackets"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxBytes"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxError"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxError"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsTxDrop"), ("MDS-IF-NX-MIB", "mIfNxStatusEndpointStatsRxDrop"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfNxStatusEndpointGroup = mIfNxStatusEndpointGroup.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusEndpointGroup.setDescription('A collection of objects providing information about\n        endpoints status.')
mIfNxStatusActChanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 2, 3, 3, 2, 4)).setObjects(("MDS-IF-NX-MIB", "mIfNxStatusActChanChannel"), ("MDS-IF-NX-MIB", "mIfNxStatusActChanFrequency"), ("MDS-IF-NX-MIB", "mIfNxStatusActChanAvgRssi"), ("MDS-IF-NX-MIB", "mIfNxStatusActChanAvgLqi"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mIfNxStatusActChanGroup = mIfNxStatusActChanGroup.setStatus('current')
if mibBuilder.loadTexts: mIfNxStatusActChanGroup.setDescription('A collection of objects providing information about\n        active channel status.')
mibBuilder.exportSymbols("MDS-IF-NX-MIB", mIfNxCurrentDeviceMode=mIfNxCurrentDeviceMode, mIfNxMacStatsTxFail=mIfNxMacStatsTxFail, mIfNxMacStatsTxError=mIfNxMacStatsTxError, mIfNxStatusConnRemStatsVersion=mIfNxStatusConnRemStatsVersion, mIfNxLastRssi=mIfNxLastRssi, mIfNxStatusConnRemLinkStatus=mIfNxStatusConnRemLinkStatus, mIfNxMacStatsTxRetry=mIfNxMacStatsTxRetry, mIfNxStatusConnRemStatsTxPackets=mIfNxStatusConnRemStatsTxPackets, mIfNxLastLqi=mIfNxLastLqi, mIfNxStatusEndpointEntry=mIfNxStatusEndpointEntry, mIfNxStatusEndpointStatsRxBytes=mIfNxStatusEndpointStatsRxBytes, InetIpAddress=InetIpAddress, mIfNxApInfoAvgLqi=mIfNxApInfoAvgLqi, mIfNxMacStatsTxQueueFull=mIfNxMacStatsTxQueueFull, mIfNxFirmwareRevision=mIfNxFirmwareRevision, mIfNxStatusConnRemAvgLqi=mIfNxStatusConnRemAvgLqi, mIfNxStatusTable=mIfNxStatusTable, mIfNxMacStatsTxNoAssoc=mIfNxMacStatsTxNoAssoc, mIfNxStatusConnRemStatsRxError=mIfNxStatusConnRemStatsRxError, mIfNxStatusActChanAvgRssi=mIfNxStatusActChanAvgRssi, FirmwareRevision=FirmwareRevision, mIfNxStatusConnRemStatsName=mIfNxStatusConnRemStatsName, mdsIfNxMIBCompliances=mdsIfNxMIBCompliances, mIfNxApInfoIpAddress=mIfNxApInfoIpAddress, mIfNxMacStatsSyncChange=mIfNxMacStatsSyncChange, mIfNxStatusEndpointStatsRxError=mIfNxStatusEndpointStatsRxError, mIfNxStatusConnRemStatsRxBytes=mIfNxStatusConnRemStatsRxBytes, mIfNxLastChan=mIfNxLastChan, mIfNxStatusEndpointRemAddress=mIfNxStatusEndpointRemAddress, mIfNxAlarms=mIfNxAlarms, mIfNxStatusEndpointStatsRxPackets=mIfNxStatusEndpointStatsRxPackets, mIfNxStatusEndpointStatsRxDrop=mIfNxStatusEndpointStatsRxDrop, mdsIfNxMIB=mdsIfNxMIB, mIfNxStatusGroup=mIfNxStatusGroup, mIfNxStatusConnRemStatsAlarmed=mIfNxStatusConnRemStatsAlarmed, mIfNxCompliance=mIfNxCompliance, mIfNxStatusEndpointStatsTxPackets=mIfNxStatusEndpointStatsTxPackets, mIfNxActiveNic=mIfNxActiveNic, mIfNxStatusConnRemIpAddress=mIfNxStatusConnRemIpAddress, mIfNxInitStatus=mIfNxInitStatus, mIfNxStatusConnRemStatsAllIp=mIfNxStatusConnRemStatsAllIp, mIfNxStatusConnRemStatsDwnRssi=mIfNxStatusConnRemStatsDwnRssi, mIfNxHardwareId=mIfNxHardwareId, mIfNxStatusActChanAvgLqi=mIfNxStatusActChanAvgLqi, DeviceModeType=DeviceModeType, mIfNxMacStatsRxSuccess=mIfNxMacStatsRxSuccess, mIfNxStatusConnRemGroup=mIfNxStatusConnRemGroup, mIfNxStatusEndpointAddress=mIfNxStatusEndpointAddress, mIfNxStatusEntry=mIfNxStatusEntry, mdsIfNxMIBGroups=mdsIfNxMIBGroups, mIfNxStatusConnRemTimeToLive=mIfNxStatusConnRemTimeToLive, InitStatus=InitStatus, mIfNxStatusEndpointIpAddress=mIfNxStatusEndpointIpAddress, mIfNxHardwareRevision=mIfNxHardwareRevision, mIfNxStatusConnRemEntry=mIfNxStatusConnRemEntry, UnsignedByte=UnsignedByte, mIfNxStatusConnRemAvgSnr=mIfNxStatusConnRemAvgSnr, mIfNxStatusConnRemNicId=mIfNxStatusConnRemNicId, mIfNxTemperature=mIfNxTemperature, mIfNxStatusEndpointTable=mIfNxStatusEndpointTable, mIfNxStatusActChanGroup=mIfNxStatusActChanGroup, mIfNxStatusConnRemStatsDwnSnr=mIfNxStatusConnRemStatsDwnSnr, mIfNxCurrentModem=mIfNxCurrentModem, UnsignedShort=UnsignedShort, mIfNxStatusConnRemStatsTemp=mIfNxStatusConnRemStatsTemp, mIfNxStatusConnRemStatsDwnLqi=mIfNxStatusConnRemStatsDwnLqi, mdsIfNxMIBConformance=mdsIfNxMIBConformance, mIfNxStatusActChanFrequency=mIfNxStatusActChanFrequency, mIfNxApInfoAvgRssi=mIfNxApInfoAvgRssi, PYSNMP_MODULE_ID=mdsIfNxMIB, mIfNxConfig=mIfNxConfig, mIfNxStatusConnRemStatsTxError=mIfNxStatusConnRemStatsTxError, mIfNxStatusConnRemStatsTxBytes=mIfNxStatusConnRemStatsTxBytes, mIfNxSerialNumber=mIfNxSerialNumber, mIfNxLinkStatus=mIfNxLinkStatus, LinkStatus=LinkStatus, mIfNxApInfoConnectedTime=mIfNxApInfoConnectedTime, mIfNxStatusConnRemStatsTxDrop=mIfNxStatusConnRemStatsTxDrop, mIfNxStatus=mIfNxStatus, mIfNxStatusEndpointTimeToLive=mIfNxStatusEndpointTimeToLive, mIfNxStatusConnRemTable=mIfNxStatusConnRemTable, mIfNxStatusEndpointStatsTxBytes=mIfNxStatusEndpointStatsTxBytes, mIfNxMacStatsTxSuccess=mIfNxMacStatsTxSuccess, mIfNxStatusActChanEntry=mIfNxStatusActChanEntry, mIfNxStatusEndpointStatsTxError=mIfNxStatusEndpointStatsTxError, mIfNxApInfoApAddress=mIfNxApInfoApAddress, mIfNxStatusConnRemStatsRxPackets=mIfNxStatusConnRemStatsRxPackets, mIfNxStatusConnRemStatsRxDrop=mIfNxStatusConnRemStatsRxDrop, AlarmFlags=AlarmFlags, mIfNxMacStatsSyncCheckError=mIfNxMacStatsSyncCheckError, ModemType=ModemType, mIfNxMacStatsTxNoSync=mIfNxMacStatsTxNoSync, mIfNxStatusEndpointStatsTxDrop=mIfNxStatusEndpointStatsTxDrop, mIfNxStatusEndpointGroup=mIfNxStatusEndpointGroup, mIfNxMIBObjects=mIfNxMIBObjects, mIfNxStatusConnRemAvgRssi=mIfNxStatusConnRemAvgRssi, mIfNxStatusConnRemAddress=mIfNxStatusConnRemAddress, mIfNxStatusActChanTable=mIfNxStatusActChanTable, mIfNxStatusActChanChannel=mIfNxStatusActChanChannel, mIfNxStatusConnRemStatsGateway=mIfNxStatusConnRemStatsGateway)
