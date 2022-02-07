#
# PySNMP MIB module SCTE-HMS-QAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/scte/SCTE-HMS-QAM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:31 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
QAMChannelModulationFormat, QAMChannelInterleaveMode = mibBuilder.importSymbols("SCTE-HMS-HEADENDIDENT-TC-MIB", "QAMChannelModulationFormat", "QAMChannelInterleaveMode")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
TimeTicks, iso, Counter64, ModuleIdentity, Gauge32, NotificationType, Unsigned32, MibIdentifier, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, enterprises, ObjectIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "iso", "Counter64", "ModuleIdentity", "Gauge32", "NotificationType", "Unsigned32", "MibIdentifier", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "enterprises", "ObjectIdentity", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
heDigitalQamMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1))
heDigitalQamMIB.setRevisions(('2008-07-16 03:05', '2008-04-18 10:55', '2008-02-04 18:50', '2007-12-17 11:50', '2007-10-03 17:00', '2007-10-02 12:00',))
if mibBuilder.loadTexts: heDigitalQamMIB.setLastUpdated('200807160305Z')
if mibBuilder.loadTexts: heDigitalQamMIB.setOrganization('SCTE HMS Working Group')
qamMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1))
if mibBuilder.loadTexts: qamMIBObjects.setStatus('current')
qamMIBConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2))
if mibBuilder.loadTexts: qamMIBConformance.setStatus('current')
qamMIBCompliances = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 1))
if mibBuilder.loadTexts: qamMIBCompliances.setStatus('current')
qamMIBGroups = ObjectIdentity((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2))
if mibBuilder.loadTexts: qamMIBGroups.setStatus('current')
qamChannelTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1), )
if mibBuilder.loadTexts: qamChannelTable.setStatus('current')
qamChannelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qamChannelEntry.setStatus('current')
qamChannelFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 1), Unsigned32()).setUnits('Hertz').setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelFrequency.setStatus('current')
qamChannelModulationFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 2), QAMChannelModulationFormat()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelModulationFormat.setStatus('current')
qamChannelInterleaverLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("level1", 1), ("level2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelInterleaverLevel.setStatus('current')
qamChannelInterleaverMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 4), QAMChannelInterleaveMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelInterleaverMode.setStatus('current')
qamChannelPower = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 5), Integer32()).setUnits('0.1 dBmV').setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelPower.setStatus('current')
qamChannelSquelch = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("unmuted", 1), ("muted", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelSquelch.setStatus('current')
qamChannelContWaveMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cwmOff", 1), ("cwmOn", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelContWaveMode.setStatus('current')
qamChannelAnnexMode = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("other", 2), ("annexA", 3), ("annexB", 4), ("annexC", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelAnnexMode.setStatus('current')
qamChannelCommonTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2), )
if mibBuilder.loadTexts: qamChannelCommonTable.setStatus('current')
qamChannelCommonEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: qamChannelCommonEntry.setStatus('current')
qamChannelCommonOutputBw = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2, 1, 1), Integer32()).setUnits('bps').setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelCommonOutputBw.setStatus('current')
qamChannelCommonUtilization = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 1000), ))).setUnits('0.1 Percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: qamChannelCommonUtilization.setStatus('current')
qamConfigTable = MibTable((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3), )
if mibBuilder.loadTexts: qamConfigTable.setStatus('current')
qamConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "SCTE-HMS-QAM-MIB", "qamConfigIndex"))
if mibBuilder.loadTexts: qamConfigEntry.setStatus('current')
qamConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 1), Unsigned32())
if mibBuilder.loadTexts: qamConfigIndex.setStatus('current')
qamConfigQamChannelIdMin = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 2), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigQamChannelIdMin.setStatus('current')
qamConfigQamChannelIdMax = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigQamChannelIdMax.setStatus('current')
qamConfigIPAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 4), InetAddressType().clone('ipv4')).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigIPAddrType.setStatus('current')
qamConfigIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigIPAddr.setStatus('current')
qamConfigUdpPortRangeMin = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigUdpPortRangeMin.setStatus('current')
qamConfigUdpPortRangeMax = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigUdpPortRangeMax.setStatus('current')
qamConfigOutputProgNoMin = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigOutputProgNoMin.setStatus('current')
qamConfigOutputProgNoMax = MibTableColumn((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)).clone(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: qamConfigOutputProgNoMax.setStatus('current')
qamSupport = ModuleCompliance((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 1, 1)).setObjects(("SCTE-HMS-QAM-MIB", "qamChannelGroup"), ("SCTE-HMS-QAM-MIB", "qamConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qamSupport = qamSupport.setStatus('current')
docsisSupport = ModuleCompliance((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 1, 2)).setObjects(("SCTE-HMS-QAM-MIB", "qamMpegDocsisCommonGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsisSupport = docsisSupport.setStatus('current')
qamMpegDocsisCommonGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2, 1)).setObjects(("SCTE-HMS-QAM-MIB", "qamChannelCommonOutputBw"), ("SCTE-HMS-QAM-MIB", "qamChannelCommonUtilization"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qamMpegDocsisCommonGroup = qamMpegDocsisCommonGroup.setStatus('current')
qamChannelGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2, 2)).setObjects(("SCTE-HMS-QAM-MIB", "qamChannelFrequency"), ("SCTE-HMS-QAM-MIB", "qamChannelModulationFormat"), ("SCTE-HMS-QAM-MIB", "qamChannelInterleaverLevel"), ("SCTE-HMS-QAM-MIB", "qamChannelInterleaverMode"), ("SCTE-HMS-QAM-MIB", "qamChannelPower"), ("SCTE-HMS-QAM-MIB", "qamChannelSquelch"), ("SCTE-HMS-QAM-MIB", "qamChannelContWaveMode"), ("SCTE-HMS-QAM-MIB", "qamChannelAnnexMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qamChannelGroup = qamChannelGroup.setStatus('current')
qamConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 3, 1, 2, 2, 3)).setObjects(("SCTE-HMS-QAM-MIB", "qamConfigQamChannelIdMin"), ("SCTE-HMS-QAM-MIB", "qamConfigQamChannelIdMax"), ("SCTE-HMS-QAM-MIB", "qamConfigIPAddrType"), ("SCTE-HMS-QAM-MIB", "qamConfigIPAddr"), ("SCTE-HMS-QAM-MIB", "qamConfigUdpPortRangeMin"), ("SCTE-HMS-QAM-MIB", "qamConfigUdpPortRangeMax"), ("SCTE-HMS-QAM-MIB", "qamConfigOutputProgNoMin"), ("SCTE-HMS-QAM-MIB", "qamConfigOutputProgNoMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    qamConfigGroup = qamConfigGroup.setStatus('current')
mibBuilder.exportSymbols("SCTE-HMS-QAM-MIB", qamChannelPower=qamChannelPower, qamMIBObjects=qamMIBObjects, qamChannelInterleaverLevel=qamChannelInterleaverLevel, heDigitalQamMIB=heDigitalQamMIB, qamSupport=qamSupport, qamConfigIndex=qamConfigIndex, qamConfigQamChannelIdMax=qamConfigQamChannelIdMax, qamChannelCommonTable=qamChannelCommonTable, docsisSupport=docsisSupport, qamChannelCommonOutputBw=qamChannelCommonOutputBw, qamChannelInterleaverMode=qamChannelInterleaverMode, qamChannelCommonEntry=qamChannelCommonEntry, qamConfigIPAddr=qamConfigIPAddr, qamConfigOutputProgNoMin=qamConfigOutputProgNoMin, qamChannelModulationFormat=qamChannelModulationFormat, qamMpegDocsisCommonGroup=qamMpegDocsisCommonGroup, qamMIBConformance=qamMIBConformance, qamChannelTable=qamChannelTable, qamConfigUdpPortRangeMin=qamConfigUdpPortRangeMin, qamConfigUdpPortRangeMax=qamConfigUdpPortRangeMax, qamConfigOutputProgNoMax=qamConfigOutputProgNoMax, qamConfigGroup=qamConfigGroup, qamChannelCommonUtilization=qamChannelCommonUtilization, qamConfigQamChannelIdMin=qamConfigQamChannelIdMin, PYSNMP_MODULE_ID=heDigitalQamMIB, qamConfigIPAddrType=qamConfigIPAddrType, qamChannelAnnexMode=qamChannelAnnexMode, qamChannelFrequency=qamChannelFrequency, qamConfigEntry=qamConfigEntry, qamChannelEntry=qamChannelEntry, qamConfigTable=qamConfigTable, qamChannelContWaveMode=qamChannelContWaveMode, qamMIBGroups=qamMIBGroups, qamChannelSquelch=qamChannelSquelch, qamChannelGroup=qamChannelGroup, qamMIBCompliances=qamMIBCompliances)
