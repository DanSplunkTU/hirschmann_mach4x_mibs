#
# PySNMP MIB module PRVT-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-VRRP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:32 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, NotificationType, ObjectIdentity, Counter64, MibIdentifier, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, ModuleIdentity, TimeTicks, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "NotificationType", "ObjectIdentity", "Counter64", "MibIdentifier", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "ModuleIdentity", "TimeTicks", "IpAddress", "Bits")
TruthValue, DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "RowStatus", "TextualConvention")
prvtVrrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 167))
prvtVrrpMIB.setRevisions(('2014-11-10 00:00',))
if mibBuilder.loadTexts: prvtVrrpMIB.setLastUpdated('201411100000Z')
if mibBuilder.loadTexts: prvtVrrpMIB.setOrganization('BATM Advanced Communication')
prvtVrrpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1))
prvtVrrpVirtualRouterTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1), )
if mibBuilder.loadTexts: prvtVrrpVirtualRouterTable.setStatus('current')
prvtVrrpVirtualRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1), ).setIndexNames((0, "PRVT-VRRP-MIB", "prvtVrrpVirtualRouterId"))
if mibBuilder.loadTexts: prvtVrrpVirtualRouterEntry.setStatus('current')
prvtVrrpVirtualRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: prvtVrrpVirtualRouterId.setStatus('current')
prvtVrrpVirtualRouterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterRowStatus.setStatus('current')
prvtVrrpVirtualRouterShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterShutdown.setStatus('current')
prvtVrrpVirtualRouterPreempt = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterPreempt.setStatus('current')
prvtVrrpVirtualRouterPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterPriority.setStatus('current')
prvtVrrpVirtualRouterVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterVersion.setStatus('current')
prvtVrrpVirtualRouterAdvertisedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 4095), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterAdvertisedInterval.setStatus('current')
prvtVrrpVirtualRouterAcceptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("icmp", 1), ("all", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterAcceptMode.setStatus('current')
prvtVrrpVirtualRouterInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 9), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterInterface.setStatus('current')
prvtVrrpVirtualRouterTraceUplinkThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterTraceUplinkThreshold.setStatus('current')
prvtVrrpVirtualRouterTraceUplinkFlushTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterTraceUplinkFlushTimer.setStatus('current')
prvtVrrpVirtualRouterStateVrrp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("init", 1), ("backup", 2), ("master", 3), ("initWait", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterStateVrrp.setStatus('current')
prvtVrrpVirtualIpAddressTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 2), )
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressTable.setStatus('current')
prvtVrrpVirtualIpAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 2, 1), ).setIndexNames((0, "PRVT-VRRP-MIB", "prvtVrrpVirtualRouterId"), (0, "PRVT-VRRP-MIB", "prvtVrrpVirtualIpAddress"))
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressEntry.setStatus('current')
prvtVrrpVirtualIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddress.setStatus('current')
prvtVrrpVirtualIpAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressRowStatus.setStatus('current')
prvtVrrpVirtualIpAddressRange = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressRange.setStatus('current')
prvtVrrpTraceUplinkTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 3), )
if mibBuilder.loadTexts: prvtVrrpTraceUplinkTable.setStatus('current')
prvtVrrpTraceUplinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 3, 1), ).setIndexNames((0, "PRVT-VRRP-MIB", "prvtVrrpVirtualRouterId"), (0, "PRVT-VRRP-MIB", "prvtVrrpTraceUplinkName"))
if mibBuilder.loadTexts: prvtVrrpTraceUplinkEntry.setStatus('current')
prvtVrrpTraceUplinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 3, 1, 1), OctetString())
if mibBuilder.loadTexts: prvtVrrpTraceUplinkName.setStatus('current')
prvtVrrpTraceUplinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpTraceUplinkRowStatus.setStatus('current')
mibBuilder.exportSymbols("PRVT-VRRP-MIB", prvtVrrpVirtualRouterEntry=prvtVrrpVirtualRouterEntry, prvtVrrpVirtualRouterPriority=prvtVrrpVirtualRouterPriority, prvtVrrpObjects=prvtVrrpObjects, prvtVrrpVirtualRouterId=prvtVrrpVirtualRouterId, prvtVrrpVirtualRouterVersion=prvtVrrpVirtualRouterVersion, prvtVrrpVirtualIpAddressRowStatus=prvtVrrpVirtualIpAddressRowStatus, prvtVrrpTraceUplinkRowStatus=prvtVrrpTraceUplinkRowStatus, prvtVrrpVirtualRouterAcceptMode=prvtVrrpVirtualRouterAcceptMode, prvtVrrpVirtualIpAddressTable=prvtVrrpVirtualIpAddressTable, prvtVrrpVirtualRouterPreempt=prvtVrrpVirtualRouterPreempt, prvtVrrpVirtualRouterInterface=prvtVrrpVirtualRouterInterface, prvtVrrpVirtualRouterRowStatus=prvtVrrpVirtualRouterRowStatus, prvtVrrpVirtualRouterTraceUplinkThreshold=prvtVrrpVirtualRouterTraceUplinkThreshold, prvtVrrpTraceUplinkEntry=prvtVrrpTraceUplinkEntry, prvtVrrpVirtualIpAddress=prvtVrrpVirtualIpAddress, prvtVrrpTraceUplinkName=prvtVrrpTraceUplinkName, prvtVrrpVirtualIpAddressRange=prvtVrrpVirtualIpAddressRange, prvtVrrpVirtualRouterShutdown=prvtVrrpVirtualRouterShutdown, prvtVrrpTraceUplinkTable=prvtVrrpTraceUplinkTable, prvtVrrpVirtualRouterTraceUplinkFlushTimer=prvtVrrpVirtualRouterTraceUplinkFlushTimer, prvtVrrpVirtualRouterAdvertisedInterval=prvtVrrpVirtualRouterAdvertisedInterval, prvtVrrpVirtualRouterStateVrrp=prvtVrrpVirtualRouterStateVrrp, prvtVrrpVirtualRouterTable=prvtVrrpVirtualRouterTable, prvtVrrpVirtualIpAddressEntry=prvtVrrpVirtualIpAddressEntry, prvtVrrpMIB=prvtVrrpMIB, PYSNMP_MODULE_ID=prvtVrrpMIB)
