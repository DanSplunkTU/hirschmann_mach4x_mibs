#
# PySNMP MIB module AV-SME-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/avaya/AV-SME-PLATFORM-MIB.mib
# Produced by pysmi-1.1.3 at Sun Nov 21 00:33:34 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
mibs, = mibBuilder.importSymbols("AVAYAGEN-MIB", "mibs")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ItuPerceivedSeverity, = mibBuilder.importSymbols("ITU-ALARM-TC-MIB", "ItuPerceivedSeverity")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
sysDescr, = mibBuilder.importSymbols("SNMPv2-MIB", "sysDescr")
Counter64, Integer32, Counter32, Unsigned32, IpAddress, ModuleIdentity, ObjectIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, iso, MibIdentifier, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Integer32", "Counter32", "Unsigned32", "IpAddress", "ModuleIdentity", "ObjectIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "iso", "MibIdentifier", "NotificationType")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
avSMEPlatformMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6889, 2, 48))
avSMEPlatformMIB.setRevisions(('2013-01-11 14:05', '2010-07-06 13:47', '2010-07-02 14:37',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: avSMEPlatformMIB.setRevisionsDescriptions(('Rev 0.03.00\n         Added the WebManagement application value for smepGTEventAppIdentity.', 'Rev 0.02.00\n        Corrected base OID to one properly allocated in Avaya tree.', 'Rev 0.01.00\n        The first rough draft of this MIB module.',))
if mibBuilder.loadTexts: avSMEPlatformMIB.setLastUpdated('201301111405Z')
if mibBuilder.loadTexts: avSMEPlatformMIB.setOrganization('Avaya Inc.')
if mibBuilder.loadTexts: avSMEPlatformMIB.setContactInfo('Avaya Customer Services\n         Postal: Avaya, Inc.\n                 211 Mt Airy Rd.\n                 Basking Ridge, NJ 07920\n                 USA\n         Tel:    +1 908 953 6000\n\n         WWW:    http://www.avaya.com')
if mibBuilder.loadTexts: avSMEPlatformMIB.setDescription('Avaya IP Office MIBs OID tree.\n\n         This MIB module defines the root items for MIBs for\n         use with Avaya SME Embedded Platform.')
smepGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1))
smepGenMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 1))
smepGenTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2))
smepGenConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3))
smepGTEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0))
smepGTObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1))
smepGTEventStdSeverity = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 1), ItuPerceivedSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventStdSeverity.setStatus('current')
if mibBuilder.loadTexts: smepGTEventStdSeverity.setDescription('Severity of the event that has occurred.\n\n        The event severity depends upon the type of\n        entity/notification that the operational state change event\n        relates to. The severity values that are normally used are\n        detailed below:\n\n        The enterprise versions of standard SNMP traps all have a\n        severity of major (4).\n\n        GenAppEvents:\n          Severity depends on event condition\n              crash       - severity is critical (3)')
smepGTEventDateTime = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 2), DateAndTime()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventDateTime.setStatus('current')
if mibBuilder.loadTexts: smepGTEventDateTime.setDescription('Date and time of the occurence of the event.')
smepGTEventDevID = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventDevID.setStatus('current')
if mibBuilder.loadTexts: smepGTEventDevID.setDescription('A unique textual identifier of the alarming device.')
smepGTEventAppEntity = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("voiceMailPro", 1), ("onex", 2), ("ipOffice", 3), ("jade", 4), ("webmanagement", 5)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventAppEntity.setStatus('current')
if mibBuilder.loadTexts: smepGTEventAppEntity.setDescription('The SME Embedded Platform application to which a\n        notification/trap relates.')
smepGTEventAppEvent = MibScalar((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("crash", 1)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: smepGTEventAppEvent.setStatus('current')
if mibBuilder.loadTexts: smepGTEventAppEvent.setDescription('SME Embedded Platform application event states. The\n        associated event severity of the notification/trap the object\n        is carried in varies depending upon the event condition. The\n        appropriate severity is detailed against event enumeration.')
smepGenColdStartEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 1)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: smepGenColdStartEvent.setStatus('current')
if mibBuilder.loadTexts: smepGenColdStartEvent.setDescription("Enterprise version of standard coldstart trap featuring\n         device identification information. A coldStart trap\n         signifies that the sending protocol entity is reinitializing\n         itself such that the agent's configuration or the protocol\n         entity implementation may be altered.")
smepGenWarmStartEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 2)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: smepGenWarmStartEvent.setStatus('current')
if mibBuilder.loadTexts: smepGenWarmStartEvent.setDescription('Enterprise version of standard warmstart trap featuring\n         device identification information. A warmStart trap\n         signifies that the sending protocol entity is reinitializing\n         that neither the agent configuration nor the protocol entity\n         implementation is altered.')
smepGenLinkDownEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 3)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: smepGenLinkDownEvent.setStatus('current')
if mibBuilder.loadTexts: smepGenLinkDownEvent.setDescription("Enterprise version of standard linkDown trap featuring device\n         identification information. A linkDown trap signifies that\n         the sending protocol entity recognizes a failure in one of\n         the communication links represented in the agent's\n         configuration.")
smepGenLinkUpEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 4)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: smepGenLinkUpEvent.setStatus('current')
if mibBuilder.loadTexts: smepGenLinkUpEvent.setDescription("Enterprise version of standard linkUp trap featuring device\n         identification information. A linkUp trap signifies that the\n         sending protocol entity recognizes that one of the\n         communication links represented in the agent's configuration\n         has come up.")
smepGenAuthFailureEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 5)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"))
if mibBuilder.loadTexts: smepGenAuthFailureEvent.setStatus('current')
if mibBuilder.loadTexts: smepGenAuthFailureEvent.setDescription('Enterprise version of standard authenticationFailure trap\n         featuring device identification information. An\n         authenticationFailure trap signifies that the sending\n         protocol entity is the addressee of a protocol message that\n         is not properly authenticated. While implementations of the\n         SNMP must be capable of generating this trap, they must also\n         be capable of suppressing the emission of such traps via an\n         implementation- specific mechanism.')
smepGenAppEvent = NotificationType((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 2, 0, 6)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("SNMPv2-MIB", "sysDescr"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEntity"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEvent"))
if mibBuilder.loadTexts: smepGenAppEvent.setStatus('current')
if mibBuilder.loadTexts: smepGenAppEvent.setDescription('A smepGenAppEvent notification is generated whenever a\n        application entity of the SME Embedded Platform experiences an\n        event. It signifies that the SNMP entity, acting as a proxy\n        for the application, has detected an event on the application\n        entity.\n\n        The event severity varies dependent upon the event condition.')
smepGenCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 1))
smepGenGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2))
smepGenCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 1, 1)).setObjects(("AV-SME-PLATFORM-MIB", "smepGenNotificationObjectsGroup"), ("AV-SME-PLATFORM-MIB", "smepGenEntGenNotificationsGroup"), ("AV-SME-PLATFORM-MIB", "smepGenAppNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenCompliance = smepGenCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: smepGenCompliance.setDescription('The compliance statement for SME Embedded Platform agents\n         which implement this MIB.')
smepGenNotificationObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 1)).setObjects(("AV-SME-PLATFORM-MIB", "smepGTEventStdSeverity"), ("AV-SME-PLATFORM-MIB", "smepGTEventDevID"), ("AV-SME-PLATFORM-MIB", "smepGTEventDateTime"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEntity"), ("AV-SME-PLATFORM-MIB", "smepGTEventAppEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenNotificationObjectsGroup = smepGenNotificationObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: smepGenNotificationObjectsGroup.setDescription('Objects that are contained in SME Embedded Platform wide\n        notifications.')
smepGenEntGenNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 2)).setObjects(("AV-SME-PLATFORM-MIB", "smepGenColdStartEvent"), ("AV-SME-PLATFORM-MIB", "smepGenWarmStartEvent"), ("AV-SME-PLATFORM-MIB", "smepGenLinkDownEvent"), ("AV-SME-PLATFORM-MIB", "smepGenLinkUpEvent"), ("AV-SME-PLATFORM-MIB", "smepGenAuthFailureEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenEntGenNotificationsGroup = smepGenEntGenNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: smepGenEntGenNotificationsGroup.setDescription('SME Embedded Platform Enterpise versions of the generic traps\n        as defined RFC1215 that provide more identification of the entity\n        concerned.')
smepGenAppNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6889, 2, 48, 1, 3, 2, 3)).setObjects(("AV-SME-PLATFORM-MIB", "smepGenAppEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smepGenAppNotificationsGroup = smepGenAppNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: smepGenAppNotificationsGroup.setDescription('The service notifications which indicate specific changes in\n        the state of Applications on the SME Embedded Platform.')
mibBuilder.exportSymbols("AV-SME-PLATFORM-MIB", smepGTEventStdSeverity=smepGTEventStdSeverity, smepGenConformance=smepGenConformance, smepGenLinkDownEvent=smepGenLinkDownEvent, PYSNMP_MODULE_ID=avSMEPlatformMIB, smepGeneric=smepGeneric, smepGenTraps=smepGenTraps, avSMEPlatformMIB=avSMEPlatformMIB, smepGTEventAppEntity=smepGTEventAppEntity, smepGenMibs=smepGenMibs, smepGenGroups=smepGenGroups, smepGTEvents=smepGTEvents, smepGenCompliance=smepGenCompliance, smepGTEventDevID=smepGTEventDevID, smepGenLinkUpEvent=smepGenLinkUpEvent, smepGTObjects=smepGTObjects, smepGTEventAppEvent=smepGTEventAppEvent, smepGenWarmStartEvent=smepGenWarmStartEvent, smepGTEventDateTime=smepGTEventDateTime, smepGenNotificationObjectsGroup=smepGenNotificationObjectsGroup, smepGenColdStartEvent=smepGenColdStartEvent, smepGenAppEvent=smepGenAppEvent, smepGenCompliances=smepGenCompliances, smepGenEntGenNotificationsGroup=smepGenEntGenNotificationsGroup, smepGenAuthFailureEvent=smepGenAuthFailureEvent, smepGenAppNotificationsGroup=smepGenAppNotificationsGroup)
