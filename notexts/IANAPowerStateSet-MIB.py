#
# PySNMP MIB module IANAPowerStateSet-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IANAPowerStateSet-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 15:51:04 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Gauge32, ObjectIdentity, Unsigned32, Counter32, MibIdentifier, TimeTicks, ModuleIdentity, mib_2, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Gauge32", "ObjectIdentity", "Unsigned32", "Counter32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "mib-2", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaPowerStateSet = ModuleIdentity((1, 3, 6, 1, 2, 1, 228))
ianaPowerStateSet.setRevisions(('2015-02-09 00:00',))
if mibBuilder.loadTexts: ianaPowerStateSet.setLastUpdated('201502090000Z')
if mibBuilder.loadTexts: ianaPowerStateSet.setOrganization('IANA')
class PowerStateSet(TextualConvention, Integer32):
    reference = 'http://www.iana.org/assignments/power-state-sets'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 255, 256, 257, 258, 259, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 1024, 1025, 1026, 1027, 1028, 1029, 1030, 1031, 1032, 1033, 1034, 1035, 1036))
    namedValues = NamedValues(("other", 0), ("unknown", 255), ("ieee1621", 256), ("ieee1621Off", 257), ("ieee1621Sleep", 258), ("ieee1621On", 259), ("dmtf", 512), ("dmtfOn", 513), ("dmtfSleepLight", 514), ("dmtfSleepDeep", 515), ("dmtfOffHard", 516), ("dmtfOffSoft", 517), ("dmtfHibernate", 518), ("dmtfPowerOffSoft", 519), ("dmtfPowerOffHard", 520), ("dmtfMasterBusReset", 521), ("dmtfDiagnosticInterrapt", 522), ("dmtfOffSoftGraceful", 523), ("dmtfOffHardGraceful", 524), ("dmtfMasterBusResetGraceful", 525), ("dmtfPowerCycleOffSoftGraceful", 526), ("dmtfPowerCycleHardGraceful", 527), ("eman", 1024), ("emanMechOff", 1025), ("emanSoftOff", 1026), ("emanHibernate", 1027), ("emanSleep", 1028), ("emanStandby", 1029), ("emanReady", 1030), ("emanLowMinus", 1031), ("emanLow", 1032), ("emanMediumMinus", 1033), ("emanMedium", 1034), ("emanHighMinus", 1035), ("emanHigh", 1036))

mibBuilder.exportSymbols("IANAPowerStateSet-MIB", ianaPowerStateSet=ianaPowerStateSet, PowerStateSet=PowerStateSet, PYSNMP_MODULE_ID=ianaPowerStateSet)
