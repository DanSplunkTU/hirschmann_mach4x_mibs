#
# PySNMP MIB module PTOPO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/PTOPO-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
PhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "PhysicalIndex")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
TimeFilter, = mibBuilder.importSymbols("RMON2-MIB", "TimeFilter")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, mib_2, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "mib-2", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
RowStatus, TimeStamp, TruthValue, DisplayString, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TimeStamp", "TruthValue", "DisplayString", "TextualConvention", "AutonomousType")
ptopoMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 79))
ptopoMIB.setRevisions(('2000-09-21 00:00',))
if mibBuilder.loadTexts: ptopoMIB.setLastUpdated('200009210000Z')
if mibBuilder.loadTexts: ptopoMIB.setOrganization('IETF; PTOPOMIB Working Group')
ptopoMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 1))
ptopoData = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 1, 1))
ptopoGeneral = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 1, 2))
ptopoConfig = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 1, 3))
class PtopoGenAddr(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class PtopoChassisIdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("chasIdEntPhysicalAlias", 1), ("chasIdIfAlias", 2), ("chasIdPortEntPhysicalAlias", 3), ("chasIdMacAddress", 4), ("chasIdPtopoGenAddr", 5))

class PtopoChassisId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class PtopoPortIdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("portIdIfAlias", 1), ("portIdEntPhysicalAlias", 2), ("portIdMacAddr", 3), ("portIdPtopoGenAddr", 4))

class PtopoPortId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class PtopoAddrSeenState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("notUsed", 1), ("unknown", 2), ("oneAddr", 3), ("multiAddr", 4))

