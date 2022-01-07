#
# PySNMP MIB module ETHER-WIS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/ETHER-WIS
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, transmission, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "transmission", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sonetLineStuff2, sonetMediumStuff2, sonetMediumCircuitIdentifier, sonetMediumType, sonetPathStuff2, sonetFarEndPathStuff2, sonetMediumLineCoding, sonetFarEndLineStuff2, sonetMediumLoopbackConfig, sonetMediumLineType, sonetSectionStuff2, sonetSESthresholdSet, sonetPathCurrentWidth = mibBuilder.importSymbols("SONET-MIB", "sonetLineStuff2", "sonetMediumStuff2", "sonetMediumCircuitIdentifier", "sonetMediumType", "sonetPathStuff2", "sonetFarEndPathStuff2", "sonetMediumLineCoding", "sonetFarEndLineStuff2", "sonetMediumLoopbackConfig", "sonetMediumLineType", "sonetSectionStuff2", "sonetSESthresholdSet", "sonetPathCurrentWidth")
etherWisMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 134))
etherWisMIB.setRevisions(('2003-09-19 00:00',))
if mibBuilder.loadTexts: etherWisMIB.setLastUpdated('200309190000Z')
if mibBuilder.loadTexts: etherWisMIB.setOrganization('IETF Ethernet Interfaces and Hub MIB Working Group')
etherWisObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 134, 1))
etherWisObjectsPath = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 134, 2))
etherWisConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 134, 3))
etherWisDevice = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 134, 1, 1))
etherWisSection = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 134, 1, 2))
etherWisPath = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 134, 2, 1))
etherWisFarEndPath = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 134, 2, 2))
etherWisDeviceTable = MibTable((1, 3, 6, 1, 2, 1, 10, 134, 1, 1, 1), )
if mibBuilder.loadTexts: etherWisDeviceTable.setStatus('current')
etherWisDeviceEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 134, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etherWisDeviceEntry.setStatus('current')
etherWisDeviceTxTestPatternMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 134, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("squareWave", 2), ("prbs31", 3), ("mixedFrequency", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etherWisDeviceTxTestPatternMode.setStatus('current')
etherWisDeviceRxTestPatternMode = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 134, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 3, 4))).clone(namedValues=NamedValues(("none", 1), ("prbs31", 3), ("mixedFrequency", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etherWisDeviceRxTestPatternMode.setStatus('current')
etherWisDeviceRxTestPatternErrors = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 134, 1, 1, 1, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etherWisDeviceRxTestPatternErrors.setStatus('current')
etherWisSectionCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 134, 1, 2, 1), )
if mibBuilder.loadTexts: etherWisSectionCurrentTable.setStatus('current')
etherWisSectionCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 134, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etherWisSectionCurrentEntry.setStatus('current')
etherWisSectionCurrentJ0Transmitted = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 134, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etherWisSectionCurrentJ0Transmitted.setStatus('current')
etherWisSectionCurrentJ0Received = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 134, 1, 2, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherWisSectionCurrentJ0Received.setStatus('current')
etherWisPathCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 134, 2, 1, 1), )
if mibBuilder.loadTexts: etherWisPathCurrentTable.setStatus('current')
etherWisPathCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 134, 2, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etherWisPathCurrentEntry.setStatus('current')
etherWisPathCurrentStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 134, 2, 1, 1, 1, 1), Bits().clone(namedValues=NamedValues(("etherWisPathLOP", 0), ("etherWisPathAIS", 1), ("etherWisPathPLM", 2), ("etherWisPathLCD", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherWisPathCurrentStatus.setStatus('current')
etherWisPathCurrentJ1Transmitted = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 134, 2, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etherWisPathCurrentJ1Transmitted.setStatus('current')
etherWisPathCurrentJ1Received = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 134, 2, 1, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherWisPathCurrentJ1Received.setStatus('current')
etherWisFarEndPathCurrentTable = MibTable((1, 3, 6, 1, 2, 1, 10, 134, 2, 2, 1), )
if mibBuilder.loadTexts: etherWisFarEndPathCurrentTable.setStatus('current')
etherWisFarEndPathCurrentEntry = MibTableRow((1, 3, 6, 1, 2, 1, 10, 134, 2, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: etherWisFarEndPathCurrentEntry.setStatus('current')
etherWisFarEndPathCurrentStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 10, 134, 2, 2, 1, 1, 1), Bits().clone(namedValues=NamedValues(("etherWisFarEndPayloadDefect", 0), ("etherWisFarEndServerDefect", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: etherWisFarEndPathCurrentStatus.setStatus('current')
etherWisGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 134, 3, 1))
etherWisCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 10, 134, 3, 2))
etherWisDeviceGroupBasic = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 134, 3, 1, 1)).setObjects(("ETHER-WIS", "etherWisDeviceTxTestPatternMode"), ("ETHER-WIS", "etherWisDeviceRxTestPatternMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherWisDeviceGroupBasic = etherWisDeviceGroupBasic.setStatus('current')
etherWisDeviceGroupExtra = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 134, 3, 1, 2)).setObjects(("ETHER-WIS", "etherWisDeviceRxTestPatternErrors"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherWisDeviceGroupExtra = etherWisDeviceGroupExtra.setStatus('current')
etherWisSectionGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 134, 3, 1, 3)).setObjects(("ETHER-WIS", "etherWisSectionCurrentJ0Transmitted"), ("ETHER-WIS", "etherWisSectionCurrentJ0Received"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherWisSectionGroup = etherWisSectionGroup.setStatus('current')
etherWisPathGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 134, 3, 1, 4)).setObjects(("ETHER-WIS", "etherWisPathCurrentStatus"), ("ETHER-WIS", "etherWisPathCurrentJ1Transmitted"), ("ETHER-WIS", "etherWisPathCurrentJ1Received"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherWisPathGroup = etherWisPathGroup.setStatus('current')
etherWisFarEndPathGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 10, 134, 3, 1, 5)).setObjects(("ETHER-WIS", "etherWisFarEndPathCurrentStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherWisFarEndPathGroup = etherWisFarEndPathGroup.setStatus('current')
etherWisCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 10, 134, 3, 2, 1)).setObjects(("ETHER-WIS", "etherWisDeviceGroupBasic"), ("ETHER-WIS", "etherWisSectionGroup"), ("ETHER-WIS", "etherWisPathGroup"), ("ETHER-WIS", "etherWisFarEndPathGroup"), ("SONET-MIB", "sonetMediumStuff2"), ("SONET-MIB", "sonetSectionStuff2"), ("SONET-MIB", "sonetLineStuff2"), ("SONET-MIB", "sonetFarEndLineStuff2"), ("SONET-MIB", "sonetPathStuff2"), ("SONET-MIB", "sonetFarEndPathStuff2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etherWisCompliance = etherWisCompliance.setStatus('current')
mibBuilder.exportSymbols("ETHER-WIS", etherWisSection=etherWisSection, etherWisDeviceTable=etherWisDeviceTable, etherWisDeviceRxTestPatternMode=etherWisDeviceRxTestPatternMode, etherWisSectionCurrentEntry=etherWisSectionCurrentEntry, etherWisFarEndPathCurrentEntry=etherWisFarEndPathCurrentEntry, PYSNMP_MODULE_ID=etherWisMIB, etherWisFarEndPathCurrentStatus=etherWisFarEndPathCurrentStatus, etherWisDeviceRxTestPatternErrors=etherWisDeviceRxTestPatternErrors, etherWisConformance=etherWisConformance, etherWisDeviceEntry=etherWisDeviceEntry, etherWisDeviceTxTestPatternMode=etherWisDeviceTxTestPatternMode, etherWisSectionCurrentTable=etherWisSectionCurrentTable, etherWisFarEndPathGroup=etherWisFarEndPathGroup, etherWisPathCurrentJ1Received=etherWisPathCurrentJ1Received, etherWisMIB=etherWisMIB, etherWisPath=etherWisPath, etherWisObjectsPath=etherWisObjectsPath, etherWisCompliance=etherWisCompliance, etherWisFarEndPath=etherWisFarEndPath, etherWisDevice=etherWisDevice, etherWisPathCurrentJ1Transmitted=etherWisPathCurrentJ1Transmitted, etherWisPathGroup=etherWisPathGroup, etherWisPathCurrentTable=etherWisPathCurrentTable, etherWisSectionCurrentJ0Received=etherWisSectionCurrentJ0Received, etherWisDeviceGroupExtra=etherWisDeviceGroupExtra, etherWisSectionGroup=etherWisSectionGroup, etherWisSectionCurrentJ0Transmitted=etherWisSectionCurrentJ0Transmitted, etherWisObjects=etherWisObjects, etherWisGroups=etherWisGroups, etherWisDeviceGroupBasic=etherWisDeviceGroupBasic, etherWisCompliances=etherWisCompliances, etherWisPathCurrentEntry=etherWisPathCurrentEntry, etherWisFarEndPathCurrentTable=etherWisFarEndPathCurrentTable, etherWisPathCurrentStatus=etherWisPathCurrentStatus)
