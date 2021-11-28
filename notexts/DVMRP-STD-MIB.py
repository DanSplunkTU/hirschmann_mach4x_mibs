#
# PySNMP MIB module DVMRP-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/DVMRP-STD-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:09:00 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, ObjectIdentity, iso, experimental, Counter64, Gauge32, MibIdentifier, Counter32, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Bits, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "ObjectIdentity", "iso", "experimental", "Counter64", "Gauge32", "MibIdentifier", "Counter32", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Bits", "Unsigned32")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
dvmrpStdMIB = ModuleIdentity((1, 3, 6, 1, 3, 62))
dvmrpStdMIB.setRevisions(('2001-11-21 12:00',))
if mibBuilder.loadTexts: dvmrpStdMIB.setLastUpdated('200111211200Z')
if mibBuilder.loadTexts: dvmrpStdMIB.setOrganization('IETF IDMR Working Group.')
dvmrpMIBObjects = MibIdentifier((1, 3, 6, 1, 3, 62, 1))
dvmrp = MibIdentifier((1, 3, 6, 1, 3, 62, 1, 1))
dvmrpScalar = MibIdentifier((1, 3, 6, 1, 3, 62, 1, 1, 1))
dvmrpVersionString = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpVersionString.setStatus('current')
dvmrpNumRoutes = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNumRoutes.setStatus('current')
dvmrpReachableRoutes = MibScalar((1, 3, 6, 1, 3, 62, 1, 1, 1, 4), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpReachableRoutes.setStatus('current')
dvmrpInterfaceTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 2), )
if mibBuilder.loadTexts: dvmrpInterfaceTable.setStatus('current')
dvmrpInterfaceEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 2, 1), ).setIndexNames((0, "DVMRP-STD-MIB", "dvmrpInterfaceIndex"))
if mibBuilder.loadTexts: dvmrpInterfaceEntry.setStatus('current')
dvmrpInterfaceIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dvmrpInterfaceIndex.setStatus('current')
dvmrpInterfaceLocalAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 2), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceLocalAddress.setStatus('current')
dvmrpInterfaceMetric = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31)).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceMetric.setStatus('current')
dvmrpInterfaceStatus = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceStatus.setStatus('current')
dvmrpInterfaceRcvBadPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadPkts.setStatus('current')
dvmrpInterfaceRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceRcvBadRoutes.setStatus('current')
dvmrpInterfaceSentRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceSentRoutes.setStatus('current')
dvmrpInterfaceKey = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 8), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceKey.setStatus('current')
dvmrpInterfaceKeyVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: dvmrpInterfaceKeyVersion.setStatus('current')
dvmrpInterfaceGenerationId = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpInterfaceGenerationId.setStatus('current')
dvmrpNeighborTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 3), )
if mibBuilder.loadTexts: dvmrpNeighborTable.setStatus('current')
dvmrpNeighborEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 3, 1), ).setIndexNames((0, "DVMRP-STD-MIB", "dvmrpNeighborIfIndex"), (0, "DVMRP-STD-MIB", "dvmrpNeighborAddress"))
if mibBuilder.loadTexts: dvmrpNeighborEntry.setStatus('current')
dvmrpNeighborIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: dvmrpNeighborIfIndex.setStatus('current')
dvmrpNeighborAddress = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpNeighborAddress.setStatus('current')
dvmrpNeighborUpTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 3), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborUpTime.setStatus('current')
dvmrpNeighborExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborExpiryTime.setStatus('current')
dvmrpNeighborGenerationId = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborGenerationId.setStatus('current')
dvmrpNeighborMajorVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborMajorVersion.setStatus('current')
dvmrpNeighborMinorVersion = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborMinorVersion.setStatus('current')
dvmrpNeighborCapabilities = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 8), Bits().clone(namedValues=NamedValues(("leaf", 0), ("prune", 1), ("generationID", 2), ("mtrace", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborCapabilities.setStatus('current')
dvmrpNeighborRcvRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvRoutes.setStatus('current')
dvmrpNeighborRcvBadPkts = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvBadPkts.setStatus('current')
dvmrpNeighborRcvBadRoutes = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborRcvBadRoutes.setStatus('current')
dvmrpNeighborState = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 3, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("oneway", 1), ("active", 2), ("ignoring", 3), ("down", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpNeighborState.setStatus('current')
dvmrpRouteTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 4), )
if mibBuilder.loadTexts: dvmrpRouteTable.setStatus('current')
dvmrpRouteEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 4, 1), ).setIndexNames((0, "DVMRP-STD-MIB", "dvmrpRouteSource"), (0, "DVMRP-STD-MIB", "dvmrpRouteSourceMask"))
if mibBuilder.loadTexts: dvmrpRouteEntry.setStatus('current')
dvmrpRouteSource = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteSource.setStatus('current')
dvmrpRouteSourceMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteSourceMask.setStatus('current')
dvmrpRouteUpstreamNeighbor = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 3), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteUpstreamNeighbor.setStatus('current')
dvmrpRouteIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteIfIndex.setStatus('current')
dvmrpRouteMetric = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteMetric.setStatus('current')
dvmrpRouteExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteExpiryTime.setStatus('current')
dvmrpRouteUpTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 4, 1, 7), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteUpTime.setStatus('current')
dvmrpRouteNextHopTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 5), )
if mibBuilder.loadTexts: dvmrpRouteNextHopTable.setStatus('current')
dvmrpRouteNextHopEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 5, 1), ).setIndexNames((0, "DVMRP-STD-MIB", "dvmrpRouteNextHopSource"), (0, "DVMRP-STD-MIB", "dvmrpRouteNextHopSourceMask"), (0, "DVMRP-STD-MIB", "dvmrpRouteNextHopIfIndex"))
if mibBuilder.loadTexts: dvmrpRouteNextHopEntry.setStatus('current')
dvmrpRouteNextHopSource = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteNextHopSource.setStatus('current')
dvmrpRouteNextHopSourceMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpRouteNextHopSourceMask.setStatus('current')
dvmrpRouteNextHopIfIndex = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 3), InterfaceIndex())
if mibBuilder.loadTexts: dvmrpRouteNextHopIfIndex.setStatus('current')
dvmrpRouteNextHopType = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("leaf", 1), ("branch", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpRouteNextHopType.setStatus('current')
dvmrpPruneTable = MibTable((1, 3, 6, 1, 3, 62, 1, 1, 6), )
if mibBuilder.loadTexts: dvmrpPruneTable.setStatus('current')
dvmrpPruneEntry = MibTableRow((1, 3, 6, 1, 3, 62, 1, 1, 6, 1), ).setIndexNames((0, "DVMRP-STD-MIB", "dvmrpPruneGroup"), (0, "DVMRP-STD-MIB", "dvmrpPruneSource"), (0, "DVMRP-STD-MIB", "dvmrpPruneSourceMask"))
if mibBuilder.loadTexts: dvmrpPruneEntry.setStatus('current')
dvmrpPruneGroup = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 1), IpAddress())
if mibBuilder.loadTexts: dvmrpPruneGroup.setStatus('current')
dvmrpPruneSource = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 2), IpAddress())
if mibBuilder.loadTexts: dvmrpPruneSource.setStatus('current')
dvmrpPruneSourceMask = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 3), IpAddress())
if mibBuilder.loadTexts: dvmrpPruneSourceMask.setStatus('current')
dvmrpPruneExpiryTime = MibTableColumn((1, 3, 6, 1, 3, 62, 1, 1, 6, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dvmrpPruneExpiryTime.setStatus('current')
dvmrpTraps = MibIdentifier((1, 3, 6, 1, 3, 62, 1, 1, 7))
dvmrpNeighborLoss = NotificationType((1, 3, 6, 1, 3, 62, 1, 1, 7, 1)).setObjects(("DVMRP-STD-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB", "dvmrpNeighborState"))
if mibBuilder.loadTexts: dvmrpNeighborLoss.setStatus('current')
dvmrpNeighborNotPruning = NotificationType((1, 3, 6, 1, 3, 62, 1, 1, 7, 2)).setObjects(("DVMRP-STD-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB", "dvmrpNeighborCapabilities"))
if mibBuilder.loadTexts: dvmrpNeighborNotPruning.setStatus('current')
dvmrpMIBConformance = MibIdentifier((1, 3, 6, 1, 3, 62, 2))
dvmrpMIBCompliances = MibIdentifier((1, 3, 6, 1, 3, 62, 2, 1))
dvmrpMIBGroups = MibIdentifier((1, 3, 6, 1, 3, 62, 2, 2))
dvmrpMIBCompliance = ModuleCompliance((1, 3, 6, 1, 3, 62, 2, 1, 1)).setObjects(("DVMRP-STD-MIB", "dvmrpGeneralGroup"), ("DVMRP-STD-MIB", "dvmrpInterfaceGroup"), ("DVMRP-STD-MIB", "dvmrpNeighborGroup"), ("DVMRP-STD-MIB", "dvmrpRoutingGroup"), ("DVMRP-STD-MIB", "dvmrpTreeGroup"), ("DVMRP-STD-MIB", "dvmrpSecurityGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpMIBCompliance = dvmrpMIBCompliance.setStatus('current')
dvmrpGeneralGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 2)).setObjects(("DVMRP-STD-MIB", "dvmrpVersionString"), ("DVMRP-STD-MIB", "dvmrpNumRoutes"), ("DVMRP-STD-MIB", "dvmrpReachableRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpGeneralGroup = dvmrpGeneralGroup.setStatus('current')
dvmrpInterfaceGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 3)).setObjects(("DVMRP-STD-MIB", "dvmrpInterfaceLocalAddress"), ("DVMRP-STD-MIB", "dvmrpInterfaceMetric"), ("DVMRP-STD-MIB", "dvmrpInterfaceStatus"), ("DVMRP-STD-MIB", "dvmrpInterfaceGenerationId"), ("DVMRP-STD-MIB", "dvmrpInterfaceRcvBadPkts"), ("DVMRP-STD-MIB", "dvmrpInterfaceRcvBadRoutes"), ("DVMRP-STD-MIB", "dvmrpInterfaceSentRoutes"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpInterfaceGroup = dvmrpInterfaceGroup.setStatus('current')
dvmrpNeighborGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 4)).setObjects(("DVMRP-STD-MIB", "dvmrpNeighborUpTime"), ("DVMRP-STD-MIB", "dvmrpNeighborExpiryTime"), ("DVMRP-STD-MIB", "dvmrpNeighborGenerationId"), ("DVMRP-STD-MIB", "dvmrpNeighborMajorVersion"), ("DVMRP-STD-MIB", "dvmrpNeighborMinorVersion"), ("DVMRP-STD-MIB", "dvmrpNeighborCapabilities"), ("DVMRP-STD-MIB", "dvmrpNeighborRcvRoutes"), ("DVMRP-STD-MIB", "dvmrpNeighborRcvBadPkts"), ("DVMRP-STD-MIB", "dvmrpNeighborRcvBadRoutes"), ("DVMRP-STD-MIB", "dvmrpNeighborState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpNeighborGroup = dvmrpNeighborGroup.setStatus('current')
dvmrpRoutingGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 5)).setObjects(("DVMRP-STD-MIB", "dvmrpRouteUpstreamNeighbor"), ("DVMRP-STD-MIB", "dvmrpRouteIfIndex"), ("DVMRP-STD-MIB", "dvmrpRouteMetric"), ("DVMRP-STD-MIB", "dvmrpRouteExpiryTime"), ("DVMRP-STD-MIB", "dvmrpRouteUpTime"), ("DVMRP-STD-MIB", "dvmrpRouteNextHopType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpRoutingGroup = dvmrpRoutingGroup.setStatus('current')
dvmrpSecurityGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 6)).setObjects(("DVMRP-STD-MIB", "dvmrpInterfaceKey"), ("DVMRP-STD-MIB", "dvmrpInterfaceKeyVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpSecurityGroup = dvmrpSecurityGroup.setStatus('current')
dvmrpTreeGroup = ObjectGroup((1, 3, 6, 1, 3, 62, 2, 2, 7)).setObjects(("DVMRP-STD-MIB", "dvmrpPruneExpiryTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpTreeGroup = dvmrpTreeGroup.setStatus('current')
dvmrpNotificationGroup = NotificationGroup((1, 3, 6, 1, 3, 62, 2, 2, 8)).setObjects(("DVMRP-STD-MIB", "dvmrpNeighborLoss"), ("DVMRP-STD-MIB", "dvmrpNeighborNotPruning"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    dvmrpNotificationGroup = dvmrpNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("DVMRP-STD-MIB", dvmrpMIBCompliances=dvmrpMIBCompliances, dvmrpNotificationGroup=dvmrpNotificationGroup, dvmrpNeighborMajorVersion=dvmrpNeighborMajorVersion, dvmrpNeighborCapabilities=dvmrpNeighborCapabilities, dvmrpNeighborRcvRoutes=dvmrpNeighborRcvRoutes, dvmrpGeneralGroup=dvmrpGeneralGroup, dvmrpInterfaceLocalAddress=dvmrpInterfaceLocalAddress, dvmrpTreeGroup=dvmrpTreeGroup, dvmrpReachableRoutes=dvmrpReachableRoutes, dvmrpRouteTable=dvmrpRouteTable, dvmrpPruneSource=dvmrpPruneSource, dvmrpRouteSourceMask=dvmrpRouteSourceMask, dvmrpNeighborState=dvmrpNeighborState, dvmrp=dvmrp, dvmrpRouteNextHopEntry=dvmrpRouteNextHopEntry, dvmrpRouteSource=dvmrpRouteSource, dvmrpRouteNextHopIfIndex=dvmrpRouteNextHopIfIndex, PYSNMP_MODULE_ID=dvmrpStdMIB, dvmrpInterfaceMetric=dvmrpInterfaceMetric, dvmrpRouteMetric=dvmrpRouteMetric, dvmrpNeighborAddress=dvmrpNeighborAddress, dvmrpPruneGroup=dvmrpPruneGroup, dvmrpNeighborRcvBadPkts=dvmrpNeighborRcvBadPkts, dvmrpInterfaceRcvBadRoutes=dvmrpInterfaceRcvBadRoutes, dvmrpInterfaceEntry=dvmrpInterfaceEntry, dvmrpRouteNextHopType=dvmrpRouteNextHopType, dvmrpInterfaceKey=dvmrpInterfaceKey, dvmrpNumRoutes=dvmrpNumRoutes, dvmrpPruneTable=dvmrpPruneTable, dvmrpPruneSourceMask=dvmrpPruneSourceMask, dvmrpInterfaceIndex=dvmrpInterfaceIndex, dvmrpPruneExpiryTime=dvmrpPruneExpiryTime, dvmrpTraps=dvmrpTraps, dvmrpMIBGroups=dvmrpMIBGroups, dvmrpSecurityGroup=dvmrpSecurityGroup, dvmrpInterfaceGenerationId=dvmrpInterfaceGenerationId, dvmrpNeighborRcvBadRoutes=dvmrpNeighborRcvBadRoutes, dvmrpRouteUpstreamNeighbor=dvmrpRouteUpstreamNeighbor, dvmrpScalar=dvmrpScalar, dvmrpMIBConformance=dvmrpMIBConformance, dvmrpNeighborNotPruning=dvmrpNeighborNotPruning, dvmrpInterfaceGroup=dvmrpInterfaceGroup, dvmrpStdMIB=dvmrpStdMIB, dvmrpRoutingGroup=dvmrpRoutingGroup, dvmrpVersionString=dvmrpVersionString, dvmrpNeighborGroup=dvmrpNeighborGroup, dvmrpNeighborUpTime=dvmrpNeighborUpTime, dvmrpNeighborGenerationId=dvmrpNeighborGenerationId, dvmrpRouteNextHopTable=dvmrpRouteNextHopTable, dvmrpMIBCompliance=dvmrpMIBCompliance, dvmrpRouteExpiryTime=dvmrpRouteExpiryTime, dvmrpNeighborTable=dvmrpNeighborTable, dvmrpRouteNextHopSourceMask=dvmrpRouteNextHopSourceMask, dvmrpPruneEntry=dvmrpPruneEntry, dvmrpMIBObjects=dvmrpMIBObjects, dvmrpNeighborEntry=dvmrpNeighborEntry, dvmrpInterfaceRcvBadPkts=dvmrpInterfaceRcvBadPkts, dvmrpRouteNextHopSource=dvmrpRouteNextHopSource, dvmrpNeighborMinorVersion=dvmrpNeighborMinorVersion, dvmrpInterfaceKeyVersion=dvmrpInterfaceKeyVersion, dvmrpNeighborIfIndex=dvmrpNeighborIfIndex, dvmrpRouteIfIndex=dvmrpRouteIfIndex, dvmrpRouteEntry=dvmrpRouteEntry, dvmrpInterfaceTable=dvmrpInterfaceTable, dvmrpNeighborExpiryTime=dvmrpNeighborExpiryTime, dvmrpNeighborLoss=dvmrpNeighborLoss, dvmrpInterfaceSentRoutes=dvmrpInterfaceSentRoutes, dvmrpRouteUpTime=dvmrpRouteUpTime, dvmrpInterfaceStatus=dvmrpInterfaceStatus)
