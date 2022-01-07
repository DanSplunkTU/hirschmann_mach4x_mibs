#
# PySNMP MIB module LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifGeneralInformationGroup, = mibBuilder.importSymbols("IF-MIB", "ifGeneralInformationGroup")
lldpV2Xdot1MIB, = mibBuilder.importSymbols("LLDP-EXT-DOT1-V2-MIB", "lldpV2Xdot1MIB")
lldpV2PortConfigEntry, lldpV2RemLocalDestMACAddress, lldpV2LocPortIfIndex, lldpV2RemLocalIfIndex, lldpV2RemTimeMark, lldpV2RemIndex = mibBuilder.importSymbols("LLDP-V2-MIB", "lldpV2PortConfigEntry", "lldpV2RemLocalDestMACAddress", "lldpV2LocPortIfIndex", "lldpV2RemLocalIfIndex", "lldpV2RemTimeMark", "lldpV2RemIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
lldpXDot1EvbExtensions = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1))
lldpXDot1EvbExtensions.setRevisions(('2018-06-21 00:00', '2014-12-15 00:00', '2012-02-15 00:00',))
if mibBuilder.loadTexts: lldpXDot1EvbExtensions.setLastUpdated('201806210000Z')
if mibBuilder.loadTexts: lldpXDot1EvbExtensions.setOrganization('IEEE 802.1 Working Group')
lldpXdot1StandAloneExtensions = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7))
lldpXdot1EvbMIB = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1))
lldpXdot1EvbObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1))
lldpXdot1EvbConfig = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1))
lldpXdot1EvbLocalData = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2))
lldpXdot1EvbRemoteData = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3))
lldpXdot1EvbConfigEvbTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 1), )
if mibBuilder.loadTexts: lldpXdot1EvbConfigEvbTable.setStatus('current')
lldpXdot1EvbConfigEvbEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 1, 1), )
lldpV2PortConfigEntry.registerAugmentions(("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpXdot1EvbConfigEvbEntry"))
lldpXdot1EvbConfigEvbEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXdot1EvbConfigEvbEntry.setStatus('current')
lldpXdot1EvbConfigEvbTxEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 1, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdot1EvbConfigEvbTxEnable.setStatus('current')
lldpXdot1EvbConfigCdcpTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 2), )
if mibBuilder.loadTexts: lldpXdot1EvbConfigCdcpTable.setStatus('current')
lldpXdot1EvbConfigCdcpEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 2, 1), )
lldpV2PortConfigEntry.registerAugmentions(("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpXdot1EvbConfigCdcpEntry"))
lldpXdot1EvbConfigCdcpEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
if mibBuilder.loadTexts: lldpXdot1EvbConfigCdcpEntry.setStatus('current')
lldpXdot1EvbConfigCdcpTxEnable = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 1, 2, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lldpXdot1EvbConfigCdcpTxEnable.setStatus('current')
lldpV2Xdot1LocEvbTlvTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 1), )
if mibBuilder.loadTexts: lldpV2Xdot1LocEvbTlvTable.setStatus('current')
lldpV2Xdot1LocEvbTlvEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 1, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"))
if mibBuilder.loadTexts: lldpV2Xdot1LocEvbTlvEntry.setStatus('current')
lldpV2Xdot1LocEvbTlvString = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 514))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2Xdot1LocEvbTlvString.setStatus('current')
lldpV2Xdot1LocCdcpTlvTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 2), )
if mibBuilder.loadTexts: lldpV2Xdot1LocCdcpTlvTable.setStatus('current')
lldpV2Xdot1LocCdcpTlvEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 2, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2LocPortIfIndex"))
if mibBuilder.loadTexts: lldpV2Xdot1LocCdcpTlvEntry.setStatus('current')
lldpV2Xdot1LocCdcpTlvString = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 2, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 514))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2Xdot1LocCdcpTlvString.setStatus('current')
lldpV2Xdot1RemEvbTlvTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 1), )
if mibBuilder.loadTexts: lldpV2Xdot1RemEvbTlvTable.setStatus('current')
lldpV2Xdot1RemEvbTlvEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 1, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2RemTimeMark"), (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"), (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"), (0, "LLDP-V2-MIB", "lldpV2RemIndex"))
if mibBuilder.loadTexts: lldpV2Xdot1RemEvbTlvEntry.setStatus('current')
lldpV2Xdot1RemEvbTlvString = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 514))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2Xdot1RemEvbTlvString.setStatus('current')
lldpV2Xdot1RemCdcpTlvTable = MibTable((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 2), )
if mibBuilder.loadTexts: lldpV2Xdot1RemCdcpTlvTable.setStatus('current')
lldpV2Xdot1RemCdcpTlvEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 2, 1), ).setIndexNames((0, "LLDP-V2-MIB", "lldpV2RemTimeMark"), (0, "LLDP-V2-MIB", "lldpV2RemLocalIfIndex"), (0, "LLDP-V2-MIB", "lldpV2RemLocalDestMACAddress"), (0, "LLDP-V2-MIB", "lldpV2RemIndex"))
if mibBuilder.loadTexts: lldpV2Xdot1RemCdcpTlvEntry.setStatus('current')
lldpV2Xdot1RemCdcpTlvString = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 1, 1, 3, 2, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 514))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lldpV2Xdot1RemCdcpTlvString.setStatus('current')
lldpXdot1EvbConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 2))
lldpXdot1EvbCompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 2, 1))
lldpXdot1EvbGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 2, 2))
lldpXdot1EvbCompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 2, 1, 1)).setObjects(("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpXdot1EvbGroup"), ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "ifGeneralInformationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot1EvbCompliance = lldpXdot1EvbCompliance.setStatus('current')
lldpXdot1EvbGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 13, 1, 5, 32962, 7, 1, 2, 2, 1)).setObjects(("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpXdot1EvbConfigEvbTxEnable"), ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpXdot1EvbConfigCdcpTxEnable"), ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpV2Xdot1LocEvbTlvString"), ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpV2Xdot1LocCdcpTlvString"), ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpV2Xdot1RemEvbTlvString"), ("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", "lldpV2Xdot1RemCdcpTlvString"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    lldpXdot1EvbGroup = lldpXdot1EvbGroup.setStatus('current')
mibBuilder.exportSymbols("LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB", lldpXdot1EvbCompliance=lldpXdot1EvbCompliance, lldpV2Xdot1LocCdcpTlvTable=lldpV2Xdot1LocCdcpTlvTable, lldpXDot1EvbExtensions=lldpXDot1EvbExtensions, lldpV2Xdot1RemCdcpTlvEntry=lldpV2Xdot1RemCdcpTlvEntry, lldpXdot1EvbConfig=lldpXdot1EvbConfig, lldpXdot1EvbGroups=lldpXdot1EvbGroups, lldpXdot1EvbConfigEvbTxEnable=lldpXdot1EvbConfigEvbTxEnable, lldpXdot1EvbCompliances=lldpXdot1EvbCompliances, lldpV2Xdot1LocEvbTlvEntry=lldpV2Xdot1LocEvbTlvEntry, lldpXdot1EvbConfigEvbTable=lldpXdot1EvbConfigEvbTable, lldpXdot1EvbMIB=lldpXdot1EvbMIB, lldpV2Xdot1RemEvbTlvTable=lldpV2Xdot1RemEvbTlvTable, lldpV2Xdot1RemEvbTlvString=lldpV2Xdot1RemEvbTlvString, lldpXdot1EvbConformance=lldpXdot1EvbConformance, lldpV2Xdot1LocCdcpTlvEntry=lldpV2Xdot1LocCdcpTlvEntry, lldpXdot1EvbRemoteData=lldpXdot1EvbRemoteData, lldpXdot1EvbConfigCdcpEntry=lldpXdot1EvbConfigCdcpEntry, lldpXdot1StandAloneExtensions=lldpXdot1StandAloneExtensions, lldpV2Xdot1LocEvbTlvTable=lldpV2Xdot1LocEvbTlvTable, lldpXdot1EvbGroup=lldpXdot1EvbGroup, lldpXdot1EvbConfigCdcpTable=lldpXdot1EvbConfigCdcpTable, PYSNMP_MODULE_ID=lldpXDot1EvbExtensions, lldpXdot1EvbObjects=lldpXdot1EvbObjects, lldpV2Xdot1LocEvbTlvString=lldpV2Xdot1LocEvbTlvString, lldpV2Xdot1RemCdcpTlvString=lldpV2Xdot1RemCdcpTlvString, lldpV2Xdot1RemCdcpTlvTable=lldpV2Xdot1RemCdcpTlvTable, lldpV2Xdot1LocCdcpTlvString=lldpV2Xdot1LocCdcpTlvString, lldpV2Xdot1RemEvbTlvEntry=lldpV2Xdot1RemEvbTlvEntry, lldpXdot1EvbLocalData=lldpXdot1EvbLocalData, lldpXdot1EvbConfigEvbEntry=lldpXdot1EvbConfigEvbEntry, lldpXdot1EvbConfigCdcpTxEnable=lldpXdot1EvbConfigCdcpTxEnable)
