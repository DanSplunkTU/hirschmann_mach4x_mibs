#
# PySNMP MIB module BENU-PLATFORM-DEFN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-DEFN-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:11:16 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Counter32, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Gauge32, TimeTicks, MibIdentifier, ObjectIdentity, iso, Unsigned32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Gauge32", "TimeTicks", "MibIdentifier", "ObjectIdentity", "iso", "Unsigned32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
benuPlatformDefn = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 2))
benuPlatformDefn.setRevisions(('2016-11-17 00:00', '2016-10-13 00:00', '2016-04-12 00:00', '2012-10-18 00:00',))
if mibBuilder.loadTexts: benuPlatformDefn.setLastUpdated('201611170000Z')
if mibBuilder.loadTexts: benuPlatformDefn.setOrganization('Benu Networks,Inc')
benuPlatformTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1))
platformUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 0))
Benu_xMEG_100 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 1)).setLabel("Benu-xMEG-100")
Benu_xMEG_10 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 2)).setLabel("Benu-xMEG-10")
Benu_Internal = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 3)).setLabel("Benu-Internal")
Benu_Virtual = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 4)).setLabel("Benu-Virtual")
Benu_KVM = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 5)).setLabel("Benu-KVM")
Benu_VMware = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 6)).setLabel("Benu-VMware")
Benu_VirtualBox = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 1, 7)).setLabel("Benu-VirtualBox")
benuChassisTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2))
benuChassisTypeUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 0))
benuChassisTypeMEG100 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 1))
benuChassisTypeMEG400 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 2))
benuChassisTypeMEG1200 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 3))
benuChassisTypeMEG50 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 2, 4))
benuCardTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3))
benuCardUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 0))
benuCardRSM = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 1))
benuCardSwitchFabric = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 2))
benuCardShelfMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 3))
benuCardSEFP = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 4))
benuCardIO = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 5))
benuCardSwitchMesh = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 3, 6))
benuPortTypes = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4))
benuPortUnknown = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 0))
benuPortGige = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 1))
benuPortEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 2))
benuPortl2tp = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 3))
benuPortLoopback = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 4))
benuPortT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 5))
benuPortNULL = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 6))
benuPortTunnel = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 7))
benuPortPOS = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 8))
benuPortATM = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 9))
benuPortIpGre = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 10))
benuPortBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 11))
benuPortLag = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 12))
benuPortMultiBind = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 13))
benuPortMultiBindLastResort = MibIdentifier((1, 3, 6, 1, 4, 1, 39406, 1, 2, 4, 14))
mibBuilder.exportSymbols("BENU-PLATFORM-DEFN-MIB", benuCardSEFP=benuCardSEFP, PYSNMP_MODULE_ID=benuPlatformDefn, benuPortT1=benuPortT1, Benu_Internal=Benu_Internal, benuPortBridge=benuPortBridge, benuPortUnknown=benuPortUnknown, benuPortNULL=benuPortNULL, benuCardRSM=benuCardRSM, benuPortIpGre=benuPortIpGre, Benu_xMEG_100=Benu_xMEG_100, benuPortATM=benuPortATM, benuChassisTypeMEG400=benuChassisTypeMEG400, benuChassisTypes=benuChassisTypes, benuPortl2tp=benuPortl2tp, benuChassisTypeMEG50=benuChassisTypeMEG50, benuPortLag=benuPortLag, benuCardUnknown=benuCardUnknown, benuChassisTypeMEG1200=benuChassisTypeMEG1200, benuCardShelfMgr=benuCardShelfMgr, benuCardSwitchMesh=benuCardSwitchMesh, benuPortTypes=benuPortTypes, benuPortLoopback=benuPortLoopback, Benu_VMware=Benu_VMware, benuPortMultiBind=benuPortMultiBind, benuPortGige=benuPortGige, benuChassisTypeMEG100=benuChassisTypeMEG100, Benu_xMEG_10=Benu_xMEG_10, benuChassisTypeUnknown=benuChassisTypeUnknown, platformUnknown=platformUnknown, benuCardIO=benuCardIO, benuPortMultiBindLastResort=benuPortMultiBindLastResort, Benu_Virtual=Benu_Virtual, benuCardSwitchFabric=benuCardSwitchFabric, benuCardTypes=benuCardTypes, benuPortEthernet=benuPortEthernet, benuPortTunnel=benuPortTunnel, benuPlatformDefn=benuPlatformDefn, benuPortPOS=benuPortPOS, Benu_KVM=Benu_KVM, benuPlatformTypes=benuPlatformTypes, Benu_VirtualBox=Benu_VirtualBox)
