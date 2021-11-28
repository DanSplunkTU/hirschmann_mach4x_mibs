#
# PySNMP MIB module BENU-PLATFORM-DEFN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-PLATFORM-DEFN-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:33:42 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
benuPlatform, = mibBuilder.importSymbols("BENU-PLATFORM-MIB", "benuPlatform")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, Integer32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Unsigned32, NotificationType, TimeTicks, MibIdentifier, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Integer32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Unsigned32", "NotificationType", "TimeTicks", "MibIdentifier", "Gauge32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuPlatformDefn = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 1, 2))
benuPlatformDefn.setRevisions(('2016-11-17 00:00', '2016-10-13 00:00', '2016-04-12 00:00', '2012-10-18 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benuPlatformDefn.setRevisionsDescriptions(('Updated platform types', 'Changed vMEG to xMEG', 'Changed benuVSE to vMEG', 'Initial Version.',))
if mibBuilder.loadTexts: benuPlatformDefn.setLastUpdated('201611170000Z')
if mibBuilder.loadTexts: benuPlatformDefn.setOrganization('Benu Networks,Inc')
if mibBuilder.loadTexts: benuPlatformDefn.setContactInfo('Benu Networks,Inc\n                          Corporate Headquarters\n                          300 Concord Road, Suite 110\n                          Billerica, MA 01821 USA\n                          Tel: +1 978-223-4700\n                          Fax: +1 978-362-1908\n                          Email: info@benunets.com')
if mibBuilder.loadTexts: benuPlatformDefn.setDescription('This module defines the object identifiers that are\n                 assigned to various hardware platforms')
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
mibBuilder.exportSymbols("BENU-PLATFORM-DEFN-MIB", benuChassisTypes=benuChassisTypes, benuChassisTypeMEG50=benuChassisTypeMEG50, benuPortMultiBind=benuPortMultiBind, benuCardRSM=benuCardRSM, Benu_Internal=Benu_Internal, benuPortLag=benuPortLag, benuCardSEFP=benuCardSEFP, PYSNMP_MODULE_ID=benuPlatformDefn, benuChassisTypeMEG1200=benuChassisTypeMEG1200, Benu_KVM=Benu_KVM, Benu_xMEG_10=Benu_xMEG_10, benuCardTypes=benuCardTypes, benuPortT1=benuPortT1, benuPortMultiBindLastResort=benuPortMultiBindLastResort, benuCardShelfMgr=benuCardShelfMgr, benuCardUnknown=benuCardUnknown, benuPlatformTypes=benuPlatformTypes, benuPortTunnel=benuPortTunnel, benuPortLoopback=benuPortLoopback, benuCardSwitchFabric=benuCardSwitchFabric, benuPortUnknown=benuPortUnknown, benuChassisTypeMEG100=benuChassisTypeMEG100, benuChassisTypeMEG400=benuChassisTypeMEG400, benuPortEthernet=benuPortEthernet, benuPlatformDefn=benuPlatformDefn, Benu_VirtualBox=Benu_VirtualBox, benuPortPOS=benuPortPOS, benuCardIO=benuCardIO, benuPortNULL=benuPortNULL, benuPortGige=benuPortGige, benuPortATM=benuPortATM, Benu_VMware=Benu_VMware, Benu_Virtual=Benu_Virtual, benuPortBridge=benuPortBridge, benuPortTypes=benuPortTypes, benuCardSwitchMesh=benuCardSwitchMesh, benuPortIpGre=benuPortIpGre, benuPortl2tp=benuPortl2tp, Benu_xMEG_100=Benu_xMEG_100, platformUnknown=platformUnknown, benuChassisTypeUnknown=benuChassisTypeUnknown)
