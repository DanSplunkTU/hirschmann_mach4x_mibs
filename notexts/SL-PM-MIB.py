#
# PySNMP MIB module SL-PM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-PM-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:42:23 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PerfIntervalCount, PerfTotalCount, PerfCurrentCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfIntervalCount", "PerfTotalCount", "PerfCurrentCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
XpdrServiceType, = mibBuilder.importSymbols("SL-XPDR-MIB", "XpdrServiceType")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, transmission, Integer32, Counter64, ModuleIdentity, IpAddress, NotificationType, MibIdentifier, Gauge32, Counter32, ObjectIdentity, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "transmission", "Integer32", "Counter64", "ModuleIdentity", "IpAddress", "NotificationType", "MibIdentifier", "Gauge32", "Counter32", "ObjectIdentity", "TimeTicks", "iso")
DisplayString, DateAndTime, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "DateAndTime", "TextualConvention", "TruthValue")
slPmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25))
if mibBuilder.loadTexts: slPmMib.setLastUpdated('201105170000Z')
if mibBuilder.loadTexts: slPmMib.setOrganization('PacketLight Networks Ltd.')
class SlPmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("native", 1))

class SlPmL2Type(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("rxPackets", 1), ("txPackets", 2), ("rxBytes", 3), ("txBytes", 4), ("rxCrc", 5), ("txCrc", 6))

class SlPmDirectionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("near", 1), ("far", 2))

class SlPmIntervalType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fifteen", 1), ("day", 2))

slPmIntervals = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1))
slPmL2Intervals = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2))
slPmIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1), )
if mibBuilder.loadTexts: slPmIntervalTable.setStatus('current')
slPmIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SL-PM-MIB", "slPmType"), (0, "SL-PM-MIB", "slPmDirectionType"), (0, "SL-PM-MIB", "slPmIntervalType"), (0, "SL-PM-MIB", "slPmIntervalNumber"))
if mibBuilder.loadTexts: slPmIntervalEntry.setStatus('current')
slPmType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 1), SlPmType())
if mibBuilder.loadTexts: slPmType.setStatus('current')
slPmDirectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 2), SlPmDirectionType())
if mibBuilder.loadTexts: slPmDirectionType.setStatus('current')
slPmIntervalType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 3), SlPmIntervalType())
if mibBuilder.loadTexts: slPmIntervalType.setStatus('current')
slPmIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96)))
if mibBuilder.loadTexts: slPmIntervalNumber.setStatus('current')
slPmIntervalCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalCVs.setStatus('current')
slPmIntervalESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 6), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalESs.setStatus('current')
slPmIntervalSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 7), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalSESs.setStatus('current')
slPmIntervalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 8), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalSEFSs.setStatus('current')
slPmIntervalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 9), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalUASs.setStatus('current')
slPmIntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalValidData.setStatus('current')
slPmIntervalTcaFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalTcaFlag.setStatus('current')
slPmIntervalReset = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slPmIntervalReset.setStatus('current')
slPmIntervalStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 13), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalStartTime.setStatus('current')
slPmServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 14), XpdrServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmServiceType.setStatus('current')
slPmL2Table = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1), )
if mibBuilder.loadTexts: slPmL2Table.setStatus('current')
slPmL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SL-PM-MIB", "slPmL2CounterType"), (0, "SL-PM-MIB", "slPmL2IntervalType"), (0, "SL-PM-MIB", "slPmL2IntervalNumber"))
if mibBuilder.loadTexts: slPmL2Entry.setStatus('current')
slPmL2CounterType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 1), SlPmL2Type())
if mibBuilder.loadTexts: slPmL2CounterType.setStatus('current')
slPmL2IntervalType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 2), SlPmIntervalType())
if mibBuilder.loadTexts: slPmL2IntervalType.setStatus('current')
slPmL2IntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96)))
if mibBuilder.loadTexts: slPmL2IntervalNumber.setStatus('current')
slPmL2Count = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmL2Count.setStatus('current')
slPmL2ValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmL2ValidData.setStatus('current')
slPmL2Reset = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slPmL2Reset.setStatus('current')
slPmL2StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmL2StartTime.setStatus('current')
slPmL2ServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 8), XpdrServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmL2ServiceType.setStatus('current')
mibBuilder.exportSymbols("SL-PM-MIB", SlPmL2Type=SlPmL2Type, slPmMib=slPmMib, slPmL2StartTime=slPmL2StartTime, slPmL2Intervals=slPmL2Intervals, slPmIntervalTcaFlag=slPmIntervalTcaFlag, PYSNMP_MODULE_ID=slPmMib, slPmL2ValidData=slPmL2ValidData, slPmIntervalReset=slPmIntervalReset, slPmL2CounterType=slPmL2CounterType, slPmL2Entry=slPmL2Entry, slPmIntervals=slPmIntervals, slPmIntervalESs=slPmIntervalESs, slPmIntervalSEFSs=slPmIntervalSEFSs, slPmL2IntervalNumber=slPmL2IntervalNumber, slPmL2Table=slPmL2Table, slPmIntervalTable=slPmIntervalTable, slPmIntervalEntry=slPmIntervalEntry, slPmIntervalType=slPmIntervalType, slPmIntervalStartTime=slPmIntervalStartTime, slPmServiceType=slPmServiceType, slPmIntervalUASs=slPmIntervalUASs, slPmL2Reset=slPmL2Reset, slPmDirectionType=slPmDirectionType, SlPmDirectionType=SlPmDirectionType, SlPmIntervalType=SlPmIntervalType, slPmIntervalValidData=slPmIntervalValidData, slPmL2IntervalType=slPmL2IntervalType, slPmIntervalSESs=slPmIntervalSESs, slPmType=slPmType, SlPmType=SlPmType, slPmL2ServiceType=slPmL2ServiceType, slPmIntervalCVs=slPmIntervalCVs, slPmL2Count=slPmL2Count, slPmIntervalNumber=slPmIntervalNumber)
