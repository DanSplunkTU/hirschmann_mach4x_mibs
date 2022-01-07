#
# PySNMP MIB module ARISTA-BGP4V2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-BGP4V2-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:09:47 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
AristaBgp4V2AddressFamilyIdentifierTC, AristaBgp4V2IdentifierTC, AristaBgp4V2SubsequentAddressFamilyIdentifierTC = mibBuilder.importSymbols("ARISTA-BGP4V2-TC-MIB", "AristaBgp4V2AddressFamilyIdentifierTC", "AristaBgp4V2IdentifierTC", "AristaBgp4V2SubsequentAddressFamilyIdentifierTC")
aristaExperiment, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaExperiment")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
InetAddress, InetAddressType, InetAddressPrefixLength, InetPortNumber, InetAutonomousSystemNumber = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType", "InetAddressPrefixLength", "InetPortNumber", "InetAutonomousSystemNumber")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, Gauge32, IpAddress, MibIdentifier, NotificationType, ObjectIdentity, Unsigned32, Counter64, Counter32, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "Gauge32", "IpAddress", "MibIdentifier", "NotificationType", "ObjectIdentity", "Unsigned32", "Counter64", "Counter32", "Integer32", "Bits")
RowPointer, DisplayString, TruthValue, TimeStamp, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DisplayString", "TruthValue", "TimeStamp", "TextualConvention")
aristaBgp4V2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 4, 1))
aristaBgp4V2.setRevisions(('2014-08-15 00:00', '2012-10-19 00:00', '2012-03-11 00:00',))
if mibBuilder.loadTexts: aristaBgp4V2.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaBgp4V2.setOrganization('Arista Networks, Inc.')
aristaBgp4V2Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 4, 1, 0))
aristaBgp4V2Objects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1))
aristaBgp4V2Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2))
aristaBgp4V2DiscontinuityTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 1), )
if mibBuilder.loadTexts: aristaBgp4V2DiscontinuityTable.setStatus('current')
aristaBgp4V2DiscontinuityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 1, 1), ).setIndexNames((0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"))
if mibBuilder.loadTexts: aristaBgp4V2DiscontinuityEntry.setStatus('current')
aristaBgp4V2DiscontinuityTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 1, 1, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2DiscontinuityTime.setStatus('current')
aristaBgp4V2PeerTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2), )
if mibBuilder.loadTexts: aristaBgp4V2PeerTable.setStatus('current')
aristaBgp4V2PeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1), ).setIndexNames((0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddrType"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddr"))
if mibBuilder.loadTexts: aristaBgp4V2PeerEntry.setStatus('current')
aristaBgp4V2PeerInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: aristaBgp4V2PeerInstance.setStatus('current')
aristaBgp4V2PeerLocalAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 2), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLocalAddrType.setStatus('current')
aristaBgp4V2PeerLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 3), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLocalAddr.setStatus('current')
aristaBgp4V2PeerRemoteAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 4), InetAddressType())
if mibBuilder.loadTexts: aristaBgp4V2PeerRemoteAddrType.setStatus('current')
aristaBgp4V2PeerRemoteAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 5), InetAddress())
if mibBuilder.loadTexts: aristaBgp4V2PeerRemoteAddr.setStatus('current')
aristaBgp4V2PeerLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 6), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLocalPort.setStatus('current')
aristaBgp4V2PeerLocalAs = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 7), InetAutonomousSystemNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLocalAs.setStatus('current')
aristaBgp4V2PeerLocalIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 8), AristaBgp4V2IdentifierTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLocalIdentifier.setStatus('current')
aristaBgp4V2PeerRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 9), InetPortNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerRemotePort.setStatus('current')
aristaBgp4V2PeerRemoteAs = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 10), InetAutonomousSystemNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerRemoteAs.setStatus('current')
aristaBgp4V2PeerRemoteIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 11), AristaBgp4V2IdentifierTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerRemoteIdentifier.setStatus('current')
aristaBgp4V2PeerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("halted", 1), ("running", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerAdminStatus.setStatus('current')
aristaBgp4V2PeerState = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("idle", 1), ("connect", 2), ("active", 3), ("opensent", 4), ("openconfirm", 5), ("established", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerState.setStatus('current')
aristaBgp4V2PeerDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 2, 1, 14), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerDescription.setStatus('current')
aristaBgp4V2PeerErrorsTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3), )
if mibBuilder.loadTexts: aristaBgp4V2PeerErrorsTable.setStatus('current')
aristaBgp4V2PeerErrorsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1), )
aristaBgp4V2PeerEntry.registerAugmentions(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerErrorsEntry"))
aristaBgp4V2PeerErrorsEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
if mibBuilder.loadTexts: aristaBgp4V2PeerErrorsEntry.setStatus('current')
aristaBgp4V2PeerLastErrorCodeReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLastErrorCodeReceived.setStatus('current')
aristaBgp4V2PeerLastErrorSubCodeReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLastErrorSubCodeReceived.setStatus('current')
aristaBgp4V2PeerLastErrorReceivedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLastErrorReceivedTime.setStatus('current')
aristaBgp4V2PeerLastErrorReceivedText = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLastErrorReceivedText.setStatus('current')
aristaBgp4V2PeerLastErrorReceivedData = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4075))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLastErrorReceivedData.setStatus('current')
aristaBgp4V2PeerLastErrorCodeSent = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLastErrorCodeSent.setStatus('current')
aristaBgp4V2PeerLastErrorSubCodeSent = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLastErrorSubCodeSent.setStatus('current')
aristaBgp4V2PeerLastErrorSentTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 8), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLastErrorSentTime.setStatus('current')
aristaBgp4V2PeerLastErrorSentText = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLastErrorSentText.setStatus('current')
aristaBgp4V2PeerLastErrorSentData = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 3, 1, 10), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4075))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerLastErrorSentData.setStatus('current')
aristaBgp4V2PeerEventTimesTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 4), )
if mibBuilder.loadTexts: aristaBgp4V2PeerEventTimesTable.setStatus('current')
aristaBgp4V2PeerEventTimesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 4, 1), )
aristaBgp4V2PeerEntry.registerAugmentions(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerEventTimesEntry"))
aristaBgp4V2PeerEventTimesEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
if mibBuilder.loadTexts: aristaBgp4V2PeerEventTimesEntry.setStatus('current')
aristaBgp4V2PeerFsmEstablishedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 4, 1, 1), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerFsmEstablishedTime.setStatus('current')
aristaBgp4V2PeerInUpdatesElapsedTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 4, 1, 2), Gauge32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerInUpdatesElapsedTime.setStatus('current')
aristaBgp4V2PeerConfiguredTimersTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5), )
if mibBuilder.loadTexts: aristaBgp4V2PeerConfiguredTimersTable.setStatus('current')
aristaBgp4V2PeerConfiguredTimersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1), )
aristaBgp4V2PeerEntry.registerAugmentions(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerConfiguredTimersEntry"))
aristaBgp4V2PeerConfiguredTimersEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
if mibBuilder.loadTexts: aristaBgp4V2PeerConfiguredTimersEntry.setStatus('current')
aristaBgp4V2PeerConnectRetryInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerConnectRetryInterval.setStatus('current')
aristaBgp4V2PeerHoldTimeConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerHoldTimeConfigured.setStatus('current')
aristaBgp4V2PeerKeepAliveConfigured = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1, 3), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), ))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerKeepAliveConfigured.setStatus('current')
aristaBgp4V2PeerMinASOrigInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerMinASOrigInterval.setStatus('current')
aristaBgp4V2PeerMinRouteAdverInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 5, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerMinRouteAdverInterval.setStatus('current')
aristaBgp4V2PeerNegotiatedTimersTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 6), )
if mibBuilder.loadTexts: aristaBgp4V2PeerNegotiatedTimersTable.setStatus('current')
aristaBgp4V2PeerNegotiatedTimersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 6, 1), )
aristaBgp4V2PeerEntry.registerAugmentions(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerNegotiatedTimersEntry"))
aristaBgp4V2PeerNegotiatedTimersEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
if mibBuilder.loadTexts: aristaBgp4V2PeerNegotiatedTimersEntry.setStatus('current')
aristaBgp4V2PeerHoldTime = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 6, 1, 1), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(3, 65535), ))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerHoldTime.setStatus('current')
aristaBgp4V2PeerKeepAlive = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 6, 1, 2), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 21845), ))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerKeepAlive.setStatus('current')
aristaBgp4V2PeerCountersTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7), )
if mibBuilder.loadTexts: aristaBgp4V2PeerCountersTable.setStatus('current')
aristaBgp4V2PeerCountersEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1), )
aristaBgp4V2PeerEntry.registerAugmentions(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerCountersEntry"))
aristaBgp4V2PeerCountersEntry.setIndexNames(*aristaBgp4V2PeerEntry.getIndexNames())
if mibBuilder.loadTexts: aristaBgp4V2PeerCountersEntry.setStatus('current')
aristaBgp4V2PeerInUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerInUpdates.setStatus('current')
aristaBgp4V2PeerOutUpdates = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerOutUpdates.setStatus('current')
aristaBgp4V2PeerInTotalMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerInTotalMessages.setStatus('current')
aristaBgp4V2PeerOutTotalMessages = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerOutTotalMessages.setStatus('current')
aristaBgp4V2PeerFsmEstablishedTransitions = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 7, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PeerFsmEstablishedTransitions.setStatus('current')
aristaBgp4V2PrefixGaugesTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8), )
if mibBuilder.loadTexts: aristaBgp4V2PrefixGaugesTable.setStatus('current')
aristaBgp4V2PrefixGaugesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1), ).setIndexNames((0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddrType"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddr"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PrefixGaugesAfi"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PrefixGaugesSafi"))
if mibBuilder.loadTexts: aristaBgp4V2PrefixGaugesEntry.setStatus('current')
aristaBgp4V2PrefixGaugesAfi = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1, 1), AristaBgp4V2AddressFamilyIdentifierTC())
if mibBuilder.loadTexts: aristaBgp4V2PrefixGaugesAfi.setStatus('current')
aristaBgp4V2PrefixGaugesSafi = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1, 2), AristaBgp4V2SubsequentAddressFamilyIdentifierTC())
if mibBuilder.loadTexts: aristaBgp4V2PrefixGaugesSafi.setStatus('current')
aristaBgp4V2PrefixInPrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PrefixInPrefixes.setStatus('current')
aristaBgp4V2PrefixInPrefixesAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PrefixInPrefixesAccepted.setStatus('current')
aristaBgp4V2PrefixOutPrefixes = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 8, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2PrefixOutPrefixes.setStatus('current')
aristaBgp4V2NlriTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9), )
if mibBuilder.loadTexts: aristaBgp4V2NlriTable.setStatus('current')
aristaBgp4V2NlriEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1), ).setIndexNames((0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAfi"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriSafi"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefixType"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefix"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefixLen"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddrType"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddr"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriIndex"))
if mibBuilder.loadTexts: aristaBgp4V2NlriEntry.setStatus('current')
aristaBgp4V2NlriIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: aristaBgp4V2NlriIndex.setStatus('current')
aristaBgp4V2NlriAfi = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 2), AristaBgp4V2AddressFamilyIdentifierTC())
if mibBuilder.loadTexts: aristaBgp4V2NlriAfi.setStatus('current')
aristaBgp4V2NlriSafi = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 3), AristaBgp4V2SubsequentAddressFamilyIdentifierTC())
if mibBuilder.loadTexts: aristaBgp4V2NlriSafi.setStatus('current')
aristaBgp4V2NlriPrefixType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 4), InetAddressType())
if mibBuilder.loadTexts: aristaBgp4V2NlriPrefixType.setStatus('current')
aristaBgp4V2NlriPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 5), InetAddress())
if mibBuilder.loadTexts: aristaBgp4V2NlriPrefix.setStatus('current')
aristaBgp4V2NlriPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 6), InetAddressPrefixLength())
if mibBuilder.loadTexts: aristaBgp4V2NlriPrefixLen.setStatus('current')
aristaBgp4V2NlriBest = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriBest.setStatus('current')
aristaBgp4V2NlriCalcLocalPref = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriCalcLocalPref.setStatus('current')
aristaBgp4V2NlriOrigin = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("igp", 1), ("egp", 2), ("incomplete", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriOrigin.setStatus('current')
aristaBgp4V2NlriNextHopAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 10), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriNextHopAddrType.setStatus('current')
aristaBgp4V2NlriNextHopAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 11), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(4, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriNextHopAddr.setStatus('current')
aristaBgp4V2NlriLinkLocalNextHopAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 12), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriLinkLocalNextHopAddrType.setStatus('current')
aristaBgp4V2NlriLinkLocalNextHopAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 13), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriLinkLocalNextHopAddr.setStatus('current')
aristaBgp4V2NlriLocalPrefPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriLocalPrefPresent.setStatus('current')
aristaBgp4V2NlriLocalPref = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriLocalPref.setStatus('current')
aristaBgp4V2NlriMedPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriMedPresent.setStatus('current')
aristaBgp4V2NlriMed = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriMed.setStatus('current')
aristaBgp4V2NlriAtomicAggregate = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 18), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriAtomicAggregate.setStatus('current')
aristaBgp4V2NlriAggregatorPresent = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriAggregatorPresent.setStatus('current')
aristaBgp4V2NlriAggregatorAS = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 20), InetAutonomousSystemNumber()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriAggregatorAS.setStatus('current')
aristaBgp4V2NlriAggregatorAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 21), AristaBgp4V2IdentifierTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriAggregatorAddr.setStatus('current')
aristaBgp4V2NlriAsPathCalcLength = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 22), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriAsPathCalcLength.setStatus('current')
aristaBgp4V2NlriAsPathString = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 23), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriAsPathString.setStatus('current')
aristaBgp4V2NlriAsPath = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 24), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 4072))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriAsPath.setStatus('current')
aristaBgp4V2NlriPathAttrUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 9, 1, 25), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 4072))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2NlriPathAttrUnknown.setStatus('current')
aristaBgp4V2AdjRibsOutTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 10), )
if mibBuilder.loadTexts: aristaBgp4V2AdjRibsOutTable.setStatus('current')
aristaBgp4V2AdjRibsOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 10, 1), ).setIndexNames((0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInstance"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAfi"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriSafi"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefixType"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefix"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPrefixLen"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddrType"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAddr"), (0, "ARISTA-BGP4V2-MIB", "aristaBgp4V2AdjRibsOutIndex"))
if mibBuilder.loadTexts: aristaBgp4V2AdjRibsOutEntry.setStatus('current')
aristaBgp4V2AdjRibsOutIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: aristaBgp4V2AdjRibsOutIndex.setStatus('current')
aristaBgp4V2AdjRibsOutRoute = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 4, 1, 1, 10, 1, 2), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaBgp4V2AdjRibsOutRoute.setStatus('current')
aristaBgp4V2EstablishedNotification = NotificationType((1, 3, 6, 1, 4, 1, 30065, 4, 1, 0, 1)).setObjects(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerState"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalPort"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemotePort"))
if mibBuilder.loadTexts: aristaBgp4V2EstablishedNotification.setStatus('current')
aristaBgp4V2BackwardTransitionNotification = NotificationType((1, 3, 6, 1, 4, 1, 30065, 4, 1, 0, 2)).setObjects(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerState"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalPort"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemotePort"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorCodeReceived"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSubCodeReceived"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorReceivedText"))
if mibBuilder.loadTexts: aristaBgp4V2BackwardTransitionNotification.setStatus('current')
aristaBgp4V2Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 1))
aristaBgp4V2Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2))
aristaBgp4V2Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 1, 4)).setObjects(("ARISTA-BGP4V2-MIB", "aristaBgp4V2StdMIBTimersGroup"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2StdMIBCountersGroup"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2StdMIBErrorsGroup"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2StdMIBPeerGroup"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2StdMIBNlriGroup"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2GlobalsGroup"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2StdMIBNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBgp4V2Compliance = aristaBgp4V2Compliance.setStatus('current')
aristaBgp4V2GlobalsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 1)).setObjects(("ARISTA-BGP4V2-MIB", "aristaBgp4V2DiscontinuityTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBgp4V2GlobalsGroup = aristaBgp4V2GlobalsGroup.setStatus('current')
aristaBgp4V2StdMIBTimersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 2)).setObjects(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerFsmEstablishedTime"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInUpdatesElapsedTime"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerConnectRetryInterval"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerHoldTimeConfigured"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerKeepAliveConfigured"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerMinASOrigInterval"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerMinRouteAdverInterval"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerHoldTime"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerKeepAlive"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBgp4V2StdMIBTimersGroup = aristaBgp4V2StdMIBTimersGroup.setStatus('current')
aristaBgp4V2StdMIBCountersGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 3)).setObjects(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInUpdates"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerOutUpdates"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerInTotalMessages"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerOutTotalMessages"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerFsmEstablishedTransitions"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PrefixInPrefixes"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PrefixInPrefixesAccepted"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PrefixOutPrefixes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBgp4V2StdMIBCountersGroup = aristaBgp4V2StdMIBCountersGroup.setStatus('current')
aristaBgp4V2StdMIBErrorsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 5)).setObjects(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorCodeReceived"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSubCodeReceived"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorReceivedData"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorReceivedTime"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorReceivedText"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorCodeSent"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSubCodeSent"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSentData"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSentTime"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLastErrorSentText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBgp4V2StdMIBErrorsGroup = aristaBgp4V2StdMIBErrorsGroup.setStatus('current')
aristaBgp4V2StdMIBPeerGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 6)).setObjects(("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerState"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerAdminStatus"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalAddrType"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalAddr"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalPort"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalAs"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemotePort"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteAs"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerLocalIdentifier"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerRemoteIdentifier"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2PeerDescription"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBgp4V2StdMIBPeerGroup = aristaBgp4V2StdMIBPeerGroup.setStatus('current')
aristaBgp4V2StdMIBNlriGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 7)).setObjects(("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAsPathCalcLength"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAsPathString"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriBest"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriCalcLocalPref"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2AdjRibsOutRoute"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAggregatorPresent"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAggregatorAS"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAggregatorAddr"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAtomicAggregate"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriLocalPref"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriLocalPrefPresent"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriMed"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriMedPresent"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriNextHopAddr"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriNextHopAddrType"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriLinkLocalNextHopAddrType"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriLinkLocalNextHopAddr"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriOrigin"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriAsPath"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2NlriPathAttrUnknown"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBgp4V2StdMIBNlriGroup = aristaBgp4V2StdMIBNlriGroup.setStatus('current')
aristaBgp4V2StdMIBNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 4, 1, 2, 2, 8)).setObjects(("ARISTA-BGP4V2-MIB", "aristaBgp4V2EstablishedNotification"), ("ARISTA-BGP4V2-MIB", "aristaBgp4V2BackwardTransitionNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaBgp4V2StdMIBNotificationGroup = aristaBgp4V2StdMIBNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-BGP4V2-MIB", aristaBgp4V2PrefixOutPrefixes=aristaBgp4V2PrefixOutPrefixes, aristaBgp4V2NlriCalcLocalPref=aristaBgp4V2NlriCalcLocalPref, aristaBgp4V2EstablishedNotification=aristaBgp4V2EstablishedNotification, aristaBgp4V2NlriAsPathCalcLength=aristaBgp4V2NlriAsPathCalcLength, aristaBgp4V2PeerNegotiatedTimersTable=aristaBgp4V2PeerNegotiatedTimersTable, aristaBgp4V2AdjRibsOutTable=aristaBgp4V2AdjRibsOutTable, aristaBgp4V2PeerRemoteAs=aristaBgp4V2PeerRemoteAs, aristaBgp4V2GlobalsGroup=aristaBgp4V2GlobalsGroup, aristaBgp4V2PeerLastErrorReceivedTime=aristaBgp4V2PeerLastErrorReceivedTime, aristaBgp4V2PeerOutUpdates=aristaBgp4V2PeerOutUpdates, aristaBgp4V2NlriSafi=aristaBgp4V2NlriSafi, aristaBgp4V2PeerEntry=aristaBgp4V2PeerEntry, aristaBgp4V2NlriAsPath=aristaBgp4V2NlriAsPath, aristaBgp4V2PeerInTotalMessages=aristaBgp4V2PeerInTotalMessages, aristaBgp4V2NlriAggregatorAS=aristaBgp4V2NlriAggregatorAS, aristaBgp4V2AdjRibsOutIndex=aristaBgp4V2AdjRibsOutIndex, aristaBgp4V2PeerConnectRetryInterval=aristaBgp4V2PeerConnectRetryInterval, aristaBgp4V2AdjRibsOutEntry=aristaBgp4V2AdjRibsOutEntry, aristaBgp4V2NlriOrigin=aristaBgp4V2NlriOrigin, aristaBgp4V2Notifications=aristaBgp4V2Notifications, aristaBgp4V2PeerInstance=aristaBgp4V2PeerInstance, aristaBgp4V2PeerAdminStatus=aristaBgp4V2PeerAdminStatus, aristaBgp4V2=aristaBgp4V2, aristaBgp4V2PeerLastErrorSubCodeSent=aristaBgp4V2PeerLastErrorSubCodeSent, aristaBgp4V2PrefixInPrefixesAccepted=aristaBgp4V2PrefixInPrefixesAccepted, aristaBgp4V2PeerEventTimesTable=aristaBgp4V2PeerEventTimesTable, aristaBgp4V2NlriIndex=aristaBgp4V2NlriIndex, aristaBgp4V2NlriPrefixLen=aristaBgp4V2NlriPrefixLen, aristaBgp4V2PeerRemoteIdentifier=aristaBgp4V2PeerRemoteIdentifier, aristaBgp4V2PeerLastErrorSentTime=aristaBgp4V2PeerLastErrorSentTime, aristaBgp4V2PeerEventTimesEntry=aristaBgp4V2PeerEventTimesEntry, aristaBgp4V2PeerNegotiatedTimersEntry=aristaBgp4V2PeerNegotiatedTimersEntry, aristaBgp4V2StdMIBTimersGroup=aristaBgp4V2StdMIBTimersGroup, aristaBgp4V2PeerInUpdates=aristaBgp4V2PeerInUpdates, aristaBgp4V2PeerErrorsEntry=aristaBgp4V2PeerErrorsEntry, aristaBgp4V2DiscontinuityTime=aristaBgp4V2DiscontinuityTime, aristaBgp4V2PeerHoldTime=aristaBgp4V2PeerHoldTime, aristaBgp4V2PeerInUpdatesElapsedTime=aristaBgp4V2PeerInUpdatesElapsedTime, aristaBgp4V2PeerFsmEstablishedTime=aristaBgp4V2PeerFsmEstablishedTime, aristaBgp4V2PeerLastErrorReceivedText=aristaBgp4V2PeerLastErrorReceivedText, aristaBgp4V2NlriLocalPref=aristaBgp4V2NlriLocalPref, aristaBgp4V2Compliance=aristaBgp4V2Compliance, aristaBgp4V2NlriPrefix=aristaBgp4V2NlriPrefix, aristaBgp4V2PeerRemoteAddr=aristaBgp4V2PeerRemoteAddr, aristaBgp4V2PeerKeepAliveConfigured=aristaBgp4V2PeerKeepAliveConfigured, aristaBgp4V2NlriAtomicAggregate=aristaBgp4V2NlriAtomicAggregate, aristaBgp4V2StdMIBCountersGroup=aristaBgp4V2StdMIBCountersGroup, aristaBgp4V2PeerLastErrorReceivedData=aristaBgp4V2PeerLastErrorReceivedData, aristaBgp4V2PeerConfiguredTimersTable=aristaBgp4V2PeerConfiguredTimersTable, aristaBgp4V2DiscontinuityTable=aristaBgp4V2DiscontinuityTable, aristaBgp4V2DiscontinuityEntry=aristaBgp4V2DiscontinuityEntry, aristaBgp4V2StdMIBNlriGroup=aristaBgp4V2StdMIBNlriGroup, aristaBgp4V2PeerDescription=aristaBgp4V2PeerDescription, aristaBgp4V2PeerLastErrorSubCodeReceived=aristaBgp4V2PeerLastErrorSubCodeReceived, aristaBgp4V2NlriEntry=aristaBgp4V2NlriEntry, aristaBgp4V2PrefixInPrefixes=aristaBgp4V2PrefixInPrefixes, aristaBgp4V2Conformance=aristaBgp4V2Conformance, aristaBgp4V2NlriAfi=aristaBgp4V2NlriAfi, aristaBgp4V2NlriAsPathString=aristaBgp4V2NlriAsPathString, aristaBgp4V2PeerFsmEstablishedTransitions=aristaBgp4V2PeerFsmEstablishedTransitions, aristaBgp4V2PrefixGaugesSafi=aristaBgp4V2PrefixGaugesSafi, aristaBgp4V2PrefixGaugesAfi=aristaBgp4V2PrefixGaugesAfi, aristaBgp4V2NlriAggregatorPresent=aristaBgp4V2NlriAggregatorPresent, PYSNMP_MODULE_ID=aristaBgp4V2, aristaBgp4V2NlriMed=aristaBgp4V2NlriMed, aristaBgp4V2NlriPathAttrUnknown=aristaBgp4V2NlriPathAttrUnknown, aristaBgp4V2PeerLastErrorCodeReceived=aristaBgp4V2PeerLastErrorCodeReceived, aristaBgp4V2NlriAggregatorAddr=aristaBgp4V2NlriAggregatorAddr, aristaBgp4V2StdMIBErrorsGroup=aristaBgp4V2StdMIBErrorsGroup, aristaBgp4V2PeerConfiguredTimersEntry=aristaBgp4V2PeerConfiguredTimersEntry, aristaBgp4V2PeerHoldTimeConfigured=aristaBgp4V2PeerHoldTimeConfigured, aristaBgp4V2Compliances=aristaBgp4V2Compliances, aristaBgp4V2PeerMinRouteAdverInterval=aristaBgp4V2PeerMinRouteAdverInterval, aristaBgp4V2PeerLocalAddr=aristaBgp4V2PeerLocalAddr, aristaBgp4V2PeerCountersEntry=aristaBgp4V2PeerCountersEntry, aristaBgp4V2NlriLinkLocalNextHopAddrType=aristaBgp4V2NlriLinkLocalNextHopAddrType, aristaBgp4V2Objects=aristaBgp4V2Objects, aristaBgp4V2PeerOutTotalMessages=aristaBgp4V2PeerOutTotalMessages, aristaBgp4V2PrefixGaugesTable=aristaBgp4V2PrefixGaugesTable, aristaBgp4V2PeerErrorsTable=aristaBgp4V2PeerErrorsTable, aristaBgp4V2NlriTable=aristaBgp4V2NlriTable, aristaBgp4V2NlriNextHopAddr=aristaBgp4V2NlriNextHopAddr, aristaBgp4V2StdMIBNotificationGroup=aristaBgp4V2StdMIBNotificationGroup, aristaBgp4V2PeerLocalAddrType=aristaBgp4V2PeerLocalAddrType, aristaBgp4V2NlriLinkLocalNextHopAddr=aristaBgp4V2NlriLinkLocalNextHopAddr, aristaBgp4V2PeerMinASOrigInterval=aristaBgp4V2PeerMinASOrigInterval, aristaBgp4V2PeerRemoteAddrType=aristaBgp4V2PeerRemoteAddrType, aristaBgp4V2PeerLocalPort=aristaBgp4V2PeerLocalPort, aristaBgp4V2NlriPrefixType=aristaBgp4V2NlriPrefixType, aristaBgp4V2PrefixGaugesEntry=aristaBgp4V2PrefixGaugesEntry, aristaBgp4V2PeerLastErrorSentData=aristaBgp4V2PeerLastErrorSentData, aristaBgp4V2PeerLocalIdentifier=aristaBgp4V2PeerLocalIdentifier, aristaBgp4V2PeerLastErrorCodeSent=aristaBgp4V2PeerLastErrorCodeSent, aristaBgp4V2PeerRemotePort=aristaBgp4V2PeerRemotePort, aristaBgp4V2NlriBest=aristaBgp4V2NlriBest, aristaBgp4V2AdjRibsOutRoute=aristaBgp4V2AdjRibsOutRoute, aristaBgp4V2PeerState=aristaBgp4V2PeerState, aristaBgp4V2PeerLocalAs=aristaBgp4V2PeerLocalAs, aristaBgp4V2Groups=aristaBgp4V2Groups, aristaBgp4V2PeerLastErrorSentText=aristaBgp4V2PeerLastErrorSentText, aristaBgp4V2PeerKeepAlive=aristaBgp4V2PeerKeepAlive, aristaBgp4V2NlriLocalPrefPresent=aristaBgp4V2NlriLocalPrefPresent, aristaBgp4V2NlriNextHopAddrType=aristaBgp4V2NlriNextHopAddrType, aristaBgp4V2StdMIBPeerGroup=aristaBgp4V2StdMIBPeerGroup, aristaBgp4V2PeerCountersTable=aristaBgp4V2PeerCountersTable, aristaBgp4V2NlriMedPresent=aristaBgp4V2NlriMedPresent, aristaBgp4V2BackwardTransitionNotification=aristaBgp4V2BackwardTransitionNotification, aristaBgp4V2PeerTable=aristaBgp4V2PeerTable)
