#
# PySNMP MIB module Juniper-UNI-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/Juniper-UNI-SMI
# Produced by pysmi-1.1.3 at Sun Nov 28 20:27:41 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, enterprises, ModuleIdentity, Gauge32, IpAddress, Integer32, iso, Unsigned32, MibIdentifier, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "enterprises", "ModuleIdentity", "Gauge32", "IpAddress", "Integer32", "iso", "Unsigned32", "MibIdentifier", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
juniperUni = ModuleIdentity((1, 3, 6, 1, 4, 1, 4874))
juniperUni.setRevisions(('2003-07-30 19:03', '2002-11-13 20:14', '2001-06-01 21:46', '2000-06-01 14:30', '2000-05-24 04:00', '1999-12-13 19:36', '1999-11-08 00:00',))
if mibBuilder.loadTexts: juniperUni.setLastUpdated('200307301903Z')
if mibBuilder.loadTexts: juniperUni.setOrganization('Juniper Networks, Inc.')
juniProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 1))
juniperUniMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 2))
if mibBuilder.loadTexts: juniperUniMibs.setStatus('current')
usVoiceMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 1))
juniMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 2, 2))
juniperUniExperiment = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 3))
if mibBuilder.loadTexts: juniperUniExperiment.setStatus('current')
usVoiceExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 1))
juniExperiment = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 3, 2))
juniperUniAdmin = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 4))
if mibBuilder.loadTexts: juniperUniAdmin.setStatus('current')
usVoiceAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 1))
juniAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 4, 2))
juniAgentCapability = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 5))
if mibBuilder.loadTexts: juniAgentCapability.setStatus('current')
usVoiceAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 1))
juniAgents = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 5, 2))
juniNetMgmtProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4874, 6))
if mibBuilder.loadTexts: juniNetMgmtProducts.setStatus('current')
juniSdxMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 4874, 6, 1))
mibBuilder.exportSymbols("Juniper-UNI-SMI", usVoiceExperiment=usVoiceExperiment, juniMibs=juniMibs, juniProducts=juniProducts, juniperUniAdmin=juniperUniAdmin, usVoiceAdmin=usVoiceAdmin, juniAgents=juniAgents, juniSdxMibs=juniSdxMibs, juniExperiment=juniExperiment, PYSNMP_MODULE_ID=juniperUni, juniperUniExperiment=juniperUniExperiment, juniperUniMibs=juniperUniMibs, juniAdmin=juniAdmin, usVoiceAgents=usVoiceAgents, juniNetMgmtProducts=juniNetMgmtProducts, juniperUni=juniperUni, usVoiceMibs=usVoiceMibs, juniAgentCapability=juniAgentCapability)
