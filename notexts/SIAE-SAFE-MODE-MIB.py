#
# PySNMP MIB module SIAE-SAFE-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SAFE-MODE-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:19:31 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
AlarmSeverityCode, AlarmStatus = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, NotificationType, TimeTicks, IpAddress, Counter32, Counter64, ObjectIdentity, ModuleIdentity, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "TimeTicks", "IpAddress", "Counter32", "Counter64", "ObjectIdentity", "ModuleIdentity", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
safeMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 99))
safeMode.setRevisions(('2016-03-10 00:00',))
if mibBuilder.loadTexts: safeMode.setLastUpdated('201603100000Z')
if mibBuilder.loadTexts: safeMode.setOrganization('SIAE MICROELETTRONICA spa')
safeModeMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: safeModeMibVersion.setStatus('current')
safeModeAlarm = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 2), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: safeModeAlarm.setStatus('current')
safeModeAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 3), AlarmSeverityCode().clone('minorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: safeModeAlarmSeverityCode.setStatus('current')
safeModeStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("safeModeStatusInactive", 1), ("safeModeStatusNoAuxService", 2), ("safeModeStatusLinkMngmt", 3), ("safeModeStatusSiteMngmt", 4), ("safeModeStatusSiteDefault", 5), ("safeModeStatusSiteRescue", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: safeModeStatus.setStatus('current')
safeModeRescueAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: safeModeRescueAdminStatus.setStatus('current')
safeModeRescuePwd = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: safeModeRescuePwd.setStatus('current')
safeModeRescueIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 7), IpAddress().clone(hexValue="ac14fd0d")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: safeModeRescueIpAddress.setStatus('current')
safeModeRescueIpNetMask = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: safeModeRescueIpNetMask.setStatus('current')
mibBuilder.exportSymbols("SIAE-SAFE-MODE-MIB", safeModeAlarm=safeModeAlarm, safeModeAlarmSeverityCode=safeModeAlarmSeverityCode, PYSNMP_MODULE_ID=safeMode, safeMode=safeMode, safeModeMibVersion=safeModeMibVersion, safeModeRescuePwd=safeModeRescuePwd, safeModeRescueAdminStatus=safeModeRescueAdminStatus, safeModeRescueIpAddress=safeModeRescueIpAddress, safeModeStatus=safeModeStatus, safeModeRescueIpNetMask=safeModeRescueIpNetMask)
