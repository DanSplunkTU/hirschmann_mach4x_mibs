#
# PySNMP MIB module SIAE-MANOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-MANOP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:37:55 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, Gauge32, Unsigned32, IpAddress, Counter64, Bits, NotificationType, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "Gauge32", "Unsigned32", "IpAddress", "Counter64", "Bits", "NotificationType", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
manualOperation = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 71))
manualOperation.setRevisions(('2014-03-17 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: manualOperation.setLastUpdated('201403170000Z')
if mibBuilder.loadTexts: manualOperation.setOrganization('SIAE MICROELETTRONICA spa')
manualOpTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 0))
manualOpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpMibVersion.setStatus('current')
manualOpTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2), )
if mibBuilder.loadTexts: manualOpTable.setStatus('current')
manualOpRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1), ).setIndexNames((0, "SIAE-MANOP-MIB", "manualOpId"))
if mibBuilder.loadTexts: manualOpRecord.setStatus('current')
manualOpId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpId.setStatus('current')
manualOpObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpObjectId.setStatus('current')
manualOpEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpEventTime.setStatus('current')
manualOpValueType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("integer32", 1), ("objectId", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpValueType.setStatus('current')
manualOpIntegerVal = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpIntegerVal.setStatus('current')
manualOpOidVal = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpOidVal.setStatus('current')
manualOpActive = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 3), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpActive.setStatus('current')
manualOpActiveSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 4), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: manualOpActiveSeverityCode.setStatus('current')
manualOpTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 172800)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: manualOpTimeOut.setStatus('current')
mibBuilder.exportSymbols("SIAE-MANOP-MIB", manualOpMibVersion=manualOpMibVersion, manualOperation=manualOperation, manualOpId=manualOpId, manualOpTable=manualOpTable, manualOpRecord=manualOpRecord, manualOpIntegerVal=manualOpIntegerVal, manualOpEventTime=manualOpEventTime, PYSNMP_MODULE_ID=manualOperation, manualOpValueType=manualOpValueType, manualOpActive=manualOpActive, manualOpObjectId=manualOpObjectId, manualOpActiveSeverityCode=manualOpActiveSeverityCode, manualOpTrap=manualOpTrap, manualOpOidVal=manualOpOidVal, manualOpTimeOut=manualOpTimeOut)
