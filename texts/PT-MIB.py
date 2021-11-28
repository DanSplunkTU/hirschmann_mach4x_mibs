#
# PySNMP MIB module PT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/protelevision/PT-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:16:33 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, enterprises, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType, Unsigned32, Bits, TimeTicks, Counter32, ModuleIdentity, Gauge32, Counter64, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "enterprises", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType", "Unsigned32", "Bits", "TimeTicks", "Counter32", "ModuleIdentity", "Gauge32", "Counter64", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pt = ModuleIdentity((1, 3, 6, 1, 4, 1, 18086))
pt.setRevisions(('2014-08-08 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pt.setRevisionsDescriptions(('PTT General Device MIB File',))
if mibBuilder.loadTexts: pt.setLastUpdated('201408081200Z')
if mibBuilder.loadTexts: pt.setOrganization('Protelevision Technologies, Denmark')
if mibBuilder.loadTexts: pt.setContactInfo('Contact:\n\n                Web: http://www.protelevision.com\n\n                Address: Valhoejs Alle 176, DK-2610 Roedovre, Denmark\n                Telephone: +45 44700000\n                Fax:       +45 44700001')
if mibBuilder.loadTexts: pt.setDescription('This is the root MIB module for PT with OID of\n                {iso org dod internet private enterprises 18086}.\n\n                Copyright (c) 2004 Protelevision Technologies A/S. All rights reserved.\n                Reproduction of this document is authorized on the condition\n                that the foregoing copyright notice is included.\n\n                IANA allocated this enterprise OID (object identifier) for the\n                exclusive use of Protelevision Technologies A/S (PT). \n                Other than internet network equipment\n                distributed or licensed by PT, no other party has any right\n                what-so-ever to distribute or license internet network equipment\n                which responds to the PT enterprise OID or its subsidiary\n                branches. PT reserves the right to criminally prosecute and/or\n                to seek civil damages from anyone fraudently using the PT\n                enterprise OID to the full extent of the law.')
mibBuilder.exportSymbols("PT-MIB", pt=pt, PYSNMP_MODULE_ID=pt)
