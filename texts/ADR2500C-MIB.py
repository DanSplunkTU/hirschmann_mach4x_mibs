#
# PySNMP MIB module ADR2500C-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR2500C-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:17:31 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, MibIdentifier, Bits, Integer32, NotificationType, Counter32, TimeTicks, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "MibIdentifier", "Bits", "Integer32", "NotificationType", "Counter32", "TimeTicks", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adr2500c = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 17))
if mibBuilder.loadTexts: adr2500c.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr2500c.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
if mibBuilder.loadTexts: adr2500c.setContactInfo('    ')
if mibBuilder.loadTexts: adr2500c.setDescription('The MIB module specific for ARD2500c equipment')
mibBuilder.exportSymbols("ADR2500C-MIB", adr2500c=adr2500c, PYSNMP_MODULE_ID=adr2500c)
