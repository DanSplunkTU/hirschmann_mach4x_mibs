#
# PySNMP MIB module OG-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/opengear/OG-SMI-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:33:34 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Gauge32, Unsigned32, NotificationType, Counter32, IpAddress, enterprises, ObjectIdentity, TimeTicks, MibIdentifier, ModuleIdentity, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Gauge32", "Unsigned32", "NotificationType", "Counter32", "IpAddress", "enterprises", "ObjectIdentity", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Bits", "Integer32")
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
mibBuilder.exportSymbols("OG-SMI-MIB", PYSNMP_MODULE_ID=opengear, ogSpecific=ogSpecific, ogExperimental=ogExperimental, opengear=opengear, ogLegacyMgmt=ogLegacyMgmt, ogInternal=ogInternal, ogReserved2=ogReserved2, ogReserved1=ogReserved1, ogAgentCapability=ogAgentCapability, ogConfig=ogConfig, ogModules=ogModules, ogMgmt=ogMgmt, otherEnterprises=otherEnterprises, ogProducts=ogProducts)
