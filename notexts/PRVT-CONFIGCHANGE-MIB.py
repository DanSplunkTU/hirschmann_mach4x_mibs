#
# PySNMP MIB module PRVT-CONFIGCHANGE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-CONFIGCHANGE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, RowPointer, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowPointer", "DisplayString")
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
mibBuilder.exportSymbols("PRVT-CONFIGCHANGE-MIB", prvtConfigChangeNotifications=prvtConfigChangeNotifications, snmpServerStatus=snmpServerStatus, cliConfigurationChange=cliConfigurationChange, prvtConfigChangeAlarmRow=prvtConfigChangeAlarmRow, cliConfigChangeCommand=cliConfigChangeCommand, prvtConfigChangeObjects=prvtConfigChangeObjects, prvtConfigChangeAlarm=prvtConfigChangeAlarm, prvtConfigChangeConformance=prvtConfigChangeConformance, prvtConfigChangeAlarmOID=prvtConfigChangeAlarmOID, snmpServerStatusChange=snmpServerStatusChange, prvtConfigChangeMIB=prvtConfigChangeMIB, cliConfigChangeNodePrompt=cliConfigChangeNodePrompt, PYSNMP_MODULE_ID=prvtConfigChangeMIB)
