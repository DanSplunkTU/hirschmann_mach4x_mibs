#
# PySNMP MIB module SNMP-USER-BASED-SM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMP-USER-BASED-SM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpEngineID, snmpPrivProtocols, snmpAuthProtocols, SnmpAdminString = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpEngineID", "snmpPrivProtocols", "snmpAuthProtocols", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
NotificationType, Gauge32, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, snmpModules, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "snmpModules", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
AutonomousType, TextualConvention, DisplayString, RowStatus, TestAndIncr, RowPointer, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TextualConvention", "DisplayString", "RowStatus", "TestAndIncr", "RowPointer", "StorageType")
snmpUsmMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 15))
snmpUsmMIB.setRevisions(('1999-01-20 00:00', '1997-11-20 00:00',))
if mibBuilder.loadTexts: snmpUsmMIB.setLastUpdated('9901200000Z')
if mibBuilder.loadTexts: snmpUsmMIB.setOrganization('SNMPv3 Working Group')
usmMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1))
usmMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2))
usmNoAuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 1))
if mibBuilder.loadTexts: usmNoAuthProtocol.setStatus('current')
usmHMACMD5AuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 2))
if mibBuilder.loadTexts: usmHMACMD5AuthProtocol.setStatus('current')
usmHMACSHAAuthProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 1, 3))
if mibBuilder.loadTexts: usmHMACSHAAuthProtocol.setStatus('current')
usmNoPrivProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 1))
if mibBuilder.loadTexts: usmNoPrivProtocol.setStatus('current')
usmDESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 2))
if mibBuilder.loadTexts: usmDESPrivProtocol.setStatus('current')
usmAESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 6, 3, 10, 1, 2, 4))
if mibBuilder.loadTexts: usmAESPrivProtocol.setStatus('current')
class KeyChange(TextualConvention, OctetString):
    status = 'current'

