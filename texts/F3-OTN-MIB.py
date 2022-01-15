#
# PySNMP MIB module F3-OTN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-OTN-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:50:40 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
PerfCounter64, CmPmIntervalType = mibBuilder.importSymbols("CM-COMMON-MIB", "PerfCounter64", "CmPmIntervalType")
cmEthernetNetPortEntry, = mibBuilder.importSymbols("CM-FACILITY-MIB", "cmEthernetNetPortEntry")
cmEthernetNetPortHistoryEntry, cmEthernetNetPortStatsEntry = mibBuilder.importSymbols("CM-PERFORMANCE-MIB", "cmEthernetNetPortHistoryEntry", "cmEthernetNetPortStatsEntry")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits, NotificationType, Gauge32, Integer32, IpAddress, Unsigned32, ObjectIdentity, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits", "NotificationType", "Gauge32", "Integer32", "IpAddress", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Counter32")
VariablePointer, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "VariablePointer", "TextualConvention", "TruthValue", "DisplayString")
f3OtnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34))
f3OtnMIB.setRevisions(('2014-07-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f3OtnMIB.setRevisionsDescriptions(('\n         Notes from release 201407150000Z,\n         (1) MIB version ready for release FSP150CC 6.5.CC.',))
if mibBuilder.loadTexts: f3OtnMIB.setLastUpdated('201407150000Z')
if mibBuilder.loadTexts: f3OtnMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: f3OtnMIB.setContactInfo('        Michal Pawlowski\n                     ADVA Optical Networking, Inc.\n                Tel: +48 58 7716 416\n             E-mail: mpawlowski@advaoptical.com\n             Postal: ul. Slaska 35/37\n                     81-310 Gdynia, Poland')
if mibBuilder.loadTexts: f3OtnMIB.setDescription('This module defines the OTN MIB definitions \n             used by the F3 (FSP150CM/CC) product lines.\n             Copyright (C) ADVA Optical Networking.')
f3OtnConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1))
f3OtnPerfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2))
f3OtnConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3))
class OtnFacilityType(TextualConvention, Integer32):
    description = 'OTN Facility Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("otu2e-eth", 1))

class OtnFecType(TextualConvention, Integer32):
    description = 'OTN Forward Error Correction (FEC) Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("nofec", 1), ("gfec", 2), ("efec-1", 3), ("efec-2", 4))

class TimDetectMode(TextualConvention, Integer32):
    description = 'Trace Identifier Mismatch (TIM) Detect Mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("off", 1), ("sapi", 2), ("dapi", 3), ("sapi-dapi", 4))

