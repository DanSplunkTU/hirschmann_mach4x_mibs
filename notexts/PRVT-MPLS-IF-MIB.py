#
# PySNMP MIB module PRVT-MPLS-IF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-MPLS-IF-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifEntry, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifEntry", "ifIndex")
InetAddress, = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress")
mpls, = mibBuilder.importSymbols("PRVT-CR-LDP-MIB", "mpls")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
RowStatus, TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TruthValue", "TextualConvention", "DisplayString")
prvtMPLSIfMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6))
prvtMPLSIfMib.setRevisions(('2008-01-01 00:00', '2007-01-23 00:00', '2006-06-27 00:00', '2006-01-08 00:00', '2005-11-11 00:00',))
if mibBuilder.loadTexts: prvtMPLSIfMib.setLastUpdated('200801010000Z')
if mibBuilder.loadTexts: prvtMPLSIfMib.setOrganization('BATM Advanced Communication')
prvtMPLSIfaceObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1))
prvtMPLSRouteObjs = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2))
prvtMplsIfaceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1), )
if mibBuilder.loadTexts: prvtMplsIfaceTable.setStatus('current')
prvtMplsIfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: prvtMplsIfaceEntry.setStatus('current')
ifaceMplsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceMplsEnable.setStatus('current')
ifaceMplsPHPEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceMplsPHPEnable.setStatus('current')
ifaceMplsIngressLblRangeLow = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32768, 131071))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceMplsIngressLblRangeLow.setStatus('current')
ifaceMplsIngressLblRangeHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32768, 131071))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceMplsIngressLblRangeHigh.setStatus('current')
ifaceMplsEgressLblRangeLow = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32768, 131071))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceMplsEgressLblRangeLow.setStatus('current')
ifaceMplsEgressLblRangeHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(32768, 131071))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceMplsEgressLblRangeHigh.setStatus('current')
ifaceMplsLdpHelloHoldTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceMplsLdpHelloHoldTimer.setStatus('current')
ifaceMplsLdpKeepaliveHoldTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceMplsLdpKeepaliveHoldTimer.setStatus('current')
ifaceMplsLdpUseGlobalLabelSpace = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 1, 1, 9), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceMplsLdpUseGlobalLabelSpace.setStatus('current')
prvtRsvpIfaceTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2), )
if mibBuilder.loadTexts: prvtRsvpIfaceTable.setStatus('current')
prvtRsvpIfaceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1), )
ifEntry.registerAugmentions(("PRVT-MPLS-IF-MIB", "prvtRsvpIfaceEntry"))
prvtRsvpIfaceEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: prvtRsvpIfaceEntry.setStatus('current')
ifaceRsvpRefreshInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpRefreshInterval.setStatus('current')
ifaceRsvpRefreshMultiple = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpRefreshMultiple.setStatus('current')
ifaceRsvpSlewNumerator = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpSlewNumerator.setStatus('current')
ifaceRsvpSlewDenom = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpSlewDenom.setStatus('current')
ifaceRsvpBlockadeMultiple = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpBlockadeMultiple.setStatus('current')
ifaceRsvpNotifyRRDecay = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpNotifyRRDecay.setStatus('current')
ifaceRsvpNotifyRRInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpNotifyRRInterval.setStatus('current')
ifaceRsvpNotifyRRLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 214783647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpNotifyRRLimit.setStatus('current')
ifaceRsvpHelloInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpHelloInterval.setStatus('current')
ifaceRsvpHelloDecay = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpHelloDecay.setStatus('current')
ifaceRsvpHelloTolerance = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 11), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpHelloTolerance.setStatus('current')
ifaceRsvpHelloPersist = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpHelloPersist.setStatus('current')
ifaceRsvpHelloTTL = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ifaceRsvpHelloTTL.setStatus('current')
prvtMplsRouteProtocolTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 1), )
if mibBuilder.loadTexts: prvtMplsRouteProtocolTable.setStatus('current')
prvtMplsRouteProtocolEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 1, 1), ).setIndexNames((0, "PRVT-MPLS-IF-MIB", "prvtMplsRouteDirection"), (0, "PRVT-MPLS-IF-MIB", "prvtMplsRouteType"))
if mibBuilder.loadTexts: prvtMplsRouteProtocolEntry.setStatus('current')
prvtMplsRouteDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsRouteDirection.setStatus('current')
prvtMplsRouteType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("bgp", 1), ("connected", 2), ("isis", 3), ("kernel", 4), ("ospf", 5), ("rip", 6), ("static", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsRouteType.setStatus('current')
prvtMplsRouteRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsRouteRowStatus.setStatus('current')
prvtMplsRouteAddressTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2), )
if mibBuilder.loadTexts: prvtMplsRouteAddressTable.setStatus('current')
prvtMplsRouteAddressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2, 1), ).setIndexNames((0, "PRVT-MPLS-IF-MIB", "prvtMplsAddressDirection"), (0, "PRVT-MPLS-IF-MIB", "prvtMplsAddressIPAddr"), (0, "PRVT-MPLS-IF-MIB", "prvtMplsAddressMask"))
if mibBuilder.loadTexts: prvtMplsRouteAddressEntry.setStatus('current')
prvtMplsAddressDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ingress", 1), ("egress", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsAddressDirection.setStatus('current')
prvtMplsAddressIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2, 1, 2), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsAddressIPAddr.setStatus('current')
prvtMplsAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtMplsAddressMask.setStatus('current')
prvtMplsAddressRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 5, 6, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtMplsAddressRowStatus.setStatus('current')
mibBuilder.exportSymbols("PRVT-MPLS-IF-MIB", ifaceMplsEgressLblRangeHigh=ifaceMplsEgressLblRangeHigh, prvtMplsRouteProtocolEntry=prvtMplsRouteProtocolEntry, ifaceRsvpRefreshMultiple=ifaceRsvpRefreshMultiple, PYSNMP_MODULE_ID=prvtMPLSIfMib, ifaceRsvpSlewDenom=ifaceRsvpSlewDenom, ifaceRsvpBlockadeMultiple=ifaceRsvpBlockadeMultiple, ifaceRsvpHelloTolerance=ifaceRsvpHelloTolerance, prvtRsvpIfaceEntry=prvtRsvpIfaceEntry, prvtMplsAddressDirection=prvtMplsAddressDirection, prvtMplsRouteAddressTable=prvtMplsRouteAddressTable, prvtMplsAddressRowStatus=prvtMplsAddressRowStatus, ifaceMplsIngressLblRangeHigh=ifaceMplsIngressLblRangeHigh, ifaceMplsLdpUseGlobalLabelSpace=ifaceMplsLdpUseGlobalLabelSpace, ifaceMplsEgressLblRangeLow=ifaceMplsEgressLblRangeLow, ifaceRsvpHelloInterval=ifaceRsvpHelloInterval, prvtMPLSIfMib=prvtMPLSIfMib, prvtMplsAddressMask=prvtMplsAddressMask, prvtMplsRouteDirection=prvtMplsRouteDirection, ifaceRsvpNotifyRRDecay=ifaceRsvpNotifyRRDecay, prvtMplsAddressIPAddr=prvtMplsAddressIPAddr, prvtMplsRouteAddressEntry=prvtMplsRouteAddressEntry, ifaceRsvpRefreshInterval=ifaceRsvpRefreshInterval, ifaceRsvpNotifyRRLimit=ifaceRsvpNotifyRRLimit, prvtMPLSRouteObjs=prvtMPLSRouteObjs, ifaceRsvpHelloDecay=ifaceRsvpHelloDecay, prvtMplsIfaceEntry=prvtMplsIfaceEntry, prvtMPLSIfaceObjs=prvtMPLSIfaceObjs, ifaceMplsEnable=ifaceMplsEnable, ifaceRsvpHelloTTL=ifaceRsvpHelloTTL, prvtRsvpIfaceTable=prvtRsvpIfaceTable, ifaceRsvpSlewNumerator=ifaceRsvpSlewNumerator, prvtMplsRouteType=prvtMplsRouteType, ifaceRsvpHelloPersist=ifaceRsvpHelloPersist, prvtMplsIfaceTable=prvtMplsIfaceTable, prvtMplsRouteProtocolTable=prvtMplsRouteProtocolTable, ifaceMplsLdpHelloHoldTimer=ifaceMplsLdpHelloHoldTimer, ifaceMplsIngressLblRangeLow=ifaceMplsIngressLblRangeLow, prvtMplsRouteRowStatus=prvtMplsRouteRowStatus, ifaceMplsPHPEnable=ifaceMplsPHPEnable, ifaceRsvpNotifyRRInterval=ifaceRsvpNotifyRRInterval, ifaceMplsLdpKeepaliveHoldTimer=ifaceMplsLdpKeepaliveHoldTimer)
