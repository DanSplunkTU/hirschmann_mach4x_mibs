#
# PySNMP MIB module ACD-TID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/accedian/ACD-TID-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:15:17 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
acdMibs, = mibBuilder.importSymbols("ACCEDIAN-SMI", "acdMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, IpAddress, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Gauge32, ObjectIdentity, iso, Counter32, TimeTicks, Bits, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "IpAddress", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Gauge32", "ObjectIdentity", "iso", "Counter32", "TimeTicks", "Bits", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
acdTid = ModuleIdentity((1, 3, 6, 1, 4, 1, 22420, 2, 14))
acdTid.setRevisions(('2011-11-11 01:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: acdTid.setRevisionsDescriptions(('Initial version of MIB module ACD-TID-MIB.',))
if mibBuilder.loadTexts: acdTid.setLastUpdated('201111110100Z')
if mibBuilder.loadTexts: acdTid.setOrganization('Accedian Networks, Inc.')
if mibBuilder.loadTexts: acdTid.setContactInfo('Accedian Technical Assistance Center\n             Accedian Networks, Inc.\n             2351 Boul. Alfred-Nobel, Suite N-410\n             Montreal, Quebec Canada H4S 2A9\n             E-mail: support@accedian.com')
if mibBuilder.loadTexts: acdTid.setDescription('The Transaction ID database for this Accedian Networks device.')
acdTidNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 0))
acdTidMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1))
acdTidConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2))
acdTidGeneral = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1))
acdTidInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2))
class AcdTidType(TextualConvention, Integer32):
    description = 'Indicate if the object is covers by the acdTidCfgLastChangeTid or\n        or by the acdTidStatusLastChangeTid transaction identifier.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("configuration", 1), ("status", 2))

acdTidCfgLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidCfgLastChangeTid.setStatus('current')
if mibBuilder.loadTexts: acdTidCfgLastChangeTid.setDescription('This is the transaction ID of the last change of a configuration\n        object.  If this value is different since the last read this is \n        indicate a change.')
acdTidStatusLastChangeTid = MibScalar((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidStatusLastChangeTid.setStatus('current')
if mibBuilder.loadTexts: acdTidStatusLastChangeTid.setDescription('This is the transaction ID of the last change of a status object.\n        If this value is different since the last read this is indicate \n        a change.')
acdTidInfoTable = MibTable((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1), )
if mibBuilder.loadTexts: acdTidInfoTable.setStatus('current')
if mibBuilder.loadTexts: acdTidInfoTable.setDescription('Table of all object covers by Transaction Identifier feature.')
acdTidInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1), ).setIndexNames((0, "ACD-TID-MIB", "acdTidInfoIndex"))
if mibBuilder.loadTexts: acdTidInfoEntry.setStatus('current')
if mibBuilder.loadTexts: acdTidInfoEntry.setDescription('An entry contains information applicble to a specific object.')
acdTidInfoIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: acdTidInfoIndex.setStatus('current')
if mibBuilder.loadTexts: acdTidInfoIndex.setDescription('A unique value, greater than zero, for each entry.')
acdTidInfoOID = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoOID.setStatus('current')
if mibBuilder.loadTexts: acdTidInfoOID.setDescription('This object identifies the OID covers by this transaction\n             Identifier.')
acdTidInfoType = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 3), AcdTidType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoType.setStatus('current')
if mibBuilder.loadTexts: acdTidInfoType.setDescription('Indicate if the object is covers by the acdTidCfgLastChangeTid or\n        or by the acdTidStatusLastChangeTid transaction identifier.')
acdTidInfoDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoDescr.setStatus('current')
if mibBuilder.loadTexts: acdTidInfoDescr.setDescription('A textual description of the object point by acdTidInfoOID.')
acdTidInfoLastChangeTid = MibTableColumn((1, 3, 6, 1, 4, 1, 22420, 2, 14, 1, 2, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: acdTidInfoLastChangeTid.setStatus('current')
if mibBuilder.loadTexts: acdTidInfoLastChangeTid.setDescription('This is the transaction ID of the last change of a the object\n        point by acdTidInfoOID. If this value is different since the \n        last read this is indicate a change.')
acdTidCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 1))
acdTidGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2))
acdTidGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 1)).setObjects(("ACD-TID-MIB", "acdTidCfgLastChangeTid"), ("ACD-TID-MIB", "acdTidStatusLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidGeneralGroup = acdTidGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: acdTidGeneralGroup.setDescription('List of scalars to monitior changes in supported object.')
acdTidTableGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 2, 2)).setObjects(("ACD-TID-MIB", "acdTidInfoOID"), ("ACD-TID-MIB", "acdTidInfoType"), ("ACD-TID-MIB", "acdTidInfoDescr"), ("ACD-TID-MIB", "acdTidInfoLastChangeTid"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidTableGroup = acdTidTableGroup.setStatus('current')
if mibBuilder.loadTexts: acdTidTableGroup.setDescription('Group for the acdTidTable.')
acdTidCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 22420, 2, 14, 2, 1, 1)).setObjects(("ACD-TID-MIB", "acdTidGeneralGroup"), ("ACD-TID-MIB", "acdTidTableGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    acdTidCompliance = acdTidCompliance.setStatus('current')
if mibBuilder.loadTexts: acdTidCompliance.setDescription('The compliance statement for support of the ACD-TID-MIB module.')
mibBuilder.exportSymbols("ACD-TID-MIB", acdTidGeneral=acdTidGeneral, acdTidInfoTable=acdTidInfoTable, acdTidGeneralGroup=acdTidGeneralGroup, acdTid=acdTid, acdTidInfoEntry=acdTidInfoEntry, acdTidInfoDescr=acdTidInfoDescr, acdTidInfoOID=acdTidInfoOID, acdTidNotifications=acdTidNotifications, PYSNMP_MODULE_ID=acdTid, acdTidConformance=acdTidConformance, acdTidGroups=acdTidGroups, AcdTidType=AcdTidType, acdTidCfgLastChangeTid=acdTidCfgLastChangeTid, acdTidInfoIndex=acdTidInfoIndex, acdTidCompliances=acdTidCompliances, acdTidInfoLastChangeTid=acdTidInfoLastChangeTid, acdTidInfo=acdTidInfo, acdTidCompliance=acdTidCompliance, acdTidTableGroup=acdTidTableGroup, acdTidInfoType=acdTidInfoType, acdTidMIBObjects=acdTidMIBObjects, acdTidStatusLastChangeTid=acdTidStatusLastChangeTid)
