#
# PySNMP MIB module ELTEK-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/eltek/ELTEK-COMMON-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:11:45 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Counter64, ModuleIdentity, Unsigned32, MibIdentifier, Integer32, Gauge32, mib_2, iso, Bits, IpAddress, TimeTicks, ObjectIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter64", "ModuleIdentity", "Unsigned32", "MibIdentifier", "Integer32", "Gauge32", "mib-2", "iso", "Bits", "IpAddress", "TimeTicks", "ObjectIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
eltek = ModuleIdentity((1, 3, 6, 1, 4, 1, 12148))
eltek.setRevisions(('2015-01-03 08:25', '2010-10-29 08:29', '2009-03-12 15:15', '2008-01-30 11:49', '2007-06-22 11:27', '2005-09-07 12:38', '2005-06-28 11:30',))
if mibBuilder.loadTexts: eltek.setLastUpdated('201501030825Z')
if mibBuilder.loadTexts: eltek.setOrganization('ELTEK dcSystem MIB Working Group')
mibBuilder.exportSymbols("ELTEK-COMMON-MIB", PYSNMP_MODULE_ID=eltek, eltek=eltek)
