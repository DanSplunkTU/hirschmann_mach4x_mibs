#
# PySNMP MIB module AT-UDLD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/AT-UDLD-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:37 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
modules, = mibBuilder.importSymbols("AT-SMI-MIB", "modules")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, Integer32, ObjectIdentity, Unsigned32, IpAddress, NotificationType, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Bits, iso, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Integer32", "ObjectIdentity", "Unsigned32", "IpAddress", "NotificationType", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Bits", "iso", "Counter64", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atUdld = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550))
atUdld.setRevisions(('2011-11-22 00:00', '2011-05-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: atUdld.setRevisionsDescriptions(('The definition of OBJECT IDENTIFIER was modified.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: atUdld.setLastUpdated('201111220000Z')
if mibBuilder.loadTexts: atUdld.setOrganization('Allied Telesis, Inc.')
if mibBuilder.loadTexts: atUdld.setContactInfo('http://www.alliedtelesis.com')
if mibBuilder.loadTexts: atUdld.setDescription('This MIB file contains definitions of managed objects for the\n                UDLD module.')
atUdldTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0))
atUdldPortDisabledTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0, 1)).setObjects(("AT-UDLD-MIB", "atUdldIfIndex"))
if mibBuilder.loadTexts: atUdldPortDisabledTrap.setStatus('current')
if mibBuilder.loadTexts: atUdldPortDisabledTrap.setDescription('Generated when UDLD feature disabled an interface when\n                 detecting uni-directional link.')
atUdldPortRecoveredTrap = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 0, 2)).setObjects(("AT-UDLD-MIB", "atUdldIfIndex"))
if mibBuilder.loadTexts: atUdldPortRecoveredTrap.setStatus('current')
if mibBuilder.loadTexts: atUdldPortRecoveredTrap.setDescription('Generated when an interface recovers from error disable\n                 status when detecting uni-directional link.')
atUdldIfIndex = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 550, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atUdldIfIndex.setStatus('current')
if mibBuilder.loadTexts: atUdldIfIndex.setDescription('The index value of an interface of which the link status\n                 is changed.')
mibBuilder.exportSymbols("AT-UDLD-MIB", atUdldPortDisabledTrap=atUdldPortDisabledTrap, PYSNMP_MODULE_ID=atUdld, atUdld=atUdld, atUdldPortRecoveredTrap=atUdldPortRecoveredTrap, atUdldTrap=atUdldTrap, atUdldIfIndex=atUdldIfIndex)
