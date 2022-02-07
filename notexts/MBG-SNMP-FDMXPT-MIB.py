#
# PySNMP MIB module MBG-SNMP-FDMXPT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/meinberg/MBG-SNMP-FDMXPT-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:16:07 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mbgSnmpRoot, = mibBuilder.importSymbols("MBG-SNMP-ROOT-MIB", "mbgSnmpRoot")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
NotificationType, Integer32, iso, Bits, Counter32, Counter64, TimeTicks, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ObjectIdentity, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Integer32", "iso", "Bits", "Counter32", "Counter64", "TimeTicks", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mbgFDM = ModuleIdentity((1, 3, 6, 1, 4, 1, 5597, 15))
mbgFDM.setRevisions(('2012-01-25 00:00', '2006-01-20 00:00',))
if mibBuilder.loadTexts: mbgFDM.setLastUpdated('201201250000Z')
if mibBuilder.loadTexts: mbgFDM.setOrganization('www.meinberg.de')
mbgFDMData = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 15, 2))
mbgFDMTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 15, 3))
mbgFDMMode = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMMode.setStatus('current')
mbgFDMModeVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMModeVal.setStatus('current')
mbgFDMFrequency = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMFrequency.setStatus('current')
mbgFDMFrequencyVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMFrequencyVal.setStatus('current')
mbgFDMRefTime = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMRefTime.setStatus('current')
mbgFDMPLTime = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMPLTime.setStatus('current')
mbgFDMFreqDev = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMFreqDev.setStatus('current')
mbgFDMFreqDevVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMFreqDevVal.setStatus('current')
mbgFDMTimeDev = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMTimeDev.setStatus('current')
mbgFDMTimeDevVal = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMTimeDevVal.setStatus('current')
mbgFDMErrorStatus = MibScalar((1, 3, 6, 1, 4, 1, 5597, 15, 2, 11), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mbgFDMErrorStatus.setStatus('current')
mbgFDMTrapInternalError = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 1))
if mibBuilder.loadTexts: mbgFDMTrapInternalError.setStatus('current')
mbgFDMTrapNoTimeString = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 2))
if mibBuilder.loadTexts: mbgFDMTrapNoTimeString.setStatus('current')
mbgFDMTrapNo10Mhz = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 3))
if mibBuilder.loadTexts: mbgFDMTrapNo10Mhz.setStatus('current')
mbgFDMTrapNoPPS = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 4))
if mibBuilder.loadTexts: mbgFDMTrapNoPPS.setStatus('current')
mbgFDMTrapNoPowerline = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 5))
if mibBuilder.loadTexts: mbgFDMTrapNoPowerline.setStatus('current')
mbgFDMTrapTimeDeviationOverflow = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 6))
if mibBuilder.loadTexts: mbgFDMTrapTimeDeviationOverflow.setStatus('current')
mbgFDMTrapA1Overflow = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 7))
if mibBuilder.loadTexts: mbgFDMTrapA1Overflow.setStatus('current')
mbgFDMTrapA2Overflow = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 8))
if mibBuilder.loadTexts: mbgFDMTrapA2Overflow.setStatus('current')
mbgFDMTrapFreqLimitExceeded = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 9))
if mibBuilder.loadTexts: mbgFDMTrapFreqLimitExceeded.setStatus('current')
mbgFDMXPTReboot = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 10))
if mibBuilder.loadTexts: mbgFDMXPTReboot.setStatus('current')
mbgFDMNormalOperation = NotificationType((1, 3, 6, 1, 4, 1, 5597, 15, 3, 99))
if mibBuilder.loadTexts: mbgFDMNormalOperation.setStatus('current')
mbgFDMConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 15, 90))
mbgFDMCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 15, 90, 1))
mbgFDMGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5597, 15, 90, 2))
mbgFDMCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5597, 15, 90, 1, 1)).setObjects(("MBG-SNMP-FDMXPT-MIB", "mbgFDMObjectsGroup"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgFDMCompliance = mbgFDMCompliance.setStatus('current')
mbgFDMObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5597, 15, 90, 2, 1)).setObjects(("MBG-SNMP-FDMXPT-MIB", "mbgFDMMode"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMModeVal"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFrequency"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFrequencyVal"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMRefTime"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMPLTime"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFreqDev"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMFreqDevVal"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTimeDev"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTimeDevVal"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMErrorStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgFDMObjectsGroup = mbgFDMObjectsGroup.setStatus('current')
mbgFDMTrapsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 5597, 15, 90, 2, 2)).setObjects(("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapInternalError"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNoTimeString"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNo10Mhz"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNoPPS"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapNoPowerline"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapTimeDeviationOverflow"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapA1Overflow"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapA2Overflow"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMTrapFreqLimitExceeded"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMXPTReboot"), ("MBG-SNMP-FDMXPT-MIB", "mbgFDMNormalOperation"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mbgFDMTrapsGroup = mbgFDMTrapsGroup.setStatus('current')
mibBuilder.exportSymbols("MBG-SNMP-FDMXPT-MIB", mbgFDMTimeDev=mbgFDMTimeDev, mbgFDMTrapFreqLimitExceeded=mbgFDMTrapFreqLimitExceeded, mbgFDMFrequency=mbgFDMFrequency, mbgFDMXPTReboot=mbgFDMXPTReboot, mbgFDMPLTime=mbgFDMPLTime, mbgFDMFreqDevVal=mbgFDMFreqDevVal, mbgFDMTrapTimeDeviationOverflow=mbgFDMTrapTimeDeviationOverflow, mbgFDMFrequencyVal=mbgFDMFrequencyVal, mbgFDMTimeDevVal=mbgFDMTimeDevVal, mbgFDMObjectsGroup=mbgFDMObjectsGroup, mbgFDMTrapNoPowerline=mbgFDMTrapNoPowerline, mbgFDMTrapA2Overflow=mbgFDMTrapA2Overflow, mbgFDMRefTime=mbgFDMRefTime, mbgFDMCompliance=mbgFDMCompliance, mbgFDMGroups=mbgFDMGroups, mbgFDMTrapA1Overflow=mbgFDMTrapA1Overflow, mbgFDMConformance=mbgFDMConformance, mbgFDMTrapNo10Mhz=mbgFDMTrapNo10Mhz, mbgFDMMode=mbgFDMMode, PYSNMP_MODULE_ID=mbgFDM, mbgFDM=mbgFDM, mbgFDMTraps=mbgFDMTraps, mbgFDMFreqDev=mbgFDMFreqDev, mbgFDMCompliances=mbgFDMCompliances, mbgFDMTrapsGroup=mbgFDMTrapsGroup, mbgFDMData=mbgFDMData, mbgFDMTrapNoTimeString=mbgFDMTrapNoTimeString, mbgFDMNormalOperation=mbgFDMNormalOperation, mbgFDMTrapNoPPS=mbgFDMTrapNoPPS, mbgFDMTrapInternalError=mbgFDMTrapInternalError, mbgFDMModeVal=mbgFDMModeVal, mbgFDMErrorStatus=mbgFDMErrorStatus)
