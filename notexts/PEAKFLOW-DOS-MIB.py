#
# PySNMP MIB module PEAKFLOW-DOS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arbornet/ARBORNET-PEAKFLOW-DOS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:37:35 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
arbornetworksProducts, = mibBuilder.importSymbols("ARBOR-SMI", "arbornetworksProducts")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ObjectIdentity, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, Unsigned32, NotificationType, Counter64, MibIdentifier, Gauge32, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ObjectIdentity", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "Unsigned32", "NotificationType", "Counter64", "MibIdentifier", "Gauge32", "ModuleIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
peakflowDosMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9694, 1, 1))
peakflowDosMIB.setRevisions(('2015-11-17 00:00', '2014-06-24 00:00', '2013-08-19 00:00', '2010-05-20 00:00', '2009-03-30 00:00', '2008-11-13 00:00', '2008-05-08 00:00', '2008-04-24 00:00', '2008-01-08 00:00', '2007-12-14 00:00', '2005-11-23 00:00', '2005-09-12 00:00', '2005-08-26 00:00', '2005-05-09 00:00', '2005-02-11 00:00', '2004-11-10 00:00', '2004-10-26 00:00', '2001-05-01 00:00',))
if mibBuilder.loadTexts: peakflowDosMIB.setLastUpdated('201406240000Z')
if mibBuilder.loadTexts: peakflowDosMIB.setOrganization('Arbor Networks, Inc.')
peakflowDosCMI = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1))
peakflowDosMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 1, 2))
peakflowDosTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3))
pdosUrl = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosUrl.setStatus('current')
pdosAnomalyId = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 2), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyId.setStatus('current')
pdosAnomalyDirection = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyDirection.setStatus('current')
pdosAnomalyResource = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyResource.setStatus('current')
pdosHeartbeatSource = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosHeartbeatSource.setStatus('obsolete')
internalErrorLocation = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: internalErrorLocation.setStatus('obsolete')
internalErrorReason = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: internalErrorReason.setStatus('obsolete')
pdosAnomalyProto = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 256))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyProto.setStatus('current')
pdosAnomalyLinkPercent = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 9), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyLinkPercent.setStatus('current')
pdosAnomalyAlertCnt = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 10), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyAlertCnt.setStatus('obsolete')
pdosAnomalyStart = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyStart.setStatus('current')
pdosAnomalyDuration = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 12), TimeTicks()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyDuration.setStatus('current')
pdosAnomalyTcpFlags = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyTcpFlags.setStatus('current')
pdosAnomalyRouter = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 14), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyRouter.setStatus('current')
pdosAnomalyRouterInterfaces = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyRouterInterfaces.setStatus('current')
pdosAnomalyClassification = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 16), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 8))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyClassification.setStatus('current')
pdosAnomalyIpVersion = MibScalar((1, 3, 6, 1, 4, 1, 9694, 1, 1, 1, 17), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: pdosAnomalyIpVersion.setStatus('current')
peakflowDosTrapsEnumerate = MibIdentifier((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0))
bandwidthAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 1)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: bandwidthAnomaly.setStatus('current')
tcpflagsAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 2)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
if mibBuilder.loadTexts: tcpflagsAnomaly.setStatus('obsolete')
protocolAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 3)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
if mibBuilder.loadTexts: protocolAnomaly.setStatus('current')
heartbeatLoss = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 4)).setObjects(("PEAKFLOW-DOS-MIB", "pdosHeartbeatSource"))
if mibBuilder.loadTexts: heartbeatLoss.setStatus('obsolete')
internalError = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 5)).setObjects(("PEAKFLOW-DOS-MIB", "internalErrorLocation"), ("PEAKFLOW-DOS-MIB", "internalErrorReason"))
if mibBuilder.loadTexts: internalError.setStatus('obsolete')
anomalyDone = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 6)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: anomalyDone.setStatus('current')
netflowMissing = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 7)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyRouter"))
if mibBuilder.loadTexts: netflowMissing.setStatus('obsolete')
netflowMissingDone = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 8)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyRouter"))
if mibBuilder.loadTexts: netflowMissingDone.setStatus('obsolete')
icmpMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 9)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
if mibBuilder.loadTexts: icmpMisuseAnomaly.setStatus('current')
tcpNullMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 10)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
if mibBuilder.loadTexts: tcpNullMisuseAnomaly.setStatus('current')
tcpSynMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 11)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
if mibBuilder.loadTexts: tcpSynMisuseAnomaly.setStatus('current')
ipNullMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 12)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: ipNullMisuseAnomaly.setStatus('current')
ipFragMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 13)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
if mibBuilder.loadTexts: ipFragMisuseAnomaly.setStatus('current')
ipPrivateMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 14)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: ipPrivateMisuseAnomaly.setStatus('current')
heartbeatLossDone = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 15)).setObjects(("PEAKFLOW-DOS-MIB", "pdosHeartbeatSource"))
if mibBuilder.loadTexts: heartbeatLossDone.setStatus('obsolete')
tcpRstMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 16)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyTcpFlags"))
if mibBuilder.loadTexts: tcpRstMisuseAnomaly.setStatus('current')
totalTrafficMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 17)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: totalTrafficMisuseAnomaly.setStatus('current')
fingerprintAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 18)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"))
if mibBuilder.loadTexts: fingerprintAnomaly.setStatus('current')
dnsMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 19)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
if mibBuilder.loadTexts: dnsMisuseAnomaly.setStatus('current')
udpMisuseAnomaly = NotificationType((1, 3, 6, 1, 4, 1, 9694, 1, 1, 3, 0, 20)).setObjects(("PEAKFLOW-DOS-MIB", "pdosAnomalyId"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDirection"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyIpVersion"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyResource"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyLinkPercent"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyClassification"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyStart"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyDuration"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyRouterInterfaces"), ("PEAKFLOW-DOS-MIB", "pdosUrl"), ("PEAKFLOW-DOS-MIB", "pdosAnomalyProto"))
if mibBuilder.loadTexts: udpMisuseAnomaly.setStatus('current')
mibBuilder.exportSymbols("PEAKFLOW-DOS-MIB", pdosAnomalyIpVersion=pdosAnomalyIpVersion, pdosAnomalyDuration=pdosAnomalyDuration, tcpSynMisuseAnomaly=tcpSynMisuseAnomaly, ipNullMisuseAnomaly=ipNullMisuseAnomaly, internalErrorLocation=internalErrorLocation, pdosAnomalyTcpFlags=pdosAnomalyTcpFlags, peakflowDosTraps=peakflowDosTraps, pdosAnomalyProto=pdosAnomalyProto, peakflowDosMgr=peakflowDosMgr, pdosAnomalyId=pdosAnomalyId, netflowMissingDone=netflowMissingDone, pdosAnomalyClassification=pdosAnomalyClassification, fingerprintAnomaly=fingerprintAnomaly, pdosUrl=pdosUrl, bandwidthAnomaly=bandwidthAnomaly, internalErrorReason=internalErrorReason, pdosAnomalyAlertCnt=pdosAnomalyAlertCnt, tcpNullMisuseAnomaly=tcpNullMisuseAnomaly, dnsMisuseAnomaly=dnsMisuseAnomaly, peakflowDosMIB=peakflowDosMIB, PYSNMP_MODULE_ID=peakflowDosMIB, pdosAnomalyResource=pdosAnomalyResource, anomalyDone=anomalyDone, heartbeatLoss=heartbeatLoss, peakflowDosCMI=peakflowDosCMI, totalTrafficMisuseAnomaly=totalTrafficMisuseAnomaly, pdosHeartbeatSource=pdosHeartbeatSource, ipPrivateMisuseAnomaly=ipPrivateMisuseAnomaly, pdosAnomalyDirection=pdosAnomalyDirection, protocolAnomaly=protocolAnomaly, heartbeatLossDone=heartbeatLossDone, udpMisuseAnomaly=udpMisuseAnomaly, pdosAnomalyLinkPercent=pdosAnomalyLinkPercent, tcpflagsAnomaly=tcpflagsAnomaly, internalError=internalError, ipFragMisuseAnomaly=ipFragMisuseAnomaly, pdosAnomalyStart=pdosAnomalyStart, netflowMissing=netflowMissing, tcpRstMisuseAnomaly=tcpRstMisuseAnomaly, peakflowDosTrapsEnumerate=peakflowDosTrapsEnumerate, pdosAnomalyRouterInterfaces=pdosAnomalyRouterInterfaces, icmpMisuseAnomaly=icmpMisuseAnomaly, pdosAnomalyRouter=pdosAnomalyRouter)
