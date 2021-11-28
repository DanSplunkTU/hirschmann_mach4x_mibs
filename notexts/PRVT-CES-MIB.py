#
# PySNMP MIB module PRVT-CES-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binos/PRVT-CES-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:40 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
dsx1ConfigEntry, = mibBuilder.importSymbols("DS1-MIB", "dsx1ConfigEntry")
switch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "switch")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Gauge32, NotificationType, TimeTicks, Integer32, Bits, Counter64, Unsigned32, iso, MibIdentifier, ObjectIdentity, ModuleIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Gauge32", "NotificationType", "TimeTicks", "Integer32", "Bits", "Counter64", "Unsigned32", "iso", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TimeStamp")
prvtCESMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 1, 5, 111))
prvtCESMib.setRevisions(('2009-05-18 00:00', '2009-05-14 00:00', '2009-05-05 00:00', '2009-03-19 00:00', '2009-02-25 00:00', '2009-02-16 00:00', '2008-06-19 00:00', '2006-03-07 00:00', '2006-02-23 00:00', '2005-03-11 00:00',))
if mibBuilder.loadTexts: prvtCESMib.setLastUpdated('200905180000Z')
if mibBuilder.loadTexts: prvtCESMib.setOrganization('BATM Advanced Communication')
class ConfigAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("noop", 1), ("applyConfiguration", 2), ("rejectConfiguration", 3), ("restart", 4))

