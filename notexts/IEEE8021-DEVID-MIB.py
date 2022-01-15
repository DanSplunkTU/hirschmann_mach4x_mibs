#
# PySNMP MIB module IEEE8021-DEVID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-DEVID-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
entPhysicalIndex, PhysicalIndex = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex", "PhysicalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ieee8021DevIDMIB = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 17))
ieee8021DevIDMIB.setRevisions(('2018-07-15 19:04', '2009-06-25 00:00',))
if mibBuilder.loadTexts: ieee8021DevIDMIB.setLastUpdated('201807151904Z')
if mibBuilder.loadTexts: ieee8021DevIDMIB.setOrganization('IEEE 802.1 Working Group')
devIDMIBNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 17, 0))
devIDMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 17, 1))
devIDMIBConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 17, 2))
class DevIDFingerprint(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x:1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 49)

devIDGlobalMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 17, 1, 1))
devIDMgmtMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 17, 1, 2))
devIDStatsMIBObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 17, 1, 3))
devIDModuleTable = MibTable((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 6), )
if mibBuilder.loadTexts: devIDModuleTable.setStatus('current')
devIDModuleEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 6, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: devIDModuleEntry.setStatus('current')
devIDModuleSupportsLDevIDs = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 6, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDModuleSupportsLDevIDs.setStatus('current')
devIDModuleGeneratesLDevIDKeys = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 6, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDModuleGeneratesLDevIDKeys.setStatus('current')
devIDModuleInsertsLDevIDKeys = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 6, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDModuleInsertsLDevIDKeys.setStatus('current')
devIDCertTable = MibTable((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7), )
if mibBuilder.loadTexts: devIDCertTable.setStatus('current')
devIDCertEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "IEEE8021-DEVID-MIB", "devIDCertFingerprint"))
if mibBuilder.loadTexts: devIDCertEntry.setStatus('current')
devIDCertFingerprint = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 1), DevIDFingerprint())
if mibBuilder.loadTexts: devIDCertFingerprint.setStatus('current')
devIDCertPublicKeyInfoFprint = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 2), DevIDFingerprint()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCertPublicKeyInfoFprint.setStatus('current')
devIDCertIDevID = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCertIDevID.setStatus('current')
devIDCertKeyEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 4), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCertKeyEnabled.setStatus('current')
devIDCertEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCertEnabled.setStatus('current')
devIDCert = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 7, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCert.setStatus('current')
devIDChainTable = MibTable((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 8), )
if mibBuilder.loadTexts: devIDChainTable.setStatus('current')
devIDChainEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 8, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"), (0, "IEEE8021-DEVID-MIB", "devIDCertFingerprint"), (0, "IEEE8021-DEVID-MIB", "devIDChainCertIndex"))
if mibBuilder.loadTexts: devIDChainEntry.setStatus('current')
devIDChainCertIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 8, 1, 1), Unsigned32())
if mibBuilder.loadTexts: devIDChainCertIndex.setStatus('current')
devIDChainCertFingerprint = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 8, 1, 2), DevIDFingerprint()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDChainCertFingerprint.setStatus('current')
devIDChainCert = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 8, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDChainCert.setStatus('current')
devIDStatisticsTable = MibTable((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5), )
if mibBuilder.loadTexts: devIDStatisticsTable.setStatus('current')
devIDStatisticsEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: devIDStatisticsEntry.setStatus('current')
devIDStatisticKeyGenerationCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDStatisticKeyGenerationCount.setStatus('current')
devIDStatisticKeyInsertionCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDStatisticKeyInsertionCount.setStatus('current')
devIDStatisticKeyDeletionCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDStatisticKeyDeletionCount.setStatus('current')
devIDStatisticCSRGenerationCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDStatisticCSRGenerationCount.setStatus('deprecated')
devIDStatisticCredentialInsertionCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDStatisticCredentialInsertionCount.setStatus('obsolete')
devIDStatisticCredentialDeletionCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDStatisticCredentialDeletionCount.setStatus('obsolete')
devIDStatisticCertInsertionCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDStatisticCertInsertionCount.setStatus('current')
devIDStatisticCertDeletionCount = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 5, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDStatisticCertDeletionCount.setStatus('current')
devIDMIBCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 17, 2, 1))
devIDMIBGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 17, 2, 2))
devIDMIBModuleCompliance2 = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 17, 2, 1, 2)).setObjects(("IEEE8021-DEVID-MIB", "devIDMIBModuleGroup"), ("IEEE8021-DEVID-MIB", "devIDMIBCertificateGroup"), ("IEEE8021-DEVID-MIB", "devIDMIBAuditGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    devIDMIBModuleCompliance2 = devIDMIBModuleCompliance2.setStatus('current')
devIDMIBModuleGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 17, 2, 2, 2)).setObjects(("IEEE8021-DEVID-MIB", "devIDModuleSupportsLDevIDs"), ("IEEE8021-DEVID-MIB", "devIDModuleGeneratesLDevIDKeys"), ("IEEE8021-DEVID-MIB", "devIDModuleInsertsLDevIDKeys"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    devIDMIBModuleGroup = devIDMIBModuleGroup.setStatus('current')
devIDMIBCertificateGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 17, 2, 2, 3)).setObjects(("IEEE8021-DEVID-MIB", "devIDCertPublicKeyInfoFprint"), ("IEEE8021-DEVID-MIB", "devIDCertIDevID"), ("IEEE8021-DEVID-MIB", "devIDCertKeyEnabled"), ("IEEE8021-DEVID-MIB", "devIDCertEnabled"), ("IEEE8021-DEVID-MIB", "devIDCert"), ("IEEE8021-DEVID-MIB", "devIDChainCertFingerprint"), ("IEEE8021-DEVID-MIB", "devIDChainCert"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    devIDMIBCertificateGroup = devIDMIBCertificateGroup.setStatus('current')
devIDMIBAuditGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 17, 2, 2, 4)).setObjects(("IEEE8021-DEVID-MIB", "devIDStatisticKeyGenerationCount"), ("IEEE8021-DEVID-MIB", "devIDStatisticKeyInsertionCount"), ("IEEE8021-DEVID-MIB", "devIDStatisticKeyDeletionCount"), ("IEEE8021-DEVID-MIB", "devIDStatisticCertInsertionCount"), ("IEEE8021-DEVID-MIB", "devIDStatisticCertDeletionCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    devIDMIBAuditGroup = devIDMIBAuditGroup.setStatus('current')
class DevIDErrorStatus(TextualConvention, Integer32):
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("none", 1), ("internalError", 2))

class DevIDAlgorithmIdentifier(TextualConvention, Integer32):
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("rsaEncryption", 1), ("idecPublicKey", 2))

