#
# PySNMP MIB module PRVT-VRRP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-VRRP-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:35 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Unsigned32, ObjectIdentity, ModuleIdentity, NotificationType, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, IpAddress, Bits, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "NotificationType", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "IpAddress", "Bits", "Counter64", "TimeTicks")
TextualConvention, RowStatus, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString", "TruthValue")
prvtVrrpMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 5, 167))
prvtVrrpMIB.setRevisions(('2014-11-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtVrrpMIB.setRevisionsDescriptions(('Initial version',))
if mibBuilder.loadTexts: prvtVrrpMIB.setLastUpdated('201411100000Z')
if mibBuilder.loadTexts: prvtVrrpMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtVrrpMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtVrrpMIB.setDescription('This MIB describes objects used for managing Virtual Router Redundancy Protocol (VRRP) routers.')
prvtVrrpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1))
prvtVrrpVirtualRouterTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1), )
if mibBuilder.loadTexts: prvtVrrpVirtualRouterTable.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterTable.setDescription('')
prvtVrrpVirtualRouterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1), ).setIndexNames((0, "PRVT-VRRP-MIB", "prvtVrrpVirtualRouterId"))
if mibBuilder.loadTexts: prvtVrrpVirtualRouterEntry.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterEntry.setDescription('NONE')
prvtVrrpVirtualRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: prvtVrrpVirtualRouterId.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterId.setDescription('')
prvtVrrpVirtualRouterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterRowStatus.setDescription('')
prvtVrrpVirtualRouterShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 3), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterShutdown.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterShutdown.setDescription('')
prvtVrrpVirtualRouterPreempt = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 4), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterPreempt.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterPreempt.setDescription('')
prvtVrrpVirtualRouterPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 254))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterPriority.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterPriority.setDescription('')
prvtVrrpVirtualRouterVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 6), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterVersion.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterVersion.setDescription('')
prvtVrrpVirtualRouterAdvertisedInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 7), Unsigned32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 4095), ))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterAdvertisedInterval.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterAdvertisedInterval.setDescription('')
prvtVrrpVirtualRouterAcceptMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("icmp", 1), ("all", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterAcceptMode.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterAcceptMode.setDescription('')
prvtVrrpVirtualRouterInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 9), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterInterface.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterInterface.setDescription('')
prvtVrrpVirtualRouterTraceUplinkThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterTraceUplinkThreshold.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterTraceUplinkThreshold.setDescription('')
prvtVrrpVirtualRouterTraceUplinkFlushTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 101))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterTraceUplinkFlushTimer.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterTraceUplinkFlushTimer.setDescription('')
prvtVrrpVirtualRouterStateVrrp = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("init", 1), ("backup", 2), ("master", 3), ("initWait", 4), ("none", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtVrrpVirtualRouterStateVrrp.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualRouterStateVrrp.setDescription('')
prvtVrrpVirtualIpAddressTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 2), )
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressTable.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressTable.setDescription('')
prvtVrrpVirtualIpAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 2, 1), ).setIndexNames((0, "PRVT-VRRP-MIB", "prvtVrrpVirtualRouterId"), (0, "PRVT-VRRP-MIB", "prvtVrrpVirtualIpAddress"))
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressEntry.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressEntry.setDescription('')
prvtVrrpVirtualIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 2, 1, 1), IpAddress())
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddress.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddress.setDescription('')
prvtVrrpVirtualIpAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressRowStatus.setDescription('')
prvtVrrpVirtualIpAddressRange = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 2, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressRange.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpVirtualIpAddressRange.setDescription('')
prvtVrrpTraceUplinkTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 3), )
if mibBuilder.loadTexts: prvtVrrpTraceUplinkTable.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpTraceUplinkTable.setDescription('')
prvtVrrpTraceUplinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 3, 1), ).setIndexNames((0, "PRVT-VRRP-MIB", "prvtVrrpVirtualRouterId"), (0, "PRVT-VRRP-MIB", "prvtVrrpTraceUplinkName"))
if mibBuilder.loadTexts: prvtVrrpTraceUplinkEntry.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpTraceUplinkEntry.setDescription('')
prvtVrrpTraceUplinkName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 3, 1, 1), OctetString())
if mibBuilder.loadTexts: prvtVrrpTraceUplinkName.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpTraceUplinkName.setDescription('')
prvtVrrpTraceUplinkRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 5, 167, 1, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtVrrpTraceUplinkRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtVrrpTraceUplinkRowStatus.setDescription('')
mibBuilder.exportSymbols("PRVT-VRRP-MIB", prvtVrrpVirtualIpAddress=prvtVrrpVirtualIpAddress, prvtVrrpVirtualRouterRowStatus=prvtVrrpVirtualRouterRowStatus, prvtVrrpTraceUplinkName=prvtVrrpTraceUplinkName, prvtVrrpVirtualRouterVersion=prvtVrrpVirtualRouterVersion, prvtVrrpVirtualRouterShutdown=prvtVrrpVirtualRouterShutdown, prvtVrrpVirtualRouterPriority=prvtVrrpVirtualRouterPriority, prvtVrrpVirtualIpAddressTable=prvtVrrpVirtualIpAddressTable, prvtVrrpVirtualRouterInterface=prvtVrrpVirtualRouterInterface, prvtVrrpTraceUplinkRowStatus=prvtVrrpTraceUplinkRowStatus, prvtVrrpVirtualRouterTable=prvtVrrpVirtualRouterTable, prvtVrrpTraceUplinkEntry=prvtVrrpTraceUplinkEntry, prvtVrrpVirtualRouterId=prvtVrrpVirtualRouterId, prvtVrrpVirtualIpAddressRowStatus=prvtVrrpVirtualIpAddressRowStatus, prvtVrrpObjects=prvtVrrpObjects, prvtVrrpVirtualRouterAcceptMode=prvtVrrpVirtualRouterAcceptMode, prvtVrrpVirtualRouterPreempt=prvtVrrpVirtualRouterPreempt, prvtVrrpVirtualIpAddressRange=prvtVrrpVirtualIpAddressRange, prvtVrrpVirtualRouterTraceUplinkFlushTimer=prvtVrrpVirtualRouterTraceUplinkFlushTimer, prvtVrrpVirtualRouterAdvertisedInterval=prvtVrrpVirtualRouterAdvertisedInterval, prvtVrrpVirtualRouterEntry=prvtVrrpVirtualRouterEntry, prvtVrrpTraceUplinkTable=prvtVrrpTraceUplinkTable, PYSNMP_MODULE_ID=prvtVrrpMIB, prvtVrrpVirtualIpAddressEntry=prvtVrrpVirtualIpAddressEntry, prvtVrrpVirtualRouterStateVrrp=prvtVrrpVirtualRouterStateVrrp, prvtVrrpMIB=prvtVrrpMIB, prvtVrrpVirtualRouterTraceUplinkThreshold=prvtVrrpVirtualRouterTraceUplinkThreshold)
