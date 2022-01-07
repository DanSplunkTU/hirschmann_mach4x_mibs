#
# PySNMP MIB module ACD-SMAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-SMAP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:51:55 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, iso, TimeTicks, Counter32, ObjectIdentity, NotificationType, Integer32, Unsigned32, Counter64, Gauge32, ModuleIdentity, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "iso", "TimeTicks", "Counter32", "ObjectIdentity", "NotificationType", "Integer32", "Unsigned32", "Counter64", "Gauge32", "ModuleIdentity", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
acdSmap = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 8))
acdSmap.setRevisions(('2008-10-01 01:00', '2008-06-15 01:00',))
if mibBuilder.loadTexts: acdSmap.setLastUpdated('200810010100Z')
if mibBuilder.loadTexts: acdSmap.setOrganization('Accedian Networks, Inc.')
acdSmapNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 0))
acdSmapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1))
acdSmapConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2))
acdSmapConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1))
acdSmapCoSProfTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1), )
if mibBuilder.loadTexts: acdSmapCoSProfTable.setStatus('current')
acdSmapCoSProfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapCoSProfID"))
if mibBuilder.loadTexts: acdSmapCoSProfEntry.setStatus('current')
acdSmapCoSProfID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSmapCoSProfID.setStatus('current')
acdSmapCoSProfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfRowStatus.setStatus('current')
acdSmapCoSProfName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfName.setStatus('current')
acdSmapCoSProfType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pcp", 1), ("dscp", 2), ("pre", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfType.setStatus('current')
acdSmapCoSProfDecodeDropBit = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfDecodeDropBit.setStatus('current')
acdSmapCoSProfEncodeDropBit = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapCoSProfEncodeDropBit.setStatus('current')
acdSmapCoSProfCodePointTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2), )
if mibBuilder.loadTexts: acdSmapCoSProfCodePointTable.setStatus('current')
acdSmapCoSProfCodePointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapCoSProfID"), (0, "ACD-SMAP-MIB", "acdSmapCoSProfCodePointID"))
if mibBuilder.loadTexts: acdSmapCoSProfCodePointEntry.setStatus('current')
acdSmapCoSProfCodePointID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: acdSmapCoSProfCodePointID.setStatus('current')
acdSmapCoSProfCodePointPreMarkingColor = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("green", 1), ("yellow", 2))).clone('green')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapCoSProfCodePointPreMarkingColor.setStatus('current')
acdSmapCoSProfCodePointGreenOut = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapCoSProfCodePointGreenOut.setStatus('current')
acdSmapCoSProfCodePointYellowOut = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 2, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapCoSProfCodePointYellowOut.setStatus('current')
acdSmapRegSetTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3), )
if mibBuilder.loadTexts: acdSmapRegSetTable.setStatus('current')
acdSmapRegSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapRegSetID"))
if mibBuilder.loadTexts: acdSmapRegSetEntry.setStatus('current')
acdSmapRegSetID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdSmapRegSetID.setStatus('current')
acdSmapRegSetRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapRegSetRowStatus.setStatus('current')
acdSmapRegSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapRegSetName.setStatus('current')
acdSmapRegSetType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pcp", 1), ("dscp", 2), ("pre", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: acdSmapRegSetType.setStatus('current')
acdSmapRegSetCodePointTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4), )
if mibBuilder.loadTexts: acdSmapRegSetCodePointTable.setStatus('current')
acdSmapRegSetCodePointEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1), ).setIndexNames((0, "ACD-SMAP-MIB", "acdSmapRegSetID"), (0, "ACD-SMAP-MIB", "acdSmapRegSetCodePointID"))
if mibBuilder.loadTexts: acdSmapRegSetCodePointEntry.setStatus('current')
acdSmapRegSetCodePointID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 63)))
if mibBuilder.loadTexts: acdSmapRegSetCodePointID.setStatus('current')
acdSmapRegSetCodePointRegulatorID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapRegSetCodePointRegulatorID.setStatus('current')
acdSmapRegSetCodePointRegulatorEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 8, 1, 1, 4, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: acdSmapRegSetCodePointRegulatorEnable.setStatus('current')
acdSmapCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 1))
acdSmapGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2))
acdSmapCoSProfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 1)).setObjects(("ACD-SMAP-MIB", "acdSmapCoSProfRowStatus"), ("ACD-SMAP-MIB", "acdSmapCoSProfName"), ("ACD-SMAP-MIB", "acdSmapCoSProfType"), ("ACD-SMAP-MIB", "acdSmapCoSProfDecodeDropBit"), ("ACD-SMAP-MIB", "acdSmapCoSProfEncodeDropBit"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapCoSProfGroup = acdSmapCoSProfGroup.setStatus('current')
acdSmapCoSProfCodePointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 2)).setObjects(("ACD-SMAP-MIB", "acdSmapCoSProfCodePointPreMarkingColor"), ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointGreenOut"), ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointYellowOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapCoSProfCodePointGroup = acdSmapCoSProfCodePointGroup.setStatus('current')
acdSmapRegSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 3)).setObjects(("ACD-SMAP-MIB", "acdSmapRegSetRowStatus"), ("ACD-SMAP-MIB", "acdSmapRegSetName"), ("ACD-SMAP-MIB", "acdSmapRegSetType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapRegSetGroup = acdSmapRegSetGroup.setStatus('current')
acdSmapRegSetCodePointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 2, 4)).setObjects(("ACD-SMAP-MIB", "acdSmapRegSetCodePointRegulatorID"), ("ACD-SMAP-MIB", "acdSmapRegSetCodePointRegulatorEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapRegSetCodePointGroup = acdSmapRegSetCodePointGroup.setStatus('current')
acdSmapCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 8, 2, 1, 1)).setObjects(("ACD-SMAP-MIB", "acdSmapCoSProfGroup"), ("ACD-SMAP-MIB", "acdSmapCoSProfCodePointGroup"), ("ACD-SMAP-MIB", "acdSmapRegSetGroup"), ("ACD-SMAP-MIB", "acdSmapRegSetCodePointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdSmapCompliance = acdSmapCompliance.setStatus('current')
mibBuilder.exportSymbols("ACD-SMAP-MIB", acdSmapRegSetTable=acdSmapRegSetTable, acdSmapRegSetEntry=acdSmapRegSetEntry, acdSmapCompliances=acdSmapCompliances, acdSmapRegSetID=acdSmapRegSetID, acdSmapRegSetCodePointRegulatorID=acdSmapRegSetCodePointRegulatorID, acdSmapCoSProfType=acdSmapCoSProfType, acdSmapCoSProfCodePointGroup=acdSmapCoSProfCodePointGroup, acdSmapCoSProfCodePointGreenOut=acdSmapCoSProfCodePointGreenOut, acdSmapRegSetType=acdSmapRegSetType, acdSmapCoSProfCodePointTable=acdSmapCoSProfCodePointTable, acdSmapRegSetName=acdSmapRegSetName, acdSmap=acdSmap, acdSmapCoSProfEncodeDropBit=acdSmapCoSProfEncodeDropBit, acdSmapNotifications=acdSmapNotifications, acdSmapCoSProfRowStatus=acdSmapCoSProfRowStatus, acdSmapCoSProfDecodeDropBit=acdSmapCoSProfDecodeDropBit, acdSmapCoSProfCodePointEntry=acdSmapCoSProfCodePointEntry, acdSmapRegSetGroup=acdSmapRegSetGroup, acdSmapConfig=acdSmapConfig, acdSmapRegSetCodePointRegulatorEnable=acdSmapRegSetCodePointRegulatorEnable, acdSmapRegSetCodePointEntry=acdSmapRegSetCodePointEntry, PYSNMP_MODULE_ID=acdSmap, acdSmapCoSProfEntry=acdSmapCoSProfEntry, acdSmapRegSetRowStatus=acdSmapRegSetRowStatus, acdSmapCoSProfID=acdSmapCoSProfID, acdSmapCoSProfGroup=acdSmapCoSProfGroup, acdSmapCompliance=acdSmapCompliance, acdSmapCoSProfTable=acdSmapCoSProfTable, acdSmapCoSProfCodePointYellowOut=acdSmapCoSProfCodePointYellowOut, acdSmapCoSProfName=acdSmapCoSProfName, acdSmapMIBObjects=acdSmapMIBObjects, acdSmapCoSProfCodePointPreMarkingColor=acdSmapCoSProfCodePointPreMarkingColor, acdSmapRegSetCodePointID=acdSmapRegSetCodePointID, acdSmapRegSetCodePointGroup=acdSmapRegSetCodePointGroup, acdSmapCoSProfCodePointID=acdSmapCoSProfCodePointID, acdSmapGroups=acdSmapGroups, acdSmapConformance=acdSmapConformance, acdSmapRegSetCodePointTable=acdSmapRegSetCodePointTable)