usmStats = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1, 1))
usmStatsUnsupportedSecLevels = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsUnsupportedSecLevels.setStatus('current')
usmStatsNotInTimeWindows = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsNotInTimeWindows.setStatus('current')
usmStatsUnknownUserNames = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsUnknownUserNames.setStatus('current')
usmStatsUnknownEngineIDs = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsUnknownEngineIDs.setStatus('current')
usmStatsWrongDigests = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsWrongDigests.setStatus('current')
usmStatsDecryptionErrors = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmStatsDecryptionErrors.setStatus('current')
usmUser = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 1, 2))
usmUserSpinLock = MibScalar((1, 3, 6, 1, 6, 3, 15, 1, 2, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: usmUserSpinLock.setStatus('current')
usmUserTable = MibTable((1, 3, 6, 1, 6, 3, 15, 1, 2, 2), )
if mibBuilder.loadTexts: usmUserTable.setStatus('current')
usmUserEntry = MibTableRow((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1), ).setIndexNames((0, "SNMP-USER-BASED-SM-MIB", "usmUserEngineID"), (0, "SNMP-USER-BASED-SM-MIB", "usmUserName"))
if mibBuilder.loadTexts: usmUserEntry.setStatus('current')
usmUserEngineID = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 1), SnmpEngineID())
if mibBuilder.loadTexts: usmUserEngineID.setStatus('current')
usmUserName = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: usmUserName.setStatus('current')
usmUserSecurityName = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: usmUserSecurityName.setStatus('current')
usmUserCloneFrom = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 4), RowPointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserCloneFrom.setStatus('current')
usmUserAuthProtocol = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 5), AutonomousType().clone((1, 3, 6, 1, 6, 3, 10, 1, 1, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserAuthProtocol.setStatus('current')
usmUserAuthKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 6), KeyChange().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserAuthKeyChange.setStatus('current')
usmUserOwnAuthKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 7), KeyChange().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserOwnAuthKeyChange.setStatus('current')
usmUserPrivProtocol = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 8), AutonomousType().clone((1, 3, 6, 1, 6, 3, 10, 1, 2, 1))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserPrivProtocol.setStatus('current')
usmUserPrivKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 9), KeyChange().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserPrivKeyChange.setStatus('current')
usmUserOwnPrivKeyChange = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 10), KeyChange().clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserOwnPrivKeyChange.setStatus('current')
usmUserPublic = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 11), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserPublic.setStatus('current')
usmUserStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 12), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserStorageType.setStatus('current')
usmUserStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 15, 1, 2, 2, 1, 13), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: usmUserStatus.setStatus('current')
usmMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2, 1))
usmMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 15, 2, 2))
usmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 15, 2, 1, 1)).setObjects(("SNMP-USER-BASED-SM-MIB", "usmMIBBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmMIBCompliance = usmMIBCompliance.setStatus('current')
usmMIBBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 15, 2, 2, 1)).setObjects(("SNMP-USER-BASED-SM-MIB", "usmStatsUnsupportedSecLevels"), ("SNMP-USER-BASED-SM-MIB", "usmStatsNotInTimeWindows"), ("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownUserNames"), ("SNMP-USER-BASED-SM-MIB", "usmStatsUnknownEngineIDs"), ("SNMP-USER-BASED-SM-MIB", "usmStatsWrongDigests"), ("SNMP-USER-BASED-SM-MIB", "usmStatsDecryptionErrors"), ("SNMP-USER-BASED-SM-MIB", "usmUserSpinLock"), ("SNMP-USER-BASED-SM-MIB", "usmUserSecurityName"), ("SNMP-USER-BASED-SM-MIB", "usmUserCloneFrom"), ("SNMP-USER-BASED-SM-MIB", "usmUserAuthProtocol"), ("SNMP-USER-BASED-SM-MIB", "usmUserAuthKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserOwnAuthKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserPrivProtocol"), ("SNMP-USER-BASED-SM-MIB", "usmUserPrivKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserOwnPrivKeyChange"), ("SNMP-USER-BASED-SM-MIB", "usmUserPublic"), ("SNMP-USER-BASED-SM-MIB", "usmUserStorageType"), ("SNMP-USER-BASED-SM-MIB", "usmUserStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    usmMIBBasicGroup = usmMIBBasicGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", usmNoPrivProtocol=usmNoPrivProtocol, usmUserOwnAuthKeyChange=usmUserOwnAuthKeyChange, usmStatsWrongDigests=usmStatsWrongDigests, usmUserSpinLock=usmUserSpinLock, usmUserCloneFrom=usmUserCloneFrom, usmHMACMD5AuthProtocol=usmHMACMD5AuthProtocol, usmUserAuthProtocol=usmUserAuthProtocol, usmStatsUnknownEngineIDs=usmStatsUnknownEngineIDs, usmUserAuthKeyChange=usmUserAuthKeyChange, usmUserPrivKeyChange=usmUserPrivKeyChange, usmStatsUnsupportedSecLevels=usmStatsUnsupportedSecLevels, usmStatsDecryptionErrors=usmStatsDecryptionErrors, usmMIBCompliance=usmMIBCompliance, usmMIBConformance=usmMIBConformance, usmUserStorageType=usmUserStorageType, usmStatsNotInTimeWindows=usmStatsNotInTimeWindows, usmUserEngineID=usmUserEngineID, usmStatsUnknownUserNames=usmStatsUnknownUserNames, usmUserName=usmUserName, KeyChange=KeyChange, usmMIBBasicGroup=usmMIBBasicGroup, usmUserPublic=usmUserPublic, snmpUsmMIB=snmpUsmMIB, usmHMACSHAAuthProtocol=usmHMACSHAAuthProtocol, usmUserPrivProtocol=usmUserPrivProtocol, usmMIBObjects=usmMIBObjects, usmNoAuthProtocol=usmNoAuthProtocol, usmMIBGroups=usmMIBGroups, usmUserEntry=usmUserEntry, usmDESPrivProtocol=usmDESPrivProtocol, usmUserSecurityName=usmUserSecurityName, usmUserOwnPrivKeyChange=usmUserOwnPrivKeyChange, usmUser=usmUser, usmUserStatus=usmUserStatus, usmStats=usmStats, PYSNMP_MODULE_ID=snmpUsmMIB, usmAESPrivProtocol=usmAESPrivProtocol, usmUserTable=usmUserTable, usmMIBCompliances=usmMIBCompliances)
