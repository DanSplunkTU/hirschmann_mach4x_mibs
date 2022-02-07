#
# PySNMP MIB module HC-PerfHist-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/output/asn1/HC-PerfHist-TC-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:06:55 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, Bits, ModuleIdentity, IpAddress, MibIdentifier, iso, Unsigned32, Counter64, mib_2, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "ModuleIdentity", "IpAddress", "MibIdentifier", "iso", "Unsigned32", "Counter64", "mib-2", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
hcPerfHistTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 107))
hcPerfHistTCMIB.setRevisions(('2004-02-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hcPerfHistTCMIB.setRevisionsDescriptions(('Initial version, published as RFC 3705.',))
if mibBuilder.loadTexts: hcPerfHistTCMIB.setLastUpdated('200402030000Z')
if mibBuilder.loadTexts: hcPerfHistTCMIB.setOrganization('ADSLMIB Working Group')
if mibBuilder.loadTexts: hcPerfHistTCMIB.setContactInfo('WG-email:  adslmib@ietf.org\n           Info:      https://www1.ietf.org/mailman/listinfo/adslmib\n\n           Chair:     Mike Sneed\n                      Sand Channel Systems\n           Postal:    P.O.  Box 37324\n                      Raleigh NC 27627-7324\n                      USA\n           Email:     sneedmike@hotmail.com\n           Phone:     +1 206 600 7022\n\n           Co-editor: Bob Ray\n                      PESA Switching Systems, Inc.\n           Postal:    330-A Wynn Drive\n                      Huntsville, AL 35805\n                      USA\n           Email:     rray@pesa.com\n           Phone:     +1 256 726 9200 ext.  142\n\n           Co-editor: Rajesh Abbi\n                      Alcatel USA\n           Postal:    2301 Sugar Bush Road\n                      Raleigh, NC 27612-3339\n                      USA\n           Email:     Rajesh.Abbi@alcatel.com\n           Phone:     +1 919 850 6194\n           ')
if mibBuilder.loadTexts: hcPerfHistTCMIB.setDescription('This MIB Module provides Textual Conventions to be\n            used by systems supporting 15 minute based performance\n            history counts that require high-capacity counts.\n\n            Copyright (C) The Internet Society (2004).  This version\n            of this MIB module is part of RFC 3705: see the RFC\n            itself for full legal notices.')
class HCPerfValidIntervals(TextualConvention, Integer32):
    description = 'The number of near end intervals for which data was\n          collected.  The value of an object with an\n          HCPerfValidIntervals syntax will be 96 unless the\n          measurement was (re-)started within the last 1440 minutes,\n          in which case the value will be the number of complete 15\n          minute intervals for which the agent has at least some data.\n          In certain cases (e.g., in the case where the agent is a\n          proxy) it is possible that some intervals are unavailable.\n          In this case, this interval is the maximum interval number\n          for which data is available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 96)

class HCPerfInvalidIntervals(TextualConvention, Integer32):
    description = 'The number of near end intervals for which no data is\n          available.  The value of an object with an\n          HCPerfInvalidIntervals syntax will typically be zero except\n          in cases where the data for some intervals are not available\n          (e.g., in proxy situations).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 96)

class HCPerfTimeElapsed(TextualConvention, Integer32):
    description = "The number of seconds that have elapsed since the beginning\n          of the current measurement period.  If, for some reason,\n          such as an adjustment in the system's time-of-day clock or\n          the addition of a leap second, the duration of the current\n          interval exceeds the maximum value, the agent will return\n          the maximum value.\n\n          For 15 minute intervals, the range is limited to (0..899).\n          For 24 hour intervals, the range is limited to (0..86399)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 86399)

class HCPerfIntervalThreshold(TextualConvention, Unsigned32):
    description = 'This convention defines a range of values that may be set\n           in a fault threshold alarm control.  As the number of\n           seconds in a 15-minute interval numbers at most 900,\n           objects of this type may have a range of 0...900, where the\n           value of 0 disables the alarm.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 900)

class HCPerfCurrentCount(TextualConvention, Counter64):
    description = "A gauge associated with a performance measurement in a\n            current 15 minute measurement interval.  The value of an\n            object with an HCPerfCurrentCount syntax starts from zero\n            and is increased when associated events occur, until the\n            end of the 15 minute interval.  At that time the value of\n            the gauge is stored in the first 15 minute history\n            interval, and the gauge is restarted at zero.  In the case\n            where the agent has no valid data available for the\n            current interval, the corresponding object instance is not\n            available and upon a retrieval request a corresponding\n            error message shall be returned to indicate that this\n            instance does not exist.\n\n            This count represents a non-negative integer, which\n            may increase or decrease, but shall never exceed 2^64-1\n            (18446744073709551615 decimal), nor fall below 0.  The\n            value of an object with HCPerfCurrentCount syntax\n            assumes its maximum value whenever the underlying count\n            exceeds 2^64-1.  If the underlying count subsequently\n            decreases below 2^64-1 (due, e.g., to a retroactive\n            adjustment as a result of entering or exiting unavailable\n            time), then the object's value also decreases.\n\n            Note that this TC is not strictly supported in SMIv2,\n            because the 'always increasing' and 'counter wrap'\n            semantics associated with the Counter64 base type are not\n            preserved.  It is possible that management applications\n            which rely solely upon the (Counter64) ASN.1 tag to\n            determine object semantics will mistakenly operate upon\n            objects of this type as they would for Counter64 objects.\n\n            This textual convention represents a limited and short-\n            term solution, and may be deprecated as a long term\n            solution is defined and deployed to replace it."
    status = 'current'

class HCPerfIntervalCount(TextualConvention, Counter64):
    description = "A gauge associated with a performance measurement in\n            a previous 15 minute measurement interval.  In the case\n            where the agent has no valid data available for a\n            particular interval, the corresponding object instance is\n            not available and upon a retrieval request a corresponding\n            error message shall be returned to indicate that this\n            instance does not exist.\n\n            Let X be an object with HCPerfIntervalCount syntax.\n            Let Y be an object with HCPerfCurrentCount syntax.\n            Let Z be an object with HCPerfTotalCount syntax.\n            Then, in a system supporting a history of n intervals with\n            X(1) and X(n) the most and least recent intervals\n            respectively, the following applies at the end of a 15\n            minute interval:\n\n               - discard the value of X(n)\n               - the value of X(i) becomes that of X(i-1)\n                 for n >= i > 1\n               - the value of X(1) becomes that of Y.\n               - the value of Z, if supported, is adjusted.\n\n            This count represents a non-negative integer, which\n            may increase or decrease, but shall never exceed 2^64-1\n            (18446744073709551615 decimal), nor fall below 0.  The\n            value of an object with HCPerfIntervalCount syntax\n            assumes its maximum value whenever the underlying count\n            exceeds 2^64-1.  If the underlying count subsequently\n            decreases below 2^64-1 (due, e.g., to a retroactive\n            adjustment as a result of entering or exiting unavailable\n            time), then the value of the object also decreases.\n\n            Note that this TC is not strictly supported in SMIv2,\n            because the 'always increasing' and 'counter wrap'\n            semantics associated with the Counter64 base type are not\n            preserved.  It is possible that management applications\n            which rely solely upon the (Counter64) ASN.1 tag to\n            determine object semantics will mistakenly operate upon\n            objects of this type as they would for Counter64 objects.\n\n            This textual convention represents a limited and short-\n            term solution, and may be deprecated as a long term\n            solution is defined and deployed to replace it."
    status = 'current'

class HCPerfTotalCount(TextualConvention, Counter64):
    description = "A gauge representing the aggregate of previous valid 15\n            minute measurement intervals.  Intervals for which no\n            valid data was available are not counted.\n\n            This count represents a non-negative integer, which\n            may increase or decrease, but shall never exceed 2^64-1\n            (18446744073709551615 decimal), nor fall below 0.  The\n            value of an object with HCPerfTotalCount syntax\n            assumes its maximum value whenever the underlying count\n            exceeds 2^64-1.  If the underlying count subsequently\n            decreases below 2^64-1 (due, e.g., to a retroactive\n            adjustment as a result of entering or exiting unavailable\n            time), then the object's value also decreases.\n\n            Note that this TC is not strictly supported in SMIv2,\n            because the 'always increasing' and 'counter wrap'\n            semantics associated with the Counter64 base type are not\n            preserved.  It is possible that management applications\n            which rely solely upon the (Counter64) ASN.1 tag to\n            determine object semantics will mistakenly operate upon\n            objects of this type as they would for Counter64 objects.\n\n            This textual convention represents a limited and short-\n            term solution, and may be deprecated as a long term\n            solution is defined and deployed to replace it."
    status = 'current'

mibBuilder.exportSymbols("HC-PerfHist-TC-MIB", hcPerfHistTCMIB=hcPerfHistTCMIB, HCPerfInvalidIntervals=HCPerfInvalidIntervals, HCPerfTimeElapsed=HCPerfTimeElapsed, HCPerfTotalCount=HCPerfTotalCount, HCPerfIntervalCount=HCPerfIntervalCount, PYSNMP_MODULE_ID=hcPerfHistTCMIB, HCPerfValidIntervals=HCPerfValidIntervals, HCPerfCurrentCount=HCPerfCurrentCount, HCPerfIntervalThreshold=HCPerfIntervalThreshold)
