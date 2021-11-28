#
# PySNMP MIB module SL-RETIMER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-RETIMER-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:30:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slService, = mibBuilder.importSymbols("SL-NE-MIB", "slService")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Integer32, NotificationType, ObjectIdentity, Bits, Counter32, Gauge32, TimeTicks, Counter64, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, IpAddress, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "ObjectIdentity", "Bits", "Counter32", "Gauge32", "TimeTicks", "Counter64", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "IpAddress", "MibIdentifier")
TruthValue, TextualConvention, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "DateAndTime")
slRetimer = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14))
if mibBuilder.loadTexts: slRetimer.setLastUpdated('200508171200Z')
if mibBuilder.loadTexts: slRetimer.setOrganization('PacketLight Networks Ltd.')
slRetimerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1))
slRetimerStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 2))
slRetimerPm = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3))
slRetimerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 7))
slRetimerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1), )
if mibBuilder.loadTexts: slRetimerConfigTable.setStatus('current')
slRetimerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1, 1), ).setIndexNames((0, "SL-RETIMER-MIB", "slRetimerLineIndex"))
if mibBuilder.loadTexts: slRetimerConfigEntry.setStatus('current')
slRetimerLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRetimerLineIndex.setStatus('current')
slRetimerResetPmCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRetimerResetPmCounters.setStatus('current')
slRetimerCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1), )
if mibBuilder.loadTexts: slRetimerCurrentTable.setStatus('current')
slRetimerCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1), ).setIndexNames((0, "SL-RETIMER-MIB", "slRetimerCurrentIndex"))
if mibBuilder.loadTexts: slRetimerCurrentEntry.setStatus('current')
slRetimerCurrentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRetimerCurrentIndex.setStatus('current')
slRetimerCurrentRxRllES = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRetimerCurrentRxRllES.setStatus('current')
slRetimerCurrentRxK285ES = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRetimerCurrentRxK285ES.setStatus('current')
slRetimerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 7, 1)).setObjects(("SL-RETIMER-MIB", "slRetimerLineIndex"))
if mibBuilder.loadTexts: slRetimerStatusChange.setStatus('current')
mibBuilder.exportSymbols("SL-RETIMER-MIB", PYSNMP_MODULE_ID=slRetimer, slRetimerConfigTable=slRetimerConfigTable, slRetimerStatusChange=slRetimerStatusChange, slRetimerConfig=slRetimerConfig, slRetimerCurrentIndex=slRetimerCurrentIndex, slRetimerCurrentRxK285ES=slRetimerCurrentRxK285ES, slRetimerConfigEntry=slRetimerConfigEntry, slRetimerPm=slRetimerPm, slRetimerResetPmCounters=slRetimerResetPmCounters, slRetimerLineIndex=slRetimerLineIndex, slRetimerStat=slRetimerStat, slRetimerCurrentRxRllES=slRetimerCurrentRxRllES, slRetimer=slRetimer, slRetimerTraps=slRetimerTraps, slRetimerCurrentEntry=slRetimerCurrentEntry, slRetimerCurrentTable=slRetimerCurrentTable)
