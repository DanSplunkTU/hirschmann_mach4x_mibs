#
# PySNMP MIB module IEEE8021-ECMP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/iee/IEEE8021-ECMP-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:23 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ieee8021BridgeBasePort, ieee8021BridgeBasePortComponentId = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort", "ieee8021BridgeBasePortComponentId")
ieee8021QBridgeTpFdbEntry, ieee8021QBridgePortVlanStatisticsEntry = mibBuilder.importSymbols("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeTpFdbEntry", "ieee8021QBridgePortVlanStatisticsEntry")
IEEE8021SpbBridgePriority, ieee8021SpbTopIx, ieee8021SpbmTopSrvTableEntry = mibBuilder.importSymbols("IEEE8021-SPB-MIB", "IEEE8021SpbBridgePriority", "ieee8021SpbTopIx", "ieee8021SpbmTopSrvTableEntry")
ieee802dot1mibs, = mibBuilder.importSymbols("IEEE8021-TC-MIB", "ieee802dot1mibs")
PortList, VlanId = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList", "VlanId")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, NotificationType, IpAddress, Counter32, Bits, Counter64, Gauge32, TimeTicks, ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "NotificationType", "IpAddress", "Counter32", "Bits", "Counter64", "Gauge32", "TimeTicks", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
ieee8021EcmpMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 28))
ieee8021EcmpMib.setRevisions(('2018-06-28 00:00', '2014-12-15 00:00', '2013-05-13 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021EcmpMib.setRevisionsDescriptions(('Published as part of IEEE Std 802.1Q 2017 revision.\n            Cross references updated and corrected.\n            Description replaced.', 'Incorporated into IEEE Std 802.1Q 2014 Revision.\n                 Cross-references and front matter updated.', '802.1 Equal Cost Multiple Paths MIB Initial Version',))
if mibBuilder.loadTexts: ieee8021EcmpMib.setLastUpdated('201806280000Z')
if mibBuilder.loadTexts: ieee8021EcmpMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021EcmpMib.setContactInfo('WG-URL:   http://www.ieee802.org/1/\n         WG-EMail: stds-802-1-L@ieee.org\n\n          Contact: IEEE 802.1 Working Group Chair\n           Postal: C/O IEEE 802.1 Working Group\n                   IEEE Standards Association\n                   445 Hoes Lane\n                   Piscataway\n                   NJ 08854\n                   USA\n           E-mail: STDS-802-1-L@IEEE.ORG')
if mibBuilder.loadTexts: ieee8021EcmpMib.setDescription('MIB Module for managing systems that provide\n         802.1Q Equal Cost Multiple Paths.\n\n         Unless otherwise indicated, the references in this MIB\n         module are to IEEE Std 802.1Q.\n\n         Copyright (C) IEEE (2018).\n         This version of this MIB module is part of IEEE Std 802.1Q;\n         see the draft itself for full legal notices.')
ieee8021EcmpNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 28, 0))
ieee8021EcmpObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 28, 1))
ieee8021EcmpConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 28, 2))
ieee8021QBridgeEcmpFdbTable = MibTable((1, 3, 111, 2, 802, 1, 1, 28, 1, 1), )
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbTable.setReference('12.7.7.3, 8.8.3:c')
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbTable.setDescription('A table that contains information about unicast entries\n        for which the device has forwarding and/or filtering\n        information.  This information is used by the\n        ECMP next hop selection function in determining how to\n        propagate a received frame.')
ieee8021QBridgeEcmpFdbEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 28, 1, 1, 1), )
ieee8021QBridgeTpFdbEntry.registerAugmentions(("IEEE8021-ECMP-MIB", "ieee8021QBridgeEcmpFdbEntry"))
ieee8021QBridgeEcmpFdbEntry.setIndexNames(*ieee8021QBridgeTpFdbEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbEntry.setDescription('Information about a specific unicast MAC address for\n        which the device has some forwarding and/or filtering\n        information.')
ieee8021QBridgeEcmpFdbPortList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 1, 1, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbPortList.setStatus('current')
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbPortList.setDescription('The complete set of ports, in this FID, to which\n         frames destined for this individual MAC address may be\n         forwarded.')
ieee8021EcmpFlowFilterCtlTable = MibTable((1, 3, 111, 2, 802, 1, 1, 28, 1, 2), )
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlTable.setReference('12.16.5.4, 12.16.5.5')
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlTable.setDescription('A table flow filtering control informmation for ports\n         in a Bridge supporting F-Tag processing.')
ieee8021EcmpFlowFilterCtlEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePortComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlVid"))
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlEntry.setDescription('An entry in the Flow Filtering Control Table for a\n         port (CPB or PNP).')
ieee8021EcmpFlowFilterCtlVid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 1), VlanId())
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlVid.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlVid.setDescription('A B-vID registered on the port.')
ieee8021EcmpFlowFilterCtlEnabled = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlEnabled.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlEnabled.setDescription('Indicates whether or not flow filtering behavior\n         is enabled on the port for the VID\n         (true(1) is enabled, false(2) is disabled).')
ieee8021EcmpFlowFilterCtlHashGen = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlHashGen.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlHashGen.setDescription('indicates whether or not flow hash generation\n         is enabled on the port for the VID\n         (true(1) is enabled, false(2) is disabled).')
ieee8021EcmpFlowFilterCtlTtl = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 63))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlTtl.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlTtl.setDescription('the initial TTL value for frames entering\n         the flow filtering SPT Domain.\n         Valid values are 1..63, zero indicates the\n         value has not been set.\n         This object is persistent.')
ieee8021EcmpEctStaticTable = MibTable((1, 3, 111, 2, 802, 1, 1, 28, 1, 3), )
if mibBuilder.loadTexts: ieee8021EcmpEctStaticTable.setReference('12.25.14')
if mibBuilder.loadTexts: ieee8021EcmpEctStaticTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpEctStaticTable.setDescription('Table containing alternate Bridge priorities for tie-breaker\n         masks used in selecting shared tree root bridges.\n         The table is indexed by\n         - ieee8021SpbTopIx from ieee8021SpbMtidStaticTable\n             indicating the ISIS-SPB topology instance into\n             which the bridge priority will be advertised, and\n         - ieee8021EcmpEctStaticEntryTieBreakMask\n             the associated tie-break mask value.')
ieee8021EcmpEctStaticEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1), ).setIndexNames((0, "IEEE8021-SPB-MIB", "ieee8021SpbTopIx"), (0, "IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticEntryTieBreakMask"))
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntry.setReference('12.25.8')
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntry.setDescription('This entry contains information about backbone services\n         configured on this system to be advertised by ISIS-SPB.')
ieee8021EcmpEctStaticEntryTieBreakMask = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15)))
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntryTieBreakMask.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntryTieBreakMask.setDescription('The value used to create the Tie-Break Mask\n         for selecting a shared tree root bridge.')
ieee8021EcmpEctStaticEntryBridgePriority = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1, 2), IEEE8021SpbBridgePriority()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntryBridgePriority.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntryBridgePriority.setDescription('A Bridge Priority value to be used\n         for selecting a shared tree root bridge,\n         i.e., the most significant 4 bits of the\n         Bridge Identifier.\n         This object is persistent.')
ieee8021EcmpEctStaticEntryRowStatus = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 3, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntryRowStatus.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpEctStaticEntryRowStatus.setDescription('This column holds the status for this row.\n\n         When the status is active, no columns of this table may be\n         modified.  All columns must have a valid value before the row\n         can be activated.\n         This object is persistent.')
ieee8021EcmpTopSrvTable = MibTable((1, 3, 111, 2, 802, 1, 1, 28, 1, 4), )
if mibBuilder.loadTexts: ieee8021EcmpTopSrvTable.setReference('12.25.8')
if mibBuilder.loadTexts: ieee8021EcmpTopSrvTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpTopSrvTable.setDescription('Added info for SPBM PBB encapsulated services in this network.')
ieee8021EcmpTopSrvEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 28, 1, 4, 1), )
if mibBuilder.loadTexts: ieee8021EcmpTopSrvEntry.setReference('12.25.8')
ieee8021SpbmTopSrvTableEntry.registerAugmentions(("IEEE8021-ECMP-MIB", "ieee8021EcmpTopSrvEntry"))
ieee8021EcmpTopSrvEntry.setIndexNames(*ieee8021SpbmTopSrvTableEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021EcmpTopSrvEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpTopSrvEntry.setDescription('This table contains additional information about backbone\n         services configured on this system to be advertised by\n         ISIS-SPB.')
ieee8021EcmpTopSrvEntryTsBit = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 4, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021EcmpTopSrvEntryTsBit.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpTopSrvEntryTsBit.setDescription('If true(1), indicates the BSI transmits multicast\n         frames on a shared tree from this CBP.')
ieee8021EcmpTopSrvEntryTieBreakMask = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 15))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021EcmpTopSrvEntryTieBreakMask.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpTopSrvEntryTieBreakMask.setDescription('The value used to create the Tie-Break Mask\n         for calculating multicast trees.')
ieee8021QBridgePortVlanTtlStatisticsTable = MibTable((1, 3, 111, 2, 802, 1, 1, 28, 1, 5), )
if mibBuilder.loadTexts: ieee8021QBridgePortVlanTtlStatisticsTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021QBridgePortVlanTtlStatisticsTable.setDescription('A table containing per-port, per-VID TTL discard statistics.')
ieee8021QBridgePortVlanTtlStatisticsEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 28, 1, 5, 1), )
ieee8021QBridgePortVlanStatisticsEntry.registerAugmentions(("IEEE8021-ECMP-MIB", "ieee8021QBridgePortVlanTtlStatisticsEntry"))
ieee8021QBridgePortVlanTtlStatisticsEntry.setIndexNames(*ieee8021QBridgePortVlanStatisticsEntry.getIndexNames())
if mibBuilder.loadTexts: ieee8021QBridgePortVlanTtlStatisticsEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021QBridgePortVlanTtlStatisticsEntry.setDescription('TTL discard statistics for a VID on an interface.')
ieee8021QBridgeTpVlanPortTtlDiscards = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 28, 1, 5, 1, 1), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021QBridgeTpVlanPortTtlDiscards.setReference('12.6.1.1.3')
if mibBuilder.loadTexts: ieee8021QBridgeTpVlanPortTtlDiscards.setStatus('current')
if mibBuilder.loadTexts: ieee8021QBridgeTpVlanPortTtlDiscards.setDescription('The number of valid frames received by this port from\n        its segment that were classified as belonging to this\n        VLAN and that were discarded due to TTL expiry.\n        Discontinuities in the value of the counter can occur\n        at re-initialization of the management system, and at\n        other times as indicated by the value of\n        ifCounterDiscontinuityTime object of the associated\n        interface (if any).')
ieee8021EcmpGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 28, 2, 1))
ieee8021EcmpCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 28, 2, 2))
ieee8021QBridgeEcmpFdbGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 1)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021QBridgeEcmpFdbPortList"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021QBridgeEcmpFdbGroup = ieee8021QBridgeEcmpFdbGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021QBridgeEcmpFdbGroup.setDescription('FDB Port Map for ECMP Individual address')
ieee8021EcmpFlowFilterCtlGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 2)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlEnabled"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlHashGen"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlTtl"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021EcmpFlowFilterCtlGroup = ieee8021EcmpFlowFilterCtlGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpFlowFilterCtlGroup.setDescription('Flow filtering control parameters on a CBP or PNP')
ieee8021EcmpEctStaticGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 3)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticEntryBridgePriority"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticEntryRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021EcmpEctStaticGroup = ieee8021EcmpEctStaticGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpEctStaticGroup.setDescription('Optional Bridge Priority for selecting shared tree root')
ieee8021EcmpTopSrvGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 4)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021EcmpTopSrvEntryTsBit"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpTopSrvEntryTieBreakMask"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021EcmpTopSrvGroup = ieee8021EcmpTopSrvGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpTopSrvGroup.setDescription('Advertised I-SID parameters controlling multicast routing')
ieee8021QBridgePortVlanTtlStatisticsGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 28, 2, 1, 5)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021QBridgeTpVlanPortTtlDiscards"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021QBridgePortVlanTtlStatisticsGroup = ieee8021QBridgePortVlanTtlStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021QBridgePortVlanTtlStatisticsGroup.setDescription('TTL discard statistics')
ieee8021EcmpCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 28, 2, 2, 1)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021QBridgeEcmpFdbGroup"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpEctStaticGroup"), ("IEEE8021-ECMP-MIB", "ieee8021EcmpTopSrvGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021EcmpCompliance = ieee8021EcmpCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpCompliance.setDescription('Compliance to IEEE 802.1 SPBM ECMP')
ieee8021EcmpFlowFilteringCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 28, 2, 2, 2)).setObjects(("IEEE8021-ECMP-MIB", "ieee8021EcmpFlowFilterCtlGroup"), ("IEEE8021-ECMP-MIB", "ieee8021QBridgePortVlanTtlStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021EcmpFlowFilteringCompliance = ieee8021EcmpFlowFilteringCompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021EcmpFlowFilteringCompliance.setDescription('Compliance to IEEE 802.1 SPBM ECMP with flow filtering')
mibBuilder.exportSymbols("IEEE8021-ECMP-MIB", ieee8021QBridgeEcmpFdbPortList=ieee8021QBridgeEcmpFdbPortList, ieee8021EcmpFlowFilterCtlHashGen=ieee8021EcmpFlowFilterCtlHashGen, ieee8021EcmpConformance=ieee8021EcmpConformance, ieee8021EcmpFlowFilterCtlEntry=ieee8021EcmpFlowFilterCtlEntry, ieee8021EcmpTopSrvGroup=ieee8021EcmpTopSrvGroup, ieee8021EcmpMib=ieee8021EcmpMib, ieee8021EcmpEctStaticEntryRowStatus=ieee8021EcmpEctStaticEntryRowStatus, ieee8021EcmpGroups=ieee8021EcmpGroups, ieee8021QBridgePortVlanTtlStatisticsTable=ieee8021QBridgePortVlanTtlStatisticsTable, ieee8021EcmpEctStaticEntryBridgePriority=ieee8021EcmpEctStaticEntryBridgePriority, ieee8021QBridgePortVlanTtlStatisticsGroup=ieee8021QBridgePortVlanTtlStatisticsGroup, ieee8021EcmpFlowFilterCtlVid=ieee8021EcmpFlowFilterCtlVid, ieee8021EcmpFlowFilterCtlTable=ieee8021EcmpFlowFilterCtlTable, ieee8021QBridgeEcmpFdbEntry=ieee8021QBridgeEcmpFdbEntry, ieee8021EcmpObjects=ieee8021EcmpObjects, ieee8021EcmpEctStaticEntryTieBreakMask=ieee8021EcmpEctStaticEntryTieBreakMask, ieee8021EcmpTopSrvEntryTsBit=ieee8021EcmpTopSrvEntryTsBit, ieee8021EcmpFlowFilterCtlTtl=ieee8021EcmpFlowFilterCtlTtl, ieee8021EcmpEctStaticTable=ieee8021EcmpEctStaticTable, ieee8021QBridgeTpVlanPortTtlDiscards=ieee8021QBridgeTpVlanPortTtlDiscards, ieee8021EcmpTopSrvEntry=ieee8021EcmpTopSrvEntry, ieee8021EcmpTopSrvTable=ieee8021EcmpTopSrvTable, ieee8021EcmpCompliance=ieee8021EcmpCompliance, ieee8021EcmpFlowFilteringCompliance=ieee8021EcmpFlowFilteringCompliance, ieee8021EcmpEctStaticGroup=ieee8021EcmpEctStaticGroup, ieee8021QBridgeEcmpFdbTable=ieee8021QBridgeEcmpFdbTable, ieee8021EcmpNotifications=ieee8021EcmpNotifications, ieee8021EcmpCompliances=ieee8021EcmpCompliances, ieee8021EcmpTopSrvEntryTieBreakMask=ieee8021EcmpTopSrvEntryTieBreakMask, ieee8021EcmpEctStaticEntry=ieee8021EcmpEctStaticEntry, ieee8021QBridgeEcmpFdbGroup=ieee8021QBridgeEcmpFdbGroup, PYSNMP_MODULE_ID=ieee8021EcmpMib, ieee8021EcmpFlowFilterCtlEnabled=ieee8021EcmpFlowFilterCtlEnabled, ieee8021QBridgePortVlanTtlStatisticsEntry=ieee8021QBridgePortVlanTtlStatisticsEntry, ieee8021EcmpFlowFilterCtlGroup=ieee8021EcmpFlowFilterCtlGroup)
