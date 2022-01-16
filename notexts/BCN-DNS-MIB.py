#
# PySNMP MIB module BCN-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-DNS-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:32:27 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, Unsigned32, ObjectIdentity, TimeTicks, iso, Counter32, MibIdentifier, Counter64, IpAddress, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "ObjectIdentity", "TimeTicks", "iso", "Counter32", "MibIdentifier", "Counter64", "IpAddress", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bcnDnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 1))
bcnDnsMIB.setRevisions(('2010-11-30 12:00',))
if mibBuilder.loadTexts: bcnDnsMIB.setLastUpdated('201011301200Z')
if mibBuilder.loadTexts: bcnDnsMIB.setOrganization('BlueCat Networks')
bcnDns = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2))
bcnDnsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2))
bcnDnsNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3))
bcnDnsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4))
bcnDnsServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1))
if mibBuilder.loadTexts: bcnDnsServiceStatus.setStatus('current')
bcnDnsSerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("notRunning", 2), ("starting", 3), ("stopping", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerOperState.setStatus('current')
bcnDnsSerNumberOfZones = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerNumberOfZones.setStatus('current')
bcnDnsSerTransfersRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerTransfersRunning.setStatus('current')
bcnDnsSerTransfersDeferred = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerTransfersDeferred.setStatus('current')
bcnDnsSerSOAQueriesInProgress = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerSOAQueriesInProgress.setStatus('current')
bcnDnsSerQueryLogging = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerQueryLogging.setStatus('current')
bcnDnsSerDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerDebugLevel.setStatus('current')
bcnDnsServiceStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2))
if mibBuilder.loadTexts: bcnDnsServiceStatistics.setStatus('current')
bcnDnsStatServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1))
if mibBuilder.loadTexts: bcnDnsStatServer.setStatus('current')
bcnDnsStatSrvQrySuccess = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQrySuccess.setStatus('current')
bcnDnsStatSrvQryReferral = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQryReferral.setStatus('current')
bcnDnsStatSrvQryNXRRSet = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQryNXRRSet.setStatus('current')
bcnDnsStatSrvQryNXDomain = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQryNXDomain.setStatus('current')
bcnDnsStatSrvQryRecursion = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQryRecursion.setStatus('current')
bcnDnsStatSrvQryFailure = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQryFailure.setStatus('current')
bcnDnsNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 0))
bcnDnsNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 1))
bcnDnsAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDnsAlarmSeverity.setStatus('current')
bcnDnsAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDnsAlarmInfo.setStatus('current')
bcnDnsAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 0, 1)).setObjects(("BCN-DNS-MIB", "bcnDnsSerOperState"), ("BCN-DNS-MIB", "bcnDnsAlarmSeverity"), ("BCN-DNS-MIB", "bcnDnsAlarmInfo"))
if mibBuilder.loadTexts: bcnDnsAlarmNotif.setStatus('current')
bcnDnsServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 1))
bcnDnsServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2))
bcnDnsServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 1)).setObjects(("BCN-DNS-MIB", "bcnDnsSerOperState"), ("BCN-DNS-MIB", "bcnDnsSerNumberOfZones"), ("BCN-DNS-MIB", "bcnDnsSerTransfersRunning"), ("BCN-DNS-MIB", "bcnDnsSerTransfersDeferred"), ("BCN-DNS-MIB", "bcnDnsSerSOAQueriesInProgress"), ("BCN-DNS-MIB", "bcnDnsSerQueryLogging"), ("BCN-DNS-MIB", "bcnDnsSerDebugLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDnsServiceStatusGroup = bcnDnsServiceStatusGroup.setStatus('current')
bcnDnsServerStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 2)).setObjects(("BCN-DNS-MIB", "bcnDnsStatSrvQrySuccess"), ("BCN-DNS-MIB", "bcnDnsStatSrvQryReferral"), ("BCN-DNS-MIB", "bcnDnsStatSrvQryNXRRSet"), ("BCN-DNS-MIB", "bcnDnsStatSrvQryNXDomain"), ("BCN-DNS-MIB", "bcnDnsStatSrvQryRecursion"), ("BCN-DNS-MIB", "bcnDnsStatSrvQryFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDnsServerStatisticsGroup = bcnDnsServerStatisticsGroup.setStatus('current')
bcnDnsNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 3)).setObjects(("BCN-DNS-MIB", "bcnDnsAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDnsNotificationEventGroup = bcnDnsNotificationEventGroup.setStatus('current')
bcnDnsNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 4)).setObjects(("BCN-DNS-MIB", "bcnDnsAlarmSeverity"), ("BCN-DNS-MIB", "bcnDnsAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDnsNotificationDataGroup = bcnDnsNotificationDataGroup.setStatus('current')
bcnDnsStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 1, 1)).setObjects(("BCN-DNS-MIB", "bcnDnsServiceStatusGroup"), ("BCN-DNS-MIB", "bcnDnsServerStatisticsGroup"), ("BCN-DNS-MIB", "bcnDnsNotificationEventGroup"), ("BCN-DNS-MIB", "bcnDnsNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDnsStatusCompliance = bcnDnsStatusCompliance.setStatus('current')
mibBuilder.exportSymbols("BCN-DNS-MIB", PYSNMP_MODULE_ID=bcnDnsMIB, bcnDnsObjects=bcnDnsObjects, bcnDnsSerQueryLogging=bcnDnsSerQueryLogging, bcnDnsStatServer=bcnDnsStatServer, bcnDnsStatSrvQryReferral=bcnDnsStatSrvQryReferral, bcnDnsSerOperState=bcnDnsSerOperState, bcnDnsStatSrvQryRecursion=bcnDnsStatSrvQryRecursion, bcnDns=bcnDns, bcnDnsServerStatisticsGroup=bcnDnsServerStatisticsGroup, bcnDnsServiceCompliances=bcnDnsServiceCompliances, bcnDnsSerSOAQueriesInProgress=bcnDnsSerSOAQueriesInProgress, bcnDnsStatSrvQryNXDomain=bcnDnsStatSrvQryNXDomain, bcnDnsStatSrvQryFailure=bcnDnsStatSrvQryFailure, bcnDnsServiceStatus=bcnDnsServiceStatus, bcnDnsAlarmSeverity=bcnDnsAlarmSeverity, bcnDnsNotification=bcnDnsNotification, bcnDnsAlarmInfo=bcnDnsAlarmInfo, bcnDnsServiceGroups=bcnDnsServiceGroups, bcnDnsNotificationEventGroup=bcnDnsNotificationEventGroup, bcnDnsStatusCompliance=bcnDnsStatusCompliance, bcnDnsConformance=bcnDnsConformance, bcnDnsSerNumberOfZones=bcnDnsSerNumberOfZones, bcnDnsSerTransfersDeferred=bcnDnsSerTransfersDeferred, bcnDnsAlarmNotif=bcnDnsAlarmNotif, bcnDnsNotificationDataGroup=bcnDnsNotificationDataGroup, bcnDnsServiceStatistics=bcnDnsServiceStatistics, bcnDnsNotificationData=bcnDnsNotificationData, bcnDnsStatSrvQryNXRRSet=bcnDnsStatSrvQryNXRRSet, bcnDnsSerTransfersRunning=bcnDnsSerTransfersRunning, bcnDnsSerDebugLevel=bcnDnsSerDebugLevel, bcnDnsMIB=bcnDnsMIB, bcnDnsNotificationEvents=bcnDnsNotificationEvents, bcnDnsServiceStatusGroup=bcnDnsServiceStatusGroup, bcnDnsStatSrvQrySuccess=bcnDnsStatSrvQrySuccess)
