#
# PySNMP MIB module JUNIPER-WX-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/JUNIPER-WX-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:46:27 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
jnxWxCommonMib, jnxWxModules = mibBuilder.importSymbols("JUNIPER-WX-GLOBAL-REG", "jnxWxCommonMib", "jnxWxModules")
TcChassisType, = mibBuilder.importSymbols("JUNIPER-WX-GLOBAL-TC", "TcChassisType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, NotificationType, IpAddress, iso, ObjectIdentity, MibIdentifier, ModuleIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "NotificationType", "IpAddress", "iso", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Bits", "Counter32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
jnxWxCommonMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 1, 3))
jnxWxCommonMibModule.setRevisions(('2003-09-30 08:45', '2003-04-01 00:00', '2003-03-10 00:00', '2002-06-03 00:00', '2002-03-27 00:00', '2002-02-22 00:00', '2002-01-23 00:00', '2002-01-17 00:00', '2001-08-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxWxCommonMibModule.setRevisionsDescriptions(('\n\t\t\tFix minor error in description of jnxWxSysDaylightSaving.', '\n\t\t\tAdd interface duplex mismatch notification.', '\n\t\t\tAdd interface speed mismatch notifications.', '\n\t\t\tAdd Fan notifications.', '\n\t\t\tAdd FaultTolerantPassthrough notification.', '\n\t\t\tAdd LoginFailure notification.', '\n\t\t\tAdd LicenseWillExpire notification.', '\n\t\t\tAdd ThruputLimitExceeded notification.', '\n\t\t\tRev 1.0\n\t\t\tInitial version of MIB module JUNIPER-WX-COMMON-MIB.',))
if mibBuilder.loadTexts: jnxWxCommonMibModule.setLastUpdated('200206030000Z')
if mibBuilder.loadTexts: jnxWxCommonMibModule.setOrganization('Juniper Networks, Inc')
if mibBuilder.loadTexts: jnxWxCommonMibModule.setContactInfo('\n\t\t\t\t\tCustomer Support\n\t\t\t\t\tJuniper Networks, Inc.\n\t\t\t\t\t1194 North Mathilda Avenue\n\t\t\t\t\tSunnyvale, CA  94089\n\n\t\t\t\t\t+1 888-314-JTAC\n\t\t\t\t\tsupport@juniper.net')
if mibBuilder.loadTexts: jnxWxCommonMibModule.setDescription("\n\t\t\tA MIB module containing definitions of managed objects\n\t\t\timplemented by all Juniper Networks' products.")
jnxWxCommonConfMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 1))
if mibBuilder.loadTexts: jnxWxCommonConfMib.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonConfMib.setDescription('\n\t\t\tSub-tree for WAN Acceleration MIB conformance statements.')
jnxWxCommonObjs = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2))
if mibBuilder.loadTexts: jnxWxCommonObjs.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonObjs.setDescription('\n\t\t\tSub-tree for common MIB objects.')
jnxWxCommonEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3))
if mibBuilder.loadTexts: jnxWxCommonEvents.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEvents.setDescription('\n\t\t\tSub-tree for common MIB events.')
jnxWxSys = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1))
if mibBuilder.loadTexts: jnxWxSys.setStatus('current')
if mibBuilder.loadTexts: jnxWxSys.setDescription('\n\t\t\tSub-tree for common system objects.')
jnxWxChassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 2))
if mibBuilder.loadTexts: jnxWxChassis.setStatus('current')
if mibBuilder.loadTexts: jnxWxChassis.setDescription('\n\t\t\tSub-tree for common chassis information.')
jnxWxSysSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxSysSwVersion.setStatus('current')
if mibBuilder.loadTexts: jnxWxSysSwVersion.setDescription('Full software version. The first two components of the full\n\t\t\tversion are the major and minor versions. The third component\n\t\t\tindicates the maintenance release number and the fourth,\n\t\t\tthe build number.')
jnxWxSysHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxSysHwVersion.setStatus('current')
if mibBuilder.loadTexts: jnxWxSysHwVersion.setDescription('Hardware version of the unit.')
jnxWxSysSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxSysSerialNumber.setStatus('current')
if mibBuilder.loadTexts: jnxWxSysSerialNumber.setDescription('The serial number of the unit. If not available,\n\t\t\tan empty string is returned.')
jnxWxSysTimeZoneOffset = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxSysTimeZoneOffset.setStatus('current')
if mibBuilder.loadTexts: jnxWxSysTimeZoneOffset.setDescription("The offset in seconds from UTC of the system's time zone.\n\t\t\tValues are negative for locations west of UTC and positive\n\t\t\tfor locations east of UTC.")
jnxWxSysDaylightSaving = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxSysDaylightSaving.setStatus('current')
if mibBuilder.loadTexts: jnxWxSysDaylightSaving.setDescription("Whether daylight savings are currently in effect for the\n\t\t\tsystem's time zone.")
jnxWxChassisType = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 2, 1), TcChassisType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxChassisType.setStatus('current')
if mibBuilder.loadTexts: jnxWxChassisType.setDescription('Chassis type for this WX device.')
jnxWxCommonEventObjs = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 1))
if mibBuilder.loadTexts: jnxWxCommonEventObjs.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventObjs.setDescription('\n\t\t\tBranch for objects meant only to be sent in event varbinds.')
jnxWxCommonEventEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2))
if mibBuilder.loadTexts: jnxWxCommonEventEvents.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventEvents.setDescription('\n\t\t\tBranch for the events themselves.')
jnxWxCommonEventEventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0))
if mibBuilder.loadTexts: jnxWxCommonEventEventsV2.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventEventsV2.setDescription('\n\t\t\tBranch for SNMPv2 events. The OIDs for SNMPv2 events should\n\t\t\thave a zero as the next-to-last sub-identifier (as specified\n\t\t\tin RFC1902).')
jnxWxCommonEventDescr = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxWxCommonEventDescr.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventDescr.setDescription('String that provides a textual description of the event.')
jnxWxCommonEventInFailSafeMode = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 1))
if mibBuilder.loadTexts: jnxWxCommonEventInFailSafeMode.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventInFailSafeMode.setDescription('This trap is sent when the device boots up in fail-safe mode.\n\t\t\tThis can happen for one of the following reasons:\n\t\t\to Fail-safe reboot was explicitly initiated by the user.\n\t\t\to The device rebooted automatically too many times because of\n\t\t\t  the failure of internal consistency checks or the failure of\n\t\t\t  tests that verify proper operation of the device.')
jnxWxCommonEventPowerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 2))
if mibBuilder.loadTexts: jnxWxCommonEventPowerSupplyFailure.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventPowerSupplyFailure.setDescription('One or more sources of power to the system has failed.\n\t\t\tA redundant power-supply has presumably taken over.\n\n\t\t\tNOTE: This trap is for future use.\n\t\t\t      WX devices currently do not generate this trap.')
jnxWxCommonEventPowerSupplyOk = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 3))
if mibBuilder.loadTexts: jnxWxCommonEventPowerSupplyOk.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventPowerSupplyOk.setDescription('One or more previously failed sources of power is now\n\t\t\tworking normally. The transition to normal condition happened\n\t\t\twithout the system having to be restarted.\n\n\t\t\tNOTE: This trap is for future use.\n\t\t\t      WX devices currently do not generate this trap.')
jnxWxCommonEventLicenseExpired = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 4)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventLicenseExpired.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventLicenseExpired.setDescription('The license for the system expired.\n\t\t\tAs a result, the system will switch over to\n\t\t\tand stay in pass-through mode.')
jnxWxCommonEventThruputLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 5)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventThruputLimitExceeded.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventThruputLimitExceeded.setDescription('The throughput of traffic through the device\n\t\t\thas exceeded the limit for which it has\n\t\t\tbeen licensed.')
jnxWxCommonEventLicenseWillExpire = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 6)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventLicenseWillExpire.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventLicenseWillExpire.setDescription('The license for the system is about to\n\t\t\texpire shortly. When it eventually does\n\t\t\texpire, the system will switch over to\n\t\t\tand stay in pass-through mode.')
jnxWxCommonEventLoginFailure = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 7)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventLoginFailure.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventLoginFailure.setDescription("A user's login attempt via the console/ssh/web server\n\t\t\tfailed due to incorrect username or password.")
jnxWxCommonEventFaultTolerantPassThrough = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 8)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventFaultTolerantPassThrough.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventFaultTolerantPassThrough.setDescription('An anomalous health condition was detected.\n\t\t\tIt would have subsequently triggered hardware\n\t\t\tpass through mode followed by a reboot.')
jnxWxCommonEventFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 9)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventFanFailure.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventFanFailure.setDescription("A cooling fan inside the device has failed.\n\t\t\tThe 'jnxWxCommonEventDescr' object has the name of\n\t\t\tthe fan that failed.\n\t\t\t\n            This trap is currently unused")
jnxWxCommonEventFanSpeedVariation = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 10)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventFanSpeedVariation.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventFanSpeedVariation.setDescription("The speed of a cooling fan inside the device is either\n\t\t\ttoo low or too high. The 'jnxWxCommonEventDescr' object\n\t\t\thas the name of the fan that has the problem.\n\t\t\t\n\t\t\tThis trap is currently unused.")
jnxWxCommonEventFanOk = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 11)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventFanOk.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventFanOk.setDescription("A cooling fan inside the device that had previously\n\t\t\tfailed or whose speed variation was high is now\n\t\t\tworking properly. The 'jnxWxCommonEventDescr' object\n\t\t\thas the name of the fan that has recovered.\n\t\t\t\n\t\t\tThis trap is currently unused.")
jnxWxCommonEventInterfaceSpeedMismatch = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 12)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventInterfaceSpeedMismatch.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventInterfaceSpeedMismatch.setDescription('A mismatch is detected between the local and remote\n\t\t\tinterface settings. This can happen due to a mismatch\n\t\t\tin the local and remote interface speed or mode. ')
jnxWxCommonEventInterfaceSpeedOk = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 13)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventInterfaceSpeedOk.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventInterfaceSpeedOk.setDescription('A mismatch previously detected between the local and remote\n\t\t\tinterface settings is now resolved. The local and remote interface\n\t\t\tspeed and mode are matched. ')
jnxWxCommonEventInterfaceDuplexMismatch = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 14)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventInterfaceDuplexMismatch.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventInterfaceDuplexMismatch.setDescription("A possible mismatch was detected between the duplex setting\n\t\t\tof either the local or remote interface and that of the\n\t\t\tdevice attached to that interface. The interface (local\n\t\t\tor remote) is identified by the 'jnxWxCommonEventDescr' object.\n\n\t\t\tNote that this notification is quite different from\n\t\t\tjnxWxCommonEventInterfaceSpeedMismatch, which compares the\n\t\t\tlocal and remote interfaces on the same WX device.")
jnxWxCommonEventIpsecSecurityAssociationAdded = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 15)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventIpsecSecurityAssociationAdded.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventIpsecSecurityAssociationAdded.setDescription('An IPSec security association has been negotiated and added\n            to security association database.')
jnxWxCommonEventIpsecSecurityAssociationExpired = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 16)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventIpsecSecurityAssociationExpired.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventIpsecSecurityAssociationExpired.setDescription('An IPSec security association has been deleted from the\n            security association database.')
jnxWxCommonEventIpsecSecurityAssociationDeleted = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 17)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventIpsecSecurityAssociationDeleted.setStatus('current')
if mibBuilder.loadTexts: jnxWxCommonEventIpsecSecurityAssociationDeleted.setDescription('An IPSec security association has been deleted from the\n            security association database.')
mibBuilder.exportSymbols("JUNIPER-WX-COMMON-MIB", jnxWxSys=jnxWxSys, jnxWxCommonConfMib=jnxWxCommonConfMib, jnxWxCommonEventFanOk=jnxWxCommonEventFanOk, jnxWxCommonEventInFailSafeMode=jnxWxCommonEventInFailSafeMode, jnxWxSysSerialNumber=jnxWxSysSerialNumber, jnxWxCommonEventInterfaceDuplexMismatch=jnxWxCommonEventInterfaceDuplexMismatch, jnxWxCommonEventIpsecSecurityAssociationDeleted=jnxWxCommonEventIpsecSecurityAssociationDeleted, jnxWxChassisType=jnxWxChassisType, jnxWxCommonEventPowerSupplyOk=jnxWxCommonEventPowerSupplyOk, jnxWxSysDaylightSaving=jnxWxSysDaylightSaving, jnxWxCommonMibModule=jnxWxCommonMibModule, jnxWxCommonEventEvents=jnxWxCommonEventEvents, jnxWxCommonEvents=jnxWxCommonEvents, jnxWxCommonEventIpsecSecurityAssociationAdded=jnxWxCommonEventIpsecSecurityAssociationAdded, jnxWxCommonEventObjs=jnxWxCommonEventObjs, jnxWxCommonEventFanFailure=jnxWxCommonEventFanFailure, jnxWxCommonEventPowerSupplyFailure=jnxWxCommonEventPowerSupplyFailure, jnxWxCommonEventLicenseWillExpire=jnxWxCommonEventLicenseWillExpire, jnxWxCommonEventLoginFailure=jnxWxCommonEventLoginFailure, jnxWxSysSwVersion=jnxWxSysSwVersion, jnxWxCommonEventEventsV2=jnxWxCommonEventEventsV2, jnxWxCommonEventInterfaceSpeedOk=jnxWxCommonEventInterfaceSpeedOk, jnxWxCommonEventThruputLimitExceeded=jnxWxCommonEventThruputLimitExceeded, jnxWxCommonEventLicenseExpired=jnxWxCommonEventLicenseExpired, jnxWxCommonEventInterfaceSpeedMismatch=jnxWxCommonEventInterfaceSpeedMismatch, jnxWxCommonEventIpsecSecurityAssociationExpired=jnxWxCommonEventIpsecSecurityAssociationExpired, jnxWxSysHwVersion=jnxWxSysHwVersion, jnxWxCommonEventDescr=jnxWxCommonEventDescr, jnxWxCommonEventFanSpeedVariation=jnxWxCommonEventFanSpeedVariation, jnxWxCommonObjs=jnxWxCommonObjs, jnxWxSysTimeZoneOffset=jnxWxSysTimeZoneOffset, jnxWxCommonEventFaultTolerantPassThrough=jnxWxCommonEventFaultTolerantPassThrough, jnxWxChassis=jnxWxChassis, PYSNMP_MODULE_ID=jnxWxCommonMibModule)
