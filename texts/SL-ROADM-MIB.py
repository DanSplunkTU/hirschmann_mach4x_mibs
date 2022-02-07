#
# PySNMP MIB module SL-ROADM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-ROADM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:17:48 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slService, = mibBuilder.importSymbols("SL-NE-MIB", "slService")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, MibIdentifier, TimeTicks, ObjectIdentity, Unsigned32, IpAddress, Counter32, Gauge32, Counter64, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "Gauge32", "Counter64", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType")
DateAndTime, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TruthValue", "TextualConvention")
slROADM = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16))
if mibBuilder.loadTexts: slROADM.setLastUpdated('0508171200Z')
if mibBuilder.loadTexts: slROADM.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slROADM.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slROADM.setDescription('This MIB module describes the ROADM')
slROADMConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1))
slROADMPm = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 2))
slROADMTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 3))
class ROCHProvisioningType(TextualConvention, Integer32):
    description = 'The channel provisioning type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("exp", 2), ("add", 3))

slWSSConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1), )
if mibBuilder.loadTexts: slWSSConfigTable.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigTable.setDescription('The ROADM Configuration table.')
slWSSConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1), ).setIndexNames((0, "SL-ROADM-MIB", "slWSSConfigLineIndex"))
if mibBuilder.loadTexts: slWSSConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigEntry.setDescription('An entry in the WSS Configuration table.')
slWSSConfigLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigLineIndex.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigLineIndex.setDescription('Only one entry in the table.\n\t\t Thus this is a dummy ifIndex that equals to 1.')
slWSSConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigOperStatus.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigOperStatus.setDescription('The WSS operational status. 0 - DOWN, 1 - UP.')
slWSSConfigSwitchTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigSwitchTemp.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigSwitchTemp.setDescription('The switch temperature in 0.1 celsius')
slWSSConfigBoardTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigBoardTemp.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigBoardTemp.setDescription('The board temperature in 0.1 celsius')
slWSSConfigCaseTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigCaseTemp.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigCaseTemp.setDescription('The case temperature in 0.1 celsius')
slWSSConfigUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigUptime.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigUptime.setDescription('The case temperature in 0.1 celsius')
slWSSConfigComFirstWl = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slWSSConfigComFirstWl.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigComFirstWl.setDescription('The first DWDM ITU G.694.1 channel of the Waveplan.\n    \t Specified in 3.125GHz units')
slWSSConfigComChCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slWSSConfigComChCount.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigComChCount.setDescription('The overall count of channels in the Waveplan.\n    \t The channels are ordered in increasing frequency (decreasing wavelength).')
slWSSConfigPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigPowerLevel.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigPowerLevel.setDescription('The received Destination Access Point Identifier.')
slWSSConfigAttenLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigAttenLevel.setStatus('current')
if mibBuilder.loadTexts: slWSSConfigAttenLevel.setDescription('The received Source Access Point Identifier.')
slROCHConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2), )
if mibBuilder.loadTexts: slROCHConfigTable.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigTable.setDescription('The ROADM Channel Configuration table.')
slROCHConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1), ).setIndexNames((0, "SL-ROADM-MIB", "slROCHConfigLineIndex"))
if mibBuilder.loadTexts: slROCHConfigEntry.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigEntry.setDescription('An entry in the ROADM Configuration table.')
slROCHConfigLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slROCHConfigLineIndex.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigLineIndex.setDescription('The ifIndex of the channel.\n\t\tThe channels use the paths 1-48 with the port number of the COM')
slROCHConfigProvisioning = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 2), ROCHProvisioningType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigProvisioning.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigProvisioning.setDescription('The channel provisioning')
slROCHConfigInPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slROCHConfigInPowerLevel.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigInPowerLevel.setDescription('The Power Level of the channel equal to Out Power Level + Attenuation')
slROCHConfigOutPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slROCHConfigOutPowerLevel.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigOutPowerLevel.setDescription('The Output Power Level of the channel')
slROCHConfigChannelDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slROCHConfigChannelDetect.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigChannelDetect.setDescription('Channel detect indication. 0 - not detected, 1 - channel is detected')
slROCHConfigChPowerFailHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerFailHighThresh.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigChPowerFailHighThresh.setDescription('The threshold for channel High Power Failure.\n    \t Setting this value applies to all channels.')
slROCHConfigChPowerFailLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerFailLowThresh.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigChPowerFailLowThresh.setDescription('The threshold for channel Low Power Failure.\n    \t Setting this value applies to all channels.')
slROCHConfigChPowerDegHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerDegHighThresh.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigChPowerDegHighThresh.setDescription('The threshold for channel High Power Degrade.\n    \t Setting this value applies to all channels.')
slROCHConfigChPowerDegLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerDegLowThresh.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigChPowerDegLowThresh.setDescription('The threshold for channel Low Power Degrade.\n    \t Setting this value applies to all channels.')
slROCHConfigChPowerHystHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerHystHighThresh.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigChPowerHystHighThresh.setDescription('The threshold for channel High Power Hysteresis.\n    \t Setting this value applies to all channels.')
slROCHConfigChPowerHystLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerHystLowThresh.setStatus('current')
if mibBuilder.loadTexts: slROCHConfigChPowerHystLowThresh.setDescription('The threshold for channel Low Power Hysteresis.\n    \t Setting this value applies to all channels.')
mibBuilder.exportSymbols("SL-ROADM-MIB", slROADMPm=slROADMPm, slWSSConfigPowerLevel=slWSSConfigPowerLevel, slROCHConfigTable=slROCHConfigTable, slROADMConfig=slROADMConfig, slROCHConfigInPowerLevel=slROCHConfigInPowerLevel, slROCHConfigChPowerDegLowThresh=slROCHConfigChPowerDegLowThresh, slROCHConfigLineIndex=slROCHConfigLineIndex, slWSSConfigComFirstWl=slWSSConfigComFirstWl, slROCHConfigEntry=slROCHConfigEntry, slWSSConfigEntry=slWSSConfigEntry, slWSSConfigComChCount=slWSSConfigComChCount, slROCHConfigChPowerHystHighThresh=slROCHConfigChPowerHystHighThresh, slROCHConfigOutPowerLevel=slROCHConfigOutPowerLevel, slWSSConfigAttenLevel=slWSSConfigAttenLevel, slROCHConfigChPowerFailLowThresh=slROCHConfigChPowerFailLowThresh, slROCHConfigProvisioning=slROCHConfigProvisioning, slWSSConfigUptime=slWSSConfigUptime, slROCHConfigChPowerHystLowThresh=slROCHConfigChPowerHystLowThresh, PYSNMP_MODULE_ID=slROADM, slROCHConfigChPowerFailHighThresh=slROCHConfigChPowerFailHighThresh, slROADM=slROADM, slWSSConfigSwitchTemp=slWSSConfigSwitchTemp, slWSSConfigTable=slWSSConfigTable, slROADMTraps=slROADMTraps, slWSSConfigLineIndex=slWSSConfigLineIndex, slWSSConfigOperStatus=slWSSConfigOperStatus, slROCHConfigChannelDetect=slROCHConfigChannelDetect, slWSSConfigCaseTemp=slWSSConfigCaseTemp, ROCHProvisioningType=ROCHProvisioningType, slROCHConfigChPowerDegHighThresh=slROCHConfigChPowerDegHighThresh, slWSSConfigBoardTemp=slWSSConfigBoardTemp)
