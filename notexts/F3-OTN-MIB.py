#
# PySNMP MIB module F3-OTN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-OTN-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:20 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
PerfCounter64, CmPmIntervalType = mibBuilder.importSymbols("CM-COMMON-MIB", "PerfCounter64", "CmPmIntervalType")
cmEthernetNetPortEntry, = mibBuilder.importSymbols("CM-FACILITY-MIB", "cmEthernetNetPortEntry")
cmEthernetNetPortStatsEntry, cmEthernetNetPortHistoryEntry = mibBuilder.importSymbols("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsEntry", "cmEthernetNetPortHistoryEntry")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Counter64, TimeTicks, MibIdentifier, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, IpAddress, Integer32, Unsigned32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "TimeTicks", "MibIdentifier", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "IpAddress", "Integer32", "Unsigned32", "ModuleIdentity", "iso")
VariablePointer, TruthValue, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "VariablePointer", "TruthValue", "DisplayString", "TextualConvention")
f3OtnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34))
f3OtnMIB.setRevisions(('2014-07-15 00:00',))
if mibBuilder.loadTexts: f3OtnMIB.setLastUpdated('201407150000Z')
if mibBuilder.loadTexts: f3OtnMIB.setOrganization('ADVA Optical Networking')
f3OtnConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1))
f3OtnPerfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2))
f3OtnConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3))
class OtnFacilityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("otu2e-eth", 1))

class OtnFecType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("nofec", 1), ("gfec", 2), ("efec-1", 3), ("efec-2", 4))

class TimDetectMode(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("off", 1), ("sapi", 2), ("dapi", 3), ("sapi-dapi", 4))

