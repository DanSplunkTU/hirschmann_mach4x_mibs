#
# PySNMP MIB module VEL-HOST2-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vigintos/VEL-HOST2-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:27:52 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Gauge32, ObjectIdentity, Integer32, iso, ModuleIdentity, Unsigned32, Bits, TimeTicks, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "ObjectIdentity", "Integer32", "iso", "ModuleIdentity", "Unsigned32", "Bits", "TimeTicks", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Counter64")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vel, = mibBuilder.importSymbols("VEL-MIB", "vel")
host2 = ModuleIdentity((1, 3, 6, 1, 4, 1, 27993, 5))
host2.setRevisions(('2013-03-07 08:00',))
if mibBuilder.loadTexts: host2.setLastUpdated('201508121000Z')
if mibBuilder.loadTexts: host2.setOrganization('Vigintos Elektronika')
host2Name = MibScalar((1, 3, 6, 1, 4, 1, 27993, 5, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2Name.setStatus('current')
host2Version = MibScalar((1, 3, 6, 1, 4, 1, 27993, 5, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2Version.setStatus('current')
host2LoaderVersion = MibScalar((1, 3, 6, 1, 4, 1, 27993, 5, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2LoaderVersion.setStatus('current')
host2CmdTable = MibTable((1, 3, 6, 1, 4, 1, 27993, 5, 4), )
if mibBuilder.loadTexts: host2CmdTable.setStatus('current')
host2CmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27993, 5, 4, 1), ).setIndexNames((0, "VEL-HOST2-MIB", "host2CmdIndex"))
if mibBuilder.loadTexts: host2CmdEntry.setStatus('current')
host2CmdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2CmdIndex.setStatus('current')
host2CmdName = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2CmdName.setStatus('current')
host2CmdExecute = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: host2CmdExecute.setStatus('current')
host2HistoryTable = MibTable((1, 3, 6, 1, 4, 1, 27993, 5, 5), )
if mibBuilder.loadTexts: host2HistoryTable.setStatus('current')
host2HistoryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27993, 5, 5, 1), ).setIndexNames((0, "VEL-HOST2-MIB", "host2HisIndex"))
if mibBuilder.loadTexts: host2HistoryEntry.setStatus('current')
host2HisIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1008))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2HisIndex.setStatus('current')
host2HisRecord = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 5, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2HisRecord.setStatus('current')
host2DevAttrTable = MibTable((1, 3, 6, 1, 4, 1, 27993, 5, 6), )
if mibBuilder.loadTexts: host2DevAttrTable.setStatus('current')
host2DevAttrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27993, 5, 6, 1), ).setIndexNames((0, "VEL-HOST2-MIB", "host2DevIndex"))
if mibBuilder.loadTexts: host2DevAttrEntry.setStatus('current')
host2DevIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevIndex.setStatus('current')
host2DevLocalAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 6, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(2, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevLocalAddr.setStatus('current')
host2DevTypeNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 6, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevTypeNumber.setStatus('current')
host2DevLanState = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disconnected", 0), ("connected", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevLanState.setStatus('current')
host2DevTxtTable = MibTable((1, 3, 6, 1, 4, 1, 27993, 5, 7), )
if mibBuilder.loadTexts: host2DevTxtTable.setStatus('current')
host2DevTxtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27993, 5, 7, 1), ).setIndexNames((0, "VEL-HOST2-MIB", "host2DevIndex"), (0, "VEL-HOST2-MIB", "host2DevTxtIndex"))
if mibBuilder.loadTexts: host2DevTxtEntry.setStatus('current')
host2DevTxtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevTxtIndex.setStatus('current')
host2DevTxtName = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 7, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevTxtName.setStatus('current')
host2DevTxtValue = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 7, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevTxtValue.setStatus('current')
host2DevEvtTable = MibTable((1, 3, 6, 1, 4, 1, 27993, 5, 8), )
if mibBuilder.loadTexts: host2DevEvtTable.setStatus('current')
host2DevEvtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27993, 5, 8, 1), ).setIndexNames((0, "VEL-HOST2-MIB", "host2DevIndex"), (0, "VEL-HOST2-MIB", "host2DevEvtIndex"))
if mibBuilder.loadTexts: host2DevEvtEntry.setStatus('current')
host2DevEvtIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevEvtIndex.setStatus('current')
host2DevEvtName = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 8, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevEvtName.setStatus('current')
host2DevEvtType = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notice", 0), ("warning", 1), ("alarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevEvtType.setStatus('current')
host2DevEvtState = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevEvtState.setStatus('current')
host2DevParTable = MibTable((1, 3, 6, 1, 4, 1, 27993, 5, 9), )
if mibBuilder.loadTexts: host2DevParTable.setStatus('current')
host2DevParEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27993, 5, 9, 1), ).setIndexNames((0, "VEL-HOST2-MIB", "host2DevIndex"), (0, "VEL-HOST2-MIB", "host2DevParIndex"))
if mibBuilder.loadTexts: host2DevParEntry.setStatus('current')
host2DevParIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevParIndex.setStatus('current')
host2DevParName = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevParName.setStatus('current')
host2DevParValue = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevParValue.setStatus('current')
host2DevParUnit = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 3))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevParUnit.setStatus('current')
host2DevParStateType = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("notice", 0), ("warning", 1), ("alarm", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevParStateType.setStatus('current')
host2DevParState = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 9, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("noAlarm", 0), ("lessThanMin", 1), ("greatherThanMax", 2), ("blocked", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevParState.setStatus('current')
host2DevQntTable = MibTable((1, 3, 6, 1, 4, 1, 27993, 5, 10), )
if mibBuilder.loadTexts: host2DevQntTable.setStatus('current')
host2DevQntEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27993, 5, 10, 1), ).setIndexNames((0, "VEL-HOST2-MIB", "host2DevIndex"), (0, "VEL-HOST2-MIB", "host2DevQntIndex"))
if mibBuilder.loadTexts: host2DevQntEntry.setStatus('current')
host2DevQntIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevQntIndex.setStatus('current')
host2DevQntName = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevQntName.setStatus('current')
host2DevQntValue = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: host2DevQntValue.setStatus('current')
host2DevQntMin = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevQntMin.setStatus('current')
host2DevQntMax = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 12))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevQntMax.setStatus('current')
host2DevQntAccess = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 10, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("read-only", 0), ("read-write", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevQntAccess.setStatus('current')
host2DevCmdTable = MibTable((1, 3, 6, 1, 4, 1, 27993, 5, 11), )
if mibBuilder.loadTexts: host2DevCmdTable.setStatus('current')
host2DevCmdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 27993, 5, 11, 1), ).setIndexNames((0, "VEL-HOST2-MIB", "host2DevIndex"), (0, "VEL-HOST2-MIB", "host2DevCmdIndex"))
if mibBuilder.loadTexts: host2DevCmdEntry.setStatus('current')
host2DevCmdIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 11, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevCmdIndex.setStatus('current')
host2DevCmdName = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 11, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: host2DevCmdName.setStatus('current')
host2DevCmdExecute = MibTableColumn((1, 3, 6, 1, 4, 1, 27993, 5, 11, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("no", 0), ("yes", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: host2DevCmdExecute.setStatus('current')
host2DevConnectionTrap = NotificationType((1, 3, 6, 1, 4, 1, 27993, 5) + (0,5001)).setObjects(("VEL-HOST2-MIB", "host2DevLanState"))
host2DevEvtStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 27993, 5) + (0,5002)).setObjects(("VEL-HOST2-MIB", "host2DevEvtState"))
host2DevParStateTrap = NotificationType((1, 3, 6, 1, 4, 1, 27993, 5) + (0,5003)).setObjects(("VEL-HOST2-MIB", "host2DevParState"))
mibBuilder.exportSymbols("VEL-HOST2-MIB", host2DevIndex=host2DevIndex, host2DevEvtType=host2DevEvtType, host2DevParValue=host2DevParValue, host2DevLocalAddr=host2DevLocalAddr, host2CmdExecute=host2CmdExecute, host2CmdTable=host2CmdTable, host2DevQntTable=host2DevQntTable, host2HisRecord=host2HisRecord, host2DevTxtTable=host2DevTxtTable, host2Version=host2Version, host2DevEvtEntry=host2DevEvtEntry, host2HistoryTable=host2HistoryTable, host2DevAttrEntry=host2DevAttrEntry, host2DevTxtValue=host2DevTxtValue, host2DevParEntry=host2DevParEntry, host2=host2, host2DevEvtName=host2DevEvtName, host2DevParState=host2DevParState, host2LoaderVersion=host2LoaderVersion, host2CmdEntry=host2CmdEntry, host2DevCmdIndex=host2DevCmdIndex, host2Name=host2Name, host2DevEvtState=host2DevEvtState, host2DevQntMax=host2DevQntMax, host2DevEvtIndex=host2DevEvtIndex, host2DevAttrTable=host2DevAttrTable, PYSNMP_MODULE_ID=host2, host2HisIndex=host2HisIndex, host2DevTxtEntry=host2DevTxtEntry, host2DevTxtIndex=host2DevTxtIndex, host2DevCmdExecute=host2DevCmdExecute, host2DevEvtStateTrap=host2DevEvtStateTrap, host2DevQntMin=host2DevQntMin, host2DevParStateType=host2DevParStateType, host2HistoryEntry=host2HistoryEntry, host2DevParTable=host2DevParTable, host2DevParName=host2DevParName, host2DevQntEntry=host2DevQntEntry, host2DevQntIndex=host2DevQntIndex, host2DevLanState=host2DevLanState, host2DevCmdTable=host2DevCmdTable, host2DevTxtName=host2DevTxtName, host2CmdIndex=host2CmdIndex, host2DevCmdName=host2DevCmdName, host2DevQntAccess=host2DevQntAccess, host2DevParUnit=host2DevParUnit, host2DevConnectionTrap=host2DevConnectionTrap, host2DevTypeNumber=host2DevTypeNumber, host2DevParIndex=host2DevParIndex, host2DevQntName=host2DevQntName, host2DevEvtTable=host2DevEvtTable, host2CmdName=host2CmdName, host2DevQntValue=host2DevQntValue, host2DevParStateTrap=host2DevParStateTrap, host2DevCmdEntry=host2DevCmdEntry)
