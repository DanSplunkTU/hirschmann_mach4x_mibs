#
# PySNMP MIB module SIAE-AGGRL1-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-AGGRL1-MANAGEMENT-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:44:13 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
AlarmSeverityCode, AlarmStatus = mibBuilder.importSymbols("SIAE-ALARM-MIB", "AlarmSeverityCode", "AlarmStatus")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Bits, Gauge32, Unsigned32, ModuleIdentity, iso, IpAddress, Counter32, NotificationType, MibIdentifier, Integer32, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Bits", "Gauge32", "Unsigned32", "ModuleIdentity", "iso", "IpAddress", "Counter32", "NotificationType", "MibIdentifier", "Integer32", "Counter64", "ObjectIdentity")
RowStatus, StorageType, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "StorageType", "DisplayString", "TextualConvention")
aggregationL1 = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 83))
aggregationL1.setRevisions(('2014-09-29 00:00', '2014-05-26 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aggregationL1.setRevisionsDescriptions(('MIB version 01.00.01.\n             - Added table aggrL1ConnectionTable.\n             - Added TEXTUAL-CONVENTION AggregableType\n             - Revised document form.\n            ', 'Initial version 01.00.00.\n            ',))
if mibBuilder.loadTexts: aggregationL1.setLastUpdated('201409290000Z')
if mibBuilder.loadTexts: aggregationL1.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: aggregationL1.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: aggregationL1.setDescription('Level 1 aggregations management for SIAE equipments.\n            ')
class AggregableType(TextualConvention, Integer32):
    description = 'Type of aggregable interface'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("other", 1), ("radio", 2), ("lan", 3))

aggrL1MibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1MibVersion.setStatus('current')
if mibBuilder.loadTexts: aggrL1MibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
aggrL1CapabilityTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2), )
if mibBuilder.loadTexts: aggrL1CapabilityTable.setStatus('current')
if mibBuilder.loadTexts: aggrL1CapabilityTable.setDescription('A list of capability entries to show the manager all the \n            possible L1 aggregations.')
aggrL1CapabilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1), ).setIndexNames((0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1CapabilityAggregableIndex"), (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1CapabilityAggregableType"), (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1CapabilityAggregatorIndex"))
if mibBuilder.loadTexts: aggrL1CapabilityEntry.setStatus('current')
if mibBuilder.loadTexts: aggrL1CapabilityEntry.setDescription('An entry showing the manager the aggregator and the aggregable\n             interfaces that can be involved in L1 aggregations.')
aggrL1CapabilityAggregableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1CapabilityAggregableIndex.setStatus('current')
if mibBuilder.loadTexts: aggrL1CapabilityAggregableIndex.setDescription('This object defines the aggregable physical interface that can be used \n            in a L1 aggregation. If the interface is a radio, this object matches \n            the index in radioTable, otherwise this object corresponds to the \n            ifIndex in ifTable.')
aggrL1CapabilityAggregableType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1, 2), AggregableType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1CapabilityAggregableType.setStatus('current')
if mibBuilder.loadTexts: aggrL1CapabilityAggregableType.setDescription('L1 aggregable interface type. \n            ')
aggrL1CapabilityAggregatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 2, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1CapabilityAggregatorIndex.setStatus('current')
if mibBuilder.loadTexts: aggrL1CapabilityAggregatorIndex.setDescription('This object defines the ifIndex of each aggregator physical\n            interface that can be used as source of a L1 aggregation.')
aggrL1Table = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3), )
if mibBuilder.loadTexts: aggrL1Table.setStatus('current')
if mibBuilder.loadTexts: aggrL1Table.setDescription('A list of L1 aggregation entries.')
aggrL1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1), ).setIndexNames((0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1AggregableIndex"), (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1AggregableType"))
if mibBuilder.loadTexts: aggrL1Entry.setStatus('current')
if mibBuilder.loadTexts: aggrL1Entry.setDescription('An entry containing management information applicable to a L1\n             aggregation. Rows with the same aggrL1AggregatorIndex share \n             ethernet traffic and made up a L1 aggregation.')
aggrL1AggregableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1AggregableIndex.setStatus('current')
if mibBuilder.loadTexts: aggrL1AggregableIndex.setDescription('This object defines the aggregable physical interface used in a given \n            L1 aggregation. If the interface is a radio, this object matches \n            the index in radioTable, otherwise, this object corresponds to the \n            ifIndex in ifTable. It must correspond to a valid aggregable interface\n            in aggrL1CapabilityTable.')
aggrL1AggregableType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 2), AggregableType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1AggregableType.setStatus('current')
if mibBuilder.loadTexts: aggrL1AggregableType.setDescription('Interface type of the respective aggregable L1 interface.')
aggrL1AggregatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrL1AggregatorIndex.setStatus('current')
if mibBuilder.loadTexts: aggrL1AggregatorIndex.setDescription('This object defines the ifIndex of the physical interface \n            used as source of a given L1 aggregation. It must correspond to a\n            valid aggregator interface in aggrL1CapabilityTable.')
aggrL1StorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 4), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrL1StorageType.setStatus('current')
if mibBuilder.loadTexts: aggrL1StorageType.setDescription('The storage type for this conceptual row.')
aggrL1Rowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 3, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aggrL1Rowstatus.setStatus('current')
if mibBuilder.loadTexts: aggrL1Rowstatus.setDescription('Status of this conceptual row in aggrL1Table.')
aggrL1AlarmTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4), )
if mibBuilder.loadTexts: aggrL1AlarmTable.setStatus('current')
if mibBuilder.loadTexts: aggrL1AlarmTable.setDescription('Table with alarms related to L1 aggregations. NE agent adds an entry \n             in this table when at least two aggregable interfaces (in aggrL1Table) are\n             connected to the same aggregator interface. NE agent removes an entry in \n             this table when a L1 aggregation made up of more than one aggregable \n             interfaces is modified in a L1 aggregation composed by one or less \n             aggregable interfaces.')
aggrL1AlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1), ).setIndexNames((0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1AlarmAggregatorIndex"))
if mibBuilder.loadTexts: aggrL1AlarmEntry.setStatus('current')
if mibBuilder.loadTexts: aggrL1AlarmEntry.setDescription('AggrL1Alarm entry.')
aggrL1AlarmAggregatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 1), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1AlarmAggregatorIndex.setStatus('current')
if mibBuilder.loadTexts: aggrL1AlarmAggregatorIndex.setDescription('This object defines the ifIndex of the physical interface \n            used as source of a given L1 aggregation.')
aggrL1FailAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 2), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1FailAlarm.setStatus('current')
if mibBuilder.loadTexts: aggrL1FailAlarm.setDescription('L1 Aggregation Fail Alarm with associated severity.')
aggrL1DegradeAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 3), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1DegradeAlarm.setStatus('current')
if mibBuilder.loadTexts: aggrL1DegradeAlarm.setDescription('L1 Aggregation Degrade Alarm with associated severity.')
aggrL1RealignmentAlarm = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 4, 1, 4), AlarmStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1RealignmentAlarm.setStatus('current')
if mibBuilder.loadTexts: aggrL1RealignmentAlarm.setDescription('L1 Aggregation Realignment Alarm with associated severity.')
aggrL1FailAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 5), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aggrL1FailAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: aggrL1FailAlarmSeverityCode.setDescription('Defines the severity associated to the L1 aggregation fail alarm\n             and enables/disables the trap generation on status change event.')
aggrL1DegradeAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 6), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aggrL1DegradeAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: aggrL1DegradeAlarmSeverityCode.setDescription('Defines the severity associated to the L1 aggregation degrade alarm\n             and enables/disables the trap generation on status change event.')
aggrL1RealignmentAlarmSeverityCode = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 7), AlarmSeverityCode().clone('majorTrapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aggrL1RealignmentAlarmSeverityCode.setStatus('current')
if mibBuilder.loadTexts: aggrL1RealignmentAlarmSeverityCode.setDescription('Defines the severity associated to the L1 aggregation realignment alarm\n             and enables/disables the trap generation on status change event.')
aggrL1ConnectionTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8), )
if mibBuilder.loadTexts: aggrL1ConnectionTable.setStatus('current')
if mibBuilder.loadTexts: aggrL1ConnectionTable.setDescription('A list of associations between aggregables and traffic source.')
aggrL1ConnectionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1), ).setIndexNames((0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1ConnAggregableIndex"), (0, "SIAE-AGGRL1-MANAGEMENT-MIB", "aggrL1ConnAggregableType"))
if mibBuilder.loadTexts: aggrL1ConnectionEntry.setStatus('current')
if mibBuilder.loadTexts: aggrL1ConnectionEntry.setDescription('An entry containing an associations between aggregable radios and\n             traffic source. Rows with the same aggrL1ConnAggregatorIndex\n             identifies aggregable radios that are connected to the same traffic\n             source. In the 1+1 radio configuration, traffic is the same on\n             each aggregable radio, in other radio configurations, traffic is\n             shared between each aggregable radio.')
aggrL1ConnAggregableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1ConnAggregableIndex.setStatus('current')
if mibBuilder.loadTexts: aggrL1ConnAggregableIndex.setDescription('This object defines the aggregable physical interface used in a\n            given  L1 aggregation (or radio protection). If the interface is a\n            radio, this object matches the index in radioTable, otherwise,\n            this object corresponds to the  ifIndex in ifTable.\n            It must correspond to a valid aggregable interface in\n            aggrL1CapabilityTable.')
aggrL1ConnAggregableType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1, 2), AggregableType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1ConnAggregableType.setStatus('current')
if mibBuilder.loadTexts: aggrL1ConnAggregableType.setDescription('Interface type of the respective aggregable L1 interface.')
aggrL1ConnAggregatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 83, 8, 1, 3), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aggrL1ConnAggregatorIndex.setStatus('current')
if mibBuilder.loadTexts: aggrL1ConnAggregatorIndex.setDescription('This object defines the ifIndex of the physical interface \n            used as source of a given L1 aggregation. It must correspond to a\n            valid aggregator interface in aggrL1CapabilityTable.')
mibBuilder.exportSymbols("SIAE-AGGRL1-MANAGEMENT-MIB", aggrL1AggregableType=aggrL1AggregableType, AggregableType=AggregableType, aggrL1AlarmTable=aggrL1AlarmTable, aggrL1StorageType=aggrL1StorageType, aggrL1RealignmentAlarmSeverityCode=aggrL1RealignmentAlarmSeverityCode, aggrL1MibVersion=aggrL1MibVersion, aggrL1CapabilityAggregatorIndex=aggrL1CapabilityAggregatorIndex, aggrL1AlarmEntry=aggrL1AlarmEntry, aggrL1ConnAggregableIndex=aggrL1ConnAggregableIndex, aggrL1AggregableIndex=aggrL1AggregableIndex, aggrL1Entry=aggrL1Entry, aggrL1Rowstatus=aggrL1Rowstatus, aggregationL1=aggregationL1, aggrL1AlarmAggregatorIndex=aggrL1AlarmAggregatorIndex, PYSNMP_MODULE_ID=aggregationL1, aggrL1FailAlarm=aggrL1FailAlarm, aggrL1FailAlarmSeverityCode=aggrL1FailAlarmSeverityCode, aggrL1DegradeAlarmSeverityCode=aggrL1DegradeAlarmSeverityCode, aggrL1CapabilityTable=aggrL1CapabilityTable, aggrL1Table=aggrL1Table, aggrL1ConnAggregableType=aggrL1ConnAggregableType, aggrL1CapabilityAggregableIndex=aggrL1CapabilityAggregableIndex, aggrL1RealignmentAlarm=aggrL1RealignmentAlarm, aggrL1CapabilityAggregableType=aggrL1CapabilityAggregableType, aggrL1ConnAggregatorIndex=aggrL1ConnAggregatorIndex, aggrL1ConnectionEntry=aggrL1ConnectionEntry, aggrL1ConnectionTable=aggrL1ConnectionTable, aggrL1DegradeAlarm=aggrL1DegradeAlarm, aggrL1CapabilityEntry=aggrL1CapabilityEntry, aggrL1AggregatorIndex=aggrL1AggregatorIndex)
