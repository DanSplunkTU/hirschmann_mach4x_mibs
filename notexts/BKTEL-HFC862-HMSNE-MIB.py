#
# PySNMP MIB module BKTEL-HFC862-HMSNE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bktel/BKTEL-HFC862-HMSNE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:53:04 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ne, NESlotValue, PerceivedSeverityValue, TruthValue, DisplayString = mibBuilder.importSymbols("BKTEL-HFC862-BASE-MIB", "ne", "NESlotValue", "PerceivedSeverityValue", "TruthValue", "DisplayString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, NotificationType, iso, ModuleIdentity, Counter64, NotificationType, TimeTicks, Bits, Gauge32, Counter32, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "NotificationType", "iso", "ModuleIdentity", "Counter64", "NotificationType", "TimeTicks", "Bits", "Gauge32", "Counter32", "Integer32", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
neCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1))
neType = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neType.setStatus('mandatory')
neDescription = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neDescription.setStatus('mandatory')
neLocationStreet = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neLocationStreet.setStatus('mandatory')
neLocationCity = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neLocationCity.setStatus('mandatory')
neObsolete_UsingAPS = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_UsingAPS.setStatus('obsolete')
neObsolete_APSMode = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neObsolete_APSMode.setStatus('obsolete')
neObsolete_CommonSubrackWidth = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_CommonSubrackWidth.setStatus('obsolete')
neObsolete_CommonSubrackNumber = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_CommonSubrackNumber.setStatus('obsolete')
neObsolete_NumberModul = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 61))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_NumberModul.setStatus('obsolete')
neObsolete_UsingRevertiveMode = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_UsingRevertiveMode.setStatus('obsolete')
neObsolete_RevertiveMode = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neObsolete_RevertiveMode.setStatus('obsolete')
neObsolete_InitPhase = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neObsolete_InitPhase.setStatus('obsolete')
neObsolete_PredecessorRedundantPath = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 14), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neObsolete_PredecessorRedundantPath.setStatus('obsolete')
neObsolete_PredecessorNominalPath = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 15), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neObsolete_PredecessorNominalPath.setStatus('obsolete')
neModuleTable = MibTable((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16), )
if mibBuilder.loadTexts: neModuleTable.setStatus('mandatory')
neModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1), ).setIndexNames((0, "BKTEL-HFC862-HMSNE-MIB", "neModuleNESlot"))
if mibBuilder.loadTexts: neModuleEntry.setStatus('mandatory')
neModuleNESlot = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 1), NESlotValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleNESlot.setStatus('mandatory')
neModuleSubrack = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleSubrack.setStatus('mandatory')
neModuleModelName = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleModelName.setStatus('mandatory')
neModuleMibLink = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 4), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleMibLink.setStatus('mandatory')
neModuleSubrackSlot = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleSubrackSlot.setStatus('mandatory')
neModuleSlotUnitsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleSlotUnitsUsed.setStatus('mandatory')
neModuleSlotRackDetection = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("notSupported", 1), ("supported", 2), ("detectionError", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleSlotRackDetection.setStatus('mandatory')
neModuleHousingType = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("housingUnknownOrDefault", 1), ("housingBk", 2), ("housing2G6", 3), ("housing19inch", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleHousingType.setStatus('mandatory')
neModuleFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleFirmwareVersion.setStatus('mandatory')
neModuleHardwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleHardwareVersion.setStatus('mandatory')
neModuleDateOfProduction = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleDateOfProduction.setStatus('mandatory')
neModuleSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 12), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleSerialNumber.setStatus('mandatory')
neModuleArticleNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleArticleNumber.setStatus('mandatory')
neModuleCustomerCode = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neModuleCustomerCode.setStatus('mandatory')
neModuleAliasName = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 15), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neModuleAliasName.setStatus('mandatory')
neModuleUserdata = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 16), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neModuleUserdata.setStatus('mandatory')
neModuleReset = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 17), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neModuleReset.setStatus('mandatory')
neModuleLedBlink = MibTableColumn((1, 3, 6, 1, 4, 1, 7501, 1, 1, 1, 16, 1, 18), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neModuleLedBlink.setStatus('mandatory')
neStates = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2))
neStatesObsolete_TrapDisable = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 1), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_TrapDisable.setStatus('obsolete')
neStatesObsolete_TerminalConnected = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 2), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_TerminalConnected.setStatus('obsolete')
neStatesObsolete_Isolated = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 4), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_Isolated.setStatus('obsolete')
neStatesObsolete_ResetModullist = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 5), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_ResetModullist.setStatus('obsolete')
neStatesObsolete_Redundant = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 6), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_Redundant.setStatus('obsolete')
neStatesObsolete_ActivateRedundantPath = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 7), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_ActivateRedundantPath.setStatus('obsolete')
neStatesObsolete_AutoOff = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 2, 8), PerceivedSeverityValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: neStatesObsolete_AutoOff.setStatus('obsolete')
neConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3))
neConfigObsolete_NEtype = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neConfigObsolete_NEtype.setStatus('obsolete')
neConfigObsolete_IPaddress = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neConfigObsolete_IPaddress.setStatus('obsolete')
neConfigObsolete_Alarmdelay = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 60))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neConfigObsolete_Alarmdelay.setStatus('obsolete')
neConfigDeprecated_MinTrapInterval = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 10))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neConfigDeprecated_MinTrapInterval.setStatus('optional')
neConfigDeprecated_MaxTrapLifetime = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 3, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(30, 300))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neConfigDeprecated_MaxTrapLifetime.setStatus('optional')
neControl = MibIdentifier((1, 3, 6, 1, 4, 1, 7501, 1, 1, 4))
neControlTrapDisable = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 4, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neControlTrapDisable.setStatus('mandatory')
neControlResetModullist = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 4, 2), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neControlResetModullist.setStatus('mandatory')
neControlObsolete_SetDefaultAPS = MibScalar((1, 3, 6, 1, 4, 1, 7501, 1, 1, 4, 3), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: neControlObsolete_SetDefaultAPS.setStatus('obsolete')
neSynchronizeEvent = NotificationType((1, 3, 6, 1, 4, 1, 7501, 1, 1) + (0,1))
mibBuilder.exportSymbols("BKTEL-HFC862-HMSNE-MIB", neSynchronizeEvent=neSynchronizeEvent, neLocationCity=neLocationCity, neModuleReset=neModuleReset, neStatesObsolete_ResetModullist=neStatesObsolete_ResetModullist, neModuleSlotRackDetection=neModuleSlotRackDetection, neModuleLedBlink=neModuleLedBlink, neDescription=neDescription, neStatesObsolete_TrapDisable=neStatesObsolete_TrapDisable, neStatesObsolete_Isolated=neStatesObsolete_Isolated, neModuleHousingType=neModuleHousingType, neModuleAliasName=neModuleAliasName, neControlResetModullist=neControlResetModullist, neModuleFirmwareVersion=neModuleFirmwareVersion, neConfigDeprecated_MinTrapInterval=neConfigDeprecated_MinTrapInterval, neCommon=neCommon, neConfigDeprecated_MaxTrapLifetime=neConfigDeprecated_MaxTrapLifetime, neObsolete_CommonSubrackNumber=neObsolete_CommonSubrackNumber, neStatesObsolete_AutoOff=neStatesObsolete_AutoOff, neObsolete_UsingAPS=neObsolete_UsingAPS, neObsolete_CommonSubrackWidth=neObsolete_CommonSubrackWidth, neObsolete_UsingRevertiveMode=neObsolete_UsingRevertiveMode, neConfigObsolete_IPaddress=neConfigObsolete_IPaddress, neObsolete_RevertiveMode=neObsolete_RevertiveMode, neType=neType, neModuleSerialNumber=neModuleSerialNumber, neObsolete_PredecessorRedundantPath=neObsolete_PredecessorRedundantPath, neStatesObsolete_TerminalConnected=neStatesObsolete_TerminalConnected, neModuleTable=neModuleTable, neConfigObsolete_Alarmdelay=neConfigObsolete_Alarmdelay, neConfigObsolete_NEtype=neConfigObsolete_NEtype, neModuleSubrackSlot=neModuleSubrackSlot, neModuleCustomerCode=neModuleCustomerCode, neControlTrapDisable=neControlTrapDisable, neStatesObsolete_ActivateRedundantPath=neStatesObsolete_ActivateRedundantPath, neObsolete_InitPhase=neObsolete_InitPhase, neObsolete_PredecessorNominalPath=neObsolete_PredecessorNominalPath, neModuleArticleNumber=neModuleArticleNumber, neStates=neStates, neModuleSlotUnitsUsed=neModuleSlotUnitsUsed, neModuleSubrack=neModuleSubrack, neModuleDateOfProduction=neModuleDateOfProduction, neModuleHardwareVersion=neModuleHardwareVersion, neModuleUserdata=neModuleUserdata, neConfig=neConfig, neControl=neControl, neModuleModelName=neModuleModelName, neStatesObsolete_Redundant=neStatesObsolete_Redundant, neLocationStreet=neLocationStreet, neControlObsolete_SetDefaultAPS=neControlObsolete_SetDefaultAPS, neModuleEntry=neModuleEntry, neModuleNESlot=neModuleNESlot, neObsolete_APSMode=neObsolete_APSMode, neObsolete_NumberModul=neObsolete_NumberModul, neModuleMibLink=neModuleMibLink)