class E1Impedance(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notApplicable", 0), ("e1-75ohm", 1), ("e1-75hrl", 2), ("e1-120ohm", 3), ("e1-120hrl", 4))

class T1LongCableLength(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notApplicable", 1), ("neg75dB", 2), ("neg15dB", 3), ("neg225dB", 4), ("zerodB", 5))

class T1GainLimit(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("none", 1), ("gain30", 2), ("gain36", 3))

class CESLineType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("e1", 1), ("t1", 2), ("e1-sdh", 3), ("t1-sdh", 4), ("t1-sonet", 5))

class ServiceClock(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("notAplicable", 0), ("loopTiming", 1), ("localTiming", 2), ("adaptive", 3), ("differntial", 4))

prvtCESNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 0))
prvtCESObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1))
prvtCESConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2))
prvtCESDsx1ExtTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1), )
if mibBuilder.loadTexts: prvtCESDsx1ExtTable.setStatus('current')
prvtCESDsx1ExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1), )
dsx1ConfigEntry.registerAugmentions(("PRVT-CES-MIB", "prvtCESDsx1ExtEntry"))
prvtCESDsx1ExtEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: prvtCESDsx1ExtEntry.setStatus('current')
prvtCESE1Impedance = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 1), E1Impedance()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESE1Impedance.setStatus('current')
prvtCEST1GainLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 2), T1GainLimit()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCEST1GainLimit.setStatus('current')
prvtCESPortShutdown = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESPortShutdown.setStatus('current')
prvtCESPortLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("other", 1), ("dsx1ESF", 2), ("dsx1D4", 3), ("dsx1E1", 4), ("dsx1E1CRC", 5), ("dsx1E1MF", 6), ("dsx1E1CRCMF", 7), ("dsx1Unframed", 8), ("dsx1E1Unframed", 9), ("dsx1DS2M12", 10), ("dsx1E2", 11), ("dsx1E1Q50", 12), ("dsx1E1Q50CRC", 13), ("dsx1SFCAS", 14), ("dsx1ESFCAS", 15), ("notApplicable", 16)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESPortLineType.setStatus('current')
prvtCEST1LongCableLength = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 5), T1LongCableLength()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCEST1LongCableLength.setStatus('current')
prvtCESPortOperStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerlayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESPortOperStatus.setStatus('current')
prvtCESClearPortStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESClearPortStatistics.setStatus('current')
prvtCESServiceClock = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 1, 1, 8), ServiceClock()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESServiceClock.setStatus('current')
prvtCESUnappTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3), )
if mibBuilder.loadTexts: prvtCESUnappTable.setStatus('current')
prvtCESUnappEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1), )
dsx1ConfigEntry.registerAugmentions(("PRVT-CES-MIB", "prvtCESUnappEntry"))
prvtCESUnappEntry.setIndexNames(*dsx1ConfigEntry.getIndexNames())
if mibBuilder.loadTexts: prvtCESUnappEntry.setStatus('current')
prvtCESUnappLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))).clone(namedValues=NamedValues(("other", 1), ("dsx1ESF", 2), ("dsx1D4", 3), ("dsx1E1", 4), ("dsx1E1CRC", 5), ("dsx1E1MF", 6), ("dsx1E1CRCMF", 7), ("dsx1Unframed", 8), ("dsx1E1Unframed", 9), ("dsx1DS2M12", 10), ("dsx1E2", 11), ("dsx1E1Q50", 12), ("dsx1E1Q50CRC", 13)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappLineType.setStatus('current')
prvtCESUnappLineCoding = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("dsx1JBZS", 1), ("dsx1B8ZS", 2), ("dsx1HDB3", 3), ("dsx1ZBTSI", 4), ("dsx1AMI", 5), ("other", 6), ("dsx1B6ZS", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappLineCoding.setStatus('current')
prvtCESUnappLoopbackConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("dsx1NoLoop", 1), ("dsx1PayloadLoop", 2), ("dsx1LineLoop", 3), ("dsx1OtherLoop", 4), ("dsx1InwardLoop", 5), ("dsx1DualLoop", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappLoopbackConfig.setStatus('current')
prvtCESUnappSignalMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("none", 1), ("robbedBit", 2), ("bitOriented", 3), ("messageOriented", 4), ("other", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappSignalMode.setStatus('current')
prvtCESUnappTransmitClockSource = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3), ("adaptive", 4), ("external-port", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappTransmitClockSource.setStatus('current')
prvtCESUnappTransmitClockBackup = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappTransmitClockBackup.setStatus('current')
prvtCESUnappLineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 64000))).setUnits('meters').setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappLineLength.setStatus('current')
prvtCESUnappLineMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("csu", 1), ("dsu", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappLineMode.setStatus('current')
prvtCESUnappLineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("notApplicable", 1), ("neg75dB", 2), ("neg15dB", 3), ("neg225dB", 4), ("zerodB", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappLineBuildOut.setStatus('current')
prvtCESUnappE1Impedance = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 10), E1Impedance()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappE1Impedance.setStatus('current')
prvtCESUnappT1GainLimit = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 11), T1GainLimit()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappT1GainLimit.setStatus('current')
prvtCESUnappIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 12), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappIPAddress.setStatus('current')
prvtCESUnappIPAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 13), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappIPAddressMask.setStatus('current')
prvtCESUnappGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 3, 1, 14), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUnappGateway.setStatus('current')
prvtCESModuleConfTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2), )
if mibBuilder.loadTexts: prvtCESModuleConfTable.setStatus('current')
prvtCESModuleConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1), ).setIndexNames((0, "PRVT-CES-MIB", "prvtCESModuleIndex"))
if mibBuilder.loadTexts: prvtCESModuleConfEntry.setStatus('current')
prvtCESModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtCESModuleIndex.setStatus('current')
prvtCESModuleLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 2), CESLineType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModuleLineType.setStatus('current')
prvtCESModuleTxClock = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("loopTiming", 1), ("localTiming", 2), ("throughTiming", 3), ("adaptive", 4), ("external-port", 5), ("line", 6), ("ptp", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModuleTxClock.setStatus('current')
prvtCESModuleTxBackupClock = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModuleTxBackupClock.setStatus('current')
prvtCESModuleConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 5), ConfigAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModuleConfig.setStatus('current')
prvtCESModuleIPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModuleIPAddress.setStatus('current')
prvtCESModuleIPAddressMask = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 7), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModuleIPAddressMask.setStatus('current')
prvtCESModuleGateway = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModuleGateway.setStatus('current')
prvtCESModuleUpTime = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 9), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESModuleUpTime.setStatus('current')
prvtCESModuleMACAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 10), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESModuleMACAddress.setStatus('current')
prvtCESModuleHardwareRevision = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 11), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESModuleHardwareRevision.setStatus('current')
prvtCESModuleFirmwareVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 12), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESModuleFirmwareVersion.setStatus('current')
prvtCESModuleClearCircuitStatistics = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("clear", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModuleClearCircuitStatistics.setStatus('current')
prvtCESModuleLbit = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModuleLbit.setStatus('current')
prvtCESModulePolicyLops = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("idle", 0), ("all-one", 1), ("channel-idle", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyLops.setStatus('current')
prvtCESModulePolicyLbit = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 16), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("idle", 0), ("all-one", 1), ("channel-idle", 2), ("none", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyLbit.setStatus('current')
prvtCESModulePolicyRbit = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("rai", 1), ("channel-idle", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyRbit.setStatus('current')
prvtCESModulePolicyRd = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("rai", 1), ("channel-idle", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyRd.setStatus('current')
prvtCESModulePolicyIdlePattern = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyIdlePattern.setStatus('current')
prvtCESModulePolicyIdleSignalling = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 15))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyIdleSignalling.setStatus('current')
prvtCESModulePolicyLopsEnter = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 21), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyLopsEnter.setStatus('current')
prvtCESModulePolicyLopsExit = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 22), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 1023))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyLopsExit.setStatus('current')
prvtCESModulePolicyuUnstrLbit = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("all-one", 1))).clone('all-one')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyuUnstrLbit.setStatus('current')
prvtCESModulePolicyuStrReplace = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("all-one", 1), ("idle", 2))).clone('all-one')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyuStrReplace.setStatus('current')
prvtCESModulePolicyuUnstrReplace = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("all-one", 1), ("idle", 2))).clone('all-one')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyuUnstrReplace.setStatus('current')
prvtCESModulePolicyuUnstrLops = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("none", 0), ("all-one", 1))).clone('all-one')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyuUnstrLops.setStatus('current')
prvtCESModuleServiceClock = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 27), ServiceClock()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModuleServiceClock.setStatus('current')
prvtCESModulePolicyuUnstrReplacePattern = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 2, 1, 28), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESModulePolicyuUnstrReplacePattern.setStatus('current')
prvtCESDsx1AlarmTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4), )
if mibBuilder.loadTexts: prvtCESDsx1AlarmTable.setStatus('current')
prvtCESDsx1AlarmEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1), ).setIndexNames((0, "PRVT-CES-MIB", "prvtCESDsx1AlarmPort"), (0, "PRVT-CES-MIB", "prvtCESDsx1AlarmIndex"))
if mibBuilder.loadTexts: prvtCESDsx1AlarmEntry.setStatus('current')
prvtCESDsx1AlarmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: prvtCESDsx1AlarmPort.setStatus('current')
prvtCESDsx1AlarmIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1, 2), Gauge32())
if mibBuilder.loadTexts: prvtCESDsx1AlarmIndex.setStatus('current')
prvtCESDsx1AlarmVariable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESDsx1AlarmVariable.setStatus('current')
prvtCESDsx1AlarmThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESDsx1AlarmThreshold.setStatus('current')
prvtCESDsx1AlarmValue = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 4, 1, 5), Integer32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: prvtCESDsx1AlarmValue.setStatus('current')
prvtCESAlarmMonitor = MibScalar((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESAlarmMonitor.setStatus('current')
prvtCESCICTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6), )
if mibBuilder.loadTexts: prvtCESCICTable.setStatus('current')
prvtCESCICEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1), ).setIndexNames((0, "PRVT-CES-MIB", "prvtCESCICModuleId"), (0, "PRVT-CES-MIB", "prvtCESCICNumber"))
if mibBuilder.loadTexts: prvtCESCICEntry.setStatus('current')
prvtCESCICModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)))
if mibBuilder.loadTexts: prvtCESCICModuleId.setStatus('current')
prvtCESCICNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 2), Gauge32())
if mibBuilder.loadTexts: prvtCESCICNumber.setStatus('current')
prvtCESCICClockNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESCICClockNumber.setStatus('current')
prvtCESCICMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("freeRun", 1), ("acquisition", 2), ("normal", 3), ("holdover", 4), ("fastAcquisiton", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESCICMode.setStatus('current')
prvtCESCICTdmPort = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESCICTdmPort.setStatus('current')
prvtCESCICCircuit = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESCICCircuit.setStatus('current')
prvtCESCICStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("locked", 1), ("notlocked", 2), ("sourceInputLost", 3), ("sourceInputDegraded", 4), ("sourceTraceLost", 5), ("sourceTraceDegraded", 6), ("sourceFreqOffsetFailure", 7), ("recoveredClockDegraded", 8), ("localReferenceFailure", 9), ("remoteReferenceFailure", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESCICStatus.setStatus('current')
prvtCESCICState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 6, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("backup", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESCICState.setStatus('current')
prvtCESCICMappTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7), )
if mibBuilder.loadTexts: prvtCESCICMappTable.setStatus('current')
prvtCESCICMappEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7, 1), ).setIndexNames((0, "PRVT-CES-MIB", "prvtCESCICMappModuleId"), (0, "PRVT-CES-MIB", "prvtCESCICMappClockNumber"), (0, "PRVT-CES-MIB", "prvtCESCICMappCICNumber"))
if mibBuilder.loadTexts: prvtCESCICMappEntry.setStatus('current')
prvtCESCICMappModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESCICMappModuleId.setStatus('current')
prvtCESCICMappClockNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESCICMappClockNumber.setStatus('current')
prvtCESCICMappCICNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7, 1, 3), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESCICMappCICNumber.setStatus('current')
prvtCESCICMappState = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 7, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("backup", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESCICMappState.setStatus('current')
prvtCESApsTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8), )
if mibBuilder.loadTexts: prvtCESApsTable.setStatus('current')
prvtCESApsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1), ).setIndexNames((0, "PRVT-CES-MIB", "prvtCESModuleId"))
if mibBuilder.loadTexts: prvtCESApsEntry.setStatus('current')
prvtCESApsModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1, 1), Integer32())
if mibBuilder.loadTexts: prvtCESApsModuleId.setStatus('current')
prvtCESApsEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('enable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESApsEnable.setStatus('current')
prvtCESApsActiveLine = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESApsActiveLine.setStatus('current')
prvtSdBerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(5, 9))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtSdBerThreshold.setStatus('current')
prvtSfBerThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 8, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(3, 5))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtSfBerThreshold.setStatus('current')
prvtCESUpdateFirmwareTable = MibTable((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9), )
if mibBuilder.loadTexts: prvtCESUpdateFirmwareTable.setStatus('current')
prvtCESUpdateFirmwareEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1), ).setIndexNames((0, "PRVT-CES-MIB", "prvtCESModuleId"))
if mibBuilder.loadTexts: prvtCESUpdateFirmwareEntry.setStatus('current')
prvtCESModuleId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 32000)))
if mibBuilder.loadTexts: prvtCESModuleId.setStatus('current')
prvtCESFirmwareImageName = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESFirmwareImageName.setStatus('current')
prvtCESUpdateAction = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("none", 1), ("update", 2), ("updateThroughUART", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESUpdateAction.setStatus('current')
prvtCESUpdateStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("updateStatusUnknown", 1), ("updateSuccess", 2), ("updateInProgress", 3), ("updateFailed", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtCESUpdateStatus.setStatus('current')
prvtCESTFTPServer = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 1, 9, 1, 5), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtCESTFTPServer.setStatus('current')
prvtCESDsx1Alarm = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 0, 1)).setObjects(("PRVT-CES-MIB", "prvtCESDsx1AlarmVariable"), ("PRVT-CES-MIB", "prvtCESDsx1AlarmThreshold"), ("PRVT-CES-MIB", "prvtCESDsx1AlarmValue"))
if mibBuilder.loadTexts: prvtCESDsx1Alarm.setStatus('current')
prvtCESModuleAvailable = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 0, 2)).setObjects(("PRVT-CES-MIB", "prvtCESModuleIndex"))
if mibBuilder.loadTexts: prvtCESModuleAvailable.setStatus('current')
prvtCESModuleUnAvailableDueExtract = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 0, 3)).setObjects(("PRVT-CES-MIB", "prvtCESModuleIndex"))
if mibBuilder.loadTexts: prvtCESModuleUnAvailableDueExtract.setStatus('current')
prvtCESModuleUnAvailableDueReload = NotificationType((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 0, 4)).setObjects(("PRVT-CES-MIB", "prvtCESModuleIndex"))
if mibBuilder.loadTexts: prvtCESModuleUnAvailableDueReload.setStatus('current')
prvtCESDsx1Compliances = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2, 1))
prvtCESDsx1Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2, 2))
prvtCESDsx1Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2, 1, 1)).setObjects(("PRVT-CES-MIB", "prvtCESDsx1NotificationsGroup"), ("PRVT-CES-MIB", "prvtCESDsx1ROGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtCESDsx1Compliance = prvtCESDsx1Compliance.setStatus('current')
prvtCESDsx1NotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2, 2, 1)).setObjects(("PRVT-CES-MIB", "prvtCESDsx1Alarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtCESDsx1NotificationsGroup = prvtCESDsx1NotificationsGroup.setStatus('current')
prvtCESDsx1ROGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 738, 1, 5, 111, 2, 2, 2)).setObjects(("PRVT-CES-MIB", "prvtCESE1Impedance"), ("PRVT-CES-MIB", "prvtCEST1GainLimit"), ("PRVT-CES-MIB", "prvtCESModuleLineType"), ("PRVT-CES-MIB", "prvtCESModuleTxClock"), ("PRVT-CES-MIB", "prvtCESModuleConfig"), ("PRVT-CES-MIB", "prvtCESModuleIPAddress"), ("PRVT-CES-MIB", "prvtCESModuleIPAddressMask"), ("PRVT-CES-MIB", "prvtCESModuleGateway"), ("PRVT-CES-MIB", "prvtCESDsx1AlarmThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    prvtCESDsx1ROGroup = prvtCESDsx1ROGroup.setStatus('current')
mibBuilder.exportSymbols("PRVT-CES-MIB", prvtCESCICMappTable=prvtCESCICMappTable, prvtCESModuleClearCircuitStatistics=prvtCESModuleClearCircuitStatistics, prvtCESUnappTransmitClockSource=prvtCESUnappTransmitClockSource, prvtCESCICNumber=prvtCESCICNumber, prvtSdBerThreshold=prvtSdBerThreshold, prvtCESUpdateAction=prvtCESUpdateAction, prvtCESModulePolicyuUnstrLbit=prvtCESModulePolicyuUnstrLbit, prvtCESCICTdmPort=prvtCESCICTdmPort, prvtCESModuleMACAddress=prvtCESModuleMACAddress, prvtCESApsModuleId=prvtCESApsModuleId, prvtCESCICMappClockNumber=prvtCESCICMappClockNumber, prvtCESCICState=prvtCESCICState, prvtCESModuleTxBackupClock=prvtCESModuleTxBackupClock, prvtCESApsEnable=prvtCESApsEnable, prvtCESUnappE1Impedance=prvtCESUnappE1Impedance, E1Impedance=E1Impedance, ConfigAction=ConfigAction, prvtCEST1GainLimit=prvtCEST1GainLimit, prvtCESModulePolicyRd=prvtCESModulePolicyRd, prvtCESPortOperStatus=prvtCESPortOperStatus, prvtCESCICCircuit=prvtCESCICCircuit, prvtCESUnappIPAddressMask=prvtCESUnappIPAddressMask, prvtCESModulePolicyIdleSignalling=prvtCESModulePolicyIdleSignalling, prvtCESPortLineType=prvtCESPortLineType, prvtCESCICEntry=prvtCESCICEntry, prvtCESCICMappState=prvtCESCICMappState, prvtCESCICModuleId=prvtCESCICModuleId, prvtCESMib=prvtCESMib, prvtCESModuleIPAddress=prvtCESModuleIPAddress, prvtCESModuleLbit=prvtCESModuleLbit, prvtCESUnappEntry=prvtCESUnappEntry, prvtCESModulePolicyIdlePattern=prvtCESModulePolicyIdlePattern, prvtCESModuleConfig=prvtCESModuleConfig, prvtCESUnappLineType=prvtCESUnappLineType, prvtCESDsx1AlarmTable=prvtCESDsx1AlarmTable, prvtCESUpdateFirmwareEntry=prvtCESUpdateFirmwareEntry, prvtCESModulePolicyuUnstrLops=prvtCESModulePolicyuUnstrLops, prvtCESModulePolicyRbit=prvtCESModulePolicyRbit, prvtCESUnappLineLength=prvtCESUnappLineLength, prvtCESCICMappEntry=prvtCESCICMappEntry, CESLineType=CESLineType, prvtCESApsEntry=prvtCESApsEntry, prvtCESUnappTable=prvtCESUnappTable, prvtCESDsx1AlarmValue=prvtCESDsx1AlarmValue, prvtCESAlarmMonitor=prvtCESAlarmMonitor, prvtCESUnappLineCoding=prvtCESUnappLineCoding, PYSNMP_MODULE_ID=prvtCESMib, prvtCESModuleUnAvailableDueExtract=prvtCESModuleUnAvailableDueExtract, prvtCESCICTable=prvtCESCICTable, prvtCESModuleTxClock=prvtCESModuleTxClock, prvtCESModulePolicyLops=prvtCESModulePolicyLops, prvtCESDsx1Compliance=prvtCESDsx1Compliance, prvtCESDsx1NotificationsGroup=prvtCESDsx1NotificationsGroup, prvtCESDsx1Alarm=prvtCESDsx1Alarm, prvtCESModuleHardwareRevision=prvtCESModuleHardwareRevision, prvtCESModuleGateway=prvtCESModuleGateway, prvtCESDsx1Groups=prvtCESDsx1Groups, prvtCESConformance=prvtCESConformance, prvtCESUnappSignalMode=prvtCESUnappSignalMode, prvtCESCICClockNumber=prvtCESCICClockNumber, prvtCESCICMode=prvtCESCICMode, ServiceClock=ServiceClock, prvtCESModulePolicyuStrReplace=prvtCESModulePolicyuStrReplace, prvtCESApsActiveLine=prvtCESApsActiveLine, prvtCESModulePolicyLopsEnter=prvtCESModulePolicyLopsEnter, prvtCESDsx1ExtEntry=prvtCESDsx1ExtEntry, prvtCESModuleIPAddressMask=prvtCESModuleIPAddressMask, prvtCESUnappLineMode=prvtCESUnappLineMode, prvtCESModulePolicyLbit=prvtCESModulePolicyLbit, prvtCESCICMappCICNumber=prvtCESCICMappCICNumber, prvtCESModulePolicyuUnstrReplacePattern=prvtCESModulePolicyuUnstrReplacePattern, prvtCESClearPortStatistics=prvtCESClearPortStatistics, prvtCESUnappT1GainLimit=prvtCESUnappT1GainLimit, prvtCESModuleId=prvtCESModuleId, prvtCESUpdateFirmwareTable=prvtCESUpdateFirmwareTable, prvtCESModuleConfEntry=prvtCESModuleConfEntry, prvtCESNotifications=prvtCESNotifications, prvtCESModulePolicyuUnstrReplace=prvtCESModulePolicyuUnstrReplace, prvtCESCICMappModuleId=prvtCESCICMappModuleId, T1LongCableLength=T1LongCableLength, prvtCESE1Impedance=prvtCESE1Impedance, prvtCESUnappIPAddress=prvtCESUnappIPAddress, prvtCESDsx1AlarmEntry=prvtCESDsx1AlarmEntry, prvtCESDsx1AlarmPort=prvtCESDsx1AlarmPort, prvtCESServiceClock=prvtCESServiceClock, prvtCESDsx1ExtTable=prvtCESDsx1ExtTable, prvtCEST1LongCableLength=prvtCEST1LongCableLength, prvtCESTFTPServer=prvtCESTFTPServer, prvtCESModuleServiceClock=prvtCESModuleServiceClock, prvtSfBerThreshold=prvtSfBerThreshold, prvtCESModuleUpTime=prvtCESModuleUpTime, prvtCESUpdateStatus=prvtCESUpdateStatus, prvtCESObjects=prvtCESObjects, prvtCESDsx1AlarmIndex=prvtCESDsx1AlarmIndex, T1GainLimit=T1GainLimit, prvtCESModuleLineType=prvtCESModuleLineType, prvtCESUnappGateway=prvtCESUnappGateway, prvtCESModuleFirmwareVersion=prvtCESModuleFirmwareVersion, prvtCESDsx1AlarmVariable=prvtCESDsx1AlarmVariable, prvtCESDsx1ROGroup=prvtCESDsx1ROGroup, prvtCESUnappLineBuildOut=prvtCESUnappLineBuildOut, prvtCESApsTable=prvtCESApsTable, prvtCESModuleAvailable=prvtCESModuleAvailable, prvtCESModuleConfTable=prvtCESModuleConfTable, prvtCESModulePolicyLopsExit=prvtCESModulePolicyLopsExit, prvtCESPortShutdown=prvtCESPortShutdown, prvtCESUnappTransmitClockBackup=prvtCESUnappTransmitClockBackup, prvtCESUnappLoopbackConfig=prvtCESUnappLoopbackConfig, prvtCESModuleUnAvailableDueReload=prvtCESModuleUnAvailableDueReload, prvtCESCICStatus=prvtCESCICStatus, prvtCESFirmwareImageName=prvtCESFirmwareImageName, prvtCESModuleIndex=prvtCESModuleIndex, prvtCESDsx1Compliances=prvtCESDsx1Compliances, prvtCESDsx1AlarmThreshold=prvtCESDsx1AlarmThreshold)
