#
# PySNMP MIB module ADR155C-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sagemcom/ADR155C-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:35:53 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
sagemDr, = mibBuilder.importSymbols("SAGEM-DR-MIB", "sagemDr")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Counter64, TimeTicks, ModuleIdentity, iso, Unsigned32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter32, ObjectIdentity, MibIdentifier, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter64", "TimeTicks", "ModuleIdentity", "iso", "Unsigned32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter32", "ObjectIdentity", "MibIdentifier", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adr155c = ModuleIdentity((1, 3, 6, 1, 4, 1, 1038, 12))
if mibBuilder.loadTexts: adr155c.setLastUpdated('0211150000Z')
if mibBuilder.loadTexts: adr155c.setOrganization('SAGEM-Tolbiac drd/ddp/tmhd')
mibBuilder.exportSymbols("ADR155C-MIB", adr155c=adr155c, PYSNMP_MODULE_ID=adr155c)
