#
# PySNMP MIB module CTRON-PRIORITY-CLASSIFY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-PRIORITY-CLASSIFY-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:06 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ctPriorityExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctPriorityExt")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, NotificationType, ObjectIdentity, TimeTicks, MibIdentifier, Bits, Integer32, Gauge32, ModuleIdentity, Counter32, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "NotificationType", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "Integer32", "Gauge32", "ModuleIdentity", "Counter32", "Unsigned32", "IpAddress", "iso")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ctPriClassify = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6))
if mibBuilder.loadTexts: ctPriClassify.setLastUpdated('200203121855Z')
if mibBuilder.loadTexts: ctPriClassify.setOrganization('Cabletron Systems, Inc')
ctPriClassifyObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1))
class CtPriClassifyType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25))
    namedValues = NamedValues(("etherType", 1), ("llcDsapSsap", 2), ("ipTypeOfService", 3), ("ipProtocolType", 4), ("ipxClassOfService", 5), ("ipxPacketType", 6), ("ipAddressSource", 7), ("ipAddressDestination", 8), ("ipAddressBilateral", 9), ("ipxNetworkSource", 10), ("ipxNetworkDestination", 11), ("ipxNetworkBilateral", 12), ("ipUdpPortSource", 13), ("ipUdpPortDestination", 14), ("ipUdpPortBilateral", 15), ("ipTcpPortSource", 16), ("ipTcpPortDestination", 17), ("ipTcpPortBilateral", 18), ("ipxSocketSource", 19), ("ipxSocketDestination", 20), ("ipxSocketBilateral", 21), ("macAddressSource", 22), ("macAddressDestination", 23), ("macAddressBilateral", 24), ("ipFragments", 25))

class PortList(TextualConvention, OctetString):
    status = 'current'

ctPriClassifyStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyStatus.setStatus('current')
ctPriClassifyMaxEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyMaxEntries.setStatus('current')
ctPriClassifyNumEntries = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyNumEntries.setStatus('current')
ctPriClassifyTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4), )
if mibBuilder.loadTexts: ctPriClassifyTable.setStatus('current')
ctPriClassifyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1), ).setIndexNames((0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyPriority"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataMeaning"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataVal"), (0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyDataMask"))
if mibBuilder.loadTexts: ctPriClassifyEntry.setStatus('current')
ctPriClassifyPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7)))
if mibBuilder.loadTexts: ctPriClassifyPriority.setStatus('current')
ctPriClassifyDataMeaning = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 2), CtPriClassifyType())
if mibBuilder.loadTexts: ctPriClassifyDataMeaning.setStatus('current')
ctPriClassifyDataVal = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 3), Unsigned32())
if mibBuilder.loadTexts: ctPriClassifyDataVal.setStatus('current')
ctPriClassifyDataMask = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 4), Unsigned32())
if mibBuilder.loadTexts: ctPriClassifyDataMask.setStatus('current')
ctPriClassifyIngressList = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 5), PortList().clone(hexValue="0000")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctPriClassifyIngressList.setStatus('current')
ctPriClassifyRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: ctPriClassifyRowStatus.setStatus('current')
ctPriClassifyRowInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyRowInfo.setStatus('current')
ctPriClassifyTOSStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyTOSStatus.setStatus('current')
ctPriClassifyTOSValue = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 4, 1, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctPriClassifyTOSValue.setStatus('current')
ctPriClassifyAbilityTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5), )
if mibBuilder.loadTexts: ctPriClassifyAbilityTable.setStatus('current')
ctPriClassifyAbilityEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1), ).setIndexNames((0, "CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyAbility"))
if mibBuilder.loadTexts: ctPriClassifyAbilityEntry.setStatus('current')
ctPriClassifyAbility = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1, 1), CtPriClassifyType())
if mibBuilder.loadTexts: ctPriClassifyAbility.setStatus('current')
ctPriClassifyPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 5, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyPorts.setStatus('current')
ctPriClassifyTableLastChange = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctPriClassifyTableLastChange.setStatus('current')
ctPriClassifyConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2))
ctPriClassifyGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 1))
ctPriClassifyCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 2))
ctPriClassifyBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 1, 1)).setObjects(("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyMaxEntries"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyNumEntries"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyIngressList"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyRowStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyRowInfo"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTOSStatus"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTOSValue"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyPorts"), ("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyTableLastChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctPriClassifyBaseGroup = ctPriClassifyBaseGroup.setStatus('current')
ctPriClassifyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14, 6, 2, 2, 1)).setObjects(("CTRON-PRIORITY-CLASSIFY-MIB", "ctPriClassifyBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctPriClassifyCompliance = ctPriClassifyCompliance.setStatus('current')
mibBuilder.exportSymbols("CTRON-PRIORITY-CLASSIFY-MIB", ctPriClassifyDataMask=ctPriClassifyDataMask, PortList=PortList, ctPriClassifyCompliances=ctPriClassifyCompliances, ctPriClassifyDataVal=ctPriClassifyDataVal, ctPriClassifyTOSValue=ctPriClassifyTOSValue, ctPriClassifyConformance=ctPriClassifyConformance, ctPriClassifyAbility=ctPriClassifyAbility, ctPriClassifyCompliance=ctPriClassifyCompliance, ctPriClassifyNumEntries=ctPriClassifyNumEntries, ctPriClassifyAbilityTable=ctPriClassifyAbilityTable, ctPriClassifyEntry=ctPriClassifyEntry, ctPriClassifyPorts=ctPriClassifyPorts, ctPriClassifyObjects=ctPriClassifyObjects, ctPriClassifyTableLastChange=ctPriClassifyTableLastChange, ctPriClassifyIngressList=ctPriClassifyIngressList, ctPriClassify=ctPriClassify, ctPriClassifyPriority=ctPriClassifyPriority, ctPriClassifyTOSStatus=ctPriClassifyTOSStatus, ctPriClassifyGroups=ctPriClassifyGroups, ctPriClassifyTable=ctPriClassifyTable, ctPriClassifyBaseGroup=ctPriClassifyBaseGroup, ctPriClassifyStatus=ctPriClassifyStatus, CtPriClassifyType=CtPriClassifyType, ctPriClassifyMaxEntries=ctPriClassifyMaxEntries, ctPriClassifyRowInfo=ctPriClassifyRowInfo, ctPriClassifyDataMeaning=ctPriClassifyDataMeaning, ctPriClassifyAbilityEntry=ctPriClassifyAbilityEntry, PYSNMP_MODULE_ID=ctPriClassify, ctPriClassifyRowStatus=ctPriClassifyRowStatus)
