#
# PySNMP MIB module CTRON-SFPS-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-COMMON-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:36:36 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
sfpsAOProperties, sfpsDiagEventLog, sfpsSystemGenerics, sfpsAOPropertiesAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsAOProperties", "sfpsDiagEventLog", "sfpsSystemGenerics", "sfpsAOPropertiesAPI")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ObjectIdentity, iso, Counter64, Unsigned32, MibIdentifier, Integer32, Counter32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Gauge32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "iso", "Counter64", "Unsigned32", "MibIdentifier", "Integer32", "Counter32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Gauge32", "ModuleIdentity", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class HexInteger(Integer32):
    pass

sfpsGenericVersionTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1), )
if mibBuilder.loadTexts: sfpsGenericVersionTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsGenericVersionTable.setDescription('Table describing the SFS generics and their versions\n                that are contained within this image.')
sfpsGenericVersionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1), ).setIndexNames((0, "CTRON-SFPS-COMMON-MIB", "sfpsGenericVersionHash"))
if mibBuilder.loadTexts: sfpsGenericVersionEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsGenericVersionEntry.setDescription('An entry in the table instanced by the Generic name.')
sfpsGenericVersionHash = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsGenericVersionHash.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsGenericVersionHash.setDescription('Hash of the name to make it a unique entry.')
sfpsGenericVersionName = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsGenericVersionName.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsGenericVersionName.setDescription('Name of the Generic.')
sfpsGenericVersionVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsGenericVersionVersion.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsGenericVersionVersion.setDescription('Version stamp of the generic component.')
sfpsGenericVersionMIBRev = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 3, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsGenericVersionMIBRev.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsGenericVersionMIBRev.setDescription('MIB version of the generic component.')
sfpsDiagLogConfigTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1), )
if mibBuilder.loadTexts: sfpsDiagLogConfigTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigTable.setDescription('This table contains the informtion to configure an\n                 Event Logger object.')
sfpsDiagLogConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1), ).setIndexNames((0, "CTRON-SFPS-COMMON-MIB", "sfpsDiagLogConfigInstance"))
if mibBuilder.loadTexts: sfpsDiagLogConfigEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigEntry.setDescription('Each entry contains configuration data.')
sfpsDiagLogConfigInstance = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsDiagLogConfigInstance.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigInstance.setDescription('The instance of this Event Logger.')
sfpsDiagLogConfigStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigStatus.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigStatus.setDescription('The status of this Event Logger object.')
sfpsDiagLogConfigIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsDiagLogConfigIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigIndex.setDescription('The current index in the circular buffer where events are \n                 being logged.')
sfpsDiagLogConfigStart = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigStart.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigStart.setDescription('The starting index in the circular buffer to display.')
sfpsDiagLogConfigStop = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigStop.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigStop.setDescription('The last index in the circular buffer to display.')
sfpsDiagLogConfigLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigLogIndex.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigLogIndex.setDescription('The current index in the log buffer where we are looking.')
sfpsDiagLogConfigFilterMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigFilterMatch.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigFilterMatch.setDescription('The specified Event Id to log. A value of 0 will \n                 cause every event to be logged.')
sfpsDiagLogConfigFilterStart = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigFilterStart.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigFilterStart.setDescription('The beginning range of Event Ids to log.')
sfpsDiagLogConfigFilterStop = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigFilterStop.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigFilterStop.setDescription('The ending range of Event Ids to log.')
sfpsDiagLogAccessPortControl = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 10), HexInteger()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogAccessPortControl.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogAccessPortControl.setDescription('Leaf to be used to set a port bit mask. This bit mask\n                 represents which ports shall be statically set to be\n                 an ACCESS port. Bit 0 corresponds to Port 1.')
sfpsDiagLogCallIdleTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 11), Integer32().clone(60)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogCallIdleTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogCallIdleTime.setDescription('Leaf to be used to set a debug variable. (in seconds)')
sfpsDiagLogFilterAddTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 12), Integer32().clone(900)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogFilterAddTimer.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogFilterAddTimer.setDescription('Leaf to be used to set how long a filter connection\n                 should be (Default : 900 seconds)')
sfpsDiagLogRedirectorWakeup = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogRedirectorWakeup.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogRedirectorWakeup.setDescription('Leaf to be used to set how often the Redirector\n                 wakes up to service the queue (in seconds)')
sfpsDiagLogRedirectorNumPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 14), Integer32().clone(64)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogRedirectorNumPackets.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogRedirectorNumPackets.setDescription('Leaf to be used to set how many packets the\n                 Redirector reads off at a time.')
sfpsDiagLogEndSystemTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 15), Integer32().clone(600)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogEndSystemTimeout.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogEndSystemTimeout.setDescription('Leaf to be used to set a debug variable. (Default : \n                 10 minutes) (in seconds)')
sfpsDiagLogSwitchIdleInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 16), Integer32().clone(30)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogSwitchIdleInterval.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogSwitchIdleInterval.setDescription('Leaf to be used to set a debug variable. (in seconds)')
sfpsDiagLogInlnFltrAgeTime = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 17), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogInlnFltrAgeTime.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogInlnFltrAgeTime.setDescription('Leaf to be used to set the BAF age time (seconds).')
sfpsDiagLogConfigDebug9 = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 18), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigDebug9.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigDebug9.setDescription('Leaf to be used to set a debug variable.')
sfpsDiagLogSignalThrottle = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 19), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogSignalThrottle.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogSignalThrottle.setDescription('Leaf to be used to set the Signal Thottle knob.\n                 Throttling defaults to off. By setting it to\n                 1,2,5, or 10 one can dictate the rate (signal/second)\n                 at which SFPS sends signals to the ACMS Signal Stack..')
sfpsDiagLogConfigOther = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("string", 1), ("integer", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigOther.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigOther.setDescription('Dictates the format of the Event to be displayed (either \n                 Text or Integer values).')
sfpsDiagLogConfigSoftReset = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 21), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigSoftReset.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigSoftReset.setDescription('')
sfpsDiagLogConfigSFPSVlan = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 2, 6, 1, 1, 1, 22), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsDiagLogConfigSFPSVlan.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsDiagLogConfigSFPSVlan.setDescription('')
sfpsAOPropertiesTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1), )
if mibBuilder.loadTexts: sfpsAOPropertiesTable.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesTable.setDescription('')
sfpsAOPropertiesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1), ).setIndexNames((0, "CTRON-SFPS-COMMON-MIB", "sfpsAOPropertiesTag"))
if mibBuilder.loadTexts: sfpsAOPropertiesEntry.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesEntry.setDescription('An entry in the table instanced by the tag.')
sfpsAOPropertiesTag = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesTag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesTag.setDescription('')
sfpsAOPropertiesTagDescriptor = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesTagDescriptor.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesTagDescriptor.setDescription('')
sfpsAOPropertiesPrettyType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesPrettyType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesPrettyType.setDescription('')
sfpsAOPropertiesNumBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesNumBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesNumBytes.setDescription('')
sfpsAOPropertiesIsLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesIsLimit.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesIsLimit.setDescription('')
sfpsAOPropertiesIsMobile = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesIsMobile.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesIsMobile.setDescription('')
sfpsAOPropertiesIsSingle = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesIsSingle.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesIsSingle.setDescription('')
sfpsAOPropertiesNoBlock = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesNoBlock.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesNoBlock.setDescription('')
sfpsAOPropertiesNoDelta = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("false", 1), ("true", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesNoDelta.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesNoDelta.setDescription('')
sfpsAOPropertiesAPITag = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPITag.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesAPITag.setDescription('')
sfpsAOPropertiesAPITagString = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesAPITagString.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesAPITagString.setDescription('')
sfpsAOPropertiesAPIPrettyType = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesAPIPrettyType.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesAPIPrettyType.setDescription('')
sfpsAOPropertiesAPINumBytes = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsAOPropertiesAPINumBytes.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesAPINumBytes.setDescription('')
sfpsAOPropertiesAPIIsLimit = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("false", 2), ("true", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPIIsLimit.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesAPIIsLimit.setDescription('')
sfpsAOPropertiesAPIIsMobile = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("false", 2), ("true", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPIIsMobile.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesAPIIsMobile.setDescription('')
sfpsAOPropertiesAPIIsSingle = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("false", 2), ("true", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPIIsSingle.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesAPIIsSingle.setDescription('')
sfpsAOPropertiesAPINoBlock = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("false", 2), ("true", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPINoBlock.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesAPINoBlock.setDescription('')
sfpsAOPropertiesAPINoDelta = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSet", 1), ("false", 2), ("true", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPINoDelta.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesAPINoDelta.setDescription('')
sfpsAOPropertiesAPIAction = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 1, 5, 2, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("readProperties", 1), ("setProperties", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsAOPropertiesAPIAction.setStatus('mandatory')
if mibBuilder.loadTexts: sfpsAOPropertiesAPIAction.setDescription('')
mibBuilder.exportSymbols("CTRON-SFPS-COMMON-MIB", sfpsAOPropertiesNumBytes=sfpsAOPropertiesNumBytes, sfpsDiagLogConfigSFPSVlan=sfpsDiagLogConfigSFPSVlan, sfpsAOPropertiesAPIIsSingle=sfpsAOPropertiesAPIIsSingle, sfpsAOPropertiesEntry=sfpsAOPropertiesEntry, sfpsDiagLogConfigLogIndex=sfpsDiagLogConfigLogIndex, sfpsAOPropertiesTable=sfpsAOPropertiesTable, sfpsAOPropertiesAPIIsMobile=sfpsAOPropertiesAPIIsMobile, sfpsDiagLogConfigEntry=sfpsDiagLogConfigEntry, sfpsDiagLogConfigSoftReset=sfpsDiagLogConfigSoftReset, sfpsGenericVersionEntry=sfpsGenericVersionEntry, sfpsGenericVersionTable=sfpsGenericVersionTable, sfpsDiagLogConfigStatus=sfpsDiagLogConfigStatus, sfpsDiagLogConfigFilterStart=sfpsDiagLogConfigFilterStart, sfpsAOPropertiesTagDescriptor=sfpsAOPropertiesTagDescriptor, sfpsDiagLogConfigStop=sfpsDiagLogConfigStop, sfpsDiagLogSignalThrottle=sfpsDiagLogSignalThrottle, sfpsDiagLogConfigDebug9=sfpsDiagLogConfigDebug9, sfpsDiagLogConfigFilterStop=sfpsDiagLogConfigFilterStop, sfpsDiagLogConfigOther=sfpsDiagLogConfigOther, sfpsAOPropertiesAPINoBlock=sfpsAOPropertiesAPINoBlock, sfpsGenericVersionMIBRev=sfpsGenericVersionMIBRev, sfpsDiagLogConfigInstance=sfpsDiagLogConfigInstance, sfpsDiagLogConfigTable=sfpsDiagLogConfigTable, sfpsGenericVersionName=sfpsGenericVersionName, sfpsDiagLogConfigStart=sfpsDiagLogConfigStart, sfpsDiagLogCallIdleTime=sfpsDiagLogCallIdleTime, sfpsDiagLogRedirectorWakeup=sfpsDiagLogRedirectorWakeup, sfpsAOPropertiesIsSingle=sfpsAOPropertiesIsSingle, sfpsAOPropertiesNoDelta=sfpsAOPropertiesNoDelta, sfpsGenericVersionHash=sfpsGenericVersionHash, sfpsDiagLogEndSystemTimeout=sfpsDiagLogEndSystemTimeout, sfpsAOPropertiesNoBlock=sfpsAOPropertiesNoBlock, sfpsDiagLogConfigFilterMatch=sfpsDiagLogConfigFilterMatch, sfpsAOPropertiesAPINumBytes=sfpsAOPropertiesAPINumBytes, sfpsAOPropertiesAPITag=sfpsAOPropertiesAPITag, sfpsAOPropertiesAPITagString=sfpsAOPropertiesAPITagString, sfpsAOPropertiesAPIAction=sfpsAOPropertiesAPIAction, sfpsAOPropertiesAPIIsLimit=sfpsAOPropertiesAPIIsLimit, HexInteger=HexInteger, sfpsDiagLogAccessPortControl=sfpsDiagLogAccessPortControl, sfpsDiagLogSwitchIdleInterval=sfpsDiagLogSwitchIdleInterval, sfpsDiagLogRedirectorNumPackets=sfpsDiagLogRedirectorNumPackets, sfpsAOPropertiesPrettyType=sfpsAOPropertiesPrettyType, sfpsGenericVersionVersion=sfpsGenericVersionVersion, sfpsAOPropertiesIsLimit=sfpsAOPropertiesIsLimit, sfpsAOPropertiesIsMobile=sfpsAOPropertiesIsMobile, sfpsAOPropertiesAPIPrettyType=sfpsAOPropertiesAPIPrettyType, sfpsDiagLogFilterAddTimer=sfpsDiagLogFilterAddTimer, sfpsDiagLogInlnFltrAgeTime=sfpsDiagLogInlnFltrAgeTime, sfpsDiagLogConfigIndex=sfpsDiagLogConfigIndex, sfpsAOPropertiesTag=sfpsAOPropertiesTag, sfpsAOPropertiesAPINoDelta=sfpsAOPropertiesAPINoDelta)
