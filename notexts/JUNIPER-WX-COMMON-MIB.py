#
# PySNMP MIB module JUNIPER-WX-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/juniper/JUNIPER-WX-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:27:41 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
jnxWxModules, jnxWxCommonMib = mibBuilder.importSymbols("JUNIPER-WX-GLOBAL-REG", "jnxWxModules", "jnxWxCommonMib")
TcChassisType, = mibBuilder.importSymbols("JUNIPER-WX-GLOBAL-TC", "TcChassisType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, Gauge32, IpAddress, Integer32, iso, Unsigned32, MibIdentifier, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "Gauge32", "IpAddress", "Integer32", "iso", "Unsigned32", "MibIdentifier", "TimeTicks", "ObjectIdentity")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
jnxWxCommonMibModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 8239, 1, 1, 3))
jnxWxCommonMibModule.setRevisions(('2003-09-30 08:45', '2003-04-01 00:00', '2003-03-10 00:00', '2002-06-03 00:00', '2002-03-27 00:00', '2002-02-22 00:00', '2002-01-23 00:00', '2002-01-17 00:00', '2001-08-07 00:00',))
if mibBuilder.loadTexts: jnxWxCommonMibModule.setLastUpdated('200206030000Z')
if mibBuilder.loadTexts: jnxWxCommonMibModule.setOrganization('Juniper Networks, Inc')
jnxWxCommonConfMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 1))
if mibBuilder.loadTexts: jnxWxCommonConfMib.setStatus('current')
jnxWxCommonObjs = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2))
if mibBuilder.loadTexts: jnxWxCommonObjs.setStatus('current')
jnxWxCommonEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3))
if mibBuilder.loadTexts: jnxWxCommonEvents.setStatus('current')
jnxWxSys = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1))
if mibBuilder.loadTexts: jnxWxSys.setStatus('current')
jnxWxChassis = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 2))
if mibBuilder.loadTexts: jnxWxChassis.setStatus('current')
jnxWxSysSwVersion = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxSysSwVersion.setStatus('current')
jnxWxSysHwVersion = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxSysHwVersion.setStatus('current')
jnxWxSysSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxSysSerialNumber.setStatus('current')
jnxWxSysTimeZoneOffset = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxSysTimeZoneOffset.setStatus('current')
jnxWxSysDaylightSaving = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxSysDaylightSaving.setStatus('current')
jnxWxChassisType = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 2, 2, 1), TcChassisType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxWxChassisType.setStatus('current')
jnxWxCommonEventObjs = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 1))
if mibBuilder.loadTexts: jnxWxCommonEventObjs.setStatus('current')
jnxWxCommonEventEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2))
if mibBuilder.loadTexts: jnxWxCommonEventEvents.setStatus('current')
jnxWxCommonEventEventsV2 = ObjectIdentity((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0))
if mibBuilder.loadTexts: jnxWxCommonEventEventsV2.setStatus('current')
jnxWxCommonEventDescr = MibScalar((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 1, 1), DisplayString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: jnxWxCommonEventDescr.setStatus('current')
jnxWxCommonEventInFailSafeMode = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 1))
if mibBuilder.loadTexts: jnxWxCommonEventInFailSafeMode.setStatus('current')
jnxWxCommonEventPowerSupplyFailure = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 2))
if mibBuilder.loadTexts: jnxWxCommonEventPowerSupplyFailure.setStatus('current')
jnxWxCommonEventPowerSupplyOk = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 3))
if mibBuilder.loadTexts: jnxWxCommonEventPowerSupplyOk.setStatus('current')
jnxWxCommonEventLicenseExpired = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 4)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventLicenseExpired.setStatus('current')
jnxWxCommonEventThruputLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 5)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventThruputLimitExceeded.setStatus('current')
jnxWxCommonEventLicenseWillExpire = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 6)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventLicenseWillExpire.setStatus('current')
jnxWxCommonEventLoginFailure = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 7)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventLoginFailure.setStatus('current')
jnxWxCommonEventFaultTolerantPassThrough = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 8)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventFaultTolerantPassThrough.setStatus('current')
jnxWxCommonEventFanFailure = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 9)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventFanFailure.setStatus('current')
jnxWxCommonEventFanSpeedVariation = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 10)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventFanSpeedVariation.setStatus('current')
jnxWxCommonEventFanOk = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 11)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventFanOk.setStatus('current')
jnxWxCommonEventInterfaceSpeedMismatch = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 12)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventInterfaceSpeedMismatch.setStatus('current')
jnxWxCommonEventInterfaceSpeedOk = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 13)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventInterfaceSpeedOk.setStatus('current')
jnxWxCommonEventInterfaceDuplexMismatch = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 14)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventInterfaceDuplexMismatch.setStatus('current')
jnxWxCommonEventIpsecSecurityAssociationAdded = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 15)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventIpsecSecurityAssociationAdded.setStatus('current')
jnxWxCommonEventIpsecSecurityAssociationExpired = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 16)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventIpsecSecurityAssociationExpired.setStatus('current')
jnxWxCommonEventIpsecSecurityAssociationDeleted = NotificationType((1, 3, 6, 1, 4, 1, 8239, 2, 1, 3, 2, 0, 17)).setObjects(("JUNIPER-WX-COMMON-MIB", "jnxWxCommonEventDescr"))
if mibBuilder.loadTexts: jnxWxCommonEventIpsecSecurityAssociationDeleted.setStatus('current')
mibBuilder.exportSymbols("JUNIPER-WX-COMMON-MIB", jnxWxCommonEventFaultTolerantPassThrough=jnxWxCommonEventFaultTolerantPassThrough, jnxWxChassisType=jnxWxChassisType, jnxWxCommonEventThruputLimitExceeded=jnxWxCommonEventThruputLimitExceeded, jnxWxSysSwVersion=jnxWxSysSwVersion, jnxWxSysHwVersion=jnxWxSysHwVersion, jnxWxCommonEvents=jnxWxCommonEvents, jnxWxSysSerialNumber=jnxWxSysSerialNumber, jnxWxCommonEventDescr=jnxWxCommonEventDescr, jnxWxCommonConfMib=jnxWxCommonConfMib, jnxWxCommonEventPowerSupplyOk=jnxWxCommonEventPowerSupplyOk, jnxWxCommonEventPowerSupplyFailure=jnxWxCommonEventPowerSupplyFailure, jnxWxCommonEventLoginFailure=jnxWxCommonEventLoginFailure, jnxWxCommonEventLicenseExpired=jnxWxCommonEventLicenseExpired, jnxWxCommonEventIpsecSecurityAssociationDeleted=jnxWxCommonEventIpsecSecurityAssociationDeleted, PYSNMP_MODULE_ID=jnxWxCommonMibModule, jnxWxCommonEventFanFailure=jnxWxCommonEventFanFailure, jnxWxCommonMibModule=jnxWxCommonMibModule, jnxWxCommonEventInterfaceDuplexMismatch=jnxWxCommonEventInterfaceDuplexMismatch, jnxWxCommonEventLicenseWillExpire=jnxWxCommonEventLicenseWillExpire, jnxWxCommonObjs=jnxWxCommonObjs, jnxWxCommonEventFanOk=jnxWxCommonEventFanOk, jnxWxSysTimeZoneOffset=jnxWxSysTimeZoneOffset, jnxWxCommonEventFanSpeedVariation=jnxWxCommonEventFanSpeedVariation, jnxWxCommonEventObjs=jnxWxCommonEventObjs, jnxWxCommonEventInterfaceSpeedOk=jnxWxCommonEventInterfaceSpeedOk, jnxWxCommonEventEventsV2=jnxWxCommonEventEventsV2, jnxWxCommonEventInterfaceSpeedMismatch=jnxWxCommonEventInterfaceSpeedMismatch, jnxWxCommonEventEvents=jnxWxCommonEventEvents, jnxWxCommonEventIpsecSecurityAssociationExpired=jnxWxCommonEventIpsecSecurityAssociationExpired, jnxWxSysDaylightSaving=jnxWxSysDaylightSaving, jnxWxCommonEventInFailSafeMode=jnxWxCommonEventInFailSafeMode, jnxWxCommonEventIpsecSecurityAssociationAdded=jnxWxCommonEventIpsecSecurityAssociationAdded, jnxWxSys=jnxWxSys, jnxWxChassis=jnxWxChassis)
