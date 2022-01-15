#
# PySNMP MIB module AVIAT-SWMANAGEMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/aviat-wtm/AVIAT-SWMANAGEMENT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:52:29 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, ModuleIdentity, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, IpAddress, Bits, Integer32, iso, Counter64, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "ModuleIdentity", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "IpAddress", "Bits", "Integer32", "iso", "Counter64", "Gauge32", "MibIdentifier")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
aviatModules, = mibBuilder.importSymbols("STXN-GLOBALREGISTER-MIB", "aviatModules")
aviatSwManagementModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 2509, 9, 11))
aviatSwManagementModule.setRevisions(('2014-01-21 01:57',))
if mibBuilder.loadTexts: aviatSwManagementModule.setLastUpdated('201401210157Z')
if mibBuilder.loadTexts: aviatSwManagementModule.setOrganization('Aviat Networks')
aviatSwManagementConf = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 11, 1))
aviatSwManagementGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 1))
aviatSwManagementCompliance = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 2))
aviatSwManagementMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2))
aviatSwResetObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 1))
aviatSwLoadObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2))
aviatSwDetailsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 3))
aviatSmSoftReset = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("resetNone", 0), ("resetSoft", 1), ("resetHard", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatSmSoftReset.setStatus('current')
aviatSmLoadControl = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("abort", 0), ("load", 1), ("activate", 2), ("loadAndActivate", 3), ("rollback", 4), ("forceLoad", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatSmLoadControl.setStatus('current')
aviatSmLoadStatus = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("abort", 0), ("load", 1), ("commit", 2), ("activate", 3), ("rollback", 4), ("idle", 5), ("loadOk", 6), ("activateOk", 7), ("rollbackOk", 8), ("compatibilityError", 9), ("loadError", 10), ("activateError", 11), ("rollbackError", 12), ("waitingToActivate", 13), ("sameVersion", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatSmLoadStatus.setStatus('current')
aviatSmLoadRollbackDuration = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatSmLoadRollbackDuration.setStatus('current')
aviatSmLoadRollbackTimer = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatSmLoadRollbackTimer.setStatus('current')
aviatSmLoadActivateWaitDuration = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatSmLoadActivateWaitDuration.setStatus('current')
aviatSmLoadActivateWaitTimer = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 6), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-1, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatSmLoadActivateWaitTimer.setStatus('current')
aviatSmLoadActivateTime = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 7), DateAndTime()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatSmLoadActivateTime.setStatus('current')
aviatSmLoadUri = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: aviatSmLoadUri.setStatus('current')
aviatSmLoadProgress = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 2, 9), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatSmLoadProgress.setStatus('current')
aviatSmDetailsVersion = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 3, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatSmDetailsVersion.setStatus('current')
aviatSmDetailsInactiveVersion = MibScalar((1, 3, 6, 1, 4, 1, 2509, 9, 11, 2, 3, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aviatSmDetailsInactiveVersion.setStatus('current')
aviatSwResetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 1, 1)).setObjects(("AVIAT-SWMANAGEMENT-MIB", "aviatSmSoftReset"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatSwResetGroup = aviatSwResetGroup.setStatus('current')
aviatSwLoadGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 1, 2)).setObjects(("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadControl"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadStatus"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadRollbackDuration"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadRollbackTimer"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadActivateWaitDuration"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadActivateWaitTimer"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadActivateTime"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadUri"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSmLoadProgress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatSwLoadGroup = aviatSwLoadGroup.setStatus('current')
aviatSwDetailsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 1, 3)).setObjects(("AVIAT-SWMANAGEMENT-MIB", "aviatSmDetailsVersion"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSmDetailsInactiveVersion"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatSwDetailsGroup = aviatSwDetailsGroup.setStatus('current')
aviatSwManagementComplV1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 2509, 9, 11, 1, 2, 1)).setObjects(("AVIAT-SWMANAGEMENT-MIB", "aviatSwResetGroup"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSwLoadGroup"), ("AVIAT-SWMANAGEMENT-MIB", "aviatSwDetailsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aviatSwManagementComplV1 = aviatSwManagementComplV1.setStatus('current')
mibBuilder.exportSymbols("AVIAT-SWMANAGEMENT-MIB", aviatSwManagementModule=aviatSwManagementModule, aviatSmLoadControl=aviatSmLoadControl, aviatSmDetailsVersion=aviatSmDetailsVersion, aviatSwResetGroup=aviatSwResetGroup, aviatSmLoadStatus=aviatSmLoadStatus, aviatSwLoadGroup=aviatSwLoadGroup, aviatSmLoadRollbackDuration=aviatSmLoadRollbackDuration, aviatSmLoadActivateTime=aviatSmLoadActivateTime, aviatSwManagementCompliance=aviatSwManagementCompliance, aviatSwResetObjects=aviatSwResetObjects, aviatSwManagementConf=aviatSwManagementConf, aviatSwManagementMIBObjects=aviatSwManagementMIBObjects, aviatSmSoftReset=aviatSmSoftReset, aviatSmLoadActivateWaitTimer=aviatSmLoadActivateWaitTimer, aviatSwManagementComplV1=aviatSwManagementComplV1, aviatSmDetailsInactiveVersion=aviatSmDetailsInactiveVersion, aviatSmLoadActivateWaitDuration=aviatSmLoadActivateWaitDuration, aviatSwDetailsGroup=aviatSwDetailsGroup, aviatSmLoadProgress=aviatSmLoadProgress, aviatSwLoadObjects=aviatSwLoadObjects, aviatSmLoadRollbackTimer=aviatSmLoadRollbackTimer, aviatSmLoadUri=aviatSmLoadUri, aviatSwDetailsObjects=aviatSwDetailsObjects, PYSNMP_MODULE_ID=aviatSwManagementModule, aviatSwManagementGroups=aviatSwManagementGroups)
