#
# PySNMP MIB module MIMOSA-NETWORKS-BFIVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-NETWORKS-BFIVE-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:16:21 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
mimosaConformanceGroup, mimosaWireless = mibBuilder.importSymbols("MIMOSA-NETWORKS-BASE-MIB", "mimosaConformanceGroup", "mimosaWireless")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, IpAddress, Unsigned32, Gauge32, MibIdentifier, NotificationType, Integer32, Bits, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "IpAddress", "Unsigned32", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "Bits", "Counter32", "ObjectIdentity")
PhysAddress, TruthValue, TextualConvention, DisplayString, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "TruthValue", "TextualConvention", "DisplayString", "MacAddress", "RowStatus")
mimosaB5Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 43356, 2, 4, 1))
mimosaB5Module.setRevisions(('2017-04-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mimosaB5Module.setRevisionsDescriptions(('Compatible with Firmware 1.4.5',))
if mibBuilder.loadTexts: mimosaB5Module.setLastUpdated('201506030000Z')
if mibBuilder.loadTexts: mimosaB5Module.setOrganization('Mimosa Networks\n    \t\t\t  www.mimosa.co')
if mibBuilder.loadTexts: mimosaB5Module.setContactInfo('postal:\n    \tMimosa Networks, Inc.\n\t\t469 El Camino Real Ste 100\n\t\tSanta Clara, CA 95050\n        email: support@mimosa.co')
if mibBuilder.loadTexts: mimosaB5Module.setDescription('Mimosa device MIB definitions')
mimosaGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1))
mimosaLocInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2))
mimosaWanInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3))
mimosaTdmaInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4))
mimosaMgmtInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5))
mimosaRfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6))
mimosaPerfInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7))
mimosaServices = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8))
class DecimalOne(TextualConvention, Integer32):
    description = 'Fixed point, one decimal'
    status = 'current'
    displayHint = 'd-1'

class DecimalTwo(TextualConvention, Integer32):
    description = 'Fixed point, two decimals'
    status = 'current'
    displayHint = 'd-2'

class DecimalFive(TextualConvention, Integer32):
    description = 'Fixed point, five decimals'
    status = 'current'
    displayHint = 'd-5'

