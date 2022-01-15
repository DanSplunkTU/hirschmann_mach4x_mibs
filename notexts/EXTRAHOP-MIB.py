#
# PySNMP MIB module EXTRAHOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/extrahop/EXTRAHOP-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:02:19 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, Unsigned32, Integer32, Bits, IpAddress, TimeTicks, Gauge32, ObjectIdentity, enterprises, MibIdentifier, Counter64, ModuleIdentity, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "Unsigned32", "Integer32", "Bits", "IpAddress", "TimeTicks", "Gauge32", "ObjectIdentity", "enterprises", "MibIdentifier", "Counter64", "ModuleIdentity", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
extrahop = ModuleIdentity((1, 3, 6, 1, 4, 1, 32015))
extrahop.setRevisions(('2015-05-08 00:00',))
if mibBuilder.loadTexts: extrahop.setLastUpdated('201505080000Z')
if mibBuilder.loadTexts: extrahop.setOrganization('ExtraHop Networks')
extrahopInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32015, 0))
extrahopInfoVersionString = MibScalar((1, 3, 6, 1, 4, 1, 32015, 0, 0), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopInfoVersionString.setStatus('current')
extrahopInfoVersionMajor = MibScalar((1, 3, 6, 1, 4, 1, 32015, 0, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopInfoVersionMajor.setStatus('current')
extrahopInfoVersionMinor = MibScalar((1, 3, 6, 1, 4, 1, 32015, 0, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopInfoVersionMinor.setStatus('current')
extrahopInfoVersionBranchRelease = MibScalar((1, 3, 6, 1, 4, 1, 32015, 0, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopInfoVersionBranchRelease.setStatus('current')
extrahopInfoVersionRevision = MibScalar((1, 3, 6, 1, 4, 1, 32015, 0, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopInfoVersionRevision.setStatus('current')
extrahopAlert = MibIdentifier((1, 3, 6, 1, 4, 1, 32015, 1))
extrahopTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 32015, 2))
extrahopObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 32015, 4))
extrahopObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 32015, 4, 1)).setObjects(("EXTRAHOP-MIB", "extrahopAlertName"), ("EXTRAHOP-MIB", "extrahopAlertComment"), ("EXTRAHOP-MIB", "extrahopAlertObjectType"), ("EXTRAHOP-MIB", "extrahopAlertObjectName"), ("EXTRAHOP-MIB", "extrahopAlertExpr"), ("EXTRAHOP-MIB", "extrahopAlertValue"), ("EXTRAHOP-MIB", "extrahopAlertTime"), ("EXTRAHOP-MIB", "extrahopAlertObjectId"), ("EXTRAHOP-MIB", "extrahopAlertObjectStrId"), ("EXTRAHOP-MIB", "extrahopAlertObjectMACAddr"), ("EXTRAHOP-MIB", "extrahopAlertObjectIPAddr"), ("EXTRAHOP-MIB", "extrahopAlertObjectTags"), ("EXTRAHOP-MIB", "extrahopAlertObjectURL"), ("EXTRAHOP-MIB", "extrahopAlertStatName"), ("EXTRAHOP-MIB", "extrahopAlertStatFieldName"), ("EXTRAHOP-MIB", "extrahopAlertSeverity"), ("EXTRAHOP-MIB", "extrahopStatsPktsSinceBoot"), ("EXTRAHOP-MIB", "extrahopStatsBytesSinceBoot"), ("EXTRAHOP-MIB", "extrahopStorageAlertRole"), ("EXTRAHOP-MIB", "extrahopStorageAlertDevice"), ("EXTRAHOP-MIB", "extrahopStorageAlertStatus"), ("EXTRAHOP-MIB", "extrahopStorageAlertDetails"), ("EXTRAHOP-MIB", "extrahopStorageAlertSeverity"), ("EXTRAHOP-MIB", "extrahopStorageAlertMachine"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    extrahopObjectGroup = extrahopObjectGroup.setStatus('current')
extrahopNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 32015, 4, 2)).setObjects(("EXTRAHOP-MIB", "extrahopAlertTrap"), ("EXTRAHOP-MIB", "extrahopStorageAlertTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    extrahopNotificationGroup = extrahopNotificationGroup.setStatus('current')
extrahopAlertTrap = NotificationType((1, 3, 6, 1, 4, 1, 32015, 2, 1)).setObjects(("EXTRAHOP-MIB", "extrahopAlertName"), ("EXTRAHOP-MIB", "extrahopAlertComment"), ("EXTRAHOP-MIB", "extrahopAlertObjectType"), ("EXTRAHOP-MIB", "extrahopAlertObjectName"), ("EXTRAHOP-MIB", "extrahopAlertExpr"), ("EXTRAHOP-MIB", "extrahopAlertValue"), ("EXTRAHOP-MIB", "extrahopAlertTime"), ("EXTRAHOP-MIB", "extrahopAlertObjectId"), ("EXTRAHOP-MIB", "extrahopAlertObjectStrId"), ("EXTRAHOP-MIB", "extrahopAlertObjectMACAddr"), ("EXTRAHOP-MIB", "extrahopAlertObjectIPAddr"), ("EXTRAHOP-MIB", "extrahopAlertObjectTags"), ("EXTRAHOP-MIB", "extrahopAlertObjectURL"), ("EXTRAHOP-MIB", "extrahopAlertStatName"), ("EXTRAHOP-MIB", "extrahopAlertStatFieldName"), ("EXTRAHOP-MIB", "extrahopAlertSeverity"))
if mibBuilder.loadTexts: extrahopAlertTrap.setStatus('current')
extrahopAlertName = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertName.setStatus('current')
extrahopAlertComment = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertComment.setStatus('current')
extrahopAlertObjectType = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertObjectType.setStatus('current')
extrahopAlertObjectName = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertObjectName.setStatus('current')
extrahopAlertExpr = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertExpr.setStatus('current')
extrahopAlertValue = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertValue.setStatus('current')
extrahopAlertTime = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertTime.setStatus('current')
extrahopAlertObjectId = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertObjectId.setStatus('current')
extrahopAlertObjectStrId = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertObjectStrId.setStatus('current')
extrahopAlertObjectMACAddr = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertObjectMACAddr.setStatus('current')
extrahopAlertObjectIPAddr = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 11), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertObjectIPAddr.setStatus('current')
extrahopAlertObjectTags = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 12), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertObjectTags.setStatus('current')
extrahopAlertObjectURL = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertObjectURL.setStatus('current')
extrahopAlertStatName = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 14), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertStatName.setStatus('current')
extrahopAlertStatFieldName = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 15), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertStatFieldName.setStatus('current')
extrahopAlertSeverity = MibScalar((1, 3, 6, 1, 4, 1, 32015, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopAlertSeverity.setStatus('current')
extrahopStats = MibIdentifier((1, 3, 6, 1, 4, 1, 32015, 3))
extrahopStatsPktsSinceBoot = MibScalar((1, 3, 6, 1, 4, 1, 32015, 3, 1), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopStatsPktsSinceBoot.setStatus('current')
extrahopStatsBytesSinceBoot = MibScalar((1, 3, 6, 1, 4, 1, 32015, 3, 2), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopStatsBytesSinceBoot.setStatus('current')
extrahopStorageAlert = MibIdentifier((1, 3, 6, 1, 4, 1, 32015, 5))
extrahopStorageAlertTrap = NotificationType((1, 3, 6, 1, 4, 1, 32015, 2, 2)).setObjects(("EXTRAHOP-MIB", "extrahopStorageAlertRole"), ("EXTRAHOP-MIB", "extrahopStorageAlertDevice"), ("EXTRAHOP-MIB", "extrahopStorageAlertStatus"), ("EXTRAHOP-MIB", "extrahopStorageAlertDetails"), ("EXTRAHOP-MIB", "extrahopStorageAlertSeverity"), ("EXTRAHOP-MIB", "extrahopStorageAlertMachine"))
if mibBuilder.loadTexts: extrahopStorageAlertTrap.setStatus('current')
extrahopStorageAlertRole = MibScalar((1, 3, 6, 1, 4, 1, 32015, 5, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopStorageAlertRole.setStatus('current')
extrahopStorageAlertDevice = MibScalar((1, 3, 6, 1, 4, 1, 32015, 5, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopStorageAlertDevice.setStatus('current')
extrahopStorageAlertStatus = MibScalar((1, 3, 6, 1, 4, 1, 32015, 5, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopStorageAlertStatus.setStatus('current')
extrahopStorageAlertDetails = MibScalar((1, 3, 6, 1, 4, 1, 32015, 5, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopStorageAlertDetails.setStatus('current')
extrahopStorageAlertSeverity = MibScalar((1, 3, 6, 1, 4, 1, 32015, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("emergency", 0), ("alert", 1), ("critical", 2), ("error", 3), ("warning", 4), ("notice", 5), ("info", 6), ("debug", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopStorageAlertSeverity.setStatus('current')
extrahopStorageAlertMachine = MibScalar((1, 3, 6, 1, 4, 1, 32015, 5, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: extrahopStorageAlertMachine.setStatus('current')
mibBuilder.exportSymbols("EXTRAHOP-MIB", extrahopStatsPktsSinceBoot=extrahopStatsPktsSinceBoot, extrahopAlertStatFieldName=extrahopAlertStatFieldName, extrahopInfoVersionRevision=extrahopInfoVersionRevision, extrahopAlertObjectURL=extrahopAlertObjectURL, extrahopAlertSeverity=extrahopAlertSeverity, extrahopAlertObjectType=extrahopAlertObjectType, extrahopAlertName=extrahopAlertName, extrahopAlertObjectMACAddr=extrahopAlertObjectMACAddr, extrahopStorageAlertStatus=extrahopStorageAlertStatus, extrahopInfo=extrahopInfo, PYSNMP_MODULE_ID=extrahop, extrahopStats=extrahopStats, extrahopNotificationGroup=extrahopNotificationGroup, extrahopStorageAlertTrap=extrahopStorageAlertTrap, extrahopAlertObjectId=extrahopAlertObjectId, extrahopInfoVersionMajor=extrahopInfoVersionMajor, extrahopInfoVersionString=extrahopInfoVersionString, extrahopAlertObjectStrId=extrahopAlertObjectStrId, extrahopAlertStatName=extrahopAlertStatName, extrahopAlertComment=extrahopAlertComment, extrahopAlertObjectTags=extrahopAlertObjectTags, extrahopStatsBytesSinceBoot=extrahopStatsBytesSinceBoot, extrahopAlertObjectName=extrahopAlertObjectName, extrahopStorageAlertDevice=extrahopStorageAlertDevice, extrahopAlertValue=extrahopAlertValue, extrahopAlertTime=extrahopAlertTime, extrahopStorageAlert=extrahopStorageAlert, extrahopAlertObjectIPAddr=extrahopAlertObjectIPAddr, extrahopInfoVersionBranchRelease=extrahopInfoVersionBranchRelease, extrahopAlert=extrahopAlert, extrahopStorageAlertMachine=extrahopStorageAlertMachine, extrahopStorageAlertRole=extrahopStorageAlertRole, extrahop=extrahop, extrahopInfoVersionMinor=extrahopInfoVersionMinor, extrahopAlertExpr=extrahopAlertExpr, extrahopStorageAlertDetails=extrahopStorageAlertDetails, extrahopTraps=extrahopTraps, extrahopAlertTrap=extrahopAlertTrap, extrahopStorageAlertSeverity=extrahopStorageAlertSeverity, extrahopObjectGroup=extrahopObjectGroup, extrahopObjects=extrahopObjects)
