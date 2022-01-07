#
# PySNMP MIB module HPOV-NNM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alcatel/HPOV-NNM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:09:08 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter64, Counter32, ModuleIdentity, NotificationType, IpAddress, TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, Bits, MibIdentifier, enterprises, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "ModuleIdentity", "NotificationType", "IpAddress", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "Bits", "MibIdentifier", "enterprises", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
openView = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17))
hpOpenView = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 17, 1))
hpOpenView.setRevisions(('1996-07-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hpOpenView.setRevisionsDescriptions(('Initial revision published as part of hp-unix MIB.\r\r\n\t     Updated to add support for SNMPv2 Security Proxy.\r\r\n\t     Updated to use the SNMPv2 SMI.',))
if mibBuilder.loadTexts: hpOpenView.setLastUpdated('9607080000Z')
if mibBuilder.loadTexts: hpOpenView.setOrganization('Hewlett-Packard, Network & System Management Division')
if mibBuilder.loadTexts: hpOpenView.setContactInfo('Support: Hewlett-Packard Response Center\r\r\n                 Tel: +1 (800) 633-3600')
if mibBuilder.loadTexts: hpOpenView.setDescription('General management information used within the \r\r\n             HP OpenView Network Node Manager product.\r\r\n\t     \r\r\n\t     This object identifier also serves as the \r\r\n\t     OpenView Enterprise ID for SNMPv1 Traps.')
class OVTextString(TextualConvention, OctetString):
    description = 'Represents textual information consisting of either \r\r\n            single- or multi-byte characters.  \r\r\n\r\r\n            The character string is interpreted using the locale \r\r\n            (language) of the interpreting entity because the locale \r\r\n            is NOT included.  Therefore, transmitting an object value \r\r\n            of this syntax across different locales is not supported.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

openViewTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17, 2))
openViewSourceId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewSourceId.setStatus('current')
if mibBuilder.loadTexts: openViewSourceId.setDescription('The identifier of the software generating the trap/event.\r\r\n\t\t This number is used by HP OpenView software when it sends\r\r\n\t\t an event to the OpenView event system.  It identifies\r\r\n\t\t which software component sent the event.')
openViewSourceName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 2), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewSourceName.setStatus('current')
if mibBuilder.loadTexts: openViewSourceName.setDescription('The source of the event (may not be the machine upon\r\r\n\t\t which the event was generated).  This string is used\r\r\n\t\t by HP OpenView software when it sends an event.  It\r\r\n\t\t identifies for which node the event is generated.')
openViewObjectId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewObjectId.setStatus('current')
if mibBuilder.loadTexts: openViewObjectId.setDescription('The OpenView Windows object identifier associated \r\r\n                 with the source of the trap/event.')
openViewData = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 4), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewData.setStatus('current')
if mibBuilder.loadTexts: openViewData.setDescription('Any miscellaneous data sent with an OpenView trap/event.')
openViewSeverity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 5), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewSeverity.setStatus('current')
if mibBuilder.loadTexts: openViewSeverity.setDescription('The OpenView event severity associated with the trap/event.')
openViewCategory = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 6), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCategory.setStatus('current')
if mibBuilder.loadTexts: openViewCategory.setDescription('The OpenView event category associated with the trap/event.')
openViewFilter = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewFilter.setStatus('current')
if mibBuilder.loadTexts: openViewFilter.setDescription('The event filter for an application connecting to the\r\r\n\t\t OpenView event system.')
openViewEntity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 8), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEntity.setStatus('current')
if mibBuilder.loadTexts: openViewEntity.setDescription('The entity (string name) of an application connecting\r\r\n\t\t to the OpenView event system.')
openViewAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewAddress.setStatus('current')
if mibBuilder.loadTexts: openViewAddress.setDescription('The IP address of the node from where an application\r\r\n\t\t is connecting to the OpenView event system.')
openViewPid = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 10), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewPid.setStatus('current')
if mibBuilder.loadTexts: openViewPid.setDescription('The process ID of an application connecting to the\r\r\n\t\t OpenView event system.')
openViewCmipManagedObjectClass = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 11), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipManagedObjectClass.setStatus('current')
if mibBuilder.loadTexts: openViewCmipManagedObjectClass.setDescription('A cmisEventReport managedObjectClass.  Only valid when\r\r\n\t\t running with the HP OpenView DM product.')
openViewCmipEventTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 12), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipEventTime.setStatus('current')
if mibBuilder.loadTexts: openViewCmipEventTime.setDescription('A cmisEventReport eventTime.  Only valid when\r\r\n\t\t running with the HP OpenView DM product.')
openViewCmipEventType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 13), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipEventType.setStatus('current')
if mibBuilder.loadTexts: openViewCmipEventType.setDescription('A cmisEventReport eventType.  Only valid when\r\r\n\t\t running with the HP OpenView DM product.')
openViewCmipEventInfo = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 14), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipEventInfo.setStatus('current')
if mibBuilder.loadTexts: openViewCmipEventInfo.setDescription('A cmisEventReport eventInfo.  Only valid when\r\r\n\t\t running with the HP OpenView DM product.')
openViewCmipManagedObjectInstanceId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 15), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipManagedObjectInstanceId.setStatus('current')
if mibBuilder.loadTexts: openViewCmipManagedObjectInstanceId.setDescription('A cmisEventReport managedObjectInstance.  Only valid when\r\r\n\t\t running with the HP OpenView DM product.')
openViewEventUUID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 16), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEventUUID.setStatus('current')
if mibBuilder.loadTexts: openViewEventUUID.setDescription('An OpenView Event UUID which uniquely identifies an event.')
openViewEcsCorrelateEvUUID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 17), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEcsCorrelateEvUUID.setStatus('current')
if mibBuilder.loadTexts: openViewEcsCorrelateEvUUID.setDescription('If an OpenView event contains this var-bind, it indicates to\r\r\n\t\tthe Event Correlation System that the event should be correlated\r\r\n\t\twith the event whose UUID is the value of this var-bind.  If the\r\r\n\t\tvar-bind is missing or has a zero length value, then no event\r\r\n\t\tcorrelation occurs.')
openViewEcsNodeImportance = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 18), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEcsNodeImportance.setStatus('current')
if mibBuilder.loadTexts: openViewEcsNodeImportance.setDescription('If an OpenView event contains this var-bind, it indicates to\r\r\n\t\tthe Event Correlation System the importance of the node from\r\r\n\t\tan event correlation perspective.  In situations where the\r\r\n\t\tECS system would normally suppress an event, it may choose not\r\r\n\t\tto suppress it if the node is very important (e.g. an important\r\r\n\t\tserver node).  The integral value of this MIB object may evolve\r\r\n\t\tover time.  For now, non-integral values are invalid, a value of\r\r\n\t\tzero indicates that the node is a regular node and a non-zero \r\r\n\t\tvalue indicates that the node is an important node.')
hpOVNNMTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17, 1, 0))
mibBuilder.exportSymbols("HPOV-NNM-MIB", openViewPid=openViewPid, nm=nm, openViewCmipManagedObjectClass=openViewCmipManagedObjectClass, openViewSeverity=openViewSeverity, openViewCmipEventTime=openViewCmipEventTime, openViewObjectId=openViewObjectId, openViewEcsNodeImportance=openViewEcsNodeImportance, openViewCategory=openViewCategory, openViewSourceName=openViewSourceName, openView=openView, openViewEntity=openViewEntity, openViewEventUUID=openViewEventUUID, openViewSourceId=openViewSourceId, hpOpenView=hpOpenView, PYSNMP_MODULE_ID=hpOpenView, openViewData=openViewData, hpOVNNMTraps=hpOVNNMTraps, openViewCmipEventType=openViewCmipEventType, openViewTrapVars=openViewTrapVars, openViewCmipManagedObjectInstanceId=openViewCmipManagedObjectInstanceId, OVTextString=OVTextString, openViewEcsCorrelateEvUUID=openViewEcsCorrelateEvUUID, openViewCmipEventInfo=openViewCmipEventInfo, hp=hp, openViewAddress=openViewAddress, openViewFilter=openViewFilter)
