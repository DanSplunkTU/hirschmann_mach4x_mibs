#
# PySNMP MIB module DOCS-L2VPN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DOCS-L2VPN-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
dot1dBasePort, = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort")
clabProjDocsis, = mibBuilder.importSymbols("CLAB-DEF-MIB", "clabProjDocsis")
docsIfCmtsCmStatusIndex, = mibBuilder.importSymbols("DOCS-IF-MIB", "docsIfCmtsCmStatusIndex")
docsQosPktClassId, docsQosServiceFlowId = mibBuilder.importSymbols("DOCS-QOS-MIB", "docsQosPktClassId", "docsQosServiceFlowId")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
dot1qVlanIndex, dot1qFdbId, dot1qTpGroupAddress, dot1qTpFdbAddress = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex", "dot1qFdbId", "dot1qTpGroupAddress", "dot1qTpFdbAddress")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, Unsigned32, iso, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "iso", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
TextualConvention, MacAddress, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "TruthValue", "DisplayString")
docsL2vpnMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8))
docsL2vpnMIB.setRevisions(('2006-03-28 00:00',))
if mibBuilder.loadTexts: docsL2vpnMIB.setLastUpdated('200603280000Z')
if mibBuilder.loadTexts: docsL2vpnMIB.setOrganization('CableLabs')
class DocsL2vpnIdentifier(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class DocsL2vpnIndex(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class DocsNsiEncapSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("other", 1), ("ieee8021q", 2), ("ieee8021ad", 3), ("mpls", 4), ("l2tpv3", 5))

class DocsNsiEncapValue(TextualConvention, OctetString):
    status = 'current'

class DocsL2vpnIfList(TextualConvention, Bits):
    status = 'current'
    namedValues = NamedValues(("eCm", 0), ("cmci", 1), ("docsCableMacLayer", 2), ("docsCableDownstream", 3), ("docsCableUpstream", 4), ("eMta", 16), ("eStbIp", 17), ("eStbDsg", 18))

docsL2vpnMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 0))
docsL2vpnMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1))
docsL2vpnIdToIndexTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 1), )
if mibBuilder.loadTexts: docsL2vpnIdToIndexTable.setStatus('current')
docsL2vpnIdToIndexEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 1, 1), ).setIndexNames((0, "DOCS-L2VPN-MIB", "docsL2vpnId"))
if mibBuilder.loadTexts: docsL2vpnIdToIndexEntry.setStatus('current')
docsL2vpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 1, 1, 1), DocsL2vpnIdentifier())
if mibBuilder.loadTexts: docsL2vpnId.setStatus('current')
docsL2vpnIdToIndexIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 1, 1, 2), DocsL2vpnIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnIdToIndexIdx.setStatus('current')
docsL2vpnIndexToIdTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 2), )
if mibBuilder.loadTexts: docsL2vpnIndexToIdTable.setStatus('current')
docsL2vpnIndexToIdEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 2, 1), ).setIndexNames((0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"))
if mibBuilder.loadTexts: docsL2vpnIndexToIdEntry.setStatus('current')
docsL2vpnIdx = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 2, 1, 1), DocsL2vpnIndex())
if mibBuilder.loadTexts: docsL2vpnIdx.setStatus('current')
docsL2vpnIndexToIdId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 2, 1, 2), DocsL2vpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnIndexToIdId.setStatus('current')
docsL2vpnCmTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3), )
if mibBuilder.loadTexts: docsL2vpnCmTable.setStatus('current')
docsL2vpnCmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3, 1), ).setIndexNames((0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"))
if mibBuilder.loadTexts: docsL2vpnCmEntry.setStatus('current')
docsL2vpnCmCompliantCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnCmCompliantCapability.setStatus('current')
docsL2vpnCmDutFilteringCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnCmDutFilteringCapability.setStatus('current')
docsL2vpnCmDutCMIM = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3, 1, 3), DocsL2vpnIfList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnCmDutCMIM.setStatus('current')
docsL2vpnCmDhcpSnooping = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 3, 1, 4), DocsL2vpnIfList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnCmDhcpSnooping.setStatus('current')
docsL2vpnVpnCmTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 4), )
if mibBuilder.loadTexts: docsL2vpnVpnCmTable.setStatus('current')
docsL2vpnVpnCmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 4, 1), ).setIndexNames((0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"), (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"))
if mibBuilder.loadTexts: docsL2vpnVpnCmEntry.setStatus('current')
docsL2vpnVpnCmCMIM = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 4, 1, 1), DocsL2vpnIfList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnVpnCmCMIM.setStatus('current')
docsL2vpnVpnCmIndividualSAId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16383))).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnVpnCmIndividualSAId.setStatus('current')
docsL2vpnVpnCmVendorSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 4, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnVpnCmVendorSpecific.setStatus('current')
docsL2vpnVpnCmStatsTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5), )
if mibBuilder.loadTexts: docsL2vpnVpnCmStatsTable.setStatus('current')
docsL2vpnVpnCmStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1), ).setIndexNames((0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"), (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"))
if mibBuilder.loadTexts: docsL2vpnVpnCmStatsEntry.setStatus('current')
docsL2vpnVpnCmStatsUpstreamPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnVpnCmStatsUpstreamPkts.setStatus('current')
docsL2vpnVpnCmStatsUpstreamBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnVpnCmStatsUpstreamBytes.setStatus('current')
docsL2vpnVpnCmStatsUpstreamDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnVpnCmStatsUpstreamDiscards.setStatus('current')
docsL2vpnVpnCmStatsDownstreamPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnVpnCmStatsDownstreamPkts.setStatus('current')
docsL2vpnVpnCmStatsDownstreamBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnVpnCmStatsDownstreamBytes.setStatus('current')
docsL2vpnVpnCmStatsDownstreamDiscards = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 5, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnVpnCmStatsDownstreamDiscards.setStatus('current')
docsL2vpnPortStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 6), )
if mibBuilder.loadTexts: docsL2vpnPortStatusTable.setStatus('current')
docsL2vpnPortStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 6, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"))
if mibBuilder.loadTexts: docsL2vpnPortStatusEntry.setStatus('current')
docsL2vpnPortStatusGroupSAId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 16383))).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnPortStatusGroupSAId.setStatus('current')
docsL2vpnSfStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 7), )
if mibBuilder.loadTexts: docsL2vpnSfStatusTable.setStatus('current')
docsL2vpnSfStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 7, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOCS-QOS-MIB", "docsQosServiceFlowId"))
if mibBuilder.loadTexts: docsL2vpnSfStatusEntry.setStatus('current')
docsL2vpnSfStatusL2vpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 7, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnSfStatusL2vpnId.setStatus('current')
docsL2vpnSfStatusIngressUserPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 7, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnSfStatusIngressUserPriority.setStatus('current')
docsL2vpnSfStatusVendorSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 7, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnSfStatusVendorSpecific.setStatus('current')
docsL2vpnPktClassTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8), )
if mibBuilder.loadTexts: docsL2vpnPktClassTable.setStatus('current')
docsL2vpnPktClassEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "DOCS-QOS-MIB", "docsQosServiceFlowId"), (0, "DOCS-QOS-MIB", "docsQosPktClassId"))
if mibBuilder.loadTexts: docsL2vpnPktClassEntry.setStatus('current')
docsL2vpnPktClassL2vpnId = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1, 1), DocsL2vpnIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnPktClassL2vpnId.setStatus('current')
docsL2vpnPktClassUserPriRangeLow = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnPktClassUserPriRangeLow.setStatus('current')
docsL2vpnPktClassUserPriRangeHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnPktClassUserPriRangeHigh.setStatus('current')
docsL2vpnPktClassCMIM = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1, 4), DocsL2vpnIfList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnPktClassCMIM.setStatus('current')
docsL2vpnPktClassVendorSpecific = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 8, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnPktClassVendorSpecific.setStatus('current')
docsL2vpnCmNsiTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9), )
if mibBuilder.loadTexts: docsL2vpnCmNsiTable.setStatus('current')
docsL2vpnCmNsiEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1), ).setIndexNames((0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"), (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"))
if mibBuilder.loadTexts: docsL2vpnCmNsiEntry.setStatus('current')
docsL2vpnCmNsiEncapSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1, 1), DocsNsiEncapSubtype()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnCmNsiEncapSubtype.setStatus('current')
docsL2vpnCmNsiEncapValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1, 2), DocsNsiEncapValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnCmNsiEncapValue.setStatus('current')
docsL2vpnCmNsiAGI = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnCmNsiAGI.setStatus('current')
docsL2vpnCmNsiSAII = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnCmNsiSAII.setStatus('current')
docsL2vpnCmNsiTAII = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 9, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnCmNsiTAII.setStatus('current')
docsL2vpnCmVpnCpeTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 10), )
if mibBuilder.loadTexts: docsL2vpnCmVpnCpeTable.setStatus('current')
docsL2vpnCmVpnCpeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 10, 1), ).setIndexNames((0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"), (0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"), (0, "DOCS-L2VPN-MIB", "docsL2vpnCmVpnCpeMacAddress"))
if mibBuilder.loadTexts: docsL2vpnCmVpnCpeEntry.setStatus('current')
docsL2vpnCmVpnCpeMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 10, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnCmVpnCpeMacAddress.setStatus('current')
docsL2vpnVpnCmCpeTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 11), )
if mibBuilder.loadTexts: docsL2vpnVpnCmCpeTable.setStatus('current')
docsL2vpnVpnCmCpeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 11, 1), ).setIndexNames((0, "DOCS-L2VPN-MIB", "docsL2vpnIdx"), (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"), (0, "DOCS-L2VPN-MIB", "docsL2vpnVpnCmCpeMacAddress"))
if mibBuilder.loadTexts: docsL2vpnVpnCmCpeEntry.setStatus('current')
docsL2vpnVpnCmCpeMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 11, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnVpnCmCpeMacAddress.setStatus('current')
docsL2vpnDot1qTpFdbExtTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 12), )
if mibBuilder.loadTexts: docsL2vpnDot1qTpFdbExtTable.setStatus('current')
docsL2vpnDot1qTpFdbExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 12, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"))
if mibBuilder.loadTexts: docsL2vpnDot1qTpFdbExtEntry.setStatus('current')
docsL2vpnDot1qTpFdbExtTransmitPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 12, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnDot1qTpFdbExtTransmitPkts.setStatus('current')
docsL2vpnDot1qTpFdbExtReceivePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 12, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnDot1qTpFdbExtReceivePkts.setStatus('current')
docsL2vpnDot1qTpGroupExtTable = MibTable((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 13), )
if mibBuilder.loadTexts: docsL2vpnDot1qTpGroupExtTable.setStatus('current')
docsL2vpnDot1qTpGroupExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 13, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qVlanIndex"), (0, "Q-BRIDGE-MIB", "dot1qTpGroupAddress"))
if mibBuilder.loadTexts: docsL2vpnDot1qTpGroupExtEntry.setStatus('current')
docsL2vpnDot1qTpGroupExtTransmitPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 13, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnDot1qTpGroupExtTransmitPkts.setStatus('current')
docsL2vpnDot1qTpGroupExtReceivePkts = MibTableColumn((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 1, 13, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: docsL2vpnDot1qTpGroupExtReceivePkts.setStatus('current')
docsL2vpnConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2))
docsL2vpnCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 1))
docsL2vpnGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 2))
docsL2vpnCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 1, 1)).setObjects(("DOCS-L2VPN-MIB", "docsL2vpnBaseGroup"), ("DOCS-L2VPN-MIB", "docsL2vpnPointToPointGroup"), ("DOCS-L2VPN-MIB", "docsL2vpnMultipointGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsL2vpnCompliance = docsL2vpnCompliance.setStatus('current')
docsL2vpnBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 2, 1)).setObjects(("DOCS-L2VPN-MIB", "docsL2vpnIdToIndexIdx"), ("DOCS-L2VPN-MIB", "docsL2vpnIndexToIdId"), ("DOCS-L2VPN-MIB", "docsL2vpnCmCompliantCapability"), ("DOCS-L2VPN-MIB", "docsL2vpnCmDutFilteringCapability"), ("DOCS-L2VPN-MIB", "docsL2vpnCmDutCMIM"), ("DOCS-L2VPN-MIB", "docsL2vpnCmDhcpSnooping"), ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmCMIM"), ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmVendorSpecific"), ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmIndividualSAId"), ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsUpstreamPkts"), ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsUpstreamBytes"), ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsUpstreamDiscards"), ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsDownstreamPkts"), ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsDownstreamBytes"), ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmStatsDownstreamDiscards"), ("DOCS-L2VPN-MIB", "docsL2vpnPortStatusGroupSAId"), ("DOCS-L2VPN-MIB", "docsL2vpnSfStatusL2vpnId"), ("DOCS-L2VPN-MIB", "docsL2vpnSfStatusIngressUserPriority"), ("DOCS-L2VPN-MIB", "docsL2vpnSfStatusVendorSpecific"), ("DOCS-L2VPN-MIB", "docsL2vpnPktClassL2vpnId"), ("DOCS-L2VPN-MIB", "docsL2vpnPktClassUserPriRangeLow"), ("DOCS-L2VPN-MIB", "docsL2vpnPktClassUserPriRangeHigh"), ("DOCS-L2VPN-MIB", "docsL2vpnPktClassCMIM"), ("DOCS-L2VPN-MIB", "docsL2vpnPktClassVendorSpecific"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsL2vpnBaseGroup = docsL2vpnBaseGroup.setStatus('current')
docsL2vpnPointToPointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 2, 2)).setObjects(("DOCS-L2VPN-MIB", "docsL2vpnCmNsiEncapSubtype"), ("DOCS-L2VPN-MIB", "docsL2vpnCmNsiEncapValue"), ("DOCS-L2VPN-MIB", "docsL2vpnCmNsiAGI"), ("DOCS-L2VPN-MIB", "docsL2vpnCmNsiSAII"), ("DOCS-L2VPN-MIB", "docsL2vpnCmNsiTAII"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsL2vpnPointToPointGroup = docsL2vpnPointToPointGroup.setStatus('current')
docsL2vpnMultipointGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4491, 2, 1, 8, 2, 2, 3)).setObjects(("DOCS-L2VPN-MIB", "docsL2vpnCmVpnCpeMacAddress"), ("DOCS-L2VPN-MIB", "docsL2vpnVpnCmCpeMacAddress"), ("DOCS-L2VPN-MIB", "docsL2vpnDot1qTpFdbExtTransmitPkts"), ("DOCS-L2VPN-MIB", "docsL2vpnDot1qTpFdbExtReceivePkts"), ("DOCS-L2VPN-MIB", "docsL2vpnDot1qTpGroupExtTransmitPkts"), ("DOCS-L2VPN-MIB", "docsL2vpnDot1qTpGroupExtReceivePkts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    docsL2vpnMultipointGroup = docsL2vpnMultipointGroup.setStatus('current')
mibBuilder.exportSymbols("DOCS-L2VPN-MIB", docsL2vpnPktClassEntry=docsL2vpnPktClassEntry, docsL2vpnPktClassUserPriRangeLow=docsL2vpnPktClassUserPriRangeLow, docsL2vpnId=docsL2vpnId, docsL2vpnCmNsiTable=docsL2vpnCmNsiTable, docsL2vpnVpnCmCpeEntry=docsL2vpnVpnCmCpeEntry, DocsNsiEncapSubtype=DocsNsiEncapSubtype, docsL2vpnCmDutCMIM=docsL2vpnCmDutCMIM, DocsL2vpnIfList=DocsL2vpnIfList, docsL2vpnIndexToIdTable=docsL2vpnIndexToIdTable, docsL2vpnVpnCmStatsUpstreamPkts=docsL2vpnVpnCmStatsUpstreamPkts, docsL2vpnPointToPointGroup=docsL2vpnPointToPointGroup, docsL2vpnPktClassTable=docsL2vpnPktClassTable, docsL2vpnDot1qTpFdbExtReceivePkts=docsL2vpnDot1qTpFdbExtReceivePkts, docsL2vpnCmNsiEntry=docsL2vpnCmNsiEntry, docsL2vpnVpnCmStatsDownstreamDiscards=docsL2vpnVpnCmStatsDownstreamDiscards, docsL2vpnVpnCmTable=docsL2vpnVpnCmTable, docsL2vpnCmTable=docsL2vpnCmTable, docsL2vpnMultipointGroup=docsL2vpnMultipointGroup, docsL2vpnCmNsiEncapSubtype=docsL2vpnCmNsiEncapSubtype, PYSNMP_MODULE_ID=docsL2vpnMIB, docsL2vpnMIB=docsL2vpnMIB, docsL2vpnCmDutFilteringCapability=docsL2vpnCmDutFilteringCapability, docsL2vpnVpnCmEntry=docsL2vpnVpnCmEntry, docsL2vpnCmCompliantCapability=docsL2vpnCmCompliantCapability, docsL2vpnSfStatusVendorSpecific=docsL2vpnSfStatusVendorSpecific, DocsNsiEncapValue=DocsNsiEncapValue, docsL2vpnPktClassCMIM=docsL2vpnPktClassCMIM, docsL2vpnPktClassVendorSpecific=docsL2vpnPktClassVendorSpecific, docsL2vpnCmNsiSAII=docsL2vpnCmNsiSAII, docsL2vpnDot1qTpGroupExtEntry=docsL2vpnDot1qTpGroupExtEntry, docsL2vpnIndexToIdEntry=docsL2vpnIndexToIdEntry, docsL2vpnVpnCmStatsEntry=docsL2vpnVpnCmStatsEntry, docsL2vpnVpnCmCpeTable=docsL2vpnVpnCmCpeTable, docsL2vpnVpnCmStatsTable=docsL2vpnVpnCmStatsTable, docsL2vpnSfStatusIngressUserPriority=docsL2vpnSfStatusIngressUserPriority, docsL2vpnDot1qTpGroupExtReceivePkts=docsL2vpnDot1qTpGroupExtReceivePkts, docsL2vpnVpnCmStatsDownstreamBytes=docsL2vpnVpnCmStatsDownstreamBytes, docsL2vpnIndexToIdId=docsL2vpnIndexToIdId, docsL2vpnSfStatusEntry=docsL2vpnSfStatusEntry, docsL2vpnDot1qTpFdbExtTransmitPkts=docsL2vpnDot1qTpFdbExtTransmitPkts, docsL2vpnCmVpnCpeMacAddress=docsL2vpnCmVpnCpeMacAddress, docsL2vpnCmNsiAGI=docsL2vpnCmNsiAGI, docsL2vpnBaseGroup=docsL2vpnBaseGroup, docsL2vpnIdx=docsL2vpnIdx, docsL2vpnMIBObjects=docsL2vpnMIBObjects, DocsL2vpnIndex=DocsL2vpnIndex, docsL2vpnCompliances=docsL2vpnCompliances, docsL2vpnCmEntry=docsL2vpnCmEntry, docsL2vpnIdToIndexEntry=docsL2vpnIdToIndexEntry, docsL2vpnVpnCmStatsUpstreamBytes=docsL2vpnVpnCmStatsUpstreamBytes, docsL2vpnCmNsiTAII=docsL2vpnCmNsiTAII, docsL2vpnVpnCmStatsDownstreamPkts=docsL2vpnVpnCmStatsDownstreamPkts, docsL2vpnCmVpnCpeEntry=docsL2vpnCmVpnCpeEntry, docsL2vpnVpnCmCpeMacAddress=docsL2vpnVpnCmCpeMacAddress, docsL2vpnCmDhcpSnooping=docsL2vpnCmDhcpSnooping, docsL2vpnCompliance=docsL2vpnCompliance, docsL2vpnGroups=docsL2vpnGroups, docsL2vpnDot1qTpGroupExtTable=docsL2vpnDot1qTpGroupExtTable, docsL2vpnVpnCmCMIM=docsL2vpnVpnCmCMIM, docsL2vpnPortStatusEntry=docsL2vpnPortStatusEntry, docsL2vpnPortStatusGroupSAId=docsL2vpnPortStatusGroupSAId, docsL2vpnDot1qTpFdbExtEntry=docsL2vpnDot1qTpFdbExtEntry, DocsL2vpnIdentifier=DocsL2vpnIdentifier, docsL2vpnIdToIndexTable=docsL2vpnIdToIndexTable, docsL2vpnSfStatusTable=docsL2vpnSfStatusTable, docsL2vpnDot1qTpGroupExtTransmitPkts=docsL2vpnDot1qTpGroupExtTransmitPkts, docsL2vpnCmVpnCpeTable=docsL2vpnCmVpnCpeTable, docsL2vpnVpnCmVendorSpecific=docsL2vpnVpnCmVendorSpecific, docsL2vpnPktClassUserPriRangeHigh=docsL2vpnPktClassUserPriRangeHigh, docsL2vpnPktClassL2vpnId=docsL2vpnPktClassL2vpnId, docsL2vpnCmNsiEncapValue=docsL2vpnCmNsiEncapValue, docsL2vpnVpnCmIndividualSAId=docsL2vpnVpnCmIndividualSAId, docsL2vpnIdToIndexIdx=docsL2vpnIdToIndexIdx, docsL2vpnConformance=docsL2vpnConformance, docsL2vpnSfStatusL2vpnId=docsL2vpnSfStatusL2vpnId, docsL2vpnVpnCmStatsUpstreamDiscards=docsL2vpnVpnCmStatsUpstreamDiscards, docsL2vpnDot1qTpFdbExtTable=docsL2vpnDot1qTpFdbExtTable, docsL2vpnMIBNotifications=docsL2vpnMIBNotifications, docsL2vpnPortStatusTable=docsL2vpnPortStatusTable)
