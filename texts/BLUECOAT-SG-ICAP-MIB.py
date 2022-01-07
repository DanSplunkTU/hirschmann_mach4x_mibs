#
# PySNMP MIB module BLUECOAT-SG-ICAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecoat/BLUECOAT-SG-ICAP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:55:39 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, TimeTicks, ModuleIdentity, Counter32, Unsigned32, Integer32, ObjectIdentity, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "TimeTicks", "ModuleIdentity", "Counter32", "Unsigned32", "Integer32", "ObjectIdentity", "Bits", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
bluecoatSGICAPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 14))
bluecoatSGICAPMIB.setRevisions(('2013-02-08 14:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bluecoatSGICAPMIB.setRevisionsDescriptions(('Initial revision of this MIB.',))
if mibBuilder.loadTexts: bluecoatSGICAPMIB.setLastUpdated('201302081400Z')
if mibBuilder.loadTexts: bluecoatSGICAPMIB.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: bluecoatSGICAPMIB.setContactInfo('support.services@bluecoat.com\n                         http://www.bluecoat.com')
if mibBuilder.loadTexts: bluecoatSGICAPMIB.setDescription('Internet Content Adaptation Protocol (ICAP) is an open standard protocol that\n\t\t\t  allows content engines to send HTTP-based content to an ICAP server for\n\t\t\t  performing value added services. The ProxySG appliance, when integrated with a \n\t\t\t  supported ICAP server such as the Proxy-AV, provides content scanning, \n\t\t\t  filtering, and repair service for Internet-based malicious code, in addition \n\t\t\t  to reducing bandwidth usage and latency.\n\n\t                 This is the MIB module for ProxySG ICAP feature.')
bluecoatSgICAPMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1))
bluecoatSgICAPMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 2))
sgICAPMIBNotificationsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 2, 0))
bluecoatSgICAPMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3))
class ICAPServiceEntityType(TextualConvention, Integer32):
    description = 'In the ProxySG appliance, an ICAP service is a collection of attributes that\n             defines the communication between the appliance and the \n             ICAP server. Similar ICAP scanning services can then be\n             grouped together to create a service group that helps \n             to distribute and load balance scanning requests. \n\t     \n             This data type distinguishes an ICAP service entity \n             between a service group and service.\n\n             service (1)      - A single service entity which may or \n                                may not be part a service group\n\n\t     serviceGroup (2) - a collection of services of same type \n\t                        of operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("service", 1), ("servivceGroup", 2))

class ICAPServiceNotificationType(TextualConvention, Integer32):
    description = 'This TC enumerates an event related to ProxySG ICAP service. \n             The events are sent as part of ICAP service notification. \n             The events include:\n\n  \t     queuedRequestsAboveThreshold(1) - The number of queued \n  \t         ICAP requests for a service has gone above the \n  \t         permissible threshold. This event denotes an impending \n  \t         service impact for new requests. New requests may \n  \t         be rejected and can cause serviceability issues for \n  \t         users. This problem usually occur because there is \n  \t         insufficient number of ICAP connections for the load \n  \t         the ProxySG is handling.\n\n          queuedRequestsBelowThreshold(2) - The number of queued \n             ICAP requests has fallen below the alert \n             threshold. This event indicates that the number of \n             queued requests is now within normal limits and that \n             the ICAP service has returned to a healthy state.\n\n          deferredRequestsAboveThreshold(3) - The number of \n             deferred requests for a service has gone above the \n             permissible threshold. This event denotes an impending \n             service impact for new connections.\n\n          deferredRequestsBelowThreshold(4) - The number of \n             deferred ICAP requests has fallen below the \n             threshold. This event indicates that the number of \n             deferred ICAP requests is now within normal limits \n             and that the ICAP service has returned to a healthy \n             state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("queuedRequestsAboveThreshold", 1), ("queuedRequestsBelowThreshold", 2), ("deferredRequestsAboveThreshold", 3), ("deferredRequestsBelowThreshold", 4))

