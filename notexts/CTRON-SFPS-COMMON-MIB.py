#
# PySNMP MIB module CTRON-SFPS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-COMMON-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:16 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
sfpsDiagEventLog, sfpsAOPropertiesAPI, sfpsSystemGenerics, sfpsAOProperties = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsDiagEventLog", "sfpsAOPropertiesAPI", "sfpsSystemGenerics", "sfpsAOProperties")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity, Counter32, NotificationType, Unsigned32, Integer32, iso, TimeTicks, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "Unsigned32", "Integer32", "iso", "TimeTicks", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class HexInteger(Integer32):
    pass

sfpsGenericVersionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1), )
if mibBuilder.loadTexts: sfpsGenericVersionTable.setStatus('mandatory')
sfpsGenericVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1), ).setIndexNames((0, "CTRON-SFPS-COMMON-MIB", "sfpsGenericVersionHash"))
if mibBuilder.loadTexts: sfpsGenericVersionEntry.setStatus('mandatory')
sfpsGenericVersionHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsGenericVersionHash.setStatus('mandatory')
sfpsGenericVersionName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsGenericVersionName.setStatus('mandatory')
sfpsGenericVersionVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsGenericVersionVersion.setStatus('mandatory')
sfpsGenericVersionMIBRev = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsGenericVersionMIBRev.setStatus('mandatory')
sfpsDiagLogConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1), )
if mibBuilder.loadTexts: sfpsDiagLogConfigTable.setStatus('mandatory')
sfpsDiagLogConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-COMMON-MIB", "sfpsDiagLogConfigInstance"))
if mibBuilder.loadTexts: sfpsDiagLogConfigEntry.setStatus('mandatory')
sfpsDiagLogConfigInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsDiagLogConfigInstance.setStatus('mandatory')
sfpsDiagLogConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigStatus.setStatus('mandatory')
sfpsDiagLogConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsDiagLogConfigIndex.setStatus('mandatory')
sfpsDiagLogConfigStart = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigStart.setStatus('mandatory')
sfpsDiagLogConfigStop = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigStop.setStatus('mandatory')
sfpsDiagLogConfigLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigLogIndex.setStatus('mandatory')
sfpsDiagLogConfigFilterMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigFilterMatch.setStatus('mandatory')
sfpsDiagLogConfigFilterStart = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigFilterStart.setStatus('mandatory')
sfpsDiagLogConfigFilterStop = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigFilterStop.setStatus('mandatory')
sfpsDiagLogAccessPortControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 10), HexInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogAccessPortControl.setStatus('mandatory')
sfpsDiagLogCallIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 11), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogCallIdleTime.setStatus('mandatory')
sfpsDiagLogFilterAddTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 12), Integer32().clone(900)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogFilterAddTimer.setStatus('mandatory')
sfpsDiagLogRedirectorWakeup = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogRedirectorWakeup.setStatus('mandatory')
sfpsDiagLogRedirectorNumPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 14), Integer32().clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogRedirectorNumPackets.setStatus('mandatory')
sfpsDiagLogEndSystemTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 15), Integer32().clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogEndSystemTimeout.setStatus('mandatory')
sfpsDiagLogSwitchIdleInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 16), Integer32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogSwitchIdleInterval.setStatus('mandatory')
sfpsDiagLogInlnFltrAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogInlnFltrAgeTime.setStatus('mandatory')
sfpsDiagLogConfigDebug9 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigDebug9.setStatus('mandatory')
sfpsDiagLogSignalThrottle = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogSignalThrottle.setStatus('mandatory')
sfpsDiagLogConfigOther = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("string", 1), ("integer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigOther.setStatus('mandatory')
sfpsDiagLogConfigSoftReset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigSoftReset.setStatus('mandatory')
sfpsDiagLogConfigSFPSVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigSFPSVlan.setStatus('mandatory')
sfpsAOPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1), )
if mibBuilder.loadTexts: sfpsAOPropertiesTable.setStatus('mandatory')
sfpsAOPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1), ).setIndexNames((0, "CTRON-SFPS-COMMON-MIB", "sfpsAOPropertiesTag"))
if mibBuilder.loadTexts: sfpsAOPropertiesEntry.setStatus('mandatory')
sfpsAOPropertiesTag = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesTag.setStatus('mandatory')
sfpsAOPropertiesTagDescriptor = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesTagDescriptor.setStatus('mandatory')
sfpsAOPropertiesPrettyType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesPrettyType.setStatus('mandatory')
sfpsAOPropertiesNumBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesNumBytes.setStatus('mandatory')
sfpsAOPropertiesIsLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesIsLimit.setStatus('mandatory')
sfpsAOPropertiesIsMobile = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesIsMobile.setStatus('mandatory')
sfpsAOPropertiesIsSingle = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesIsSingle.setStatus('mandatory')
sfpsAOPropertiesNoBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesNoBlock.setStatus('mandatory')
sfpsAOPropertiesNoDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesNoDelta.setStatus('mandatory')
sfpsAOPropertiesAPITag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPITag.setStatus('mandatory')
sfpsAOPropertiesAPITagString = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesAPITagString.setStatus('mandatory')
sfpsAOPropertiesAPIPrettyType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesAPIPrettyType.setStatus('mandatory')
sfpsAOPropertiesAPINumBytes = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesAPINumBytes.setStatus('mandatory')
sfpsAOPropertiesAPIIsLimit = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("false", 2), ("true", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPIIsLimit.setStatus('mandatory')
sfpsAOPropertiesAPIIsMobile = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("false", 2), ("true", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPIIsMobile.setStatus('mandatory')
sfpsAOPropertiesAPIIsSingle = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("false", 2), ("true", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPIIsSingle.setStatus('mandatory')
sfpsAOPropertiesAPINoBlock = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("false", 2), ("true", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPINoBlock.setStatus('mandatory')
sfpsAOPropertiesAPINoDelta = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("false", 2), ("true", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPINoDelta.setStatus('mandatory')
sfpsAOPropertiesAPIAction = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readProperties", 1), ("setProperties", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPIAction.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-COMMON-MIB", sfpsDiagLogRedirectorWakeup=sfpsDiagLogRedirectorWakeup, sfpsAOPropertiesAPIIsSingle=sfpsAOPropertiesAPIIsSingle, sfpsGenericVersionEntry=sfpsGenericVersionEntry, sfpsDiagLogFilterAddTimer=sfpsDiagLogFilterAddTimer, sfpsDiagLogCallIdleTime=sfpsDiagLogCallIdleTime, sfpsDiagLogConfigStart=sfpsDiagLogConfigStart, sfpsDiagLogSignalThrottle=sfpsDiagLogSignalThrottle, sfpsDiagLogConfigSoftReset=sfpsDiagLogConfigSoftReset, sfpsAOPropertiesAPIPrettyType=sfpsAOPropertiesAPIPrettyType, sfpsAOPropertiesAPINoBlock=sfpsAOPropertiesAPINoBlock, sfpsDiagLogInlnFltrAgeTime=sfpsDiagLogInlnFltrAgeTime, sfpsAOPropertiesIsSingle=sfpsAOPropertiesIsSingle, sfpsDiagLogConfigInstance=sfpsDiagLogConfigInstance, sfpsAOPropertiesNoBlock=sfpsAOPropertiesNoBlock, sfpsAOPropertiesAPINoDelta=sfpsAOPropertiesAPINoDelta, sfpsAOPropertiesNumBytes=sfpsAOPropertiesNumBytes, sfpsAOPropertiesTable=sfpsAOPropertiesTable, sfpsAOPropertiesAPITagString=sfpsAOPropertiesAPITagString, sfpsAOPropertiesEntry=sfpsAOPropertiesEntry, sfpsDiagLogAccessPortControl=sfpsDiagLogAccessPortControl, sfpsAOPropertiesNoDelta=sfpsAOPropertiesNoDelta, sfpsDiagLogConfigEntry=sfpsDiagLogConfigEntry, sfpsDiagLogConfigStatus=sfpsDiagLogConfigStatus, sfpsAOPropertiesAPITag=sfpsAOPropertiesAPITag, sfpsAOPropertiesAPIIsLimit=sfpsAOPropertiesAPIIsLimit, sfpsGenericVersionHash=sfpsGenericVersionHash, sfpsAOPropertiesAPINumBytes=sfpsAOPropertiesAPINumBytes, sfpsDiagLogConfigIndex=sfpsDiagLogConfigIndex, sfpsAOPropertiesTagDescriptor=sfpsAOPropertiesTagDescriptor, sfpsGenericVersionVersion=sfpsGenericVersionVersion, sfpsGenericVersionName=sfpsGenericVersionName, sfpsGenericVersionMIBRev=sfpsGenericVersionMIBRev, HexInteger=HexInteger, sfpsDiagLogRedirectorNumPackets=sfpsDiagLogRedirectorNumPackets, sfpsDiagLogSwitchIdleInterval=sfpsDiagLogSwitchIdleInterval, sfpsDiagLogConfigStop=sfpsDiagLogConfigStop, sfpsAOPropertiesIsLimit=sfpsAOPropertiesIsLimit, sfpsGenericVersionTable=sfpsGenericVersionTable, sfpsDiagLogConfigSFPSVlan=sfpsDiagLogConfigSFPSVlan, sfpsDiagLogEndSystemTimeout=sfpsDiagLogEndSystemTimeout, sfpsDiagLogConfigFilterMatch=sfpsDiagLogConfigFilterMatch, sfpsDiagLogConfigFilterStop=sfpsDiagLogConfigFilterStop, sfpsAOPropertiesTag=sfpsAOPropertiesTag, sfpsAOPropertiesIsMobile=sfpsAOPropertiesIsMobile, sfpsAOPropertiesAPIAction=sfpsAOPropertiesAPIAction, sfpsDiagLogConfigLogIndex=sfpsDiagLogConfigLogIndex, sfpsDiagLogConfigDebug9=sfpsDiagLogConfigDebug9, sfpsAOPropertiesAPIIsMobile=sfpsAOPropertiesAPIIsMobile, sfpsDiagLogConfigTable=sfpsDiagLogConfigTable, sfpsDiagLogConfigOther=sfpsDiagLogConfigOther, sfpsDiagLogConfigFilterStart=sfpsDiagLogConfigFilterStart, sfpsAOPropertiesPrettyType=sfpsAOPropertiesPrettyType)
