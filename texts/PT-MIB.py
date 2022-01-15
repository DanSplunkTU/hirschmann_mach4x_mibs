#
# PySNMP MIB module PT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/PT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:02:04 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
miniLink, = mibBuilder.importSymbols("MINI-LINK-MIB", "miniLink")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ObjectIdentity, Bits, iso, Gauge32, NotificationType, Unsigned32, IpAddress, Counter64, Counter32, TimeTicks, MibIdentifier, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ObjectIdentity", "Bits", "iso", "Gauge32", "NotificationType", "Unsigned32", "IpAddress", "Counter64", "Counter32", "TimeTicks", "MibIdentifier", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
pt = ModuleIdentity((1, 3, 6, 1, 4, 1, 193, 223, 2))
pt.setRevisions(('2017-01-21 12:00', '2016-03-09 12:00', '2016-02-10 12:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pt.setRevisionsDescriptions(('MOC and MOI explained.', 'Validated.', 'The initial version of this MIB module.',))
if mibBuilder.loadTexts: pt.setLastUpdated('201701211200Z')
if mibBuilder.loadTexts: pt.setOrganization('Ericsson')
if mibBuilder.loadTexts: pt.setContactInfo('Anders Ekvall\n             Postal: Ericsson AB,\n             E-Mail: anders.ekvall@ericsson.com')
if mibBuilder.loadTexts: pt.setDescription('This is the MIB of PT specifics.\n            The entPhysical and ifIndex used are based on the MOC below:\n            IP_INTERFACE_MOC  10000\n            LANX_PORT_MOC     20000\n            WANX_PORT_MOC     30000\n            PT_MOC            40000\n            OM_MOC            50000\n            RMM_MOC           60000\n            SFP_MOC           70000\n            WIFI_MOC          80000\n            RJ45_MOC          90000\n            XPIC_MOC         100000\n            CT_MOC           110000\n            RLT_MOC          120000\n        \n            As MOI, slot and port are added according to:\n            Slot no * 100\n            Port no * 1\n            \n            For example an SFP in slot 1 port 3: 70103')
ptDeviceType = MibScalar((1, 3, 6, 1, 4, 1, 193, 223, 2, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ptDeviceType.setStatus('current')
if mibBuilder.loadTexts: ptDeviceType.setDescription("This object represents type of the PT. Always set to the\n             same value as 'sysObjectID'.")
ptConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 8))
ptCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 1))
ptGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 2))
ptCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 1, 1)).setObjects(("PT-MIB", "ptCompleteGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptCompliance = ptCompliance.setStatus('current')
if mibBuilder.loadTexts: ptCompliance.setDescription('The compliance statement for SNMP entities which implement everything.')
ptCompleteGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 193, 223, 2, 8, 2, 1)).setObjects(("PT-MIB", "ptDeviceType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ptCompleteGroup = ptCompleteGroup.setStatus('current')
if mibBuilder.loadTexts: ptCompleteGroup.setDescription('A collection of all current objects in this MIB module.')
mibBuilder.exportSymbols("PT-MIB", PYSNMP_MODULE_ID=pt, ptDeviceType=ptDeviceType, ptCompliance=ptCompliance, ptCompliances=ptCompliances, ptGroups=ptGroups, ptConformance=ptConformance, pt=pt, ptCompleteGroup=ptCompleteGroup)
