#
# PySNMP MIB module SYSAPPL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/SYSAPPL-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:35 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, ObjectIdentity, IpAddress, Counter64, mib_2, Bits, Counter32, NotificationType, Unsigned32, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "ObjectIdentity", "IpAddress", "Counter64", "mib-2", "Bits", "Counter32", "NotificationType", "Unsigned32", "Gauge32", "MibIdentifier")
DateAndTime, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "TextualConvention", "DisplayString")
sysApplMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 54))
sysApplMIB.setRevisions(('2006-01-06 00:00', '1997-10-20 00:00',))
if mibBuilder.loadTexts: sysApplMIB.setLastUpdated('200601060000Z')
if mibBuilder.loadTexts: sysApplMIB.setOrganization('IETF Applications MIB Working Group')
sysApplOBJ = MibIdentifier((1, 3, 6, 1, 2, 1, 54, 1))
sysApplInstalled = MibIdentifier((1, 3, 6, 1, 2, 1, 54, 1, 1))
sysApplRun = MibIdentifier((1, 3, 6, 1, 2, 1, 54, 1, 2))
sysApplMap = MibIdentifier((1, 3, 6, 1, 2, 1, 54, 1, 3))
sysApplNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 54, 2))
sysApplConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 54, 3))
class RunState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("running", 1), ("runnable", 2), ("waiting", 3), ("exiting", 4), ("other", 5))

class LongUtf8String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1024a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 1024)

class Utf8String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

