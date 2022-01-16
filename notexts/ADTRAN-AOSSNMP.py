#
# PySNMP MIB module ADTRAN-AOSSNMP (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOSSNMP
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:13 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Gauge32, ObjectIdentity, Counter64, MibIdentifier, IpAddress, iso, Counter32, ModuleIdentity, Unsigned32, Bits, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter64", "MibIdentifier", "IpAddress", "iso", "Counter32", "ModuleIdentity", "Unsigned32", "Bits", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
TDomain, RowStatus, DisplayString, TAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TDomain", "RowStatus", "DisplayString", "TAddress", "TextualConvention")
adGenAOSSnmpMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 2))
adGenAOSSnmpMib.setRevisions(('2008-10-20 00:00', '2008-10-09 00:00', '2004-09-24 00:00',))
if mibBuilder.loadTexts: adGenAOSSnmpMib.setLastUpdated('200409240000Z')
if mibBuilder.loadTexts: adGenAOSSnmpMib.setOrganization('ADTRAN, Inc.')
adGenAOSSnmp = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2))
adAOSSNMPCommunitiesTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1), )
if mibBuilder.loadTexts: adAOSSNMPCommunitiesTable.setStatus('current')
adAOSSNMPCommunitiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1), ).setIndexNames((0, "ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesIndex"))
if mibBuilder.loadTexts: adAOSSNMPCommunitiesEntry.setStatus('current')
adAOSSNMPCommunitiesIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 32)))
if mibBuilder.loadTexts: adAOSSNMPCommunitiesIndex.setStatus('current')
adAOSSNMPCommunitiesString = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 16))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPCommunitiesString.setStatus('current')
adAOSSNMPCommunitiesPrivilege = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("get", 1), ("set", 2))).clone('get')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPCommunitiesPrivilege.setStatus('current')
adAOSSNMPCommunitiesStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPCommunitiesStatus.setStatus('current')
adAOSSNMPTrapsTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2), )
if mibBuilder.loadTexts: adAOSSNMPTrapsTable.setStatus('current')
adAOSSNMPTrapsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1), ).setIndexNames((0, "ADTRAN-AOSSNMP", "adAOSSNMPTrapsIndex"))
if mibBuilder.loadTexts: adAOSSNMPTrapsEntry.setStatus('current')
adAOSSNMPTrapsIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 1), Integer32())
if mibBuilder.loadTexts: adAOSSNMPTrapsIndex.setStatus('current')
adAOSSNMPTrapsString = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPTrapsString.setStatus('current')
adAOSSNMPTrapsMngmtAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPTrapsMngmtAddr.setStatus('current')
adAOSSNMPTrapsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 2, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSSNMPTrapsStatus.setStatus('current')
adAOSSNMPEnableTraps = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSSNMPEnableTraps.setStatus('current')
adAOSSNMPAuthenticationTraps = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 2, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('enabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adAOSSNMPAuthenticationTraps.setStatus('current')
adGenAOSSnmpConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2))
adAOSSnmpCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 1))
adAOSSnmpGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 2))
adAOSSnmpConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 1, 1)).setObjects(("ADTRAN-AOSSNMP", "adAOSSNMPConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSSnmpConfigCompliance = adAOSSnmpConfigCompliance.setStatus('current')
adAOSSNMPConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 2, 2, 1)).setObjects(("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesString"), ("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesPrivilege"), ("ADTRAN-AOSSNMP", "adAOSSNMPCommunitiesStatus"), ("ADTRAN-AOSSNMP", "adAOSSNMPEnableTraps"), ("ADTRAN-AOSSNMP", "adAOSSNMPAuthenticationTraps"), ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsString"), ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsMngmtAddr"), ("ADTRAN-AOSSNMP", "adAOSSNMPTrapsStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSSNMPConfigGroup = adAOSSNMPConfigGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOSSNMP", adAOSSNMPAuthenticationTraps=adAOSSNMPAuthenticationTraps, adGenAOSSnmpMib=adGenAOSSnmpMib, adAOSSNMPTrapsTable=adAOSSNMPTrapsTable, adAOSSNMPCommunitiesTable=adAOSSNMPCommunitiesTable, adGenAOSSnmp=adGenAOSSnmp, adGenAOSSnmpConformance=adGenAOSSnmpConformance, adAOSSnmpGroups=adAOSSnmpGroups, adAOSSNMPCommunitiesString=adAOSSNMPCommunitiesString, adAOSSNMPTrapsString=adAOSSNMPTrapsString, adAOSSNMPCommunitiesStatus=adAOSSNMPCommunitiesStatus, adAOSSnmpConfigCompliance=adAOSSnmpConfigCompliance, PYSNMP_MODULE_ID=adGenAOSSnmpMib, adAOSSNMPCommunitiesIndex=adAOSSNMPCommunitiesIndex, adAOSSNMPCommunitiesPrivilege=adAOSSNMPCommunitiesPrivilege, adAOSSNMPTrapsStatus=adAOSSNMPTrapsStatus, adAOSSNMPTrapsMngmtAddr=adAOSSNMPTrapsMngmtAddr, adAOSSNMPTrapsIndex=adAOSSNMPTrapsIndex, adAOSSNMPEnableTraps=adAOSSNMPEnableTraps, adAOSSNMPCommunitiesEntry=adAOSSNMPCommunitiesEntry, adAOSSNMPConfigGroup=adAOSSNMPConfigGroup, adAOSSnmpCompliances=adAOSSnmpCompliances, adAOSSNMPTrapsEntry=adAOSSNMPTrapsEntry)
