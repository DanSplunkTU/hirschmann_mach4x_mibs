#
# PySNMP MIB module ADTRAN-AOS-SIP-REGISTRATION (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-SIP-REGISTRATION
# Produced by pysmi-1.1.8 at Fri Jan  7 15:51:59 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
adGenAOSVoice, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSVoice", "adGenAOSConformance")
adIdentityShared, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentityShared")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
sysName, = mibBuilder.importSymbols("SNMPv2-MIB", "sysName")
ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, NotificationType, Gauge32, ObjectIdentity, Unsigned32, IpAddress, Bits, Integer32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "IpAddress", "Bits", "Integer32", "MibIdentifier", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ADTRAN-AOS-SIP-REGISTRATION", adSipTrunkRegistrationTableIndex=adSipTrunkRegistrationTableIndex, adSipTrunkRegistrationSuccesses=adSipTrunkRegistrationSuccesses, PYSNMP_MODULE_ID=adGenAOSSipRegistration, adSipRegistration=adSipRegistration, adSipTrunkRegistrationSipIdentity=adSipTrunkRegistrationSipIdentity, adSipTrunkRegistrationAlarmTrunkIdentity=adSipTrunkRegistrationAlarmTrunkIdentity, adSipTrunkRegistrationStatus=adSipTrunkRegistrationStatus, adSipRegistrationNotificationGroup=adSipRegistrationNotificationGroup, adSipRegistrationCompliances=adSipRegistrationCompliances, adSipTrunkRegistrationExpireTime=adSipTrunkRegistrationExpireTime, adSipTrunkRegistrationAlarmRegistrar=adSipTrunkRegistrationAlarmRegistrar, adSipTrunkRegistrationTrunkIdentity=adSipTrunkRegistrationTrunkIdentity, adSipTrunkRegistrationFailures=adSipTrunkRegistrationFailures, adSipTrunkRegistrationEntry=adSipTrunkRegistrationEntry, adSipTrunkRegistrationTable=adSipTrunkRegistrationTable, adSipTrunkRegistrarIpAddress=adSipTrunkRegistrarIpAddress, adSipRegistrationGroups=adSipRegistrationGroups, adSipTrunkRegistrationAlarm=adSipTrunkRegistrationAlarm, adSipRegistrationTraps=adSipRegistrationTraps, adSipTrunkRegistrationRollovers=adSipTrunkRegistrationRollovers, adSipTrunkRegistrationRequests=adSipTrunkRegistrationRequests, adGenAOSSipRegistration=adGenAOSSipRegistration, adSipRegistrationConformance=adSipRegistrationConformance, adSipRegistrationFullCompliance=adSipRegistrationFullCompliance, adSipRegistrationStatisticsGroup=adSipRegistrationStatisticsGroup, adSipTrunkRegistrationGrantTime=adSipTrunkRegistrationGrantTime, adSipTrunkRegistrationAlarmTimestamp=adSipTrunkRegistrationAlarmTimestamp, adSipRegistrationNotificationUtilityGroup=adSipRegistrationNotificationUtilityGroup, adSipTrunkRegistrationAlarmSipIdentity=adSipTrunkRegistrationAlarmSipIdentity, adSipTrunkRegistrationChallenges=adSipTrunkRegistrationChallenges)
