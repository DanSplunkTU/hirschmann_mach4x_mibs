#
# PySNMP MIB module SIAE-CFGM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-CFGM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:19:31 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
alarmTrap, = mibBuilder.importSymbols("SIAE-ALARM-MIB", "alarmTrap")
equipIpSnmpAgentAddress, = mibBuilder.importSymbols("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, TimeTicks, IpAddress, Counter32, Counter64, ObjectIdentity, Gauge32, ModuleIdentity, Bits, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "TimeTicks", "IpAddress", "Counter32", "Counter64", "ObjectIdentity", "Gauge32", "ModuleIdentity", "Bits", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
configManagement = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 30))
configManagement.setRevisions(('2014-07-25 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))
if mibBuilder.loadTexts: configManagement.setLastUpdated('201407250000Z')
if mibBuilder.loadTexts: configManagement.setOrganization('SIAE MICROELETTRONICA spa')
configManagementMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 30, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: configManagementMibVersion.setStatus('current')
configManagementFileName = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 30, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configManagementFileName.setStatus('current')
configManagementServerIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 30, 3), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configManagementServerIpAddress.setStatus('current')
configManagementAction = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 30, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("configNone", 0), ("configSave", 1), ("configUse", 2), ("configBack", 3), ("configAbort", 4), ("configUseAndSwitch", 5))).clone('configNone')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configManagementAction.setStatus('current')
configManagementState = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 30, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("configCompleted", 1), ("configInterrupted", 2), ("configVerifying", 3), ("configSaving", 4), ("configDownloading", 5), ("configUploading", 6), ("configUsing", 7), ("configMakingCopy", 8), ("configAborting", 9), ("configRestarting", 10), ("configStarted", 11))).clone('configCompleted')).setMaxAccess("readonly")
if mibBuilder.loadTexts: configManagementState.setStatus('current')
configManagementFailure = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 30, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("configNoFailure", 0), ("configVerifying", 3), ("configSaving", 4), ("configDownloading", 5), ("configUploading", 6), ("configUsing", 7), ("configMakingCopy", 8), ("configAborted", 9))).clone('configNoFailure')).setMaxAccess("readonly")
if mibBuilder.loadTexts: configManagementFailure.setStatus('current')
configManagementBackupFileDate = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 30, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: configManagementBackupFileDate.setStatus('current')
configManagementTrapNotification = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 30, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("trapDisable", 1), ("trapEnable", 2))).clone('trapEnable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: configManagementTrapNotification.setStatus('current')
configManagementFtpStatusTrap = NotificationType((1, 3, 6, 1, 4, 1, 3373, 1103, 0, 3001)).setObjects(("SIAE-EQUIP-MIB", "equipIpSnmpAgentAddress"), ("SIAE-CFGM-MIB", "configManagementState"), ("SIAE-CFGM-MIB", "configManagementFailure"))
if mibBuilder.loadTexts: configManagementFtpStatusTrap.setStatus('current')
mibBuilder.exportSymbols("SIAE-CFGM-MIB", configManagementFtpStatusTrap=configManagementFtpStatusTrap, PYSNMP_MODULE_ID=configManagement, configManagementFileName=configManagementFileName, configManagementTrapNotification=configManagementTrapNotification, configManagementAction=configManagementAction, configManagementMibVersion=configManagementMibVersion, configManagementServerIpAddress=configManagementServerIpAddress, configManagement=configManagement, configManagementBackupFileDate=configManagementBackupFileDate, configManagementState=configManagementState, configManagementFailure=configManagementFailure)
