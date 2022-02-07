#
# PySNMP MIB module ADTRAN-AOSSNMP (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOSSNMP
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:55 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Integer32, Bits, ModuleIdentity, IpAddress, MibIdentifier, iso, Unsigned32, Gauge32, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "ModuleIdentity", "IpAddress", "MibIdentifier", "iso", "Unsigned32", "Gauge32", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "NotificationType")
TAddress, TDomain, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TAddress", "TDomain", "TextualConvention", "DisplayString", "RowStatus")
adGenAOSSnmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 2))
adGenAOSSnmpMib.setRevisions(('2008-10-20 00:00', '2008-10-09 00:00', '2004-09-24 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adGenAOSSnmpMib.setRevisionsDescriptions(('Fixing compile errors with adAOSSNMPConfigGroup.', "Revised text for adAOSSNMPCommunitiesString. This Object\n                    will no longer return the configured community string when\n                    this object is read. It will return the string\n                    'NOT ACCESSIBLE' instead. This was done for security\n                    reasons.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: adGenAOSSnmpMib.setLastUpdated('200409240000Z')
if mibBuilder.loadTexts: adGenAOSSnmpMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adGenAOSSnmpMib.setContactInfo('Technical Support Dept.\n                Postal: ADTRAN, Inc.\n                901 Explorer Blvd.\n                Huntsville, AL 35806\n\n                Tel: +1 800 726-8663\n                Fax: +1 256 963 6217\n                E-mail: support@adtran.com')
if mibBuilder.loadTexts: adGenAOSSnmpMib.setDescription('This MIB defines how the method for configuring an ADTRAN OS\n\t\t\t device for SNMP community names and configuration for TRAP\n\t\t\t manager destinations.')
adGenAOSSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2))
adAOSSNMPCommunitiesTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1), )
if mibBuilder.loadTexts: adAOSSNMPCommunitiesTable.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPCommunitiesTable.setDescription('Contains a list of users who have SNMP access to this\n        unit.')
adAOSSNMPCommunitiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1), ).setIndexNames((0, "ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesIndex"))
if mibBuilder.loadTexts: adAOSSNMPCommunitiesEntry.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPCommunitiesEntry.setDescription('Each entry in the list defines the community string,\n        access privilege, and Manager IP address.')
adAOSSNMPCommunitiesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32)))
if mibBuilder.loadTexts: adAOSSNMPCommunitiesIndex.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPCommunitiesIndex.setDescription('Index of the table.')
adAOSSNMPCommunitiesString = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPCommunitiesString.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPCommunitiesString.setDescription("The community string which has the specified SNMP\n        access. Due to the secruity risk of displaying the community string,\n        reading this object will always display the string 'NOT ACCESSIBLE'.")
adAOSSNMPCommunitiesPrivilege = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("get", 1), ("set", 2))).clone('get')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPCommunitiesPrivilege.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPCommunitiesPrivilege.setDescription('Set the SNMP privileges of this user.')
adAOSSNMPCommunitiesStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPCommunitiesStatus.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPCommunitiesStatus.setDescription("The status of this conceptual row.\n\n        Until instances of all corresponding columns are\n        appropriately configured, the value of the corresponding\n        instance of the adAOSSNMPCommunitiesStatus column is\n        'notReady'.")
adAOSSNMPTrapsTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2), )
if mibBuilder.loadTexts: adAOSSNMPTrapsTable.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPTrapsTable.setDescription('Contains a list of users that will receive SNMP traps\n        from this unit.')
adAOSSNMPTrapsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1), ).setIndexNames((0, "ADTRAN-AOSSNMP", "adAOSSNMPTrapsIndex"))
if mibBuilder.loadTexts: adAOSSNMPTrapsEntry.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPTrapsEntry.setDescription('Each entry in the list defines the name, privilege, and\n        Manager IP address.')
adAOSSNMPTrapsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: adAOSSNMPTrapsIndex.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPTrapsIndex.setDescription('Index of the table. ')
adAOSSNMPTrapsString = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPTrapsString.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPTrapsString.setDescription('The community string included in the SNMP traps.')
adAOSSNMPTrapsMngmtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPTrapsMngmtAddr.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPTrapsMngmtAddr.setDescription('The hostname (or IP address) that will receive SNMP\n        traps.')
adAOSSNMPTrapsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPTrapsStatus.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPTrapsStatus.setDescription("The status of this conceptual row.\n\n        Until instances of all corresponding columns are\n        appropriately configured, the value of the corresponding\n        instance of the adAOSSNMPTrapsStatus column is\n        'notReady'.")
adAOSSNMPEnableTraps = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSSNMPEnableTraps.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPEnableTraps.setDescription('Enables or disables the transmission of all Traps.')
adAOSSNMPAuthenticationTraps = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSSNMPAuthenticationTraps.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPAuthenticationTraps.setDescription('Enables or disables the transmission of Authentication\n        Traps.')
adGenAOSSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2))
adAOSSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 1))
adAOSSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 2))
adAOSSnmpConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 1, 1)).setObjects(("ADTRAN-AOSSNMP", "adAOSSNMPConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSSnmpConfigCompliance = adAOSSnmpConfigCompliance.setStatus('current')
if mibBuilder.loadTexts: adAOSSnmpConfigCompliance.setDescription('SNMP Community Names.')
adAOSSNMPConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 2, 1)).setObjects(("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesString"), ("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesPrivilege"), ("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesStatus"), ("ADTRAN-AOSSNMP", "adAOSSNMPEnableTraps"), ("ADTRAN-AOSSNMP", "adAOSSNMPAuthenticationTraps"), ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsString"), ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsMngmtAddr"), ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSSNMPConfigGroup = adAOSSNMPConfigGroup.setStatus('current')
if mibBuilder.loadTexts: adAOSSNMPConfigGroup.setDescription('The Unit SNMP Config Group.')
mibBuilder.exportSymbols("ADTRAN-AOSSNMP", adAOSSNMPEnableTraps=adAOSSNMPEnableTraps, adAOSSNMPTrapsTable=adAOSSNMPTrapsTable, adAOSSnmpConfigCompliance=adAOSSnmpConfigCompliance, adAOSSNMPCommunitiesPrivilege=adAOSSNMPCommunitiesPrivilege, adAOSSNMPCommunitiesTable=adAOSSNMPCommunitiesTable, adGenAOSSnmpMib=adGenAOSSnmpMib, adAOSSNMPCommunitiesEntry=adAOSSNMPCommunitiesEntry, adAOSSNMPTrapsString=adAOSSNMPTrapsString, adAOSSNMPTrapsEntry=adAOSSNMPTrapsEntry, adAOSSNMPTrapsMngmtAddr=adAOSSNMPTrapsMngmtAddr, adAOSSNMPConfigGroup=adAOSSNMPConfigGroup, adAOSSNMPTrapsIndex=adAOSSNMPTrapsIndex, adGenAOSSnmpConformance=adGenAOSSnmpConformance, adAOSSNMPTrapsStatus=adAOSSNMPTrapsStatus, adAOSSnmpCompliances=adAOSSnmpCompliances, adAOSSNMPCommunitiesString=adAOSSNMPCommunitiesString, adAOSSNMPAuthenticationTraps=adAOSSNMPAuthenticationTraps, adAOSSnmpGroups=adAOSSnmpGroups, PYSNMP_MODULE_ID=adGenAOSSnmpMib, adGenAOSSnmp=adGenAOSSnmp, adAOSSNMPCommunitiesIndex=adAOSSNMPCommunitiesIndex, adAOSSNMPCommunitiesStatus=adAOSSNMPCommunitiesStatus)
