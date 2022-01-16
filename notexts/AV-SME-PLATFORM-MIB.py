#
# PySNMP MIB module AV-SME-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/AV-SME-PLATFORM-MIB.mib
# Produced by pysmi-1.1.8 at Sun Jan 16 00:32:07 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
mibs, = mibBuilder.importSymbols("AVAYAGEN-MIB", "mibs")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
sysDescr, = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr")
TimeTicks, iso, Integer32, Counter64, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ObjectIdentity, IpAddress, Gauge32, MibIdentifier, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Integer32", "Counter64", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier", "ModuleIdentity", "Bits")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
avSMEPlatformMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 48))
avSMEPlatformMIB.setRevisions(('2013-01-11 14:05', '2010-07-06 13:47', '2010-07-02 14:37',))
if mibBuilder.loadTexts: avSMEPlatformMIB.setLastUpdated('201301111405Z')
if mibBuilder.loadTexts: avSMEPlatformMIB.setOrganization('Avaya Inc.')
smepGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1))
smepGenMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 1))
smepGenTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2))
smepGenConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3))
smepGTEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0))
smepGTObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1))
smepGTEventStdSeverity = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 1), ItuPerceivedSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventStdSeverity.setStatus('current')
smepGTEventDateTime = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 2), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventDateTime.setStatus('current')
smepGTEventDevID = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventDevID.setStatus('current')
smepGTEventAppEntity = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("voiceMailPro", 1), ("onex", 2), ("ipOffice", 3), ("jade", 4), ("webmanagement", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventAppEntity.setStatus('current')
smepGTEventAppEvent = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("crash", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventAppEvent.setStatus('current')
smepGenColdStartEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 1)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: smepGenColdStartEvent.setStatus('current')
smepGenWarmStartEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 2)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: smepGenWarmStartEvent.setStatus('current')
smepGenLinkDownEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 3)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: smepGenLinkDownEvent.setStatus('current')
smepGenLinkUpEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 4)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: smepGenLinkUpEvent.setStatus('current')
smepGenAuthFailureEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 5)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: smepGenAuthFailureEvent.setStatus('current')
smepGenAppEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 6)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEntity"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEvent"))
if mibBuilder.loadTexts: smepGenAppEvent.setStatus('current')
smepGenCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 1))
smepGenGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2))
smepGenCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 1, 1)).setObjects(("AV-SME-PLATFORM-MIB", "smepGenNotificationObjectsGroup"), ("AV-SME-PLATFORM-MIB", "smepGenEntGenNotificationsGroup"), ("AV-SME-PLATFORM-MIB", "smepGenAppNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenCompliance = smepGenCompliance.setStatus('deprecated')
smepGenNotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 1)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEntity"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenNotificationObjectsGroup = smepGenNotificationObjectsGroup.setStatus('current')
smepGenEntGenNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 2)).setObjects(("AV-SME-PLATFORM-MIB", "smepGenColdStartEvent"), ("AV-SME-PLATFORM-MIB", "smepGenWarmStartEvent"), ("AV-SME-PLATFORM-MIB", "smepGenLinkDownEvent"), ("AV-SME-PLATFORM-MIB", "smepGenLinkUpEvent"), ("AV-SME-PLATFORM-MIB", "smepGenAuthFailureEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenEntGenNotificationsGroup = smepGenEntGenNotificationsGroup.setStatus('current')
smepGenAppNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 3)).setObjects(("AV-SME-PLATFORM-MIB", "smepGenAppEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenAppNotificationsGroup = smepGenAppNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("AV-SME-PLATFORM-MIB", smepGenCompliance=smepGenCompliance, smepGenGroups=smepGenGroups, avSMEPlatformMIB=avSMEPlatformMIB, smepGenColdStartEvent=smepGenColdStartEvent, PYSNMP_MODULE_ID=avSMEPlatformMIB, smepGenAppEvent=smepGenAppEvent, smepGTEventAppEvent=smepGTEventAppEvent, smepGenAuthFailureEvent=smepGenAuthFailureEvent, smepGTObjects=smepGTObjects, smepGenEntGenNotificationsGroup=smepGenEntGenNotificationsGroup, smepGTEvents=smepGTEvents, smepGenTraps=smepGenTraps, smepGeneric=smepGeneric, smepGenNotificationObjectsGroup=smepGenNotificationObjectsGroup, smepGTEventStdSeverity=smepGTEventStdSeverity, smepGenLinkUpEvent=smepGenLinkUpEvent, smepGTEventDevID=smepGTEventDevID, smepGenLinkDownEvent=smepGenLinkDownEvent, smepGTEventAppEntity=smepGTEventAppEntity, smepGTEventDateTime=smepGTEventDateTime, smepGenAppNotificationsGroup=smepGenAppNotificationsGroup, smepGenCompliances=smepGenCompliances, smepGenConformance=smepGenConformance, smepGenMibs=smepGenMibs, smepGenWarmStartEvent=smepGenWarmStartEvent)
