#
# PySNMP MIB module MITEL-APPCMN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mitel/MITEL-APPCMN-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:40:58 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ItuPerceivedSeverity, = mibBuilder.importSymbols("MITEL-CMNALM-MIB", "ItuPerceivedSeverity")
mitelIdentification, mitelConfCompliances, mitelConfGroups, mitelPropApplications = mibBuilder.importSymbols("MITEL-MIB", "mitelIdentification", "mitelConfCompliances", "mitelConfGroups", "mitelPropApplications")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Unsigned32, iso, IpAddress, ModuleIdentity, Counter64, ObjectIdentity, TimeTicks, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Unsigned32", "iso", "IpAddress", "ModuleIdentity", "Counter64", "ObjectIdentity", "TimeTicks", "Integer32", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mitelAppCommon = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2))
mitelAppCommon.setRevisions(('2014-02-11 12:00', '2005-02-21 21:34', '2004-01-30 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelAppCommon.setRevisionsDescriptions(('The MITEL Application-Specific Common MIB module.', 'Some additional attributes added to the Applications table.', 'MITEL Application-Specific Common MIB Version 1.0.0.1 - Draft',))
if mibBuilder.loadTexts: mitelAppCommon.setLastUpdated('201402111200Z')
if mibBuilder.loadTexts: mitelAppCommon.setOrganization('MITEL Networks Corporation')
if mibBuilder.loadTexts: mitelAppCommon.setContactInfo('Standards Group,\n                           Postal:    MITEL Networks Corporation\n                           350 Legget Drive, PO Box 13089\n                           Kanata, Ontario\n                           Canada  K2K 2W7\n                           Tel: +1 613 592 2122\n                           Fax: +1 613 592 4784\n                           URL: www.mitel.com')
if mibBuilder.loadTexts: mitelAppCommon.setDescription('Replaced E-Mail: std@mitel.com with URL: www.mitel.com.')
mitelAppCmnObjects = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1))
if mibBuilder.loadTexts: mitelAppCmnObjects.setStatus('current')
if mibBuilder.loadTexts: mitelAppCmnObjects.setDescription('Manageable Application Common Objects.')
mitelAppTable = MibTable((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1), )
if mibBuilder.loadTexts: mitelAppTable.setStatus('current')
if mibBuilder.loadTexts: mitelAppTable.setDescription('A list of the MITEL-defined manageable applications \n                          supported by this agent. This table is typically \n                          maintained in non-volatile memory, and is re-built \n                          upon agent restart.')
mitelAppTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1), ).setIndexNames((0, "MITEL-APPCMN-MIB", "mitelAppTblProductOid"))
if mibBuilder.loadTexts: mitelAppTableEntry.setStatus('current')
if mibBuilder.loadTexts: mitelAppTableEntry.setDescription('An entry containing application information.')
mitelAppTblProductOid = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAppTblProductOid.setStatus('current')
if mibBuilder.loadTexts: mitelAppTblProductOid.setDescription('The OID value of the application.')
mitelAppTblProductManufacturer = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAppTblProductManufacturer.setStatus('current')
if mibBuilder.loadTexts: mitelAppTblProductManufacturer.setDescription('Product Manufacturer of this application.')
mitelAppTblProductName = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAppTblProductName.setStatus('current')
if mibBuilder.loadTexts: mitelAppTblProductName.setDescription('Product Name of this application.')
mitelAppTblProductVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAppTblProductVersion.setStatus('current')
if mibBuilder.loadTexts: mitelAppTblProductVersion.setDescription('Product Version of this application. The format is \n                          described in document xxx.')
mitelAppTblProductDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAppTblProductDescr.setStatus('current')
if mibBuilder.loadTexts: mitelAppTblProductDescr.setDescription("Product description of this application that may not be \n                          contained in of the MIB-variables. If the description is \n                          not available then this should return an empty string '' as\n                          its value.")
mitelAppTblAppAlrmStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 1, 1, 6), ItuPerceivedSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAppTblAppAlrmStatus.setStatus('current')
if mibBuilder.loadTexts: mitelAppTblAppAlrmStatus.setDescription("Indicates the application's alarm level severity.")
mitelAppNumberOfApps = MibScalar((1, 3, 6, 1, 4, 1, 1027, 4, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mitelAppNumberOfApps.setStatus('current')
if mibBuilder.loadTexts: mitelAppNumberOfApps.setDescription('Indicates the number of applications installed\n                      on this platform registered with the Applications \n                      Table.')
mitelGrpAppCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 2, 3))
if mibBuilder.loadTexts: mitelGrpAppCommon.setStatus('current')
if mibBuilder.loadTexts: mitelGrpAppCommon.setDescription('The groups associated with the Applications Common MIB.')
mitelComplAppCommon = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 5, 1, 5))
if mibBuilder.loadTexts: mitelComplAppCommon.setStatus('current')
if mibBuilder.loadTexts: mitelComplAppCommon.setDescription('The groups associated with the Applications Common MIB.')
mitelComplAppCmn = ModuleCompliance((1, 3, 6, 1, 4, 1, 1027, 5, 1, 5, 1)).setObjects(("MITEL-APPCMN-MIB", "mitelGrpAppCmn"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelComplAppCmn = mitelComplAppCmn.setStatus('current')
if mibBuilder.loadTexts: mitelComplAppCmn.setDescription('The compliance statement for SNMPv2 entities which\n                           implement the MITEL Applications Common MIB.')
mitelGrpAppCmn = ObjectGroup((1, 3, 6, 1, 4, 1, 1027, 5, 2, 3, 1)).setObjects(("MITEL-APPCMN-MIB", "mitelAppTblProductOid"), ("MITEL-APPCMN-MIB", "mitelAppTblProductManufacturer"), ("MITEL-APPCMN-MIB", "mitelAppTblProductName"), ("MITEL-APPCMN-MIB", "mitelAppTblProductVersion"), ("MITEL-APPCMN-MIB", "mitelAppTblProductDescr"), ("MITEL-APPCMN-MIB", "mitelAppTblAppAlrmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mitelGrpAppCmn = mitelGrpAppCmn.setStatus('current')
if mibBuilder.loadTexts: mitelGrpAppCmn.setDescription('The collection of objects providing information on\n                          the applications on the current agent platform.')
mibBuilder.exportSymbols("MITEL-APPCMN-MIB", mitelComplAppCmn=mitelComplAppCmn, mitelAppCmnObjects=mitelAppCmnObjects, mitelAppTable=mitelAppTable, mitelAppTblProductName=mitelAppTblProductName, mitelAppTblAppAlrmStatus=mitelAppTblAppAlrmStatus, mitelGrpAppCommon=mitelGrpAppCommon, mitelAppTblProductManufacturer=mitelAppTblProductManufacturer, mitelAppTableEntry=mitelAppTableEntry, mitelAppTblProductVersion=mitelAppTblProductVersion, mitelAppTblProductDescr=mitelAppTblProductDescr, mitelAppCommon=mitelAppCommon, PYSNMP_MODULE_ID=mitelAppCommon, mitelAppNumberOfApps=mitelAppNumberOfApps, mitelAppTblProductOid=mitelAppTblProductOid, mitelComplAppCommon=mitelComplAppCommon, mitelGrpAppCmn=mitelGrpAppCmn)
