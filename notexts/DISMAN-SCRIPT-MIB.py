#
# PySNMP MIB module DISMAN-SCRIPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DISMAN-SCRIPT-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:00 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, iso, Counter64, Gauge32, mib_2, Counter32, MibIdentifier, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Bits, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "Counter64", "Gauge32", "mib-2", "Counter32", "MibIdentifier", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Bits", "TimeTicks", "IpAddress")
TimeInterval, RowStatus, DisplayString, StorageType, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TimeInterval", "RowStatus", "DisplayString", "StorageType", "TextualConvention", "DateAndTime")
scriptMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 64))
scriptMIB.setRevisions(('2001-08-21 00:00', '1999-02-22 18:00',))
if mibBuilder.loadTexts: scriptMIB.setLastUpdated('200108210000Z')
if mibBuilder.loadTexts: scriptMIB.setOrganization('IETF Distributed Management Working Group')
smObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 1))
smNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 2))
smConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 3))
smLangTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 1), )
if mibBuilder.loadTexts: smLangTable.setStatus('current')
smLangEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 1, 1), ).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smLangIndex"))
if mibBuilder.loadTexts: smLangEntry.setStatus('current')
smLangIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: smLangIndex.setStatus('current')
smLangLanguage = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smLangLanguage.setStatus('current')
smLangVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smLangVersion.setStatus('current')
smLangVendor = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smLangVendor.setStatus('current')
smLangRevision = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smLangRevision.setStatus('current')
smLangDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smLangDescr.setStatus('current')
smExtsnTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 2), )
if mibBuilder.loadTexts: smExtsnTable.setStatus('current')
smExtsnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 2, 1), ).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smLangIndex"), (0, "DISMAN-SCRIPT-MIB", "smExtsnIndex"))
if mibBuilder.loadTexts: smExtsnEntry.setStatus('current')
smExtsnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: smExtsnIndex.setStatus('current')
smExtsnExtension = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smExtsnExtension.setStatus('current')
smExtsnVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smExtsnVersion.setStatus('current')
smExtsnVendor = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smExtsnVendor.setStatus('current')
smExtsnRevision = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smExtsnRevision.setStatus('current')
smExtsnDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 2, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: smExtsnDescr.setStatus('current')
smScriptObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 1, 3))
smScriptTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 3, 1), )
if mibBuilder.loadTexts: smScriptTable.setStatus('current')
smScriptEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1), ).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smScriptOwner"), (0, "DISMAN-SCRIPT-MIB", "smScriptName"))
if mibBuilder.loadTexts: smScriptEntry.setStatus('current')
smScriptOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: smScriptOwner.setStatus('current')
smScriptName = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: smScriptName.setStatus('current')
smScriptDescr = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 3), SnmpAdminString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smScriptDescr.setStatus('current')
smScriptLanguage = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smScriptLanguage.setStatus('current')
smScriptSource = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 5), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smScriptSource.setStatus('current')
smScriptAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("editing", 3))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smScriptAdminStatus.setStatus('current')
smScriptOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("editing", 3), ("retrieving", 4), ("compiling", 5), ("noSuchScript", 6), ("accessDenied", 7), ("wrongLanguage", 8), ("wrongVersion", 9), ("compilationFailed", 10), ("noResourcesLeft", 11), ("unknownProtocol", 12), ("protocolFailure", 13), ("genericError", 14))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: smScriptOperStatus.setStatus('current')
smScriptStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 8), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smScriptStorageType.setStatus('current')
smScriptRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smScriptRowStatus.setStatus('current')
smScriptError = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 10), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smScriptError.setStatus('current')
smScriptLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 1, 1, 11), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smScriptLastChange.setStatus('current')
smCodeTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 3, 2), )
if mibBuilder.loadTexts: smCodeTable.setStatus('current')
smCodeEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1), ).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smScriptOwner"), (0, "DISMAN-SCRIPT-MIB", "smScriptName"), (0, "DISMAN-SCRIPT-MIB", "smCodeIndex"))
if mibBuilder.loadTexts: smCodeEntry.setStatus('current')
smCodeIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: smCodeIndex.setStatus('current')
smCodeText = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smCodeText.setStatus('current')
smCodeRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 3, 2, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smCodeRowStatus.setStatus('current')
smRunObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 1, 4))
smLaunchTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 4, 1), )
if mibBuilder.loadTexts: smLaunchTable.setStatus('current')
smLaunchEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1), ).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smLaunchOwner"), (0, "DISMAN-SCRIPT-MIB", "smLaunchName"))
if mibBuilder.loadTexts: smLaunchEntry.setStatus('current')
smLaunchOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: smLaunchOwner.setStatus('current')
smLaunchName = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: smLaunchName.setStatus('current')
smLaunchScriptOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchScriptOwner.setStatus('current')
smLaunchScriptName = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchScriptName.setStatus('current')
smLaunchArgument = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 5), OctetString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchArgument.setStatus('current')
smLaunchMaxRunning = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchMaxRunning.setStatus('current')
smLaunchMaxCompleted = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchMaxCompleted.setStatus('current')
smLaunchLifeTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 8), TimeInterval().clone(360000)).setUnits('centi-seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchLifeTime.setStatus('current')
smLaunchExpireTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 9), TimeInterval().clone(360000)).setUnits('centi-seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchExpireTime.setStatus('current')
smLaunchStart = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchStart.setStatus('current')
smLaunchControl = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("abort", 1), ("suspend", 2), ("resume", 3), ("nop", 4))).clone('nop')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchControl.setStatus('current')
smLaunchAdminStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("autostart", 3))).clone('disabled')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchAdminStatus.setStatus('current')
smLaunchOperStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("expired", 3))).clone('disabled')).setMaxAccess("readonly")
if mibBuilder.loadTexts: smLaunchOperStatus.setStatus('current')
smLaunchRunIndexNext = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smLaunchRunIndexNext.setStatus('current')
smLaunchStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 15), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchStorageType.setStatus('current')
smLaunchRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchRowStatus.setStatus('current')
smLaunchError = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 17), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smLaunchError.setStatus('current')
smLaunchLastChange = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 18), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smLaunchLastChange.setStatus('current')
smLaunchRowExpireTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 1, 1, 19), TimeInterval().clone(2147483647)).setUnits('centi-seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: smLaunchRowExpireTime.setStatus('current')
smRunTable = MibTable((1, 3, 6, 1, 2, 1, 64, 1, 4, 2), )
if mibBuilder.loadTexts: smRunTable.setStatus('current')
smRunEntry = MibTableRow((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1), ).setIndexNames((0, "DISMAN-SCRIPT-MIB", "smLaunchOwner"), (0, "DISMAN-SCRIPT-MIB", "smLaunchName"), (0, "DISMAN-SCRIPT-MIB", "smRunIndex"))
if mibBuilder.loadTexts: smRunEntry.setStatus('current')
smRunIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: smRunIndex.setStatus('current')
smRunArgument = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 2), OctetString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smRunArgument.setStatus('current')
smRunStartTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 3), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smRunStartTime.setStatus('current')
smRunEndTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 4), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smRunEndTime.setStatus('current')
smRunLifeTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 5), TimeInterval()).setUnits('centi-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: smRunLifeTime.setStatus('current')
smRunExpireTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 6), TimeInterval()).setUnits('centi-seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: smRunExpireTime.setStatus('current')
smRunExitCode = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("noError", 1), ("halted", 2), ("lifeTimeExceeded", 3), ("noResourcesLeft", 4), ("languageError", 5), ("runtimeError", 6), ("invalidArgument", 7), ("securityViolation", 8), ("genericError", 9))).clone('noError')).setMaxAccess("readonly")
if mibBuilder.loadTexts: smRunExitCode.setStatus('current')
smRunResult = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 8), OctetString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smRunResult.setStatus('current')
smRunControl = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("abort", 1), ("suspend", 2), ("resume", 3), ("nop", 4))).clone('nop')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smRunControl.setStatus('current')
smRunState = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("initializing", 1), ("executing", 2), ("suspending", 3), ("suspended", 4), ("resuming", 5), ("aborting", 6), ("terminated", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smRunState.setStatus('current')
smRunError = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 11), SnmpAdminString().clone(hexValue="")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smRunError.setStatus('current')
smRunResultTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 12), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smRunResultTime.setStatus('current')
smRunErrorTime = MibTableColumn((1, 3, 6, 1, 2, 1, 64, 1, 4, 2, 1, 13), DateAndTime().clone(hexValue="0000000000000000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: smRunErrorTime.setStatus('current')
smTraps = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 2, 0))
smScriptAbort = NotificationType((1, 3, 6, 1, 2, 1, 64, 2, 0, 1)).setObjects(("DISMAN-SCRIPT-MIB", "smRunExitCode"), ("DISMAN-SCRIPT-MIB", "smRunEndTime"), ("DISMAN-SCRIPT-MIB", "smRunError"))
if mibBuilder.loadTexts: smScriptAbort.setStatus('current')
smScriptResult = NotificationType((1, 3, 6, 1, 2, 1, 64, 2, 0, 2)).setObjects(("DISMAN-SCRIPT-MIB", "smRunResult"))
if mibBuilder.loadTexts: smScriptResult.setStatus('current')
smScriptException = NotificationType((1, 3, 6, 1, 2, 1, 64, 2, 0, 3)).setObjects(("DISMAN-SCRIPT-MIB", "smRunError"))
if mibBuilder.loadTexts: smScriptException.setStatus('current')
smCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 3, 1))
smGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 64, 3, 2))
smCompliance2 = ModuleCompliance((1, 3, 6, 1, 2, 1, 64, 3, 1, 2)).setObjects(("DISMAN-SCRIPT-MIB", "smLanguageGroup"), ("DISMAN-SCRIPT-MIB", "smScriptGroup2"), ("DISMAN-SCRIPT-MIB", "smLaunchGroup2"), ("DISMAN-SCRIPT-MIB", "smRunGroup2"), ("DISMAN-SCRIPT-MIB", "smNotificationsGroup2"), ("DISMAN-SCRIPT-MIB", "smCodeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smCompliance2 = smCompliance2.setStatus('current')
smLanguageGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 1)).setObjects(("DISMAN-SCRIPT-MIB", "smLangLanguage"), ("DISMAN-SCRIPT-MIB", "smLangVersion"), ("DISMAN-SCRIPT-MIB", "smLangVendor"), ("DISMAN-SCRIPT-MIB", "smLangRevision"), ("DISMAN-SCRIPT-MIB", "smLangDescr"), ("DISMAN-SCRIPT-MIB", "smExtsnExtension"), ("DISMAN-SCRIPT-MIB", "smExtsnVersion"), ("DISMAN-SCRIPT-MIB", "smExtsnVendor"), ("DISMAN-SCRIPT-MIB", "smExtsnRevision"), ("DISMAN-SCRIPT-MIB", "smExtsnDescr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smLanguageGroup = smLanguageGroup.setStatus('current')
smScriptGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 7)).setObjects(("DISMAN-SCRIPT-MIB", "smScriptDescr"), ("DISMAN-SCRIPT-MIB", "smScriptLanguage"), ("DISMAN-SCRIPT-MIB", "smScriptSource"), ("DISMAN-SCRIPT-MIB", "smScriptAdminStatus"), ("DISMAN-SCRIPT-MIB", "smScriptOperStatus"), ("DISMAN-SCRIPT-MIB", "smScriptStorageType"), ("DISMAN-SCRIPT-MIB", "smScriptRowStatus"), ("DISMAN-SCRIPT-MIB", "smScriptError"), ("DISMAN-SCRIPT-MIB", "smScriptLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smScriptGroup2 = smScriptGroup2.setStatus('current')
smCodeGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 3)).setObjects(("DISMAN-SCRIPT-MIB", "smCodeText"), ("DISMAN-SCRIPT-MIB", "smCodeRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smCodeGroup = smCodeGroup.setStatus('current')
smLaunchGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 8)).setObjects(("DISMAN-SCRIPT-MIB", "smLaunchScriptOwner"), ("DISMAN-SCRIPT-MIB", "smLaunchScriptName"), ("DISMAN-SCRIPT-MIB", "smLaunchArgument"), ("DISMAN-SCRIPT-MIB", "smLaunchMaxRunning"), ("DISMAN-SCRIPT-MIB", "smLaunchMaxCompleted"), ("DISMAN-SCRIPT-MIB", "smLaunchLifeTime"), ("DISMAN-SCRIPT-MIB", "smLaunchExpireTime"), ("DISMAN-SCRIPT-MIB", "smLaunchStart"), ("DISMAN-SCRIPT-MIB", "smLaunchControl"), ("DISMAN-SCRIPT-MIB", "smLaunchAdminStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchOperStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchRunIndexNext"), ("DISMAN-SCRIPT-MIB", "smLaunchStorageType"), ("DISMAN-SCRIPT-MIB", "smLaunchRowStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchError"), ("DISMAN-SCRIPT-MIB", "smLaunchLastChange"), ("DISMAN-SCRIPT-MIB", "smLaunchRowExpireTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smLaunchGroup2 = smLaunchGroup2.setStatus('current')
smRunGroup2 = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 9)).setObjects(("DISMAN-SCRIPT-MIB", "smRunArgument"), ("DISMAN-SCRIPT-MIB", "smRunStartTime"), ("DISMAN-SCRIPT-MIB", "smRunEndTime"), ("DISMAN-SCRIPT-MIB", "smRunLifeTime"), ("DISMAN-SCRIPT-MIB", "smRunExpireTime"), ("DISMAN-SCRIPT-MIB", "smRunExitCode"), ("DISMAN-SCRIPT-MIB", "smRunResult"), ("DISMAN-SCRIPT-MIB", "smRunState"), ("DISMAN-SCRIPT-MIB", "smRunControl"), ("DISMAN-SCRIPT-MIB", "smRunError"), ("DISMAN-SCRIPT-MIB", "smRunResultTime"), ("DISMAN-SCRIPT-MIB", "smRunErrorTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smRunGroup2 = smRunGroup2.setStatus('current')
smNotificationsGroup2 = NotificationGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 10)).setObjects(("DISMAN-SCRIPT-MIB", "smScriptAbort"), ("DISMAN-SCRIPT-MIB", "smScriptResult"), ("DISMAN-SCRIPT-MIB", "smScriptException"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smNotificationsGroup2 = smNotificationsGroup2.setStatus('current')
smCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 64, 3, 1, 1)).setObjects(("DISMAN-SCRIPT-MIB", "smLanguageGroup"), ("DISMAN-SCRIPT-MIB", "smScriptGroup"), ("DISMAN-SCRIPT-MIB", "smLaunchGroup"), ("DISMAN-SCRIPT-MIB", "smRunGroup"), ("DISMAN-SCRIPT-MIB", "smCodeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smCompliance = smCompliance.setStatus('deprecated')
smScriptGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 2)).setObjects(("DISMAN-SCRIPT-MIB", "smScriptDescr"), ("DISMAN-SCRIPT-MIB", "smScriptLanguage"), ("DISMAN-SCRIPT-MIB", "smScriptSource"), ("DISMAN-SCRIPT-MIB", "smScriptAdminStatus"), ("DISMAN-SCRIPT-MIB", "smScriptOperStatus"), ("DISMAN-SCRIPT-MIB", "smScriptStorageType"), ("DISMAN-SCRIPT-MIB", "smScriptRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smScriptGroup = smScriptGroup.setStatus('deprecated')
smLaunchGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 4)).setObjects(("DISMAN-SCRIPT-MIB", "smLaunchScriptOwner"), ("DISMAN-SCRIPT-MIB", "smLaunchScriptName"), ("DISMAN-SCRIPT-MIB", "smLaunchArgument"), ("DISMAN-SCRIPT-MIB", "smLaunchMaxRunning"), ("DISMAN-SCRIPT-MIB", "smLaunchMaxCompleted"), ("DISMAN-SCRIPT-MIB", "smLaunchLifeTime"), ("DISMAN-SCRIPT-MIB", "smLaunchExpireTime"), ("DISMAN-SCRIPT-MIB", "smLaunchStart"), ("DISMAN-SCRIPT-MIB", "smLaunchControl"), ("DISMAN-SCRIPT-MIB", "smLaunchAdminStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchOperStatus"), ("DISMAN-SCRIPT-MIB", "smLaunchRunIndexNext"), ("DISMAN-SCRIPT-MIB", "smLaunchStorageType"), ("DISMAN-SCRIPT-MIB", "smLaunchRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smLaunchGroup = smLaunchGroup.setStatus('deprecated')
smRunGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 5)).setObjects(("DISMAN-SCRIPT-MIB", "smRunArgument"), ("DISMAN-SCRIPT-MIB", "smRunStartTime"), ("DISMAN-SCRIPT-MIB", "smRunEndTime"), ("DISMAN-SCRIPT-MIB", "smRunLifeTime"), ("DISMAN-SCRIPT-MIB", "smRunExpireTime"), ("DISMAN-SCRIPT-MIB", "smRunExitCode"), ("DISMAN-SCRIPT-MIB", "smRunResult"), ("DISMAN-SCRIPT-MIB", "smRunState"), ("DISMAN-SCRIPT-MIB", "smRunControl"), ("DISMAN-SCRIPT-MIB", "smRunError"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smRunGroup = smRunGroup.setStatus('deprecated')
smNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 64, 3, 2, 6)).setObjects(("DISMAN-SCRIPT-MIB", "smScriptAbort"), ("DISMAN-SCRIPT-MIB", "smScriptResult"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    smNotificationsGroup = smNotificationsGroup.setStatus('deprecated')
mibBuilder.exportSymbols("DISMAN-SCRIPT-MIB", smRunState=smRunState, smScriptObjects=smScriptObjects, smRunExpireTime=smRunExpireTime, smLaunchExpireTime=smLaunchExpireTime, smRunGroup=smRunGroup, smLaunchOperStatus=smLaunchOperStatus, smNotificationsGroup2=smNotificationsGroup2, smLaunchLifeTime=smLaunchLifeTime, smRunIndex=smRunIndex, smTraps=smTraps, smRunExitCode=smRunExitCode, smLaunchControl=smLaunchControl, smLaunchStart=smLaunchStart, smRunGroup2=smRunGroup2, smExtsnVersion=smExtsnVersion, smCodeRowStatus=smCodeRowStatus, smRunLifeTime=smRunLifeTime, smLaunchMaxRunning=smLaunchMaxRunning, smLaunchGroup=smLaunchGroup, PYSNMP_MODULE_ID=scriptMIB, smScriptError=smScriptError, smLaunchLastChange=smLaunchLastChange, smObjects=smObjects, smLangDescr=smLangDescr, smScriptResult=smScriptResult, smLanguageGroup=smLanguageGroup, smScriptException=smScriptException, smExtsnDescr=smExtsnDescr, smScriptGroup=smScriptGroup, smRunTable=smRunTable, smRunResultTime=smRunResultTime, smLaunchRunIndexNext=smLaunchRunIndexNext, scriptMIB=scriptMIB, smLangVendor=smLangVendor, smLangRevision=smLangRevision, smCompliance2=smCompliance2, smLangEntry=smLangEntry, smLaunchScriptName=smLaunchScriptName, smLaunchRowExpireTime=smLaunchRowExpireTime, smScriptRowStatus=smScriptRowStatus, smLaunchStorageType=smLaunchStorageType, smRunObjects=smRunObjects, smGroups=smGroups, smLaunchMaxCompleted=smLaunchMaxCompleted, smExtsnRevision=smExtsnRevision, smCompliances=smCompliances, smRunError=smRunError, smScriptTable=smScriptTable, smLaunchArgument=smLaunchArgument, smLaunchOwner=smLaunchOwner, smLaunchName=smLaunchName, smRunArgument=smRunArgument, smCodeEntry=smCodeEntry, smScriptOwner=smScriptOwner, smRunEntry=smRunEntry, smCodeIndex=smCodeIndex, smLaunchGroup2=smLaunchGroup2, smRunControl=smRunControl, smConformance=smConformance, smExtsnExtension=smExtsnExtension, smScriptDescr=smScriptDescr, smScriptGroup2=smScriptGroup2, smLaunchAdminStatus=smLaunchAdminStatus, smScriptEntry=smScriptEntry, smLaunchRowStatus=smLaunchRowStatus, smScriptSource=smScriptSource, smRunErrorTime=smRunErrorTime, smExtsnVendor=smExtsnVendor, smLangIndex=smLangIndex, smLaunchScriptOwner=smLaunchScriptOwner, smScriptOperStatus=smScriptOperStatus, smScriptLanguage=smScriptLanguage, smRunEndTime=smRunEndTime, smScriptLastChange=smScriptLastChange, smScriptAdminStatus=smScriptAdminStatus, smCodeText=smCodeText, smNotificationsGroup=smNotificationsGroup, smLaunchTable=smLaunchTable, smLaunchEntry=smLaunchEntry, smScriptStorageType=smScriptStorageType, smExtsnEntry=smExtsnEntry, smCodeTable=smCodeTable, smLaunchError=smLaunchError, smScriptAbort=smScriptAbort, smRunResult=smRunResult, smCompliance=smCompliance, smScriptName=smScriptName, smExtsnTable=smExtsnTable, smRunStartTime=smRunStartTime, smExtsnIndex=smExtsnIndex, smCodeGroup=smCodeGroup, smLangVersion=smLangVersion, smLangLanguage=smLangLanguage, smNotifications=smNotifications, smLangTable=smLangTable)
