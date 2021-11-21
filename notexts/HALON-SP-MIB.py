#
# PySNMP MIB module HALON-SP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/halon/HALON-SP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:41:00 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, ModuleIdentity, iso, TimeTicks, NotificationType, Unsigned32, Gauge32, enterprises, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Bits, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "ModuleIdentity", "iso", "TimeTicks", "NotificationType", "Unsigned32", "Gauge32", "enterprises", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Bits", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
halonSecuritySP = ModuleIdentity((1, 3, 6, 1, 4, 1, 33234, 1, 1))
halonSecuritySP.setRevisions(('2013-02-07 11:32',))
if mibBuilder.loadTexts: halonSecuritySP.setLastUpdated('201302061107Z')
if mibBuilder.loadTexts: halonSecuritySP.setOrganization('Halon Security')
halonSecurity = MibIdentifier((1, 3, 6, 1, 4, 1, 33234))
halonSecurityProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 33234, 1))
halonSecuritySPObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1))
serialNumber = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: serialNumber.setStatus('current')
configurationRevision = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configurationRevision.setStatus('current')
mailQueueLength = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mailQueueLength.setStatus('current')
quarantinedMessages = MibScalar((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: quarantinedMessages.setStatus('current')
statTable = MibTable((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5), )
if mibBuilder.loadTexts: statTable.setStatus('current')
statEntry = MibTableRow((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1), ).setIndexNames((0, "HALON-SP-MIB", "statKey1Index"), (0, "HALON-SP-MIB", "statKey2Index"), (0, "HALON-SP-MIB", "statKey3Index"))
if mibBuilder.loadTexts: statEntry.setStatus('current')
statKey1Index = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statKey1Index.setStatus('current')
statKey2Index = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statKey2Index.setStatus('current')
statKey3Index = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statKey3Index.setStatus('current')
statCount = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statCount.setStatus('current')
statCreated = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statCreated.setStatus('current')
statUpdated = MibTableColumn((1, 3, 6, 1, 4, 1, 33234, 1, 1, 1, 5, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: statUpdated.setStatus('current')
mibBuilder.exportSymbols("HALON-SP-MIB", statCreated=statCreated, mailQueueLength=mailQueueLength, halonSecurity=halonSecurity, halonSecuritySPObjects=halonSecuritySPObjects, halonSecurityProducts=halonSecurityProducts, quarantinedMessages=quarantinedMessages, statTable=statTable, statKey3Index=statKey3Index, statCount=statCount, statEntry=statEntry, configurationRevision=configurationRevision, statKey1Index=statKey1Index, serialNumber=serialNumber, statUpdated=statUpdated, statKey2Index=statKey2Index, halonSecuritySP=halonSecuritySP, PYSNMP_MODULE_ID=halonSecuritySP)
