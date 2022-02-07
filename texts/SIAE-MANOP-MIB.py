#
# PySNMP MIB module SIAE-MANOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-MANOP-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:19:33 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
AlarmStatus, AlarmSeverityCode = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmStatus", "AlarmSeverityCode")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, TimeTicks, Integer32, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Bits, Counter32, Counter64, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "TimeTicks", "Integer32", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Bits", "Counter32", "Counter64", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
manualOperation = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 71))
manualOperation.setRevisions(('2014-03-17 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: manualOperation.setRevisionsDescriptions(('Fixed DESCRIPTION of manualOpActiveSeverityCode\n            ', 'Improved description of manualOpMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: manualOperation.setLastUpdated('201403170000Z')
if mibBuilder.loadTexts: manualOperation.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: manualOperation.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: manualOperation.setDescription('Manual Operation management.\n            ')
manualOpTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 0))
manualOpMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpMibVersion.setStatus('current')
if mibBuilder.loadTexts: manualOpMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
manualOpTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2), )
if mibBuilder.loadTexts: manualOpTable.setStatus('current')
if mibBuilder.loadTexts: manualOpTable.setDescription('Table with manual operation record.')
manualOpRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1), ).setIndexNames((0, "SIAE-MANOP-MIB", "manualOpId"))
if mibBuilder.loadTexts: manualOpRecord.setStatus('current')
if mibBuilder.loadTexts: manualOpRecord.setDescription('Manual operation record.')
manualOpId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpId.setStatus('current')
if mibBuilder.loadTexts: manualOpId.setDescription('Manual operation index.')
manualOpObjectId = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpObjectId.setStatus('current')
if mibBuilder.loadTexts: manualOpObjectId.setDescription('Object identifier of the manual operation active element.')
manualOpEventTime = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpEventTime.setStatus('current')
if mibBuilder.loadTexts: manualOpEventTime.setDescription('The time (in seconds since 01-Gen-1970) when the event was \n             registered in the table.')
manualOpValueType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("integer32", 1), ("objectId", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpValueType.setStatus('current')
if mibBuilder.loadTexts: manualOpValueType.setDescription('The type of the value. One and only one of the value object\n             that follow is used for a given row in this table, based on\n             this type.')
manualOpIntegerVal = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpIntegerVal.setStatus('current')
if mibBuilder.loadTexts: manualOpIntegerVal.setDescription("The value when manualOpValueType is 'integer32'.")
manualOpOidVal = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 2, 1, 6), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpOidVal.setStatus('current')
if mibBuilder.loadTexts: manualOpOidVal.setDescription("The value when manualOpValueType is 'objectId'.")
manualOpActive = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 3), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: manualOpActive.setStatus('current')
if mibBuilder.loadTexts: manualOpActive.setDescription('Manual Operation active on the equipment.')
manualOpActiveSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 4), AlarmSeverityCode().clone('warningTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: manualOpActiveSeverityCode.setStatus('current')
if mibBuilder.loadTexts: manualOpActiveSeverityCode.setDescription('Defines the severity associated to manualOpActive  \n             and enables/disables the trap generation on status change event.')
manualOpTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 71, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 172800)).clone(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: manualOpTimeOut.setStatus('current')
if mibBuilder.loadTexts: manualOpTimeOut.setDescription('This object defines the time (in seconds) after wich the manual\n             operations are cleared. The maximum value is equivalent to 48 hours.\n             A zero means no Time-out.')
mibBuilder.exportSymbols("SIAE-MANOP-MIB", manualOpTable=manualOpTable, PYSNMP_MODULE_ID=manualOperation, manualOpTrap=manualOpTrap, manualOpEventTime=manualOpEventTime, manualOpValueType=manualOpValueType, manualOpIntegerVal=manualOpIntegerVal, manualOpRecord=manualOpRecord, manualOpId=manualOpId, manualOperation=manualOperation, manualOpObjectId=manualOpObjectId, manualOpActive=manualOpActive, manualOpOidVal=manualOpOidVal, manualOpActiveSeverityCode=manualOpActiveSeverityCode, manualOpTimeOut=manualOpTimeOut, manualOpMibVersion=manualOpMibVersion)
