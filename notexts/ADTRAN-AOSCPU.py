#
# PySNMP MIB module ADTRAN-AOSCPU (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOSCPU
# Produced by pysmi-1.1.8 at Sun Jan 16 00:31:13 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSCommon, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSCommon", "adGenAOSConformance")
adIdentityShared, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
Gauge32, ObjectIdentity, Counter64, MibIdentifier, IpAddress, iso, Unsigned32, ModuleIdentity, Counter32, Bits, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter64", "MibIdentifier", "IpAddress", "iso", "Unsigned32", "ModuleIdentity", "Counter32", "Bits", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "TextualConvention", "DisplayString")
adGenAOSCpuUtilMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 4))
adGenAOSCpuUtilMib.setRevisions(('2004-10-04 00:00', '2009-04-30 00:00', '2009-08-13 00:00',))
if mibBuilder.loadTexts: adGenAOSCpuUtilMib.setLastUpdated('200904300000Z')
if mibBuilder.loadTexts: adGenAOSCpuUtilMib.setOrganization('ADTRAN, Inc.')
adGenAOSCpuUtil = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4))
adGenAOSResUtilThreshTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 0))
if mibBuilder.loadTexts: adGenAOSResUtilThreshTraps.setStatus('current')
adGenAOSCurrentCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 1), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSCurrentCpuUtil.setStatus('current')
adGenAOSClearUtilizationStats = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("reset", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: adGenAOSClearUtilizationStats.setStatus('current')
adGenAOS1MinCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS1MinCpuUtil.setStatus('current')
adGenAOS5MinCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 4), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOS5MinCpuUtil.setStatus('current')
adGenAOSMaxCpuUtil = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSMaxCpuUtil.setStatus('current')
adGenAOSMemPool = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 6), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSMemPool.setStatus('current')
adGenAOSHeapSize = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 7), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSHeapSize.setStatus('current')
adGenAOSHeapFree = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 8), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSHeapFree.setStatus('current')
adGenAOSProcessTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9), )
if mibBuilder.loadTexts: adGenAOSProcessTable.setStatus('current')
adGenAOSProcessEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1), ).setIndexNames((0, "ADTRAN-AOSCPU", "adGenAOSProcID"))
if mibBuilder.loadTexts: adGenAOSProcessEntry.setStatus('current')
adGenAOSProcID = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: adGenAOSProcID.setStatus('current')
adGenAOSProcName = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSProcName.setStatus('current')
adGenAOSProcPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSProcPriority.setStatus('current')
adGenAOSProcState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("running", 1), ("ready", 2), ("wait", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSProcState.setStatus('current')
adGenAOSProcCount = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 5), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSProcCount.setStatus('current')
adGenAOSProcExecTime = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 6), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSProcExecTime.setStatus('current')
adGenAOSProcRunTime = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 7), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSProcRunTime.setStatus('current')
adGenAOSProc1SecLd = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 9, 1, 8), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adGenAOSProc1SecLd.setStatus('current')
adGenAOSResUtilThreshTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10), )
if mibBuilder.loadTexts: adGenAOSResUtilThreshTable.setStatus('current')
adGenAOSResUtilThreshEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10, 1), ).setIndexNames((0, "ADTRAN-AOSCPU", "adGenAOSResType"), (0, "ADTRAN-AOSCPU", "adGenAOSResUtilThresh"), (0, "ADTRAN-AOSCPU", "adGenAOSResUtilTimeInterval"))
if mibBuilder.loadTexts: adGenAOSResUtilThreshEntry.setStatus('current')
adGenAOSResType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("cpu", 1), ("heap", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSResType.setStatus('current')
adGenAOSResUtilThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10, 1, 2), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 100))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSResUtilThresh.setStatus('current')
adGenAOSResUtilTimeInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10, 1, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(1, 86400))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSResUtilTimeInterval.setStatus('current')
adGenAOSResUtilThreshRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 10, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adGenAOSResUtilThreshRowStatus.setStatus('current')
adGenAOSResUtilThreshTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 11), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adGenAOSResUtilThreshTimestamp.setStatus('current')
adGenAOSResUtilThreshAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 0, 1)).setObjects(("ADTRAN-AOSCPU", "adGenAOSResType"), ("ADTRAN-AOSCPU", "adGenAOSResUtilThresh"), ("ADTRAN-AOSCPU", "adGenAOSResUtilTimeInterval"), ("ADTRAN-AOSCPU", "adGenAOSResUtilThreshTimestamp"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: adGenAOSResUtilThreshAlarm.setStatus('current')
adGenAOSResUtilThreshNormal = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 4, 0, 2)).setObjects(("ADTRAN-AOSCPU", "adGenAOSResType"), ("ADTRAN-AOSCPU", "adGenAOSResUtilThresh"), ("ADTRAN-AOSCPU", "adGenAOSResUtilTimeInterval"), ("ADTRAN-AOSCPU", "adGenAOSResUtilThreshTimestamp"), ("SNMPv2-MIB", "sysName"))
if mibBuilder.loadTexts: adGenAOSResUtilThreshNormal.setStatus('current')
adGenAOSCpuConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4))
adAOSCpuCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 1))
adAOSCpuGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 2))
adAOSCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 1, 1)).setObjects(("ADTRAN-AOSCPU", "adGenAOSCpuGroup"), ("ADTRAN-AOSCPU", "adGenAOSProcessGroup"), ("ADTRAN-AOSCPU", "adGenAOSThresholdGroup"), ("ADTRAN-AOSCPU", "adGenAOSThresholdTrapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSCompliance = adAOSCompliance.setStatus('current')
adGenAOSCpuGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 2, 1)).setObjects(("ADTRAN-AOSCPU", "adGenAOSCurrentCpuUtil"), ("ADTRAN-AOSCPU", "adGenAOSClearUtilizationStats"), ("ADTRAN-AOSCPU", "adGenAOS1MinCpuUtil"), ("ADTRAN-AOSCPU", "adGenAOS5MinCpuUtil"), ("ADTRAN-AOSCPU", "adGenAOSMaxCpuUtil"), ("ADTRAN-AOSCPU", "adGenAOSMemPool"), ("ADTRAN-AOSCPU", "adGenAOSHeapSize"), ("ADTRAN-AOSCPU", "adGenAOSHeapFree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSCpuGroup = adGenAOSCpuGroup.setStatus('current')
adGenAOSProcessGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 2, 2)).setObjects(("ADTRAN-AOSCPU", "adGenAOSProcName"), ("ADTRAN-AOSCPU", "adGenAOSProcPriority"), ("ADTRAN-AOSCPU", "adGenAOSProcState"), ("ADTRAN-AOSCPU", "adGenAOSProcCount"), ("ADTRAN-AOSCPU", "adGenAOSProcExecTime"), ("ADTRAN-AOSCPU", "adGenAOSProcRunTime"), ("ADTRAN-AOSCPU", "adGenAOSProc1SecLd"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSProcessGroup = adGenAOSProcessGroup.setStatus('current')
adGenAOSThresholdGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 2, 3)).setObjects(("ADTRAN-AOSCPU", "adGenAOSResType"), ("ADTRAN-AOSCPU", "adGenAOSResUtilThresh"), ("ADTRAN-AOSCPU", "adGenAOSResUtilTimeInterval"), ("ADTRAN-AOSCPU", "adGenAOSResUtilThreshRowStatus"), ("ADTRAN-AOSCPU", "adGenAOSResUtilThreshTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSThresholdGroup = adGenAOSThresholdGroup.setStatus('current')
adGenAOSThresholdTrapGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 4, 2, 4)).setObjects(("ADTRAN-AOSCPU", "adGenAOSResUtilThreshAlarm"), ("ADTRAN-AOSCPU", "adGenAOSResUtilThreshNormal"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSThresholdTrapGroup = adGenAOSThresholdTrapGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOSCPU", adGenAOSResUtilTimeInterval=adGenAOSResUtilTimeInterval, adGenAOSCpuConformance=adGenAOSCpuConformance, adGenAOSProcName=adGenAOSProcName, adAOSCpuGroups=adAOSCpuGroups, adAOSCpuCompliances=adAOSCpuCompliances, adGenAOSProcState=adGenAOSProcState, adGenAOSProcID=adGenAOSProcID, adGenAOSProcessGroup=adGenAOSProcessGroup, adGenAOSThresholdTrapGroup=adGenAOSThresholdTrapGroup, adGenAOSMaxCpuUtil=adGenAOSMaxCpuUtil, adGenAOSResUtilThreshNormal=adGenAOSResUtilThreshNormal, adGenAOSProc1SecLd=adGenAOSProc1SecLd, adGenAOSClearUtilizationStats=adGenAOSClearUtilizationStats, adGenAOSCpuGroup=adGenAOSCpuGroup, adGenAOSProcessEntry=adGenAOSProcessEntry, adGenAOSProcessTable=adGenAOSProcessTable, adGenAOSResUtilThreshAlarm=adGenAOSResUtilThreshAlarm, adGenAOSResType=adGenAOSResType, adGenAOSResUtilThreshTraps=adGenAOSResUtilThreshTraps, adAOSCompliance=adAOSCompliance, PYSNMP_MODULE_ID=adGenAOSCpuUtilMib, adGenAOSCpuUtil=adGenAOSCpuUtil, adGenAOSThresholdGroup=adGenAOSThresholdGroup, adGenAOSHeapSize=adGenAOSHeapSize, adGenAOS1MinCpuUtil=adGenAOS1MinCpuUtil, adGenAOSCpuUtilMib=adGenAOSCpuUtilMib, adGenAOS5MinCpuUtil=adGenAOS5MinCpuUtil, adGenAOSResUtilThreshTable=adGenAOSResUtilThreshTable, adGenAOSCurrentCpuUtil=adGenAOSCurrentCpuUtil, adGenAOSProcCount=adGenAOSProcCount, adGenAOSResUtilThreshTimestamp=adGenAOSResUtilThreshTimestamp, adGenAOSResUtilThreshEntry=adGenAOSResUtilThreshEntry, adGenAOSHeapFree=adGenAOSHeapFree, adGenAOSResUtilThreshRowStatus=adGenAOSResUtilThreshRowStatus, adGenAOSMemPool=adGenAOSMemPool, adGenAOSResUtilThresh=adGenAOSResUtilThresh, adGenAOSProcRunTime=adGenAOSProcRunTime, adGenAOSProcPriority=adGenAOSProcPriority, adGenAOSProcExecTime=adGenAOSProcExecTime)
