#
# PySNMP MIB module BENU-WAG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/benuos/BENU-WAG-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:33:42 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
benuPlatSerMIB, = mibBuilder.importSymbols("BENU-PLATFORM-SERVICE-MIB", "benuPlatSerMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Counter32, Integer32, Bits, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter64, Unsigned32, NotificationType, TimeTicks, MibIdentifier, Gauge32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Counter32", "Integer32", "Bits", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter64", "Unsigned32", "NotificationType", "TimeTicks", "MibIdentifier", "Gauge32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
benuWAG = ModuleIdentity((1, 3, 6, 1, 4, 1, 39406, 2, 1))
benuWAG.setRevisions(('2012-10-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: benuWAG.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: benuWAG.setLastUpdated('201210080000Z')
if mibBuilder.loadTexts: benuWAG.setOrganization('Benu Networks')
if mibBuilder.loadTexts: benuWAG.setContactInfo('Benu Networks Inc,\n      300 Concord Road,\n      Billerca MA 01821\n      Email: support@benunets.com')
if mibBuilder.loadTexts: benuWAG.setDescription('The MIB module for defining all mib sub modules \n        that are specific to WiFiAccessGateway\n        Copyright (C) 2001, 2008 by Benu Networks, Inc.\n        All rights reserved.')
mibBuilder.exportSymbols("BENU-WAG-MIB", PYSNMP_MODULE_ID=benuWAG, benuWAG=benuWAG)