devIDPublicKeyCount = MibScalar((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDPublicKeyCount.setStatus('obsolete')
devIDPublicKeyTable = MibTable((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2), )
if mibBuilder.loadTexts: devIDPublicKeyTable.setStatus('obsolete')
devIDPublicKeyEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1), ).setIndexNames((0, "ENTITY-MIB", "entPhysicalIndex"))
if mibBuilder.loadTexts: devIDPublicKeyEntry.setStatus('obsolete')
devIDPublicKeyIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: devIDPublicKeyIndex.setStatus('obsolete')
devIDPublicKeyEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devIDPublicKeyEnabled.setStatus('obsolete')
devIDPublicKeyAlgorithm = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1, 3), DevIDAlgorithmIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDPublicKeyAlgorithm.setStatus('obsolete')
devIDPublicKeyPubkeySHA1Hash = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDPublicKeyPubkeySHA1Hash.setStatus('obsolete')
devIDPublicKeyErrStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 2, 1, 5), DevIDErrorStatus().clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDPublicKeyErrStatus.setStatus('obsolete')
devIDCredentialCount = MibScalar((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCredentialCount.setStatus('obsolete')
devIDCredentialTable = MibTable((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4), )
if mibBuilder.loadTexts: devIDCredentialTable.setStatus('obsolete')
devIDCredentialEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1), ).setIndexNames((0, "IEEE8021-DEVID-MIB", "devIDCredentialIndex"))
if mibBuilder.loadTexts: devIDCredentialEntry.setStatus('obsolete')
devIDCredentialIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: devIDCredentialIndex.setStatus('obsolete')
devIDCredentialEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: devIDCredentialEnabled.setStatus('obsolete')
devIDCredentialSHA1Hash = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 3), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCredentialSHA1Hash.setStatus('obsolete')
devIDCredentialSerialNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCredentialSerialNumber.setStatus('obsolete')
devIDCredentialIssuer = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCredentialIssuer.setStatus('obsolete')
devIDCredentialSubject = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCredentialSubject.setStatus('obsolete')
devIDCredentialSubjectAltName = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCredentialSubjectAltName.setStatus('obsolete')
devIDCredentialEntityIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 8), PhysicalIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCredentialEntityIndex.setStatus('obsolete')
devIDCredentialPubkeyIndex = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCredentialPubkeyIndex.setStatus('obsolete')
devIDCredentialErrStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 17, 1, 2, 4, 1, 10), DevIDErrorStatus().clone('none')).setMaxAccess("readonly")
if mibBuilder.loadTexts: devIDCredentialErrStatus.setStatus('obsolete')
devIDMIBModuleCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 17, 2, 1, 1)).setObjects(("IEEE8021-DEVID-MIB", "devIDMIBObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    devIDMIBModuleCompliance = devIDMIBModuleCompliance.setStatus('obsolete')
devIDMIBObjectGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 17, 2, 2, 1)).setObjects(("IEEE8021-DEVID-MIB", "devIDPublicKeyCount"), ("IEEE8021-DEVID-MIB", "devIDPublicKeyEnabled"), ("IEEE8021-DEVID-MIB", "devIDPublicKeyAlgorithm"), ("IEEE8021-DEVID-MIB", "devIDPublicKeyPubkeySHA1Hash"), ("IEEE8021-DEVID-MIB", "devIDPublicKeyErrStatus"), ("IEEE8021-DEVID-MIB", "devIDCredentialCount"), ("IEEE8021-DEVID-MIB", "devIDCredentialEnabled"), ("IEEE8021-DEVID-MIB", "devIDCredentialSHA1Hash"), ("IEEE8021-DEVID-MIB", "devIDCredentialSerialNumber"), ("IEEE8021-DEVID-MIB", "devIDCredentialIssuer"), ("IEEE8021-DEVID-MIB", "devIDCredentialSubject"), ("IEEE8021-DEVID-MIB", "devIDCredentialSubjectAltName"), ("IEEE8021-DEVID-MIB", "devIDCredentialEntityIndex"), ("IEEE8021-DEVID-MIB", "devIDCredentialPubkeyIndex"), ("IEEE8021-DEVID-MIB", "devIDCredentialErrStatus"), ("IEEE8021-DEVID-MIB", "devIDStatisticKeyGenerationCount"), ("IEEE8021-DEVID-MIB", "devIDStatisticKeyInsertionCount"), ("IEEE8021-DEVID-MIB", "devIDStatisticKeyDeletionCount"), ("IEEE8021-DEVID-MIB", "devIDStatisticCSRGenerationCount"), ("IEEE8021-DEVID-MIB", "devIDStatisticCredentialInsertionCount"), ("IEEE8021-DEVID-MIB", "devIDStatisticCredentialDeletionCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    devIDMIBObjectGroup = devIDMIBObjectGroup.setStatus('obsolete')
mibBuilder.exportSymbols("IEEE8021-DEVID-MIB", devIDGlobalMIBObjects=devIDGlobalMIBObjects, devIDModuleSupportsLDevIDs=devIDModuleSupportsLDevIDs, devIDCertPublicKeyInfoFprint=devIDCertPublicKeyInfoFprint, devIDPublicKeyPubkeySHA1Hash=devIDPublicKeyPubkeySHA1Hash, devIDStatisticsTable=devIDStatisticsTable, devIDCertEnabled=devIDCertEnabled, devIDMIBCertificateGroup=devIDMIBCertificateGroup, devIDStatisticsEntry=devIDStatisticsEntry, devIDCredentialTable=devIDCredentialTable, devIDMIBCompliances=devIDMIBCompliances, devIDCredentialEntry=devIDCredentialEntry, devIDPublicKeyAlgorithm=devIDPublicKeyAlgorithm, devIDMIBObjectGroup=devIDMIBObjectGroup, devIDCredentialSubjectAltName=devIDCredentialSubjectAltName, devIDPublicKeyEnabled=devIDPublicKeyEnabled, devIDModuleEntry=devIDModuleEntry, devIDMIBModuleCompliance2=devIDMIBModuleCompliance2, devIDMIBModuleCompliance=devIDMIBModuleCompliance, ieee8021DevIDMIB=ieee8021DevIDMIB, DevIDErrorStatus=DevIDErrorStatus, devIDCredentialIssuer=devIDCredentialIssuer, devIDStatisticKeyInsertionCount=devIDStatisticKeyInsertionCount, devIDChainCertFingerprint=devIDChainCertFingerprint, devIDCredentialErrStatus=devIDCredentialErrStatus, devIDPublicKeyErrStatus=devIDPublicKeyErrStatus, devIDPublicKeyTable=devIDPublicKeyTable, PYSNMP_MODULE_ID=ieee8021DevIDMIB, devIDCertIDevID=devIDCertIDevID, devIDModuleGeneratesLDevIDKeys=devIDModuleGeneratesLDevIDKeys, devIDCredentialSubject=devIDCredentialSubject, devIDMIBConformance=devIDMIBConformance, devIDStatsMIBObjects=devIDStatsMIBObjects, devIDModuleTable=devIDModuleTable, devIDChainEntry=devIDChainEntry, devIDCert=devIDCert, devIDMgmtMIBObjects=devIDMgmtMIBObjects, devIDStatisticCredentialInsertionCount=devIDStatisticCredentialInsertionCount, devIDCredentialEnabled=devIDCredentialEnabled, devIDMIBObjects=devIDMIBObjects, devIDStatisticKeyGenerationCount=devIDStatisticKeyGenerationCount, devIDStatisticCertInsertionCount=devIDStatisticCertInsertionCount, devIDCertTable=devIDCertTable, devIDMIBAuditGroup=devIDMIBAuditGroup, devIDStatisticKeyDeletionCount=devIDStatisticKeyDeletionCount, DevIDAlgorithmIdentifier=DevIDAlgorithmIdentifier, devIDChainTable=devIDChainTable, devIDPublicKeyIndex=devIDPublicKeyIndex, devIDCertEntry=devIDCertEntry, devIDModuleInsertsLDevIDKeys=devIDModuleInsertsLDevIDKeys, devIDChainCert=devIDChainCert, devIDMIBGroups=devIDMIBGroups, devIDCredentialSHA1Hash=devIDCredentialSHA1Hash, devIDCredentialSerialNumber=devIDCredentialSerialNumber, devIDStatisticCredentialDeletionCount=devIDStatisticCredentialDeletionCount, devIDMIBModuleGroup=devIDMIBModuleGroup, devIDMIBNotifications=devIDMIBNotifications, devIDCertFingerprint=devIDCertFingerprint, devIDChainCertIndex=devIDChainCertIndex, devIDPublicKeyEntry=devIDPublicKeyEntry, devIDCredentialPubkeyIndex=devIDCredentialPubkeyIndex, devIDStatisticCertDeletionCount=devIDStatisticCertDeletionCount, devIDCertKeyEnabled=devIDCertKeyEnabled, devIDCredentialEntityIndex=devIDCredentialEntityIndex, devIDCredentialIndex=devIDCredentialIndex, devIDPublicKeyCount=devIDPublicKeyCount, devIDStatisticCSRGenerationCount=devIDStatisticCSRGenerationCount, DevIDFingerprint=DevIDFingerprint, devIDCredentialCount=devIDCredentialCount)