f3OtnNetPortExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1), )
if mibBuilder.loadTexts: f3OtnNetPortExtTable.setStatus('current')
f3OtnNetPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1), )
cmEthernetNetPortEntry.registerAugmentions(("F3-OTN-MIB", "f3OtnNetPortEntry"))
f3OtnNetPortEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
if mibBuilder.loadTexts: f3OtnNetPortEntry.setStatus('current')
f3OtnNetPortPayloadType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortPayloadType.setStatus('current')
f3OtnNetPortFacilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 2), OtnFacilityType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortFacilityType.setStatus('current')
f3OtnNetPortFec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 3), OtnFecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortFec.setStatus('current')
f3OtnNetPortTimDetectModeOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 4), TimDetectMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTimDetectModeOtu.setStatus('current')
f3OtnNetPortTimAisInsertOtuEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTimAisInsertOtuEnabled.setStatus('current')
f3OtnNetPortTtiActualRxHexOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiActualRxHexOtu.setStatus('current')
f3OtnNetPortTtiSapiActualRxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiActualRxOtu.setStatus('current')
f3OtnNetPortTtiDapiActualRxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiActualRxOtu.setStatus('current')
f3OtnNetPortTtiOpSpActualRxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpActualRxOtu.setStatus('current')
f3OtnNetPortTtiSapiExpectedRxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiExpectedRxOtu.setStatus('current')
f3OtnNetPortTtiSapiTxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiTxOtu.setStatus('current')
f3OtnNetPortTtiDapiTxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiTxOtu.setStatus('current')
f3OtnNetPortTtiOpSpTxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpTxOtu.setStatus('current')
f3OtnNetPortTimDetectModeOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 14), TimDetectMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTimDetectModeOdu.setStatus('current')
f3OtnNetPortTimAisInsertOduEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTimAisInsertOduEnabled.setStatus('current')
f3OtnNetPortTtiActualRxHexOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiActualRxHexOdu.setStatus('current')
f3OtnNetPortTtiSapiActualRxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiActualRxOdu.setStatus('current')
f3OtnNetPortTtiDapiActualRxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiActualRxOdu.setStatus('current')
f3OtnNetPortTtiOpSpActualRxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpActualRxOdu.setStatus('current')
f3OtnNetPortTtiSapiExpectedRxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiExpectedRxOdu.setStatus('current')
f3OtnNetPortTtiSapiTxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiTxOdu.setStatus('current')
f3OtnNetPortTtiDapiTxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiTxOdu.setStatus('current')
f3OtnNetPortTtiOpSpTxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpTxOdu.setStatus('current')
f3OtnNetPortStatsExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1), )
if mibBuilder.loadTexts: f3OtnNetPortStatsExtTable.setStatus('current')
f3OtnNetPortStatsExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1), )
cmEthernetNetPortStatsEntry.registerAugmentions(("F3-OTN-MIB", "f3OtnNetPortStatsExtEntry"))
f3OtnNetPortStatsExtEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
if mibBuilder.loadTexts: f3OtnNetPortStatsExtEntry.setStatus('current')
f3OtnNetPortStatsExtBerBeforeCorr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 1), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtBerBeforeCorr.setStatus('current')
f3OtnNetPortStatsExtFecErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecErrSec.setStatus('current')
f3OtnNetPortStatsExtFecSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecSES.setStatus('current')
f3OtnNetPortStatsExtFecCorrErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 4), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecCorrErr.setStatus('current')
f3OtnNetPortStatsExtFecUncorrBlockErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 5), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecUncorrBlockErr.setStatus('current')
f3OtnNetPortStatsExtOtuErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuErrSec.setStatus('current')
f3OtnNetPortStatsExtOtuSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuSES.setStatus('current')
f3OtnNetPortStatsExtOtuBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 8), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuBBE.setStatus('current')
f3OtnNetPortStatsExtOtuUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuUAS.setStatus('current')
f3OtnNetPortStatsExtOduErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduErrSec.setStatus('current')
f3OtnNetPortStatsExtOduSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduSES.setStatus('current')
f3OtnNetPortStatsExtOduBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 12), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduBBE.setStatus('current')
f3OtnNetPortStatsExtOduUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduUAS.setStatus('current')
f3OtnNetPortHistoryExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2), )
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtTable.setStatus('current')
f3OtnNetPortHistoryExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1), )
cmEthernetNetPortHistoryEntry.registerAugmentions(("F3-OTN-MIB", "f3OtnNetPortHistoryExtEntry"))
f3OtnNetPortHistoryExtEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtEntry.setStatus('current')
f3OtnNetPortHistoryExtBerBeforeCorr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 1), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtBerBeforeCorr.setStatus('current')
f3OtnNetPortHistoryExtFecErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecErrSec.setStatus('current')
f3OtnNetPortHistoryExtFecSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecSES.setStatus('current')
f3OtnNetPortHistoryExtFecCorrErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 4), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecCorrErr.setStatus('current')
f3OtnNetPortHistoryExtFecUncorrBlockErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 5), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecUncorrBlockErr.setStatus('current')
f3OtnNetPortHistoryExtOtuErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuErrSec.setStatus('current')
f3OtnNetPortHistoryExtOtuSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuSES.setStatus('current')
f3OtnNetPortHistoryExtOtuBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 8), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuBBE.setStatus('current')
f3OtnNetPortHistoryExtOtuUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuUAS.setStatus('current')
f3OtnNetPortHistoryExtOduErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduErrSec.setStatus('current')
f3OtnNetPortHistoryExtOduSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduSES.setStatus('current')
f3OtnNetPortHistoryExtOduBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 12), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduBBE.setStatus('current')
f3OtnNetPortHistoryExtOduUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduUAS.setStatus('current')
f3OtnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 1))
f3OtnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 2))
f3OtnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 1, 1)).setObjects(("F3-OTN-MIB", "f3OtnConfigGroup"), ("F3-OTN-MIB", "f3OtnPerfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OtnCompliance = f3OtnCompliance.setStatus('current')
f3OtnConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 2, 1)).setObjects(("F3-OTN-MIB", "f3OtnNetPortPayloadType"), ("F3-OTN-MIB", "f3OtnNetPortFacilityType"), ("F3-OTN-MIB", "f3OtnNetPortFec"), ("F3-OTN-MIB", "f3OtnNetPortTimDetectModeOtu"), ("F3-OTN-MIB", "f3OtnNetPortTimAisInsertOtuEnabled"), ("F3-OTN-MIB", "f3OtnNetPortTtiActualRxHexOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiActualRxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiDapiActualRxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpActualRxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiExpectedRxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiTxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiDapiTxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpTxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTimDetectModeOdu"), ("F3-OTN-MIB", "f3OtnNetPortTimAisInsertOduEnabled"), ("F3-OTN-MIB", "f3OtnNetPortTtiActualRxHexOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiActualRxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiDapiActualRxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpActualRxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiExpectedRxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiTxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiDapiTxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpTxOdu"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OtnConfigGroup = f3OtnConfigGroup.setStatus('current')
f3OtnPerfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 2, 2)).setObjects(("F3-OTN-MIB", "f3OtnNetPortStatsExtBerBeforeCorr"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecErrSec"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecSES"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecCorrErr"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecUncorrBlockErr"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuErrSec"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuSES"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuBBE"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuUAS"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduErrSec"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduSES"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduBBE"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduUAS"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtBerBeforeCorr"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecErrSec"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecSES"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecCorrErr"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecUncorrBlockErr"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuErrSec"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuSES"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuBBE"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuUAS"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduErrSec"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduSES"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduBBE"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduUAS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OtnPerfGroup = f3OtnPerfGroup.setStatus('current')
mibBuilder.exportSymbols("F3-OTN-MIB", f3OtnConfigObjects=f3OtnConfigObjects, f3OtnNetPortTimDetectModeOdu=f3OtnNetPortTimDetectModeOdu, f3OtnNetPortStatsExtFecErrSec=f3OtnNetPortStatsExtFecErrSec, f3OtnNetPortStatsExtBerBeforeCorr=f3OtnNetPortStatsExtBerBeforeCorr, f3OtnNetPortHistoryExtOduUAS=f3OtnNetPortHistoryExtOduUAS, f3OtnNetPortTtiSapiActualRxOtu=f3OtnNetPortTtiSapiActualRxOtu, f3OtnConformance=f3OtnConformance, f3OtnNetPortFec=f3OtnNetPortFec, f3OtnNetPortTtiDapiTxOtu=f3OtnNetPortTtiDapiTxOtu, f3OtnNetPortStatsExtFecSES=f3OtnNetPortStatsExtFecSES, f3OtnNetPortStatsExtFecUncorrBlockErr=f3OtnNetPortStatsExtFecUncorrBlockErr, f3OtnNetPortHistoryExtOtuSES=f3OtnNetPortHistoryExtOtuSES, f3OtnNetPortStatsExtOduSES=f3OtnNetPortStatsExtOduSES, f3OtnNetPortHistoryExtOtuBBE=f3OtnNetPortHistoryExtOtuBBE, f3OtnNetPortEntry=f3OtnNetPortEntry, f3OtnNetPortTtiDapiActualRxOtu=f3OtnNetPortTtiDapiActualRxOtu, f3OtnNetPortTtiSapiExpectedRxOtu=f3OtnNetPortTtiSapiExpectedRxOtu, f3OtnNetPortHistoryExtOduBBE=f3OtnNetPortHistoryExtOduBBE, f3OtnNetPortTtiActualRxHexOtu=f3OtnNetPortTtiActualRxHexOtu, f3OtnNetPortTtiActualRxHexOdu=f3OtnNetPortTtiActualRxHexOdu, f3OtnNetPortStatsExtOtuBBE=f3OtnNetPortStatsExtOtuBBE, f3OtnNetPortTimAisInsertOduEnabled=f3OtnNetPortTimAisInsertOduEnabled, f3OtnNetPortHistoryExtTable=f3OtnNetPortHistoryExtTable, f3OtnNetPortStatsExtOtuErrSec=f3OtnNetPortStatsExtOtuErrSec, f3OtnNetPortTtiSapiExpectedRxOdu=f3OtnNetPortTtiSapiExpectedRxOdu, f3OtnNetPortTtiOpSpTxOtu=f3OtnNetPortTtiOpSpTxOtu, f3OtnNetPortTtiSapiActualRxOdu=f3OtnNetPortTtiSapiActualRxOdu, f3OtnNetPortHistoryExtEntry=f3OtnNetPortHistoryExtEntry, f3OtnGroups=f3OtnGroups, OtnFacilityType=OtnFacilityType, f3OtnNetPortStatsExtOduErrSec=f3OtnNetPortStatsExtOduErrSec, f3OtnNetPortHistoryExtFecSES=f3OtnNetPortHistoryExtFecSES, f3OtnNetPortStatsExtTable=f3OtnNetPortStatsExtTable, f3OtnNetPortStatsExtOduBBE=f3OtnNetPortStatsExtOduBBE, f3OtnMIB=f3OtnMIB, f3OtnNetPortHistoryExtBerBeforeCorr=f3OtnNetPortHistoryExtBerBeforeCorr, f3OtnNetPortTtiOpSpActualRxOdu=f3OtnNetPortTtiOpSpActualRxOdu, f3OtnNetPortStatsExtFecCorrErr=f3OtnNetPortStatsExtFecCorrErr, f3OtnNetPortHistoryExtOtuUAS=f3OtnNetPortHistoryExtOtuUAS, f3OtnNetPortHistoryExtOduSES=f3OtnNetPortHistoryExtOduSES, OtnFecType=OtnFecType, f3OtnNetPortPayloadType=f3OtnNetPortPayloadType, f3OtnNetPortTtiSapiTxOtu=f3OtnNetPortTtiSapiTxOtu, f3OtnNetPortHistoryExtOduErrSec=f3OtnNetPortHistoryExtOduErrSec, f3OtnNetPortTtiOpSpActualRxOtu=f3OtnNetPortTtiOpSpActualRxOtu, f3OtnNetPortTimAisInsertOtuEnabled=f3OtnNetPortTimAisInsertOtuEnabled, f3OtnNetPortHistoryExtFecErrSec=f3OtnNetPortHistoryExtFecErrSec, f3OtnNetPortHistoryExtOtuErrSec=f3OtnNetPortHistoryExtOtuErrSec, f3OtnNetPortTtiOpSpTxOdu=f3OtnNetPortTtiOpSpTxOdu, f3OtnNetPortTtiDapiActualRxOdu=f3OtnNetPortTtiDapiActualRxOdu, f3OtnCompliance=f3OtnCompliance, f3OtnNetPortStatsExtEntry=f3OtnNetPortStatsExtEntry, TimDetectMode=TimDetectMode, f3OtnPerfObjects=f3OtnPerfObjects, f3OtnNetPortExtTable=f3OtnNetPortExtTable, f3OtnPerfGroup=f3OtnPerfGroup, PYSNMP_MODULE_ID=f3OtnMIB, f3OtnNetPortTimDetectModeOtu=f3OtnNetPortTimDetectModeOtu, f3OtnCompliances=f3OtnCompliances, f3OtnNetPortTtiDapiTxOdu=f3OtnNetPortTtiDapiTxOdu, f3OtnNetPortStatsExtOduUAS=f3OtnNetPortStatsExtOduUAS, f3OtnNetPortHistoryExtFecCorrErr=f3OtnNetPortHistoryExtFecCorrErr, f3OtnNetPortHistoryExtFecUncorrBlockErr=f3OtnNetPortHistoryExtFecUncorrBlockErr, f3OtnNetPortFacilityType=f3OtnNetPortFacilityType, f3OtnConfigGroup=f3OtnConfigGroup, f3OtnNetPortTtiSapiTxOdu=f3OtnNetPortTtiSapiTxOdu, f3OtnNetPortStatsExtOtuUAS=f3OtnNetPortStatsExtOtuUAS, f3OtnNetPortStatsExtOtuSES=f3OtnNetPortStatsExtOtuSES)
