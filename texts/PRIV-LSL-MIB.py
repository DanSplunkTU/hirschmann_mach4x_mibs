#
# PySNMP MIB module PRIV-LSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRIV-LSL-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:48 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, iso, Integer32, Counter32, IpAddress, Bits, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Gauge32, TimeTicks, NotificationType, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Integer32", "Counter32", "IpAddress", "Bits", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Gauge32", "TimeTicks", "NotificationType", "Unsigned32")
DisplayString, MacAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "MacAddress", "TextualConvention")
privLsl = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 113))
privLsl.setRevisions(('2008-03-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: privLsl.setRevisionsDescriptions(('Initial',))
if mibBuilder.loadTexts: privLsl.setLastUpdated('200803210000Z')
if mibBuilder.loadTexts: privLsl.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: privLsl.setContactInfo(' BATM/Telco Systems Support team\nEmail:\nFor North America: techsupport@telco.com\nFor North Europe: support@batm.de, info@batm.de\nFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: privLsl.setDescription('MIB module for management of Logical Service Loopback(LSL) Iometrix compatible product.')
privLslLevel1 = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1))
privLslObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1))
privLslNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 2))
privLslConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3))
class PrivLslStates(TextualConvention, Integer32):
    description = 'The the switch on/off states for LSL on ports.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

privLslGlobalMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 1), MacAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: privLslGlobalMacAddress.setStatus('current')
if mibBuilder.loadTexts: privLslGlobalMacAddress.setDescription('This object defines the destination mac address assigned\nto lsl packets. The device can recognise the lsl packets\nby a specific destination mac address given by this\nobject.\n')
privLslManagementTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2), )
if mibBuilder.loadTexts: privLslManagementTable.setStatus('current')
if mibBuilder.loadTexts: privLslManagementTable.setDescription('LSL interface extention table.\nThis table contains all objects which are used for LSL\nmanagement per interface. It uses ifIndex defined in\nrfc1213')
privLslManagementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: privLslManagementEntry.setStatus('current')
if mibBuilder.loadTexts: privLslManagementEntry.setDescription('The only valid LSL interfaces are phyical port interfaces')
privLslStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 2, 1, 1), PrivLslStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: privLslStatus.setStatus('current')
if mibBuilder.loadTexts: privLslStatus.setDescription('This object indicates whether the port have Logical Service\nLoopback enabled or disabled. It allows the client to\ndetermine which interface should be used for this type\nof service')
privIometrixManagementTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3), )
if mibBuilder.loadTexts: privIometrixManagementTable.setStatus('current')
if mibBuilder.loadTexts: privIometrixManagementTable.setDescription('Iometrix Level 1 table.\nThis table contains all objects which are used for Iometrix\nlevel 1 management per interface. It uses ifIndex defined in\nrfc1213')
privIometrixManagementEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: privIometrixManagementEntry.setStatus('current')
if mibBuilder.loadTexts: privIometrixManagementEntry.setDescription('the index is ifindex')
privIometrixStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 1, 3, 1, 1), PrivLslStates()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: privIometrixStatus.setStatus('current')
if mibBuilder.loadTexts: privIometrixStatus.setDescription('This object indicates whether the port have Logical Service\nLoopback enabled or disabled. It allows the client to\ndetermine which interface should be used for this type\nof service')
privLslGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 1))
privLslCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 2))
privLevel1ObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 1, 1)).setObjects(("PRIV-LSL-MIB", "privLslGlobalMacAddress"), ("PRIV-LSL-MIB", "privLslStatus"), ("PRIV-LSL-MIB", "privIometrixStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    privLevel1ObjectsGroup = privLevel1ObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: privLevel1ObjectsGroup.setDescription('All objects related to level1 logical loopback service. Object\ngrouping will be extended if the mib is also extended')
privLevel1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 5, 113, 1, 3, 2, 1)).setObjects(("PRIV-LSL-MIB", "privLevel1ObjectsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    privLevel1Compliance = privLevel1Compliance.setStatus('current')
if mibBuilder.loadTexts: privLevel1Compliance.setDescription('The compliance statement. It will be extended if new\nfunctionality is added')
mibBuilder.exportSymbols("PRIV-LSL-MIB", privLslGlobalMacAddress=privLslGlobalMacAddress, privLslLevel1=privLslLevel1, privLslNotifications=privLslNotifications, privIometrixStatus=privIometrixStatus, privLslManagementTable=privLslManagementTable, privLsl=privLsl, privLslManagementEntry=privLslManagementEntry, privLslCompliances=privLslCompliances, privLevel1ObjectsGroup=privLevel1ObjectsGroup, privLslStatus=privLslStatus, PYSNMP_MODULE_ID=privLsl, privIometrixManagementTable=privIometrixManagementTable, privLslGroups=privLslGroups, privLevel1Compliance=privLevel1Compliance, privIometrixManagementEntry=privIometrixManagementEntry, privLslObjects=privLslObjects, PrivLslStates=PrivLslStates, privLslConformance=privLslConformance)