mimosaDeviceName = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaDeviceName.setStatus('current')
if mibBuilder.loadTexts: mimosaDeviceName.setDescription('The name of the local Mimosa device. This unique identifier could\n         be the same as the sysName object.')
mimosaSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaSerialNumber.setStatus('current')
if mibBuilder.loadTexts: mimosaSerialNumber.setDescription('The unique serial number of the Mimosa device.')
mimosaFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: mimosaFirmwareVersion.setDescription('The version of the currently installed and/or running firmware\n         on the Mimosa device.')
mimosaFirmwareBuildDate = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaFirmwareBuildDate.setStatus('current')
if mibBuilder.loadTexts: mimosaFirmwareBuildDate.setDescription('The creation date of the currently installed and/or running\n         firmware on the Mimosa device.')
mimosaLastRebootTime = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLastRebootTime.setStatus('current')
if mibBuilder.loadTexts: mimosaLastRebootTime.setDescription('The last time the Mimosa device rebooted.')
mimosaUnlockCode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaUnlockCode.setStatus('current')
if mibBuilder.loadTexts: mimosaUnlockCode.setDescription('The code used to unlock the Mimosa device.')
mimosaLEDBrightness = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("auto", 1), ("low", 2), ("medium", 3), ("high", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLEDBrightness.setStatus('current')
if mibBuilder.loadTexts: mimosaLEDBrightness.setDescription('Indicates the intensity of the status indicator lights on the\n         device exterior. The Auto option adjusts the amount of light\n         based upon ambient conditions. Manual options include Low,\n         Medium, and High.')
mimosaInternalTemp = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 8), DecimalOne()).setUnits('C').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaInternalTemp.setStatus('current')
if mibBuilder.loadTexts: mimosaInternalTemp.setDescription('The internal temperature of the Mimosa device.')
mimosaRegulatoryDomain = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRegulatoryDomain.setStatus('current')
if mibBuilder.loadTexts: mimosaRegulatoryDomain.setDescription('The country in which the Mimosa device has been configured to run.')
mimosaLongitude = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 1), DecimalFive()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLongitude.setStatus('current')
if mibBuilder.loadTexts: mimosaLongitude.setDescription('The Longitude of the Mimosa device location, in 5 decimal points.')
mimosaLatitude = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 2), DecimalFive()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLatitude.setStatus('current')
if mibBuilder.loadTexts: mimosaLatitude.setDescription('The Latitude of the Mimosa device location, in 5 decimal points.')
mimosaAltitude = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 3), Integer32()).setUnits('meters').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaAltitude.setStatus('current')
if mibBuilder.loadTexts: mimosaAltitude.setDescription('The Altitude of the Mimosa device location in meters.')
mimosaSatelliteSNR = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 4), DecimalOne()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaSatelliteSNR.setStatus('current')
if mibBuilder.loadTexts: mimosaSatelliteSNR.setDescription('The average Signal to Noise Ratio (SNR) amongst all of the satellites\n         detected by the Mimosa device. Display is in 1 decimal point.')
mimosaSatelliteStrength = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("good", 1), ("bad", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaSatelliteStrength.setStatus('current')
if mibBuilder.loadTexts: mimosaSatelliteStrength.setDescription('Strength of the satellites based on the number of satellites available.\n         It is considered good if more than 2 satellites are available.')
mimosaGPSSatellites = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaGPSSatellites.setStatus('current')
if mibBuilder.loadTexts: mimosaGPSSatellites.setDescription('Total number of GPS satellites detected.')
mimosaGlonassSatellites = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaGlonassSatellites.setStatus('current')
if mibBuilder.loadTexts: mimosaGlonassSatellites.setDescription('Total number of GLONASS satellites detected.')
mimosaClockAccuracy = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 2, 8), DecimalTwo()).setUnits('PPB').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaClockAccuracy.setStatus('current')
if mibBuilder.loadTexts: mimosaClockAccuracy.setDescription('Timing signal accuracy measured in parts per billion (PPB) by the\n         Mimosa device. Display is in 2 decimal points.')
mimosaWirelessMode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("accessPoint", 1), ("station", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWirelessMode.setStatus('current')
if mibBuilder.loadTexts: mimosaWirelessMode.setDescription('Describes wherger the Mimosa device acts as an access point or station.')
mimosaWirelessProtocol = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tdma", 1), ("csma", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWirelessProtocol.setStatus('current')
if mibBuilder.loadTexts: mimosaWirelessProtocol.setDescription('Describes the wireless protocol configured on the Mimosa device. \n\t     Both TDMA and CSMA are supported. TDMA is a deterministic protocol\n         where each device is assigned a time slot during which it is allowed\n         to transmit. This allows for collocated radios to utilize the same\n         channel and avoid Tx/Rx collisions and interference.')
mimosaTDMAMode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("a", 1), ("b", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTDMAMode.setStatus('current')
if mibBuilder.loadTexts: mimosaTDMAMode.setDescription('Specifies the TDMA Gender of the radio (A or B).')
mimosaTDMAWindow = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 4), Integer32()).setUnits('ms').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTDMAWindow.setStatus('current')
if mibBuilder.loadTexts: mimosaTDMAWindow.setDescription('Specifies the length of the transmit time slot in milliseconds.')
mimosaTrafficSplit = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 4, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("symmetric", 1), ("asymmetric", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTrafficSplit.setStatus('current')
if mibBuilder.loadTexts: mimosaTrafficSplit.setDescription('The radio can be configured to allocate bandwidth symmetrically (50/50)\n         or asymmetrically (75/25 or 25/75) in environments where traffic\n         direction is expected to be heavier in one direction than the other.\n         With an asymmetrical split, the local radio is represented first in the\n         slash notation, (local/remote). For example, in the (75/25) split, the\n         local radio gets 75, while the remote radio gets 25. If Auto is selected\n         the radio will automatically determine, based upon traffic flow, which\n         ratio will be used. The radio will continue to evaluate the flow and\n         adjust accordingly.')
mimosaChainTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1), )
if mibBuilder.loadTexts: mimosaChainTable.setStatus('current')
if mibBuilder.loadTexts: mimosaChainTable.setDescription('A list of RF chain entries, which is part of MIMO tables. MIMO stands\n         for Multiple In Multiple Out.')
mimosaChainEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-BFIVE-MIB", "mimosaChain"))
if mibBuilder.loadTexts: mimosaChainEntry.setStatus('current')
if mibBuilder.loadTexts: mimosaChainEntry.setDescription('An entry containing chain information applicable to a particular\n         RF chain.')
mimosaChain = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: mimosaChain.setStatus('current')
if mibBuilder.loadTexts: mimosaChain.setDescription('An index which is used to access a particular entry in the chain table.')
mimosaTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 2), DecimalOne()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTxPower.setStatus('current')
if mibBuilder.loadTexts: mimosaTxPower.setDescription('Specifies the transmit power of the given RF chain. A value of -8 means\n         this particular TxChain is not a valid entry.')
mimosaRxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 3), DecimalOne()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxPower.setStatus('current')
if mibBuilder.loadTexts: mimosaRxPower.setDescription('Specifies the receive power of the given RF chain. A value of -100\n         means this particular RxChain is not a valid entry (SNR must be -100).')
mimosaRxNoise = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 4), DecimalOne()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxNoise.setStatus('current')
if mibBuilder.loadTexts: mimosaRxNoise.setDescription('Specifies the received noise level for the given RF chain.')
mimosaSNR = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 5), DecimalOne()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaSNR.setStatus('current')
if mibBuilder.loadTexts: mimosaSNR.setDescription('Indicates the Signal to Noise Ratio (SNR) for the given RF chain.\n         A value of -100 means this particular RxChain is not a valid entry.')
mimosaCenterFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 6), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaCenterFreq.setStatus('current')
if mibBuilder.loadTexts: mimosaCenterFreq.setDescription('The center frequency for the given RF chain. A value of 0 means this\n         particular Chain is not a valid entry.')
mimosaPolarization = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("horizontal", 1), ("vertical", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPolarization.setStatus('current')
if mibBuilder.loadTexts: mimosaPolarization.setDescription('The ploarization of the given RF chain. It could be horizontal or\n         vertical.')
mimosaStreamTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2), )
if mibBuilder.loadTexts: mimosaStreamTable.setStatus('current')
if mibBuilder.loadTexts: mimosaStreamTable.setDescription('A list of data stream entries, which are part of MIMO tables. MIMO\n         stands for Multiple In Multiple Out.')
mimosaStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-BFIVE-MIB", "mimosaStream"))
if mibBuilder.loadTexts: mimosaStreamEntry.setStatus('current')
if mibBuilder.loadTexts: mimosaStreamEntry.setDescription('The entry containing information applicable to a particular stream.')
mimosaStream = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: mimosaStream.setStatus('current')
if mibBuilder.loadTexts: mimosaStream.setDescription('The index used to access a particular entry in the stream table.')
mimosaTxPhy = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 2), Integer32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTxPhy.setStatus('current')
if mibBuilder.loadTexts: mimosaTxPhy.setDescription('Specifies the transmit rate of the given data stream.')
mimosaTxMCS = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTxMCS.setStatus('current')
if mibBuilder.loadTexts: mimosaTxMCS.setDescription('Specifies the transmit MCS of the given data stream. A value of\n         -1 means this particular TxStream is not a valid entry.')
mimosaTxWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 4), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTxWidth.setStatus('current')
if mibBuilder.loadTexts: mimosaTxWidth.setDescription('Specifies the channel width based on MCS. A value of \n\t -1 means this particular TxWidth is not a valid entry')
mimosaRxPhy = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 5), Integer32()).setUnits('Mbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxPhy.setStatus('current')
if mibBuilder.loadTexts: mimosaRxPhy.setDescription('Specifies the receive rate of the given data stream.')
mimosaRxMCS = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxMCS.setStatus('current')
if mibBuilder.loadTexts: mimosaRxMCS.setDescription('Specifies the receive MCS of the given data stream. A value of\n         -1 means this particular RxStream is not a valid entry.')
mimosaRxWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 7), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxWidth.setStatus('current')
if mibBuilder.loadTexts: mimosaRxWidth.setDescription('Specifies the receive Rx Width of the given data stream. A value of\n         -1 means this particular RxWidth is not a valid entry.')
mimosaRxEVM = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 2, 1, 8), DecimalOne()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRxEVM.setStatus('current')
if mibBuilder.loadTexts: mimosaRxEVM.setDescription('Specifies the receive Error Vector Magnitude (EVM) of the given data\n         stream.')
mimosaChannelTable = MibTable((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3), )
if mibBuilder.loadTexts: mimosaChannelTable.setStatus('current')
if mibBuilder.loadTexts: mimosaChannelTable.setDescription('A list of RF channel entries on the Mimosa device.')
mimosaChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1), ).setIndexNames((0, "MIMOSA-NETWORKS-BFIVE-MIB", "mimosaChannel"))
if mibBuilder.loadTexts: mimosaChannelEntry.setStatus('current')
if mibBuilder.loadTexts: mimosaChannelEntry.setDescription('The entry containing management information applicable to a particular\n         channel.')
mimosaChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: mimosaChannel.setStatus('current')
if mibBuilder.loadTexts: mimosaChannel.setDescription('The index used to access a particular entry in the RF channel table.')
mimosaChannelMode = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("transmit", 1), ("receive", 2), ("bidirectional", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaChannelMode.setStatus('current')
if mibBuilder.loadTexts: mimosaChannelMode.setDescription('Specifies the mode for the given channel. The transmit or receive\n\t values indicate Frequency Diversity (FD) mode is in use. The\n\t bidirectional value means that the channel is used for both transmit\n\t and receive in all other single or dual channel modes.')
mimosaChannelWidth = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 3), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaChannelWidth.setStatus('current')
if mibBuilder.loadTexts: mimosaChannelWidth.setDescription('Specifies the channel width of the given channel.')
mimosaChannelTxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 4), Integer32()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaChannelTxPower.setStatus('current')
if mibBuilder.loadTexts: mimosaChannelTxPower.setDescription('Specifies the transmit power level on the channel. If Channel Width\n         is set to 1xN MHz, Channel 2 is not be used. In Frequency Diversity mode,\n         Power 1 and Power 2 represent transmit power on the local and remote\n         sides, respectively.')
mimosaChannelCenterFreq = MibTableColumn((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 3, 1, 5), Integer32()).setUnits('MHz').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaChannelCenterFreq.setStatus('current')
if mibBuilder.loadTexts: mimosaChannelCenterFreq.setDescription('Specifies the center frequency of the channel used on the link. In all\n         modes, the center frequency represents the absolute center of the\n         selected channel width without any offset, and the center can be moved\n         in 5 MHz increments.\n\n         A value of 0 means this particular channel is not a valid entry.')
mimosaAntennaGain = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 4), Integer32()).setUnits('dBi').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaAntennaGain.setStatus('current')
if mibBuilder.loadTexts: mimosaAntennaGain.setDescription('The antenna gain on the Mimosa device.')
mimosaTotalTxPower = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 5), DecimalOne()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTotalTxPower.setStatus('current')
if mibBuilder.loadTexts: mimosaTotalTxPower.setDescription('The total transmit power for all the channels on the Mimosa device.')
mimosaTotalRxPower = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 6), DecimalOne()).setUnits('dBm').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTotalRxPower.setStatus('current')
if mibBuilder.loadTexts: mimosaTotalRxPower.setDescription('The total receive power for all the channels on the Mimosa device.')
mimosaTargetSignalStrength = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 6, 7), Integer32()).setUnits('dB').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTargetSignalStrength.setStatus('current')
if mibBuilder.loadTexts: mimosaTargetSignalStrength.setDescription('The calculated target receive signal strength based on device coordinates and settings.')
mimosaWanSsid = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWanSsid.setStatus('current')
if mibBuilder.loadTexts: mimosaWanSsid.setDescription('The wireless link name used by both radios. Both AP and Station must\n         use the same SSID to communicate with each other.')
mimosaWanMac = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 2), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWanMac.setStatus('current')
if mibBuilder.loadTexts: mimosaWanMac.setDescription('The MAC address used for the wireless link.')
mimosaWanStatus = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("connected", 1), ("disconnected", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWanStatus.setStatus('current')
if mibBuilder.loadTexts: mimosaWanStatus.setDescription('The wireless link status between the Mimosa devices.')
mimosaWanUpTime = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 3, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaWanUpTime.setStatus('current')
if mibBuilder.loadTexts: mimosaWanUpTime.setDescription('The wireless link up time since last reboot.')
mimosaPhyTxRate = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 1), DecimalTwo()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPhyTxRate.setStatus('current')
if mibBuilder.loadTexts: mimosaPhyTxRate.setDescription('The transmit packet rate at the physical level over a 5 second interval.')
mimosaPhyRxRate = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 2), DecimalTwo()).setUnits('kbps').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPhyRxRate.setStatus('current')
if mibBuilder.loadTexts: mimosaPhyRxRate.setDescription('The receive packet rate at the physical level over a 5 second interval.')
mimosaPerTxRate = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 3), DecimalTwo()).setUnits('%').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPerTxRate.setStatus('current')
if mibBuilder.loadTexts: mimosaPerTxRate.setDescription('The trasnmit Packet Error Rate (PER) over a 5 second interval. It is\n         caluculated as packets with errors versuss packets without errors.')
mimosaPerRxRate = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 7, 4), DecimalTwo()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPerRxRate.setStatus('current')
if mibBuilder.loadTexts: mimosaPerRxRate.setDescription('The receive Packet Error Rate (PER) over a 5 second interval. It is\n         caluculated as packets with errors versuss packets without errors.')
mimosaNetworkMode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("auto", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaNetworkMode.setStatus('current')
if mibBuilder.loadTexts: mimosaNetworkMode.setDescription('Specifies the mode for the local 2.4 GHz wireless network operation.\n         If Auto is selected, the 2.4 GHz management network is turned on for a\n         limited time (defined in Console Timeout ) after boot and then turned\n         off if there is no activity. If a user associates with the radio within\n         the timeout period, they will not be disconnected.')
mimosaRecoverySsid = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRecoverySsid.setStatus('current')
if mibBuilder.loadTexts: mimosaRecoverySsid.setDescription('The recovery SSID that allows the device to be reset to factory\n         defaults. This is available for 10 minutes after device boot. Disabling\n         the 2.4 GHz management network will not impact availability of this\n         option. The serial number of the device must be known in order to\n         perform the factory reset.')
mimosaLocalSsid = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalSsid.setStatus('current')
if mibBuilder.loadTexts: mimosaLocalSsid.setDescription('The SSID for managing the local 2.4 GHz wireless interface.')
mimosaLocalChannel = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalChannel.setStatus('current')
if mibBuilder.loadTexts: mimosaLocalChannel.setDescription('The channel used for the local 2.4 GHz wireless interface.')
mimosaConsoleTimeout = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 5), Integer32()).setUnits('min').setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaConsoleTimeout.setStatus('current')
if mibBuilder.loadTexts: mimosaConsoleTimeout.setDescription('The amount inactivity on the 2.4 GHz wireless interface before\n         turning it off in Auto mode.')
mimosaMaxClients = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaMaxClients.setStatus('current')
if mibBuilder.loadTexts: mimosaMaxClients.setDescription('The maximum number of wireless clients that can simultaneously access\n         the 2.4 GHz management interface.')
mimosaLocalMac = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalMac.setStatus('current')
if mibBuilder.loadTexts: mimosaLocalMac.setDescription('The MAC address used for 2.4 GHz wireless link.')
mimosaLocalIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 8), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalIpAddr.setStatus('current')
if mibBuilder.loadTexts: mimosaLocalIpAddr.setDescription('The IP address assigned to the 2.4 GHz wireless link.')
mimosaLocalNetMask = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 9), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalNetMask.setStatus('current')
if mibBuilder.loadTexts: mimosaLocalNetMask.setDescription('The IP netmask assigned to the 2.4 GHz wireless link.')
mimosaLocalGateway = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 10), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaLocalGateway.setStatus('current')
if mibBuilder.loadTexts: mimosaLocalGateway.setDescription('The IP address of the gateway for the 2.4 GHz wireless link.')
mimosaFlowControl = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 5, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaFlowControl.setStatus('current')
if mibBuilder.loadTexts: mimosaFlowControl.setDescription('Specifies whether Flow Control is enabled on the Mimosa device.')
mimosaHttpsEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaHttpsEnabled.setStatus('current')
if mibBuilder.loadTexts: mimosaHttpsEnabled.setDescription('Specifies whether HTTPS is enabled on the Mimosa device.')
mimosaMgmtVlanEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaMgmtVlanEnabled.setStatus('current')
if mibBuilder.loadTexts: mimosaMgmtVlanEnabled.setDescription('Specifies whether the Management VLAN is enabled on the Mimosa device.')
mimosaMgmtCloudEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaMgmtCloudEnabled.setStatus('current')
if mibBuilder.loadTexts: mimosaMgmtCloudEnabled.setDescription('Specifies whether the Management Cloud is enabled on the Mimosa device.')
mimosaRestMgmtEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaRestMgmtEnabled.setStatus('current')
if mibBuilder.loadTexts: mimosaRestMgmtEnabled.setDescription('Specifies whether the REST management is enabled on the Mimosa device.')
mimosaPingWatchdogEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaPingWatchdogEnabled.setStatus('current')
if mibBuilder.loadTexts: mimosaPingWatchdogEnabled.setDescription('Specifies whether the IP Ping watchdog is enabled on the Mimosa device.\n         This is used to reset the device if a configured IP address is\n         not reached in certain number of retries.')
mimosaSyslogEnabled = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaSyslogEnabled.setStatus('current')
if mibBuilder.loadTexts: mimosaSyslogEnabled.setDescription('Specifies whether the Syslog client is enabled on the Mimosa device.\n         Syslog client sends the log messages to configured syslog server.')
mimosaNtpMode = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("custom", 1), ("standard", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaNtpMode.setStatus('current')
if mibBuilder.loadTexts: mimosaNtpMode.setDescription('Specifies whether the NTP client is configured to use standard servers\n         from NIST, NTP organizations or custom NTP server.')
mimosaNtpServer = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2, 8, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaNtpServer.setStatus('current')
if mibBuilder.loadTexts: mimosaNtpServer.setDescription('Specifies the name or address of the custom NTP server.')
mibBuilder.exportSymbols("MIMOSA-NETWORKS-BFIVE-MIB", mimosaGlonassSatellites=mimosaGlonassSatellites, mimosaTDMAWindow=mimosaTDMAWindow, mimosaUnlockCode=mimosaUnlockCode, mimosaWirelessMode=mimosaWirelessMode, mimosaChain=mimosaChain, mimosaChainTable=mimosaChainTable, mimosaChainEntry=mimosaChainEntry, mimosaSatelliteStrength=mimosaSatelliteStrength, mimosaTotalRxPower=mimosaTotalRxPower, mimosaPerTxRate=mimosaPerTxRate, mimosaPingWatchdogEnabled=mimosaPingWatchdogEnabled, mimosaTdmaInfo=mimosaTdmaInfo, mimosaLEDBrightness=mimosaLEDBrightness, mimosaRxPower=mimosaRxPower, mimosaSerialNumber=mimosaSerialNumber, mimosaFirmwareBuildDate=mimosaFirmwareBuildDate, mimosaWanUpTime=mimosaWanUpTime, mimosaTargetSignalStrength=mimosaTargetSignalStrength, mimosaLocalMac=mimosaLocalMac, mimosaMgmtInfo=mimosaMgmtInfo, mimosaSNR=mimosaSNR, mimosaLongitude=mimosaLongitude, mimosaWanMac=mimosaWanMac, mimosaTotalTxPower=mimosaTotalTxPower, mimosaRfInfo=mimosaRfInfo, mimosaLastRebootTime=mimosaLastRebootTime, mimosaRegulatoryDomain=mimosaRegulatoryDomain, mimosaLocalChannel=mimosaLocalChannel, PYSNMP_MODULE_ID=mimosaB5Module, mimosaStream=mimosaStream, mimosaWanInfo=mimosaWanInfo, mimosaWirelessProtocol=mimosaWirelessProtocol, mimosaNetworkMode=mimosaNetworkMode, mimosaInternalTemp=mimosaInternalTemp, mimosaPolarization=mimosaPolarization, mimosaChannelTable=mimosaChannelTable, mimosaClockAccuracy=mimosaClockAccuracy, mimosaChannelMode=mimosaChannelMode, mimosaMgmtVlanEnabled=mimosaMgmtVlanEnabled, mimosaRestMgmtEnabled=mimosaRestMgmtEnabled, mimosaNtpServer=mimosaNtpServer, mimosaNtpMode=mimosaNtpMode, mimosaServices=mimosaServices, mimosaConsoleTimeout=mimosaConsoleTimeout, mimosaRxPhy=mimosaRxPhy, mimosaPerRxRate=mimosaPerRxRate, mimosaChannelEntry=mimosaChannelEntry, mimosaChannel=mimosaChannel, mimosaLocInfo=mimosaLocInfo, mimosaRxWidth=mimosaRxWidth, mimosaChannelCenterFreq=mimosaChannelCenterFreq, DecimalFive=DecimalFive, mimosaB5Module=mimosaB5Module, mimosaHttpsEnabled=mimosaHttpsEnabled, mimosaSatelliteSNR=mimosaSatelliteSNR, mimosaCenterFreq=mimosaCenterFreq, mimosaAntennaGain=mimosaAntennaGain, mimosaLocalSsid=mimosaLocalSsid, mimosaLocalIpAddr=mimosaLocalIpAddr, mimosaPerfInfo=mimosaPerfInfo, mimosaRxMCS=mimosaRxMCS, mimosaTrafficSplit=mimosaTrafficSplit, mimosaSyslogEnabled=mimosaSyslogEnabled, mimosaStreamTable=mimosaStreamTable, mimosaChannelWidth=mimosaChannelWidth, mimosaRxNoise=mimosaRxNoise, mimosaWanStatus=mimosaWanStatus, mimosaTDMAMode=mimosaTDMAMode, mimosaAltitude=mimosaAltitude, mimosaLatitude=mimosaLatitude, DecimalOne=DecimalOne, mimosaDeviceName=mimosaDeviceName, mimosaPhyTxRate=mimosaPhyTxRate, mimosaChannelTxPower=mimosaChannelTxPower, DecimalTwo=DecimalTwo, mimosaMaxClients=mimosaMaxClients, mimosaWanSsid=mimosaWanSsid, mimosaStreamEntry=mimosaStreamEntry, mimosaTxPhy=mimosaTxPhy, mimosaLocalNetMask=mimosaLocalNetMask, mimosaTxMCS=mimosaTxMCS, mimosaFirmwareVersion=mimosaFirmwareVersion, mimosaMgmtCloudEnabled=mimosaMgmtCloudEnabled, mimosaGPSSatellites=mimosaGPSSatellites, mimosaTxPower=mimosaTxPower, mimosaGeneral=mimosaGeneral, mimosaTxWidth=mimosaTxWidth, mimosaPhyRxRate=mimosaPhyRxRate, mimosaFlowControl=mimosaFlowControl, mimosaLocalGateway=mimosaLocalGateway, mimosaRecoverySsid=mimosaRecoverySsid, mimosaRxEVM=mimosaRxEVM)
