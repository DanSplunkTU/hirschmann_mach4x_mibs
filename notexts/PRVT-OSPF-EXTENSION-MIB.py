#
# PySNMP MIB module PRVT-OSPF-EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-OSPF-EXTENSION-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:26:57 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ipSwitch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "ipSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, Bits, Counter64, MibIdentifier, TimeTicks, Counter32, NotificationType, IpAddress, Unsigned32, ObjectIdentity, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Bits", "Counter64", "MibIdentifier", "TimeTicks", "Counter32", "NotificationType", "IpAddress", "Unsigned32", "ObjectIdentity", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
prvtOSPFExtensionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2))
prvtOSPFExtensionMib.setRevisions(('2008-01-01 00:00', '2005-02-16 00:00', '2002-11-11 00:00',))
if mibBuilder.loadTexts: prvtOSPFExtensionMib.setLastUpdated('200801010000Z')
if mibBuilder.loadTexts: prvtOSPFExtensionMib.setOrganization('BATM Advanced Communication')
routingProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 4))
ospfExtension = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1))
ospfEnable = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ospfEnable.setStatus('current')
ospfRedistributeTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2), )
if mibBuilder.loadTexts: ospfRedistributeTable.setStatus('current')
ospfRedistributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1), ).setIndexNames((0, "PRVT-OSPF-EXTENSION-MIB", "ospfRedistributeProtocol"))
if mibBuilder.loadTexts: ospfRedistributeEntry.setStatus('current')
ospfRedistributeProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kernel", 1), ("connected", 2), ("static", 3), ("rip", 4), ("bgp", 5)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ospfRedistributeProtocol.setStatus('current')
ospfRedistributeMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777214))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ospfRedistributeMetric.setStatus('current')
ospfRedistributeMetricType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("e1", 1), ("e2", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ospfRedistributeMetricType.setStatus('current')
ospfRedistributeRouteMap = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1, 4), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ospfRedistributeRouteMap.setStatus('current')
ospfRedistributeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 2, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ospfRedistributeRowStatus.setStatus('current')
mibBuilder.exportSymbols("PRVT-OSPF-EXTENSION-MIB", ospfEnable=ospfEnable, PYSNMP_MODULE_ID=prvtOSPFExtensionMib, ospfRedistributeProtocol=ospfRedistributeProtocol, ospfRedistributeRouteMap=ospfRedistributeRouteMap, routingProtocols=routingProtocols, ospfRedistributeRowStatus=ospfRedistributeRowStatus, ospfRedistributeTable=ospfRedistributeTable, ospfRedistributeMetric=ospfRedistributeMetric, ospfExtension=ospfExtension, prvtOSPFExtensionMib=prvtOSPFExtensionMib, ospfRedistributeEntry=ospfRedistributeEntry, ospfRedistributeMetricType=ospfRedistributeMetricType)
