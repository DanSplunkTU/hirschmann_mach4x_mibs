#
# PySNMP MIB module PACKETLOGIC-CHANNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/procera/PACKETLOGIC-CHANNEL-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:34:56 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
packetlogic2, = mibBuilder.importSymbols("PACKETLOGIC-MIB", "packetlogic2")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, Gauge32, ObjectIdentity, MibIdentifier, Integer32, Bits, TimeTicks, NotificationType, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Gauge32", "ObjectIdentity", "MibIdentifier", "Integer32", "Bits", "TimeTicks", "NotificationType", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Counter32", "iso")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
channelstats = ModuleIdentity((1, 3, 6, 1, 4, 1, 15397, 2, 2))
channelstats.setRevisions(('2019-09-12 15:00',))
if mibBuilder.loadTexts: channelstats.setLastUpdated('201909121500Z')
if mibBuilder.loadTexts: channelstats.setOrganization('Procera Networks, Inc.')
channelCfg = MibIdentifier((1, 3, 6, 1, 4, 1, 15397, 2, 2, 8))
channelInfoTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17), )
if mibBuilder.loadTexts: channelInfoTable.setStatus('current')
channelInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1), ).setIndexNames((0, "PACKETLOGIC-CHANNEL-MIB", "channelInfoEntryIndex"))
if mibBuilder.loadTexts: channelInfoEntry.setStatus('current')
channelInfoEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: channelInfoEntryIndex.setStatus('current')
netDeviceTable = MibTable((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25), )
if mibBuilder.loadTexts: netDeviceTable.setStatus('current')
netDeviceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1), ).setIndexNames((0, "PACKETLOGIC-CHANNEL-MIB", "netDeviceEntryIndex"))
if mibBuilder.loadTexts: netDeviceEntry.setStatus('current')
netDeviceEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 999), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: netDeviceEntryIndex.setStatus('current')
channelRxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: channelRxPackets.setStatus('current')
channelTxPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2), ObjectIdentifier())
if mibBuilder.loadTexts: channelTxPackets.setStatus('current')
channelRxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3), ObjectIdentifier())
if mibBuilder.loadTexts: channelRxBytes.setStatus('current')
channelTxBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4), ObjectIdentifier())
if mibBuilder.loadTexts: channelTxBytes.setStatus('current')
channelRxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5), ObjectIdentifier())
if mibBuilder.loadTexts: channelRxErrors.setStatus('current')
channelTxErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6), ObjectIdentifier())
if mibBuilder.loadTexts: channelTxErrors.setStatus('current')
channelRxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7), ObjectIdentifier())
if mibBuilder.loadTexts: channelRxDrops.setStatus('current')
channelTxDrops = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8), ObjectIdentifier())
if mibBuilder.loadTexts: channelTxDrops.setStatus('current')
channelCollisions = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9), ObjectIdentifier())
if mibBuilder.loadTexts: channelCollisions.setStatus('current')
channelMulticast = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10), ObjectIdentifier())
if mibBuilder.loadTexts: channelMulticast.setStatus('current')
channelRxLengthErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11), ObjectIdentifier())
if mibBuilder.loadTexts: channelRxLengthErrors.setStatus('current')
channelRxCrcErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12), ObjectIdentifier())
if mibBuilder.loadTexts: channelRxCrcErrors.setStatus('current')
channelRxFrameErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13), ObjectIdentifier())
if mibBuilder.loadTexts: channelRxFrameErrors.setStatus('current')
channelRxFifoErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14), ObjectIdentifier())
if mibBuilder.loadTexts: channelRxFifoErrors.setStatus('current')
channelRxMissedErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15), ObjectIdentifier())
if mibBuilder.loadTexts: channelRxMissedErrors.setStatus('current')
channelTxAborted = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16), ObjectIdentifier())
if mibBuilder.loadTexts: channelTxAborted.setStatus('current')
channelTxWindowErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17), ObjectIdentifier())
if mibBuilder.loadTexts: channelTxWindowErrors.setStatus('current')
channelTxCarrierErrors = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18), ObjectIdentifier())
if mibBuilder.loadTexts: channelTxCarrierErrors.setStatus('current')
channelNumber = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 8, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelNumber.setStatus('current')
channelInternalMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("auto", 0), ("hd-10", 1), ("fd-10", 2), ("hd-100", 3), ("fd-100", 4), ("fd-1000", 5), ("fd-10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalMedia.setStatus('current')
channelExternalMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("auto", 0), ("hd-10", 1), ("fd-10", 2), ("hd-100", 3), ("fd-100", 4), ("fd-1000", 5), ("fd-10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalMedia.setStatus('current')
channelInternalNegotiatedMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("linkdown", 0), ("hd10", 1), ("fd10", 2), ("hd100", 3), ("fd100", 4), ("fd1000", 5), ("fd10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalNegotiatedMedia.setStatus('current')
channelExternalNegotiatedMedia = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("linkdown", 0), ("hd10", 1), ("fd10", 2), ("hd100", 3), ("fd100", 4), ("fd1000", 5), ("fd10000", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalNegotiatedMedia.setStatus('current')
channelActive = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("inactive", 0), ("active", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelActive.setStatus('current')
channelName = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelName.setStatus('current')
channelInternalNegotiatedMediaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalNegotiatedMediaTime.setStatus('current')
channelExternalNegotiatedMediaTime = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalNegotiatedMediaTime.setStatus('current')
channelInternalTransceiverVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTransceiverVendor.setStatus('current')
channelInternalTransceiverPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTransceiverPartNumber.setStatus('current')
channelInternalTransceiverSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTransceiverSerial.setStatus('current')
channelInternalTransceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTransceiverType.setStatus('current')
channelInternalTransceiverWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTransceiverWavelength.setStatus('current')
channelExternalTransceiverVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTransceiverVendor.setStatus('current')
channelExternalTransceiverPartNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTransceiverPartNumber.setStatus('current')
channelExternalTransceiverSerial = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTransceiverSerial.setStatus('current')
channelExternalTransceiverType = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTransceiverType.setStatus('current')
channelExternalTransceiverWavelength = MibTableColumn((1, 3, 6, 1, 4, 1, 15397, 2, 2, 17, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTransceiverWavelength.setStatus('current')
channelInternalRxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxPackets.setStatus('current')
channelExternalRxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxPackets.setStatus('current')
channelInternalTxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxPackets.setStatus('current')
channelExternalTxPackets = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 2, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxPackets.setStatus('current')
channelInternalRxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxBytes.setStatus('current')
channelExternalRxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxBytes.setStatus('current')
channelInternalTxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxBytes.setStatus('current')
channelExternalTxBytes = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 4, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxBytes.setStatus('current')
channelInternalRxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxErrors.setStatus('current')
channelExternalRxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 5, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxErrors.setStatus('current')
channelInternalTxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxErrors.setStatus('current')
channelExternalTxErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 6, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxErrors.setStatus('current')
channelInternalRxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxDrops.setStatus('current')
channelExternalRxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 7, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxDrops.setStatus('current')
channelInternalTxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxDrops.setStatus('current')
channelExternalTxDrops = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 8, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxDrops.setStatus('current')
channelInternalCollisions = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalCollisions.setStatus('current')
channelExternalCollisions = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 9, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalCollisions.setStatus('current')
channelInternalMulticast = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalMulticast.setStatus('current')
channelExternalMulticast = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 10, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalMulticast.setStatus('current')
channelInternalRxLengthErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxLengthErrors.setStatus('current')
channelExternalRxLengthErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 11, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxLengthErrors.setStatus('current')
channelInternalRxCrcErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxCrcErrors.setStatus('current')
channelExternalRxCrcErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 12, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxCrcErrors.setStatus('current')
channelInternalRxFrameErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxFrameErrors.setStatus('current')
channelExternalRxFrameErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 13, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxFrameErrors.setStatus('current')
channelINternalRxFifoErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelINternalRxFifoErrors.setStatus('current')
channelExternalRxFifoErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 14, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxFifoErrors.setStatus('current')
channelInternalRxMissedErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalRxMissedErrors.setStatus('current')
channelExternalRxMissedErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 15, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalRxMissedErrors.setStatus('current')
channelInternalTxAborted = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxAborted.setStatus('current')
channelExternalTxAborted = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 16, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxAborted.setStatus('current')
channelInternalTxWindowErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxWindowErrors.setStatus('current')
channelExternalTxWindowErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 17, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxWindowErrors.setStatus('current')
channelInternalTxCarrierErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelInternalTxCarrierErrors.setStatus('current')
channelExternalTxCarrierErrors = MibScalar((1, 3, 6, 1, 4, 1, 15397, 2, 2, 25, 1, 18, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelExternalTxCarrierErrors.setStatus('current')
mibBuilder.exportSymbols("PACKETLOGIC-CHANNEL-MIB", netDeviceEntryIndex=netDeviceEntryIndex, channelTxPackets=channelTxPackets, channelstats=channelstats, channelRxFrameErrors=channelRxFrameErrors, PYSNMP_MODULE_ID=channelstats, channelExternalTransceiverPartNumber=channelExternalTransceiverPartNumber, channelName=channelName, channelExternalTxCarrierErrors=channelExternalTxCarrierErrors, channelInternalTransceiverSerial=channelInternalTransceiverSerial, channelInternalRxBytes=channelInternalRxBytes, channelTxWindowErrors=channelTxWindowErrors, channelInternalRxErrors=channelInternalRxErrors, channelExternalNegotiatedMediaTime=channelExternalNegotiatedMediaTime, channelExternalTxDrops=channelExternalTxDrops, channelInternalCollisions=channelInternalCollisions, channelRxErrors=channelRxErrors, channelInternalTxDrops=channelInternalTxDrops, channelExternalRxFifoErrors=channelExternalRxFifoErrors, channelInternalTransceiverType=channelInternalTransceiverType, channelInternalMedia=channelInternalMedia, channelExternalTxBytes=channelExternalTxBytes, channelInternalTxPackets=channelInternalTxPackets, channelExternalTxAborted=channelExternalTxAborted, channelExternalRxFrameErrors=channelExternalRxFrameErrors, channelRxPackets=channelRxPackets, channelRxBytes=channelRxBytes, channelInternalRxCrcErrors=channelInternalRxCrcErrors, channelExternalMulticast=channelExternalMulticast, channelExternalCollisions=channelExternalCollisions, channelInternalTxAborted=channelInternalTxAborted, channelExternalTxErrors=channelExternalTxErrors, channelInternalTxWindowErrors=channelInternalTxWindowErrors, channelInternalTransceiverWavelength=channelInternalTransceiverWavelength, channelInternalRxPackets=channelInternalRxPackets, channelInfoEntry=channelInfoEntry, channelInternalRxDrops=channelInternalRxDrops, channelRxCrcErrors=channelRxCrcErrors, channelExternalRxBytes=channelExternalRxBytes, netDeviceTable=netDeviceTable, channelExternalRxErrors=channelExternalRxErrors, channelExternalTransceiverWavelength=channelExternalTransceiverWavelength, channelExternalRxDrops=channelExternalRxDrops, channelInternalNegotiatedMediaTime=channelInternalNegotiatedMediaTime, channelTxCarrierErrors=channelTxCarrierErrors, channelExternalTxPackets=channelExternalTxPackets, channelExternalTxWindowErrors=channelExternalTxWindowErrors, channelInfoTable=channelInfoTable, channelExternalTransceiverType=channelExternalTransceiverType, channelInternalTxBytes=channelInternalTxBytes, channelInternalRxFrameErrors=channelInternalRxFrameErrors, channelInternalTxCarrierErrors=channelInternalTxCarrierErrors, channelCollisions=channelCollisions, channelTxBytes=channelTxBytes, channelRxMissedErrors=channelRxMissedErrors, netDeviceEntry=netDeviceEntry, channelExternalRxMissedErrors=channelExternalRxMissedErrors, channelInfoEntryIndex=channelInfoEntryIndex, channelInternalTxErrors=channelInternalTxErrors, channelTxAborted=channelTxAborted, channelInternalTransceiverVendor=channelInternalTransceiverVendor, channelInternalRxLengthErrors=channelInternalRxLengthErrors, channelExternalMedia=channelExternalMedia, channelNumber=channelNumber, channelExternalTransceiverVendor=channelExternalTransceiverVendor, channelExternalRxPackets=channelExternalRxPackets, channelExternalRxLengthErrors=channelExternalRxLengthErrors, channelExternalNegotiatedMedia=channelExternalNegotiatedMedia, channelInternalMulticast=channelInternalMulticast, channelTxErrors=channelTxErrors, channelExternalTransceiverSerial=channelExternalTransceiverSerial, channelTxDrops=channelTxDrops, channelInternalNegotiatedMedia=channelInternalNegotiatedMedia, channelInternalTransceiverPartNumber=channelInternalTransceiverPartNumber, channelActive=channelActive, channelCfg=channelCfg, channelInternalRxMissedErrors=channelInternalRxMissedErrors, channelINternalRxFifoErrors=channelINternalRxFifoErrors, channelRxLengthErrors=channelRxLengthErrors, channelMulticast=channelMulticast, channelExternalRxCrcErrors=channelExternalRxCrcErrors, channelRxDrops=channelRxDrops, channelRxFifoErrors=channelRxFifoErrors)
