#
# PySNMP MIB module MEF-SOAM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/MEF-SOAM-TC-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:39 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, ModuleIdentity, iso, Unsigned32, TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType, IpAddress, Counter64, Counter32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "iso", "Unsigned32", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType", "IpAddress", "Counter64", "Counter32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mefSoamTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 15007, 1, 1))
mefSoamTcMib.setRevisions(('2012-01-10 00:00', '2010-10-11 00:00',))
if mibBuilder.loadTexts: mefSoamTcMib.setLastUpdated('201201100000Z')
if mibBuilder.loadTexts: mefSoamTcMib.setOrganization('Metro Ethernet Forum')
class MefSoamTcAvailabilityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("available", 1), ("unavailable", 2), ("unknown", 3))

class MefSoamTcConnectivityStatusType(TextualConvention, Integer32):
    reference = '[MEF17] 9.2 and [MEF7.1] III.2 Enumeration'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inactive", 1), ("active", 2), ("partiallyActive", 3))

class MefSoamTcDataPatternType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("zeroPattern", 1), ("onesPattern", 2))

class MefSoamTcDelayMeasurementBinType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("twoWayFrameDelay", 1), ("forwardFrameDelay", 2), ("backwardFrameDelay", 3), ("twoWayIfdv", 4), ("forwardIfdv", 5), ("backwardIfdv", 6), ("twoWayFrameDelayRange", 7), ("forwardFrameDelayRange", 8), ("backwardFrameDelayRange", 9))

class MefSoamTcIntervalTypeAisLck(TextualConvention, Integer32):
    reference = '[MEF7.1] III.2 Enumeration, [Y.1731] 7.4, 7.6'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oneSecond", 1), ("oneMinute", 2))

class MefSoamTcMeasurementPeriodType(TextualConvention, Unsigned32):
    reference = '[MEF SOAM-PM] R56'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(3, 3600000)

class MefSoamTcMegIdType(TextualConvention, Integer32):
    reference = '[Y.1731] Table A-1, [CFM] 17.5, 21.6.5.1'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 32))
    namedValues = NamedValues(("primaryVid", 1), ("charString", 2), ("unsignedInt16", 3), ("rfc2865VpnId", 4), ("iccBased", 32))

class MefSoamTcOperationTimeType(TextualConvention, Integer32):
    reference = '[SOAM-PM] R2, [SOAM-FM] 8.7'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("immediate", 2), ("relative", 3), ("fixed", 4))

class MefSoamTcSessionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("proactive", 1), ("onDemand", 2))

class MefSoamTcStatusType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("notActive", 2))

class MefSoamTcTestPatternType(TextualConvention, Integer32):
    reference = '[MEF7.1], Appendix III.2 Enumeration, [Y.1731] 7.7'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("null", 1), ("nullCrc32", 2), ("prbs", 3), ("prbsCrc32", 4))

mibBuilder.exportSymbols("MEF-SOAM-TC-MIB", MefSoamTcOperationTimeType=MefSoamTcOperationTimeType, mefSoamTcMib=mefSoamTcMib, MefSoamTcDataPatternType=MefSoamTcDataPatternType, MefSoamTcConnectivityStatusType=MefSoamTcConnectivityStatusType, MefSoamTcAvailabilityType=MefSoamTcAvailabilityType, MefSoamTcMegIdType=MefSoamTcMegIdType, MefSoamTcMeasurementPeriodType=MefSoamTcMeasurementPeriodType, PYSNMP_MODULE_ID=mefSoamTcMib, MefSoamTcTestPatternType=MefSoamTcTestPatternType, MefSoamTcSessionType=MefSoamTcSessionType, MefSoamTcDelayMeasurementBinType=MefSoamTcDelayMeasurementBinType, MefSoamTcIntervalTypeAisLck=MefSoamTcIntervalTypeAisLck, MefSoamTcStatusType=MefSoamTcStatusType)
