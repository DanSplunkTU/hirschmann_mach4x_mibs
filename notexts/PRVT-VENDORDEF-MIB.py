#
# PySNMP MIB module PRVT-VENDORDEF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-VENDORDEF-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:51 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Unsigned32, MibIdentifier, Counter64, Gauge32, ModuleIdentity, Integer32, Counter32, NotificationType, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Unsigned32", "MibIdentifier", "Counter64", "Gauge32", "ModuleIdentity", "Integer32", "Counter32", "NotificationType", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
prvtVendorDefMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738))
prvtVendorDefMIB.setRevisions(('2007-09-29 00:00',))
if mibBuilder.loadTexts: prvtVendorDefMIB.setLastUpdated('200709290000Z')
if mibBuilder.loadTexts: prvtVendorDefMIB.setOrganization('BATM Advanced Communication')
prvt_products = ObjectIdentity((1, 3, 6, 1, 4, 1, 738, 10)).setLabel("prvt-products")
if mibBuilder.loadTexts: prvt_products.setStatus('current')
mibBuilder.exportSymbols("PRVT-VENDORDEF-MIB", PYSNMP_MODULE_ID=prvtVendorDefMIB, prvt_products=prvt_products, prvtVendorDefMIB=prvtVendorDefMIB)
