#
# PySNMP MIB module AT-MIBVERSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-MIBVERSION-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:37 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
sysinfo, = mibBuilder.importSymbols("AT-SMI-MIB", "sysinfo")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, ObjectIdentity, Unsigned32, IpAddress, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Bits", "iso", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atMibVersion = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 15))
atMibVersion.setRevisions(('2010-06-15 00:11', '2009-01-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atMibVersion.setRevisionsDescriptions(('MIB revision history dates in descriptions updated.', 'Initial revision.',))
if mibBuilder.loadTexts: atMibVersion.setLastUpdated('201006150011Z')
if mibBuilder.loadTexts: atMibVersion.setOrganization('Allied Telesis Labs New Zealand')
if mibBuilder.loadTexts: atMibVersion.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atMibVersion.setDescription("The mib-set version MIB, for detailing the versions of MIB's\n                that are currently supported by AT software.")
atMibsetVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3, 15, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atMibsetVersion.setStatus('current')
if mibBuilder.loadTexts: atMibsetVersion.setDescription("The overall version of the complete set of MIB's that is\n                currently supported by the software running on the device.\n\n                It returns an integer which relates to the last software\n                release that contained changes to the supported AT Enterprise\n                MIB definition files. For example, if the currently loaded\n                software release on the the device is 5.3.1-03 but the\n                Enterprise MIB's have not changed since 5.3.1-01, then the\n                value returned will be 5030101 (5.03.01-01).")
mibBuilder.exportSymbols("AT-MIBVERSION-MIB", PYSNMP_MODULE_ID=atMibVersion, atMibVersion=atMibVersion, atMibsetVersion=atMibsetVersion)
