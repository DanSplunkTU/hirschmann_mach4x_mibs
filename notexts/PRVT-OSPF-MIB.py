#
# PySNMP MIB module PRVT-OSPF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-OSPF-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:45 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
routingProtocols, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "routingProtocols")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, Integer32, NotificationType, MibIdentifier, TimeTicks, Unsigned32, Counter32, IpAddress, Bits, Gauge32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "Integer32", "NotificationType", "MibIdentifier", "TimeTicks", "Unsigned32", "Counter32", "IpAddress", "Bits", "Gauge32", "Counter64")
TruthValue, TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "RowStatus", "DisplayString")
prvtOspfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2))
prvtOspfMIB.setRevisions(('2012-04-01 00:00', '2011-06-02 00:00', '2009-11-13 00:00',))
if mibBuilder.loadTexts: prvtOspfMIB.setLastUpdated('201204010000Z')
if mibBuilder.loadTexts: prvtOspfMIB.setOrganization('BATM Advanced Communication')
class PrvtOspfDesignatedRouterPriority(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

class PrvtOspfIpAddress(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
prvtOspfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1))
prvtOspfRouterId = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtOspfRouterId.setStatus('current')
prvtOspfAdminStat = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtOspfAdminStat.setStatus('current')
prvtOspfVersionNumber = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2))).clone(namedValues=NamedValues(("version2", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfVersionNumber.setStatus('current')
prvtOspfExternLsaCount = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfExternLsaCount.setStatus('current')
prvtOspfExternLsaCksumSum = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfExternLsaCksumSum.setStatus('current')
prvtOspfTOSSupport = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfTOSSupport.setStatus('current')
prvtOspfOriginateNewLsas = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfOriginateNewLsas.setStatus('current')
prvtOspfRxNewLsas = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfRxNewLsas.setStatus('current')
prvtOspfExtLsdbLimit = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtOspfExtLsdbLimit.setStatus('current')
prvtOspfMulticastExtensions = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfMulticastExtensions.setStatus('current')
prvtOspfExitOverflowInterval = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 11), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtOspfExitOverflowInterval.setStatus('current')
prvtOspfDemandExtensions = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfDemandExtensions.setStatus('current')
prvtOspfAreaTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13), )
if mibBuilder.loadTexts: prvtOspfAreaTable.setStatus('current')
prvtOspfAreaEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1), ).setIndexNames((0, "PRVT-OSPF-MIB", "prvtOspfAreaId"))
if mibBuilder.loadTexts: prvtOspfAreaEntry.setStatus('current')
prvtOspfAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 1), OctetString())
if mibBuilder.loadTexts: prvtOspfAreaId.setStatus('current')
prvtOspfAreaRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaRowStatus.setStatus('current')
prvtOspfAreaType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("default", 0), ("stub", 1), ("nssa", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaType.setStatus('current')
prvtOspfAreaSummary = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAreaSummary", 1), ("sendAreaSummary", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaSummary.setStatus('current')
prvtOspfAreaAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("md5", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaAuthType.setStatus('current')
prvtOspfAreaShortcutConfiguration = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 6), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaShortcutConfiguration.setStatus('current')
prvtOspfAreaNssaTransitRole = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("ospfNssaRoleNever", 0), ("ospfNssaRoleAlways", 1), ("ospfNssaRoleCandidate", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaNssaTransitRole.setStatus('current')
prvtOspfAreaImportList = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 8), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaImportList.setStatus('current')
prvtOspfAreaExportList = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 9), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaExportList.setStatus('current')
prvtOspfAreaMetric = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaMetric.setStatus('current')
prvtOspfAreaMetricType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ospfMetric", 1), ("comparableCost", 2), ("nonComparable", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaMetricType.setStatus('current')
prvtOspfAreaDefaultCost = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 13, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfAreaDefaultCost.setStatus('current')
prvtOspfLsdbTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14), )
if mibBuilder.loadTexts: prvtOspfLsdbTable.setStatus('current')
prvtOspfLsdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14, 1), ).setIndexNames((0, "PRVT-OSPF-MIB", "prvtOspfLsdbAreaId"), (0, "PRVT-OSPF-MIB", "prvtOspfLsdbType"), (0, "PRVT-OSPF-MIB", "prvtOspfLsdbLsid"), (0, "PRVT-OSPF-MIB", "prvtOspfLsdbRouterId"))
if mibBuilder.loadTexts: prvtOspfLsdbEntry.setStatus('current')
prvtOspfLsdbAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14, 1, 1), IpAddress())
if mibBuilder.loadTexts: prvtOspfLsdbAreaId.setStatus('current')
prvtOspfLsdbType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("routerLink", 1), ("networkLink", 2), ("summaryLink", 3), ("asSummaryLink", 4), ("asExternalLink", 5), ("multicastLink", 6), ("nssaExternalLink", 7), ("unknownLink", 8), ("opaqueLinkLsa", 9), ("opaqueAreaLsa", 10), ("opaqueAsLsa", 11))))
if mibBuilder.loadTexts: prvtOspfLsdbType.setStatus('current')
prvtOspfLsdbLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14, 1, 3), IpAddress())
if mibBuilder.loadTexts: prvtOspfLsdbLsid.setStatus('current')
prvtOspfLsdbRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14, 1, 4), IpAddress())
if mibBuilder.loadTexts: prvtOspfLsdbRouterId.setStatus('current')
prvtOspfLsdbSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfLsdbSequence.setStatus('current')
prvtOspfLsdbAge = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfLsdbAge.setStatus('current')
prvtOspfLsdbChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfLsdbChecksum.setStatus('current')
prvtOspfLsdbLength = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfLsdbLength.setStatus('current')
prvtOspfLsdbAdvertisement = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 14, 1, 9), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfLsdbAdvertisement.setStatus('current')
prvtOspfExtLsdbTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 15), )
if mibBuilder.loadTexts: prvtOspfExtLsdbTable.setStatus('current')
prvtOspfExtLsdbEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 15, 1), ).setIndexNames((0, "PRVT-OSPF-MIB", "prvtOspfExtLsdbType"), (0, "PRVT-OSPF-MIB", "prvtOspfExtLsdbLsid"), (0, "PRVT-OSPF-MIB", "prvtOspfExtLsdbRouterId"))
if mibBuilder.loadTexts: prvtOspfExtLsdbEntry.setStatus('current')
prvtOspfExtLsdbType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 15, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("routerLink", 1), ("networkLink", 2), ("summaryLink", 3), ("asSummaryLink", 4), ("asExternalLink", 5), ("multicastLink", 6), ("nssaExternalLink", 7), ("unknownLink", 8), ("opaqueLinkLsa", 9), ("opaqueAreaLsa", 10), ("opaqueAsLsa", 11))))
if mibBuilder.loadTexts: prvtOspfExtLsdbType.setStatus('current')
prvtOspfExtLsdbLsid = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 15, 1, 2), IpAddress())
if mibBuilder.loadTexts: prvtOspfExtLsdbLsid.setStatus('current')
prvtOspfExtLsdbRouterId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 15, 1, 3), IpAddress())
if mibBuilder.loadTexts: prvtOspfExtLsdbRouterId.setStatus('current')
prvtOspfExtLsdbSequence = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 15, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfExtLsdbSequence.setStatus('current')
prvtOspfExtLsdbAge = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 15, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-32768, 32767))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfExtLsdbAge.setStatus('current')
prvtOspfExtLsdbChecksum = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 15, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfExtLsdbChecksum.setStatus('current')
prvtOspfExtLsdbAdvertisement = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 15, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfExtLsdbAdvertisement.setStatus('current')
prvtOspfIfTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16), )
if mibBuilder.loadTexts: prvtOspfIfTable.setStatus('current')
prvtOspfIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1), ).setIndexNames((0, "PRVT-OSPF-MIB", "prvtOspfIfIpAddress"))
if mibBuilder.loadTexts: prvtOspfIfEntry.setStatus('current')
prvtOspfIfIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 1), IpAddress())
if mibBuilder.loadTexts: prvtOspfIfIpAddress.setStatus('current')
prvtOspfIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfRowStatus.setStatus('current')
prvtOspfIfAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 3), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfAreaId.setStatus('current')
prvtOspfIfWorkingMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("active", 0), ("passive", 1)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfWorkingMode.setStatus('current')
prvtOspfIfTransitDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfTransitDelay.setStatus('current')
prvtOspfIfPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfPriority.setStatus('current')
prvtOspfIfHelloTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfHelloTimer.setStatus('current')
prvtOspfIfDeadTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfDeadTimer.setStatus('current')
prvtOspfIfRetransmitInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfRetransmitInterval.setStatus('current')
prvtOspfIfOutputCost = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfOutputCost.setStatus('current')
prvtOspfIfAuthType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("simple", 1), ("md5", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfAuthType.setStatus('current')
prvtOspfIfAuthSimple = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 12), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 8))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfAuthSimple.setStatus('current')
prvtOspfIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 16, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("none", 0), ("broadcast", 1), ("nbma", 2), ("pointToPoint", 3), ("pointToMultipoint", 5), ("virtualLink", 6), ("loopback", 7)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfType.setStatus('current')
prvtOspfIfAuthMd5Table = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 17), )
if mibBuilder.loadTexts: prvtOspfIfAuthMd5Table.setStatus('current')
prvtOspfIfAuthMd5Entry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 17, 1), ).setIndexNames((0, "PRVT-OSPF-MIB", "prvtOspfIfIpAddress"), (0, "PRVT-OSPF-MIB", "prvtOspfIfAuthMd5Key"))
if mibBuilder.loadTexts: prvtOspfIfAuthMd5Entry.setStatus('current')
prvtOspfIfAuthMd5Key = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 17, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: prvtOspfIfAuthMd5Key.setStatus('current')
prvtOspfIfAuthMd5RowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 17, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfAuthMd5RowStatus.setStatus('current')
prvtOspfIfAuthMd5Word = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 17, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfIfAuthMd5Word.setStatus('current')
prvtOspfNbrTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18), )
if mibBuilder.loadTexts: prvtOspfNbrTable.setStatus('current')
prvtOspfNbrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1), ).setIndexNames((0, "PRVT-OSPF-MIB", "prvtOspfNbrIpAddr"), (0, "PRVT-OSPF-MIB", "prvtOspfNbrAddressLessIndex"))
if mibBuilder.loadTexts: prvtOspfNbrEntry.setStatus('current')
prvtOspfNbrIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1, 1), PrvtOspfIpAddress())
if mibBuilder.loadTexts: prvtOspfNbrIpAddr.setStatus('current')
prvtOspfNbrAddressLessIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-2147483648, 2147483647)))
if mibBuilder.loadTexts: prvtOspfNbrAddressLessIndex.setStatus('current')
prvtOspfNbrRtrId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1, 3), PrvtOspfIpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfNbrRtrId.setStatus('current')
prvtOspfNbrOptions = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfNbrOptions.setStatus('current')
prvtOspfNbrPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1, 5), PrvtOspfDesignatedRouterPriority()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfNbrPriority.setStatus('current')
prvtOspfNbrState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))).clone(namedValues=NamedValues(("down", 1), ("attempt", 2), ("init", 3), ("twoWay", 4), ("exchangeStart", 5), ("exchange", 6), ("loading", 7), ("full", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfNbrState.setStatus('current')
prvtOspfNbrEvents = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfNbrEvents.setStatus('current')
prvtOspfNbrLsRetransQLen = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfNbrLsRetransQLen.setStatus('current')
prvtOspfNbmaNbrPermanence = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("dynamic", 1), ("permanent", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfNbmaNbrPermanence.setStatus('current')
prvtOspfNbrHelloSuppressed = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 18, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfNbrHelloSuppressed.setStatus('current')
prvtOspfRedistributeTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 19), )
if mibBuilder.loadTexts: prvtOspfRedistributeTable.setStatus('current')
prvtOspfRedistributeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 19, 1), ).setIndexNames((0, "PRVT-OSPF-MIB", "prvtOspfRedistributeProtocol"))
if mibBuilder.loadTexts: prvtOspfRedistributeEntry.setStatus('current')
prvtOspfRedistributeProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 19, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 17))).clone(namedValues=NamedValues(("kernel", 2), ("connected", 3), ("static", 4), ("default", 17))))
if mibBuilder.loadTexts: prvtOspfRedistributeProtocol.setStatus('current')
prvtOspfRedistributeRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 19, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfRedistributeRowStatus.setStatus('current')
prvtOspfRedistributeMetric1 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 19, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfRedistributeMetric1.setStatus('current')
prvtOspfRedistributeMetric2 = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 19, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16777215))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfRedistributeMetric2.setStatus('current')
prvtOspfRedistributeRouteMap = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 19, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtOspfRedistributeRouteMap.setStatus('current')
prvtOspfRouterDataTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20), )
if mibBuilder.loadTexts: prvtOspfRouterDataTable.setStatus('current')
prvtOspfRouterDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1), ).setIndexNames((0, "PRVT-OSPF-MIB", "prvtOspfRouterDataPrefix"), (0, "PRVT-OSPF-MIB", "prvtOspfRouterDataType"), (0, "PRVT-OSPF-MIB", "prvtOspfRouterDataAreaId"))
if mibBuilder.loadTexts: prvtOspfRouterDataEntry.setStatus('current')
prvtOspfRouterDataPrefix = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(5, 5)).setFixedLength(5))
if mibBuilder.loadTexts: prvtOspfRouterDataPrefix.setStatus('current')
prvtOspfRouterDataType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("network", 1), ("router", 2), ("external", 3))))
if mibBuilder.loadTexts: prvtOspfRouterDataType.setStatus('current')
prvtOspfRouterDataAreaId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 3), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: prvtOspfRouterDataAreaId.setStatus('current')
prvtOspfRouterDataId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 4), IpAddress())
if mibBuilder.loadTexts: prvtOspfRouterDataId.setStatus('current')
prvtOspfRouterDataCost = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 5), Unsigned32())
if mibBuilder.loadTexts: prvtOspfRouterDataCost.setStatus('current')
prvtOspfRouterDataCostType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfRouterDataCostType.setStatus('current')
prvtOspfRouterDataDestType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("router", 1), ("network", 2), ("disables", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfRouterDataDestType.setStatus('current')
prvtOspfRouterDataPathType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("intraArea", 1), ("interArea", 2), ("external1", 3), ("external3", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfRouterDataPathType.setStatus('current')
prvtOspfRouterDataFlags = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 9), Bits().clone(namedValues=NamedValues(("abr", 0), ("asbr", 1), ("virtual", 2), ("unknown", 3), ("nssa", 4), ("shortcut", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfRouterDataFlags.setStatus('current')
prvtOspfRouterDataExternalRouting = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("default", 0), ("stub", 1), ("nssa", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfRouterDataExternalRouting.setStatus('current')
prvtOspfRouterDataTag = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 20, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfRouterDataTag.setStatus('current')
prvtOspfRouterPathTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 21), )
if mibBuilder.loadTexts: prvtOspfRouterPathTable.setStatus('current')
prvtOspfRouterPathEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 21, 1), ).setIndexNames((0, "PRVT-OSPF-MIB", "prvtOspfRouterDataPrefix"), (0, "PRVT-OSPF-MIB", "prvtOspfRouterDataType"), (0, "PRVT-OSPF-MIB", "prvtOspfRouterDataAreaId"), (0, "PRVT-OSPF-MIB", "prvtOspfRouterPathNextHop"))
if mibBuilder.loadTexts: prvtOspfRouterPathEntry.setStatus('current')
prvtOspfRouterPathNextHop = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 21, 1, 1), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: prvtOspfRouterPathNextHop.setStatus('current')
prvtOspfRouterPathAdvertisingRouter = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 21, 1, 2), OctetString().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfRouterPathAdvertisingRouter.setStatus('current')
prvtOspfRouterPathInterfaceName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 21, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtOspfRouterPathInterfaceName.setStatus('current')
prvtOspfTrafficEngEnable = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 4, 2, 1, 22), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtOspfTrafficEngEnable.setStatus('current')
mibBuilder.exportSymbols("PRVT-OSPF-MIB", prvtOspfAreaEntry=prvtOspfAreaEntry, prvtOspfRouterDataTable=prvtOspfRouterDataTable, prvtOspfMIB=prvtOspfMIB, prvtOspfIfAuthType=prvtOspfIfAuthType, prvtOspfNbrPriority=prvtOspfNbrPriority, prvtOspfIfWorkingMode=prvtOspfIfWorkingMode, prvtOspfRouterDataTag=prvtOspfRouterDataTag, prvtOspfAreaNssaTransitRole=prvtOspfAreaNssaTransitRole, prvtOspfRedistributeRowStatus=prvtOspfRedistributeRowStatus, prvtOspfRouterDataType=prvtOspfRouterDataType, prvtOspfRouterDataDestType=prvtOspfRouterDataDestType, prvtOspfRouterDataPrefix=prvtOspfRouterDataPrefix, prvtOspfRxNewLsas=prvtOspfRxNewLsas, prvtOspfRouterId=prvtOspfRouterId, prvtOspfExtLsdbAge=prvtOspfExtLsdbAge, PrvtOspfDesignatedRouterPriority=PrvtOspfDesignatedRouterPriority, prvtOspfRouterDataAreaId=prvtOspfRouterDataAreaId, prvtOspfLsdbLength=prvtOspfLsdbLength, prvtOspfIfEntry=prvtOspfIfEntry, prvtOspfExtLsdbTable=prvtOspfExtLsdbTable, prvtOspfMulticastExtensions=prvtOspfMulticastExtensions, prvtOspfAreaShortcutConfiguration=prvtOspfAreaShortcutConfiguration, prvtOspfExternLsaCount=prvtOspfExternLsaCount, prvtOspfIfTransitDelay=prvtOspfIfTransitDelay, prvtOspfIfRetransmitInterval=prvtOspfIfRetransmitInterval, prvtOspfNbrTable=prvtOspfNbrTable, prvtOspfRedistributeProtocol=prvtOspfRedistributeProtocol, prvtOspfExtLsdbChecksum=prvtOspfExtLsdbChecksum, prvtOspfLsdbAge=prvtOspfLsdbAge, prvtOspfNbrEvents=prvtOspfNbrEvents, prvtOspfExtLsdbLimit=prvtOspfExtLsdbLimit, prvtOspfAreaAuthType=prvtOspfAreaAuthType, prvtOspfRedistributeTable=prvtOspfRedistributeTable, prvtOspfRedistributeEntry=prvtOspfRedistributeEntry, prvtOspfIfAuthMd5Key=prvtOspfIfAuthMd5Key, prvtOspfRouterDataCostType=prvtOspfRouterDataCostType, PrvtOspfIpAddress=PrvtOspfIpAddress, prvtOspfRouterDataExternalRouting=prvtOspfRouterDataExternalRouting, prvtOspfAreaMetric=prvtOspfAreaMetric, prvtOspfAreaImportList=prvtOspfAreaImportList, prvtOspfAreaSummary=prvtOspfAreaSummary, prvtOspfIfType=prvtOspfIfType, prvtOspfRedistributeMetric1=prvtOspfRedistributeMetric1, prvtOspfExtLsdbAdvertisement=prvtOspfExtLsdbAdvertisement, prvtOspfRouterPathAdvertisingRouter=prvtOspfRouterPathAdvertisingRouter, prvtOspfExtLsdbLsid=prvtOspfExtLsdbLsid, prvtOspfAreaExportList=prvtOspfAreaExportList, prvtOspfLsdbTable=prvtOspfLsdbTable, prvtOspfRouterPathInterfaceName=prvtOspfRouterPathInterfaceName, prvtOspfLsdbChecksum=prvtOspfLsdbChecksum, prvtOspfExtLsdbSequence=prvtOspfExtLsdbSequence, prvtOspfObjects=prvtOspfObjects, prvtOspfNbmaNbrPermanence=prvtOspfNbmaNbrPermanence, prvtOspfIfIpAddress=prvtOspfIfIpAddress, prvtOspfVersionNumber=prvtOspfVersionNumber, prvtOspfRouterDataPathType=prvtOspfRouterDataPathType, prvtOspfNbrState=prvtOspfNbrState, prvtOspfLsdbRouterId=prvtOspfLsdbRouterId, prvtOspfIfAuthMd5RowStatus=prvtOspfIfAuthMd5RowStatus, prvtOspfRedistributeMetric2=prvtOspfRedistributeMetric2, prvtOspfRouterPathEntry=prvtOspfRouterPathEntry, prvtOspfRedistributeRouteMap=prvtOspfRedistributeRouteMap, prvtOspfNbrIpAddr=prvtOspfNbrIpAddr, prvtOspfDemandExtensions=prvtOspfDemandExtensions, prvtOspfAreaDefaultCost=prvtOspfAreaDefaultCost, prvtOspfRouterDataFlags=prvtOspfRouterDataFlags, prvtOspfRouterPathNextHop=prvtOspfRouterPathNextHop, prvtOspfAdminStat=prvtOspfAdminStat, prvtOspfAreaRowStatus=prvtOspfAreaRowStatus, prvtOspfNbrHelloSuppressed=prvtOspfNbrHelloSuppressed, prvtOspfAreaMetricType=prvtOspfAreaMetricType, PYSNMP_MODULE_ID=prvtOspfMIB, prvtOspfNbrRtrId=prvtOspfNbrRtrId, prvtOspfIfPriority=prvtOspfIfPriority, prvtOspfIfRowStatus=prvtOspfIfRowStatus, prvtOspfExtLsdbType=prvtOspfExtLsdbType, prvtOspfIfAuthMd5Word=prvtOspfIfAuthMd5Word, prvtOspfRouterPathTable=prvtOspfRouterPathTable, prvtOspfRouterDataEntry=prvtOspfRouterDataEntry, prvtOspfLsdbEntry=prvtOspfLsdbEntry, prvtOspfIfAreaId=prvtOspfIfAreaId, prvtOspfExtLsdbRouterId=prvtOspfExtLsdbRouterId, prvtOspfLsdbType=prvtOspfLsdbType, prvtOspfAreaType=prvtOspfAreaType, prvtOspfRouterDataCost=prvtOspfRouterDataCost, prvtOspfNbrAddressLessIndex=prvtOspfNbrAddressLessIndex, prvtOspfLsdbLsid=prvtOspfLsdbLsid, prvtOspfIfAuthMd5Table=prvtOspfIfAuthMd5Table, prvtOspfLsdbSequence=prvtOspfLsdbSequence, prvtOspfAreaId=prvtOspfAreaId, prvtOspfNbrEntry=prvtOspfNbrEntry, prvtOspfExitOverflowInterval=prvtOspfExitOverflowInterval, prvtOspfLsdbAdvertisement=prvtOspfLsdbAdvertisement, prvtOspfExtLsdbEntry=prvtOspfExtLsdbEntry, prvtOspfOriginateNewLsas=prvtOspfOriginateNewLsas, prvtOspfRouterDataId=prvtOspfRouterDataId, prvtOspfNbrOptions=prvtOspfNbrOptions, prvtOspfIfDeadTimer=prvtOspfIfDeadTimer, prvtOspfNbrLsRetransQLen=prvtOspfNbrLsRetransQLen, prvtOspfIfHelloTimer=prvtOspfIfHelloTimer, prvtOspfLsdbAreaId=prvtOspfLsdbAreaId, prvtOspfIfAuthSimple=prvtOspfIfAuthSimple, prvtOspfTOSSupport=prvtOspfTOSSupport, prvtOspfIfOutputCost=prvtOspfIfOutputCost, prvtOspfIfAuthMd5Entry=prvtOspfIfAuthMd5Entry, prvtOspfIfTable=prvtOspfIfTable, prvtOspfExternLsaCksumSum=prvtOspfExternLsaCksumSum, prvtOspfTrafficEngEnable=prvtOspfTrafficEngEnable, prvtOspfAreaTable=prvtOspfAreaTable)