sysApplInstallPkgTable = MibTable((1, 3, 6, 1, 2, 1, 54, 1, 1, 1), )
if mibBuilder.loadTexts: sysApplInstallPkgTable.setStatus('current')
sysApplInstallPkgEntry = MibTableRow((1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1), ).setIndexNames((0, "SYSAPPL-MIB", "sysApplInstallPkgIndex"))
if mibBuilder.loadTexts: sysApplInstallPkgEntry.setStatus('current')
sysApplInstallPkgIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sysApplInstallPkgIndex.setStatus('current')
sysApplInstallPkgManufacturer = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 2), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallPkgManufacturer.setStatus('current')
sysApplInstallPkgProductName = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 3), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallPkgProductName.setStatus('current')
sysApplInstallPkgVersion = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 4), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallPkgVersion.setStatus('current')
sysApplInstallPkgSerialNumber = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 5), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallPkgSerialNumber.setStatus('current')
sysApplInstallPkgDate = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 6), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallPkgDate.setStatus('current')
sysApplInstallPkgLocation = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 1, 1, 7), LongUtf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallPkgLocation.setStatus('current')
sysApplInstallElmtTable = MibTable((1, 3, 6, 1, 2, 1, 54, 1, 1, 2), )
if mibBuilder.loadTexts: sysApplInstallElmtTable.setStatus('current')
sysApplInstallElmtEntry = MibTableRow((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1), ).setIndexNames((0, "SYSAPPL-MIB", "sysApplInstallPkgIndex"), (0, "SYSAPPL-MIB", "sysApplInstallElmtIndex"))
if mibBuilder.loadTexts: sysApplInstallElmtEntry.setStatus('current')
sysApplInstallElmtIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sysApplInstallElmtIndex.setStatus('current')
sysApplInstallElmtName = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 2), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallElmtName.setStatus('current')
sysApplInstallElmtType = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("nonexecutable", 2), ("operatingSystem", 3), ("deviceDriver", 4), ("application", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallElmtType.setStatus('current')
sysApplInstallElmtDate = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallElmtDate.setStatus('current')
sysApplInstallElmtPath = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 5), LongUtf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallElmtPath.setStatus('current')
sysApplInstallElmtSizeHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallElmtSizeHigh.setStatus('current')
sysApplInstallElmtSizeLow = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 7), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallElmtSizeLow.setStatus('current')
sysApplInstallElmtRole = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysApplInstallElmtRole.setStatus('current')
sysApplInstallElmtModifyDate = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 9), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallElmtModifyDate.setStatus('current')
sysApplInstallElmtCurSizeHigh = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 10), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallElmtCurSizeHigh.setStatus('current')
sysApplInstallElmtCurSizeLow = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 1, 2, 1, 11), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplInstallElmtCurSizeLow.setStatus('current')
sysApplRunTable = MibTable((1, 3, 6, 1, 2, 1, 54, 1, 2, 1), )
if mibBuilder.loadTexts: sysApplRunTable.setStatus('current')
sysApplRunEntry = MibTableRow((1, 3, 6, 1, 2, 1, 54, 1, 2, 1, 1), ).setIndexNames((0, "SYSAPPL-MIB", "sysApplInstallPkgIndex"), (0, "SYSAPPL-MIB", "sysApplRunIndex"))
if mibBuilder.loadTexts: sysApplRunEntry.setStatus('current')
sysApplRunIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sysApplRunIndex.setStatus('current')
sysApplRunStarted = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 1, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplRunStarted.setStatus('current')
sysApplRunCurrentState = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 1, 1, 3), RunState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplRunCurrentState.setStatus('current')
sysApplPastRunTable = MibTable((1, 3, 6, 1, 2, 1, 54, 1, 2, 2), )
if mibBuilder.loadTexts: sysApplPastRunTable.setStatus('current')
sysApplPastRunEntry = MibTableRow((1, 3, 6, 1, 2, 1, 54, 1, 2, 2, 1), ).setIndexNames((0, "SYSAPPL-MIB", "sysApplInstallPkgIndex"), (0, "SYSAPPL-MIB", "sysApplPastRunIndex"))
if mibBuilder.loadTexts: sysApplPastRunEntry.setStatus('current')
sysApplPastRunIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 2, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sysApplPastRunIndex.setStatus('current')
sysApplPastRunStarted = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 2, 1, 2), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplPastRunStarted.setStatus('current')
sysApplPastRunExitState = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("complete", 1), ("failed", 2), ("other", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplPastRunExitState.setStatus('current')
sysApplPastRunTimeEnded = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplPastRunTimeEnded.setStatus('current')
sysApplElmtRunTable = MibTable((1, 3, 6, 1, 2, 1, 54, 1, 2, 3), )
if mibBuilder.loadTexts: sysApplElmtRunTable.setStatus('current')
sysApplElmtRunEntry = MibTableRow((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1), ).setIndexNames((0, "SYSAPPL-MIB", "sysApplElmtRunInstallPkg"), (0, "SYSAPPL-MIB", "sysApplElmtRunInvocID"), (0, "SYSAPPL-MIB", "sysApplElmtRunIndex"))
if mibBuilder.loadTexts: sysApplElmtRunEntry.setStatus('current')
sysApplElmtRunInstallPkg = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: sysApplElmtRunInstallPkg.setStatus('current')
sysApplElmtRunInvocID = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: sysApplElmtRunInvocID.setStatus('current')
sysApplElmtRunIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: sysApplElmtRunIndex.setStatus('current')
sysApplElmtRunInstallID = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtRunInstallID.setStatus('current')
sysApplElmtRunTimeStarted = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtRunTimeStarted.setStatus('current')
sysApplElmtRunState = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 6), RunState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtRunState.setStatus('current')
sysApplElmtRunName = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 7), LongUtf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtRunName.setStatus('current')
sysApplElmtRunParameters = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 8), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtRunParameters.setStatus('current')
sysApplElmtRunCPU = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 9), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtRunCPU.setStatus('current')
sysApplElmtRunMemory = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 10), Gauge32()).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtRunMemory.setStatus('current')
sysApplElmtRunNumFiles = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 11), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtRunNumFiles.setStatus('current')
sysApplElmtRunUser = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 3, 1, 12), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtRunUser.setStatus('current')
sysApplElmtPastRunTable = MibTable((1, 3, 6, 1, 2, 1, 54, 1, 2, 4), )
if mibBuilder.loadTexts: sysApplElmtPastRunTable.setStatus('current')
sysApplElmtPastRunEntry = MibTableRow((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1), ).setIndexNames((0, "SYSAPPL-MIB", "sysApplInstallPkgIndex"), (0, "SYSAPPL-MIB", "sysApplElmtPastRunInvocID"), (0, "SYSAPPL-MIB", "sysApplElmtPastRunIndex"))
if mibBuilder.loadTexts: sysApplElmtPastRunEntry.setStatus('current')
sysApplElmtPastRunInvocID = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295)))
if mibBuilder.loadTexts: sysApplElmtPastRunInvocID.setStatus('current')
sysApplElmtPastRunIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: sysApplElmtPastRunIndex.setStatus('current')
sysApplElmtPastRunInstallID = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtPastRunInstallID.setStatus('current')
sysApplElmtPastRunTimeStarted = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtPastRunTimeStarted.setStatus('current')
sysApplElmtPastRunTimeEnded = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtPastRunTimeEnded.setStatus('current')
sysApplElmtPastRunName = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 6), LongUtf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtPastRunName.setStatus('current')
sysApplElmtPastRunParameters = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 7), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtPastRunParameters.setStatus('current')
sysApplElmtPastRunCPU = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 8), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtPastRunCPU.setStatus('current')
sysApplElmtPastRunMemory = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setUnits('Kbytes').setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtPastRunMemory.setStatus('current')
sysApplElmtPastRunNumFiles = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtPastRunNumFiles.setStatus('current')
sysApplElmtPastRunUser = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 2, 4, 1, 11), Utf8String()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElmtPastRunUser.setStatus('current')
sysApplPastRunMaxRows = MibScalar((1, 3, 6, 1, 2, 1, 54, 1, 2, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysApplPastRunMaxRows.setStatus('current')
sysApplPastRunTableRemItems = MibScalar((1, 3, 6, 1, 2, 1, 54, 1, 2, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplPastRunTableRemItems.setStatus('current')
sysApplPastRunTblTimeLimit = MibScalar((1, 3, 6, 1, 2, 1, 54, 1, 2, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(7200)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysApplPastRunTblTimeLimit.setStatus('current')
sysApplElemPastRunMaxRows = MibScalar((1, 3, 6, 1, 2, 1, 54, 1, 2, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(500)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysApplElemPastRunMaxRows.setStatus('current')
sysApplElemPastRunTableRemItems = MibScalar((1, 3, 6, 1, 2, 1, 54, 1, 2, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplElemPastRunTableRemItems.setStatus('current')
sysApplElemPastRunTblTimeLimit = MibScalar((1, 3, 6, 1, 2, 1, 54, 1, 2, 10), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(7200)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysApplElemPastRunTblTimeLimit.setStatus('current')
sysApplAgentPollInterval = MibScalar((1, 3, 6, 1, 2, 1, 54, 1, 2, 11), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)).clone(60)).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: sysApplAgentPollInterval.setStatus('current')
sysApplMapTable = MibTable((1, 3, 6, 1, 2, 1, 54, 1, 3, 1), )
if mibBuilder.loadTexts: sysApplMapTable.setStatus('current')
sysApplMapEntry = MibTableRow((1, 3, 6, 1, 2, 1, 54, 1, 3, 1, 1), ).setIndexNames((0, "SYSAPPL-MIB", "sysApplElmtRunIndex"), (0, "SYSAPPL-MIB", "sysApplElmtRunInvocID"), (0, "SYSAPPL-MIB", "sysApplMapInstallElmtIndex"))
if mibBuilder.loadTexts: sysApplMapEntry.setStatus('current')
sysApplMapInstallElmtIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 3, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295)))
if mibBuilder.loadTexts: sysApplMapInstallElmtIndex.setStatus('current')
sysApplMapInstallPkgIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 54, 1, 3, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sysApplMapInstallPkgIndex.setStatus('current')
sysApplMIBCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 54, 3, 1))
sysApplMIBGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 54, 3, 2))
sysApplMIBCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 54, 3, 1, 1)).setObjects(("SYSAPPL-MIB", "sysApplInstalledGroup"), ("SYSAPPL-MIB", "sysApplRunGroup"), ("SYSAPPL-MIB", "sysApplMapGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysApplMIBCompliance = sysApplMIBCompliance.setStatus('current')
sysApplInstalledGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 54, 3, 2, 1)).setObjects(("SYSAPPL-MIB", "sysApplInstallPkgManufacturer"), ("SYSAPPL-MIB", "sysApplInstallPkgProductName"), ("SYSAPPL-MIB", "sysApplInstallPkgVersion"), ("SYSAPPL-MIB", "sysApplInstallPkgSerialNumber"), ("SYSAPPL-MIB", "sysApplInstallPkgDate"), ("SYSAPPL-MIB", "sysApplInstallPkgLocation"), ("SYSAPPL-MIB", "sysApplInstallElmtName"), ("SYSAPPL-MIB", "sysApplInstallElmtType"), ("SYSAPPL-MIB", "sysApplInstallElmtDate"), ("SYSAPPL-MIB", "sysApplInstallElmtPath"), ("SYSAPPL-MIB", "sysApplInstallElmtSizeHigh"), ("SYSAPPL-MIB", "sysApplInstallElmtSizeLow"), ("SYSAPPL-MIB", "sysApplInstallElmtRole"), ("SYSAPPL-MIB", "sysApplInstallElmtModifyDate"), ("SYSAPPL-MIB", "sysApplInstallElmtCurSizeHigh"), ("SYSAPPL-MIB", "sysApplInstallElmtCurSizeLow"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysApplInstalledGroup = sysApplInstalledGroup.setStatus('current')
sysApplRunGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 54, 3, 2, 2)).setObjects(("SYSAPPL-MIB", "sysApplRunStarted"), ("SYSAPPL-MIB", "sysApplRunCurrentState"), ("SYSAPPL-MIB", "sysApplPastRunStarted"), ("SYSAPPL-MIB", "sysApplPastRunExitState"), ("SYSAPPL-MIB", "sysApplPastRunTimeEnded"), ("SYSAPPL-MIB", "sysApplElmtRunInstallID"), ("SYSAPPL-MIB", "sysApplElmtRunTimeStarted"), ("SYSAPPL-MIB", "sysApplElmtRunState"), ("SYSAPPL-MIB", "sysApplElmtRunName"), ("SYSAPPL-MIB", "sysApplElmtRunParameters"), ("SYSAPPL-MIB", "sysApplElmtRunCPU"), ("SYSAPPL-MIB", "sysApplElmtRunMemory"), ("SYSAPPL-MIB", "sysApplElmtRunNumFiles"), ("SYSAPPL-MIB", "sysApplElmtRunUser"), ("SYSAPPL-MIB", "sysApplElmtPastRunInstallID"), ("SYSAPPL-MIB", "sysApplElmtPastRunTimeStarted"), ("SYSAPPL-MIB", "sysApplElmtPastRunTimeEnded"), ("SYSAPPL-MIB", "sysApplElmtPastRunName"), ("SYSAPPL-MIB", "sysApplElmtPastRunParameters"), ("SYSAPPL-MIB", "sysApplElmtPastRunCPU"), ("SYSAPPL-MIB", "sysApplElmtPastRunMemory"), ("SYSAPPL-MIB", "sysApplElmtPastRunNumFiles"), ("SYSAPPL-MIB", "sysApplElmtPastRunUser"), ("SYSAPPL-MIB", "sysApplPastRunMaxRows"), ("SYSAPPL-MIB", "sysApplPastRunTableRemItems"), ("SYSAPPL-MIB", "sysApplPastRunTblTimeLimit"), ("SYSAPPL-MIB", "sysApplElemPastRunMaxRows"), ("SYSAPPL-MIB", "sysApplElemPastRunTableRemItems"), ("SYSAPPL-MIB", "sysApplElemPastRunTblTimeLimit"), ("SYSAPPL-MIB", "sysApplAgentPollInterval"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysApplRunGroup = sysApplRunGroup.setStatus('current')
sysApplMapGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 54, 3, 2, 3)).setObjects(("SYSAPPL-MIB", "sysApplMapInstallPkgIndex"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    sysApplMapGroup = sysApplMapGroup.setStatus('current')
mibBuilder.exportSymbols("SYSAPPL-MIB", sysApplMap=sysApplMap, sysApplElmtRunMemory=sysApplElmtRunMemory, sysApplMIBCompliance=sysApplMIBCompliance, sysApplRunEntry=sysApplRunEntry, sysApplElmtPastRunMemory=sysApplElmtPastRunMemory, sysApplRunIndex=sysApplRunIndex, sysApplElmtRunInstallID=sysApplElmtRunInstallID, sysApplElmtPastRunUser=sysApplElmtPastRunUser, sysApplMapGroup=sysApplMapGroup, sysApplPastRunTblTimeLimit=sysApplPastRunTblTimeLimit, sysApplInstallElmtName=sysApplInstallElmtName, sysApplRunCurrentState=sysApplRunCurrentState, sysApplPastRunTableRemItems=sysApplPastRunTableRemItems, sysApplRunStarted=sysApplRunStarted, sysApplInstallPkgTable=sysApplInstallPkgTable, sysApplElmtRunNumFiles=sysApplElmtRunNumFiles, sysApplElmtRunTable=sysApplElmtRunTable, sysApplInstallElmtDate=sysApplInstallElmtDate, sysApplMapInstallElmtIndex=sysApplMapInstallElmtIndex, sysApplElmtPastRunCPU=sysApplElmtPastRunCPU, sysApplInstallPkgProductName=sysApplInstallPkgProductName, sysApplElmtRunInstallPkg=sysApplElmtRunInstallPkg, sysApplElmtRunUser=sysApplElmtRunUser, sysApplElmtPastRunTimeStarted=sysApplElmtPastRunTimeStarted, sysApplRun=sysApplRun, sysApplOBJ=sysApplOBJ, sysApplInstallPkgEntry=sysApplInstallPkgEntry, sysApplElmtRunEntry=sysApplElmtRunEntry, sysApplElmtPastRunName=sysApplElmtPastRunName, sysApplElemPastRunTblTimeLimit=sysApplElemPastRunTblTimeLimit, sysApplElmtPastRunTimeEnded=sysApplElmtPastRunTimeEnded, PYSNMP_MODULE_ID=sysApplMIB, sysApplElmtPastRunInvocID=sysApplElmtPastRunInvocID, sysApplElmtRunParameters=sysApplElmtRunParameters, sysApplInstalled=sysApplInstalled, sysApplInstallPkgManufacturer=sysApplInstallPkgManufacturer, sysApplElmtPastRunEntry=sysApplElmtPastRunEntry, sysApplElmtPastRunInstallID=sysApplElmtPastRunInstallID, sysApplMIB=sysApplMIB, sysApplElemPastRunMaxRows=sysApplElemPastRunMaxRows, sysApplElemPastRunTableRemItems=sysApplElemPastRunTableRemItems, sysApplMIBCompliances=sysApplMIBCompliances, sysApplPastRunStarted=sysApplPastRunStarted, sysApplInstallPkgIndex=sysApplInstallPkgIndex, sysApplInstallElmtEntry=sysApplInstallElmtEntry, sysApplElmtRunTimeStarted=sysApplElmtRunTimeStarted, sysApplRunTable=sysApplRunTable, sysApplAgentPollInterval=sysApplAgentPollInterval, sysApplElmtRunCPU=sysApplElmtRunCPU, sysApplMapInstallPkgIndex=sysApplMapInstallPkgIndex, sysApplInstallElmtModifyDate=sysApplInstallElmtModifyDate, sysApplMapEntry=sysApplMapEntry, sysApplInstallPkgVersion=sysApplInstallPkgVersion, LongUtf8String=LongUtf8String, sysApplInstallElmtTable=sysApplInstallElmtTable, Utf8String=Utf8String, sysApplInstalledGroup=sysApplInstalledGroup, sysApplElmtRunName=sysApplElmtRunName, sysApplInstallElmtSizeLow=sysApplInstallElmtSizeLow, sysApplPastRunTimeEnded=sysApplPastRunTimeEnded, sysApplElmtRunInvocID=sysApplElmtRunInvocID, sysApplPastRunTable=sysApplPastRunTable, sysApplInstallElmtType=sysApplInstallElmtType, RunState=RunState, sysApplInstallPkgLocation=sysApplInstallPkgLocation, sysApplInstallElmtCurSizeLow=sysApplInstallElmtCurSizeLow, sysApplElmtPastRunNumFiles=sysApplElmtPastRunNumFiles, sysApplInstallElmtIndex=sysApplInstallElmtIndex, sysApplInstallElmtPath=sysApplInstallElmtPath, sysApplMIBGroups=sysApplMIBGroups, sysApplElmtPastRunParameters=sysApplElmtPastRunParameters, sysApplRunGroup=sysApplRunGroup, sysApplInstallElmtSizeHigh=sysApplInstallElmtSizeHigh, sysApplElmtPastRunIndex=sysApplElmtPastRunIndex, sysApplPastRunMaxRows=sysApplPastRunMaxRows, sysApplElmtPastRunTable=sysApplElmtPastRunTable, sysApplConformance=sysApplConformance, sysApplPastRunExitState=sysApplPastRunExitState, sysApplNotifications=sysApplNotifications, sysApplInstallPkgDate=sysApplInstallPkgDate, sysApplInstallElmtCurSizeHigh=sysApplInstallElmtCurSizeHigh, sysApplPastRunIndex=sysApplPastRunIndex, sysApplElmtRunState=sysApplElmtRunState, sysApplMapTable=sysApplMapTable, sysApplInstallPkgSerialNumber=sysApplInstallPkgSerialNumber, sysApplElmtRunIndex=sysApplElmtRunIndex, sysApplInstallElmtRole=sysApplInstallElmtRole, sysApplPastRunEntry=sysApplPastRunEntry)
