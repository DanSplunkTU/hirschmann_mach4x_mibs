#
# PySNMP MIB module SL-RETIMER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-RETIMER-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:15:38 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slService, = mibBuilder.importSymbols("SL-NE-MIB", "slService")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Unsigned32, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, Gauge32, Counter64, NotificationType, Counter32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Unsigned32", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "Gauge32", "Counter64", "NotificationType", "Counter32", "Bits", "ModuleIdentity")
DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
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
mibBuilder.exportSymbols("SL-RETIMER-MIB", slRetimerConfigEntry=slRetimerConfigEntry, slRetimerResetPmCounters=slRetimerResetPmCounters, slRetimerCurrentRxRllES=slRetimerCurrentRxRllES, slRetimer=slRetimer, slRetimerConfigTable=slRetimerConfigTable, slRetimerCurrentEntry=slRetimerCurrentEntry, slRetimerPm=slRetimerPm, slRetimerConfig=slRetimerConfig, slRetimerCurrentRxK285ES=slRetimerCurrentRxK285ES, slRetimerTraps=slRetimerTraps, slRetimerCurrentIndex=slRetimerCurrentIndex, slRetimerCurrentTable=slRetimerCurrentTable, slRetimerStatusChange=slRetimerStatusChange, slRetimerLineIndex=slRetimerLineIndex, PYSNMP_MODULE_ID=slRetimer, slRetimerStat=slRetimerStat)
