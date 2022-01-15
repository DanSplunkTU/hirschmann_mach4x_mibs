#
# PySNMP MIB module AVIAT-MODEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-MODEM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:52:29 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
AviatModulationType, = mibBuilder.importSymbols("AVIAT-TEXTCONVENTION-MIB", "AviatModulationType")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, IpAddress, Bits, Integer32, iso, Counter64, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "IpAddress", "Bits", "Integer32", "iso", "Counter64", "Gauge32", "MibIdentifier")
TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention")
aviatModules, = mibBuilder.importSymbols("STXN-GLOBALREGISTER-MIB", "aviatModules")
aviatModemModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 3))
aviatModemModule.setRevisions(('2018-09-20 11:30', '2017-03-28 01:19', '2015-04-28 15:30', '2014-09-19 15:05', '2014-02-03 22:20', '2014-01-21 01:57',))
if mibBuilder.loadTexts: aviatModemModule.setLastUpdated('201703280119Z')
if mibBuilder.loadTexts: aviatModemModule.setOrganization('Aviat Networks')
aviatModemConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 3, 1))
aviatModemGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1))
aviatModemCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 2))
aviatModemMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2))
class AviatModemCapacityType(TextualConvention, Gauge32):
    status = 'current'
    displayHint = 'd'

aviatModemTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1), )
if mibBuilder.loadTexts: aviatModemTable.setStatus('current')
aviatModemEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatModemEntry.setStatus('current')
aviatModemBandwidth = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 1), Gauge32()).setUnits('kHz').setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemBandwidth.setStatus('current')
aviatModemModulationType = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("fixed", 0), ("acm256", 1), ("acm1024", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemModulationType.setStatus('current')
aviatModemModulationBase = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 3), AviatModulationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemModulationBase.setStatus('current')
aviatModemModulationMax = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 4), AviatModulationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemModulationMax.setStatus('current')
aviatModemLicensedModulationMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 5), AviatModulationType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemLicensedModulationMask.setStatus('current')
aviatModemRegulatoryStandard = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("ansi", 2), ("etsi", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemRegulatoryStandard.setStatus('current')
aviatModemProfileVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 7), Integer32().clone(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemProfileVersion.setStatus('current')
aviatModemCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemCapacity.setStatus('current')
aviatModemL1laLiteEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemL1laLiteEnabled.setStatus('current')
aviatModemMLHCEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemMLHCEnabled.setStatus('current')
aviatModemCurCapacityTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 11), AviatModemCapacityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemCurCapacityTx.setStatus('current')
aviatModemCurCapacityRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 12), AviatModemCapacityType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemCurCapacityRx.setStatus('current')
aviatModemCurModulationTx = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 13), AviatModulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemCurModulationTx.setStatus('current')
aviatModemCurModulationRx = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 1, 1, 14), AviatModulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemCurModulationRx.setStatus('current')
aviatModemModulationTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 2), )
if mibBuilder.loadTexts: aviatModemModulationTable.setStatus('current')
aviatModemModulationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "AVIAT-MODEM-MIB", "aviatModemModulationIndex"))
if mibBuilder.loadTexts: aviatModemModulationEntry.setStatus('current')
aviatModemModulationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 2, 1, 1), Gauge32())
if mibBuilder.loadTexts: aviatModemModulationIndex.setStatus('current')
aviatModemModulation = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 2, 1, 2), AviatModulationType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemModulation.setStatus('current')
aviatModemXpicTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 3), )
if mibBuilder.loadTexts: aviatModemXpicTable.setStatus('current')
aviatModemXpicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatModemXpicEntry.setStatus('current')
aviatModemXpicEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 3, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatModemXpicEnable.setStatus('current')
aviatModemStatusTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 4), )
if mibBuilder.loadTexts: aviatModemStatusTable.setStatus('current')
aviatModemStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 4, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: aviatModemStatusEntry.setStatus('current')
aviatModemStatusMaxCapacity = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 4, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemStatusMaxCapacity.setStatus('current')
aviatModemStatusOper = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemStatusOper.setStatus('current')
aviatModemModulationStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5), )
if mibBuilder.loadTexts: aviatModemModulationStatsTable.setStatus('current')
aviatModemModulationStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "AVIAT-MODEM-MIB", "aviatModemModStatsModulation"))
if mibBuilder.loadTexts: aviatModemModulationStatsEntry.setStatus('current')
aviatModemModStatsModulation = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1, 1), AviatModulationType())
if mibBuilder.loadTexts: aviatModemModStatsModulation.setStatus('current')
aviatModemModStatsTxSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemModStatsTxSecs.setStatus('current')
aviatModemModStatsTxPct = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemModStatsTxPct.setStatus('current')
aviatModemModStatsRxSecs = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemModStatsRxSecs.setStatus('current')
aviatModemModStatsRxPct = MibTableColumn((1, 3, 6, 1, 4, 1, 2509, 9, 3, 2, 5, 1, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatModemModStatsRxPct.setStatus('current')
aviatModemObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1, 1)).setObjects(("AVIAT-MODEM-MIB", "aviatModemBandwidth"), ("AVIAT-MODEM-MIB", "aviatModemModulationType"), ("AVIAT-MODEM-MIB", "aviatModemModulationBase"), ("AVIAT-MODEM-MIB", "aviatModemModulationMax"), ("AVIAT-MODEM-MIB", "aviatModemLicensedModulationMask"), ("AVIAT-MODEM-MIB", "aviatModemRegulatoryStandard"), ("AVIAT-MODEM-MIB", "aviatModemProfileVersion"), ("AVIAT-MODEM-MIB", "aviatModemCapacity"), ("AVIAT-MODEM-MIB", "aviatModemL1laLiteEnabled"), ("AVIAT-MODEM-MIB", "aviatModemModulation"), ("AVIAT-MODEM-MIB", "aviatModemStatusMaxCapacity"), ("AVIAT-MODEM-MIB", "aviatModemMLHCEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatModemObjectGroup = aviatModemObjectGroup.setStatus('current')
aviatModemXpicGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1, 2)).setObjects(("AVIAT-MODEM-MIB", "aviatModemXpicEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatModemXpicGroup = aviatModemXpicGroup.setStatus('current')
aviatModemModulationStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1, 3)).setObjects(("AVIAT-MODEM-MIB", "aviatModemModStatsTxSecs"), ("AVIAT-MODEM-MIB", "aviatModemModStatsTxPct"), ("AVIAT-MODEM-MIB", "aviatModemModStatsRxSecs"), ("AVIAT-MODEM-MIB", "aviatModemModStatsRxPct"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatModemModulationStatsGroup = aviatModemModulationStatsGroup.setStatus('current')
aviatModemModulationCurrentGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1, 4)).setObjects(("AVIAT-MODEM-MIB", "aviatModemCurCapacityTx"), ("AVIAT-MODEM-MIB", "aviatModemCurCapacityRx"), ("AVIAT-MODEM-MIB", "aviatModemCurModulationTx"), ("AVIAT-MODEM-MIB", "aviatModemCurModulationRx"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatModemModulationCurrentGroup = aviatModemModulationCurrentGroup.setStatus('current')
aviatModemStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 1, 5)).setObjects(("AVIAT-MODEM-MIB", "aviatModemStatusOper"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatModemStatusGroup = aviatModemStatusGroup.setStatus('current')
aviatModemComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2509, 9, 3, 1, 2, 1)).setObjects(("AVIAT-MODEM-MIB", "aviatModemObjectGroup"), ("AVIAT-MODEM-MIB", "aviatModemXpicGroup"), ("AVIAT-MODEM-MIB", "aviatModemModulationStatsGroup"), ("AVIAT-MODEM-MIB", "aviatModemModulationCurrentGroup"), ("AVIAT-MODEM-MIB", "aviatModemStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatModemComplV1 = aviatModemComplV1.setStatus('current')
mibBuilder.exportSymbols("AVIAT-MODEM-MIB", aviatModemCurCapacityRx=aviatModemCurCapacityRx, aviatModemCurModulationRx=aviatModemCurModulationRx, aviatModemComplV1=aviatModemComplV1, aviatModemConformance=aviatModemConformance, aviatModemModStatsTxSecs=aviatModemModStatsTxSecs, aviatModemMLHCEnabled=aviatModemMLHCEnabled, aviatModemXpicTable=aviatModemXpicTable, aviatModemXpicEntry=aviatModemXpicEntry, aviatModemModulationMax=aviatModemModulationMax, aviatModemCompliance=aviatModemCompliance, aviatModemCurCapacityTx=aviatModemCurCapacityTx, aviatModemModulation=aviatModemModulation, aviatModemXpicEnable=aviatModemXpicEnable, aviatModemStatusTable=aviatModemStatusTable, aviatModemModStatsRxPct=aviatModemModStatsRxPct, aviatModemBandwidth=aviatModemBandwidth, aviatModemModulationBase=aviatModemModulationBase, aviatModemModStatsModulation=aviatModemModStatsModulation, aviatModemModulationEntry=aviatModemModulationEntry, aviatModemMIBObjects=aviatModemMIBObjects, aviatModemModule=aviatModemModule, aviatModemModulationIndex=aviatModemModulationIndex, aviatModemStatusOper=aviatModemStatusOper, aviatModemXpicGroup=aviatModemXpicGroup, aviatModemCapacity=aviatModemCapacity, aviatModemModStatsTxPct=aviatModemModStatsTxPct, aviatModemModulationStatsEntry=aviatModemModulationStatsEntry, aviatModemGroups=aviatModemGroups, aviatModemModulationType=aviatModemModulationType, aviatModemStatusEntry=aviatModemStatusEntry, aviatModemTable=aviatModemTable, aviatModemEntry=aviatModemEntry, aviatModemRegulatoryStandard=aviatModemRegulatoryStandard, aviatModemL1laLiteEnabled=aviatModemL1laLiteEnabled, aviatModemLicensedModulationMask=aviatModemLicensedModulationMask, aviatModemModulationTable=aviatModemModulationTable, aviatModemModulationCurrentGroup=aviatModemModulationCurrentGroup, AviatModemCapacityType=AviatModemCapacityType, aviatModemModStatsRxSecs=aviatModemModStatsRxSecs, aviatModemObjectGroup=aviatModemObjectGroup, aviatModemStatusMaxCapacity=aviatModemStatusMaxCapacity, PYSNMP_MODULE_ID=aviatModemModule, aviatModemModulationStatsTable=aviatModemModulationStatsTable, aviatModemStatusGroup=aviatModemStatusGroup, aviatModemProfileVersion=aviatModemProfileVersion, aviatModemCurModulationTx=aviatModemCurModulationTx, aviatModemModulationStatsGroup=aviatModemModulationStatsGroup)
