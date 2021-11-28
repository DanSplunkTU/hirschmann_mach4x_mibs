#
# PySNMP MIB module LIEBERT-GP-SYSTEM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-SYSTEM-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:31:08 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
lgpAgentDeviceIndex, lgpAgentConnectedDeviceCount = mibBuilder.importSymbols("LIEBERT-GP-AGENT-MIB", "lgpAgentDeviceIndex", "lgpAgentConnectedDeviceCount")
liebertSystemModuleReg, lgpSystem = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "liebertSystemModuleReg", "lgpSystem")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Counter32, Unsigned32, Counter64, ObjectIdentity, Integer32, ModuleIdentity, Gauge32, TimeTicks, IpAddress, MibIdentifier, NotificationType, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Counter32", "Unsigned32", "Counter64", "ObjectIdentity", "Integer32", "ModuleIdentity", "Gauge32", "TimeTicks", "IpAddress", "MibIdentifier", "NotificationType", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
liebertSystemModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 8, 1))
liebertSystemModule.setRevisions(('2008-11-17 00:00', '2008-07-02 00:00', '2008-01-10 00:00', '2007-05-29 00:00', '2006-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: liebertSystemModule.setRevisionsDescriptions(('Added support for NXL unit.', 'Added missing items to the IMPORT statement', 'Add system notifications sub-tree and modified contact email address.', 'Added support for XDF Unit.', 'Added support for Liebert DS Unit.',))
if mibBuilder.loadTexts: liebertSystemModule.setLastUpdated('200811170000Z')
if mibBuilder.loadTexts: liebertSystemModule.setOrganization('Liebert Corporation')
if mibBuilder.loadTexts: liebertSystemModule.setContactInfo('Contact:   Technical Support\n\n      Postal:\n      Liebert Corporation\n      1050 Dearborn Drive\n      P.O. Box 29186\n      Columbus OH, 43229\n      US\n\n      Tel: +1 (800) 222-5877\n\n      E-mail: liebert.monitoring@vertivco.com\n      Web:    www.vertivco.com\n\n      Author:  Gregory M. Hoge')
if mibBuilder.loadTexts: liebertSystemModule.setDescription("The MIB module used to specify Liebert Controller OIDs\n\n      Copyright 2000-2008 Liebert Corporation. All rights reserved.\n      Reproduction of this document is authorized on the condition\n      that the forgoing copyright notice is included.\n\n      This Specification is supplied 'AS IS' and Liebert Corporation\n      makes no warranty, either express or implied, as to the use,\n      operation, condition, or performance of the Specification.")
lgpSysStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 1))
if mibBuilder.loadTexts: lgpSysStatistics.setStatus('current')
if mibBuilder.loadTexts: lgpSysStatistics.setDescription('This sub-tree is used to register Liebert System Statistics object\n        identifiers.')
if mibBuilder.loadTexts: lgpSysStatistics.setReference('The registrations for the objects in this sub-tree are\n        defined below in the sub-section titled Liebert System Statistics\n        Group.')
lgpSysStatus = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2))
if mibBuilder.loadTexts: lgpSysStatus.setStatus('current')
if mibBuilder.loadTexts: lgpSysStatus.setDescription('This sub-tree is used to register Liebert System Status object\n        identifiers.')
if mibBuilder.loadTexts: lgpSysStatus.setReference('The registrations for the objects in this sub-tree are\n        defined below in the sub-section titled Liebert System Status\n        Group.')
lgpSysSettings = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 3))
if mibBuilder.loadTexts: lgpSysSettings.setStatus('current')
if mibBuilder.loadTexts: lgpSysSettings.setDescription('This sub-tree is used to register Liebert System Settings object\n        identifiers.')
if mibBuilder.loadTexts: lgpSysSettings.setReference('The registrations for the objects in this sub-tree are\n        defined below in the sub-section titled Liebert System Settings\n        Group.')
lgpSysControl = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4))
if mibBuilder.loadTexts: lgpSysControl.setStatus('current')
if mibBuilder.loadTexts: lgpSysControl.setDescription('This sub-tree is used to register Liebert System Control object\n        identifiers.')
if mibBuilder.loadTexts: lgpSysControl.setReference('The registrations for the objects in this sub-tree are\n        defined below in the sub-section titled Liebert System Control\n        Group.')
lgpSysTime = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 5))
if mibBuilder.loadTexts: lgpSysTime.setStatus('current')
if mibBuilder.loadTexts: lgpSysTime.setDescription('This sub-tree is used to register Liebert System Time object\n        identifiers.')
if mibBuilder.loadTexts: lgpSysTime.setReference('The registrations for the objects in this sub-tree are\n        defined below in the sub-section titled Liebert System Time\n        Group.')
lgpSysMaintenance = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6))
if mibBuilder.loadTexts: lgpSysMaintenance.setStatus('current')
if mibBuilder.loadTexts: lgpSysMaintenance.setDescription('This sub-tree is used to register Liebert System Maintenance object\n        identifiers.')
if mibBuilder.loadTexts: lgpSysMaintenance.setReference('The registrations for the objects in this sub-tree are\n        defined below in the sub-section titled Liebert System Maintenance\n        Group.')
lgpSysEventDescription = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysEventDescription.setStatus('current')
if mibBuilder.loadTexts: lgpSysEventDescription.setDescription('An ASCII textual description for the event. This object is\n        primarily used in the varbind of some notifications to provide\n        a simple human-readable description.')
lgpSysEventNotifications = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8))
if mibBuilder.loadTexts: lgpSysEventNotifications.setStatus('current')
if mibBuilder.loadTexts: lgpSysEventNotifications.setDescription('This sub-tree is used to register Liebert System Notification object\n        identifiers.')
lgpSysDeviceComponentGroup = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9))
if mibBuilder.loadTexts: lgpSysDeviceComponentGroup.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceComponentGroup.setDescription('This sub-tree registers well known device components.')
if mibBuilder.loadTexts: lgpSysDeviceComponentGroup.setReference("These well known components are referenced in the\n        'lgpSysDeviceComponentDescr' column in the\n        'lgpSysDeviceComponentTable'.")
lgpSysDeviceComponentTable = MibTable((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1), )
if mibBuilder.loadTexts: lgpSysDeviceComponentTable.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceComponentTable.setDescription('A list of components of devices identified by their serial number and \n            or model number.\n\n            This table contains zero, one, or many rows. The NMS cannot create or\n            delete rows from the table. The rows are created by the agent based upon\n            the capabilities of the managed device.')
lgpSysDeviceComponentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1), ).setIndexNames((0, "LIEBERT-GP-AGENT-MIB", "lgpAgentDeviceIndex"), (0, "LIEBERT-GP-SYSTEM-MIB", "lgpSysDeviceComponentIndex"))
if mibBuilder.loadTexts: lgpSysDeviceComponentEntry.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceComponentEntry.setDescription("This entry defines the contents of the columns for the table\n                'lgpSysDeviceComponentTable'.")
lgpSysDeviceComponentIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: lgpSysDeviceComponentIndex.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceComponentIndex.setDescription("This is the index indicating the row in the table\n                 'lgpSysDeviceComponentTable' for a component entry.")
lgpSysDeviceComponentDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysDeviceComponentDescr.setReference("The object identifiers in this column can be found in the \n                 sub-tree 'lgpSysDeviceComponentWellknown'.")
if mibBuilder.loadTexts: lgpSysDeviceComponentDescr.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceComponentDescr.setDescription('An OID representing a component of the device indicated by the\n                index lgpAgentDeviceIndex.')
lgpSysDeviceComponentSerialNum = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysDeviceComponentSerialNum.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceComponentSerialNum.setDescription("This is the serial number of the component described by the OID \n                'lgpSysDeviceComponentDescr'. This data is intended for \n                display / human consumption. Do not use this field for determining\n                programmatic behavior.")
lgpSysDeviceComponentModelNum = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(255, 255)).setFixedLength(255)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysDeviceComponentModelNum.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceComponentModelNum.setDescription("This is the model identifier of the component described by the OID \n                'lgpSysDeviceComponentDescr'. This data is intended for \n                display / human consumption. Do not use this field for determining\n                programmatic behavior.")
lgpSysDeviceComponentWellknown = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5))
if mibBuilder.loadTexts: lgpSysDeviceComponentWellknown.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceComponentWellknown.setDescription('This sub-tree registers well known Liebert System Components.')
if mibBuilder.loadTexts: lgpSysDeviceComponentWellknown.setReference("These well known measurement identifiers are referenced in the\n             'lgpSysDeviceComponentDescr' column in the\n             'lgpSysDeviceComponentTable'.")
lgpSysDeviceBatCabinet = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 5))
if mibBuilder.loadTexts: lgpSysDeviceBatCabinet.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceBatCabinet.setDescription("This sub-tree is used to register a battery cabinet component.\n                    To determine the cabinet being described in a\n                    multi-cabinet system, this point implements an additional\n                    two indexes. The first index describes the module the cabinet\n                    is located in. The second index describes the cabinet\n                    number. In an SMS (Single-Module System) the first index is\n                    always 1.\n\n                    Example: lgpSysDeviceComponentCabinet.2.4\n\n                        'lgpSysDeviceCabinet' = Point is a battery cabinet.\n                                     '.2' = Cabinet is in the second module.\n                                     '.4' = Cabinet number 4 in second module")
lgpSysDeviceParallelCabinet = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 6))
if mibBuilder.loadTexts: lgpSysDeviceParallelCabinet.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceParallelCabinet.setDescription('This sub-tree is used to register a parallel cabinet.')
lgpSysDeviceMaintBypass = ObjectIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 9, 5, 7))
if mibBuilder.loadTexts: lgpSysDeviceMaintBypass.setStatus('current')
if mibBuilder.loadTexts: lgpSysDeviceMaintBypass.setDescription('This sub-tree is used to register the maintenance bypass.')
lgpSysNotification = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8, 1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-SYSTEM-MIB", "lgpSysEventDescription"))
if mibBuilder.loadTexts: lgpSysNotification.setStatus('current')
if mibBuilder.loadTexts: lgpSysNotification.setDescription("This notification is a generic notification intended for direct user\n        visibility.  The user event description identifies the system\n        condition that has occurred.  This text will be prefixed with either\n        'Active:', 'Cleared:', or 'Message:' depending on the state of the\n        event.  Note: That a prefix of 'Message:' identifies a stateless event\n        and as such there will be no corresponding 'Cleared:' trap sent.")
lgpSysNormal = NotificationType((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 8, 2)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("LIEBERT-GP-AGENT-MIB", "lgpAgentConnectedDeviceCount"))
if mibBuilder.loadTexts: lgpSysNormal.setStatus('current')
if mibBuilder.loadTexts: lgpSysNormal.setDescription('The system has returned to a normal operating state. This implies\n        prior to the generation of this event the system was operating in a\n        state where one or more alarm or warning conditions were present.\n        All of those alarms or conditions have now cleared.\n\n        NOTE: This notification may be generated after a short delay during a\n        cold boot of the system -- if no alarms or conditions are present in the\n        monitored device(s) at that time.')
lgpSysStatisticsRunHrs = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 1, 1), Unsigned32()).setUnits('hours').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysStatisticsRunHrs.setStatus('current')
if mibBuilder.loadTexts: lgpSysStatisticsRunHrs.setDescription('Accumulated run hours of the system.')
lgpSysSelfTestResult = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("passed", 2), ("failed", 3), ("inProgress", 4), ("sysFailure", 5), ("inhibited", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysSelfTestResult.setStatus('current')
if mibBuilder.loadTexts: lgpSysSelfTestResult.setDescription('The outcome of the previous self-test.')
lgpSysState = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("normalOperation", 1), ("startUp", 2), ("normalWithWarning", 3), ("normalWithAlarm", 4), ("abnormalOperation", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysState.setStatus('current')
if mibBuilder.loadTexts: lgpSysState.setDescription('The operating status for the system. The intent of this data\n        is to provide a high level status of the system.\n\n        The possible states are:\n\n            normalOperation(1)\n                The system is operating normally with no active warnings or \n                alarms.\n            startUp(2)\n                The system is in a startup state (initializing). Monitoring \n                operations and information may not be fully supported at this \n                time. This state will clear automatically when the system is \n                fully initialized and ready to accept monitoring commands.\n            normalWithWarning(3)\n                The system is operating normally with one or more active \n                warnings. Appropriate personnel should investigate the \n                warning(s) as soon as possible and take appropriate action. \n            normalWithAlarm(4)\n                The system is operating normally with one or more active \n                alarms. Appropriate personnel should investigate the alarm(s)\n                as soon as possible and take appropriate action. \n            abnormalOperation(5)\n                They system is operating abnormally. There is a \n                failure within the system that is unexpected under normal \n                operating conditions. Appropriate personnel should investigate\n                the cause as soon as possible. The normal functioning of\n                the system is likely inhibited.')
lgpSysAudibleAlarm = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysAudibleAlarm.setStatus('current')
if mibBuilder.loadTexts: lgpSysAudibleAlarm.setDescription('The state of the audible alarm of the device.')
lgpSysSelfTest = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysSelfTest.setStatus('current')
if mibBuilder.loadTexts: lgpSysSelfTest.setDescription("Self-Test Command.  This command will initiate a system self-test of\n        the system.  If already initiated, this command will abort the\n        self-test.  This command should be sent with a parameter of 1.  This\n        variable doesn't return a value when read.")
lgpSysControlOperationOnOff = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("on", 1), ("off", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysControlOperationOnOff.setStatus('current')
if mibBuilder.loadTexts: lgpSysControlOperationOnOff.setDescription("This object allows control of the system functionality.  This will not\n        affect the communications or control of the system, so that once turned\n        off, the system operation can be restored by setting this value to \n        'on'.")
lgpSysTimeEpoch = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 5, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpSysTimeEpoch.setStatus('current')
if mibBuilder.loadTexts: lgpSysTimeEpoch.setDescription('The present time of the system.  This time is represented as the\n        number of seconds since the epoch of 1970-01-01 00:00:00 GMT.')
lgpSysMaintenanceCapacity = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 1), Unsigned32()).setUnits('percent').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysMaintenanceCapacity.setStatus('current')
if mibBuilder.loadTexts: lgpSysMaintenanceCapacity.setDescription('The relative percentage of time that has elapsed since the last\n        scheduled maintenance was performed.  When this value reaches 100%,\n        the device is due for another scheduled maintenance procedure.')
lgpSysMaintenanceYear = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 2), Unsigned32()).setUnits('year').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysMaintenanceYear.setStatus('current')
if mibBuilder.loadTexts: lgpSysMaintenanceYear.setDescription('The year in which the next scheduled service is due')
lgpSysMaintenanceMonth = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 7, 6, 3), Unsigned32()).setUnits('month').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpSysMaintenanceMonth.setStatus('current')
if mibBuilder.loadTexts: lgpSysMaintenanceMonth.setDescription('The month in which the next scheduled service is due')
mibBuilder.exportSymbols("LIEBERT-GP-SYSTEM-MIB", lgpSysDeviceComponentModelNum=lgpSysDeviceComponentModelNum, lgpSysDeviceMaintBypass=lgpSysDeviceMaintBypass, lgpSysStatisticsRunHrs=lgpSysStatisticsRunHrs, lgpSysTimeEpoch=lgpSysTimeEpoch, lgpSysDeviceBatCabinet=lgpSysDeviceBatCabinet, lgpSysSelfTest=lgpSysSelfTest, liebertSystemModule=liebertSystemModule, lgpSysDeviceComponentIndex=lgpSysDeviceComponentIndex, lgpSysNotification=lgpSysNotification, lgpSysAudibleAlarm=lgpSysAudibleAlarm, lgpSysDeviceComponentWellknown=lgpSysDeviceComponentWellknown, lgpSysDeviceComponentEntry=lgpSysDeviceComponentEntry, lgpSysDeviceParallelCabinet=lgpSysDeviceParallelCabinet, lgpSysMaintenanceCapacity=lgpSysMaintenanceCapacity, lgpSysSelfTestResult=lgpSysSelfTestResult, PYSNMP_MODULE_ID=liebertSystemModule, lgpSysMaintenanceMonth=lgpSysMaintenanceMonth, lgpSysMaintenance=lgpSysMaintenance, lgpSysDeviceComponentDescr=lgpSysDeviceComponentDescr, lgpSysStatus=lgpSysStatus, lgpSysMaintenanceYear=lgpSysMaintenanceYear, lgpSysSettings=lgpSysSettings, lgpSysControlOperationOnOff=lgpSysControlOperationOnOff, lgpSysState=lgpSysState, lgpSysControl=lgpSysControl, lgpSysDeviceComponentTable=lgpSysDeviceComponentTable, lgpSysStatistics=lgpSysStatistics, lgpSysDeviceComponentGroup=lgpSysDeviceComponentGroup, lgpSysTime=lgpSysTime, lgpSysDeviceComponentSerialNum=lgpSysDeviceComponentSerialNum, lgpSysEventDescription=lgpSysEventDescription, lgpSysEventNotifications=lgpSysEventNotifications, lgpSysNormal=lgpSysNormal)
