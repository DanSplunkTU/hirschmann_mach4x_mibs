#
# PySNMP MIB module BENU-TWAG-STATS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-TWAG-STATS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:33:39 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Gauge32, ModuleIdentity, Counter64, MibIdentifier, Integer32, TimeTicks, Counter32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Bits, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Counter64", "MibIdentifier", "Integer32", "TimeTicks", "Counter32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Bits", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuTWagStatsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7))
benuTWagStatsMIB.setRevisions(('2016-07-19 00:00', '2016-07-27 00:00',))
if mibBuilder.loadTexts: benuTWagStatsMIB.setLastUpdated('201607270000Z')
if mibBuilder.loadTexts: benuTWagStatsMIB.setOrganization('Benu Networks,Inc')
bTWagNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 0))
if mibBuilder.loadTexts: bTWagNotifications.setStatus('current')
bTWagS2aSubscriberMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1))
if mibBuilder.loadTexts: bTWagS2aSubscriberMIBObjects.setStatus('current')
bTWagS2aSubscriberNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 2))
if mibBuilder.loadTexts: bTWagS2aSubscriberNotifObjects.setStatus('current')
bTWagS2aStatsMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3))
if mibBuilder.loadTexts: bTWagS2aStatsMIBObjects.setStatus('current')
bTWagS2aNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 4))
if mibBuilder.loadTexts: bTWagS2aNotifObjects.setStatus('current')
bTWagGTPStatsMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 5))
if mibBuilder.loadTexts: bTWagGTPStatsMIBObjects.setStatus('current')
bTWagGTPNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 6))
if mibBuilder.loadTexts: bTWagGTPNotifObjects.setStatus('current')
bTWagGnGpSubscriberMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7))
if mibBuilder.loadTexts: bTWagGnGpSubscriberMIBObjects.setStatus('current')
bTWagGnGpSubscriberNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 8))
if mibBuilder.loadTexts: bTWagGnGpSubscriberNotifObjects.setStatus('current')
bTWagGnGpStatsMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9))
if mibBuilder.loadTexts: bTWagGnGpStatsMIBObjects.setStatus('current')
bTWagGnGpNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 10))
if mibBuilder.loadTexts: bTWagGnGpNotifObjects.setStatus('current')
bTWagPmip6MIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11))
if mibBuilder.loadTexts: bTWagPmip6MIBObjects.setStatus('current')
bTWagGTPCurrentNumOfTunnels = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 5, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGTPCurrentNumOfTunnels.setStatus('current')
bTWagNumCurrentSecureSSIDS2aSubscribers = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagNumCurrentSecureSSIDS2aSubscribers.setStatus('current')
bTWagNumPreAuthenticatedS2aSubscribers = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagNumPreAuthenticatedS2aSubscribers.setStatus('current')
bTWagNumCurrentSecureSSIDGnGpSubscribers = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagNumCurrentSecureSSIDGnGpSubscribers.setStatus('current')
bTWagNumPreAuthenticatedGnGpSubscribers = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagNumPreAuthenticatedGnGpSubscribers.setStatus('current')
bTWagNumPreAuthenticatedPmip6Subscribers = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagNumPreAuthenticatedPmip6Subscribers.setStatus('current')
bTWagNumGrePmip6Tunnels = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagNumGrePmip6Tunnels.setStatus('current')
bTWagPmip6StatsTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3), )
if mibBuilder.loadTexts: bTWagPmip6StatsTable.setStatus('current')
bTWagPmip6StatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1), ).setIndexNames((0, "BENU-TWAG-STATS-MIB", "bTWagPmip6StatsInterval"))
if mibBuilder.loadTexts: bTWagPmip6StatsEntry.setStatus('current')
bTWagPmip6StatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: bTWagPmip6StatsInterval.setStatus('current')
bTWagPmip6IntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6IntervalDuration.setStatus('current')
bTWagPmip6TotalPacketsRxvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6TotalPacketsRxvd.setStatus('current')
bTWagPmip6TotalPacketsRxvdError = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6TotalPacketsRxvdError.setStatus('current')
bTWagPmip6TotalPacketHeaderDecodeError = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6TotalPacketHeaderDecodeError.setStatus('current')
bTWagPmip6TotalPbuSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6TotalPbuSent.setStatus('current')
bTWagPmip6TotalPbuSendError = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6TotalPbuSendError.setStatus('current')
bTWagPmip6TotalPbaReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6TotalPbaReceived.setStatus('current')
bTWagPmip6TotalBriReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6TotalBriReceived.setStatus('current')
bTWagPmip6TotalBraSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6TotalBraSent.setStatus('current')
bTWagPmip6HeartBeatReqSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6HeartBeatReqSent.setStatus('current')
bTWagPmip6HeartBeatRspSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6HeartBeatRspSent.setStatus('current')
bTWagPmip6HeartBeatReqRestartCountMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6HeartBeatReqRestartCountMismatch.setStatus('current')
bTWagPmip6HeartBeatReqSeqMismatch = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6HeartBeatReqSeqMismatch.setStatus('current')
bTWagPmip6DeletedDueToLmaInitBriMsg = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 11, 3, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPmip6DeletedDueToLmaInitBriMsg.setStatus('current')
bTWagS2aSubscriberTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3), )
if mibBuilder.loadTexts: bTWagS2aSubscriberTable.setStatus('current')
bTWagS2aSubscriberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1), ).setIndexNames((0, "BENU-TWAG-STATS-MIB", "bTWagS2aSubsStatsInterval"))
if mibBuilder.loadTexts: bTWagS2aSubscriberEntry.setStatus('current')
bTWagS2aSubsStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: bTWagS2aSubsStatsInterval.setStatus('current')
bTWagS2aSubsIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsIntervalDuration.setStatus('current')
bTWagSecureSSIDS2aSubsAdded = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagSecureSSIDS2aSubsAdded.setStatus('current')
bTWagPreAuthenticatedS2aSubsAdded = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPreAuthenticatedS2aSubsAdded.setStatus('current')
bTWagS2aSubsDeletionsByDMinitiatedByPGW = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsDeletionsByDMinitiatedByPGW.setStatus('current')
bTWagS2aSubsGtpSessionCreateFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsGtpSessionCreateFailed.setStatus('current')
bTWagS2aSubsCSRQSendFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsCSRQSendFailed.setStatus('current')
bTWagS2aSubsInvalidGtpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsInvalidGtpVersion.setStatus('current')
bTWagS2aSubsRadiusMissingMandatoryParams = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsRadiusMissingMandatoryParams.setStatus('current')
bTWagS2aSubsRadiusInvalidPGWIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsRadiusInvalidPGWIPAddr.setStatus('current')
bTWagS2aSubsRadiusMSISDN = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsRadiusMSISDN.setStatus('current')
bTWagS2aSubsRadiusQoSProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsRadiusQoSProfile.setStatus('current')
bTWagS2aSubsRadiusGBRQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsRadiusGBRQoS.setStatus('current')
bTWagS2aSubsRadiusNonGBRQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsRadiusNonGBRQoS.setStatus('current')
bTWagS2aSubsGtpIPAddFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsGtpIPAddFailed.setStatus('current')
bTWagS2aSubsRadiusEapAkaHash = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 1, 3, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSubsRadiusEapAkaHash.setStatus('current')
bTWagS2aTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1), )
if mibBuilder.loadTexts: bTWagS2aTable.setStatus('current')
bTWagS2aEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1), ).setIndexNames((0, "BENU-TWAG-STATS-MIB", "bTWagS2aStatsInterval"))
if mibBuilder.loadTexts: bTWagS2aEntry.setStatus('current')
bTWagS2aStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bTWagS2aStatsInterval.setStatus('current')
bTWagS2aIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aIntervalDuration.setStatus('current')
bTWagS2aSessCreateReqSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSessCreateReqSent.setStatus('current')
bTWagS2aSessCreateRespRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSessCreateRespRcvd.setStatus('current')
bTWagS2aSessCreateRespAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSessCreateRespAccepted.setStatus('current')
bTWagS2aSessCreateRespRej = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSessCreateRespRej.setStatus('current')
bTWagS2aSessDelReqSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSessDelReqSent.setStatus('current')
bTWagS2aSessDelRespRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSessDelRespRcvd.setStatus('current')
bTWagS2aSessDelRespRejRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aSessDelRespRejRcvd.setStatus('current')
bTWagS2aDBRQRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aDBRQRcvd.setStatus('current')
bTWagS2aDBRPSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aDBRPSent.setStatus('current')
bTWagS2aCBRQRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aCBRQRcvd.setStatus('current')
bTWagS2aCBRPSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aCBRPSent.setStatus('current')
bTWagS2aUBRQRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aUBRQRcvd.setStatus('current')
bTWagS2aUBRPSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 3, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagS2aUBRPSent.setStatus('current')
bTWagGnGpSubscriberTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3), )
if mibBuilder.loadTexts: bTWagGnGpSubscriberTable.setStatus('current')
bTWagGnGpSubscriberEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1), ).setIndexNames((0, "BENU-TWAG-STATS-MIB", "bTWagGnGpSubsStatsInterval"))
if mibBuilder.loadTexts: bTWagGnGpSubscriberEntry.setStatus('current')
bTWagGnGpSubsStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 1), Integer32())
if mibBuilder.loadTexts: bTWagGnGpSubsStatsInterval.setStatus('current')
bTWagGnGpSubsIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsIntervalDuration.setStatus('current')
bTWagSecureSSIDGnGpSubsAdded = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagSecureSSIDGnGpSubsAdded.setStatus('current')
bTWagPreAuthenticatedGnGpSubsAdded = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagPreAuthenticatedGnGpSubsAdded.setStatus('current')
bTWagGnGpSubsDeletionsByDMinitiatedByGGSN = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsDeletionsByDMinitiatedByGGSN.setStatus('current')
bTWagGnGpSubsGtpSessionCreateFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsGtpSessionCreateFailed.setStatus('current')
bTWagGnGpSubsCPCRQSendFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsCPCRQSendFailed.setStatus('current')
bTWagGnGpSubsPDPCtxSendFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsPDPCtxSendFailed.setStatus('current')
bTWagGnGpSubsInvalidGtpVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsInvalidGtpVersion.setStatus('current')
bTWagGnGpSubsRadiusMissingMandatoryParams = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsRadiusMissingMandatoryParams.setStatus('current')
bTWagGnGpSubsRadiusInvalidGGSNIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsRadiusInvalidGGSNIPAddr.setStatus('current')
bTWagGnGpSubsRadiusMSISDN = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsRadiusMSISDN.setStatus('current')
bTWagGnGpSubsRadiusQoSProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsRadiusQoSProfile.setStatus('current')
bTWagGnGpSubsRadiusGBRQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsRadiusGBRQoS.setStatus('current')
bTWagGnGpSubsRadiusNonGBRQoS = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsRadiusNonGBRQoS.setStatus('current')
bTWagGnGpSubsGtpIPAddFailed = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 16), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsGtpIPAddFailed.setStatus('current')
bTWagGnGpSubsRadiusEapAkaHash = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 7, 3, 1, 17), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpSubsRadiusEapAkaHash.setStatus('current')
bTWagGnGpTable = MibTable((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1), )
if mibBuilder.loadTexts: bTWagGnGpTable.setStatus('current')
bTWagGnGpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1), ).setIndexNames((0, "BENU-TWAG-STATS-MIB", "bTWagGnGpStatsInterval"))
if mibBuilder.loadTexts: bTWagGnGpEntry.setStatus('current')
bTWagGnGpStatsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: bTWagGnGpStatsInterval.setStatus('current')
bTWagGnGpIntervalDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpIntervalDuration.setStatus('current')
bTWagGnGpCPCRQSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpCPCRQSent.setStatus('current')
bTWagGnGpCPCRPRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpCPCRPRcvd.setStatus('current')
bTWagGnGpCPCRPAccepted = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpCPCRPAccepted.setStatus('current')
bTWagGnGpCPCRPRej = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpCPCRPRej.setStatus('current')
bTWagGnGpDPCRQSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpDPCRQSent.setStatus('current')
bTWagGnGpDPCRPRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpDPCRPRcvd.setStatus('current')
bTWagGnGpDPCRPRejRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpDPCRPRejRcvd.setStatus('current')
bTWagGnGpDPCRQRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpDPCRQRcvd.setStatus('current')
bTWagGnGpDPCRPSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpDPCRPSent.setStatus('current')
bTWagGnGpCPCRQRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpCPCRQRcvd.setStatus('current')
bTWagGnGpCPCRPSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 13), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpCPCRPSent.setStatus('current')
bTWagGnGpUPCRQRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 14), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpUPCRQRcvd.setStatus('current')
bTWagGnGpUPCRPSent = MibTableColumn((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 9, 1, 1, 15), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bTWagGnGpUPCRPSent.setStatus('current')
bTWagGTPMaxNumOfTunnels = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 6, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bTWagGTPMaxNumOfTunnels.setStatus('current')
bTWagGTPHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 6, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bTWagGTPHighThreshold.setStatus('current')
bTWagGTPLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 6, 3), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bTWagGTPLowThreshold.setStatus('current')
bTWagGTPHighThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 0, 1)).setObjects(("BENU-TWAG-STATS-MIB", "bTWagGTPMaxNumOfTunnels"), ("BENU-TWAG-STATS-MIB", "bTWagGTPHighThreshold"))
if mibBuilder.loadTexts: bTWagGTPHighThresholdReached.setStatus('current')
bTWagGTPLowThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 7, 0, 2)).setObjects(("BENU-TWAG-STATS-MIB", "bTWagGTPMaxNumOfTunnels"), ("BENU-TWAG-STATS-MIB", "bTWagGTPLowThreshold"))
if mibBuilder.loadTexts: bTWagGTPLowThresholdReached.setStatus('current')
mibBuilder.exportSymbols("BENU-TWAG-STATS-MIB", bTWagPmip6TotalPacketsRxvdError=bTWagPmip6TotalPacketsRxvdError, bTWagGnGpSubscriberTable=bTWagGnGpSubscriberTable, bTWagS2aStatsMIBObjects=bTWagS2aStatsMIBObjects, bTWagPreAuthenticatedS2aSubsAdded=bTWagPreAuthenticatedS2aSubsAdded, bTWagS2aSubsRadiusGBRQoS=bTWagS2aSubsRadiusGBRQoS, bTWagS2aIntervalDuration=bTWagS2aIntervalDuration, bTWagS2aSessCreateReqSent=bTWagS2aSessCreateReqSent, bTWagGTPHighThresholdReached=bTWagGTPHighThresholdReached, bTWagS2aCBRPSent=bTWagS2aCBRPSent, bTWagS2aSubsStatsInterval=bTWagS2aSubsStatsInterval, bTWagGnGpIntervalDuration=bTWagGnGpIntervalDuration, bTWagGnGpCPCRPAccepted=bTWagGnGpCPCRPAccepted, bTWagGnGpStatsMIBObjects=bTWagGnGpStatsMIBObjects, bTWagS2aSubscriberNotifObjects=bTWagS2aSubscriberNotifObjects, bTWagGnGpSubsRadiusQoSProfile=bTWagGnGpSubsRadiusQoSProfile, bTWagGnGpDPCRPRcvd=bTWagGnGpDPCRPRcvd, bTWagS2aNotifObjects=bTWagS2aNotifObjects, bTWagS2aSessCreateRespRcvd=bTWagS2aSessCreateRespRcvd, bTWagGnGpDPCRPRejRcvd=bTWagGnGpDPCRPRejRcvd, bTWagGnGpDPCRQRcvd=bTWagGnGpDPCRQRcvd, bTWagGnGpSubscriberMIBObjects=bTWagGnGpSubscriberMIBObjects, bTWagNumPreAuthenticatedGnGpSubscribers=bTWagNumPreAuthenticatedGnGpSubscribers, bTWagGnGpUPCRQRcvd=bTWagGnGpUPCRQRcvd, bTWagPmip6HeartBeatReqRestartCountMismatch=bTWagPmip6HeartBeatReqRestartCountMismatch, bTWagS2aSessDelReqSent=bTWagS2aSessDelReqSent, bTWagPmip6DeletedDueToLmaInitBriMsg=bTWagPmip6DeletedDueToLmaInitBriMsg, bTWagGnGpSubsDeletionsByDMinitiatedByGGSN=bTWagGnGpSubsDeletionsByDMinitiatedByGGSN, bTWagPreAuthenticatedGnGpSubsAdded=bTWagPreAuthenticatedGnGpSubsAdded, bTWagPmip6TotalPbuSendError=bTWagPmip6TotalPbuSendError, bTWagS2aSubsInvalidGtpVersion=bTWagS2aSubsInvalidGtpVersion, bTWagGTPLowThreshold=bTWagGTPLowThreshold, bTWagGnGpSubsGtpSessionCreateFailed=bTWagGnGpSubsGtpSessionCreateFailed, bTWagS2aEntry=bTWagS2aEntry, bTWagPmip6TotalPacketHeaderDecodeError=bTWagPmip6TotalPacketHeaderDecodeError, bTWagS2aSessCreateRespAccepted=bTWagS2aSessCreateRespAccepted, bTWagGnGpNotifObjects=bTWagGnGpNotifObjects, bTWagS2aSubsRadiusInvalidPGWIPAddr=bTWagS2aSubsRadiusInvalidPGWIPAddr, bTWagGnGpUPCRPSent=bTWagGnGpUPCRPSent, bTWagGnGpSubsRadiusNonGBRQoS=bTWagGnGpSubsRadiusNonGBRQoS, bTWagS2aSubsIntervalDuration=bTWagS2aSubsIntervalDuration, bTWagPmip6HeartBeatReqSeqMismatch=bTWagPmip6HeartBeatReqSeqMismatch, bTWagNumCurrentSecureSSIDGnGpSubscribers=bTWagNumCurrentSecureSSIDGnGpSubscribers, bTWagNumGrePmip6Tunnels=bTWagNumGrePmip6Tunnels, bTWagSecureSSIDGnGpSubsAdded=bTWagSecureSSIDGnGpSubsAdded, bTWagNumPreAuthenticatedPmip6Subscribers=bTWagNumPreAuthenticatedPmip6Subscribers, benuTWagStatsMIB=benuTWagStatsMIB, bTWagGnGpTable=bTWagGnGpTable, bTWagGnGpSubscriberNotifObjects=bTWagGnGpSubscriberNotifObjects, bTWagPmip6StatsEntry=bTWagPmip6StatsEntry, bTWagPmip6TotalPbaReceived=bTWagPmip6TotalPbaReceived, bTWagGnGpDPCRPSent=bTWagGnGpDPCRPSent, bTWagS2aSessDelRespRejRcvd=bTWagS2aSessDelRespRejRcvd, bTWagS2aTable=bTWagS2aTable, bTWagNotifications=bTWagNotifications, bTWagS2aDBRPSent=bTWagS2aDBRPSent, bTWagPmip6TotalPbuSent=bTWagPmip6TotalPbuSent, bTWagS2aSubsGtpIPAddFailed=bTWagS2aSubsGtpIPAddFailed, bTWagGnGpSubscriberEntry=bTWagGnGpSubscriberEntry, bTWagPmip6TotalBraSent=bTWagPmip6TotalBraSent, bTWagS2aSubsRadiusQoSProfile=bTWagS2aSubsRadiusQoSProfile, bTWagS2aSubsRadiusMSISDN=bTWagS2aSubsRadiusMSISDN, bTWagGTPMaxNumOfTunnels=bTWagGTPMaxNumOfTunnels, bTWagPmip6StatsTable=bTWagPmip6StatsTable, bTWagNumCurrentSecureSSIDS2aSubscribers=bTWagNumCurrentSecureSSIDS2aSubscribers, bTWagGnGpSubsStatsInterval=bTWagGnGpSubsStatsInterval, bTWagGnGpSubsIntervalDuration=bTWagGnGpSubsIntervalDuration, bTWagGTPLowThresholdReached=bTWagGTPLowThresholdReached, bTWagPmip6IntervalDuration=bTWagPmip6IntervalDuration, bTWagPmip6MIBObjects=bTWagPmip6MIBObjects, bTWagGnGpSubsGtpIPAddFailed=bTWagGnGpSubsGtpIPAddFailed, bTWagS2aUBRQRcvd=bTWagS2aUBRQRcvd, bTWagS2aCBRQRcvd=bTWagS2aCBRQRcvd, bTWagGnGpSubsPDPCtxSendFailed=bTWagGnGpSubsPDPCtxSendFailed, bTWagGnGpCPCRPRcvd=bTWagGnGpCPCRPRcvd, bTWagGTPCurrentNumOfTunnels=bTWagGTPCurrentNumOfTunnels, bTWagS2aSubsRadiusNonGBRQoS=bTWagS2aSubsRadiusNonGBRQoS, bTWagGnGpCPCRPRej=bTWagGnGpCPCRPRej, bTWagGTPStatsMIBObjects=bTWagGTPStatsMIBObjects, bTWagS2aStatsInterval=bTWagS2aStatsInterval, bTWagS2aSubscriberTable=bTWagS2aSubscriberTable, bTWagPmip6TotalBriReceived=bTWagPmip6TotalBriReceived, bTWagS2aSubsRadiusEapAkaHash=bTWagS2aSubsRadiusEapAkaHash, bTWagGnGpSubsInvalidGtpVersion=bTWagGnGpSubsInvalidGtpVersion, bTWagPmip6HeartBeatReqSent=bTWagPmip6HeartBeatReqSent, bTWagGnGpSubsRadiusMSISDN=bTWagGnGpSubsRadiusMSISDN, bTWagGnGpCPCRPSent=bTWagGnGpCPCRPSent, PYSNMP_MODULE_ID=benuTWagStatsMIB, bTWagS2aSubsDeletionsByDMinitiatedByPGW=bTWagS2aSubsDeletionsByDMinitiatedByPGW, bTWagGnGpDPCRQSent=bTWagGnGpDPCRQSent, bTWagPmip6TotalPacketsRxvd=bTWagPmip6TotalPacketsRxvd, bTWagGnGpSubsRadiusEapAkaHash=bTWagGnGpSubsRadiusEapAkaHash, bTWagPmip6HeartBeatRspSent=bTWagPmip6HeartBeatRspSent, bTWagGnGpSubsRadiusInvalidGGSNIPAddr=bTWagGnGpSubsRadiusInvalidGGSNIPAddr, bTWagGnGpCPCRQSent=bTWagGnGpCPCRQSent, bTWagGTPHighThreshold=bTWagGTPHighThreshold, bTWagGnGpCPCRQRcvd=bTWagGnGpCPCRQRcvd, bTWagS2aSessCreateRespRej=bTWagS2aSessCreateRespRej, bTWagPmip6StatsInterval=bTWagPmip6StatsInterval, bTWagS2aUBRPSent=bTWagS2aUBRPSent, bTWagNumPreAuthenticatedS2aSubscribers=bTWagNumPreAuthenticatedS2aSubscribers, bTWagGnGpSubsRadiusMissingMandatoryParams=bTWagGnGpSubsRadiusMissingMandatoryParams, bTWagGnGpStatsInterval=bTWagGnGpStatsInterval, bTWagSecureSSIDS2aSubsAdded=bTWagSecureSSIDS2aSubsAdded, bTWagS2aDBRQRcvd=bTWagS2aDBRQRcvd, bTWagS2aSubscriberMIBObjects=bTWagS2aSubscriberMIBObjects, bTWagGnGpSubsCPCRQSendFailed=bTWagGnGpSubsCPCRQSendFailed, bTWagGTPNotifObjects=bTWagGTPNotifObjects, bTWagS2aSubscriberEntry=bTWagS2aSubscriberEntry, bTWagS2aSessDelRespRcvd=bTWagS2aSessDelRespRcvd, bTWagS2aSubsRadiusMissingMandatoryParams=bTWagS2aSubsRadiusMissingMandatoryParams, bTWagS2aSubsGtpSessionCreateFailed=bTWagS2aSubsGtpSessionCreateFailed, bTWagGnGpSubsRadiusGBRQoS=bTWagGnGpSubsRadiusGBRQoS, bTWagGnGpEntry=bTWagGnGpEntry, bTWagS2aSubsCSRQSendFailed=bTWagS2aSubsCSRQSendFailed)
