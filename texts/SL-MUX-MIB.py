#
# PySNMP MIB module SL-MUX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-MUX-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:15:40 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
CleiCode, = mibBuilder.importSymbols("SL-ENTITY-MIB", "CleiCode")
sitelight, = mibBuilder.importSymbols("SL-NE-MIB", "sitelight")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, ModuleIdentity, IpAddress, Integer32, ObjectIdentity, Unsigned32, Gauge32, MibIdentifier, Bits, NotificationType, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "ModuleIdentity", "IpAddress", "Integer32", "ObjectIdentity", "Unsigned32", "Gauge32", "MibIdentifier", "Bits", "NotificationType", "Counter64", "Counter32")
TextualConvention, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString")
slMux = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 5))
if mibBuilder.loadTexts: slMux.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slMux.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slMux.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slMux.setDescription('This MIB module describes the Mux interfaces')
muxIfTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1), )
if mibBuilder.loadTexts: muxIfTable.setStatus('current')
if mibBuilder.loadTexts: muxIfTable.setDescription('The Mux interface entity table.')
muxIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1), ).setIndexNames((0, "SL-MUX-MIB", "muxIfIndex"))
if mibBuilder.loadTexts: muxIfEntry.setStatus('current')
if mibBuilder.loadTexts: muxIfEntry.setDescription('An entry in the MUX interface table.')
muxIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfIndex.setStatus('current')
if mibBuilder.loadTexts: muxIfIndex.setDescription('The interface index of the Mux (type=196).')
muxIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfType.setStatus('current')
if mibBuilder.loadTexts: muxIfType.setDescription('The number of wave lengths supported by the mux.')
muxIfWaveSpacing = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("ghzNone", 0), ("ghz400", 1), ("ghz200", 2), ("ghz100", 3), ("ghz50", 4), ("ghz2500", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfWaveSpacing.setStatus('current')
if mibBuilder.loadTexts: muxIfWaveSpacing.setDescription('The spacing between two adjacent optical channels in GHz units.')
muxIfWaveLengthNm = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfWaveLengthNm.setStatus('current')
if mibBuilder.loadTexts: muxIfWaveLengthNm.setDescription('The WDM base wave length.\n\t\tFor DWDM values are ituGrid[10] = 1569.59 to ituGrid[69] = 1522.56\n\t\tFor CWDM  values are ituGrid[70] = 1470 to ituGrid[77] = 1610\n\t\tand ituGrid[80] = 1270 to ituGrid[89] = 1450.')
muxIfOscWaveLengthNm = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 5, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: muxIfOscWaveLengthNm.setStatus('current')
if mibBuilder.loadTexts: muxIfOscWaveLengthNm.setDescription('The OSC WDM wave length.\n\t\tFor DWDM values are ituGrid[71] = 1490 or ituGrid[72] = 1510\n\t\tFor CWDM values are ituGrid[81] = 1290 or ituGrid[82] = 1310.')
mibBuilder.exportSymbols("SL-MUX-MIB", PYSNMP_MODULE_ID=slMux, muxIfType=muxIfType, muxIfWaveLengthNm=muxIfWaveLengthNm, muxIfWaveSpacing=muxIfWaveSpacing, muxIfIndex=muxIfIndex, muxIfEntry=muxIfEntry, muxIfTable=muxIfTable, slMux=slMux, muxIfOscWaveLengthNm=muxIfOscWaveLengthNm)
