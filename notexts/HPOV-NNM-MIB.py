#
# PySNMP MIB module HPOV-NNM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/alcatel/HPOV-NNM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:37:20 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, enterprises, Bits, MibIdentifier, IpAddress, Unsigned32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Gauge32, Counter32, iso, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "enterprises", "Bits", "MibIdentifier", "IpAddress", "Unsigned32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Gauge32", "Counter32", "iso", "TimeTicks", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hp = MibIdentifier((1, 3, 6, 1, 4, 1, 11))
nm = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2))
openView = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17))
hpOpenView = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 17, 1))
hpOpenView.setRevisions(('1996-07-08 00:00',))
if mibBuilder.loadTexts: hpOpenView.setLastUpdated('9607080000Z')
if mibBuilder.loadTexts: hpOpenView.setOrganization('Hewlett-Packard, Network & System Management Division')
class OVTextString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

openViewTrapVars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17, 2))
openViewSourceId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 1), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewSourceId.setStatus('current')
openViewSourceName = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 2), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewSourceName.setStatus('current')
openViewObjectId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewObjectId.setStatus('current')
openViewData = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 4), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewData.setStatus('current')
openViewSeverity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 5), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewSeverity.setStatus('current')
openViewCategory = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 6), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCategory.setStatus('current')
openViewFilter = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 7), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewFilter.setStatus('current')
openViewEntity = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 8), OVTextString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEntity.setStatus('current')
openViewAddress = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 9), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewAddress.setStatus('current')
openViewPid = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 10), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewPid.setStatus('current')
openViewCmipManagedObjectClass = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 11), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipManagedObjectClass.setStatus('current')
openViewCmipEventTime = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 12), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipEventTime.setStatus('current')
openViewCmipEventType = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 13), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipEventType.setStatus('current')
openViewCmipEventInfo = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 14), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipEventInfo.setStatus('current')
openViewCmipManagedObjectInstanceId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 15), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewCmipManagedObjectInstanceId.setStatus('current')
openViewEventUUID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 16), OctetString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEventUUID.setStatus('current')
openViewEcsCorrelateEvUUID = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 17), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEcsCorrelateEvUUID.setStatus('current')
openViewEcsNodeImportance = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 17, 2, 18), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: openViewEcsNodeImportance.setStatus('current')
hpOVNNMTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 17, 1, 0))
mibBuilder.exportSymbols("HPOV-NNM-MIB", openViewCmipEventType=openViewCmipEventType, hpOpenView=hpOpenView, hpOVNNMTraps=hpOVNNMTraps, openViewCmipManagedObjectClass=openViewCmipManagedObjectClass, openViewFilter=openViewFilter, openViewCategory=openViewCategory, openViewData=openViewData, openViewObjectId=openViewObjectId, openViewEcsNodeImportance=openViewEcsNodeImportance, openViewEntity=openViewEntity, openViewPid=openViewPid, nm=nm, openViewAddress=openViewAddress, openViewEventUUID=openViewEventUUID, hp=hp, openViewSourceId=openViewSourceId, PYSNMP_MODULE_ID=hpOpenView, openViewEcsCorrelateEvUUID=openViewEcsCorrelateEvUUID, openViewTrapVars=openViewTrapVars, openViewCmipManagedObjectInstanceId=openViewCmipManagedObjectInstanceId, OVTextString=OVTextString, openViewCmipEventInfo=openViewCmipEventInfo, openViewSeverity=openViewSeverity, openView=openView, openViewSourceName=openViewSourceName, openViewCmipEventTime=openViewCmipEventTime)
