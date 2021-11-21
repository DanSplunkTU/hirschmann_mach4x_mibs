#
# PySNMP MIB module CTRON-SFPS-VSTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-VSTP-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:13 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
vlanSpanningTreePort, vlanSpanningTreeSwitch = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "vlanSpanningTreePort", "vlanSpanningTreeSwitch")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, IpAddress, Counter64, Integer32, Counter32, ObjectIdentity, NotificationType, Gauge32, MibIdentifier, Bits, Unsigned32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "IpAddress", "Counter64", "Integer32", "Counter32", "ObjectIdentity", "NotificationType", "Gauge32", "MibIdentifier", "Bits", "Unsigned32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class SfpsSwitchPort(Integer32):
    pass

class HexInteger(Integer32):
    pass

vlanSpanningTreePortTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1), )
if mibBuilder.loadTexts: vlanSpanningTreePortTable.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreePortTable.setDescription('This table contains information used by the spanning tree algorithm\n                 for each port instance.')
vlanSpanningTreePortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VSTP-MIB", "vlanSpanningTreePortPortNumber"))
if mibBuilder.loadTexts: vlanSpanningTreePortEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreePortEntry.setDescription('Each entry contains spanning tree information for that port instance.')
vlanSpanningTreePortPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 1), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortPortNumber.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreePortPortNumber.setDescription('The port number of the port instance. This value is also the \n                 primary index for the table.')
vlanSpanningTreePortPortState = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2), ("blocking", 3), ("listening", 4), ("learning", 5), ("forwarding", 6), ("broken", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortPortState.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreePortPortState.setDescription('The spanning tree port state for this port.')
vlanSpanningTreePortPortIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 3), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortPortIdentifier.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreePortPortIdentifier.setDescription('The spanning tree port identifier for this port.')
vlanSpanningTreePortPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpanningTreePortPathCost.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreePortPathCost.setDescription('The spanning tree path cost for this port.')
vlanSpanningTreePortDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedRoot.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedRoot.setDescription('The spanning tree designated root for this port.')
vlanSpanningTreePortDesignatedCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedCost.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedCost.setDescription('The spanning tree designated cost for this port.')
vlanSpanningTreePortDesignatedBridge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedBridge.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedBridge.setDescription('The spanning tree designated bridge for this port.')
vlanSpanningTreePortDesignatedPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 1, 1, 1, 8), HexInteger()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedPort.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreePortDesignatedPort.setDescription('The spanning tree designated port.')
vlanSpanningTreeSwitchTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1), )
if mibBuilder.loadTexts: vlanSpanningTreeSwitchTable.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchTable.setDescription('This table contains information used by the spanning tree\n                 algorithm specific to the switch on which the algorithm is\n                 running.')
vlanSpanningTreeSwitchEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1), ).setIndexNames((0, "CTRON-SFPS-VSTP-MIB", "vlanSpanningTreeSwitchIndex"))
if mibBuilder.loadTexts: vlanSpanningTreeSwitchEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchEntry.setDescription('Each entry specifies switch specific spanning tree information.')
vlanSpanningTreeSwitchIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchIndex.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchIndex.setDescription('Table index value.')
vlanSpanningTreeSwitchBridgePriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 2), HexInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchBridgePriority.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchBridgePriority.setDescription('Spanning tree designated bridge priority.')
vlanSpanningTreeSwitchBridgeId = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchBridgeId.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchBridgeId.setDescription('Spanning tree bridge id value.')
vlanSpanningTreeSwitchDesignatedRoot = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchDesignatedRoot.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchDesignatedRoot.setDescription('Spanning tree designated root value.')
vlanSpanningTreeSwitchRootPathCost = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchRootPathCost.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchRootPathCost.setDescription('Spanning tree root path cost.')
vlanSpanningTreeSwitchOperTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchOperTime.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchOperTime.setDescription('Spanning tree operational time.')
vlanSpanningTreeSwitchRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 7), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchRootPort.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchRootPort.setDescription('Spanning tree root port.')
vlanSpanningTreeSwitchRootPortTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchRootPortTime.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchRootPortTime.setDescription('Spanning tree root port time.')
vlanSpanningTreeSwitchPrevRootPort = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 9), SfpsSwitchPort()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchPrevRootPort.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchPrevRootPort.setDescription('Spanning tree previous root port.')
vlanSpanningTreeSwitchPrevRootPortTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 10), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchPrevRootPortTime.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchPrevRootPortTime.setDescription('Spanning tree previous root port time.')
vlanSpanningTreeSwitchMaxAge = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchMaxAge.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchMaxAge.setDescription('Spanning tree max age value.')
vlanSpanningTreeSwitchHelloTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchHelloTime.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchHelloTime.setDescription('Spanning tree hello time value.')
vlanSpanningTreeSwitchForwardDelay = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 12, 1, 2, 8, 2, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vlanSpanningTreeSwitchForwardDelay.setStatus('mandatory')
if mibBuilder.loadTexts: vlanSpanningTreeSwitchForwardDelay.setDescription('Spanning tree forward delay value.')
mibBuilder.exportSymbols("CTRON-SFPS-VSTP-MIB", vlanSpanningTreeSwitchEntry=vlanSpanningTreeSwitchEntry, vlanSpanningTreePortPathCost=vlanSpanningTreePortPathCost, vlanSpanningTreePortPortNumber=vlanSpanningTreePortPortNumber, vlanSpanningTreeSwitchRootPort=vlanSpanningTreeSwitchRootPort, vlanSpanningTreePortTable=vlanSpanningTreePortTable, vlanSpanningTreeSwitchDesignatedRoot=vlanSpanningTreeSwitchDesignatedRoot, vlanSpanningTreeSwitchHelloTime=vlanSpanningTreeSwitchHelloTime, vlanSpanningTreeSwitchBridgePriority=vlanSpanningTreeSwitchBridgePriority, SfpsSwitchPort=SfpsSwitchPort, vlanSpanningTreePortPortState=vlanSpanningTreePortPortState, vlanSpanningTreePortEntry=vlanSpanningTreePortEntry, vlanSpanningTreePortPortIdentifier=vlanSpanningTreePortPortIdentifier, vlanSpanningTreeSwitchRootPortTime=vlanSpanningTreeSwitchRootPortTime, vlanSpanningTreeSwitchOperTime=vlanSpanningTreeSwitchOperTime, vlanSpanningTreeSwitchPrevRootPortTime=vlanSpanningTreeSwitchPrevRootPortTime, vlanSpanningTreeSwitchIndex=vlanSpanningTreeSwitchIndex, vlanSpanningTreePortDesignatedPort=vlanSpanningTreePortDesignatedPort, HexInteger=HexInteger, vlanSpanningTreeSwitchRootPathCost=vlanSpanningTreeSwitchRootPathCost, vlanSpanningTreeSwitchMaxAge=vlanSpanningTreeSwitchMaxAge, vlanSpanningTreeSwitchPrevRootPort=vlanSpanningTreeSwitchPrevRootPort, vlanSpanningTreeSwitchTable=vlanSpanningTreeSwitchTable, vlanSpanningTreeSwitchForwardDelay=vlanSpanningTreeSwitchForwardDelay, vlanSpanningTreePortDesignatedRoot=vlanSpanningTreePortDesignatedRoot, vlanSpanningTreePortDesignatedBridge=vlanSpanningTreePortDesignatedBridge, vlanSpanningTreePortDesignatedCost=vlanSpanningTreePortDesignatedCost, vlanSpanningTreeSwitchBridgeId=vlanSpanningTreeSwitchBridgeId)
