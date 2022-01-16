#
# PySNMP MIB module CTFRAMER-CONFIG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTFRAMER-CONFIG-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:36 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ctFramerConfig, ctIfPortPortNumber = mibBuilder.importSymbols("CTIF-EXT-MIB", "ctFramerConfig", "ctIfPortPortNumber")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, iso, Counter64, Unsigned32, MibIdentifier, Integer32, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "iso", "Counter64", "Unsigned32", "MibIdentifier", "Integer32", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ctFramerBaseConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1))
ctFramerSonetConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 2))
ctFramerDS3Config = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 3))
ctFramerConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1), )
if mibBuilder.loadTexts: ctFramerConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: ctFramerConfigTable.setDescription('A list of framer configuration objects for a physical port on\n          a particular interface.')
ctFramerConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "CTIF-EXT-MIB", "ctIfPortPortNumber"))
if mibBuilder.loadTexts: ctFramerConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: ctFramerConfigEntry.setDescription('An entry containing objects pertaining to the configuration\n          of the framer on a physical port on an interface.')
ctFramerStatsConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFramerStatsConfig.setStatus('mandatory')
if mibBuilder.loadTexts: ctFramerStatsConfig.setDescription("Setting this object to 'on' will activate the framer MIBs as\n          specified by either RFC-1595 or RFC-1407 depending on whether\n          the interface uses SONET/SDH framing or DS3 framing respectively.\n          Note: Setting this to 'on' will permit gathering of framer\n          statistics at the expense of processing time. However, it might\n          be a valuable debugging aid to turn on the framer MIB.\n \n          Setting this object to 'off' will deactivate the respective\n          framer MIBs, thus saving processing time.\n \n          It is emphasized that collection of statistics for the framer\n          is resource (processor, memory) intensive.\n \n          This object is persistent.")
ctFramerAlarmsConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2))).clone('off')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFramerAlarmsConfig.setStatus('mandatory')
if mibBuilder.loadTexts: ctFramerAlarmsConfig.setDescription('This object activates/deactivates the detection and initiation\n          of framer alarms.\n\n          for SONET/SDH framed physical ports: \n              RDI - remote defect indicator \n              AIS - alarm indication signal\n\n          for DS3 framed physical ports: \n              yellow signal alarms\n \n          This object is persistent.')
ctFramerMediumConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("sonet", 1), ("sdh", 2))).clone('sonet')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFramerMediumConfig.setStatus('mandatory')
if mibBuilder.loadTexts: ctFramerMediumConfig.setDescription('This object controls whether a SONET or a SDH signal is used\n          across this physical port.\n \n          sonet - synchronous optical network\n          sdh - synchronous digital heirarchy\n\n          This object is persistent.')
ctFramerIdleCellsConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("idle", 1), ("unassigned", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFramerIdleCellsConfig.setStatus('mandatory')
if mibBuilder.loadTexts: ctFramerIdleCellsConfig.setDescription('When this object is set to idle, null cells\n          will have the CLP bit set.\n\n          When this object is set to unassigned, null\n          cells will not have the CLP bit set.\n\n          This object is persistent.')
ctFramerCellPayScramConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 3, 3, 9, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctFramerCellPayScramConfig.setStatus('mandatory')
if mibBuilder.loadTexts: ctFramerCellPayScramConfig.setDescription('This object activates/deactivates cell payload\n          transmit scrambling and receive descrambling.\n\n          This object is persistent.')
mibBuilder.exportSymbols("CTFRAMER-CONFIG-MIB", ctFramerStatsConfig=ctFramerStatsConfig, ctFramerIdleCellsConfig=ctFramerIdleCellsConfig, ctFramerSonetConfig=ctFramerSonetConfig, ctFramerCellPayScramConfig=ctFramerCellPayScramConfig, ctFramerMediumConfig=ctFramerMediumConfig, ctFramerBaseConfig=ctFramerBaseConfig, ctFramerConfigEntry=ctFramerConfigEntry, ctFramerAlarmsConfig=ctFramerAlarmsConfig, ctFramerConfigTable=ctFramerConfigTable, ctFramerDS3Config=ctFramerDS3Config)
