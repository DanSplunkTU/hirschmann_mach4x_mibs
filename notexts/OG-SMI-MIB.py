#
# PySNMP MIB module OG-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-SMI-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:42:14 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, NotificationType, Integer32, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, ObjectIdentity, Counter64, enterprises, Unsigned32, IpAddress, MibIdentifier, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "NotificationType", "Integer32", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "ObjectIdentity", "Counter64", "enterprises", "Unsigned32", "IpAddress", "MibIdentifier", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
opengear = ModuleIdentity((1, 3, 6, 1, 4, 1, 25049))
opengear.setRevisions(('2018-06-15 00:00', '2013-11-15 00:00', '2013-08-11 00:00', '2010-03-22 11:27', '2005-02-24 01:00',))
if mibBuilder.loadTexts: opengear.setLastUpdated('201806150000Z')
if mibBuilder.loadTexts: opengear.setOrganization('Opengear Inc.')
ogProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 1))
if mibBuilder.loadTexts: ogProducts.setStatus('current')
ogLegacyMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 2))
if mibBuilder.loadTexts: ogLegacyMgmt.setStatus('current')
ogExperimental = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 3))
if mibBuilder.loadTexts: ogExperimental.setStatus('current')
ogInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 4))
if mibBuilder.loadTexts: ogInternal.setStatus('current')
ogReserved1 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 5))
if mibBuilder.loadTexts: ogReserved1.setStatus('current')
ogReserved2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 6))
if mibBuilder.loadTexts: ogReserved2.setStatus('current')
otherEnterprises = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 7))
if mibBuilder.loadTexts: otherEnterprises.setStatus('current')
ogAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 8))
if mibBuilder.loadTexts: ogAgentCapability.setStatus('current')
ogConfig = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 9))
if mibBuilder.loadTexts: ogConfig.setStatus('current')
ogMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 10))
if mibBuilder.loadTexts: ogMgmt.setStatus('current')
ogModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 11))
if mibBuilder.loadTexts: ogModules.setStatus('current')
ogSpecific = ObjectIdentity((1, 3, 6, 1, 4, 1, 25049, 18))
if mibBuilder.loadTexts: ogSpecific.setStatus('current')
mibBuilder.exportSymbols("OG-SMI-MIB", ogLegacyMgmt=ogLegacyMgmt, ogSpecific=ogSpecific, PYSNMP_MODULE_ID=opengear, ogConfig=ogConfig, ogAgentCapability=ogAgentCapability, opengear=opengear, ogInternal=ogInternal, otherEnterprises=otherEnterprises, ogModules=ogModules, ogReserved2=ogReserved2, ogReserved1=ogReserved1, ogExperimental=ogExperimental, ogMgmt=ogMgmt, ogProducts=ogProducts)
