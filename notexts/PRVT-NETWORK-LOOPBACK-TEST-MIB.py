#
# PySNMP MIB module PRVT-NETWORK-LOOPBACK-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-NETWORK-LOOPBACK-TEST-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:45:45 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
accessListControlListGroup, = mibBuilder.importSymbols("PRVT-SWITCH-ACCESS-LIST-MIB", "accessListControlListGroup")
ipSwitch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "ipSwitch")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Counter32, Bits, Integer32, ModuleIdentity, iso, Counter64, ObjectIdentity, Gauge32, IpAddress, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Integer32", "ModuleIdentity", "iso", "Counter64", "ObjectIdentity", "Gauge32", "IpAddress", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier", "Unsigned32")
DisplayString, TextualConvention, RowStatus, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TimeStamp")
prvtNetworkLoopbackTestMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 6, 7))
prvtNetworkLoopbackTestMib.setRevisions(('2010-08-31 00:00',))
if mibBuilder.loadTexts: prvtNetworkLoopbackTestMib.setLastUpdated('201008310000Z')
if mibBuilder.loadTexts: prvtNetworkLoopbackTestMib.setOrganization('BATM Advanced Communication')
prvtNetworkLoopbackTestNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 0))
prvtNetworkLoopbackTestObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1))
prvtNetworkLoopbackTestConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2))
prvtNetworkLoopbackTestTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1), )
if mibBuilder.loadTexts: prvtNetworkLoopbackTestTable.setStatus('current')
prvtNetworkLoopbackTestEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PRVT-SWITCH-ACCESS-LIST-MIB", "accessListControlListGroup"))
if mibBuilder.loadTexts: prvtNetworkLoopbackTestEntry.setStatus('current')
prvtNetworkLoopTestDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100000))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtNetworkLoopTestDuration.setStatus('current')
prvtNetworkLoopStartDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1, 1, 2), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtNetworkLoopStartDuration.setStatus('current')
prvtNetworkLoopEndDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1, 1, 3), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtNetworkLoopEndDuration.setStatus('current')
prvtNetworkLoopRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 1, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtNetworkLoopRowStatus.setStatus('current')
prvtNetworkLoopbackTestFinish = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 0, 1)).setObjects(("IF-MIB", "ifIndex"), ("PRVT-SWITCH-ACCESS-LIST-MIB", "accessListControlListGroup"))
if mibBuilder.loadTexts: prvtNetworkLoopbackTestFinish.setStatus('current')
prvtNetworkLoopTestCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2, 1))
prvtNetworkLoopTestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2, 2))
prvtNetworkLoopTestCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2, 1, 1)).setObjects(("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopTestGroup"), ("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopTestNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtNetworkLoopTestCompliance = prvtNetworkLoopTestCompliance.setStatus('current')
prvtNetworkLoopTestGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2, 2, 1)).setObjects(("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopTestDuration"), ("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopStartDuration"), ("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopEndDuration"), ("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtNetworkLoopTestGroup = prvtNetworkLoopTestGroup.setStatus('current')
prvtNetworkLoopTestNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 738, 1, 6, 7, 2, 2, 2)).setObjects(("PRVT-NETWORK-LOOPBACK-TEST-MIB", "prvtNetworkLoopbackTestFinish"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtNetworkLoopTestNotificationsGroup = prvtNetworkLoopTestNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("PRVT-NETWORK-LOOPBACK-TEST-MIB", prvtNetworkLoopTestGroup=prvtNetworkLoopTestGroup, prvtNetworkLoopbackTestConformance=prvtNetworkLoopbackTestConformance, prvtNetworkLoopTestGroups=prvtNetworkLoopTestGroups, prvtNetworkLoopbackTestNotifications=prvtNetworkLoopbackTestNotifications, prvtNetworkLoopbackTestMib=prvtNetworkLoopbackTestMib, prvtNetworkLoopbackTestTable=prvtNetworkLoopbackTestTable, prvtNetworkLoopTestCompliances=prvtNetworkLoopTestCompliances, PYSNMP_MODULE_ID=prvtNetworkLoopbackTestMib, prvtNetworkLoopTestNotificationsGroup=prvtNetworkLoopTestNotificationsGroup, prvtNetworkLoopTestDuration=prvtNetworkLoopTestDuration, prvtNetworkLoopStartDuration=prvtNetworkLoopStartDuration, prvtNetworkLoopbackTestEntry=prvtNetworkLoopbackTestEntry, prvtNetworkLoopbackTestFinish=prvtNetworkLoopbackTestFinish, prvtNetworkLoopEndDuration=prvtNetworkLoopEndDuration, prvtNetworkLoopRowStatus=prvtNetworkLoopRowStatus, prvtNetworkLoopbackTestObjects=prvtNetworkLoopbackTestObjects, prvtNetworkLoopTestCompliance=prvtNetworkLoopTestCompliance)
