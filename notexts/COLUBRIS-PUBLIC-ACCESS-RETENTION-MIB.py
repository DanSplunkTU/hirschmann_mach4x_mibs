#
# PySNMP MIB module COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB.my
# Produced by pysmi-1.1.8 at Mon Feb  7 16:13:22 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ColubrisSSIDOrNone, = mibBuilder.importSymbols("COLUBRIS-TC", "ColubrisSSIDOrNone")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
TimeTicks, Gauge32, ObjectIdentity, MibIdentifier, ModuleIdentity, IpAddress, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, NotificationType, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "IpAddress", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "NotificationType", "Counter64", "iso")
DisplayString, TextualConvention, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "DateAndTime")
colubrisPublicAccessRetentionMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 15))
if mibBuilder.loadTexts: colubrisPublicAccessRetentionMIB.setLastUpdated('200410280000Z')
if mibBuilder.loadTexts: colubrisPublicAccessRetentionMIB.setOrganization('Colubris Networks, Inc.')
colubrisPublicAccessRetentionMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1))
publicAccessRetentionSessionsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1))
publicAccessRetentionPeriodicStatsGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2))
publicAccessRetentionSessionsMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 1), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionSessionsMaxCount.setStatus('current')
publicAccessRetentionSessionsMaxTime = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 1200)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionSessionsMaxTime.setStatus('current')
publicAccessRetentionSessionTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3), )
if mibBuilder.loadTexts: publicAccessRetentionSessionTable.setStatus('current')
publicAccessRetentionSessionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1), ).setIndexNames((0, "COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionIndex"))
if mibBuilder.loadTexts: publicAccessRetentionSessionEntry.setStatus('current')
publicAccessRetentionSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: publicAccessRetentionSessionIndex.setStatus('current')
publicAccessRetentionSessionState = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unassigned", 0), ("connected", 2), ("reconnecting", 3), ("disconnecting", 4), ("disconnected", 5), ("disconnectingAdministrative", 6), ("disconnectedAdministrative", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionState.setStatus('current')
publicAccessRetentionSessionUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 253))).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionUserName.setStatus('current')
publicAccessRetentionSessionStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionStartTime.setStatus('current')
publicAccessRetentionSessionDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 5), Counter32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionDuration.setStatus('current')
publicAccessRetentionSessionStationIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionStationIpAddress.setStatus('current')
publicAccessRetentionSessionPacketsSent = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionPacketsSent.setStatus('current')
publicAccessRetentionSessionPacketsReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionPacketsReceived.setStatus('current')
publicAccessRetentionSessionBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionBytesSent.setStatus('current')
publicAccessRetentionSessionBytesReceived = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionBytesReceived.setStatus('current')
publicAccessRetentionSessionSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 1, 3, 1, 11), ColubrisSSIDOrNone()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionSessionSSID.setStatus('current')
publicAccessRetentionPeriodicStatsMaxCount = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionPeriodicStatsMaxCount.setStatus('current')
publicAccessRetentionPeriodicStatsDuration = MibScalar((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(300, 1200)).clone(300)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: publicAccessRetentionPeriodicStatsDuration.setStatus('current')
publicAccessRetentionPeriodTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3), )
if mibBuilder.loadTexts: publicAccessRetentionPeriodTable.setStatus('current')
publicAccessRetentionPeriodEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1), ).setIndexNames((0, "COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodIndex"))
if mibBuilder.loadTexts: publicAccessRetentionPeriodEntry.setStatus('current')
publicAccessRetentionPeriodIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 9999)))
if mibBuilder.loadTexts: publicAccessRetentionPeriodIndex.setStatus('current')
publicAccessRetentionPeriodStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodStartTime.setStatus('current')
publicAccessRetentionPeriodStopTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 3), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodStopTime.setStatus('current')
publicAccessRetentionPeriodHighestSessionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodHighestSessionCount.setStatus('current')
publicAccessRetentionPeriodTotalSessionCount = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 15, 1, 2, 3, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: publicAccessRetentionPeriodTotalSessionCount.setStatus('current')
publicAccessRetentionMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 2))
publicAccessRetentionMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 2, 0))
publicAccessRetentionSessionMaxCountReachedTrap = NotificationType((1, 3, 6, 1, 4, 1, 8744, 5, 15, 2, 0, 1)).setObjects(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxCount"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxTime"))
if mibBuilder.loadTexts: publicAccessRetentionSessionMaxCountReachedTrap.setStatus('current')
colubrisPublicAccessRetentionMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3))
colubrisPublicAccessRetentionMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 1))
colubrisPublicAccessRetentionMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2))
colubrisPublicAccessRetentionMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 1, 1)).setObjects(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "colubrisPublicAccessRetentionSessionsMIBGroup"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "colubrisPublicAccessRetentionPeriodicStatsMIBGroup"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "colubrisPublicAccessRetentionNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessRetentionMIBCompliance = colubrisPublicAccessRetentionMIBCompliance.setStatus('current')
colubrisPublicAccessRetentionSessionsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2, 1)).setObjects(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxCount"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionsMaxTime"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionState"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionUserName"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionStartTime"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionDuration"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionStationIpAddress"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionPacketsSent"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionPacketsReceived"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionBytesSent"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionBytesReceived"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionSSID"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessRetentionSessionsMIBGroup = colubrisPublicAccessRetentionSessionsMIBGroup.setStatus('current')
colubrisPublicAccessRetentionPeriodicStatsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2, 2)).setObjects(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodicStatsDuration"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodicStatsMaxCount"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodStartTime"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodStopTime"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodHighestSessionCount"), ("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionPeriodTotalSessionCount"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessRetentionPeriodicStatsMIBGroup = colubrisPublicAccessRetentionPeriodicStatsMIBGroup.setStatus('current')
colubrisPublicAccessRetentionNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 8744, 5, 15, 3, 2, 3)).setObjects(("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", "publicAccessRetentionSessionMaxCountReachedTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisPublicAccessRetentionNotificationGroup = colubrisPublicAccessRetentionNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("COLUBRIS-PUBLIC-ACCESS-RETENTION-MIB", publicAccessRetentionPeriodStopTime=publicAccessRetentionPeriodStopTime, publicAccessRetentionSessionEntry=publicAccessRetentionSessionEntry, colubrisPublicAccessRetentionMIB=colubrisPublicAccessRetentionMIB, publicAccessRetentionMIBNotifications=publicAccessRetentionMIBNotifications, publicAccessRetentionSessionState=publicAccessRetentionSessionState, publicAccessRetentionSessionBytesSent=publicAccessRetentionSessionBytesSent, publicAccessRetentionSessionPacketsReceived=publicAccessRetentionSessionPacketsReceived, colubrisPublicAccessRetentionPeriodicStatsMIBGroup=colubrisPublicAccessRetentionPeriodicStatsMIBGroup, publicAccessRetentionSessionsGroup=publicAccessRetentionSessionsGroup, publicAccessRetentionSessionTable=publicAccessRetentionSessionTable, colubrisPublicAccessRetentionNotificationGroup=colubrisPublicAccessRetentionNotificationGroup, publicAccessRetentionPeriodStartTime=publicAccessRetentionPeriodStartTime, colubrisPublicAccessRetentionMIBObjects=colubrisPublicAccessRetentionMIBObjects, publicAccessRetentionSessionMaxCountReachedTrap=publicAccessRetentionSessionMaxCountReachedTrap, colubrisPublicAccessRetentionSessionsMIBGroup=colubrisPublicAccessRetentionSessionsMIBGroup, publicAccessRetentionSessionDuration=publicAccessRetentionSessionDuration, publicAccessRetentionSessionStartTime=publicAccessRetentionSessionStartTime, PYSNMP_MODULE_ID=colubrisPublicAccessRetentionMIB, publicAccessRetentionPeriodicStatsMaxCount=publicAccessRetentionPeriodicStatsMaxCount, publicAccessRetentionSessionsMaxCount=publicAccessRetentionSessionsMaxCount, colubrisPublicAccessRetentionMIBGroups=colubrisPublicAccessRetentionMIBGroups, publicAccessRetentionSessionSSID=publicAccessRetentionSessionSSID, publicAccessRetentionSessionPacketsSent=publicAccessRetentionSessionPacketsSent, colubrisPublicAccessRetentionMIBCompliance=colubrisPublicAccessRetentionMIBCompliance, publicAccessRetentionSessionsMaxTime=publicAccessRetentionSessionsMaxTime, publicAccessRetentionSessionUserName=publicAccessRetentionSessionUserName, publicAccessRetentionPeriodicStatsDuration=publicAccessRetentionPeriodicStatsDuration, publicAccessRetentionSessionBytesReceived=publicAccessRetentionSessionBytesReceived, publicAccessRetentionPeriodicStatsGroup=publicAccessRetentionPeriodicStatsGroup, colubrisPublicAccessRetentionMIBCompliances=colubrisPublicAccessRetentionMIBCompliances, publicAccessRetentionMIBNotificationPrefix=publicAccessRetentionMIBNotificationPrefix, publicAccessRetentionPeriodTable=publicAccessRetentionPeriodTable, publicAccessRetentionPeriodEntry=publicAccessRetentionPeriodEntry, publicAccessRetentionSessionStationIpAddress=publicAccessRetentionSessionStationIpAddress, colubrisPublicAccessRetentionMIBConformance=colubrisPublicAccessRetentionMIBConformance, publicAccessRetentionPeriodHighestSessionCount=publicAccessRetentionPeriodHighestSessionCount, publicAccessRetentionSessionIndex=publicAccessRetentionSessionIndex, publicAccessRetentionPeriodIndex=publicAccessRetentionPeriodIndex, publicAccessRetentionPeriodTotalSessionCount=publicAccessRetentionPeriodTotalSessionCount)
