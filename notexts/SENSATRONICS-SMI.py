#
# PySNMP MIB module SENSATRONICS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/sensatronics/SENSATRONICS-SMI
# Produced by pysmi-1.1.3 at Sun Nov 21 00:35:44 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter64, IpAddress, Gauge32, ObjectIdentity, enterprises, TimeTicks, iso, MibIdentifier, Bits, Counter32, Unsigned32, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter64", "IpAddress", "Gauge32", "ObjectIdentity", "enterprises", "TimeTicks", "iso", "MibIdentifier", "Bits", "Counter32", "Unsigned32", "Integer32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sensatronics = ModuleIdentity((1, 3, 6, 1, 4, 1, 16174))
sensatronics.setRevisions(('2004-04-20 00:00',))
if mibBuilder.loadTexts: sensatronics.setLastUpdated('200404200000Z')
if mibBuilder.loadTexts: sensatronics.setOrganization('Sensatronics LLC')
consumerProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1))
if mibBuilder.loadTexts: consumerProducts.setStatus('current')
envMonitors = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1))
if mibBuilder.loadTexts: envMonitors.setStatus('current')
consumerTools = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 2))
if mibBuilder.loadTexts: consumerTools.setStatus('current')
customProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 3))
if mibBuilder.loadTexts: customProducts.setStatus('current')
customTools = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 4))
if mibBuilder.loadTexts: customTools.setStatus('current')
productITTM = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 1))
if mibBuilder.loadTexts: productITTM.setStatus('current')
productCRYO = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 2))
if mibBuilder.loadTexts: productCRYO.setStatus('current')
productEM1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 16174, 1, 1, 3))
if mibBuilder.loadTexts: productEM1.setStatus('current')
mibBuilder.exportSymbols("SENSATRONICS-SMI", customProducts=customProducts, productEM1=productEM1, productITTM=productITTM, consumerTools=consumerTools, productCRYO=productCRYO, sensatronics=sensatronics, PYSNMP_MODULE_ID=sensatronics, customTools=customTools, envMonitors=envMonitors, consumerProducts=consumerProducts)