ptopoConnTable = MibTable((1, 3, 6, 1, 2, 1, 79, 1, 1, 1), )
if mibBuilder.loadTexts: ptopoConnTable.setStatus('current')
ptopoConnEntry = MibTableRow((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1), ).setIndexNames((0, "PTOPO-MIB", "ptopoConnTimeMark"), (0, "PTOPO-MIB", "ptopoConnLocalChassis"), (0, "PTOPO-MIB", "ptopoConnLocalPort"), (0, "PTOPO-MIB", "ptopoConnIndex"))
if mibBuilder.loadTexts: ptopoConnEntry.setStatus('current')
ptopoConnTimeMark = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 1), TimeFilter())
if mibBuilder.loadTexts: ptopoConnTimeMark.setStatus('current')
ptopoConnLocalChassis = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 2), PhysicalIndex())
if mibBuilder.loadTexts: ptopoConnLocalChassis.setStatus('current')
ptopoConnLocalPort = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 3), PhysicalIndex())
if mibBuilder.loadTexts: ptopoConnLocalPort.setStatus('current')
ptopoConnIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: ptopoConnIndex.setStatus('current')
ptopoConnRemoteChassisType = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 5), PtopoChassisIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnRemoteChassisType.setStatus('current')
ptopoConnRemoteChassis = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 6), PtopoChassisId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnRemoteChassis.setStatus('current')
ptopoConnRemotePortType = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 7), PtopoPortIdType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnRemotePortType.setStatus('current')
ptopoConnRemotePort = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 8), PtopoPortId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnRemotePort.setStatus('current')
ptopoConnDiscAlgorithm = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 9), AutonomousType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnDiscAlgorithm.setStatus('current')
ptopoConnAgentNetAddrType = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 10), AddressFamilyNumbers()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnAgentNetAddrType.setStatus('current')
ptopoConnAgentNetAddr = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 11), PtopoGenAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnAgentNetAddr.setStatus('current')
ptopoConnMultiMacSASeen = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 12), PtopoAddrSeenState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnMultiMacSASeen.setStatus('current')
ptopoConnMultiNetSASeen = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 13), PtopoAddrSeenState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnMultiNetSASeen.setStatus('current')
ptopoConnIsStatic = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 14), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnIsStatic.setStatus('current')
ptopoConnLastVerifyTime = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 15), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnLastVerifyTime.setStatus('current')
ptopoConnRowStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 79, 1, 1, 1, 1, 16), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ptopoConnRowStatus.setStatus('current')
ptopoLastChangeTime = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoLastChangeTime.setStatus('current')
ptopoConnTabInserts = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 2, 2), Counter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnTabInserts.setStatus('current')
ptopoConnTabDeletes = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 2, 3), Counter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnTabDeletes.setStatus('current')
ptopoConnTabDrops = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 2, 4), Counter32()).setUnits('table entries').setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnTabDrops.setStatus('current')
ptopoConnTabAgeouts = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 2, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptopoConnTabAgeouts.setStatus('current')
ptopoConfigTrapInterval = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(5, 3600), ))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptopoConfigTrapInterval.setStatus('current')
ptopoConfigMaxHoldTime = MibScalar((1, 3, 6, 1, 2, 1, 79, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: ptopoConfigMaxHoldTime.setStatus('current')
ptopoMIBNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 2))
ptopoMIBTrapPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 2, 0))
ptopoConfigChange = NotificationType((1, 3, 6, 1, 2, 1, 79, 2, 0, 1)).setObjects(("PTOPO-MIB", "ptopoConnTabInserts"), ("PTOPO-MIB", "ptopoConnTabDeletes"), ("PTOPO-MIB", "ptopoConnTabDrops"), ("PTOPO-MIB", "ptopoConnTabAgeouts"))
if mibBuilder.loadTexts: ptopoConfigChange.setStatus('current')
ptopoRegistrationPoints = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 3))
ptopoDiscoveryMechanisms = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 3, 1))
ptopoDiscoveryLocal = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 3, 1, 1))
ptopoConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 4))
ptopoCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 4, 1))
ptopoGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 79, 4, 2))
ptopoCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 79, 4, 1, 1)).setObjects(("PTOPO-MIB", "ptopoDataGroup"), ("PTOPO-MIB", "ptopoGeneralGroup"), ("PTOPO-MIB", "ptopoConfigGroup"), ("PTOPO-MIB", "ptopoNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptopoCompliance = ptopoCompliance.setStatus('current')
ptopoDataGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 79, 4, 2, 1)).setObjects(("PTOPO-MIB", "ptopoConnRemoteChassisType"), ("PTOPO-MIB", "ptopoConnRemoteChassis"), ("PTOPO-MIB", "ptopoConnRemotePortType"), ("PTOPO-MIB", "ptopoConnRemotePort"), ("PTOPO-MIB", "ptopoConnDiscAlgorithm"), ("PTOPO-MIB", "ptopoConnAgentNetAddrType"), ("PTOPO-MIB", "ptopoConnAgentNetAddr"), ("PTOPO-MIB", "ptopoConnMultiMacSASeen"), ("PTOPO-MIB", "ptopoConnMultiNetSASeen"), ("PTOPO-MIB", "ptopoConnIsStatic"), ("PTOPO-MIB", "ptopoConnLastVerifyTime"), ("PTOPO-MIB", "ptopoConnRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptopoDataGroup = ptopoDataGroup.setStatus('current')
ptopoGeneralGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 79, 4, 2, 2)).setObjects(("PTOPO-MIB", "ptopoLastChangeTime"), ("PTOPO-MIB", "ptopoConnTabInserts"), ("PTOPO-MIB", "ptopoConnTabDeletes"), ("PTOPO-MIB", "ptopoConnTabDrops"), ("PTOPO-MIB", "ptopoConnTabAgeouts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptopoGeneralGroup = ptopoGeneralGroup.setStatus('current')
ptopoConfigGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 79, 4, 2, 3)).setObjects(("PTOPO-MIB", "ptopoConfigTrapInterval"), ("PTOPO-MIB", "ptopoConfigMaxHoldTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptopoConfigGroup = ptopoConfigGroup.setStatus('current')
ptopoNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 79, 4, 2, 4)).setObjects(("PTOPO-MIB", "ptopoConfigChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptopoNotificationsGroup = ptopoNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("PTOPO-MIB", ptopoData=ptopoData, ptopoDiscoveryMechanisms=ptopoDiscoveryMechanisms, ptopoConnTabAgeouts=ptopoConnTabAgeouts, ptopoConnTable=ptopoConnTable, ptopoConfigChange=ptopoConfigChange, ptopoConnLocalChassis=ptopoConnLocalChassis, ptopoMIBObjects=ptopoMIBObjects, PtopoChassisIdType=PtopoChassisIdType, ptopoConnIsStatic=ptopoConnIsStatic, ptopoGeneral=ptopoGeneral, ptopoConnRemoteChassis=ptopoConnRemoteChassis, PtopoAddrSeenState=PtopoAddrSeenState, ptopoConnMultiMacSASeen=ptopoConnMultiMacSASeen, ptopoConnTabDeletes=ptopoConnTabDeletes, ptopoRegistrationPoints=ptopoRegistrationPoints, ptopoConnEntry=ptopoConnEntry, ptopoConfig=ptopoConfig, ptopoCompliances=ptopoCompliances, ptopoMIB=ptopoMIB, ptopoConnAgentNetAddrType=ptopoConnAgentNetAddrType, ptopoDiscoveryLocal=ptopoDiscoveryLocal, ptopoConformance=ptopoConformance, ptopoMIBNotifications=ptopoMIBNotifications, PtopoGenAddr=PtopoGenAddr, ptopoConnTimeMark=ptopoConnTimeMark, PtopoPortIdType=PtopoPortIdType, ptopoConnRemoteChassisType=ptopoConnRemoteChassisType, ptopoConnRemotePortType=ptopoConnRemotePortType, ptopoConfigTrapInterval=ptopoConfigTrapInterval, ptopoConnAgentNetAddr=ptopoConnAgentNetAddr, ptopoConnTabInserts=ptopoConnTabInserts, ptopoConfigMaxHoldTime=ptopoConfigMaxHoldTime, ptopoLastChangeTime=ptopoLastChangeTime, ptopoMIBTrapPrefix=ptopoMIBTrapPrefix, PYSNMP_MODULE_ID=ptopoMIB, ptopoConnMultiNetSASeen=ptopoConnMultiNetSASeen, ptopoConnRowStatus=ptopoConnRowStatus, ptopoConnTabDrops=ptopoConnTabDrops, ptopoConnIndex=ptopoConnIndex, ptopoDataGroup=ptopoDataGroup, ptopoGeneralGroup=ptopoGeneralGroup, ptopoConnLastVerifyTime=ptopoConnLastVerifyTime, ptopoConnLocalPort=ptopoConnLocalPort, PtopoChassisId=PtopoChassisId, ptopoGroups=ptopoGroups, ptopoNotificationsGroup=ptopoNotificationsGroup, ptopoConnDiscAlgorithm=ptopoConnDiscAlgorithm, ptopoCompliance=ptopoCompliance, ptopoConfigGroup=ptopoConfigGroup, ptopoConnRemotePort=ptopoConnRemotePort, PtopoPortId=PtopoPortId)
