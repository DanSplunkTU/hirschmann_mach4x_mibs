#
# PySNMP MIB module BCN-DNS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-DNS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:41:27 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, ModuleIdentity, Gauge32, Counter32, IpAddress, Integer32, TimeTicks, iso, NotificationType, ObjectIdentity, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "ModuleIdentity", "Gauge32", "Counter32", "IpAddress", "Integer32", "TimeTicks", "iso", "NotificationType", "ObjectIdentity", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
bcnDnsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 1))
bcnDnsMIB.setRevisions(('2010-11-30 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcnDnsMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bcnDnsMIB.setLastUpdated('201011301200Z')
if mibBuilder.loadTexts: bcnDnsMIB.setOrganization('BlueCat Networks')
if mibBuilder.loadTexts: bcnDnsMIB.setContactInfo('BlueCat Networks. Customer Care.\n\n        North America\n        Call: +1.866.491.2228\n        Europe\n        Call: +44.8081.011.306\n        Other\n        Call: +1.416.646.8433\n        \n        Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bcnDnsMIB.setDescription('This module provides status as well as statistical information\n        about the DNS service.')
bcnDns = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2))
bcnDnsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2))
bcnDnsNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3))
bcnDnsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4))
bcnDnsServiceStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1))
if mibBuilder.loadTexts: bcnDnsServiceStatus.setStatus('current')
if mibBuilder.loadTexts: bcnDnsServiceStatus.setDescription('General state of the DNS Service.')
bcnDnsSerOperState = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("running", 1), ("notRunning", 2), ("starting", 3), ("stopping", 4), ("fault", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerOperState.setStatus('current')
if mibBuilder.loadTexts: bcnDnsSerOperState.setDescription('Operational state of the Service. The possible states are:\n        running(1)    The service is running normally.\n        notRunning(2) The service is stopped either intentionally (i.e.:\n                      the service is not supposed to run on this node) or\n                      unintentionally (a problem has occurred).\n        starting(3)   The service is in the process of starting, either\n                      for the first time of after an event occurred.\n        stopping(4)   The service is in the process of stopping. Stopping\n                      a service might be necessary after a configuration\n                      change.\n        fault(5)      An error has been detected and the state is undefined.\n        ')
bcnDnsSerNumberOfZones = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerNumberOfZones.setStatus('current')
if mibBuilder.loadTexts: bcnDnsSerNumberOfZones.setDescription('Number of zones loaded.')
bcnDnsSerTransfersRunning = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerTransfersRunning.setStatus('current')
if mibBuilder.loadTexts: bcnDnsSerTransfersRunning.setDescription('Number of zone transfers currently in progress.')
bcnDnsSerTransfersDeferred = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerTransfersDeferred.setStatus('current')
if mibBuilder.loadTexts: bcnDnsSerTransfersDeferred.setDescription('Number of zone transfers currently deferred.')
bcnDnsSerSOAQueriesInProgress = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerSOAQueriesInProgress.setStatus('current')
if mibBuilder.loadTexts: bcnDnsSerSOAQueriesInProgress.setDescription('Number of SOA queries in progress.')
bcnDnsSerQueryLogging = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerQueryLogging.setStatus('current')
if mibBuilder.loadTexts: bcnDnsSerQueryLogging.setDescription('State of query logging. The possible values are on(1) or off(2).')
bcnDnsSerDebugLevel = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsSerDebugLevel.setStatus('current')
if mibBuilder.loadTexts: bcnDnsSerDebugLevel.setDescription('Debug log level. The possible values range from 0 to 99.\n        Where 0 indicates no logging and 99 is the maximum level of logging.')
bcnDnsServiceStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2))
if mibBuilder.loadTexts: bcnDnsServiceStatistics.setStatus('current')
if mibBuilder.loadTexts: bcnDnsServiceStatistics.setDescription('DNS statistics objects container')
bcnDnsStatServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1))
if mibBuilder.loadTexts: bcnDnsStatServer.setStatus('current')
if mibBuilder.loadTexts: bcnDnsStatServer.setDescription('DNS server statistics objects container')
bcnDnsStatSrvQrySuccess = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQrySuccess.setStatus('current')
if mibBuilder.loadTexts: bcnDnsStatSrvQrySuccess.setDescription('Queries resulted in a successful answer.')
bcnDnsStatSrvQryReferral = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQryReferral.setStatus('current')
if mibBuilder.loadTexts: bcnDnsStatSrvQryReferral.setDescription('Queries resulted in referral answer.')
bcnDnsStatSrvQryNXRRSet = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQryNXRRSet.setStatus('current')
if mibBuilder.loadTexts: bcnDnsStatSrvQryNXRRSet.setDescription('Queries resulted in non-existent record responses with no data.')
bcnDnsStatSrvQryNXDomain = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQryNXDomain.setStatus('current')
if mibBuilder.loadTexts: bcnDnsStatSrvQryNXDomain.setDescription('Queries resulted in non-existent domain responses with no data.')
bcnDnsStatSrvQryRecursion = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQryRecursion.setStatus('current')
if mibBuilder.loadTexts: bcnDnsStatSrvQryRecursion.setDescription('Queries which caused the server to perform recursion lookups in\n        order to find the final answer.')
bcnDnsStatSrvQryFailure = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnDnsStatSrvQryFailure.setStatus('current')
if mibBuilder.loadTexts: bcnDnsStatSrvQryFailure.setDescription('Number of failed queries that did not result in non-existent\n        domain or record.')
bcnDnsNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 0))
bcnDnsNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 1))
bcnDnsAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDnsAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: bcnDnsAlarmSeverity.setDescription('Severity classification for the alarm.')
bcnDnsAlarmInfo = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 1, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnDnsAlarmInfo.setStatus('current')
if mibBuilder.loadTexts: bcnDnsAlarmInfo.setDescription('Descriptive information about the alarm event.')
bcnDnsAlarmNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 3, 0, 1)).setObjects(("BCN-DNS-MIB", "bcnDnsSerOperState"), ("BCN-DNS-MIB", "bcnDnsAlarmSeverity"), ("BCN-DNS-MIB", "bcnDnsAlarmInfo"))
if mibBuilder.loadTexts: bcnDnsAlarmNotif.setStatus('current')
if mibBuilder.loadTexts: bcnDnsAlarmNotif.setDescription('A bcnDnsAlarmNotif signifies that the DNS service has transitioned\n        state or a particular event has been detected on the service.')
bcnDnsServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 1))
bcnDnsServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2))
bcnDnsServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 1)).setObjects(("BCN-DNS-MIB", "bcnDnsSerOperState"), ("BCN-DNS-MIB", "bcnDnsSerNumberOfZones"), ("BCN-DNS-MIB", "bcnDnsSerTransfersRunning"), ("BCN-DNS-MIB", "bcnDnsSerTransfersDeferred"), ("BCN-DNS-MIB", "bcnDnsSerSOAQueriesInProgress"), ("BCN-DNS-MIB", "bcnDnsSerQueryLogging"), ("BCN-DNS-MIB", "bcnDnsSerDebugLevel"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDnsServiceStatusGroup = bcnDnsServiceStatusGroup.setStatus('current')
if mibBuilder.loadTexts: bcnDnsServiceStatusGroup.setDescription('Status conformance.')
bcnDnsServerStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 2)).setObjects(("BCN-DNS-MIB", "bcnDnsStatSrvQrySuccess"), ("BCN-DNS-MIB", "bcnDnsStatSrvQryReferral"), ("BCN-DNS-MIB", "bcnDnsStatSrvQryNXRRSet"), ("BCN-DNS-MIB", "bcnDnsStatSrvQryNXDomain"), ("BCN-DNS-MIB", "bcnDnsStatSrvQryRecursion"), ("BCN-DNS-MIB", "bcnDnsStatSrvQryFailure"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDnsServerStatisticsGroup = bcnDnsServerStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: bcnDnsServerStatisticsGroup.setDescription('Server statistics conformance.')
bcnDnsNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 3)).setObjects(("BCN-DNS-MIB", "bcnDnsAlarmNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDnsNotificationEventGroup = bcnDnsNotificationEventGroup.setStatus('current')
if mibBuilder.loadTexts: bcnDnsNotificationEventGroup.setDescription('Server statistics conformance.')
bcnDnsNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 2, 4)).setObjects(("BCN-DNS-MIB", "bcnDnsAlarmSeverity"), ("BCN-DNS-MIB", "bcnDnsAlarmInfo"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDnsNotificationDataGroup = bcnDnsNotificationDataGroup.setStatus('current')
if mibBuilder.loadTexts: bcnDnsNotificationDataGroup.setDescription('Server statistics conformance.')
bcnDnsStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 2, 4, 1, 1)).setObjects(("BCN-DNS-MIB", "bcnDnsServiceStatusGroup"), ("BCN-DNS-MIB", "bcnDnsServerStatisticsGroup"), ("BCN-DNS-MIB", "bcnDnsNotificationEventGroup"), ("BCN-DNS-MIB", "bcnDnsNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnDnsStatusCompliance = bcnDnsStatusCompliance.setStatus('current')
if mibBuilder.loadTexts: bcnDnsStatusCompliance.setDescription('Basic conformance')
mibBuilder.exportSymbols("BCN-DNS-MIB", bcnDnsStatSrvQrySuccess=bcnDnsStatSrvQrySuccess, bcnDnsNotification=bcnDnsNotification, bcnDnsStatSrvQryReferral=bcnDnsStatSrvQryReferral, bcnDnsConformance=bcnDnsConformance, bcnDnsStatServer=bcnDnsStatServer, bcnDnsSerTransfersDeferred=bcnDnsSerTransfersDeferred, bcnDnsNotificationDataGroup=bcnDnsNotificationDataGroup, bcnDnsServiceGroups=bcnDnsServiceGroups, bcnDnsServiceStatusGroup=bcnDnsServiceStatusGroup, bcnDnsStatSrvQryNXDomain=bcnDnsStatSrvQryNXDomain, bcnDnsServiceCompliances=bcnDnsServiceCompliances, bcnDnsStatusCompliance=bcnDnsStatusCompliance, bcnDnsSerOperState=bcnDnsSerOperState, bcnDnsServerStatisticsGroup=bcnDnsServerStatisticsGroup, bcnDnsSerDebugLevel=bcnDnsSerDebugLevel, bcnDnsObjects=bcnDnsObjects, bcnDnsNotificationEvents=bcnDnsNotificationEvents, bcnDnsMIB=bcnDnsMIB, bcnDnsAlarmInfo=bcnDnsAlarmInfo, bcnDnsAlarmSeverity=bcnDnsAlarmSeverity, bcnDnsStatSrvQryNXRRSet=bcnDnsStatSrvQryNXRRSet, bcnDnsNotificationData=bcnDnsNotificationData, bcnDnsStatSrvQryRecursion=bcnDnsStatSrvQryRecursion, bcnDnsServiceStatistics=bcnDnsServiceStatistics, bcnDns=bcnDns, bcnDnsSerNumberOfZones=bcnDnsSerNumberOfZones, bcnDnsNotificationEventGroup=bcnDnsNotificationEventGroup, bcnDnsSerSOAQueriesInProgress=bcnDnsSerSOAQueriesInProgress, PYSNMP_MODULE_ID=bcnDnsMIB, bcnDnsServiceStatus=bcnDnsServiceStatus, bcnDnsSerTransfersRunning=bcnDnsSerTransfersRunning, bcnDnsSerQueryLogging=bcnDnsSerQueryLogging, bcnDnsAlarmNotif=bcnDnsAlarmNotif, bcnDnsStatSrvQryFailure=bcnDnsStatSrvQryFailure)
