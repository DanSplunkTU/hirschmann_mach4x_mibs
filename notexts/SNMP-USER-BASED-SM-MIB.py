#
# PySNMP MIB module SNMP-USER-BASED-SM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/SNMP-USER-BASED-SM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:22 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
SnmpAdminString, snmpPrivProtocols, SnmpEngineID, snmpAuthProtocols = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "snmpPrivProtocols", "SnmpEngineID", "snmpAuthProtocols")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Integer32, Counter32, ObjectIdentity, TimeTicks, Gauge32, ModuleIdentity, Counter64, IpAddress, MibIdentifier, Unsigned32, snmpModules, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Integer32", "Counter32", "ObjectIdentity", "TimeTicks", "Gauge32", "ModuleIdentity", "Counter64", "IpAddress", "MibIdentifier", "Unsigned32", "snmpModules", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
AutonomousType, TestAndIncr, RowStatus, TextualConvention, RowPointer, DisplayString, StorageType = mibBuilder.importSymbols("SNMPv2-TC", "AutonomousType", "TestAndIncr", "RowStatus", "TextualConvention", "RowPointer", "DisplayString", "StorageType")
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
mibBuilder.exportSymbols("SNMP-USER-BASED-SM-MIB", usmUserStatus=usmUserStatus, usmMIBConformance=usmMIBConformance, usmStatsWrongDigests=usmStatsWrongDigests, usmMIBCompliances=usmMIBCompliances, usmUserStorageType=usmUserStorageType, usmDESPrivProtocol=usmDESPrivProtocol, KeyChange=KeyChange, usmUserTable=usmUserTable, usmUserSpinLock=usmUserSpinLock, usmNoPrivProtocol=usmNoPrivProtocol, usmUserPrivKeyChange=usmUserPrivKeyChange, usmStatsUnknownEngineIDs=usmStatsUnknownEngineIDs, usmStatsUnknownUserNames=usmStatsUnknownUserNames, usmMIBGroups=usmMIBGroups, usmMIBBasicGroup=usmMIBBasicGroup, usmMIBCompliance=usmMIBCompliance, usmStatsDecryptionErrors=usmStatsDecryptionErrors, usmUserOwnAuthKeyChange=usmUserOwnAuthKeyChange, usmUserName=usmUserName, PYSNMP_MODULE_ID=snmpUsmMIB, usmAESPrivProtocol=usmAESPrivProtocol, usmNoAuthProtocol=usmNoAuthProtocol, usmUserEntry=usmUserEntry, usmStatsUnsupportedSecLevels=usmStatsUnsupportedSecLevels, usmUserAuthProtocol=usmUserAuthProtocol, usmUserCloneFrom=usmUserCloneFrom, usmHMACMD5AuthProtocol=usmHMACMD5AuthProtocol, usmStats=usmStats, usmUserPrivProtocol=usmUserPrivProtocol, snmpUsmMIB=snmpUsmMIB, usmStatsNotInTimeWindows=usmStatsNotInTimeWindows, usmUserSecurityName=usmUserSecurityName, usmUserAuthKeyChange=usmUserAuthKeyChange, usmUserPublic=usmUserPublic, usmHMACSHAAuthProtocol=usmHMACSHAAuthProtocol, usmUser=usmUser, usmMIBObjects=usmMIBObjects, usmUserOwnPrivKeyChange=usmUserOwnPrivKeyChange, usmUserEngineID=usmUserEngineID)