f3OtnNetPortExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1), )
if mibBuilder.loadTexts: f3OtnNetPortExtTable.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortExtTable.setDescription('A list of entries corresponding to Ethernet Network Port\n             Facilities for the OTN attributes configuration purposes.')
f3OtnNetPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1), )
cmEthernetNetPortEntry.registerAugmentions(("F3-OTN-MIB", "f3OtnNetPortEntry"))
f3OtnNetPortEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
if mibBuilder.loadTexts: f3OtnNetPortEntry.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortEntry.setDescription('A conceptual row in the f3OtnNetPortEntry.')
f3OtnNetPortPayloadType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortPayloadType.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortPayloadType.setDescription('Represents the value to be transmitted in the PT signal of\n             the OPU Payload Structure Identifier (PSI) overhead.\n             The value is also used for detection of Payload Label Mismatch of\n             the PT signal in the received ODU PSI overhead.')
f3OtnNetPortFacilityType = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 2), OtnFacilityType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortFacilityType.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortFacilityType.setDescription('Represents the OTN transport wrapper and payload.')
f3OtnNetPortFec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 3), OtnFecType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortFec.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortFec.setDescription('Represents the Forward Error Correction (FEC) for the\n             OTN transport frame.')
f3OtnNetPortTimDetectModeOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 4), TimDetectMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTimDetectModeOtu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTimDetectModeOtu.setDescription('Represents the support for Trace Identifier Mismatch (TIM)\n             detection in the OTU overhead.')
f3OtnNetPortTimAisInsertOtuEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTimAisInsertOtuEnabled.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTimAisInsertOtuEnabled.setDescription('Represents the support for downstream AIS insertion when OTU\n             Trace Identifier Mismatch (TIM) is detected.')
f3OtnNetPortTtiActualRxHexOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiActualRxHexOtu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiActualRxHexOtu.setDescription('Represents the value of the Trail Trace Identifier (TTI)\n             in the OTU overhead.')
f3OtnNetPortTtiSapiActualRxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiActualRxOtu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiActualRxOtu.setDescription('Represents the SAPI value of the Trail Trace Identifier (TTI)\n             in the OTU overhead.')
f3OtnNetPortTtiDapiActualRxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiActualRxOtu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiActualRxOtu.setDescription('Represents the DAPI value of the Trail Trace Identifier (TTI)\n             in the OTU overhead.')
f3OtnNetPortTtiOpSpActualRxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpActualRxOtu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpActualRxOtu.setDescription('Represents the Operator Specific (OpSp) value of the\n             Trail Trace Identifier (TTI) in the OTU overhead.')
f3OtnNetPortTtiSapiExpectedRxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiExpectedRxOtu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiExpectedRxOtu.setDescription('Represents the expected SAPI value in the received OTU overhead.')
f3OtnNetPortTtiSapiTxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiTxOtu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiTxOtu.setDescription('Represents the SAPI value in the transmitted OTU overhead.')
f3OtnNetPortTtiDapiTxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiTxOtu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiTxOtu.setDescription('Represents the DAPI value in the transmitted OTU overhead.')
f3OtnNetPortTtiOpSpTxOtu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpTxOtu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpTxOtu.setDescription('Represents the Operator Specific (OpSp) value in the transmitted\n             OTU overhead.')
f3OtnNetPortTimDetectModeOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 14), TimDetectMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTimDetectModeOdu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTimDetectModeOdu.setDescription('Represents the support for Trace Identifier Mismatch (TIM)\n             detection in the ODU overhead.')
f3OtnNetPortTimAisInsertOduEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 15), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTimAisInsertOduEnabled.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTimAisInsertOduEnabled.setDescription('Represents the support for downstream AIS insertion when ODU\n             Trace Identifier Mismatch (TIM) is detected.')
f3OtnNetPortTtiActualRxHexOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 16), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiActualRxHexOdu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiActualRxHexOdu.setDescription('Represents the value of the Trail Trace Identifier (TTI)\n             in the ODU overhead.')
f3OtnNetPortTtiSapiActualRxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiActualRxOdu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiActualRxOdu.setDescription('Represents the SAPI value of the Trail Trace Identifier (TTI)\n             in the ODU overhead.')
f3OtnNetPortTtiDapiActualRxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 18), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiActualRxOdu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiActualRxOdu.setDescription('Represents the DAPI value of the Trail Trace Identifier (TTI)\n             in the ODU overhead.')
f3OtnNetPortTtiOpSpActualRxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 19), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpActualRxOdu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpActualRxOdu.setDescription('Represents the Operator Specific (OpSp) value of\n             the Trail Trace Identifier (TTI) in the ODU overhead.')
f3OtnNetPortTtiSapiExpectedRxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 20), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiExpectedRxOdu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiExpectedRxOdu.setDescription('Represents the expected SAPI value in the received ODU overhead.')
f3OtnNetPortTtiSapiTxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 21), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiTxOdu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiSapiTxOdu.setDescription('Represents the SAPI value in the transmitted ODU overhead.')
f3OtnNetPortTtiDapiTxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 22), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiTxOdu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiDapiTxOdu.setDescription('Represents the DAPI value in the transmitted ODU overhead.')
f3OtnNetPortTtiOpSpTxOdu = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 1, 1, 1, 23), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpTxOdu.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortTtiOpSpTxOdu.setDescription('Represents the Operator Specific (OpSp) value in the transmitted ODU overhead.')
f3OtnNetPortStatsExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1), )
if mibBuilder.loadTexts: f3OtnNetPortStatsExtTable.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtTable.setDescription('A collection of Ethernet Network Port OTN attributes \n             related statistics. These reflect the current data.')
f3OtnNetPortStatsExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1), )
cmEthernetNetPortStatsEntry.registerAugmentions(("F3-OTN-MIB", "f3OtnNetPortStatsExtEntry"))
f3OtnNetPortStatsExtEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
if mibBuilder.loadTexts: f3OtnNetPortStatsExtEntry.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtEntry.setDescription('A conceptual row in the f3OtnNetPortStatsExtEntry.')
f3OtnNetPortStatsExtBerBeforeCorr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 1), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtBerBeforeCorr.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtBerBeforeCorr.setDescription("Ber Before Correction.\n          Lower 32 bits represent the value in a Decimal32 interchange format.\n          For details on encoding please refer to Decimal32's description,\n          defined in fsp150cm-common.mib.")
f3OtnNetPortStatsExtFecErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecErrSec.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecErrSec.setDescription('FEC Errored Seconds.')
f3OtnNetPortStatsExtFecSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecSES.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecSES.setDescription('FEC SES.')
f3OtnNetPortStatsExtFecCorrErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 4), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecCorrErr.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecCorrErr.setDescription('FEC Corrected Seconds.')
f3OtnNetPortStatsExtFecUncorrBlockErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 5), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecUncorrBlockErr.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtFecUncorrBlockErr.setDescription('FEC Uncorrected Block Errors.')
f3OtnNetPortStatsExtOtuErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuErrSec.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuErrSec.setDescription('OTU Errored Seconds.')
f3OtnNetPortStatsExtOtuSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuSES.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuSES.setDescription('OTU SES.')
f3OtnNetPortStatsExtOtuBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 8), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuBBE.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuBBE.setDescription('OTU BBE.')
f3OtnNetPortStatsExtOtuUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuUAS.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOtuUAS.setDescription('OTU UAS.')
f3OtnNetPortStatsExtOduErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduErrSec.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduErrSec.setDescription('ODU Errored Seconds.')
f3OtnNetPortStatsExtOduSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduSES.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduSES.setDescription('ODU SES.')
f3OtnNetPortStatsExtOduBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 12), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduBBE.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduBBE.setDescription('ODU BBE.')
f3OtnNetPortStatsExtOduUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduUAS.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortStatsExtOduUAS.setDescription('ODU UAS.')
f3OtnNetPortHistoryExtTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2), )
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtTable.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtTable.setDescription('A collection of Ethernet Network Port OTN attributes \n             related statistics. These reflect the history data.')
f3OtnNetPortHistoryExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1), )
cmEthernetNetPortHistoryEntry.registerAugmentions(("F3-OTN-MIB", "f3OtnNetPortHistoryExtEntry"))
f3OtnNetPortHistoryExtEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtEntry.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtEntry.setDescription('A conceptual row in the f3OtnNetPortHistoryExtEntry.')
f3OtnNetPortHistoryExtBerBeforeCorr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 1), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtBerBeforeCorr.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtBerBeforeCorr.setDescription('Ber Before Correction.')
f3OtnNetPortHistoryExtFecErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecErrSec.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecErrSec.setDescription('FEC Errored Seconds.')
f3OtnNetPortHistoryExtFecSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecSES.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecSES.setDescription('FEC SES.')
f3OtnNetPortHistoryExtFecCorrErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 4), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecCorrErr.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecCorrErr.setDescription('FEC Corrected Seconds.')
f3OtnNetPortHistoryExtFecUncorrBlockErr = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 5), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecUncorrBlockErr.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtFecUncorrBlockErr.setDescription('FEC Uncorrected Block Errors.')
f3OtnNetPortHistoryExtOtuErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuErrSec.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuErrSec.setDescription('OTU Errored Seconds.')
f3OtnNetPortHistoryExtOtuSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuSES.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuSES.setDescription('OTU SES.')
f3OtnNetPortHistoryExtOtuBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 8), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuBBE.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuBBE.setDescription('OTU BBE.')
f3OtnNetPortHistoryExtOtuUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuUAS.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOtuUAS.setDescription('OTU UAS.')
f3OtnNetPortHistoryExtOduErrSec = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduErrSec.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduErrSec.setDescription('ODU Errored Seconds.')
f3OtnNetPortHistoryExtOduSES = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduSES.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduSES.setDescription('ODU SES.')
f3OtnNetPortHistoryExtOduBBE = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 12), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduBBE.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduBBE.setDescription('ODU BBE.')
f3OtnNetPortHistoryExtOduUAS = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 2, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduUAS.setStatus('current')
if mibBuilder.loadTexts: f3OtnNetPortHistoryExtOduUAS.setDescription('ODU UAS.')
f3OtnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 1))
f3OtnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 2))
f3OtnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 1, 1)).setObjects(("F3-OTN-MIB", "f3OtnConfigGroup"), ("F3-OTN-MIB", "f3OtnPerfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OtnCompliance = f3OtnCompliance.setStatus('current')
if mibBuilder.loadTexts: f3OtnCompliance.setDescription('Describes the requirements for conformance to the F3-OTN-MIB compliance.')
f3OtnConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 2, 1)).setObjects(("F3-OTN-MIB", "f3OtnNetPortPayloadType"), ("F3-OTN-MIB", "f3OtnNetPortFacilityType"), ("F3-OTN-MIB", "f3OtnNetPortFec"), ("F3-OTN-MIB", "f3OtnNetPortTimDetectModeOtu"), ("F3-OTN-MIB", "f3OtnNetPortTimAisInsertOtuEnabled"), ("F3-OTN-MIB", "f3OtnNetPortTtiActualRxHexOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiActualRxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiDapiActualRxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpActualRxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiExpectedRxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiTxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiDapiTxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpTxOtu"), ("F3-OTN-MIB", "f3OtnNetPortTimDetectModeOdu"), ("F3-OTN-MIB", "f3OtnNetPortTimAisInsertOduEnabled"), ("F3-OTN-MIB", "f3OtnNetPortTtiActualRxHexOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiActualRxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiDapiActualRxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpActualRxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiExpectedRxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiSapiTxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiDapiTxOdu"), ("F3-OTN-MIB", "f3OtnNetPortTtiOpSpTxOdu"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OtnConfigGroup = f3OtnConfigGroup.setStatus('current')
if mibBuilder.loadTexts: f3OtnConfigGroup.setDescription('A collection of objects used to manage the OTN.')
f3OtnPerfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 34, 3, 2, 2)).setObjects(("F3-OTN-MIB", "f3OtnNetPortStatsExtBerBeforeCorr"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecErrSec"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecSES"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecCorrErr"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtFecUncorrBlockErr"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuErrSec"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuSES"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuBBE"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOtuUAS"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduErrSec"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduSES"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduBBE"), ("F3-OTN-MIB", "f3OtnNetPortStatsExtOduUAS"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtBerBeforeCorr"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecErrSec"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecSES"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecCorrErr"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtFecUncorrBlockErr"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuErrSec"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuSES"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuBBE"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOtuUAS"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduErrSec"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduSES"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduBBE"), ("F3-OTN-MIB", "f3OtnNetPortHistoryExtOduUAS"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3OtnPerfGroup = f3OtnPerfGroup.setStatus('current')
if mibBuilder.loadTexts: f3OtnPerfGroup.setDescription('A collection of objects used to manage the OTN PM.')
mibBuilder.exportSymbols("F3-OTN-MIB", f3OtnNetPortTtiSapiTxOdu=f3OtnNetPortTtiSapiTxOdu, f3OtnNetPortTtiOpSpActualRxOtu=f3OtnNetPortTtiOpSpActualRxOtu, f3OtnConformance=f3OtnConformance, f3OtnNetPortStatsExtFecUncorrBlockErr=f3OtnNetPortStatsExtFecUncorrBlockErr, f3OtnCompliances=f3OtnCompliances, f3OtnConfigObjects=f3OtnConfigObjects, f3OtnNetPortHistoryExtFecUncorrBlockErr=f3OtnNetPortHistoryExtFecUncorrBlockErr, f3OtnNetPortTimAisInsertOduEnabled=f3OtnNetPortTimAisInsertOduEnabled, f3OtnNetPortStatsExtBerBeforeCorr=f3OtnNetPortStatsExtBerBeforeCorr, f3OtnNetPortTtiDapiActualRxOtu=f3OtnNetPortTtiDapiActualRxOtu, f3OtnNetPortHistoryExtOtuUAS=f3OtnNetPortHistoryExtOtuUAS, f3OtnNetPortHistoryExtFecCorrErr=f3OtnNetPortHistoryExtFecCorrErr, f3OtnNetPortTtiSapiTxOtu=f3OtnNetPortTtiSapiTxOtu, f3OtnNetPortStatsExtOtuBBE=f3OtnNetPortStatsExtOtuBBE, f3OtnNetPortTtiDapiTxOdu=f3OtnNetPortTtiDapiTxOdu, f3OtnPerfGroup=f3OtnPerfGroup, f3OtnNetPortPayloadType=f3OtnNetPortPayloadType, f3OtnNetPortStatsExtTable=f3OtnNetPortStatsExtTable, f3OtnNetPortHistoryExtOduBBE=f3OtnNetPortHistoryExtOduBBE, f3OtnConfigGroup=f3OtnConfigGroup, f3OtnNetPortTimDetectModeOtu=f3OtnNetPortTimDetectModeOtu, f3OtnNetPortStatsExtOduSES=f3OtnNetPortStatsExtOduSES, f3OtnMIB=f3OtnMIB, f3OtnNetPortStatsExtFecErrSec=f3OtnNetPortStatsExtFecErrSec, f3OtnNetPortTtiOpSpTxOdu=f3OtnNetPortTtiOpSpTxOdu, f3OtnNetPortHistoryExtOtuErrSec=f3OtnNetPortHistoryExtOtuErrSec, f3OtnNetPortHistoryExtOduErrSec=f3OtnNetPortHistoryExtOduErrSec, f3OtnNetPortTtiSapiExpectedRxOdu=f3OtnNetPortTtiSapiExpectedRxOdu, f3OtnNetPortStatsExtOduBBE=f3OtnNetPortStatsExtOduBBE, f3OtnNetPortTtiSapiActualRxOtu=f3OtnNetPortTtiSapiActualRxOtu, f3OtnNetPortHistoryExtOduUAS=f3OtnNetPortHistoryExtOduUAS, f3OtnNetPortHistoryExtTable=f3OtnNetPortHistoryExtTable, f3OtnNetPortFec=f3OtnNetPortFec, f3OtnPerfObjects=f3OtnPerfObjects, f3OtnNetPortTtiSapiActualRxOdu=f3OtnNetPortTtiSapiActualRxOdu, f3OtnNetPortHistoryExtFecErrSec=f3OtnNetPortHistoryExtFecErrSec, f3OtnNetPortStatsExtOtuUAS=f3OtnNetPortStatsExtOtuUAS, f3OtnNetPortEntry=f3OtnNetPortEntry, f3OtnNetPortStatsExtEntry=f3OtnNetPortStatsExtEntry, f3OtnNetPortTtiDapiActualRxOdu=f3OtnNetPortTtiDapiActualRxOdu, f3OtnNetPortHistoryExtOtuBBE=f3OtnNetPortHistoryExtOtuBBE, f3OtnNetPortStatsExtOtuErrSec=f3OtnNetPortStatsExtOtuErrSec, OtnFacilityType=OtnFacilityType, f3OtnNetPortHistoryExtOduSES=f3OtnNetPortHistoryExtOduSES, f3OtnNetPortStatsExtFecSES=f3OtnNetPortStatsExtFecSES, f3OtnGroups=f3OtnGroups, f3OtnNetPortTtiOpSpTxOtu=f3OtnNetPortTtiOpSpTxOtu, f3OtnNetPortStatsExtFecCorrErr=f3OtnNetPortStatsExtFecCorrErr, f3OtnNetPortStatsExtOtuSES=f3OtnNetPortStatsExtOtuSES, f3OtnNetPortExtTable=f3OtnNetPortExtTable, f3OtnNetPortStatsExtOduUAS=f3OtnNetPortStatsExtOduUAS, OtnFecType=OtnFecType, f3OtnNetPortFacilityType=f3OtnNetPortFacilityType, TimDetectMode=TimDetectMode, f3OtnNetPortTtiOpSpActualRxOdu=f3OtnNetPortTtiOpSpActualRxOdu, f3OtnNetPortHistoryExtFecSES=f3OtnNetPortHistoryExtFecSES, f3OtnNetPortTtiActualRxHexOdu=f3OtnNetPortTtiActualRxHexOdu, f3OtnNetPortTtiActualRxHexOtu=f3OtnNetPortTtiActualRxHexOtu, f3OtnNetPortTtiDapiTxOtu=f3OtnNetPortTtiDapiTxOtu, f3OtnNetPortTtiSapiExpectedRxOtu=f3OtnNetPortTtiSapiExpectedRxOtu, f3OtnNetPortHistoryExtBerBeforeCorr=f3OtnNetPortHistoryExtBerBeforeCorr, f3OtnNetPortTimAisInsertOtuEnabled=f3OtnNetPortTimAisInsertOtuEnabled, f3OtnNetPortStatsExtOduErrSec=f3OtnNetPortStatsExtOduErrSec, f3OtnCompliance=f3OtnCompliance, f3OtnNetPortHistoryExtOtuSES=f3OtnNetPortHistoryExtOtuSES, f3OtnNetPortTimDetectModeOdu=f3OtnNetPortTimDetectModeOdu, PYSNMP_MODULE_ID=f3OtnMIB, f3OtnNetPortHistoryExtEntry=f3OtnNetPortHistoryExtEntry)
