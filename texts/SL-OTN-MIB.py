#
# PySNMP MIB module SL-OTN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-OTN-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:30:43 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slService, = mibBuilder.importSymbols("SL-NE-MIB", "slService")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
NotificationType, Bits, iso, Integer32, Counter32, Counter64, TimeTicks, Gauge32, ModuleIdentity, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "iso", "Integer32", "Counter32", "Counter64", "TimeTicks", "Gauge32", "ModuleIdentity", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress")
DateAndTime, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention", "TruthValue")
slOTN = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15))
if mibBuilder.loadTexts: slOTN.setLastUpdated('0508171200Z')
if mibBuilder.loadTexts: slOTN.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slOTN.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slOTN.setDescription('This MIB module describes the OTN')
slOTNConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1))
slOTNPm = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2))
slOTNTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 3))
class OTNTraceMessage(TextualConvention, OctetString):
    description = 'The Access Point Identifier, SAPI or DAPI.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(16, 16)
    fixedLength = 16

class OTNTrafficRate(TextualConvention, Integer32):
    description = 'The Host or Line bit rates.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("sonetSdh10G", 1), ("gbe10GLan", 2), ("fc10G", 3), ("otu2", 4), ("otu2eLan", 5), ("otu2eLanStuff", 6), ("otu2eFc", 7), ("otu2FcStuff", 8))

class OTNOperationMode(TextualConvention, Integer32):
    description = 'Indicates the operation mode of the OTN interface\n\t\tDetection function.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("async", 1), ("sync", 2), ("bypass", 3))

slOTNConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1), )
if mibBuilder.loadTexts: slOTNConfigTable.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigTable.setDescription('The OTN Configuration table.')
slOTNConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1), ).setIndexNames((0, "SL-OTN-MIB", "slOTNConfigLineIndex"))
if mibBuilder.loadTexts: slOTNConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigEntry.setDescription('An entry in the OTN Configuration table.')
slOTNConfigLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNConfigLineIndex.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigLineIndex.setDescription('The ifIndex of the XFP.')
slOTNConfigOperationMode = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 2), OTNOperationMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigOperationMode.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigOperationMode.setDescription('The OTN operation mode configuration\n    \tasync(1)   - OTN G.709 Async mapping with FEC\n    \tsync(2)    - OTN G.709 Sync mapping with FEC\n    \tbypass(3)  - OTN Bypass (Transparent Passthru)')
slOTNConfigFECEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigFECEnabled.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigFECEnabled.setDescription('FEC configuration\n\t\t0 - disable\n\t\t1 - G.709 FEC \n\t\t2 - disable\n\t\t3 - I.4\n\t\t4 - I.7\n\t\t5 - HG-FEC')
slOTNConfigStuffingEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigStuffingEnabled.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigStuffingEnabled.setDescription('Byte stuffing configuration \n    \ttrue(1)  - Enable OTN Byte Stuffing (255/237)\n\t\tfalse(2) - Disable OTN Byte Stuffing (255/238)')
slOTNConfigOTUkTIMDetEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 5), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigOTUkTIMDetEnabled.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigOTUkTIMDetEnabled.setDescription('TIM Detection Enabled.')
slOTNConfigOTUkDAPIToTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 6), OTNTraceMessage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigOTUkDAPIToTransmit.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigOTUkDAPIToTransmit.setDescription('The Destination Access Point Identifier to transmit.')
slOTNConfigOTUkSAPIToTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 7), OTNTraceMessage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigOTUkSAPIToTransmit.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigOTUkSAPIToTransmit.setDescription('The Source Access Point Identifier to transmit.')
slOTNConfigOTUkDAPIToExpect = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 8), OTNTraceMessage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigOTUkDAPIToExpect.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigOTUkDAPIToExpect.setDescription('The Destination Access Point Identifier to expect.')
slOTNConfigOTUkSAPIToExpect = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 9), OTNTraceMessage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigOTUkSAPIToExpect.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigOTUkSAPIToExpect.setDescription('The Source Access Point Identifier to expect.')
slOTNConfigOTUkDAPIReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 10), OTNTraceMessage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNConfigOTUkDAPIReceived.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigOTUkDAPIReceived.setDescription('The received Destination Access Point Identifier.')
slOTNConfigOTUkSAPIReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 11), OTNTraceMessage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNConfigOTUkSAPIReceived.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigOTUkSAPIReceived.setDescription('The received Source Access Point Identifier.')
slOTNConfigODUkTIMDetEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 12), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigODUkTIMDetEnabled.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigODUkTIMDetEnabled.setDescription('TIM Detection Enabled.')
slOTNConfigODUkDAPIToTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 13), OTNTraceMessage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigODUkDAPIToTransmit.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigODUkDAPIToTransmit.setDescription('The Destination Access Point Identifier to transmit.')
slOTNConfigODUkSAPIToTransmit = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 14), OTNTraceMessage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigODUkSAPIToTransmit.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigODUkSAPIToTransmit.setDescription('The Source Access Point Identifier to transmit.')
slOTNConfigODUkDAPIToExpect = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 15), OTNTraceMessage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigODUkDAPIToExpect.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigODUkDAPIToExpect.setDescription('The Destination Access Point Identifier to expect.')
slOTNConfigODUkSAPIToExpect = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 16), OTNTraceMessage()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigODUkSAPIToExpect.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigODUkSAPIToExpect.setDescription('The Source Access Point Identifier to expect.')
slOTNConfigODUkDAPIReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 17), OTNTraceMessage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNConfigODUkDAPIReceived.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigODUkDAPIReceived.setDescription('The received Destination Access Point Identifier.')
slOTNConfigODUkSAPIReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 18), OTNTraceMessage()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNConfigODUkSAPIReceived.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigODUkSAPIReceived.setDescription('The received Source Access Point Identifier.')
slOTNConfigOTUkTIMKillEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 19), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigOTUkTIMKillEnabled.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigOTUkTIMKillEnabled.setDescription('TIM Mismatch kill traffic Enabled.')
slOTNConfigODUkTIMKillEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 20), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigODUkTIMKillEnabled.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigODUkTIMKillEnabled.setDescription('TIM Mismatch kill traffic Enabled.')
slOTNConfigInbandGCC = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 1, 1, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNConfigInbandGCC.setStatus('current')
if mibBuilder.loadTexts: slOTNConfigInbandGCC.setDescription('GCC selection:\n\t\t 0 - GCC0\n\t\t 1 - GCC1')
slOTNCurrentPmTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1), )
if mibBuilder.loadTexts: slOTNCurrentPmTable.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmTable.setDescription('The OTN current table contains various OTN PM statistics.')
slOTNCurrentPmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1), ).setIndexNames((0, "SL-OTN-MIB", "slOTNCurrentPmIndex"))
if mibBuilder.loadTexts: slOTNCurrentPmEntry.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmEntry.setDescription('An entry in the OTN Current table.')
slOTNCurrentPmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNCurrentPmIndex.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmIndex.setDescription('The ifIndex of the XFP.')
slOTNCurrentPmFecCe = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNCurrentPmFecCe.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmFecCe.setDescription('FEC Corrected Errors. Increment for each FEC corrected error.')
slOTNCurrentPmFecCerMant = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNCurrentPmFecCerMant.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmFecCerMant.setDescription('FEC Corrected Error Ratio - The mantissa value.')
slOTNCurrentPmFecCerExp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNCurrentPmFecCerExp.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmFecCerExp.setDescription('FEC Corrected Error Ratio - The exponent value.')
slOTNCurrentPmFecCerValid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNCurrentPmFecCerValid.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmFecCerValid.setDescription('FEC Corrected Error Ratio - Validity flag.')
slOTNCurrentPmFecCerMantFE = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNCurrentPmFecCerMantFE.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmFecCerMantFE.setDescription('Far End FEC Corrected Error Ratio - The mantissa value.')
slOTNCurrentPmFecCerExpFE = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNCurrentPmFecCerExpFE.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmFecCerExpFE.setDescription('Far End FEC Corrected Error Ratio - The exponent value.')
slOTNCurrentPmFecCerValidFE = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 8), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slOTNCurrentPmFecCerValidFE.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmFecCerValidFE.setDescription('Far End FEC Corrected Error Ratio - Validity flag.')
slOTNCurrentPmReset = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 15, 2, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slOTNCurrentPmReset.setStatus('current')
if mibBuilder.loadTexts: slOTNCurrentPmReset.setDescription('Writing this object reset the FEC PM.')
mibBuilder.exportSymbols("SL-OTN-MIB", slOTNConfigODUkSAPIToExpect=slOTNConfigODUkSAPIToExpect, slOTNTraps=slOTNTraps, slOTNConfigOTUkDAPIToExpect=slOTNConfigOTUkDAPIToExpect, OTNTrafficRate=OTNTrafficRate, slOTNConfigOTUkTIMKillEnabled=slOTNConfigOTUkTIMKillEnabled, slOTNCurrentPmFecCerValid=slOTNCurrentPmFecCerValid, slOTNConfigODUkDAPIReceived=slOTNConfigODUkDAPIReceived, slOTNConfigFECEnabled=slOTNConfigFECEnabled, slOTNConfig=slOTNConfig, slOTNCurrentPmIndex=slOTNCurrentPmIndex, PYSNMP_MODULE_ID=slOTN, slOTNPm=slOTNPm, slOTNConfigOTUkSAPIToTransmit=slOTNConfigOTUkSAPIToTransmit, slOTNConfigInbandGCC=slOTNConfigInbandGCC, slOTNCurrentPmFecCerValidFE=slOTNCurrentPmFecCerValidFE, slOTNConfigODUkSAPIToTransmit=slOTNConfigODUkSAPIToTransmit, slOTNConfigOTUkTIMDetEnabled=slOTNConfigOTUkTIMDetEnabled, slOTNConfigOTUkDAPIToTransmit=slOTNConfigOTUkDAPIToTransmit, slOTN=slOTN, slOTNConfigODUkTIMKillEnabled=slOTNConfigODUkTIMKillEnabled, slOTNConfigOTUkDAPIReceived=slOTNConfigOTUkDAPIReceived, slOTNConfigEntry=slOTNConfigEntry, slOTNConfigODUkTIMDetEnabled=slOTNConfigODUkTIMDetEnabled, OTNOperationMode=OTNOperationMode, slOTNConfigStuffingEnabled=slOTNConfigStuffingEnabled, slOTNConfigODUkDAPIToTransmit=slOTNConfigODUkDAPIToTransmit, slOTNCurrentPmEntry=slOTNCurrentPmEntry, slOTNConfigLineIndex=slOTNConfigLineIndex, slOTNCurrentPmFecCerExpFE=slOTNCurrentPmFecCerExpFE, slOTNConfigOperationMode=slOTNConfigOperationMode, slOTNCurrentPmFecCerMantFE=slOTNCurrentPmFecCerMantFE, slOTNCurrentPmFecCerMant=slOTNCurrentPmFecCerMant, slOTNConfigOTUkSAPIToExpect=slOTNConfigOTUkSAPIToExpect, slOTNConfigODUkDAPIToExpect=slOTNConfigODUkDAPIToExpect, slOTNCurrentPmTable=slOTNCurrentPmTable, slOTNCurrentPmFecCerExp=slOTNCurrentPmFecCerExp, slOTNConfigOTUkSAPIReceived=slOTNConfigOTUkSAPIReceived, OTNTraceMessage=OTNTraceMessage, slOTNCurrentPmFecCe=slOTNCurrentPmFecCe, slOTNConfigTable=slOTNConfigTable, slOTNCurrentPmReset=slOTNCurrentPmReset, slOTNConfigODUkSAPIReceived=slOTNConfigODUkSAPIReceived)
