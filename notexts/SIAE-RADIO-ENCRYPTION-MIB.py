#
# PySNMP MIB module SIAE-RADIO-ENCRYPTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-RADIO-ENCRYPTION-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:44:11 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
AlarmSeverityCode, AlarmStatus = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, ModuleIdentity, iso, Gauge32, Unsigned32, ObjectIdentity, Integer32, NotificationType, TimeTicks, Bits, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "iso", "Gauge32", "Unsigned32", "ObjectIdentity", "Integer32", "NotificationType", "TimeTicks", "Bits", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
radioEncrypt = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 96))
radioEncrypt.setRevisions(('2015-07-20 00:00',))
if mibBuilder.loadTexts: radioEncrypt.setLastUpdated('201507200000Z')
if mibBuilder.loadTexts: radioEncrypt.setOrganization('SIAE MICROELETTRONICA spa')
rdEncryptMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdEncryptMibVersion.setStatus('current')
rdEncryptTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2), )
if mibBuilder.loadTexts: rdEncryptTable.setStatus('current')
rdEncryptTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1), ).setIndexNames((0, "SIAE-RADIO-ENCRYPTION-MIB", "rdEncryptIfIndex"))
if mibBuilder.loadTexts: rdEncryptTableEntry.setStatus('current')
rdEncryptIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: rdEncryptIfIndex.setStatus('current')
rdEncryptRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdEncryptRowStatus.setStatus('current')
rdEncryptAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdEncryptAdminStatus.setStatus('current')
rdEncryptAlgo = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("aes128", 1), ("aes256", 2))).clone('aes256')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdEncryptAlgo.setStatus('current')
rdEncryptAlgoMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("aesModeElectronicCodebook", 1), ("aesModeCipherBlockChaining", 2), ("aesModeCipherFeedback", 3), ("aesModeOutputFeedback", 4), ("aesModeCounter", 5))).clone('aesModeCounter')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdEncryptAlgoMode.setStatus('current')
rdEncryptKeyMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("manualEnteredKey", 1), ("automaticKeyGeneration", 2))).clone('manualEnteredKey')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdEncryptKeyMode.setStatus('current')
rdEncryptKey = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 7), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(16, 16), ValueSizeConstraint(32, 32), )).clone(hexValue="00")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdEncryptKey.setStatus('current')
rdEncryptKeyLifeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1096)).clone(7)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rdEncryptKeyLifeTime.setStatus('current')
rdEncryptMismatchAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 2, 1, 9), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rdEncryptMismatchAlarm.setStatus('current')
rdEncryptSystemControl = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("start", 1), ("shutdown", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdEncryptSystemControl.setStatus('current')
rdEncryptMismatchAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 96, 4), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rdEncryptMismatchAlarmSeverityCode.setStatus('current')
mibBuilder.exportSymbols("SIAE-RADIO-ENCRYPTION-MIB", rdEncryptSystemControl=rdEncryptSystemControl, rdEncryptKeyLifeTime=rdEncryptKeyLifeTime, rdEncryptRowStatus=rdEncryptRowStatus, rdEncryptIfIndex=rdEncryptIfIndex, radioEncrypt=radioEncrypt, rdEncryptAlgo=rdEncryptAlgo, rdEncryptMismatchAlarm=rdEncryptMismatchAlarm, rdEncryptKeyMode=rdEncryptKeyMode, rdEncryptMismatchAlarmSeverityCode=rdEncryptMismatchAlarmSeverityCode, rdEncryptAdminStatus=rdEncryptAdminStatus, PYSNMP_MODULE_ID=radioEncrypt, rdEncryptTableEntry=rdEncryptTableEntry, rdEncryptKey=rdEncryptKey, rdEncryptMibVersion=rdEncryptMibVersion, rdEncryptTable=rdEncryptTable, rdEncryptAlgoMode=rdEncryptAlgoMode)
