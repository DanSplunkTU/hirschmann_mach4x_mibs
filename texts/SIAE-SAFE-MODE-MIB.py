#
# PySNMP MIB module SIAE-SAFE-MODE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-SAFE-MODE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:19:22 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, NotificationType, Gauge32, Counter32, Counter64, Unsigned32, ObjectIdentity, IpAddress, ModuleIdentity, iso, Integer32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "NotificationType", "Gauge32", "Counter32", "Counter64", "Unsigned32", "ObjectIdentity", "IpAddress", "ModuleIdentity", "iso", "Integer32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
safeMode = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 99))
safeMode.setRevisions(('2016-03-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: safeMode.setRevisionsDescriptions(('Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: safeMode.setLastUpdated('201603100000Z')
if mibBuilder.loadTexts: safeMode.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: safeMode.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: help.help@siaemic.com\n            ')
if mibBuilder.loadTexts: safeMode.setDescription('Management information for safe mode.\n            ')
safeModeMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: safeModeMibVersion.setStatus('current')
if mibBuilder.loadTexts: safeModeMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
safeModeAlarm = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 2), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: safeModeAlarm.setStatus('current')
if mibBuilder.loadTexts: safeModeAlarm.setDescription('Safe mode alarm with associated severity. This object\n             indicates that the equipment is in safe mode.\n            ')
safeModeAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 3), AlarmSeverityCode().clone('minorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: safeModeAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: safeModeAlarmSeverityCode.setDescription('Defines the severity associated to the safeModeAlarm\n             and enables/disables the trap generation on status change event.\n            ')
safeModeStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("safeModeStatusInactive", 1), ("safeModeStatusNoAuxService", 2), ("safeModeStatusLinkMngmt", 3), ("safeModeStatusSiteMngmt", 4), ("safeModeStatusSiteDefault", 5), ("safeModeStatusSiteRescue", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: safeModeStatus.setStatus('current')
if mibBuilder.loadTexts: safeModeStatus.setDescription('The safe mode status of the equipment.\n             Equipment in normal-mode has safe mode status inactive')
safeModeRescueAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: safeModeRescueAdminStatus.setStatus('current')
if mibBuilder.loadTexts: safeModeRescueAdminStatus.setDescription('This object enables or disables the site-rescue .')
safeModeRescuePwd = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: safeModeRescuePwd.setStatus('current')
if mibBuilder.loadTexts: safeModeRescuePwd.setDescription('This object specifies the login password of the rescue\n             user.')
safeModeRescueIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 7), IpAddress().clone(hexValue="ac14fd0d")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: safeModeRescueIpAddress.setStatus('current')
if mibBuilder.loadTexts: safeModeRescueIpAddress.setDescription('Ip address of the equipment in status site-rescue')
safeModeRescueIpNetMask = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 99, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: safeModeRescueIpNetMask.setStatus('current')
if mibBuilder.loadTexts: safeModeRescueIpNetMask.setDescription('The subnet Mask associated with the Rescue IP address.\n             The value of the Mask is an IP address with all the network bits set to 1\n             and all the hosts bits set to 0.')
mibBuilder.exportSymbols("SIAE-SAFE-MODE-MIB", PYSNMP_MODULE_ID=safeMode, safeModeAlarmSeverityCode=safeModeAlarmSeverityCode, safeModeMibVersion=safeModeMibVersion, safeModeStatus=safeModeStatus, safeModeRescueIpNetMask=safeModeRescueIpNetMask, safeModeRescueAdminStatus=safeModeRescueAdminStatus, safeModeAlarm=safeModeAlarm, safeModeRescuePwd=safeModeRescuePwd, safeModeRescueIpAddress=safeModeRescueIpAddress, safeMode=safeMode)
