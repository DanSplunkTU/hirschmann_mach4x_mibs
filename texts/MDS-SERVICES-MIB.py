#
# PySNMP MIB module MDS-SERVICES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-SERVICES-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:19:32 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
mdsServices, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsServices")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, IpAddress, Counter32, ObjectIdentity, Unsigned32, Integer32, Bits, NotificationType, Counter64, iso, MibIdentifier, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "Counter32", "ObjectIdentity", "Unsigned32", "Integer32", "Bits", "NotificationType", "Counter64", "iso", "MibIdentifier", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mdsServicesMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1))
mdsServicesMIB.setRevisions(('2018-05-16 00:00', '2014-10-20 00:00', '2014-05-12 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsServicesMIB.setRevisionsDescriptions(('Updated conformance statments baed on smilint.', 'Removed hyphens from enumerations.', 'Initial version.',))
if mibBuilder.loadTexts: mdsServicesMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsServicesMIB.setOrganization('GE MDS LLC\n        http://www.gemds.com')
if mibBuilder.loadTexts: mdsServicesMIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n         T 585-242-9600\n         F 585-242-9620\n\n         175 Science Parkway\n         Rochester, New York 14620\n         USA')
if mibBuilder.loadTexts: mdsServicesMIB.setDescription('The MIB module to describe the services.')
mServMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1))
mServConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 1))
mServStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2))
mServStatusTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1), )
if mibBuilder.loadTexts: mServStatusTable.setStatus('current')
if mibBuilder.loadTexts: mServStatusTable.setDescription('This table contains status of services.')
mServStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1, 1), ).setIndexNames((0, "MDS-SERVICES-MIB", "mServServiceName"))
if mibBuilder.loadTexts: mServStatusEntry.setStatus('current')
if mibBuilder.loadTexts: mServStatusEntry.setDescription('Each entry contains status of a service.')
mServServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mServServiceName.setStatus('current')
if mibBuilder.loadTexts: mServServiceName.setDescription('Service name.')
mServServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("running", 0), ("disabled", 1), ("error", 2), ("notRunning", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mServServiceStatus.setStatus('current')
if mibBuilder.loadTexts: mServServiceStatus.setDescription('Service status.')
mdsServMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3))
mdsServMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 1))
mdsServMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 2))
mServCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 1, 1)).setObjects(("MDS-SERVICES-MIB", "mServStatusGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mServCompliance = mServCompliance.setStatus('current')
if mibBuilder.loadTexts: mServCompliance.setDescription('The compliance statement for SNMP entities that \n            implement the MDS-SERVICES-MIB.')
mServStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 3, 1, 3, 2, 1)).setObjects(("MDS-SERVICES-MIB", "mServServiceName"), ("MDS-SERVICES-MIB", "mServServiceStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mServStatusGroup = mServStatusGroup.setStatus('current')
if mibBuilder.loadTexts: mServStatusGroup.setDescription('A collection of objects providing information about\n        orbit services status.')
mibBuilder.exportSymbols("MDS-SERVICES-MIB", mServServiceName=mServServiceName, mServCompliance=mServCompliance, mServStatus=mServStatus, mServMIBObjects=mServMIBObjects, mdsServMIBGroups=mdsServMIBGroups, mServStatusGroup=mServStatusGroup, mServStatusTable=mServStatusTable, PYSNMP_MODULE_ID=mdsServicesMIB, mServConfig=mServConfig, mServStatusEntry=mServStatusEntry, mdsServMIBCompliances=mdsServMIBCompliances, mServServiceStatus=mServServiceStatus, mdsServMIBConformance=mdsServMIBConformance, mdsServicesMIB=mdsServicesMIB)
