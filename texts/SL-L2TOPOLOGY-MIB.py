#
# PySNMP MIB module SL-L2TOPOLOGY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-L2TOPOLOGY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:47:38 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfIntervalCount, PerfTotalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfTotalCount", "PerfCurrentCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, ObjectIdentity, TimeTicks, Counter32, Integer32, NotificationType, iso, Unsigned32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "ObjectIdentity", "TimeTicks", "Counter32", "Integer32", "NotificationType", "iso", "Unsigned32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Counter64")
RowStatus, TextualConvention, TimeStamp, DisplayString, PhysAddress, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "TimeStamp", "DisplayString", "PhysAddress", "TruthValue")
slL2Topology = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10))
if mibBuilder.loadTexts: slL2Topology.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slL2Topology.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slL2Topology.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slL2Topology.setDescription('This MIB module describes the Layer-2 Topology')
topologyL2Links = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1))
topologyL2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2))
topologyL2LinkTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1), )
if mibBuilder.loadTexts: topologyL2LinkTable.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkTable.setDescription('The Topology L2 Link table.\n\t\tThis table contains the L2 links.')
topologyL2LinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1), ).setIndexNames((0, "SL-L2TOPOLOGY-MIB", "topologyL2LinkLocalIp"), (0, "SL-L2TOPOLOGY-MIB", "topologyL2LinkLocalPort"))
if mibBuilder.loadTexts: topologyL2LinkEntry.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkEntry.setDescription('An entry in the Topology L2 Link table.')
topologyL2LinkLocalIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalIp.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkLocalIp.setDescription('The local ip.')
topologyL2LinkLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalPort.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkLocalPort.setDescription('The local node port number.')
topologyL2LinkLocalMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalMac.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkLocalMac.setDescription('The local MAC address.')
topologyL2LinkLocalTid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalTid.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkLocalTid.setDescription('The local TID.')
topologyL2LinkRemoteIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemoteIp.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkRemoteIp.setDescription('The IP of the remote node.')
topologyL2LinkRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemotePort.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkRemotePort.setDescription('The port number of the remote node.')
topologyL2LinkRemoteMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemoteMac.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkRemoteMac.setDescription('The remote MAC address.')
topologyL2LinkRemoteTid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemoteTid.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkRemoteTid.setDescription('The remote TID.')
topologyL2LastChange = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LastChange.setStatus('current')
if mibBuilder.loadTexts: topologyL2LastChange.setDescription("The value of MIB II's sysUpTime object at the\n\t\ttime the TopologyL2LinkTable was last changed.")
topologyL2ChangeTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: topologyL2ChangeTrapEnable.setStatus('current')
if mibBuilder.loadTexts: topologyL2ChangeTrapEnable.setDescription('Indicates whether L2 topology change traps\n\t\tshould be generated.')
topologyL2LinkChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 3))
if mibBuilder.loadTexts: topologyL2LinkChange.setStatus('current')
if mibBuilder.loadTexts: topologyL2LinkChange.setDescription('A topologyL2LinkChange trap is sent when the\n\t\tcontent of an instance TopologyL2LinkEntry is changed.')
mibBuilder.exportSymbols("SL-L2TOPOLOGY-MIB", topologyL2LinkLocalPort=topologyL2LinkLocalPort, PYSNMP_MODULE_ID=slL2Topology, slL2Topology=slL2Topology, topologyL2LinkEntry=topologyL2LinkEntry, topologyL2ChangeTrapEnable=topologyL2ChangeTrapEnable, topologyL2LinkTable=topologyL2LinkTable, topologyL2Traps=topologyL2Traps, topologyL2LinkRemoteIp=topologyL2LinkRemoteIp, topologyL2LinkLocalIp=topologyL2LinkLocalIp, topologyL2LinkRemoteTid=topologyL2LinkRemoteTid, topologyL2LinkLocalMac=topologyL2LinkLocalMac, topologyL2LinkRemotePort=topologyL2LinkRemotePort, topologyL2LastChange=topologyL2LastChange, topologyL2LinkChange=topologyL2LinkChange, topologyL2LinkLocalTid=topologyL2LinkLocalTid, topologyL2LinkRemoteMac=topologyL2LinkRemoteMac, topologyL2Links=topologyL2Links)
