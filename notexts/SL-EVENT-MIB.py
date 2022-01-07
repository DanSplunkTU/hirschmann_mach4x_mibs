#
# PySNMP MIB module SL-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-EVENT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:33:49 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, Counter32, Bits, TimeTicks, ModuleIdentity, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, Counter64, IpAddress, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Bits", "TimeTicks", "ModuleIdentity", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "Counter64", "IpAddress", "Integer32", "iso")
TruthValue, TimeStamp, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TimeStamp", "TextualConvention", "DisplayString")
slEventMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22))
if mibBuilder.loadTexts: slEventMib.setLastUpdated('200708280000Z')
if mibBuilder.loadTexts: slEventMib.setOrganization('PacketLight Networks Ltd.')
class SlGenEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("swUpgradeEvent", 1), ("remoteUnitFailEvent", 2), ("alsOperStatus", 3))

class SlEventType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24))
    namedValues = NamedValues(("edDate", 1), ("rstProv", 2), ("edIp", 3), ("initPm", 4), ("dltIpRoute", 5), ("edSys", 6), ("setSid", 7), ("addUser", 8), ("dltUser", 9), ("rmvFac", 10), ("rstFac", 11), ("edFac", 12), ("oprLoopback", 13), ("rlsLoopback", 14), ("entAps", 15), ("dltAps", 16), ("oprProtSw", 17), ("rlsProtSw", 18), ("oprAco", 19), ("rstProvCommit", 20), ("savProvStart", 21), ("savProvComplete", 22), ("savProvFailed", 23), ("swLoadUpgrade", 24))

class SlEventInventoryAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("inserted", 1), ("removed", 2))

class SlEventInventoryType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("psu", 1), ("optics", 2), ("fan", 3))

slEventConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1))
slEventTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2))
slEventTraps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0))
slEventConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1), )
if mibBuilder.loadTexts: slEventConfigTable.setStatus('current')
slEventConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1), ).setIndexNames((0, "SL-EVENT-MIB", "slEventIfIndex"), (0, "SL-EVENT-MIB", "slEventType"))
if mibBuilder.loadTexts: slEventConfigEntry.setStatus('current')
slEventIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEventIfIndex.setStatus('current')
slEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 2), SlEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEventType.setStatus('current')
slEventVal = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventVal.setStatus('current')
slEventUser = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventUser.setStatus('current')
slEventCtag = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventCtag.setStatus('current')
slEventTid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventTid.setStatus('current')
slEventInventoryTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2), )
if mibBuilder.loadTexts: slEventInventoryTable.setStatus('current')
slEventInventoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1), ).setIndexNames((0, "SL-EVENT-MIB", "slEventInventoryIfIndex"), (0, "SL-EVENT-MIB", "slEventInventoryType"))
if mibBuilder.loadTexts: slEventInventoryEntry.setStatus('current')
slEventInventoryIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEventInventoryIfIndex.setStatus('current')
slEventInventoryAction = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 2), SlEventInventoryAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEventInventoryAction.setStatus('current')
slEventInventoryType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 3), SlEventInventoryType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slEventInventoryType.setStatus('current')
slEventInventorySerial = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventInventorySerial.setStatus('current')
slEventInventoryPartnum = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 2, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slEventInventoryPartnum.setStatus('current')
slGenEventConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3), )
if mibBuilder.loadTexts: slGenEventConfigTable.setStatus('current')
slGenEventConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1), ).setIndexNames((0, "SL-EVENT-MIB", "slGenEventIfIndex"), (0, "SL-EVENT-MIB", "slGenEventType"))
if mibBuilder.loadTexts: slGenEventConfigEntry.setStatus('current')
slGenEventIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slGenEventIfIndex.setStatus('current')
slGenEventType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 2), SlGenEventType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slGenEventType.setStatus('current')
slGenEventVal = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slGenEventVal.setStatus('current')
slGenEventUser = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slGenEventUser.setStatus('current')
slGenEventCtag = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slGenEventCtag.setStatus('current')
slGenEventTid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 1, 3, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slGenEventTid.setStatus('current')
slEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 2)).setObjects(("SL-EVENT-MIB", "slEventIfIndex"), ("SL-EVENT-MIB", "slEventType"), ("SL-EVENT-MIB", "slEventVal"), ("SL-EVENT-MIB", "slEventUser"))
if mibBuilder.loadTexts: slEventTrap.setStatus('current')
slEventTrap0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0, 2)).setObjects(("SL-EVENT-MIB", "slEventIfIndex"), ("SL-EVENT-MIB", "slEventType"), ("SL-EVENT-MIB", "slEventVal"), ("SL-EVENT-MIB", "slEventUser"))
if mibBuilder.loadTexts: slEventTrap0.setStatus('current')
slEventInventoryTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 3)).setObjects(("SL-EVENT-MIB", "slEventInventoryIfIndex"), ("SL-EVENT-MIB", "slEventInventoryAction"), ("SL-EVENT-MIB", "slEventInventoryType"), ("SL-EVENT-MIB", "slEventInventorySerial"), ("SL-EVENT-MIB", "slEventInventoryPartnum"))
if mibBuilder.loadTexts: slEventInventoryTrap.setStatus('current')
slEventInventoryTrap0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0, 3)).setObjects(("SL-EVENT-MIB", "slEventInventoryIfIndex"), ("SL-EVENT-MIB", "slEventInventoryAction"), ("SL-EVENT-MIB", "slEventInventoryType"), ("SL-EVENT-MIB", "slEventInventorySerial"), ("SL-EVENT-MIB", "slEventInventoryPartnum"))
if mibBuilder.loadTexts: slEventInventoryTrap0.setStatus('current')
slGenEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 4)).setObjects(("SL-EVENT-MIB", "slGenEventIfIndex"), ("SL-EVENT-MIB", "slGenEventType"), ("SL-EVENT-MIB", "slGenEventVal"), ("SL-EVENT-MIB", "slGenEventUser"))
if mibBuilder.loadTexts: slGenEventTrap.setStatus('current')
slGenEventTrap0 = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 22, 2, 0, 4)).setObjects(("SL-EVENT-MIB", "slGenEventIfIndex"), ("SL-EVENT-MIB", "slGenEventType"), ("SL-EVENT-MIB", "slGenEventVal"), ("SL-EVENT-MIB", "slGenEventUser"))
if mibBuilder.loadTexts: slGenEventTrap0.setStatus('current')
mibBuilder.exportSymbols("SL-EVENT-MIB", slEventInventoryPartnum=slEventInventoryPartnum, slGenEventType=slGenEventType, slGenEventTrap0=slGenEventTrap0, slEventInventoryTrap0=slEventInventoryTrap0, slEventConfig=slEventConfig, slEventInventorySerial=slEventInventorySerial, slEventTraps=slEventTraps, SlGenEventType=SlGenEventType, PYSNMP_MODULE_ID=slEventMib, slEventConfigTable=slEventConfigTable, slEventTraps0=slEventTraps0, slEventCtag=slEventCtag, slGenEventConfigTable=slGenEventConfigTable, slEventInventoryType=slEventInventoryType, slEventInventoryEntry=slEventInventoryEntry, slEventVal=slEventVal, slEventConfigEntry=slEventConfigEntry, slEventIfIndex=slEventIfIndex, slEventTid=slEventTid, SlEventType=SlEventType, slEventMib=slEventMib, slEventTrap=slEventTrap, slEventTrap0=slEventTrap0, slGenEventVal=slGenEventVal, slGenEventTrap=slGenEventTrap, slEventInventoryAction=slEventInventoryAction, slGenEventUser=slGenEventUser, slEventInventoryTrap=slEventInventoryTrap, slGenEventTid=slGenEventTid, slEventInventoryTable=slEventInventoryTable, slGenEventCtag=slGenEventCtag, slEventUser=slEventUser, slGenEventConfigEntry=slGenEventConfigEntry, slEventInventoryIfIndex=slEventInventoryIfIndex, SlEventInventoryAction=SlEventInventoryAction, slGenEventIfIndex=slGenEventIfIndex, slEventType=slEventType, SlEventInventoryType=SlEventInventoryType)
