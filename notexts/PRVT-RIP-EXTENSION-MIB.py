#
# PySNMP MIB module PRVT-RIP-EXTENSION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-RIP-EXTENSION-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ipSwitch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "ipSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, RowStatus, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "TruthValue", "DisplayString")
prvtRIPExtensionMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1))
prvtRIPExtensionMib.setRevisions(('2008-01-01 00:00', '2005-02-16 00:00', '2003-05-06 00:00', '2002-11-11 00:00',))
if mibBuilder.loadTexts: prvtRIPExtensionMib.setLastUpdated('200801010000Z')
if mibBuilder.loadTexts: prvtRIPExtensionMib.setOrganization('BATM Advanced Communication')
routingProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 4))
ripExtension = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1))
ripEnable = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ripEnable.setStatus('current')
ripRedistributeTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2), )
if mibBuilder.loadTexts: ripRedistributeTable.setStatus('current')
ripRedistributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2, 1), ).setIndexNames((0, "PRVT-RIP-EXTENSION-MIB", "ripRedistributeProtocol"))
if mibBuilder.loadTexts: ripRedistributeEntry.setStatus('current')
ripRedistributeProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("kernel", 1), ("connected", 2), ("static", 3), ("ospf", 4), ("bgp", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ripRedistributeProtocol.setStatus('current')
ripRedistributeMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ripRedistributeMetric.setStatus('current')
ripRedistributeRouteMap = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2, 1, 3), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ripRedistributeRouteMap.setStatus('current')
ripRedistributeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 4, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ripRedistributeRowStatus.setStatus('current')
mibBuilder.exportSymbols("PRVT-RIP-EXTENSION-MIB", ripExtension=ripExtension, ripRedistributeRouteMap=ripRedistributeRouteMap, prvtRIPExtensionMib=prvtRIPExtensionMib, ripEnable=ripEnable, PYSNMP_MODULE_ID=prvtRIPExtensionMib, ripRedistributeTable=ripRedistributeTable, ripRedistributeEntry=ripRedistributeEntry, ripRedistributeProtocol=ripRedistributeProtocol, ripRedistributeRowStatus=ripRedistributeRowStatus, ripRedistributeMetric=ripRedistributeMetric, routingProtocols=routingProtocols)