bluecoatSgICAPValues = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1))
icapService = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1))
icapServiceStatsTable = MibTable((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1), )
if mibBuilder.loadTexts: icapServiceStatsTable.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsTable.setDescription('This table represents various operational \n        \t\tstatistics of ICAP services and service groups in \n        \t\tan ProxySG appliance.')
icapServiceStatsTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1), ).setIndexNames((0, "BLUECOAT-SG-ICAP-MIB", "icapServiceStatsIndex"))
if mibBuilder.loadTexts: icapServiceStatsTableEntry.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsTableEntry.setDescription('An entry in this table represents the \n        \t\tstatistics for an ICAP service entity. An entity \n        \t\tis  uniquely identified by the service name \n        \t\t(icapServiceStatsEntityName).')
icapServiceStatsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)))
if mibBuilder.loadTexts: icapServiceStatsIndex.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsIndex.setDescription('This is the index of the table and is an \n        \t\tunique identifier of the entity.')
icapServiceStatsName = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsName.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsName.setDescription('This attribute represents the configured \n        \t\tname of the service or the service group.')
icapServiceStatsEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 3), ICAPServiceEntityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsEntityType.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsEntityType.setDescription('This  attribute defines the entity type: \n        \t\tservice or service group. The service group statistics \n        \t\trepresent the sum of all the services that are\n        \t\tmembers of the group.')
icapServiceStatsPlainConns = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsPlainConns.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsPlainConns.setDescription('Number of ICAP scanning transactions that are \n        \t\t not encrypted.')
icapServiceStatsSecuredConns = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 5), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSecuredConns.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsSecuredConns.setDescription('Number of ICAP scanning transactions that \n        \t\t are encrypted and tunneled over SSL.')
icapServiceStatsPlainActvReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsPlainActvReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsPlainActvReqs.setDescription('Line of communication between the ProxySG\n        \t\t appliance and an ICAP server across which \n        \t\t plain ICAP scanning requests are sent. \n        \t\t This statistic is not tracked for service \n        \t\t groups.')
icapServiceStatsSecureActvReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSecureActvReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsSecureActvReqs.setDescription('Secure line of communication between the \n        \t\t ProxySG appliance and an ICAP server across\n        \t\t which encrypted ICAP scanning requests are\n        \t\t sent. This statistic is not tracked for \n        \t\t service groups.')
icapServiceStatsQueuedReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsQueuedReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsQueuedReqs.setDescription('ICAP scanning transactions that are waiting\n        \t\t for an available connection.')
icapServiceStatsDeferredReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 9), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsDeferredReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsDeferredReqs.setDescription('Number of ICAP scanning transactions that \n        \t\thave been deferred until the full object has\n        \t\tbeen received.')
icapServiceStatsRcvdBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsRcvdBytes.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsRcvdBytes.setDescription('Number of data bytes received from the \n        \t\tICAP service or service group.')
icapServiceStatsSentBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSentBytes.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsSentBytes.setDescription('Number of bytes of ICAP data sent to the \n        \t\t ICAP service or service group.')
icapServiceStatsFailedReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsFailedReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsFailedReqs.setDescription('Number of ICAP scanning transactions that failed\n        \t\tbecause of a scanning timeout, connection \n        \t\tfailure, server error, or a variety of other\n        \t\tsituations.')
icapServiceStatsSuccessfullReqs = MibTableColumn((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 1, 1, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: icapServiceStatsSuccessfullReqs.setStatus('current')
if mibBuilder.loadTexts: icapServiceStatsSuccessfullReqs.setDescription('Number of ICAP scanning transactions \n        \t\t that completed successfully.')
sgICAPNotification = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 14, 1, 1, 2), ICAPServiceNotificationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sgICAPNotification.setStatus('current')
if mibBuilder.loadTexts: sgICAPNotification.setDescription('A notification type that describes an ICAP event.')
sgICAPTrap = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 14, 2, 0, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "sgICAPNotification"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsName"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsDeferredReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsQueuedReqs"))
if mibBuilder.loadTexts: sgICAPTrap.setStatus('current')
if mibBuilder.loadTexts: sgICAPTrap.setDescription('A notification that represents an ICAP- \n        \t\trelated event on an ProxySG appliance. The attributes\n        \t\tof an ICAP notification include:\n        \t\t\n        \t\tsgICAPNotification - defines the event type.\n        \t\t\n        \t\ticapServiceStatsName - the service on which the event\n        \t\t       has occurred\n        \t\t\n        \t\ticapServiceStatsDeferredReqs - the number of deferred\n        \t\t       connections on the service, at the time of event\n        \t\t\n        \t\ticapServiceStatsQueuedReqs - the number of queued \n        \t\t       connections on the service, at the time of event.')
bluecoatSgICAPMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 1))
bluecoatSgICAPMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 2))
bluecoatSgICAPMIBNotifGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 3))
bluecoatSgICAPMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 1, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "bluecoatSgICAPMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bluecoatSgICAPMIBCompliance = bluecoatSgICAPMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: bluecoatSgICAPMIBCompliance.setDescription('The compliance statement for ICAP Module. ')
bluecoatSgICAPMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 2, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsName"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsEntityType"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsPlainConns"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSecuredConns"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsPlainActvReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSecureActvReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsQueuedReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsDeferredReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsRcvdBytes"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSentBytes"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsFailedReqs"), ("BLUECOAT-SG-ICAP-MIB", "icapServiceStatsSuccessfullReqs"), ("BLUECOAT-SG-ICAP-MIB", "sgICAPNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bluecoatSgICAPMIBGroup = bluecoatSgICAPMIBGroup.setStatus('current')
if mibBuilder.loadTexts: bluecoatSgICAPMIBGroup.setDescription('Group of ICAP-related objects implemented in ProxySG \n    \t   \tappliances.')
bluecoatSgICAPMIBNotifGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 3417, 2, 14, 3, 3, 1)).setObjects(("BLUECOAT-SG-ICAP-MIB", "sgICAPTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bluecoatSgICAPMIBNotifGroup = bluecoatSgICAPMIBNotifGroup.setStatus('current')
if mibBuilder.loadTexts: bluecoatSgICAPMIBNotifGroup.setDescription('Group of ICAP notifications implemented in\n    \t\tProxySG appliances.')
mibBuilder.exportSymbols("BLUECOAT-SG-ICAP-MIB", ICAPServiceEntityType=ICAPServiceEntityType, bluecoatSgICAPMIBNotifGroups=bluecoatSgICAPMIBNotifGroups, icapServiceStatsSecuredConns=icapServiceStatsSecuredConns, icapServiceStatsTable=icapServiceStatsTable, icapServiceStatsPlainActvReqs=icapServiceStatsPlainActvReqs, sgICAPNotification=sgICAPNotification, icapServiceStatsTableEntry=icapServiceStatsTableEntry, icapServiceStatsSuccessfullReqs=icapServiceStatsSuccessfullReqs, icapServiceStatsEntityType=icapServiceStatsEntityType, bluecoatSgICAPMIBCompliance=bluecoatSgICAPMIBCompliance, sgICAPTrap=sgICAPTrap, sgICAPMIBNotificationsPrefix=sgICAPMIBNotificationsPrefix, ICAPServiceNotificationType=ICAPServiceNotificationType, icapServiceStatsDeferredReqs=icapServiceStatsDeferredReqs, icapServiceStatsFailedReqs=icapServiceStatsFailedReqs, icapServiceStatsQueuedReqs=icapServiceStatsQueuedReqs, icapServiceStatsName=icapServiceStatsName, bluecoatSgICAPMIBNotifGroup=bluecoatSgICAPMIBNotifGroup, bluecoatSgICAPMIBNotifications=bluecoatSgICAPMIBNotifications, PYSNMP_MODULE_ID=bluecoatSGICAPMIB, bluecoatSgICAPValues=bluecoatSgICAPValues, bluecoatSgICAPMIBGroups=bluecoatSgICAPMIBGroups, icapServiceStatsPlainConns=icapServiceStatsPlainConns, bluecoatSgICAPMIBGroup=bluecoatSgICAPMIBGroup, bluecoatSgICAPMIBConformance=bluecoatSgICAPMIBConformance, icapServiceStatsSecureActvReqs=icapServiceStatsSecureActvReqs, bluecoatSgICAPMIBObjects=bluecoatSgICAPMIBObjects, icapServiceStatsRcvdBytes=icapServiceStatsRcvdBytes, bluecoatSgICAPMIBCompliances=bluecoatSgICAPMIBCompliances, bluecoatSGICAPMIB=bluecoatSGICAPMIB, icapServiceStatsSentBytes=icapServiceStatsSentBytes, icapService=icapService, icapServiceStatsIndex=icapServiceStatsIndex)
