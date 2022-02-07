#
# PySNMP MIB module RBN-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/ericsson/RBN-SMI
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:07 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, ModuleIdentity, TimeTicks, ObjectIdentity, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, NotificationType, Counter32, Unsigned32, MibIdentifier, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "ModuleIdentity", "TimeTicks", "ObjectIdentity", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "NotificationType", "Counter32", "Unsigned32", "MibIdentifier", "Gauge32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rbnSMI = ModuleIdentity((1, 3, 6, 1, 4, 1, 2352))
rbnSMI.setRevisions(('2011-01-19 18:00', '2002-06-06 00:00', '2001-06-27 00:00', '1998-04-18 23:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbnSMI.setRevisionsDescriptions(('Update CONTACT-INFO & ORGANIZATION. ', 'Updated Contact-info and recovered revision info.', 'Added rbnInternal.', 'Initial version.',))
if mibBuilder.loadTexts: rbnSMI.setLastUpdated('201101191800Z')
if mibBuilder.loadTexts: rbnSMI.setOrganization('Ericsson AB.')
if mibBuilder.loadTexts: rbnSMI.setContactInfo('       Ericsson AB.\n\n                Postal: 100 Headquarters Dr\n                        San Jose, CA  95134\n                        USA\n\n                 Phone: +1 408 750 5000\n                   Fax: +1 408 750 5599\n                ')
if mibBuilder.loadTexts: rbnSMI.setDescription('The Structure of Management Information for\n\t\tthe enterprise.')
rbnProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 1))
if mibBuilder.loadTexts: rbnProducts.setStatus('current')
if mibBuilder.loadTexts: rbnProducts.setDescription('')
rbnMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 2))
if mibBuilder.loadTexts: rbnMgmt.setStatus('current')
if mibBuilder.loadTexts: rbnMgmt.setDescription('')
rbnExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 3))
if mibBuilder.loadTexts: rbnExperiment.setStatus('current')
if mibBuilder.loadTexts: rbnExperiment.setDescription('')
rbnCapabilities = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 4))
if mibBuilder.loadTexts: rbnCapabilities.setStatus('current')
if mibBuilder.loadTexts: rbnCapabilities.setDescription('')
rbnModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 5))
if mibBuilder.loadTexts: rbnModules.setStatus('current')
if mibBuilder.loadTexts: rbnModules.setDescription('')
rbnEntities = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 6))
if mibBuilder.loadTexts: rbnEntities.setStatus('current')
if mibBuilder.loadTexts: rbnEntities.setDescription('')
rbnInternal = ObjectIdentity((1, 3, 6, 1, 4, 1, 2352, 7))
if mibBuilder.loadTexts: rbnInternal.setStatus('current')
if mibBuilder.loadTexts: rbnInternal.setDescription('')
mibBuilder.exportSymbols("RBN-SMI", rbnEntities=rbnEntities, rbnModules=rbnModules, rbnInternal=rbnInternal, rbnProducts=rbnProducts, rbnExperiment=rbnExperiment, rbnMgmt=rbnMgmt, rbnCapabilities=rbnCapabilities, PYSNMP_MODULE_ID=rbnSMI, rbnSMI=rbnSMI)
