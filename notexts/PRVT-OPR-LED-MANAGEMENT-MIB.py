#
# PySNMP MIB module PRVT-OPR-LED-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-OPR-LED-MANAGEMENT-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
prvtOprLedMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 110))
prvtOprLedMgmtMIB.setRevisions(('2006-07-29 00:00',))
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setLastUpdated('200607290000Z')
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setOrganization('BATM Advanced Communication')
class LedValues(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("green-stable", 1), ("green-blinking", 2), ("amber-stable", 3), ("amber-blinking", 4), ("red-stable", 5), ("red-blinking", 6))

prvtOprLedMgmtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 1))
prvtOprLedMgmtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 2))
prvtOprLedMgmtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 3))
prvtOprLedSatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 1, 1), LedValues().clone('green-stable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtOprLedSatus.setStatus('current')
mibBuilder.exportSymbols("PRVT-OPR-LED-MANAGEMENT-MIB", prvtOprLedSatus=prvtOprLedSatus, PYSNMP_MODULE_ID=prvtOprLedMgmtMIB, prvtOprLedMgmtConformance=prvtOprLedMgmtConformance, LedValues=LedValues, prvtOprLedMgmtMIB=prvtOprLedMgmtMIB, prvtOprLedMgmtObjects=prvtOprLedMgmtObjects, prvtOprLedMgmtNotifications=prvtOprLedMgmtNotifications)
