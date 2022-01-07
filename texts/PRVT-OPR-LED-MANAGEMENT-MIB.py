#
# PySNMP MIB module PRVT-OPR-LED-MANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-OPR-LED-MANAGEMENT-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:39:26 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Unsigned32, iso, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, NotificationType, Counter32, Counter64, MibIdentifier, IpAddress, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Unsigned32", "iso", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "NotificationType", "Counter32", "Counter64", "MibIdentifier", "IpAddress", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
prvtOprLedMgmtMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 110))
prvtOprLedMgmtMIB.setRevisions(('2006-07-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setRevisionsDescriptions(('Initial revision history',))
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setLastUpdated('200607290000Z')
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setContactInfo('BATM/Telco Systems Support team\nEmail:\nFor North America: techsupport@telco.com\nFor North Europe: support@batm.de, info@batm.de\nFor the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtOprLedMgmtMIB.setDescription('Initial version. This MIB will provied a way to control\nthe status of the state OPR LED for certain switches')
class LedValues(TextualConvention, Integer32):
    description = 'All possible led states'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("green-stable", 1), ("green-blinking", 2), ("amber-stable", 3), ("amber-blinking", 4), ("red-stable", 5), ("red-blinking", 6))

prvtOprLedMgmtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 1))
prvtOprLedMgmtNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 2))
prvtOprLedMgmtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 3))
prvtOprLedSatus = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 110, 1, 1), LedValues().clone('green-stable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtOprLedSatus.setStatus('current')
if mibBuilder.loadTexts: prvtOprLedSatus.setDescription('All possible led states. States red-stable and red-blinking\ncan not be set. States amber-stable and amber-blinking green-blinking can\nbe set only when the current state is green-stable. The object\nhas read-write access and its default value is green-stable')
mibBuilder.exportSymbols("PRVT-OPR-LED-MANAGEMENT-MIB", prvtOprLedMgmtMIB=prvtOprLedMgmtMIB, LedValues=LedValues, prvtOprLedSatus=prvtOprLedSatus, PYSNMP_MODULE_ID=prvtOprLedMgmtMIB, prvtOprLedMgmtObjects=prvtOprLedMgmtObjects, prvtOprLedMgmtNotifications=prvtOprLedMgmtNotifications, prvtOprLedMgmtConformance=prvtOprLedMgmtConformance)
