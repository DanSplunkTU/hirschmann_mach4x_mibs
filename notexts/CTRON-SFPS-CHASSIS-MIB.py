#
# PySNMP MIB module CTRON-SFPS-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-SFPS-CHASSIS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:25:16 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
sfpsChassisRipTable, sfpsChassisRipAPI = mibBuilder.importSymbols("CTRON-SFPS-INCLUDE-MIB", "sfpsChassisRipTable", "sfpsChassisRipAPI")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity, Counter32, NotificationType, Unsigned32, Integer32, iso, TimeTicks, Counter64, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity", "Counter32", "NotificationType", "Unsigned32", "Integer32", "iso", "TimeTicks", "Counter64", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class SfpsAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

sfpsChassisRipChassisMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipChassisMac.setStatus('mandatory')
sfpsChassisRipFPPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipFPPortMask.setStatus('mandatory')
sfpsChassisRipINBPortMask = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipINBPortMask.setStatus('mandatory')
sfpsChassisRipModifiedTime = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 4), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipModifiedTime.setStatus('mandatory')
sfpsChassisRipStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("active", 2), ("dead", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipStatus.setStatus('mandatory')
sfpsChassisRipAPIVerb = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("add", 2), ("delete", 3), ("purgePort", 4), ("sendUpdate", 5), ("clearTable", 6), ("setTimer", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIVerb.setStatus('mandatory')
sfpsChassisRipAPIChassisMac = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 2), SfpsAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIChassisMac.setStatus('mandatory')
sfpsChassisRipAPIPort = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPIPort.setStatus('mandatory')
sfpsChassisRipAPITimer = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: sfpsChassisRipAPITimer.setStatus('mandatory')
sfpsChassisRipAPINumInTable = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 6, 1, 2, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sfpsChassisRipAPINumInTable.setStatus('mandatory')
mibBuilder.exportSymbols("CTRON-SFPS-CHASSIS-MIB", sfpsChassisRipAPITimer=sfpsChassisRipAPITimer, sfpsChassisRipFPPortMask=sfpsChassisRipFPPortMask, sfpsChassisRipAPIChassisMac=sfpsChassisRipAPIChassisMac, sfpsChassisRipChassisMac=sfpsChassisRipChassisMac, sfpsChassisRipINBPortMask=sfpsChassisRipINBPortMask, sfpsChassisRipAPIPort=sfpsChassisRipAPIPort, sfpsChassisRipStatus=sfpsChassisRipStatus, sfpsChassisRipAPIVerb=sfpsChassisRipAPIVerb, SfpsAddress=SfpsAddress, sfpsChassisRipAPINumInTable=sfpsChassisRipAPINumInTable, sfpsChassisRipModifiedTime=sfpsChassisRipModifiedTime)
