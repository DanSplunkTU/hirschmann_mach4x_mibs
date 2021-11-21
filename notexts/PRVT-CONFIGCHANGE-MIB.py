#
# PySNMP MIB module PRVT-CONFIGCHANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-CONFIGCHANGE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:45 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Bits, Integer32, ModuleIdentity, iso, Counter64, ObjectIdentity, Gauge32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Integer32", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity", "Gauge32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention, RowPointer = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowPointer")
prvtConfigChangeMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 150))
prvtConfigChangeMIB.setRevisions(('2009-07-13 00:00', '2006-11-20 00:00',))
if mibBuilder.loadTexts: prvtConfigChangeMIB.setLastUpdated('200907130000Z')
if mibBuilder.loadTexts: prvtConfigChangeMIB.setOrganization('BATM Advanced Communication')
prvtConfigChangeAlarmOID = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 1), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtConfigChangeAlarmOID.setStatus('current')
prvtConfigChangeAlarmRow = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 2), RowPointer()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtConfigChangeAlarmRow.setStatus('current')
cliConfigChangeNodePrompt = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 3), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cliConfigChangeNodePrompt.setStatus('current')
cliConfigChangeCommand = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 4), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cliConfigChangeCommand.setStatus('current')
snmpServerStatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: snmpServerStatus.setStatus('current')
prvtConfigChangeAlarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0, 1)).setObjects(("PRVT-CONFIGCHANGE-MIB", "prvtConfigChangeAlarmOID"), ("PRVT-CONFIGCHANGE-MIB", "prvtConfigChangeAlarmRow"))
if mibBuilder.loadTexts: prvtConfigChangeAlarm.setStatus('current')
cliConfigurationChange = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0, 2)).setObjects(("PRVT-CONFIGCHANGE-MIB", "cliConfigChangeNodePrompt"), ("PRVT-CONFIGCHANGE-MIB", "cliConfigChangeCommand"))
if mibBuilder.loadTexts: cliConfigurationChange.setStatus('current')
snmpServerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0, 3)).setObjects(("PRVT-CONFIGCHANGE-MIB", "snmpServerStatus"))
if mibBuilder.loadTexts: snmpServerStatusChange.setStatus('current')
prvtConfigChangeNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 0))
prvtConfigChangeObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 1))
prvtConfigChangeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 150, 3))
mibBuilder.exportSymbols("PRVT-CONFIGCHANGE-MIB", snmpServerStatusChange=snmpServerStatusChange, PYSNMP_MODULE_ID=prvtConfigChangeMIB, prvtConfigChangeMIB=prvtConfigChangeMIB, prvtConfigChangeAlarmOID=prvtConfigChangeAlarmOID, prvtConfigChangeAlarmRow=prvtConfigChangeAlarmRow, prvtConfigChangeConformance=prvtConfigChangeConformance, prvtConfigChangeAlarm=prvtConfigChangeAlarm, cliConfigChangeNodePrompt=cliConfigChangeNodePrompt, prvtConfigChangeObjects=prvtConfigChangeObjects, cliConfigurationChange=cliConfigurationChange, prvtConfigChangeNotifications=prvtConfigChangeNotifications, snmpServerStatus=snmpServerStatus, cliConfigChangeCommand=cliConfigChangeCommand)
