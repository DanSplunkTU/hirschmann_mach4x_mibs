#
# PySNMP MIB module PRVT-CONFIGCHANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-CONFIGCHANGE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:48 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, iso, Integer32, Counter32, IpAddress, Bits, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, TimeTicks, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Integer32", "Counter32", "IpAddress", "Bits", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "TimeTicks", "NotificationType", "Unsigned32")
RowPointer, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DisplayString", "TextualConvention")
prvtConfigChangeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 150))
prvtConfigChangeMIB.setRevisions(('2009-07-13 00:00', '2006-11-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtConfigChangeMIB.setRevisionsDescriptions(('Add object snmpServerStatus and notification snmpServerStatusChange', 'Initial release',))
if mibBuilder.loadTexts: prvtConfigChangeMIB.setLastUpdated('200907130000Z')
if mibBuilder.loadTexts: prvtConfigChangeMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtConfigChangeMIB.setContactInfo('BATM/Telco Systems Support team\nEmail:\nFor North America: techsupport@telco.com\nFor North Europe: support@batm.de, info@batm.de\nFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtConfigChangeMIB.setDescription('Initial version. This MIB will provied traps for change')
prvtConfigChangeAlarmOID = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtConfigChangeAlarmOID.setStatus('current')
if mibBuilder.loadTexts: prvtConfigChangeAlarmOID.setDescription('The configChangeAlarmOID specifies the OID of an object whose value has been changed.')
prvtConfigChangeAlarmRow = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 2), RowPointer()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtConfigChangeAlarmRow.setStatus('current')
if mibBuilder.loadTexts: prvtConfigChangeAlarmRow.setDescription('The configChangeAlarmRow specifies the OID of the row from table, whose entry has been changed.')
cliConfigChangeNodePrompt = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cliConfigChangeNodePrompt.setStatus('current')
if mibBuilder.loadTexts: cliConfigChangeNodePrompt.setDescription('Shows the CLI prompt.')
cliConfigChangeCommand = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cliConfigChangeCommand.setStatus('current')
if mibBuilder.loadTexts: cliConfigChangeCommand.setDescription('Shows executed command.')
snmpServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: snmpServerStatus.setStatus('current')
if mibBuilder.loadTexts: snmpServerStatus.setDescription('Shows the enabled/disabled status of the SNMP server.')
prvtConfigChangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0, 1)).setObjects(("PRVT-CONFIGCHANGE-MIB", "prvtConfigChangeAlarmOID"), ("PRVT-CONFIGCHANGE-MIB", "prvtConfigChangeAlarmRow"))
if mibBuilder.loadTexts: prvtConfigChangeAlarm.setStatus('current')
if mibBuilder.loadTexts: prvtConfigChangeAlarm.setDescription('This notification is generated when the value of configurable\nattribute has been changed. The notification can be used\nto trigger maintenance polling of the running configuration\non the device. One of the varbinds will point either to entry\nof the modified table (configChangeAlarmRow) or the\nOID of the modified scalar object ')
cliConfigurationChange = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0, 2)).setObjects(("PRVT-CONFIGCHANGE-MIB", "cliConfigChangeNodePrompt"), ("PRVT-CONFIGCHANGE-MIB", "cliConfigChangeCommand"))
if mibBuilder.loadTexts: cliConfigurationChange.setStatus('current')
if mibBuilder.loadTexts: cliConfigurationChange.setDescription('This notification is generated when command in configuration node is executed.')
snmpServerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0, 3)).setObjects(("PRVT-CONFIGCHANGE-MIB", "snmpServerStatus"))
if mibBuilder.loadTexts: snmpServerStatusChange.setStatus('current')
if mibBuilder.loadTexts: snmpServerStatusChange.setDescription('The notification shall be sent whenever the enabled/disabled status\nof the SNMP server changes. If the status is changed\nfrom enabled to disabled, the notification shall be sent\nprior to disabling the SNMP server.')
prvtConfigChangeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0))
prvtConfigChangeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1))
prvtConfigChangeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 3))
mibBuilder.exportSymbols("PRVT-CONFIGCHANGE-MIB", cliConfigurationChange=cliConfigurationChange, prvtConfigChangeObjects=prvtConfigChangeObjects, cliConfigChangeNodePrompt=cliConfigChangeNodePrompt, prvtConfigChangeNotifications=prvtConfigChangeNotifications, prvtConfigChangeAlarmRow=prvtConfigChangeAlarmRow, prvtConfigChangeConformance=prvtConfigChangeConformance, cliConfigChangeCommand=cliConfigChangeCommand, prvtConfigChangeMIB=prvtConfigChangeMIB, prvtConfigChangeAlarmOID=prvtConfigChangeAlarmOID, snmpServerStatusChange=snmpServerStatusChange, snmpServerStatus=snmpServerStatus, PYSNMP_MODULE_ID=prvtConfigChangeMIB, prvtConfigChangeAlarm=prvtConfigChangeAlarm)
