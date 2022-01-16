#
# PySNMP MIB module DPS-MIB-V38 (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/dpstelecom/DPS-MIB-V38
# Produced by pysmi-1.1.8 at Sun Jan 16 00:35:42 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("RFC1212-MIB", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
sysLocation, sysDescr = mibBuilder.importSymbols("SNMPv2-MIB", "sysLocation", "sysDescr")
Gauge32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, Bits, Counter64, Counter32, ObjectIdentity, NotificationType, MibIdentifier, Unsigned32, TimeTicks, enterprises, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "Bits", "Counter64", "Counter32", "ObjectIdentity", "NotificationType", "MibIdentifier", "Unsigned32", "TimeTicks", "enterprises", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
dpsInc = MibIdentifier((1, 3, 6, 1, 4, 1, 2682))
dpsAlarmControl = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1))
tmonXM = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 1))
tmonIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 1, 1))
tmonIdentManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonIdentManufacturer.setStatus('mandatory')
if mibBuilder.loadTexts: tmonIdentManufacturer.setDescription('The TMON/XM Unit manufacturer.')
tmonIdentModel = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonIdentModel.setStatus('mandatory')
if mibBuilder.loadTexts: tmonIdentModel.setDescription('The TMON/XM model designation.')
tmonIdentSoftwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonIdentSoftwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: tmonIdentSoftwareVersion.setDescription('The TMON/XM SNMP Agent software version.')
tmonAlarmTable = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2), )
if mibBuilder.loadTexts: tmonAlarmTable.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAlarmTable.setDescription('A table of TMon Alarm-specific information.')
tmonAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1), ).setIndexNames((0, "DPS-MIB-V38", "tmonAIndex"))
if mibBuilder.loadTexts: tmonAlarmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAlarmEntry.setDescription('Information about a particular TMon alarm.')
tmonAIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAIndex.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAIndex.setDescription('Tmon alarm table index (1..NumberOfAlarms).')
tmonASite = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonASite.setStatus('mandatory')
if mibBuilder.loadTexts: tmonASite.setDescription('The site of the alarm (i.e. Atlanta Hub, Sub-Station H32).')
tmonADesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonADesc.setStatus('mandatory')
if mibBuilder.loadTexts: tmonADesc.setDescription('A user-defined text string associated with the alarm \n\t\t\t\t\t (i.e. South Door, Generator, Power Grid 1).')
tmonAState = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAState.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAState.setDescription('The current alarm state.')
tmonASeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonASeverity.setStatus('mandatory')
if mibBuilder.loadTexts: tmonASeverity.setDescription('The severity of the last alarm event.')
tmonAChgDate = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAChgDate.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAChgDate.setDescription('The date (mm/dd/yy) of the last alarm event.')
tmonAChgTime = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAChgTime.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAChgTime.setDescription('The time (hh:mm:ss) of the last alarm event.')
tmonAAuxDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAAuxDesc.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAAuxDesc.setDescription('An auxiliary user-defined text string associated with the\n\t\t\t\t\t alarm (i.e. This remote needs servicing).')
tmonADispDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonADispDesc.setStatus('mandatory')
if mibBuilder.loadTexts: tmonADispDesc.setDescription('A description of the display on which this point appears.')
tmonAPntType = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAPntType.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAPntType.setDescription('Type of this point.')
tmonAPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAPort.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAPort.setDescription('Port on which this point is reported.')
tmonAAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAAddress.setDescription('Address of unit reporting this point.')
tmonADisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonADisplay.setStatus('mandatory')
if mibBuilder.loadTexts: tmonADisplay.setDescription('Display on which this point appears.')
tmonAPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAPoint.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAPoint.setDescription('Index into display of this point.')
tmonAIPAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonAIPAddr.setStatus('mandatory')
if mibBuilder.loadTexts: tmonAIPAddr.setDescription('The IP Address of the device on which this point appears.')
tmonADevDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 1, 2, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonADevDesc.setStatus('mandatory')
if mibBuilder.loadTexts: tmonADevDesc.setDescription('A description of the device on which this point appears.')
tmonCommandGrid = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3))
tmonCPType = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCPType.setStatus('mandatory')
if mibBuilder.loadTexts: tmonCPType.setDescription('Tmon point type.')
tmonCPort = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCPort.setStatus('mandatory')
if mibBuilder.loadTexts: tmonCPort.setDescription('Tmon port number.')
tmonCAddress = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCAddress.setStatus('mandatory')
if mibBuilder.loadTexts: tmonCAddress.setDescription('Tmon_port address number.')
tmonCDisplay = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCDisplay.setStatus('mandatory')
if mibBuilder.loadTexts: tmonCDisplay.setDescription('Tmon_port_address display number.')
tmonCPoint = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCPoint.setStatus('mandatory')
if mibBuilder.loadTexts: tmonCPoint.setDescription('Tmon_port_display point number (1-64).')
tmonCEvent = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCEvent.setStatus('mandatory')
if mibBuilder.loadTexts: tmonCEvent.setDescription('Tmon event ID.')
tmonCAction = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 17, 18, 19))).clone(namedValues=NamedValues(("latch", 1), ("release", 2), ("momentary", 3), ("ack", 17), ("tag", 18), ("untag", 19)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCAction.setStatus('mandatory')
if mibBuilder.loadTexts: tmonCAction.setDescription('Requested command action (tmonXM will ignore if invalid).')
tmonCAuxText = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 8), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: tmonCAuxText.setStatus('mandatory')
if mibBuilder.loadTexts: tmonCAuxText.setDescription('An auxiliary user-defined text string associated with the\n\t\t\t\t\t command (i.e. User_initials).')
tmonCResult = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 1, 3, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("success", 1), ("failure", 2), ("pending", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: tmonCResult.setStatus('mandatory')
if mibBuilder.loadTexts: tmonCResult.setDescription('Command result.')
dpsRTU = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 2))
dpsRTUIdent = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1))
dpsRTUManufacturer = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUManufacturer.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUManufacturer.setDescription('The Remote Telemetry Unit manufacturer.')
dpsRTUModel = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUModel.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUModel.setDescription('The RTU model designation.')
dpsRTUFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUFirmwareVersion.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUFirmwareVersion.setDescription('The RTU firmware version.')
dpsRTUDateTime = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUDateTime.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUDateTime.setDescription('The RTU system date and time.')
dpsRTUSyncReq = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("sync", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUSyncReq.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUSyncReq.setDescription('Caution: SETting this object initiates traps for all\n\t\t\t\t\t standing alarms.')
dpsRTUDisplayGrid = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2), )
if mibBuilder.loadTexts: dpsRTUDisplayGrid.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUDisplayGrid.setDescription('Holds information on displays managed by the RTU.')
dpsRTUDisplayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1), ).setIndexNames((0, "DPS-MIB-V38", "dpsRTUPort"), (0, "DPS-MIB-V38", "dpsRTUAddress"), (0, "DPS-MIB-V38", "dpsRTUDisplay"))
if mibBuilder.loadTexts: dpsRTUDisplayEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUDisplayEntry.setDescription('Information about a particular RTU display.')
dpsRTUPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUPort.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUPort.setDescription('RTU port number.')
dpsRTUAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUAddress.setDescription('RTU_port address number.')
dpsRTUDisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUDisplay.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUDisplay.setDescription('RTU_port_address display number.')
dpsRTUDispDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUDispDesc.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUDispDesc.setDescription('A description of the associated display.')
dpsRTUPntMap = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 2, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUPntMap.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUPntMap.setDescription('A map of the points appearing in this display.')
dpsRTUControlGrid = MibIdentifier((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3))
dpsRTUCPort = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUCPort.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUCPort.setDescription('RTU port number.')
dpsRTUCAddress = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUCAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUCAddress.setDescription('RTU_port address number.')
dpsRTUCDisplay = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUCDisplay.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUCDisplay.setDescription('RTU_port_address display number.')
dpsRTUCPoint = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUCPoint.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUCPoint.setDescription('RTU_port_display point number (1-64).')
dpsRTUCAction = MibScalar((1, 3, 6, 1, 4, 1, 2682, 1, 2, 3, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("latch", 1), ("release", 2), ("momentary", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUCAction.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUCAction.setDescription('Requested action on point (RTU will ignore if invalid).')
dpsRTUAlarmGrid = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5), )
if mibBuilder.loadTexts: dpsRTUAlarmGrid.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUAlarmGrid.setDescription('Holds individual alarm point information.')
dpsRTUAlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1), ).setIndexNames((0, "DPS-MIB-V38", "dpsRTUAPort"), (0, "DPS-MIB-V38", "dpsRTUAAddress"), (0, "DPS-MIB-V38", "dpsRTUADisplay"), (0, "DPS-MIB-V38", "dpsRTUAPoint"))
if mibBuilder.loadTexts: dpsRTUAlarmEntry.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUAlarmEntry.setDescription('Detailed information about a particular RTU display.')
dpsRTUAPort = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUAPort.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUAPort.setDescription('RTU port number.')
dpsRTUAAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUAAddress.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUAAddress.setDescription('RTU_port address number.')
dpsRTUADisplay = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUADisplay.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUADisplay.setDescription('RTU_port_address display number.')
dpsRTUAPoint = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUAPoint.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUAPoint.setDescription('RTU_port_address_display point number.')
dpsRTUAPntDesc = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 5), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: dpsRTUAPntDesc.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUAPntDesc.setDescription('A description of this point.')
dpsRTUAState = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: dpsRTUAState.setStatus('mandatory')
if mibBuilder.loadTexts: dpsRTUAState.setDescription('The current state of this point.')
analogChannels = MibTable((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6), )
if mibBuilder.loadTexts: analogChannels.setStatus('mandatory')
if mibBuilder.loadTexts: analogChannels.setDescription('Holds information on analog channels')
channelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1), ).setIndexNames((0, "DPS-MIB-V38", "channelNumber"))
if mibBuilder.loadTexts: channelEntry.setStatus('mandatory')
if mibBuilder.loadTexts: channelEntry.setDescription('Information about a particular channel')
channelNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: channelNumber.setStatus('mandatory')
if mibBuilder.loadTexts: channelNumber.setDescription('Input channel number')
enabled = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: enabled.setStatus('mandatory')
if mibBuilder.loadTexts: enabled.setDescription('Enable status of channel')
description = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: description.setStatus('mandatory')
if mibBuilder.loadTexts: description.setDescription('The user defined description of the channel')
value = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: value.setStatus('mandatory')
if mibBuilder.loadTexts: value.setDescription('The current value of the channel')
thresholds = MibTableColumn((1, 3, 6, 1, 4, 1, 2682, 1, 2, 6, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("noAlarms", 0), ("minorUnder", 1), ("minorOver", 2), ("majorUnder", 3), ("majorOver", 4), ("notDetected", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: thresholds.setStatus('mandatory')
if mibBuilder.loadTexts: thresholds.setDescription('Highest threshold level crossed, if MJ, MN is assumed')
tmonCRalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,10)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
if mibBuilder.loadTexts: tmonCRalarmSet.setDescription('Generated when a critical alarm is set.')
tmonCRalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,11)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
if mibBuilder.loadTexts: tmonCRalarmClr.setDescription('Generated when a critical alarm clears.')
tmonMJalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,12)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
if mibBuilder.loadTexts: tmonMJalarmSet.setDescription('Generated when a major alarm is set.')
tmonMJalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,13)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
if mibBuilder.loadTexts: tmonMJalarmClr.setDescription('Generated when a major alarm clears.')
tmonMNalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,14)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
if mibBuilder.loadTexts: tmonMNalarmSet.setDescription('Generated when a minor alarm is set.')
tmonMNalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,15)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
if mibBuilder.loadTexts: tmonMNalarmClr.setDescription('Generated when a minor alarm clears.')
tmonSTalarmSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,16)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
if mibBuilder.loadTexts: tmonSTalarmSet.setDescription('Generated when a status alarm is set.')
tmonSTalarmClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 1) + (0,17)).setObjects(("DPS-MIB-V38", "tmonASite"), ("DPS-MIB-V38", "tmonADesc"), ("DPS-MIB-V38", "tmonAState"), ("DPS-MIB-V38", "tmonASeverity"), ("DPS-MIB-V38", "tmonAChgDate"), ("DPS-MIB-V38", "tmonAChgTime"), ("DPS-MIB-V38", "tmonAAuxDesc"), ("DPS-MIB-V38", "tmonADispDesc"), ("DPS-MIB-V38", "tmonAPntType"), ("DPS-MIB-V38", "tmonAPort"), ("DPS-MIB-V38", "tmonAAddress"), ("DPS-MIB-V38", "tmonADisplay"), ("DPS-MIB-V38", "tmonAPoint"), ("DPS-MIB-V38", "tmonCEvent"), ("DPS-MIB-V38", "tmonAIPAddr"), ("DPS-MIB-V38", "tmonADevDesc"))
if mibBuilder.loadTexts: tmonSTalarmClr.setDescription('Generated when a status alarm clears.')
dpsRTUPointSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,20)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"), ("DPS-MIB-V38", "dpsRTUAPort"), ("DPS-MIB-V38", "dpsRTUAAddress"), ("DPS-MIB-V38", "dpsRTUADisplay"), ("DPS-MIB-V38", "dpsRTUAPoint"), ("DPS-MIB-V38", "dpsRTUAPntDesc"), ("DPS-MIB-V38", "dpsRTUAState"))
if mibBuilder.loadTexts: dpsRTUPointSet.setDescription('Generated when a point is set.')
dpsRTUPointClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,21)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"), ("DPS-MIB-V38", "dpsRTUAPort"), ("DPS-MIB-V38", "dpsRTUCAddress"), ("DPS-MIB-V38", "dpsRTUADisplay"), ("DPS-MIB-V38", "dpsRTUAPoint"), ("DPS-MIB-V38", "dpsRTUAPntDesc"), ("DPS-MIB-V38", "dpsRTUAState"))
if mibBuilder.loadTexts: dpsRTUPointClr.setDescription('Generated when a point clears.')
dpsRTUsumPSet = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,101)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"))
if mibBuilder.loadTexts: dpsRTUsumPSet.setDescription('Generated when any point is set.')
dpsRTUsumPClr = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,102)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"))
if mibBuilder.loadTexts: dpsRTUsumPClr.setDescription('Generated when all points clear.')
dpsRTUcomFailed = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,103)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"))
if mibBuilder.loadTexts: dpsRTUcomFailed.setDescription('Generated when polled unit fails to respond.')
dpsRTUcomRestored = NotificationType((1, 3, 6, 1, 4, 1, 2682, 1, 2) + (0,104)).setObjects(("SNMPv2-MIB", "sysDescr"), ("SNMPv2-MIB", "sysLocation"), ("DPS-MIB-V38", "dpsRTUDateTime"))
if mibBuilder.loadTexts: dpsRTUcomRestored.setDescription('Generated when failed unit resumes responding.')
mibBuilder.exportSymbols("DPS-MIB-V38", tmonADispDesc=tmonADispDesc, tmonAlarmEntry=tmonAlarmEntry, enabled=enabled, tmonCPort=tmonCPort, tmonIdentSoftwareVersion=tmonIdentSoftwareVersion, dpsRTUDisplayEntry=dpsRTUDisplayEntry, dpsRTUIdent=dpsRTUIdent, dpsRTUAPoint=dpsRTUAPoint, tmonAAddress=tmonAAddress, tmonAlarmTable=tmonAlarmTable, dpsRTUPntMap=dpsRTUPntMap, tmonCRalarmSet=tmonCRalarmSet, dpsRTUDisplayGrid=dpsRTUDisplayGrid, analogChannels=analogChannels, tmonSTalarmClr=tmonSTalarmClr, dpsRTUControlGrid=dpsRTUControlGrid, tmonMNalarmSet=tmonMNalarmSet, tmonAState=tmonAState, dpsRTUCAddress=dpsRTUCAddress, dpsRTUCPort=dpsRTUCPort, tmonAChgDate=tmonAChgDate, dpsRTUDisplay=dpsRTUDisplay, dpsRTUsumPClr=dpsRTUsumPClr, tmonAPoint=tmonAPoint, channelEntry=channelEntry, dpsRTUPointClr=dpsRTUPointClr, tmonIdent=tmonIdent, tmonCResult=tmonCResult, dpsInc=dpsInc, dpsRTUADisplay=dpsRTUADisplay, tmonAPntType=tmonAPntType, dpsRTUCPoint=dpsRTUCPoint, dpsRTUAPntDesc=dpsRTUAPntDesc, dpsRTUAState=dpsRTUAState, tmonAPort=tmonAPort, tmonADesc=tmonADesc, channelNumber=channelNumber, dpsRTUsumPSet=dpsRTUsumPSet, dpsRTUFirmwareVersion=dpsRTUFirmwareVersion, dpsRTUManufacturer=dpsRTUManufacturer, value=value, dpsAlarmControl=dpsAlarmControl, tmonAIndex=tmonAIndex, tmonCDisplay=tmonCDisplay, tmonADevDesc=tmonADevDesc, dpsRTU=dpsRTU, dpsRTUCDisplay=dpsRTUCDisplay, tmonCAuxText=tmonCAuxText, tmonAChgTime=tmonAChgTime, dpsRTUAlarmEntry=dpsRTUAlarmEntry, dpsRTUAPort=dpsRTUAPort, dpsRTUcomFailed=dpsRTUcomFailed, tmonCPoint=tmonCPoint, tmonIdentModel=tmonIdentModel, tmonCRalarmClr=tmonCRalarmClr, tmonMJalarmSet=tmonMJalarmSet, tmonCPType=tmonCPType, tmonCAction=tmonCAction, dpsRTUcomRestored=dpsRTUcomRestored, tmonCEvent=tmonCEvent, tmonXM=tmonXM, tmonADisplay=tmonADisplay, thresholds=thresholds, tmonAIPAddr=tmonAIPAddr, dpsRTUCAction=dpsRTUCAction, dpsRTUPort=dpsRTUPort, dpsRTUAddress=dpsRTUAddress, tmonASite=tmonASite, dpsRTUModel=dpsRTUModel, tmonIdentManufacturer=tmonIdentManufacturer, dpsRTUAlarmGrid=dpsRTUAlarmGrid, dpsRTUDispDesc=dpsRTUDispDesc, tmonMJalarmClr=tmonMJalarmClr, tmonCAddress=tmonCAddress, dpsRTUAAddress=dpsRTUAAddress, dpsRTUDateTime=dpsRTUDateTime, dpsRTUPointSet=dpsRTUPointSet, tmonSTalarmSet=tmonSTalarmSet, dpsRTUSyncReq=dpsRTUSyncReq, tmonAAuxDesc=tmonAAuxDesc, tmonCommandGrid=tmonCommandGrid, tmonMNalarmClr=tmonMNalarmClr, tmonASeverity=tmonASeverity, description=description)
