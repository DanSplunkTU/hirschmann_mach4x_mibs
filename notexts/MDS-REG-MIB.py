#
# PySNMP MIB module MDS-REG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-REG-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:04:10 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Unsigned32, TimeTicks, ModuleIdentity, Counter64, ObjectIdentity, Counter32, IpAddress, Bits, enterprises, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Unsigned32", "TimeTicks", "ModuleIdentity", "Counter64", "ObjectIdentity", "Counter32", "IpAddress", "Bits", "enterprises", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mdsGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 4))
mdsGlobalRegModule.setRevisions(('2006-02-08 00:00',))
if mibBuilder.loadTexts: mdsGlobalRegModule.setLastUpdated('200602080000Z')
if mibBuilder.loadTexts: mdsGlobalRegModule.setOrganization('Microwave Data Systems, Inc.')
mdsRoot = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130))
if mibBuilder.loadTexts: mdsRoot.setStatus('current')
mdsWideband = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 1))
if mibBuilder.loadTexts: mdsWideband.setStatus('current')
mdsPointToPoint = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 1, 1))
if mibBuilder.loadTexts: mdsPointToPoint.setStatus('current')
mdsNarrowband = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 2))
if mibBuilder.loadTexts: mdsNarrowband.setStatus('current')
mdsPointToMultiPoint = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 2, 1))
if mibBuilder.loadTexts: mdsPointToMultiPoint.setStatus('current')
mdsBroadband = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 3))
if mibBuilder.loadTexts: mdsBroadband.setStatus('current')
mdsSoftware = ObjectIdentity((1, 3, 6, 1, 4, 1, 4130, 9))
if mibBuilder.loadTexts: mdsSoftware.setStatus('current')
mibBuilder.exportSymbols("MDS-REG-MIB", mdsBroadband=mdsBroadband, mdsSoftware=mdsSoftware, mdsPointToMultiPoint=mdsPointToMultiPoint, mdsGlobalRegModule=mdsGlobalRegModule, PYSNMP_MODULE_ID=mdsGlobalRegModule, mdsWideband=mdsWideband, mdsNarrowband=mdsNarrowband, mdsRoot=mdsRoot, mdsPointToPoint=mdsPointToPoint)
