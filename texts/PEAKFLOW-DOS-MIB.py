#
# PySNMP MIB module PEAKFLOW-DOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arbornet/ARBORNET-PEAKFLOW-DOS-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:51:40 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
arbornetworksProducts, = mibBuilder.importSymbols("ARBOR-SMI", "arbornetworksProducts")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Counter64, ObjectIdentity, IpAddress, Unsigned32, TimeTicks, NotificationType, Gauge32, iso, Counter32, Bits, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "ObjectIdentity", "IpAddress", "Unsigned32", "TimeTicks", "NotificationType", "Gauge32", "iso", "Counter32", "Bits", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
peakflowDosMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9694, 1, 1))
peakflowDosMIB.setRevisions(('2015-11-17 00:00', '2014-06-24 00:00', '2013-08-19 00:00', '2010-05-20 00:00', '2009-03-30 00:00', '2008-11-13 00:00', '2008-05-08 00:00', '2008-04-24 00:00', '2008-01-08 00:00', '2007-12-14 00:00', '2005-11-23 00:00', '2005-09-12 00:00', '2005-08-26 00:00', '2005-05-09 00:00', '2005-02-11 00:00', '2004-11-10 00:00', '2004-10-26 00:00', '2001-05-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: peakflowDosMIB.setRevisionsDescriptions(('Add pdosAnomalyIpVersion to Anomaly notifications', 'Add pdosAnomalyIpVersion', 'Updated contact information', 'Correct values of max-access for objets.', 'Update contact group name.', 'Update company address.', 'Updated SIZE of pdosAnomalyTcpFlags to be (0..8).', 'Add pdosAnomalyProto to dnsMisuseAnomaly trap', 'Clean up use of pdosAnomalyProto and pdosTcpFlags', 'Add udpMisuseAnomaly.', 'Update status of obsolete OIDs.', 'Apply fixes from validation.', 'Adjust trap variable order to match what is sent.', 'Add pdosAnomalyClassification to add DoS alert\n\t\t     classification.', 'Increase size of interfaces entry from 512 to 1024\n\t\t     characters', 'Add pdosAnomalyRouterInterfacesChange to add input/output\n\t\t     interfaces.', 'Change pdosAnomalyLinkPercent to an Unsigned32 with no\n\t\t     range support.', 'Initial writing and import.',))
if mibBuilder.loadTexts: peakflowDosMIB.setLastUpdated('201406240000Z')
if mibBuilder.loadTexts: peakflowDosMIB.setOrganization('Arbor Networks, Inc.')
if mibBuilder.loadTexts: peakflowDosMIB.setContactInfo('\tArbor Networks, Inc.\n\t\t\tArbor Technical Assistance Center\n\n\t\t\tPostal: 76 Blanchard Road\n\t\t\t\tBurlington, MA 01803\n\t\t\t\tUSA\n\n\t\t\tTel: +1 866 212 7267 (toll free)\n\t\t\t     +1 781 362 4300\n\t\t\tEmail: support@arbor.net ')
if mibBuilder.loadTexts: peakflowDosMIB.setDescription('Peakflow DoS MIB')
peakflowDosCMI = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1))
peakflowDosMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 1, 2))
peakflowDosTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3))
pdosUrl = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosUrl.setStatus('current')
if mibBuilder.loadTexts: pdosUrl.setDescription('This URL is a back reference to the Peakflow SP leader\n\t\tthat has details about the anomaly.')
pdosAnomalyId = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyId.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyId.setDescription('Identifies the Peakflow anomaly')
pdosAnomalyDirection = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyDirection.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyDirection.setDescription('Description of anomaly direction')
pdosAnomalyResource = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyResource.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyResource.setDescription('Description of anomaly resource')
pdosHeartbeatSource = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosHeartbeatSource.setStatus('obsolete')
if mibBuilder.loadTexts: pdosHeartbeatSource.setDescription('Describes the collection which lost heartbeat')
internalErrorLocation = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: internalErrorLocation.setStatus('obsolete')
if mibBuilder.loadTexts: internalErrorLocation.setDescription('Describes the location of the internal error')
internalErrorReason = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: internalErrorReason.setStatus('obsolete')
if mibBuilder.loadTexts: internalErrorReason.setDescription('Describes the location of the internal error')
pdosAnomalyProto = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyProto.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyProto.setDescription('IP protocols associated with the anomaly')
pdosAnomalyLinkPercent = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 9), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyLinkPercent.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyLinkPercent.setDescription('Percent of link usage by an anomaly')
pdosAnomalyAlertCnt = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 10), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyAlertCnt.setStatus('obsolete')
if mibBuilder.loadTexts: pdosAnomalyAlertCnt.setDescription('Number of times a notification has been issued\n\t\tfor this anomaly')
pdosAnomalyStart = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyStart.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyStart.setDescription('Textual description of the time the anomaly started')
pdosAnomalyDuration = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 12), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyDuration.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyDuration.setDescription('Duration (in centiseconds) since the start of the\n\t\tanomaly')
pdosAnomalyTcpFlags = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyTcpFlags.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyTcpFlags.setDescription('TCP flags associated with the anomaly signature')
pdosAnomalyRouter = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 14), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyRouter.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyRouter.setDescription('The router which is either not sending NetFlow\n\t\tor has resumed sending NetFlow')
pdosAnomalyRouterInterfaces = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyRouterInterfaces.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyRouterInterfaces.setDescription('Router interfaces involved in the anomaly')
pdosAnomalyClassification = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyClassification.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyClassification.setDescription('Classification of the anomaly -- high, medium, or low.')
pdosAnomalyIpVersion = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 17), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyIpVersion.setStatus('current')
if mibBuilder.loadTexts: pdosAnomalyIpVersion.setDescription('IP version of the anomaly')
peakflowDosTrapsEnumerate = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0))
bandwidthAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 1)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: bandwidthAnomaly.setStatus('current')
if mibBuilder.loadTexts: bandwidthAnomaly.setDescription('Bandwidth anomaly detected by Peakflow')
tcpflagsAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 2)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
if mibBuilder.loadTexts: tcpflagsAnomaly.setStatus('obsolete')
if mibBuilder.loadTexts: tcpflagsAnomaly.setDescription('TCP flags anomaly detected by Peakflow')
protocolAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 3)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
if mibBuilder.loadTexts: protocolAnomaly.setStatus('current')
if mibBuilder.loadTexts: protocolAnomaly.setDescription('Protocol anomaly detected by Peakflow')
heartbeatLoss = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 4)).setObjects(("PEAKFLOW-DOS-MIB", "pdosHeartbeatSource"))
if mibBuilder.loadTexts: heartbeatLoss.setStatus('obsolete')
if mibBuilder.loadTexts: heartbeatLoss.setDescription('Missing heartbeat from SP device to leader')
internalError = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 5)).setObjects(("PEAKFLOW-DOS-MIB", "internalErrorLocation"), ("PEAKFLOW-DOS-MIB", "internalErrorReason"))
if mibBuilder.loadTexts: internalError.setStatus('obsolete')
if mibBuilder.loadTexts: internalError.setDescription('Internal inconsistency or error')
anomalyDone = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 6)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: anomalyDone.setStatus('current')
if mibBuilder.loadTexts: anomalyDone.setDescription('Some previously detected anomaly is no longer active')
netflowMissing = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 7)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyRouter"))
if mibBuilder.loadTexts: netflowMissing.setStatus('obsolete')
if mibBuilder.loadTexts: netflowMissing.setDescription('NetFlow has not been received from a NetFlow\n\t\ttransmitting router')
netflowMissingDone = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 8)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyRouter"))
if mibBuilder.loadTexts: netflowMissingDone.setStatus('obsolete')
if mibBuilder.loadTexts: netflowMissingDone.setDescription('NetFlow has resumed from a router which previously\n\t\twas not forwarding NetFlow data')
icmpMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 9)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
if mibBuilder.loadTexts: icmpMisuseAnomaly.setStatus('current')
if mibBuilder.loadTexts: icmpMisuseAnomaly.setDescription('ICMP misuse anomaly detected by Peakflow')
tcpNullMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 10)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
if mibBuilder.loadTexts: tcpNullMisuseAnomaly.setStatus('current')
if mibBuilder.loadTexts: tcpNullMisuseAnomaly.setDescription('TCP Null misuse anomaly detected by Peakflow')
tcpSynMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 11)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
if mibBuilder.loadTexts: tcpSynMisuseAnomaly.setStatus('current')
if mibBuilder.loadTexts: tcpSynMisuseAnomaly.setDescription('TCP SYN misuse anomaly detected by Peakflow')
ipNullMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 12)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: ipNullMisuseAnomaly.setStatus('current')
if mibBuilder.loadTexts: ipNullMisuseAnomaly.setDescription('IP Null misuse anomaly detected by Peakflow')
ipFragMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 13)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
if mibBuilder.loadTexts: ipFragMisuseAnomaly.setStatus('current')
if mibBuilder.loadTexts: ipFragMisuseAnomaly.setDescription('IP Fragment misuse anomaly detected by Peakflow')
ipPrivateMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 14)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: ipPrivateMisuseAnomaly.setStatus('current')
if mibBuilder.loadTexts: ipPrivateMisuseAnomaly.setDescription('IP Private misuse anomaly detected by Peakflow')
heartbeatLossDone = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 15)).setObjects(("PEAKFLOW-DOS-MIB", "pdosHeartbeatSource"))
if mibBuilder.loadTexts: heartbeatLossDone.setStatus('obsolete')
if mibBuilder.loadTexts: heartbeatLossDone.setDescription('Heartbeat from SP device to leader now works')
tcpRstMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 16)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
if mibBuilder.loadTexts: tcpRstMisuseAnomaly.setStatus('current')
if mibBuilder.loadTexts: tcpRstMisuseAnomaly.setDescription('TCP RST misuse anomaly detected by Peakflow')
totalTrafficMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 17)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: totalTrafficMisuseAnomaly.setStatus('current')
if mibBuilder.loadTexts: totalTrafficMisuseAnomaly.setDescription('Total Traffic misuse anomaly detected by Peakflow')
fingerprintAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 18)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: fingerprintAnomaly.setStatus('current')
if mibBuilder.loadTexts: fingerprintAnomaly.setDescription('Fingerprint anomaly detected by Peakflow')
dnsMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 19)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
if mibBuilder.loadTexts: dnsMisuseAnomaly.setStatus('current')
if mibBuilder.loadTexts: dnsMisuseAnomaly.setDescription('DNS misuse anomaly detected by Peakflow')
udpMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 20)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
if mibBuilder.loadTexts: udpMisuseAnomaly.setStatus('current')
if mibBuilder.loadTexts: udpMisuseAnomaly.setDescription('UDP misuse anomaly detected by Peakflow')
mibBuilder.exportSymbols("PEAKFLOW-DOS-MIB", ipNullMisuseAnomaly=ipNullMisuseAnomaly, ipFragMisuseAnomaly=ipFragMisuseAnomaly, pdosAnomalyLinkPercent=pdosAnomalyLinkPercent, pdosUrl=pdosUrl, tcpRstMisuseAnomaly=tcpRstMisuseAnomaly, tcpSynMisuseAnomaly=tcpSynMisuseAnomaly, pdosAnomalyDirection=pdosAnomalyDirection, peakflowDosTrapsEnumerate=peakflowDosTrapsEnumerate, tcpflagsAnomaly=tcpflagsAnomaly, icmpMisuseAnomaly=icmpMisuseAnomaly, tcpNullMisuseAnomaly=tcpNullMisuseAnomaly, heartbeatLossDone=heartbeatLossDone, peakflowDosMIB=peakflowDosMIB, fingerprintAnomaly=fingerprintAnomaly, bandwidthAnomaly=bandwidthAnomaly, protocolAnomaly=protocolAnomaly, netflowMissing=netflowMissing, peakflowDosMgr=peakflowDosMgr, pdosAnomalyId=pdosAnomalyId, udpMisuseAnomaly=udpMisuseAnomaly, peakflowDosCMI=peakflowDosCMI, pdosAnomalyRouterInterfaces=pdosAnomalyRouterInterfaces, dnsMisuseAnomaly=dnsMisuseAnomaly, netflowMissingDone=netflowMissingDone, internalErrorLocation=internalErrorLocation, pdosAnomalyIpVersion=pdosAnomalyIpVersion, pdosAnomalyStart=pdosAnomalyStart, pdosAnomalyAlertCnt=pdosAnomalyAlertCnt, peakflowDosTraps=peakflowDosTraps, pdosAnomalyResource=pdosAnomalyResource, pdosAnomalyTcpFlags=pdosAnomalyTcpFlags, heartbeatLoss=heartbeatLoss, internalErrorReason=internalErrorReason, pdosAnomalyProto=pdosAnomalyProto, pdosAnomalyClassification=pdosAnomalyClassification, anomalyDone=anomalyDone, pdosAnomalyDuration=pdosAnomalyDuration, ipPrivateMisuseAnomaly=ipPrivateMisuseAnomaly, internalError=internalError, pdosHeartbeatSource=pdosHeartbeatSource, pdosAnomalyRouter=pdosAnomalyRouter, PYSNMP_MODULE_ID=peakflowDosMIB, totalTrafficMisuseAnomaly=totalTrafficMisuseAnomaly)
