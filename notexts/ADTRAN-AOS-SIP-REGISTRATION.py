#
# PySNMP MIB module ADTRAN-AOS-SIP-REGISTRATION (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-SIP-REGISTRATION
# Produced by pysmi-1.1.8 at Sat Jan 15 17:50:19 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
adGenAOSConformance, adGenAOSVoice = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSVoice")
adIdentityShared, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier, Counter64, IpAddress, Counter32, ModuleIdentity, TimeTicks, Bits, ObjectIdentity, NotificationType, iso, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier", "Counter64", "IpAddress", "Counter32", "ModuleIdentity", "TimeTicks", "Bits", "ObjectIdentity", "NotificationType", "iso", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
adGenAOSSipRegistration = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 5, 4))
adGenAOSSipRegistration.setRevisions(('2010-11-02 00:00',))
if mibBuilder.loadTexts: adGenAOSSipRegistration.setLastUpdated('201011020000Z')
if mibBuilder.loadTexts: adGenAOSSipRegistration.setOrganization('ADTRAN, Inc.')
adSipRegistration = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4))
adSipRegistrationTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0))
adSipTrunkRegistrationAlarmTrunkIdentity = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTrunkIdentity.setStatus('current')
adSipTrunkRegistrationAlarmSipIdentity = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 2), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmSipIdentity.setStatus('current')
adSipTrunkRegistrationAlarmRegistrar = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 3), IpAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmRegistrar.setStatus('current')
adSipTrunkRegistrationAlarmTimestamp = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 4), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarmTimestamp.setStatus('current')
adSipTrunkRegistrationTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5), )
if mibBuilder.loadTexts: adSipTrunkRegistrationTable.setStatus('current')
adSipTrunkRegistrationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1), ).setIndexNames((0, "ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationTableIndex"))
if mibBuilder.loadTexts: adSipTrunkRegistrationEntry.setStatus('current')
adSipTrunkRegistrationTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 1), Unsigned32())
if mibBuilder.loadTexts: adSipTrunkRegistrationTableIndex.setStatus('current')
adSipTrunkRegistrationTrunkIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationTrunkIdentity.setStatus('current')
adSipTrunkRegistrationSipIdentity = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationSipIdentity.setStatus('current')
adSipTrunkRegistrationStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationStatus.setStatus('current')
adSipTrunkRegistrarIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrarIpAddress.setStatus('current')
adSipTrunkRegistrationGrantTime = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationGrantTime.setStatus('current')
adSipTrunkRegistrationExpireTime = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationExpireTime.setStatus('current')
adSipTrunkRegistrationSuccesses = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationSuccesses.setStatus('current')
adSipTrunkRegistrationFailures = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationFailures.setStatus('current')
adSipTrunkRegistrationRequests = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationRequests.setStatus('current')
adSipTrunkRegistrationChallenges = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationChallenges.setStatus('current')
adSipTrunkRegistrationRollovers = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 5, 1, 12), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adSipTrunkRegistrationRollovers.setStatus('current')
adSipTrunkRegistrationAlarm = NotificationType((1, 3, 6, 1, 4, 1, 664, 5, 53, 5, 4, 0, 1)).setObjects(("SNMPv2-MIB", "sysName"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
if mibBuilder.loadTexts: adSipTrunkRegistrationAlarm.setStatus('current')
adSipRegistrationConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12))
adSipRegistrationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1))
adSipRegistrationCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2))
adSipRegistrationFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 2, 1)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationNotificationUtilityGroup"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationNotificationGroup"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipRegistrationStatisticsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationFullCompliance = adSipRegistrationFullCompliance.setStatus('current')
adSipRegistrationNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 1)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationNotificationGroup = adSipRegistrationNotificationGroup.setStatus('current')
adSipRegistrationNotificationUtilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 2)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTrunkIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmSipIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmRegistrar"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationAlarmTimestamp"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationNotificationUtilityGroup = adSipRegistrationNotificationUtilityGroup.setStatus('current')
adSipRegistrationStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 12, 1, 3)).setObjects(("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationTrunkIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationSipIdentity"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationStatus"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrarIpAddress"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationGrantTime"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationExpireTime"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationSuccesses"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationFailures"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationRequests"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationChallenges"), ("ADTRAN-AOS-SIP-REGISTRATION", "adSipTrunkRegistrationRollovers"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adSipRegistrationStatisticsGroup = adSipRegistrationStatisticsGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-SIP-REGISTRATION", adSipTrunkRegistrarIpAddress=adSipTrunkRegistrarIpAddress, adSipTrunkRegistrationAlarmSipIdentity=adSipTrunkRegistrationAlarmSipIdentity, adSipTrunkRegistrationRollovers=adSipTrunkRegistrationRollovers, adGenAOSSipRegistration=adGenAOSSipRegistration, adSipTrunkRegistrationExpireTime=adSipTrunkRegistrationExpireTime, adSipRegistrationNotificationUtilityGroup=adSipRegistrationNotificationUtilityGroup, adSipTrunkRegistrationAlarmRegistrar=adSipTrunkRegistrationAlarmRegistrar, PYSNMP_MODULE_ID=adGenAOSSipRegistration, adSipTrunkRegistrationEntry=adSipTrunkRegistrationEntry, adSipTrunkRegistrationAlarm=adSipTrunkRegistrationAlarm, adSipTrunkRegistrationAlarmTimestamp=adSipTrunkRegistrationAlarmTimestamp, adSipTrunkRegistrationChallenges=adSipTrunkRegistrationChallenges, adSipTrunkRegistrationSuccesses=adSipTrunkRegistrationSuccesses, adSipRegistrationCompliances=adSipRegistrationCompliances, adSipTrunkRegistrationTableIndex=adSipTrunkRegistrationTableIndex, adSipTrunkRegistrationStatus=adSipTrunkRegistrationStatus, adSipRegistrationTraps=adSipRegistrationTraps, adSipTrunkRegistrationTable=adSipTrunkRegistrationTable, adSipTrunkRegistrationSipIdentity=adSipTrunkRegistrationSipIdentity, adSipRegistrationConformance=adSipRegistrationConformance, adSipRegistrationFullCompliance=adSipRegistrationFullCompliance, adSipRegistrationStatisticsGroup=adSipRegistrationStatisticsGroup, adSipRegistrationGroups=adSipRegistrationGroups, adSipRegistration=adSipRegistration, adSipTrunkRegistrationRequests=adSipTrunkRegistrationRequests, adSipTrunkRegistrationAlarmTrunkIdentity=adSipTrunkRegistrationAlarmTrunkIdentity, adSipTrunkRegistrationFailures=adSipTrunkRegistrationFailures, adSipTrunkRegistrationTrunkIdentity=adSipTrunkRegistrationTrunkIdentity, adSipRegistrationNotificationGroup=adSipRegistrationNotificationGroup, adSipTrunkRegistrationGrantTime=adSipTrunkRegistrationGrantTime)
