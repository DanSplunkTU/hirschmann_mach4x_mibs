#
# PySNMP MIB module SL-DRY-CON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-EDFA-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:42:23 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
PerfIntervalCount, PerfTotalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfTotalCount", "PerfCurrentCount")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Integer32, Counter64, ModuleIdentity, IpAddress, NotificationType, MibIdentifier, Gauge32, Counter32, ObjectIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Integer32", "Counter64", "ModuleIdentity", "IpAddress", "NotificationType", "MibIdentifier", "Gauge32", "Counter32", "ObjectIdentity", "TimeTicks", "iso")
DisplayString, RowStatus, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention", "TruthValue")
slDryConMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 7))
if mibBuilder.loadTexts: slDryConMib.setLastUpdated('200108070000Z')
if mibBuilder.loadTexts: slDryConMib.setOrganization('PacketLight Networks Ltd.')
slDryConOut = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1))
slDryConIn = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2))
slDryConTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 7, 3))
slDryConAlarmCutoff = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("dummy", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConAlarmCutoff.setStatus('current')
slDryConOutTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2), )
if mibBuilder.loadTexts: slDryConOutTable.setStatus('current')
slDryConOutEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1), ).setIndexNames((0, "SL-DRY-CON-MIB", "slDryConOutIndex"))
if mibBuilder.loadTexts: slDryConOutEntry.setStatus('current')
slDryConOutIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slDryConOutIndex.setStatus('current')
slDryConOutCommand = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("activate", 1), ("deactivate", 2), ("clear", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConOutCommand.setStatus('current')
slDryConOutActiveStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slDryConOutActiveStatus.setStatus('current')
slDryConLastChange = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("dummy", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slDryConLastChange.setStatus('current')
slDryConInTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2), )
if mibBuilder.loadTexts: slDryConInTable.setStatus('current')
slDryConInEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1), ).setIndexNames((0, "SL-DRY-CON-MIB", "slDryConInIndex"))
if mibBuilder.loadTexts: slDryConInEntry.setStatus('current')
slDryConInIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slDryConInIndex.setStatus('current')
slDryConInDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 40))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConInDescription.setStatus('current')
slDryConInSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("critical", 1), ("major", 2), ("minor", 3), ("cleared", 4), ("notification", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConInSeverity.setStatus('current')
slDryConInEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConInEnable.setStatus('current')
slDryConInPolarity = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("activeClose", 1), ("activeOpen", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConInPolarity.setStatus('current')
slDryConInStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: slDryConInStatus.setStatus('current')
slDryConInAlmType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 7, 2, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38))).clone(namedValues=NamedValues(("aircompr", 1), ("aircond", 2), ("airdryd", 3), ("batdschrg", 4), ("battery", 5), ("clfan", 6), ("cpmajor", 7), ("cpminor", 8), ("engine", 9), ("engoprg", 10), ("explgs", 11), ("firdetr", 12), ("fire", 13), ("flood", 14), ("fuse", 15), ("gen", 16), ("hiair", 17), ("hihum", 18), ("hitemp", 19), ("hiwtr", 20), ("intruder", 21), ("lwbatvg", 22), ("lwfuel", 23), ("lwhum", 24), ("lwpres", 25), ("lwtemp", 26), ("lwwtr", 27), ("misc", 28), ("opendr", 29), ("pump", 30), ("power", 31), ("pwrX", 32), ("rect", 33), ("recthi", 34), ("rectlo", 35), ("smoke", 36), ("toxicgas", 37), ("ventn", 38)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slDryConInAlmType.setStatus('current')
slDryConStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 7, 3, 1)).setObjects(("SL-DRY-CON-MIB", "slDryConInIndex"), ("SL-DRY-CON-MIB", "slDryConInStatus"), ("SL-DRY-CON-MIB", "slDryConInAlmType"))
if mibBuilder.loadTexts: slDryConStatusChangeTrap.setStatus('current')
mibBuilder.exportSymbols("SL-DRY-CON-MIB", slDryConOut=slDryConOut, slDryConTraps=slDryConTraps, slDryConOutIndex=slDryConOutIndex, slDryConInEnable=slDryConInEnable, slDryConInDescription=slDryConInDescription, slDryConInEntry=slDryConInEntry, slDryConOutCommand=slDryConOutCommand, slDryConInTable=slDryConInTable, slDryConInPolarity=slDryConInPolarity, slDryConInAlmType=slDryConInAlmType, slDryConIn=slDryConIn, PYSNMP_MODULE_ID=slDryConMib, slDryConInSeverity=slDryConInSeverity, slDryConOutEntry=slDryConOutEntry, slDryConInIndex=slDryConInIndex, slDryConAlarmCutoff=slDryConAlarmCutoff, slDryConStatusChangeTrap=slDryConStatusChangeTrap, slDryConOutActiveStatus=slDryConOutActiveStatus, slDryConLastChange=slDryConLastChange, slDryConOutTable=slDryConOutTable, slDryConInStatus=slDryConInStatus, slDryConMib=slDryConMib)
