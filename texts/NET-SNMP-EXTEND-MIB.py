#
# PySNMP MIB module NET-SNMP-EXTEND-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/netsnmp/NET-SNMP-EXTEND-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:13:27 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
nsExtensions, = mibBuilder.importSymbols("NET-SNMP-AGENT-MIB", "nsExtensions")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Bits, NotificationType, TimeTicks, IpAddress, Gauge32, ObjectIdentity, iso, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, MibIdentifier, ModuleIdentity, Counter32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "TimeTicks", "IpAddress", "Gauge32", "ObjectIdentity", "iso", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "MibIdentifier", "ModuleIdentity", "Counter32", "Integer32")
DisplayString, StorageType, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "StorageType", "TextualConvention", "RowStatus")
netSnmpExtendMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8072, 1, 3, 1))
netSnmpExtendMIB.setRevisions(('2010-03-17 00:00', '2004-05-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netSnmpExtendMIB.setRevisionsDescriptions(('Fixed inconsistencies in the definition of nsExtendConfigTable.', 'First revision.',))
if mibBuilder.loadTexts: netSnmpExtendMIB.setLastUpdated('201003170000Z')
if mibBuilder.loadTexts: netSnmpExtendMIB.setOrganization('www.net-snmp.org')
if mibBuilder.loadTexts: netSnmpExtendMIB.setContactInfo('postal:   Wes Hardaker\n                    P.O. Box 382\n                    Davis CA  95617\n\n          email:    net-snmp-coders@lists.sourceforge.net')
if mibBuilder.loadTexts: netSnmpExtendMIB.setDescription('Defines a framework for scripted extensions for the Net-SNMP agent.')
nsExtendObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2))
nsExtendGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8072, 1, 3, 3))
nsExtendNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendNumEntries.setStatus('current')
if mibBuilder.loadTexts: nsExtendNumEntries.setDescription('The number of rows in the nsExtendConfigTable')
nsExtendConfigTable = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2), )
if mibBuilder.loadTexts: nsExtendConfigTable.setStatus('current')
if mibBuilder.loadTexts: nsExtendConfigTable.setDescription('A table of scripted extensions - configuration and (basic) output.')
nsExtendConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1), ).setIndexNames((0, "NET-SNMP-EXTEND-MIB", "nsExtendToken"))
if mibBuilder.loadTexts: nsExtendConfigEntry.setStatus('current')
if mibBuilder.loadTexts: nsExtendConfigEntry.setDescription('A conceptual row within the extension table.')
nsExtendToken = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 1), DisplayString())
if mibBuilder.loadTexts: nsExtendToken.setStatus('current')
if mibBuilder.loadTexts: nsExtendToken.setDescription('An arbitrary token to identify this extension entry')
nsExtendCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 2), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendCommand.setStatus('current')
if mibBuilder.loadTexts: nsExtendCommand.setDescription('The full path of the command binary (or script) to run')
nsExtendArgs = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 3), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendArgs.setStatus('current')
if mibBuilder.loadTexts: nsExtendArgs.setDescription('Any command-line arguments for the command')
nsExtendInput = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 4), DisplayString().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendInput.setStatus('current')
if mibBuilder.loadTexts: nsExtendInput.setDescription('The standard input for the command')
nsExtendCacheTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 5), Integer32().clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendCacheTime.setStatus('current')
if mibBuilder.loadTexts: nsExtendCacheTime.setDescription('The length of time for which the output of\n       this command will be cached.  During this time,\n       retrieving the output-related values will not\n       reinvoke the command.\n       A value of -1 indicates that the output results\n       should not be cached at all, and retrieving each\n       individual output-related value will invoke the\n       command afresh.')
nsExtendExecType = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exec", 1), ("shell", 2))).clone('exec')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendExecType.setStatus('current')
if mibBuilder.loadTexts: nsExtendExecType.setDescription('The mechanism used to invoke the command.')
nsExtendRunType = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("run-on-read", 1), ("run-on-set", 2), ("run-command", 3))).clone('run-on-read')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendRunType.setStatus('current')
if mibBuilder.loadTexts: nsExtendRunType.setDescription("Used to implement 'push-button' command invocation.\n       The command for a 'run-on-read' entry will be invoked\n       whenever one of the corresponding output-related\n       instances is requested (and assuming the cached value\n       is not still current).\n       The command for a 'run-on-set' entry will only be invoked\n       on receipt of a SET assignment for this object with the\n       value 'run-command'.\n       Reading an instance of this object will always return either\n       'run-on-read' or 'run-on-set'.\n      ")
nsExtendStorage = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 20), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendStorage.setStatus('current')
if mibBuilder.loadTexts: nsExtendStorage.setDescription('The storage type for this conceptual row.')
nsExtendStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 2, 1, 21), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: nsExtendStatus.setStatus('current')
if mibBuilder.loadTexts: nsExtendStatus.setDescription("Used to create new rows in the table, in the standard manner.\n       Note that is valid for an instance to be left with the value\n       notInService(2) indefinitely - i.e. the meaning of 'abnormally\n       long' (see RFC 2579, RowStatus) for this table is infinite.")
nsExtendOutput1Table = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3), )
if mibBuilder.loadTexts: nsExtendOutput1Table.setStatus('current')
if mibBuilder.loadTexts: nsExtendOutput1Table.setDescription('A table of scripted extensions - configuration and (basic) output.')
nsExtendOutput1Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1), )
nsExtendConfigEntry.registerAugmentions(("NET-SNMP-EXTEND-MIB", "nsExtendOutput1Entry"))
nsExtendOutput1Entry.setIndexNames(*nsExtendConfigEntry.getIndexNames())
if mibBuilder.loadTexts: nsExtendOutput1Entry.setStatus('current')
if mibBuilder.loadTexts: nsExtendOutput1Entry.setDescription('A conceptual row within the extension table.')
nsExtendOutput1Line = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendOutput1Line.setStatus('current')
if mibBuilder.loadTexts: nsExtendOutput1Line.setDescription('The first line of output from the command')
nsExtendOutputFull = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendOutputFull.setStatus('current')
if mibBuilder.loadTexts: nsExtendOutputFull.setDescription('The full output from the command, as a single string')
nsExtendOutNumLines = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendOutNumLines.setStatus('current')
if mibBuilder.loadTexts: nsExtendOutNumLines.setDescription('The number of lines of output (and hence\n       the number of rows in nsExtendOutputTable\n       relating to this particular entry).')
nsExtendResult = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 3, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendResult.setStatus('current')
if mibBuilder.loadTexts: nsExtendResult.setDescription('The return value of the command.')
nsExtendOutput2Table = MibTable((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4), )
if mibBuilder.loadTexts: nsExtendOutput2Table.setStatus('current')
if mibBuilder.loadTexts: nsExtendOutput2Table.setDescription('A table of (line-based) output from scripted extensions.')
nsExtendOutput2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4, 1), ).setIndexNames((0, "NET-SNMP-EXTEND-MIB", "nsExtendToken"), (0, "NET-SNMP-EXTEND-MIB", "nsExtendLineIndex"))
if mibBuilder.loadTexts: nsExtendOutput2Entry.setStatus('current')
if mibBuilder.loadTexts: nsExtendOutput2Entry.setDescription('A conceptual row within the line-based output table.')
nsExtendLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1024)))
if mibBuilder.loadTexts: nsExtendLineIndex.setStatus('current')
if mibBuilder.loadTexts: nsExtendLineIndex.setDescription('The index of this line of output.\n       For a given nsExtendToken, this will run from\n       1 to the corresponding value of nsExtendNumLines.')
nsExtendOutLine = MibTableColumn((1, 3, 6, 1, 4, 1, 8072, 1, 3, 2, 4, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nsExtendOutLine.setStatus('current')
if mibBuilder.loadTexts: nsExtendOutLine.setDescription('A single line of output from the extension command.')
nsExtendConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8072, 1, 3, 3, 1)).setObjects(("NET-SNMP-EXTEND-MIB", "nsExtendCommand"), ("NET-SNMP-EXTEND-MIB", "nsExtendArgs"), ("NET-SNMP-EXTEND-MIB", "nsExtendInput"), ("NET-SNMP-EXTEND-MIB", "nsExtendCacheTime"), ("NET-SNMP-EXTEND-MIB", "nsExtendExecType"), ("NET-SNMP-EXTEND-MIB", "nsExtendRunType"), ("NET-SNMP-EXTEND-MIB", "nsExtendStorage"), ("NET-SNMP-EXTEND-MIB", "nsExtendStatus"), ("NET-SNMP-EXTEND-MIB", "nsExtendNumEntries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nsExtendConfigGroup = nsExtendConfigGroup.setStatus('current')
if mibBuilder.loadTexts: nsExtendConfigGroup.setDescription('Objects relating to the configuration of extension commands.')
nsExtendOutputGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8072, 1, 3, 3, 2)).setObjects(("NET-SNMP-EXTEND-MIB", "nsExtendOutNumLines"), ("NET-SNMP-EXTEND-MIB", "nsExtendResult"), ("NET-SNMP-EXTEND-MIB", "nsExtendOutLine"), ("NET-SNMP-EXTEND-MIB", "nsExtendOutput1Line"), ("NET-SNMP-EXTEND-MIB", "nsExtendOutputFull"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    nsExtendOutputGroup = nsExtendOutputGroup.setStatus('current')
if mibBuilder.loadTexts: nsExtendOutputGroup.setDescription('Objects relating to the output of extension commands.')
mibBuilder.exportSymbols("NET-SNMP-EXTEND-MIB", nsExtendRunType=nsExtendRunType, nsExtendObjects=nsExtendObjects, nsExtendConfigEntry=nsExtendConfigEntry, nsExtendResult=nsExtendResult, nsExtendOutputGroup=nsExtendOutputGroup, nsExtendCacheTime=nsExtendCacheTime, nsExtendOutput1Entry=nsExtendOutput1Entry, nsExtendConfigTable=nsExtendConfigTable, nsExtendOutput2Entry=nsExtendOutput2Entry, nsExtendToken=nsExtendToken, nsExtendConfigGroup=nsExtendConfigGroup, nsExtendLineIndex=nsExtendLineIndex, nsExtendOutLine=nsExtendOutLine, nsExtendCommand=nsExtendCommand, nsExtendStatus=nsExtendStatus, nsExtendOutput2Table=nsExtendOutput2Table, nsExtendStorage=nsExtendStorage, nsExtendInput=nsExtendInput, netSnmpExtendMIB=netSnmpExtendMIB, nsExtendGroups=nsExtendGroups, nsExtendArgs=nsExtendArgs, nsExtendNumEntries=nsExtendNumEntries, nsExtendOutputFull=nsExtendOutputFull, nsExtendExecType=nsExtendExecType, nsExtendOutput1Line=nsExtendOutput1Line, PYSNMP_MODULE_ID=netSnmpExtendMIB, nsExtendOutNumLines=nsExtendOutNumLines, nsExtendOutput1Table=nsExtendOutput1Table)
