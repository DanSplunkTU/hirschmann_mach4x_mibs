#
# PySNMP MIB module IEEE8021-TSN-REMOTE-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-TSN-REMOTE-MANAGEMENT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:36 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ieee8021BridgeTrafficClass, ieee8021BridgeBaseComponentId, ieee8021BridgeBasePort = mibBuilder.importSymbols("IEEE8021-BRIDGE-MIB", "ieee8021BridgeTrafficClass", "ieee8021BridgeBaseComponentId", "ieee8021BridgeBasePort")
ieee8021QBridgeVlanIndex, = mibBuilder.importSymbols("IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanIndex")
IEEE8021BridgePortNumber, ieee802dot1mibs = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumber", "ieee802dot1mibs")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
RowStatus, DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention", "TruthValue")
ieee8021TsnRemoteMgmtMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 32))
ieee8021TsnRemoteMgmtMib.setRevisions(('2018-10-04 00:00',))
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMib.setLastUpdated('201810040000Z')
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMib.setOrganization('IEEE 802.1 Working Group')
ieee8021TsnRemoteMgmtNotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 32, 0))
ieee8021TsnRemoteMgmtObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 32, 1))
ieee8021TsnRemoteMgmtConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 32, 2))
ieee8021TsnRemoteMgmtBridgeDelay = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 32, 1, 1))
ieee8021TsnRemoteMgmtPropagationDelay = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 32, 1, 2))
ieee8021TsnRemoteMgmtStaticTrees = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 32, 1, 3))
ieee8021TsnRemoteMgmtMrpExternalControl = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 32, 1, 4))
ieee8021TsnRemoteMgmtBridgeDelayTable = MibTable((1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1), )
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtBridgeDelayTable.setStatus('current')
ieee8021TsnRemoteMgmtBridgeDelayEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeTrafficClass"), (0, "IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtBridgeIngressPort"), (0, "IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtBridgeEgressPort"))
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtBridgeDelayEntry.setStatus('current')
ieee8021TsnRemoteMgmtBridgeIngressPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 1), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtBridgeIngressPort.setStatus('current')
ieee8021TsnRemoteMgmtBridgeEgressPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 2), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtBridgeEgressPort.setStatus('current')
ieee8021TsnRemoteMgmtIndependentDelayMin = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtIndependentDelayMin.setStatus('current')
ieee8021TsnRemoteMgmtIndependentDelayMax = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtIndependentDelayMax.setStatus('current')
ieee8021TsnRemoteMgmtDependentDelayMin = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtDependentDelayMin.setStatus('current')
ieee8021TsnRemoteMgmtDependentDelayMax = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 1, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtDependentDelayMax.setStatus('current')
ieee8021TsnRemoteMgmtPropagationDelayTable = MibTable((1, 3, 111, 2, 802, 1, 1, 32, 1, 2, 1), )
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtPropagationDelayTable.setStatus('current')
ieee8021TsnRemoteMgmtPropagationDelayEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 32, 1, 2, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"))
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtPropagationDelayEntry.setStatus('current')
ieee8021TsnRemoteMgmtTxPropagationDelay = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 2, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtTxPropagationDelay.setStatus('current')
ieee8021TsnRemoteMgmtStaticTreesSupported = MibScalar((1, 3, 111, 2, 802, 1, 1, 32, 1, 3, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtStaticTreesSupported.setStatus('current')
ieee8021TsnRemoteMgmtMsrpMrpExternalControlTable = MibTable((1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1), )
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMsrpMrpExternalControlTable.setStatus('current')
ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1), ).setIndexNames((0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBaseComponentId"), (0, "IEEE8021-BRIDGE-MIB", "ieee8021BridgeBasePort"), (0, "IEEE8021-Q-BRIDGE-MIB", "ieee8021QBridgeVlanIndex"))
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry.setStatus('current')
ieee8021TsnRemoteMgmtMsrpMrpExternalControl = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMsrpMrpExternalControl.setStatus('current')
ieee8021TsnRemoteMgmtMrpIndicationList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMrpIndicationList.setStatus('current')
ieee8021TsnRemoteMgmtMrpIndicationListLength = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMrpIndicationListLength.setStatus('current')
ieee8021TsnRemoteMgmtMrpIndicationChangeCounter = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMrpIndicationChangeCounter.setStatus('current')
ieee8021TsnRemoteMgmtMrpAdminRequestList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMrpAdminRequestList.setStatus('current')
ieee8021TsnRemoteMgmtMrpAdminRequestListLength = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMrpAdminRequestListLength.setStatus('current')
ieee8021TsnRemoteMgmtMrpOperRequestList = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMrpOperRequestList.setStatus('current')
ieee8021TsnRemoteMgmtMrpOperRequestListLength = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 32, 1, 4, 1, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021TsnRemoteMgmtMrpOperRequestListLength.setStatus('current')
ieee8021TsnRemoteMgmtCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 32, 2, 1))
ieee8021TsnRemoteMgmtGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 32, 2, 2))
ieee8021TsnRemoteMgmtBridgeDelayGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 32, 2, 2, 1)).setObjects(("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtIndependentDelayMin"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtIndependentDelayMax"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtDependentDelayMin"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtDependentDelayMax"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TsnRemoteMgmtBridgeDelayGroup = ieee8021TsnRemoteMgmtBridgeDelayGroup.setStatus('current')
ieee8021TsnRemoteMgmtPropagationDelayGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 32, 2, 2, 2)).setObjects(("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtTxPropagationDelay"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TsnRemoteMgmtPropagationDelayGroup = ieee8021TsnRemoteMgmtPropagationDelayGroup.setStatus('current')
ieee8021TsnRemoteMgmtStaticTreesGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 32, 2, 2, 3)).setObjects(("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtStaticTreesSupported"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TsnRemoteMgmtStaticTreesGroup = ieee8021TsnRemoteMgmtStaticTreesGroup.setStatus('current')
ieee8021TsnRemoteMgmtMrpExternalControlGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 32, 2, 2, 4)).setObjects(("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMsrpMrpExternalControl"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpIndicationList"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpIndicationListLength"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpIndicationChangeCounter"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpAdminRequestList"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpAdminRequestListLength"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpOperRequestList"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpOperRequestListLength"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TsnRemoteMgmtMrpExternalControlGroup = ieee8021TsnRemoteMgmtMrpExternalControlGroup.setStatus('current')
ieee8021TsnRemoteMgmtCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 32, 2, 1, 1)).setObjects(("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtBridgeDelayGroup"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtPropagationDelayGroup"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtStaticTreesGroup"), ("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", "ieee8021TsnRemoteMgmtMrpExternalControlGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021TsnRemoteMgmtCompliance = ieee8021TsnRemoteMgmtCompliance.setStatus('current')
mibBuilder.exportSymbols("IEEE8021-TSN-REMOTE-MANAGEMENT-MIB", ieee8021TsnRemoteMgmtConformance=ieee8021TsnRemoteMgmtConformance, ieee8021TsnRemoteMgmtMsrpMrpExternalControlTable=ieee8021TsnRemoteMgmtMsrpMrpExternalControlTable, ieee8021TsnRemoteMgmtMrpOperRequestList=ieee8021TsnRemoteMgmtMrpOperRequestList, ieee8021TsnRemoteMgmtCompliances=ieee8021TsnRemoteMgmtCompliances, ieee8021TsnRemoteMgmtStaticTrees=ieee8021TsnRemoteMgmtStaticTrees, ieee8021TsnRemoteMgmtMrpExternalControl=ieee8021TsnRemoteMgmtMrpExternalControl, ieee8021TsnRemoteMgmtPropagationDelayTable=ieee8021TsnRemoteMgmtPropagationDelayTable, ieee8021TsnRemoteMgmtPropagationDelay=ieee8021TsnRemoteMgmtPropagationDelay, ieee8021TsnRemoteMgmtMrpExternalControlGroup=ieee8021TsnRemoteMgmtMrpExternalControlGroup, ieee8021TsnRemoteMgmtBridgeEgressPort=ieee8021TsnRemoteMgmtBridgeEgressPort, ieee8021TsnRemoteMgmtDependentDelayMax=ieee8021TsnRemoteMgmtDependentDelayMax, ieee8021TsnRemoteMgmtMrpAdminRequestList=ieee8021TsnRemoteMgmtMrpAdminRequestList, ieee8021TsnRemoteMgmtBridgeDelayEntry=ieee8021TsnRemoteMgmtBridgeDelayEntry, ieee8021TsnRemoteMgmtMib=ieee8021TsnRemoteMgmtMib, ieee8021TsnRemoteMgmtNotifications=ieee8021TsnRemoteMgmtNotifications, ieee8021TsnRemoteMgmtTxPropagationDelay=ieee8021TsnRemoteMgmtTxPropagationDelay, ieee8021TsnRemoteMgmtIndependentDelayMin=ieee8021TsnRemoteMgmtIndependentDelayMin, ieee8021TsnRemoteMgmtObjects=ieee8021TsnRemoteMgmtObjects, ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry=ieee8021TsnRemoteMgmtMsrpMrpExternalControlEntry, ieee8021TsnRemoteMgmtCompliance=ieee8021TsnRemoteMgmtCompliance, ieee8021TsnRemoteMgmtMrpIndicationChangeCounter=ieee8021TsnRemoteMgmtMrpIndicationChangeCounter, PYSNMP_MODULE_ID=ieee8021TsnRemoteMgmtMib, ieee8021TsnRemoteMgmtBridgeDelayGroup=ieee8021TsnRemoteMgmtBridgeDelayGroup, ieee8021TsnRemoteMgmtPropagationDelayGroup=ieee8021TsnRemoteMgmtPropagationDelayGroup, ieee8021TsnRemoteMgmtGroups=ieee8021TsnRemoteMgmtGroups, ieee8021TsnRemoteMgmtMrpIndicationList=ieee8021TsnRemoteMgmtMrpIndicationList, ieee8021TsnRemoteMgmtStaticTreesGroup=ieee8021TsnRemoteMgmtStaticTreesGroup, ieee8021TsnRemoteMgmtStaticTreesSupported=ieee8021TsnRemoteMgmtStaticTreesSupported, ieee8021TsnRemoteMgmtBridgeDelay=ieee8021TsnRemoteMgmtBridgeDelay, ieee8021TsnRemoteMgmtMrpOperRequestListLength=ieee8021TsnRemoteMgmtMrpOperRequestListLength, ieee8021TsnRemoteMgmtMsrpMrpExternalControl=ieee8021TsnRemoteMgmtMsrpMrpExternalControl, ieee8021TsnRemoteMgmtIndependentDelayMax=ieee8021TsnRemoteMgmtIndependentDelayMax, ieee8021TsnRemoteMgmtMrpIndicationListLength=ieee8021TsnRemoteMgmtMrpIndicationListLength, ieee8021TsnRemoteMgmtPropagationDelayEntry=ieee8021TsnRemoteMgmtPropagationDelayEntry, ieee8021TsnRemoteMgmtDependentDelayMin=ieee8021TsnRemoteMgmtDependentDelayMin, ieee8021TsnRemoteMgmtMrpAdminRequestListLength=ieee8021TsnRemoteMgmtMrpAdminRequestListLength, ieee8021TsnRemoteMgmtBridgeIngressPort=ieee8021TsnRemoteMgmtBridgeIngressPort, ieee8021TsnRemoteMgmtBridgeDelayTable=ieee8021TsnRemoteMgmtBridgeDelayTable)
