#
# PySNMP MIB module AT-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/awplus/AT-USER-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:44:40 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, iso, Unsigned32, ObjectIdentity, IpAddress, Counter64, Gauge32, NotificationType, MibIdentifier, TimeTicks, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "iso", "Unsigned32", "ObjectIdentity", "IpAddress", "Counter64", "Gauge32", "NotificationType", "MibIdentifier", "TimeTicks", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
user = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20))
user.setRevisions(('2012-09-21 00:00', '2010-09-07 00:00', '2010-06-15 00:15', '2010-06-08 00:00', '2008-10-16 12:00', '2008-08-26 00:00',))
if mibBuilder.loadTexts: user.setLastUpdated('201209210000Z')
if mibBuilder.loadTexts: user.setOrganization('Allied Telesis, Inc.')
userInfoTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1), )
if mibBuilder.loadTexts: userInfoTable.setStatus('current')
userInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1), ).setIndexNames((0, "AT-USER-MIB", "userInfoType"), (0, "AT-USER-MIB", "userInfoIndex"))
if mibBuilder.loadTexts: userInfoEntry.setStatus('current')
userInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("console", 1), ("aux", 2), ("telnet", 3), ("script", 4), ("stack", 5))))
if mibBuilder.loadTexts: userInfoType.setStatus('current')
userInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: userInfoIndex.setStatus('current')
userInfoUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoUserName.setStatus('current')
userInfoPrivilegeLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoPrivilegeLevel.setStatus('current')
userInfoIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoIdleTime.setStatus('current')
userInfoLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoLocation.setStatus('current')
userInfoPasswordLifetime = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoPasswordLifetime.setStatus('current')
userInfoPasswordLastChange = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userInfoPasswordLastChange.setStatus('current')
userConfigTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2), )
if mibBuilder.loadTexts: userConfigTable.setStatus('current')
userConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1), ).setIndexNames((0, "AT-USER-MIB", "userConfigIndex"))
if mibBuilder.loadTexts: userConfigEntry.setStatus('current')
userConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: userConfigIndex.setStatus('current')
userConfigUsername = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userConfigUsername.setStatus('current')
userConfigPrivilegeLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userConfigPrivilegeLevel.setStatus('current')
userSecurityPasswordRules = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3))
userSecurityPasswordHistory = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordHistory.setStatus('current')
userSecurityPasswordLifetime = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordLifetime.setStatus('current')
userSecurityPasswordWarning = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordWarning.setStatus('current')
userSecurityPasswordMinLength = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 23))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordMinLength.setStatus('current')
userSecurityPasswordMinCategory = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordMinCategory.setStatus('current')
userSecurityPasswordForced = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordForced.setStatus('current')
userSecurityPasswordReject = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 20, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: userSecurityPasswordReject.setStatus('current')
mibBuilder.exportSymbols("AT-USER-MIB", userInfoTable=userInfoTable, userConfigEntry=userConfigEntry, userSecurityPasswordRules=userSecurityPasswordRules, userInfoPasswordLastChange=userInfoPasswordLastChange, userSecurityPasswordMinCategory=userSecurityPasswordMinCategory, userInfoPrivilegeLevel=userInfoPrivilegeLevel, userSecurityPasswordForced=userSecurityPasswordForced, userInfoEntry=userInfoEntry, userSecurityPasswordLifetime=userSecurityPasswordLifetime, userConfigUsername=userConfigUsername, userSecurityPasswordMinLength=userSecurityPasswordMinLength, userInfoLocation=userInfoLocation, userInfoUserName=userInfoUserName, userInfoIdleTime=userInfoIdleTime, userInfoPasswordLifetime=userInfoPasswordLifetime, userSecurityPasswordWarning=userSecurityPasswordWarning, PYSNMP_MODULE_ID=user, user=user, userConfigTable=userConfigTable, userSecurityPasswordHistory=userSecurityPasswordHistory, userInfoType=userInfoType, userSecurityPasswordReject=userSecurityPasswordReject, userInfoIndex=userInfoIndex, userConfigIndex=userConfigIndex, userConfigPrivilegeLevel=userConfigPrivilegeLevel)
