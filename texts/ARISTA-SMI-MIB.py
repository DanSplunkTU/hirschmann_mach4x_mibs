#
# PySNMP MIB module ARISTA-SMI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/arista/ARISTA-SMI-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:34 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, enterprises, IpAddress, Counter64, ModuleIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Unsigned32, NotificationType, Counter32, TimeTicks, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "enterprises", "IpAddress", "Counter64", "ModuleIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Unsigned32", "NotificationType", "Counter32", "TimeTicks", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
arista = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065))
arista.setRevisions(('2014-08-15 00:00', '2011-03-31 13:00', '2008-10-27 18:30',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: arista.setRevisionsDescriptions(('Updated postal and e-mail addresses', 'Updated postal address and telephone', 'Initial version.',))
if mibBuilder.loadTexts: arista.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: arista.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: arista.setContactInfo('Arista Networks, Inc.\n\n         Postal: 5453 Great America Parkway\n                 Santa Clara, CA 95054\n\n         Tel: +1 408 547-5500\n\n         E-mail: snmp@arista.com')
if mibBuilder.loadTexts: arista.setDescription('The Structure of Management Information for the\n            Arista Networks enterprise.')
aristaProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 1))
if mibBuilder.loadTexts: aristaProducts.setStatus('current')
if mibBuilder.loadTexts: aristaProducts.setDescription('aristaProducts is the root object identifier from\n         which sysObjectID values are assigned.  Values are\n         defined in ARISTA-PRODUCTS-MIB.')
aristaModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 2))
if mibBuilder.loadTexts: aristaModules.setStatus('current')
if mibBuilder.loadTexts: aristaModules.setDescription('aristaModules provides a root object identifier\n         from which MODULE-IDENTITY values may be assigned.')
aristaMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 3))
if mibBuilder.loadTexts: aristaMibs.setStatus('current')
if mibBuilder.loadTexts: aristaMibs.setDescription('aristaMibs provides a root object identifier\n         for management-related MIBs.')
aristaExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 30065, 4))
if mibBuilder.loadTexts: aristaExperiment.setStatus('current')
if mibBuilder.loadTexts: aristaExperiment.setDescription('aristaExperiment provides a root object identifier\n         for experimental MIBs.  The structure of information\n         for these MIBs can not be guaranteed between releases.')
mibBuilder.exportSymbols("ARISTA-SMI-MIB", PYSNMP_MODULE_ID=arista, aristaProducts=aristaProducts, aristaMibs=aristaMibs, aristaExperiment=aristaExperiment, aristaModules=aristaModules, arista=arista)
