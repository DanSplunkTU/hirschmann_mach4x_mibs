#
# PySNMP MIB module BENU-PLATFORM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:32:19 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
benu, = mibBuilder.importSymbols("BENU-ENTERPRISE-MIB", "benu")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, iso, Integer32, Gauge32, MibIdentifier, Bits, TimeTicks, IpAddress, ObjectIdentity, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "iso", "Integer32", "Gauge32", "MibIdentifier", "Bits", "TimeTicks", "IpAddress", "ObjectIdentity", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuPlatform = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1))
benuPlatform.setRevisions(('2012-10-18 00:00',))
if mibBuilder.loadTexts: benuPlatform.setLastUpdated('201210180000Z')
if mibBuilder.loadTexts: benuPlatform.setOrganization('Benu Networks,Inc')
mibBuilder.exportSymbols("BENU-PLATFORM-MIB", PYSNMP_MODULE_ID=benuPlatform, benuPlatform=benuPlatform)
