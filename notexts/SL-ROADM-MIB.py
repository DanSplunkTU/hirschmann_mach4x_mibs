#
# PySNMP MIB module SL-ROADM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-ROADM-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:15:38 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
slService, = mibBuilder.importSymbols("SL-NE-MIB", "slService")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Unsigned32, MibIdentifier, TimeTicks, ObjectIdentity, Integer32, Gauge32, Counter64, NotificationType, Counter32, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Unsigned32", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Integer32", "Gauge32", "Counter64", "NotificationType", "Counter32", "Bits", "ModuleIdentity")
DateAndTime, TextualConvention, TruthValue, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "TruthValue", "DisplayString")
slROADM = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16))
if mibBuilder.loadTexts: slROADM.setLastUpdated('0508171200Z')
if mibBuilder.loadTexts: slROADM.setOrganization('PacketLight Networks Ltd.')
slROADMConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1))
slROADMPm = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 2))
slROADMTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 3))
class ROCHProvisioningType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("exp", 2), ("add", 3))

slWSSConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1), )
if mibBuilder.loadTexts: slWSSConfigTable.setStatus('current')
slWSSConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1), ).setIndexNames((0, "SL-ROADM-MIB", "slWSSConfigLineIndex"))
if mibBuilder.loadTexts: slWSSConfigEntry.setStatus('current')
slWSSConfigLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigLineIndex.setStatus('current')
slWSSConfigOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigOperStatus.setStatus('current')
slWSSConfigSwitchTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigSwitchTemp.setStatus('current')
slWSSConfigBoardTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigBoardTemp.setStatus('current')
slWSSConfigCaseTemp = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigCaseTemp.setStatus('current')
slWSSConfigUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigUptime.setStatus('current')
slWSSConfigComFirstWl = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slWSSConfigComFirstWl.setStatus('current')
slWSSConfigComChCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slWSSConfigComChCount.setStatus('current')
slWSSConfigPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigPowerLevel.setStatus('current')
slWSSConfigAttenLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 1, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slWSSConfigAttenLevel.setStatus('current')
slROCHConfigTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2), )
if mibBuilder.loadTexts: slROCHConfigTable.setStatus('current')
slROCHConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1), ).setIndexNames((0, "SL-ROADM-MIB", "slROCHConfigLineIndex"))
if mibBuilder.loadTexts: slROCHConfigEntry.setStatus('current')
slROCHConfigLineIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slROCHConfigLineIndex.setStatus('current')
slROCHConfigProvisioning = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 2), ROCHProvisioningType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigProvisioning.setStatus('current')
slROCHConfigInPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slROCHConfigInPowerLevel.setStatus('current')
slROCHConfigOutPowerLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slROCHConfigOutPowerLevel.setStatus('current')
slROCHConfigChannelDetect = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slROCHConfigChannelDetect.setStatus('current')
slROCHConfigChPowerFailHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerFailHighThresh.setStatus('current')
slROCHConfigChPowerFailLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerFailLowThresh.setStatus('current')
slROCHConfigChPowerDegHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerDegHighThresh.setStatus('current')
slROCHConfigChPowerDegLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerDegLowThresh.setStatus('current')
slROCHConfigChPowerHystHighThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerHystHighThresh.setStatus('current')
slROCHConfigChPowerHystLowThresh = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 1, 16, 1, 2, 1, 11), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slROCHConfigChPowerHystLowThresh.setStatus('current')
mibBuilder.exportSymbols("SL-ROADM-MIB", slWSSConfigOperStatus=slWSSConfigOperStatus, slROCHConfigChPowerDegLowThresh=slROCHConfigChPowerDegLowThresh, ROCHProvisioningType=ROCHProvisioningType, slWSSConfigCaseTemp=slWSSConfigCaseTemp, slROCHConfigOutPowerLevel=slROCHConfigOutPowerLevel, slROADMTraps=slROADMTraps, slROCHConfigLineIndex=slROCHConfigLineIndex, slWSSConfigAttenLevel=slWSSConfigAttenLevel, slROCHConfigTable=slROCHConfigTable, slROCHConfigChPowerHystLowThresh=slROCHConfigChPowerHystLowThresh, slROCHConfigProvisioning=slROCHConfigProvisioning, slROCHConfigChPowerFailLowThresh=slROCHConfigChPowerFailLowThresh, slROCHConfigChPowerDegHighThresh=slROCHConfigChPowerDegHighThresh, slWSSConfigUptime=slWSSConfigUptime, slROADMPm=slROADMPm, slROCHConfigChPowerHystHighThresh=slROCHConfigChPowerHystHighThresh, slROCHConfigInPowerLevel=slROCHConfigInPowerLevel, slWSSConfigComFirstWl=slWSSConfigComFirstWl, PYSNMP_MODULE_ID=slROADM, slWSSConfigTable=slWSSConfigTable, slWSSConfigSwitchTemp=slWSSConfigSwitchTemp, slWSSConfigBoardTemp=slWSSConfigBoardTemp, slROADMConfig=slROADMConfig, slROCHConfigChPowerFailHighThresh=slROCHConfigChPowerFailHighThresh, slWSSConfigComChCount=slWSSConfigComChCount, slROCHConfigChannelDetect=slROCHConfigChannelDetect, slWSSConfigPowerLevel=slWSSConfigPowerLevel, slWSSConfigLineIndex=slWSSConfigLineIndex, slROADM=slROADM, slWSSConfigEntry=slWSSConfigEntry, slROCHConfigEntry=slROCHConfigEntry)
