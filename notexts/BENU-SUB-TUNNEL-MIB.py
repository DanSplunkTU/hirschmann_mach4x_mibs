#
# PySNMP MIB module BENU-SUB-TUNNEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-SUB-TUNNEL-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:08:03 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
benuWAG, = mibBuilder.importSymbols("BENU-WAG-MIB", "benuWAG")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, iso, Gauge32, Integer32, ModuleIdentity, NotificationType, Unsigned32, Counter32, Bits, ObjectIdentity, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "iso", "Gauge32", "Integer32", "ModuleIdentity", "NotificationType", "Unsigned32", "Counter32", "Bits", "ObjectIdentity", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuWagSubTunMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2))
benuWagSubTunMIB.setRevisions(('2015-11-13 00:00', '2015-01-02 00:00', '2012-12-12 00:00',))
if mibBuilder.loadTexts: benuWagSubTunMIB.setLastUpdated('201511130000Z')
if mibBuilder.loadTexts: benuWagSubTunMIB.setOrganization('Benu Networks,Inc')
bWagSubTunnelMIBNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0))
if mibBuilder.loadTexts: bWagSubTunnelMIBNotifications.setStatus('current')
bWagSubMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 1))
if mibBuilder.loadTexts: bWagSubMIBObjects.setStatus('current')
bWagSubMIBNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 2))
if mibBuilder.loadTexts: bWagSubMIBNotifObjects.setStatus('current')
bWagTunnelMIBObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 3))
if mibBuilder.loadTexts: bWagTunnelMIBObjects.setStatus('current')
bWagTunnelMIBNotifObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 4))
if mibBuilder.loadTexts: bWagTunnelMIBNotifObjects.setStatus('current')
bWagSubMaxNumOfSubscribers = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bWagSubMaxNumOfSubscribers.setStatus('current')
bWagTunMaxNumOfTunnels = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 3, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bWagTunMaxNumOfTunnels.setStatus('current')
bWagSubHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bWagSubHighThreshold.setStatus('current')
bWagSubLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 2, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bWagSubLowThreshold.setStatus('current')
bWagSubHighThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 1)).setObjects(("BENU-SUB-TUNNEL-MIB", "bWagSubMaxNumOfSubscribers"), ("BENU-SUB-TUNNEL-MIB", "bWagSubHighThreshold"))
if mibBuilder.loadTexts: bWagSubHighThresholdReached.setStatus('current')
bWagSubLowThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 2)).setObjects(("BENU-SUB-TUNNEL-MIB", "bWagSubMaxNumOfSubscribers"), ("BENU-SUB-TUNNEL-MIB", "bWagSubLowThreshold"))
if mibBuilder.loadTexts: bWagSubLowThresholdReached.setStatus('current')
bWagTunHighThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 4, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bWagTunHighThreshold.setStatus('current')
bWagTunLowThreshold = MibScalar((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 4, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bWagTunLowThreshold.setStatus('current')
bWagTunHighThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 3)).setObjects(("BENU-SUB-TUNNEL-MIB", "bWagTunMaxNumOfTunnels"), ("BENU-SUB-TUNNEL-MIB", "bWagTunHighThreshold"))
if mibBuilder.loadTexts: bWagTunHighThresholdReached.setStatus('current')
bWagTunLowThresholdReached = NotificationType((1, 3, 6, 1, 4, 1, 39406, 2, 1, 2, 0, 4)).setObjects(("BENU-SUB-TUNNEL-MIB", "bWagTunMaxNumOfTunnels"), ("BENU-SUB-TUNNEL-MIB", "bWagTunLowThreshold"))
if mibBuilder.loadTexts: bWagTunLowThresholdReached.setStatus('current')
mibBuilder.exportSymbols("BENU-SUB-TUNNEL-MIB", bWagTunMaxNumOfTunnels=bWagTunMaxNumOfTunnels, bWagTunHighThreshold=bWagTunHighThreshold, bWagSubHighThreshold=bWagSubHighThreshold, bWagSubLowThreshold=bWagSubLowThreshold, PYSNMP_MODULE_ID=benuWagSubTunMIB, bWagSubMIBObjects=bWagSubMIBObjects, bWagTunnelMIBObjects=bWagTunnelMIBObjects, bWagTunLowThresholdReached=bWagTunLowThresholdReached, bWagSubTunnelMIBNotifications=bWagSubTunnelMIBNotifications, benuWagSubTunMIB=benuWagSubTunMIB, bWagTunnelMIBNotifObjects=bWagTunnelMIBNotifObjects, bWagSubLowThresholdReached=bWagSubLowThresholdReached, bWagTunHighThresholdReached=bWagTunHighThresholdReached, bWagSubMaxNumOfSubscribers=bWagSubMaxNumOfSubscribers, bWagSubHighThresholdReached=bWagSubHighThresholdReached, bWagTunLowThreshold=bWagTunLowThreshold, bWagSubMIBNotifObjects=bWagSubMIBNotifObjects)
