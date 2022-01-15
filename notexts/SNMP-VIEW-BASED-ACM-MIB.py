#
# PySNMP MIB module SNMP-VIEW-BASED-ACM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SNMP-VIEW-BASED-ACM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:36 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
SnmpAdminString, SnmpSecurityModel, SnmpSecurityLevel = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString", "SnmpSecurityModel", "SnmpSecurityLevel")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Integer32, snmpModules, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "snmpModules", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
StorageType, DisplayString, TestAndIncr, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "DisplayString", "TestAndIncr", "RowStatus", "TextualConvention")
snmpVacmMIB = ModuleIdentity((1, 3, 6, 1, 6, 3, 16))
snmpVacmMIB.setRevisions(('2002-10-16 00:00', '1999-01-20 00:00', '1997-11-20 00:00',))
if mibBuilder.loadTexts: snmpVacmMIB.setLastUpdated('200210160000Z')
if mibBuilder.loadTexts: snmpVacmMIB.setOrganization('SNMPv3 Working Group')
vacmMIBObjects = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 1))
vacmMIBConformance = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 2))
vacmContextTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 1), )
if mibBuilder.loadTexts: vacmContextTable.setStatus('current')
vacmContextEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 1, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"))
if mibBuilder.loadTexts: vacmContextEntry.setStatus('current')
vacmContextName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 1, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vacmContextName.setStatus('current')
vacmSecurityToGroupTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 2), )
if mibBuilder.loadTexts: vacmSecurityToGroupTable.setStatus('current')
vacmSecurityToGroupEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 2, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityName"))
if mibBuilder.loadTexts: vacmSecurityToGroupEntry.setStatus('current')
vacmSecurityModel = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 1), SnmpSecurityModel().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: vacmSecurityModel.setStatus('current')
vacmSecurityName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: vacmSecurityName.setStatus('current')
vacmGroupName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmGroupName.setStatus('current')
vacmSecurityToGroupStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 4), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmSecurityToGroupStorageType.setStatus('current')
vacmSecurityToGroupStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmSecurityToGroupStatus.setStatus('current')
vacmAccessTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 4), )
if mibBuilder.loadTexts: vacmAccessTable.setStatus('current')
vacmAccessEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 4, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmGroupName"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextPrefix"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityModel"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmAccessSecurityLevel"))
if mibBuilder.loadTexts: vacmAccessEntry.setStatus('current')
vacmAccessContextPrefix = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)))
if mibBuilder.loadTexts: vacmAccessContextPrefix.setStatus('current')
vacmAccessSecurityModel = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 2), SnmpSecurityModel())
if mibBuilder.loadTexts: vacmAccessSecurityModel.setStatus('current')
vacmAccessSecurityLevel = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 3), SnmpSecurityLevel())
if mibBuilder.loadTexts: vacmAccessSecurityLevel.setStatus('current')
vacmAccessContextMatch = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("exact", 1), ("prefix", 2))).clone('exact')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessContextMatch.setStatus('current')
vacmAccessReadViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 5), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessReadViewName.setStatus('current')
vacmAccessWriteViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessWriteViewName.setStatus('current')
vacmAccessNotifyViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 7), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessNotifyViewName.setStatus('current')
vacmAccessStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 8), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessStorageType.setStatus('current')
vacmAccessStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 4, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmAccessStatus.setStatus('current')
vacmMIBViews = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 1, 5))
vacmViewSpinLock = MibScalar((1, 3, 6, 1, 6, 3, 16, 1, 5, 1), TestAndIncr()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: vacmViewSpinLock.setStatus('current')
vacmViewTreeFamilyTable = MibTable((1, 3, 6, 1, 6, 3, 16, 1, 5, 2), )
if mibBuilder.loadTexts: vacmViewTreeFamilyTable.setStatus('current')
vacmViewTreeFamilyEntry = MibTableRow((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1), ).setIndexNames((0, "SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyViewName"), (0, "SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilySubtree"))
if mibBuilder.loadTexts: vacmViewTreeFamilyEntry.setStatus('current')
vacmViewTreeFamilyViewName = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32)))
if mibBuilder.loadTexts: vacmViewTreeFamilyViewName.setStatus('current')
vacmViewTreeFamilySubtree = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 2), ObjectIdentifier())
if mibBuilder.loadTexts: vacmViewTreeFamilySubtree.setStatus('current')
vacmViewTreeFamilyMask = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 16)).clone(hexValue="")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyMask.setStatus('current')
vacmViewTreeFamilyType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("included", 1), ("excluded", 2))).clone('included')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyType.setStatus('current')
vacmViewTreeFamilyStorageType = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyStorageType.setStatus('current')
vacmViewTreeFamilyStatus = MibTableColumn((1, 3, 6, 1, 6, 3, 16, 1, 5, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: vacmViewTreeFamilyStatus.setStatus('current')
vacmMIBCompliances = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 2, 1))
vacmMIBGroups = MibIdentifier((1, 3, 6, 1, 6, 3, 16, 2, 2))
vacmMIBCompliance = ModuleCompliance((1, 3, 6, 1, 6, 3, 16, 2, 1, 1)).setObjects(("SNMP-VIEW-BASED-ACM-MIB", "vacmBasicGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vacmMIBCompliance = vacmMIBCompliance.setStatus('current')
vacmBasicGroup = ObjectGroup((1, 3, 6, 1, 6, 3, 16, 2, 2, 1)).setObjects(("SNMP-VIEW-BASED-ACM-MIB", "vacmContextName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmGroupName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityToGroupStorageType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmSecurityToGroupStatus"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessContextMatch"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessReadViewName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessWriteViewName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessNotifyViewName"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessStorageType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmAccessStatus"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewSpinLock"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyMask"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyStorageType"), ("SNMP-VIEW-BASED-ACM-MIB", "vacmViewTreeFamilyStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vacmBasicGroup = vacmBasicGroup.setStatus('current')
mibBuilder.exportSymbols("SNMP-VIEW-BASED-ACM-MIB", vacmAccessContextPrefix=vacmAccessContextPrefix, vacmAccessWriteViewName=vacmAccessWriteViewName, vacmSecurityModel=vacmSecurityModel, vacmSecurityToGroupStorageType=vacmSecurityToGroupStorageType, vacmAccessReadViewName=vacmAccessReadViewName, vacmViewTreeFamilyStatus=vacmViewTreeFamilyStatus, vacmViewTreeFamilyEntry=vacmViewTreeFamilyEntry, vacmAccessStorageType=vacmAccessStorageType, vacmSecurityToGroupEntry=vacmSecurityToGroupEntry, vacmContextTable=vacmContextTable, snmpVacmMIB=snmpVacmMIB, vacmMIBGroups=vacmMIBGroups, vacmViewTreeFamilyType=vacmViewTreeFamilyType, vacmSecurityToGroupStatus=vacmSecurityToGroupStatus, vacmMIBViews=vacmMIBViews, vacmAccessContextMatch=vacmAccessContextMatch, vacmMIBObjects=vacmMIBObjects, vacmViewTreeFamilySubtree=vacmViewTreeFamilySubtree, vacmAccessEntry=vacmAccessEntry, vacmBasicGroup=vacmBasicGroup, vacmSecurityToGroupTable=vacmSecurityToGroupTable, vacmMIBCompliance=vacmMIBCompliance, vacmSecurityName=vacmSecurityName, vacmViewTreeFamilyTable=vacmViewTreeFamilyTable, vacmViewTreeFamilyStorageType=vacmViewTreeFamilyStorageType, PYSNMP_MODULE_ID=snmpVacmMIB, vacmViewTreeFamilyMask=vacmViewTreeFamilyMask, vacmMIBConformance=vacmMIBConformance, vacmAccessStatus=vacmAccessStatus, vacmGroupName=vacmGroupName, vacmContextName=vacmContextName, vacmViewSpinLock=vacmViewSpinLock, vacmAccessSecurityLevel=vacmAccessSecurityLevel, vacmAccessNotifyViewName=vacmAccessNotifyViewName, vacmViewTreeFamilyViewName=vacmViewTreeFamilyViewName, vacmMIBCompliances=vacmMIBCompliances, vacmContextEntry=vacmContextEntry, vacmAccessSecurityModel=vacmAccessSecurityModel, vacmAccessTable=vacmAccessTable)
