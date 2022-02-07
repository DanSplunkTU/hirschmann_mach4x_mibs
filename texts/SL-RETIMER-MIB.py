#
# PySNMP MIB module SL-RETIMER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-RETIMER-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:17:48 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slService, = mibBuilder.importSymbols("SL-NE-MIB", "slService")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, MibIdentifier, TimeTicks, ObjectIdentity, Unsigned32, IpAddress, Counter32, Gauge32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "Gauge32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType")
DateAndTime, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TruthValue", "TextualConvention")
slRetimer = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14))
if mibBuilder.loadTexts: slRetimer.setLastUpdated('200508171200Z')
if mibBuilder.loadTexts: slRetimer.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slRetimer.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slRetimer.setDescription('This MIB module describes the Retimer')
slRetimerConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1))
slRetimerStat = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 2))
slRetimerPm = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3))
slRetimerTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 7))
slRetimerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1), )
if mibBuilder.loadTexts: slRetimerConfigTable.setStatus('current')
if mibBuilder.loadTexts: slRetimerConfigTable.setDescription('The Retimer Configuration table.')
slRetimerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1, 1), ).setIndexNames((0, "SL-RETIMER-MIB", "slRetimerLineIndex"))
if mibBuilder.loadTexts: slRetimerConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slRetimerConfigEntry.setDescription('An entry in the Retimer Configuration table.')
slRetimerLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRetimerLineIndex.setStatus('current')
if mibBuilder.loadTexts: slRetimerLineIndex.setDescription('This object should be made equal to the ifIndex of the SFP.')
slRetimerResetPmCounters = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 1, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slRetimerResetPmCounters.setStatus('current')
if mibBuilder.loadTexts: slRetimerResetPmCounters.setDescription('Setting this object to 1 reset the current interval PM\n    \tcounters of the retimer.')
slRetimerCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1), )
if mibBuilder.loadTexts: slRetimerCurrentTable.setStatus('current')
if mibBuilder.loadTexts: slRetimerCurrentTable.setDescription('The Ethernet current table contains various statistics\n\t\tbeing collected for the current 15 minute\n\t\tinterval.')
slRetimerCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1), ).setIndexNames((0, "SL-RETIMER-MIB", "slRetimerCurrentIndex"))
if mibBuilder.loadTexts: slRetimerCurrentEntry.setStatus('current')
if mibBuilder.loadTexts: slRetimerCurrentEntry.setDescription('An entry in the Retimer Current table.')
slRetimerCurrentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRetimerCurrentIndex.setStatus('current')
if mibBuilder.loadTexts: slRetimerCurrentIndex.setDescription('The index value which uniquely identifies  the\n\t\tEthernet interface to which this entry is applicable.\n\t\tThe interface identified by a particular value of\n\t\tthis index is the same interface as identified by\n\t\tthe same value as a the ifIndex of the SFP.')
slRetimerCurrentRxRllES = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRetimerCurrentRxRllES.setStatus('current')
if mibBuilder.loadTexts: slRetimerCurrentRxRllES.setDescription('The total number of Errored Seconds with RLL error.')
slRetimerCurrentRxK285ES = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 3, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slRetimerCurrentRxK285ES.setStatus('current')
if mibBuilder.loadTexts: slRetimerCurrentRxK285ES.setDescription('The total number of Errored Seconds with K28.5 error.')
slRetimerStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 1, 14, 7, 1)).setObjects(("SL-RETIMER-MIB", "slRetimerLineIndex"))
if mibBuilder.loadTexts: slRetimerStatusChange.setStatus('current')
if mibBuilder.loadTexts: slRetimerStatusChange.setDescription('')
mibBuilder.exportSymbols("SL-RETIMER-MIB", slRetimerResetPmCounters=slRetimerResetPmCounters, slRetimerPm=slRetimerPm, PYSNMP_MODULE_ID=slRetimer, slRetimerCurrentEntry=slRetimerCurrentEntry, slRetimerConfigTable=slRetimerConfigTable, slRetimerCurrentRxRllES=slRetimerCurrentRxRllES, slRetimerCurrentIndex=slRetimerCurrentIndex, slRetimerCurrentRxK285ES=slRetimerCurrentRxK285ES, slRetimer=slRetimer, slRetimerTraps=slRetimerTraps, slRetimerConfigEntry=slRetimerConfigEntry, slRetimerLineIndex=slRetimerLineIndex, slRetimerCurrentTable=slRetimerCurrentTable, slRetimerConfig=slRetimerConfig, slRetimerStatusChange=slRetimerStatusChange, slRetimerStat=slRetimerStat)
