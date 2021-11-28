#
# PySNMP MIB module JUNIPER-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/JUNIPER-SMI
# Produced by pysmi-1.1.3 at Sun Nov 28 20:27:42 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, enterprises, Integer32, NotificationType, MibIdentifier, IpAddress, Counter64, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity, TimeTicks, Counter32, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "enterprises", "Integer32", "NotificationType", "MibIdentifier", "IpAddress", "Counter64", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity", "TimeTicks", "Counter32", "Gauge32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
juniperMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636))
juniperMIB.setRevisions(('2009-10-29 00:00', '2003-04-17 01:00', '2005-08-17 01:00', '2006-12-14 01:00', '2007-01-01 00:00', '2007-10-09 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: juniperMIB.setRevisionsDescriptions(('Added jnxCosNotifications branch.', 'Added jnxExperiment branch.', 'Added jnxNsm branch.', 'Added jnxCA branch.', 'Added jnxUtilMibRoot branch.', 'Added jnxAdvancedInsightMgr branch.',))
if mibBuilder.loadTexts: juniperMIB.setLastUpdated('200910290000Z')
if mibBuilder.loadTexts: juniperMIB.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: juniperMIB.setContactInfo('        Juniper Technical Assistance Center\n\t\t     Juniper Networks, Inc.\n\t\t     1194 N. Mathilda Avenue\n\t\t     Sunnyvale, CA 94089\n\t\t     E-mail: support@juniper.net')
if mibBuilder.loadTexts: juniperMIB.setDescription('The Structure of Management Information for Juniper Networks.')
jnxProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 1))
if mibBuilder.loadTexts: jnxProducts.setStatus('current')
if mibBuilder.loadTexts: jnxProducts.setDescription("The root of Juniper's Product OIDs.")
jnxReservedProducts1 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 2))
jnxReservedProducts2 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 3))
jnxReservedProducts3 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 4))
jnxReservedProducts4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 5))
jnxReservedProducts5 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 1, 6))
jnxServices = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 2))
if mibBuilder.loadTexts: jnxServices.setStatus('current')
if mibBuilder.loadTexts: jnxServices.setDescription("The root of Juniper's Services OIDs.")
jnxMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 3))
if mibBuilder.loadTexts: jnxMibs.setStatus('current')
if mibBuilder.loadTexts: jnxMibs.setDescription("The root of Juniper's MIB objects.")
jnxJsMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 39))
jnxExMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 40))
jnxWxMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 41))
jnxReservedMibs4 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 42))
jnxReservedMibs5 = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 43))
jnxPfeMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 44))
jnxBfdMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 45))
jnxXstpMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 46))
jnxUtilMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 47))
jnxl2aldMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 48))
jnxL2tpMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 49))
jnxRpmMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 50))
jnxUserAAAMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 51))
jnxIpSecMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 52))
jnxL2cpMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 53))
jnxPwTdmMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 54))
jnxPwTCMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 55))
jnxOtnMibRoot = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 56))
jnxTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 2636, 4))
if mibBuilder.loadTexts: jnxTraps.setStatus('current')
if mibBuilder.loadTexts: jnxTraps.setDescription("The root of Juniper's Trap OIDs.")
jnxChassisTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 1))
jnxChassisOKTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 2))
jnxRmonTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 3))
jnxLdpTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 4))
jnxCmNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 5))
jnxSonetNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 6))
jnxPMonNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 7))
jnxCollectorNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 8))
jnxPingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 9))
jnxSpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 10))
jnxDfcNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 11))
jnxSyslogNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 12))
jnxEventNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 13))
jnxVccpNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 14))
jnxOtnNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 15))
jnxSAIDPNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 16))
jnxCosNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 4, 17))
jnxExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 5))
jnxNsm = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 6))
jnxCA = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 7))
jnxAAA = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 8))
jnxAdvancedInsightMgr = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 9))
mibBuilder.exportSymbols("JUNIPER-SMI", jnxJsMibRoot=jnxJsMibRoot, jnxXstpMibs=jnxXstpMibs, jnxReservedMibs4=jnxReservedMibs4, jnxReservedMibs5=jnxReservedMibs5, jnxCmNotifications=jnxCmNotifications, jnxBfdMibRoot=jnxBfdMibRoot, jnxl2aldMibRoot=jnxl2aldMibRoot, jnxL2cpMibRoot=jnxL2cpMibRoot, jnxUtilMibRoot=jnxUtilMibRoot, jnxReservedProducts5=jnxReservedProducts5, jnxTraps=jnxTraps, jnxAAA=jnxAAA, jnxCollectorNotifications=jnxCollectorNotifications, jnxEventNotifications=jnxEventNotifications, jnxPMonNotifications=jnxPMonNotifications, jnxReservedProducts3=jnxReservedProducts3, jnxReservedProducts1=jnxReservedProducts1, jnxPfeMibRoot=jnxPfeMibRoot, jnxLdpTraps=jnxLdpTraps, jnxRpmMibRoot=jnxRpmMibRoot, jnxIpSecMibRoot=jnxIpSecMibRoot, jnxWxMibRoot=jnxWxMibRoot, jnxSyslogNotifications=jnxSyslogNotifications, jnxNsm=jnxNsm, jnxChassisOKTraps=jnxChassisOKTraps, jnxCA=jnxCA, PYSNMP_MODULE_ID=juniperMIB, jnxSonetNotifications=jnxSonetNotifications, jnxPingNotifications=jnxPingNotifications, jnxOtnMibRoot=jnxOtnMibRoot, jnxSAIDPNotifications=jnxSAIDPNotifications, juniperMIB=juniperMIB, jnxAdvancedInsightMgr=jnxAdvancedInsightMgr, jnxMibs=jnxMibs, jnxOtnNotifications=jnxOtnNotifications, jnxServices=jnxServices, jnxSpNotifications=jnxSpNotifications, jnxReservedProducts4=jnxReservedProducts4, jnxProducts=jnxProducts, jnxExMibRoot=jnxExMibRoot, jnxVccpNotifications=jnxVccpNotifications, jnxPwTdmMibRoot=jnxPwTdmMibRoot, jnxUserAAAMibRoot=jnxUserAAAMibRoot, jnxRmonTraps=jnxRmonTraps, jnxL2tpMibRoot=jnxL2tpMibRoot, jnxPwTCMibRoot=jnxPwTCMibRoot, jnxExperiment=jnxExperiment, jnxCosNotifications=jnxCosNotifications, jnxDfcNotifications=jnxDfcNotifications, jnxReservedProducts2=jnxReservedProducts2, jnxChassisTraps=jnxChassisTraps)
