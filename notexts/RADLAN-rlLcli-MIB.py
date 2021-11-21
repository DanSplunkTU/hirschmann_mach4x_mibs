#
# PySNMP MIB module RADLAN-rlLcli-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-rlLcli-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:13 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, NotificationType, Counter64, Gauge32, ObjectIdentity, MibIdentifier, Bits, ModuleIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "NotificationType", "Counter64", "Gauge32", "ObjectIdentity", "MibIdentifier", "Bits", "ModuleIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Unsigned32")
TextualConvention, TruthValue, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "RowStatus")
rlLCli = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 74))
rlLCli.setRevisions(('2005-04-11 00:00', '2005-03-28 00:00', '2004-03-26 00:00',))
if mibBuilder.loadTexts: rlLCli.setLastUpdated('200503280000Z')
if mibBuilder.loadTexts: rlLCli.setOrganization('Radlan Computer Communications Ltd.')
rlLCliMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLCliMibVersion.setStatus('current')
rlLCliTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTimeout.setStatus('current')
rlLCliHistoryEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 3), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliHistoryEnable.setStatus('current')
rlLCliHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliHistorySize.setStatus('current')
rlLcliCommandLevelTable = MibTable((1, 3, 6, 1, 4, 1, 89, 74, 5), )
if mibBuilder.loadTexts: rlLcliCommandLevelTable.setStatus('current')
rlLcliCommandLevelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 74, 5, 1), ).setIndexNames((0, "RADLAN-rlLcli-MIB", "rlLcliCommandLevelCommandName"), (0, "RADLAN-rlLcli-MIB", "rlLcliCommandLevelContextName"))
if mibBuilder.loadTexts: rlLcliCommandLevelEntry.setStatus('current')
rlLcliCommandLevelCommandName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 1), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelCommandName.setStatus('current')
rlLcliCommandLevelContextName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelContextName.setStatus('current')
rlLcliCommandLevelInsertTime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 3), TimeTicks()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelInsertTime.setStatus('current')
rlLcliCommandLevelCommandLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelCommandLevel.setStatus('current')
rlLcliCommandLevelActionMode = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("set", 1), ("reset", 2), ("setAll", 3), ("resetAll", 4))).clone('set')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelActionMode.setStatus('current')
rlLcliCommandLevelStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 74, 5, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLcliCommandLevelStatus.setStatus('current')
rlLCliSshTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliSshTimeout.setStatus('current')
rlLCliTelnetTimeout = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 3932159)).clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTelnetTimeout.setStatus('current')
rlLCliTelnetHistoryEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 8), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTelnetHistoryEnable.setStatus('current')
rlLCliTelnetHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliTelnetHistorySize.setStatus('current')
rlLCliSshHistoryEnable = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 10), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliSshHistoryEnable.setStatus('current')
rlLCliSshHistorySize = MibScalar((1, 3, 6, 1, 4, 1, 89, 74, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 256)).clone(10)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLCliSshHistorySize.setStatus('current')
mibBuilder.exportSymbols("RADLAN-rlLcli-MIB", rlLCliTelnetHistoryEnable=rlLCliTelnetHistoryEnable, rlLCliHistorySize=rlLCliHistorySize, rlLcliCommandLevelStatus=rlLcliCommandLevelStatus, PYSNMP_MODULE_ID=rlLCli, rlLCliSshTimeout=rlLCliSshTimeout, rlLcliCommandLevelActionMode=rlLcliCommandLevelActionMode, rlLCliTelnetTimeout=rlLCliTelnetTimeout, rlLcliCommandLevelEntry=rlLcliCommandLevelEntry, rlLcliCommandLevelTable=rlLcliCommandLevelTable, rlLcliCommandLevelCommandLevel=rlLcliCommandLevelCommandLevel, rlLCliHistoryEnable=rlLCliHistoryEnable, rlLcliCommandLevelCommandName=rlLcliCommandLevelCommandName, rlLCliMibVersion=rlLCliMibVersion, rlLcliCommandLevelContextName=rlLcliCommandLevelContextName, rlLCliTelnetHistorySize=rlLCliTelnetHistorySize, rlLCliTimeout=rlLCliTimeout, rlLCli=rlLCli, rlLcliCommandLevelInsertTime=rlLcliCommandLevelInsertTime, rlLCliSshHistoryEnable=rlLCliSshHistoryEnable, rlLCliSshHistorySize=rlLCliSshHistorySize)
