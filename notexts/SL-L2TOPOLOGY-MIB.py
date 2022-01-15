#
# PySNMP MIB module SL-L2TOPOLOGY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-L2TOPOLOGY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:15:38 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
PerfTotalCount, PerfCurrentCount, PerfIntervalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfTotalCount", "PerfCurrentCount", "PerfIntervalCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Unsigned32, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, Counter64, Gauge32, NotificationType, Counter32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Unsigned32", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "Counter64", "Gauge32", "NotificationType", "Counter32", "Bits", "ModuleIdentity")
PhysAddress, DisplayString, TruthValue, TimeStamp, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "PhysAddress", "DisplayString", "TruthValue", "TimeStamp", "TextualConvention", "RowStatus")
slL2Topology = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10))
if mibBuilder.loadTexts: slL2Topology.setLastUpdated('200008280000Z')
if mibBuilder.loadTexts: slL2Topology.setOrganization('PacketLight Networks Ltd.')
topologyL2Links = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1))
topologyL2Traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2))
topologyL2LinkTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1), )
if mibBuilder.loadTexts: topologyL2LinkTable.setStatus('current')
topologyL2LinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1), ).setIndexNames((0, "SL-L2TOPOLOGY-MIB", "topologyL2LinkLocalIp"), (0, "SL-L2TOPOLOGY-MIB", "topologyL2LinkLocalPort"))
if mibBuilder.loadTexts: topologyL2LinkEntry.setStatus('current')
topologyL2LinkLocalIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 1), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalIp.setStatus('current')
topologyL2LinkLocalPort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalPort.setStatus('current')
topologyL2LinkLocalMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 3), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalMac.setStatus('current')
topologyL2LinkLocalTid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkLocalTid.setStatus('current')
topologyL2LinkRemoteIp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemoteIp.setStatus('current')
topologyL2LinkRemotePort = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemotePort.setStatus('current')
topologyL2LinkRemoteMac = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 7), PhysAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemoteMac.setStatus('current')
topologyL2LinkRemoteTid = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 1, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LinkRemoteTid.setStatus('current')
topologyL2LastChange = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 1), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: topologyL2LastChange.setStatus('current')
topologyL2ChangeTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: topologyL2ChangeTrapEnable.setStatus('current')
topologyL2LinkChange = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 10, 2, 3))
if mibBuilder.loadTexts: topologyL2LinkChange.setStatus('current')
mibBuilder.exportSymbols("SL-L2TOPOLOGY-MIB", topologyL2LinkLocalPort=topologyL2LinkLocalPort, topologyL2LinkRemoteTid=topologyL2LinkRemoteTid, topologyL2LinkRemotePort=topologyL2LinkRemotePort, topologyL2LinkRemoteMac=topologyL2LinkRemoteMac, topologyL2LinkEntry=topologyL2LinkEntry, topologyL2LastChange=topologyL2LastChange, topologyL2LinkLocalMac=topologyL2LinkLocalMac, topologyL2LinkChange=topologyL2LinkChange, topologyL2ChangeTrapEnable=topologyL2ChangeTrapEnable, slL2Topology=slL2Topology, topologyL2LinkLocalTid=topologyL2LinkLocalTid, topologyL2Links=topologyL2Links, PYSNMP_MODULE_ID=slL2Topology, topologyL2LinkLocalIp=topologyL2LinkLocalIp, topologyL2Traps=topologyL2Traps, topologyL2LinkTable=topologyL2LinkTable, topologyL2LinkRemoteIp=topologyL2LinkRemoteIp)
