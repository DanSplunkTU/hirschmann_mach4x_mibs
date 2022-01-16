#
# PySNMP MIB module F3-PBB-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adva/F3-PBB-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:30 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
PerfCounter64, = mibBuilder.importSymbols("CM-COMMON-MIB", "PerfCounter64")
cmFlowEntry, FlowTagControl, cmEthernetNetPortEntry, cmEthernetAccPortEntry = mibBuilder.importSymbols("CM-FACILITY-MIB", "cmFlowEntry", "FlowTagControl", "cmEthernetNetPortEntry", "cmEthernetAccPortEntry")
ipManagementTunnelEntry, = mibBuilder.importSymbols("CM-IP-MIB", "ipManagementTunnelEntry")
cmEthernetNetPortStatsEntry, cmEthernetNetPortHistoryEntry = mibBuilder.importSymbols("CM-PERFORMANCE-MIB", "cmEthernetNetPortStatsEntry", "cmEthernetNetPortHistoryEntry")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Counter32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, MibIdentifier, Integer32, NotificationType, ModuleIdentity, iso, Counter64, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "MibIdentifier", "Integer32", "NotificationType", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity")
TruthValue, DisplayString, TextualConvention, MacAddress, VariablePointer = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DisplayString", "TextualConvention", "MacAddress", "VariablePointer")
f3PBBMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21))
f3PBBMIB.setRevisions(('2012-10-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: f3PBBMIB.setRevisionsDescriptions(('Notes from release 201210080000Z. ',))
if mibBuilder.loadTexts: f3PBBMIB.setLastUpdated('201210080000Z')
if mibBuilder.loadTexts: f3PBBMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: f3PBBMIB.setContactInfo('        Raghav Trivedi\n                     ADVA Optical Networking, Inc.\n                Tel: +1 972 759-1239\n             E-mail: rtrivedi@advaoptical.com\n             Postal: 2301 N. Greenville Ave. #300\n                     Richardson, TX USA 75082')
if mibBuilder.loadTexts: f3PBBMIB.setDescription('This module defines the Facility MIB definitions used by \n             the F3 (FSP150CM/CC) product lines.  \n             Copyright (C) ADVA Optical Networking.')
f3PBBConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1))
f3PBBPerformanceObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2))
f3PBBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3))
f3PbbEthernetAccPortTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1), )
if mibBuilder.loadTexts: f3PbbEthernetAccPortTable.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetAccPortTable.setDescription('A list of entries corresponding to PBB function on the net port')
f3PbbEthernetAccPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1), )
cmEthernetAccPortEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbEthernetAccPortEntry"))
f3PbbEthernetAccPortEntry.setIndexNames(*cmEthernetAccPortEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbEthernetAccPortEntry.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetAccPortEntry.setDescription('A conceptual row in the f3PbbEthernetAccPortTable.')
f3PbbEthernetAccPortITagLoopbackMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopbackMask.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopbackMask.setDescription('This object allows to specify which itag loopback has been enabled.\n             1: Itag 1 loopback enabled, 2: Itag 2 loopback enabled, 4: Itag 4 loopback enabled.')
f3PbbEthernetAccPortITagLoopback1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopback1.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopback1.setDescription('This object allows specification of the Itag 1 to be looped back when port is in\n            vlan(terminal/facility) loopback configuration. This is valid only if the\n            corresponding bit in f3PbbEthernetAccPortITagLoopbackMask is set.  The value\n            to be specified should be in the form X-Y where X is the ISID and Y is the ITAG Priority. \n            If Y is specified as a *, all Priorities (0 to 7) are looped back.')
f3PbbEthernetAccPortITagLoopback2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopback2.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopback2.setDescription('This object allows specification of the Itag 2 to be looped back when port is in\n            vlan(terminal/facility) loopback configuration. This is valid only if the\n            corresponding bit in f3PbbEthernetAccPortITagLoopbackMask is set.  The value\n            to be specified should be in the form X-Y where X is the ISID and Y is the ITAG Priority. \n            If Y is specified as a *, all Priorities (0 to 7) are looped back.')
f3PbbEthernetAccPortITagLoopback3 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopback3.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetAccPortITagLoopback3.setDescription('This object allows specification of the Itag 3 to be looped back when port is in\n            vlan(terminal/facility) loopback configuration. This is valid only if the\n            corresponding bit in f3PbbEthernetAccPortITagLoopbackMask is set.  The value\n            to be specified should be in the form X-Y where X is the ISID and Y is the ITAG Priority. \n            If Y is specified as a *, all Priorities (0 to 7) are looped back.')
f3PbbEthernetNetPortTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2), )
if mibBuilder.loadTexts: f3PbbEthernetNetPortTable.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortTable.setDescription('A list of entries corresponding to PBB function on the net port')
f3PbbEthernetNetPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1), )
cmEthernetNetPortEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbEthernetNetPortEntry"))
f3PbbEthernetNetPortEntry.setIndexNames(*cmEthernetNetPortEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbEthernetNetPortEntry.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortEntry.setDescription('A conceptual row in the f3PbbEthernetNetPortTable.')
f3PbbEthernetNetPortBackboneMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetNetPortBackboneMacAddress.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortBackboneMacAddress.setDescription('This object is mac address of backbone network port.')
f3PbbEthernetNetPortITagLoopbackMask = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopbackMask.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopbackMask.setDescription('This object allows to specify which itag loopback has been enabled.\n             1: Itag 1 loopback enabled, 2: Itag 2 loopback enabled, 4: Itag 4 loopback enabled.')
f3PbbEthernetNetPortITagLoopback1 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopback1.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopback1.setDescription('This object allows specification of the Itag 1 to be looped back when port is in\n            vlan(terminal/facility) loopback configuration. This is valid only if the\n            corresponding bit in f3PbbEthernetNetPortITagLoopbackMask is set.  The value\n            to be specified should be in the form X-Y where X is the ISID and Y is the ITAG Priority. \n            If Y is specified as a *, all Priorities (0 to 7) are looped back.')
f3PbbEthernetNetPortITagLoopback2 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopback2.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopback2.setDescription('This object allows specification of the Itag 2 to be looped back when port is in\n            vlan(terminal/facility) loopback configuration. This is valid only if the\n            corresponding bit in f3PbbEthernetNetPortITagLoopbackMask is set.  The value\n            to be specified should be in the form X-Y where X is the ISID and Y is the ITAG Priority. \n            If Y is specified as a *, all Priorities (0 to 7) are looped back.')
f3PbbEthernetNetPortITagLoopback3 = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 2, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopback3.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortITagLoopback3.setDescription('This object allows specification of the Itag 3 to be looped back when port is in\n            vlan(terminal/facility) loopback configuration. This is valid only if the\n            corresponding bit in f3PbbEthernetNetPortITagLoopbackMask is set.  The value\n            to be specified should be in the form X-Y where X is the ISID and Y is the ITAG Priority. \n            If Y is specified as a *, all Priorities (0 to 7) are looped back.')
f3PbbFlowTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3), )
if mibBuilder.loadTexts: f3PbbFlowTable.setStatus('current')
if mibBuilder.loadTexts: f3PbbFlowTable.setDescription('A list of entries corresponding to PBB function on the flow')
f3PbbFlowEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1), )
cmFlowEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbFlowEntry"))
f3PbbFlowEntry.setIndexNames(*cmFlowEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbFlowEntry.setStatus('current')
if mibBuilder.loadTexts: f3PbbFlowEntry.setDescription('A conceptual row in the f3PbbFlowTable.')
f3PbbFlowITagControl = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 1), FlowTagControl()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowITagControl.setStatus('current')
if mibBuilder.loadTexts: f3PbbFlowITagControl.setDescription("This object allows specification of the tag management \n          operation on the I-TAG.  Supported types are 'none', 'push', and 'pushisid'.\n          and it must be none while ctagcontrol or stagcontrol is not none.")
f3PbbFlowITagISID = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(256, 16777214))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowITagISID.setStatus('current')
if mibBuilder.loadTexts: f3PbbFlowITagISID.setDescription('This object is used to specify the ITagISID. Its rang from 256 to 16777214.')
f3PbbFlowITagPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowITagPriority.setStatus('current')
if mibBuilder.loadTexts: f3PbbFlowITagPriority.setDescription('This object is used to specify the priority of ITag. Its rang from 0 to 7.')
f3PbbFlowBackboneMacDestinationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowBackboneMacDestinationEnabled.setStatus('current')
if mibBuilder.loadTexts: f3PbbFlowBackboneMacDestinationEnabled.setDescription('This object indicates whether can assign BMAC value.\n          When enabled, user can assign a  unicast BMAC as B_DA for this EVC\n          When disabled, 01-1E-83-<I-SID> will be used as B-DA.')
f3PbbFlowBackboneMacDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 5), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowBackboneMacDestinationAddress.setStatus('current')
if mibBuilder.loadTexts: f3PbbFlowBackboneMacDestinationAddress.setDescription('Customer can configure the backbone MAC destination address, the\n         default value is 01-1E-83-<I-SID>.')
f3PbbFlowA2NPbbCapableFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 3, 1, 6), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbFlowA2NPbbCapableFlag.setStatus('current')
if mibBuilder.loadTexts: f3PbbFlowA2NPbbCapableFlag.setDescription('When it is false, Drop PBB frames in the A2N direction (FPGA function),\n         Allow to PUSH I-TAG on this flow;\n         When A2NPbbCapableFlag is TRUE,\n         Pass PBB frames in the A2N direction (FPGA function), Software allow PUSH I-TAG on this flow(normal)\n         will not allow to PUSH S-TAG on this flow, will not allow to PUSH C-TAG on this flow,\n         Software will allow to PUSH C-TAG/S-TAG on this flow.')
f3PbbIpManagementTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4), )
if mibBuilder.loadTexts: f3PbbIpManagementTunnelTable.setStatus('current')
if mibBuilder.loadTexts: f3PbbIpManagementTunnelTable.setDescription('A list of entries corresponding to PBB function on the mngt tunnel')
f3PbbIpManagementTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1), )
ipManagementTunnelEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbIpManagementTunnelEntry"))
f3PbbIpManagementTunnelEntry.setIndexNames(*ipManagementTunnelEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbIpManagementTunnelEntry.setStatus('current')
if mibBuilder.loadTexts: f3PbbIpManagementTunnelEntry.setDescription('A conceptual row in the f3PbbIpManagementTunnelTable.')
f3PbbIpManagementTunnelItagEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbIpManagementTunnelItagEnabled.setStatus('current')
if mibBuilder.loadTexts: f3PbbIpManagementTunnelItagEnabled.setDescription('This object ITAG whether enabled, It is Enabled only When management tunnel type is ISID based.\n        By default it is disabled')
f3PbbIpManagementTunnelISID = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(256, 16777214))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbIpManagementTunnelISID.setStatus('current')
if mibBuilder.loadTexts: f3PbbIpManagementTunnelISID.setDescription('Only applicable when iTagEnabled =  enabled (ISID is shown to user, but in IFM data type here is ITAG).')
f3PbbIpManagementTunnelIPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbIpManagementTunnelIPriority.setStatus('current')
if mibBuilder.loadTexts: f3PbbIpManagementTunnelIPriority.setDescription('Only applicable when iTagEnabled =  enabled (ISID is shown to user, but in IFM data type here is ITAG, no use at present).')
f3PbbIpManagementTunnelBackboneMacDestinationEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 4), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbIpManagementTunnelBackboneMacDestinationEnabled.setStatus('current')
if mibBuilder.loadTexts: f3PbbIpManagementTunnelBackboneMacDestinationEnabled.setDescription('When enabled, we will use provisioned B-MAC for ARP and for management packets.\n        When disabled, we will use backbone group MAC address for ARP and get B-DA from ARP response\n        By default, it is disabled')
f3PbbIpManagementTunnelBackboneMacDestinationAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 1, 4, 1, 5), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: f3PbbIpManagementTunnelBackboneMacDestinationAddress.setStatus('current')
if mibBuilder.loadTexts: f3PbbIpManagementTunnelBackboneMacDestinationAddress.setDescription('User must set a valid MAC address, Only applicable when iTagEnabled =  enabled\n        By default, it is 00:00:00:00:00:00')
f3PbbEthernetNetPortStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1), )
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsTable.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsTable.setDescription('A collection of pbb Ethernet Network Port related statistics.  \n             These reflect the current data.')
f3PbbEthernetNetPortStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1, 1), )
cmEthernetNetPortStatsEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbEthernetNetPortStatsEntry"))
f3PbbEthernetNetPortStatsEntry.setIndexNames(*cmEthernetNetPortStatsEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsEntry.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsEntry.setDescription('A conceptual row in the f3PbbEthernetNetPortStatsTable.\n             Entries exist in this table for each Ethernet interface/port.')
f3PbbEthernetNetPortStatsPbbUniBdaDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1, 1, 1), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsPbbUniBdaDiscard.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsPbbUniBdaDiscard.setDescription("Number of PBB frames (BDA is not backbone group MAC) \n         discarded due to receive BDA which is not matching the \n         port's PBB MAC address when port is non-promiscuous mode.")
f3PbbEthernetNetPortStatsPbbGroupBdaDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 1, 1, 2), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsPbbGroupBdaDiscard.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortStatsPbbGroupBdaDiscard.setDescription('Number of PBB frames discarded due to mismatch of I-SID in I-TAG and I-SID \n         in backbone group MAC in the B-DA when port is non-promiscuous mode.')
f3PbbEthernetNetPortHistoryStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2), )
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsTable.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsTable.setDescription('A collection of pbb Ethernet Network Port related statistics.  \n             These reflect the current data.')
f3PbbEthernetNetPortHistoryStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2, 1), )
cmEthernetNetPortHistoryEntry.registerAugmentions(("F3-PBB-MIB", "f3PbbEthernetNetPortHistoryStatsEntry"))
f3PbbEthernetNetPortHistoryStatsEntry.setIndexNames(*cmEthernetNetPortHistoryEntry.getIndexNames())
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsEntry.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsEntry.setDescription('A conceptual row in the f3PbbEthernetNetPortHistoryStatsTable.\n             Entries exist in this table for each Ethernet interface/port.')
f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2, 1, 1), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard.setDescription("Number of PBB frames (BDA is not backbone group MAC) \n         discarded due to receive BDA which is not matching the \n         port's PBB MAC address when port is non-promiscuous mode.")
f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard = MibTableColumn((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 2, 2, 1, 2), PerfCounter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard.setStatus('current')
if mibBuilder.loadTexts: f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard.setDescription('Number of PBB frames discarded due to mismatch of I-SID in I-TAG and I-SID \n         in backbone group MAC in the B-DA when port is non-promiscuous mode.')
f3PBBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 1))
f3PBBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 2))
f3PBBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 1, 1)).setObjects(("F3-PBB-MIB", "f3PbbConfigGroup"), ("F3-PBB-MIB", "f3PbbStatsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PBBCompliance = f3PBBCompliance.setStatus('current')
if mibBuilder.loadTexts: f3PBBCompliance.setDescription('Describes the requirements for conformance to the PBB Object\n             group.')
f3PbbConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 2, 1)).setObjects(("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopbackMask"), ("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopback1"), ("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopback2"), ("F3-PBB-MIB", "f3PbbEthernetAccPortITagLoopback3"), ("F3-PBB-MIB", "f3PbbEthernetNetPortBackboneMacAddress"), ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopbackMask"), ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopback1"), ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopback2"), ("F3-PBB-MIB", "f3PbbEthernetNetPortITagLoopback3"), ("F3-PBB-MIB", "f3PbbFlowITagControl"), ("F3-PBB-MIB", "f3PbbFlowITagISID"), ("F3-PBB-MIB", "f3PbbFlowITagPriority"), ("F3-PBB-MIB", "f3PbbFlowBackboneMacDestinationEnabled"), ("F3-PBB-MIB", "f3PbbFlowBackboneMacDestinationAddress"), ("F3-PBB-MIB", "f3PbbFlowA2NPbbCapableFlag"), ("F3-PBB-MIB", "f3PbbIpManagementTunnelItagEnabled"), ("F3-PBB-MIB", "f3PbbIpManagementTunnelISID"), ("F3-PBB-MIB", "f3PbbIpManagementTunnelIPriority"), ("F3-PBB-MIB", "f3PbbIpManagementTunnelBackboneMacDestinationEnabled"), ("F3-PBB-MIB", "f3PbbIpManagementTunnelBackboneMacDestinationAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PbbConfigGroup = f3PbbConfigGroup.setStatus('current')
if mibBuilder.loadTexts: f3PbbConfigGroup.setDescription('A collection of objects used to manage the F3 PBB Functionality\n             .')
f3PbbStatsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2544, 1, 12, 21, 3, 2, 2)).setObjects(("F3-PBB-MIB", "f3PbbEthernetNetPortStatsPbbUniBdaDiscard"), ("F3-PBB-MIB", "f3PbbEthernetNetPortStatsPbbGroupBdaDiscard"), ("F3-PBB-MIB", "f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard"), ("F3-PBB-MIB", "f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    f3PbbStatsGroup = f3PbbStatsGroup.setStatus('current')
if mibBuilder.loadTexts: f3PbbStatsGroup.setDescription('A collection of objects used to manage the F3 PBB Functionality\n            .')
mibBuilder.exportSymbols("F3-PBB-MIB", f3PbbEthernetNetPortStatsPbbUniBdaDiscard=f3PbbEthernetNetPortStatsPbbUniBdaDiscard, f3PbbEthernetAccPortITagLoopbackMask=f3PbbEthernetAccPortITagLoopbackMask, f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard=f3PbbEthernetNetPortHistoryStatsPbbUniBdaDiscard, f3PbbFlowEntry=f3PbbFlowEntry, f3PBBMIB=f3PBBMIB, f3PbbIpManagementTunnelEntry=f3PbbIpManagementTunnelEntry, f3PBBCompliance=f3PBBCompliance, f3PbbStatsGroup=f3PbbStatsGroup, f3PbbEthernetNetPortITagLoopback2=f3PbbEthernetNetPortITagLoopback2, f3PbbEthernetNetPortStatsTable=f3PbbEthernetNetPortStatsTable, f3PBBCompliances=f3PBBCompliances, f3PbbIpManagementTunnelBackboneMacDestinationAddress=f3PbbIpManagementTunnelBackboneMacDestinationAddress, f3PbbIpManagementTunnelISID=f3PbbIpManagementTunnelISID, f3PbbIpManagementTunnelItagEnabled=f3PbbIpManagementTunnelItagEnabled, PYSNMP_MODULE_ID=f3PBBMIB, f3PbbIpManagementTunnelBackboneMacDestinationEnabled=f3PbbIpManagementTunnelBackboneMacDestinationEnabled, f3PbbEthernetAccPortITagLoopback1=f3PbbEthernetAccPortITagLoopback1, f3PbbEthernetNetPortEntry=f3PbbEthernetNetPortEntry, f3PbbFlowITagPriority=f3PbbFlowITagPriority, f3PbbIpManagementTunnelIPriority=f3PbbIpManagementTunnelIPriority, f3PbbFlowA2NPbbCapableFlag=f3PbbFlowA2NPbbCapableFlag, f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard=f3PbbEthernetNetPortHistoryStatsPbbGroupBdaDiscard, f3PbbEthernetAccPortITagLoopback2=f3PbbEthernetAccPortITagLoopback2, f3PbbFlowITagControl=f3PbbFlowITagControl, f3PBBConformance=f3PBBConformance, f3PbbFlowBackboneMacDestinationAddress=f3PbbFlowBackboneMacDestinationAddress, f3PbbEthernetAccPortITagLoopback3=f3PbbEthernetAccPortITagLoopback3, f3PbbEthernetNetPortITagLoopback1=f3PbbEthernetNetPortITagLoopback1, f3PbbEthernetNetPortStatsPbbGroupBdaDiscard=f3PbbEthernetNetPortStatsPbbGroupBdaDiscard, f3PbbEthernetNetPortHistoryStatsEntry=f3PbbEthernetNetPortHistoryStatsEntry, f3PbbEthernetNetPortITagLoopbackMask=f3PbbEthernetNetPortITagLoopbackMask, f3PBBGroups=f3PBBGroups, f3PbbFlowTable=f3PbbFlowTable, f3PbbEthernetNetPortBackboneMacAddress=f3PbbEthernetNetPortBackboneMacAddress, f3PbbEthernetNetPortITagLoopback3=f3PbbEthernetNetPortITagLoopback3, f3PBBPerformanceObjects=f3PBBPerformanceObjects, f3PbbEthernetAccPortTable=f3PbbEthernetAccPortTable, f3PbbEthernetNetPortTable=f3PbbEthernetNetPortTable, f3PbbFlowITagISID=f3PbbFlowITagISID, f3PbbEthernetNetPortStatsEntry=f3PbbEthernetNetPortStatsEntry, f3PbbEthernetNetPortHistoryStatsTable=f3PbbEthernetNetPortHistoryStatsTable, f3PbbConfigGroup=f3PbbConfigGroup, f3PBBConfigObjects=f3PBBConfigObjects, f3PbbIpManagementTunnelTable=f3PbbIpManagementTunnelTable, f3PbbEthernetAccPortEntry=f3PbbEthernetAccPortEntry, f3PbbFlowBackboneMacDestinationEnabled=f3PbbFlowBackboneMacDestinationEnabled)
