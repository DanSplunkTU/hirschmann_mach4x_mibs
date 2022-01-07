#
# PySNMP MIB module COLUBRIS-AAA-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-AAA-CLIENT-MIB.my
# Produced by pysmi-1.1.8 at Fri Jan  7 16:25:15 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisProfileIndex, ColubrisServerIndexOrZero, ColubrisServerIndex = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisProfileIndex", "ColubrisServerIndexOrZero", "ColubrisServerIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Counter64, Integer32, Counter32, ModuleIdentity, NotificationType, Unsigned32, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Bits, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Counter64", "Integer32", "Counter32", "ModuleIdentity", "NotificationType", "Unsigned32", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Bits", "MibIdentifier", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisAAAClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 5))
if mibBuilder.loadTexts: colubrisAAAClientMIB.setLastUpdated('200402200000Z')
if mibBuilder.loadTexts: colubrisAAAClientMIB.setOrganization('Colubris Networks, Inc.')
colubrisAAAClientObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1))
colubrisAAAProfileGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1))
colubrisAAAServerGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2))
colubrisAAAProfileTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1), )
if mibBuilder.loadTexts: colubrisAAAProfileTable.setStatus('current')
colubrisAAAProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAProfileIndex"))
if mibBuilder.loadTexts: colubrisAAAProfileEntry.setStatus('current')
colubrisAAAProfileIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1, 1, 1), ColubrisProfileIndex())
if mibBuilder.loadTexts: colubrisAAAProfileIndex.setStatus('current')
colubrisAAAProfileName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: colubrisAAAProfileName.setStatus('current')
colubrisAAAProfilePrimaryServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1, 1, 3), ColubrisServerIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisAAAProfilePrimaryServerIndex.setStatus('current')
colubrisAAAProfileSecondaryServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 1, 1, 1, 4), ColubrisServerIndexOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisAAAProfileSecondaryServerIndex.setStatus('current')
colubrisAAAServerTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1), )
if mibBuilder.loadTexts: colubrisAAAServerTable.setStatus('current')
colubrisAAAServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1), ).setIndexNames((0, "COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAServerIndex"))
if mibBuilder.loadTexts: colubrisAAAServerEntry.setStatus('current')
colubrisAAAServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 1), ColubrisServerIndex())
if mibBuilder.loadTexts: colubrisAAAServerIndex.setStatus('current')
colubrisAAAAuthenProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("radius", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisAAAAuthenProtocol.setStatus('current')
colubrisAAAAuthenMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("pap", 1), ("chap", 2), ("mschap", 3), ("mschapv2", 4), ("eapMd5", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisAAAAuthenMethod.setStatus('current')
colubrisAAAServerName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: colubrisAAAServerName.setStatus('current')
colubrisAAASharedSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: colubrisAAASharedSecret.setStatus('current')
colubrisAAAAuthenticationPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisAAAAuthenticationPort.setStatus('current')
colubrisAAAAccountingPort = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisAAAAccountingPort.setStatus('current')
colubrisAAATimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 100))).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisAAATimeout.setStatus('current')
colubrisAAANASId = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 5, 1, 2, 1, 1, 9), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: colubrisAAANASId.setStatus('current')
colubrisAAAClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 5, 2))
colubrisAAAClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 5, 2, 1))
colubrisAAAClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 5, 2, 2))
colubrisAAAClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 5, 2, 1, 1)).setObjects(("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAProfileMIBGroup"), ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAClientMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisAAAClientMIBCompliance = colubrisAAAClientMIBCompliance.setStatus('current')
colubrisAAAProfileMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 5, 2, 2, 1)).setObjects(("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAProfileName"), ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAProfilePrimaryServerIndex"), ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAProfileSecondaryServerIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisAAAProfileMIBGroup = colubrisAAAProfileMIBGroup.setStatus('current')
colubrisAAAClientMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 5, 2, 2, 2)).setObjects(("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAAuthenProtocol"), ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAAuthenMethod"), ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAServerName"), ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAASharedSecret"), ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAAuthenticationPort"), ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAAAccountingPort"), ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAATimeout"), ("COLUBRIS-AAA-CLIENT-MIB", "colubrisAAANASId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisAAAClientMIBGroup = colubrisAAAClientMIBGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-AAA-CLIENT-MIB", colubrisAAAServerEntry=colubrisAAAServerEntry, colubrisAAAAuthenticationPort=colubrisAAAAuthenticationPort, colubrisAAAProfileTable=colubrisAAAProfileTable, colubrisAAAServerIndex=colubrisAAAServerIndex, colubrisAAAClientMIBCompliances=colubrisAAAClientMIBCompliances, colubrisAAAProfileMIBGroup=colubrisAAAProfileMIBGroup, colubrisAAAProfilePrimaryServerIndex=colubrisAAAProfilePrimaryServerIndex, colubrisAAAServerTable=colubrisAAAServerTable, colubrisAAAServerName=colubrisAAAServerName, colubrisAAAAuthenProtocol=colubrisAAAAuthenProtocol, colubrisAAAClientMIB=colubrisAAAClientMIB, colubrisAAAClientMIBCompliance=colubrisAAAClientMIBCompliance, colubrisAAASharedSecret=colubrisAAASharedSecret, colubrisAAAProfileSecondaryServerIndex=colubrisAAAProfileSecondaryServerIndex, colubrisAAAProfileIndex=colubrisAAAProfileIndex, colubrisAAANASId=colubrisAAANASId, colubrisAAAClientMIBConformance=colubrisAAAClientMIBConformance, colubrisAAAAccountingPort=colubrisAAAAccountingPort, colubrisAAAClientObjects=colubrisAAAClientObjects, PYSNMP_MODULE_ID=colubrisAAAClientMIB, colubrisAAAProfileName=colubrisAAAProfileName, colubrisAAAClientMIBGroups=colubrisAAAClientMIBGroups, colubrisAAAServerGroup=colubrisAAAServerGroup, colubrisAAAAuthenMethod=colubrisAAAAuthenMethod, colubrisAAAProfileGroup=colubrisAAAProfileGroup, colubrisAAATimeout=colubrisAAATimeout, colubrisAAAClientMIBGroup=colubrisAAAClientMIBGroup, colubrisAAAProfileEntry=colubrisAAAProfileEntry)
