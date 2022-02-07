#
# PySNMP MIB module SL-PM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-PM-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:17:48 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
XpdrServiceType, = mibBuilder.importSymbols("SL-XPDR-MIB", "XpdrServiceType")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, MibIdentifier, TimeTicks, ObjectIdentity, Unsigned32, IpAddress, Counter32, Gauge32, Counter64, Integer32, transmission, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "MibIdentifier", "TimeTicks", "ObjectIdentity", "Unsigned32", "IpAddress", "Counter32", "Gauge32", "Counter64", "Integer32", "transmission", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "NotificationType")
DateAndTime, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TruthValue", "TextualConvention")
slPmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25))
if mibBuilder.loadTexts: slPmMib.setLastUpdated('201105170000Z')
if mibBuilder.loadTexts: slPmMib.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slPmMib.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slPmMib.setDescription('This PM module ')
class SlPmType(TextualConvention, Integer32):
    description = 'The PM types:\n        \tNative types:\n        \tGBE \t- ifType=117, Path=0 \n        \tFC  \t- ifType=56,  Path=0 \n        \tSONET \t- ifType=39,  Path=0 \n        \tOTU\t\t- ifType=195, Path=0 \n        \tODU\t\t- ifType=195, Path=1..4 \n        \tFEC\t\t- ifType=195, Path=5..6\n        \tOPT\t\t- ifType=196, Path=0'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("native", 1))

class SlPmL2Type(TextualConvention, Integer32):
    description = 'The PM types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("rxPackets", 1), ("txPackets", 2), ("rxBytes", 3), ("txBytes", 4), ("rxCrc", 5), ("txCrc", 6))

class SlPmDirectionType(TextualConvention, Integer32):
    description = 'The PM direction type.\n       This relevant only to OTU or ODU types'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("near", 1), ("far", 2))

class SlPmIntervalType(TextualConvention, Integer32):
    description = 'The PM interval types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("fifteen", 1), ("day", 2))

slPmIntervals = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1))
slPmL2Intervals = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2))
slPmIntervalTable = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1), )
if mibBuilder.loadTexts: slPmIntervalTable.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalTable.setDescription('The PM Interval table.')
slPmIntervalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SL-PM-MIB", "slPmType"), (0, "SL-PM-MIB", "slPmDirectionType"), (0, "SL-PM-MIB", "slPmIntervalType"), (0, "SL-PM-MIB", "slPmIntervalNumber"))
if mibBuilder.loadTexts: slPmIntervalEntry.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalEntry.setDescription('An entry in the PM Interval table.')
slPmType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 1), SlPmType())
if mibBuilder.loadTexts: slPmType.setStatus('current')
if mibBuilder.loadTexts: slPmType.setDescription('The PM type')
slPmDirectionType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 2), SlPmDirectionType())
if mibBuilder.loadTexts: slPmDirectionType.setStatus('current')
if mibBuilder.loadTexts: slPmDirectionType.setDescription('The PM direction near-end/far-end.')
slPmIntervalType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 3), SlPmIntervalType())
if mibBuilder.loadTexts: slPmIntervalType.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalType.setDescription('The type of the PM interval 15min/day')
slPmIntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96)))
if mibBuilder.loadTexts: slPmIntervalNumber.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalNumber.setDescription('A number between 1 to 96, which identifies the\n      interval for which the set of statistics is available.\n      The interval identified by 1 is the most recently\n      completed 15 minute interval,\n      and the interval identified\n      by N is the interval immediately preceding the\n      one identified\n      by N-1.')
slPmIntervalCVs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 5), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalCVs.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalCVs.setDescription('The counter associated with the number of Coding\n       Violations encountered in a particular 15-minute interval\n       in the past 24 hours.')
slPmIntervalESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 6), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalESs.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalESs.setDescription('The counter associated with the number of\n       Errored Seconds encountered\n       in a particular 15-minute interval\n       in the past 24 hours.')
slPmIntervalSESs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 7), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalSESs.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalSESs.setDescription('The counter associated with the number of\n       Severely Errored Seconds encountered in a\n       particular 15-minute interval in the past 24 hours.')
slPmIntervalSEFSs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 8), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalSEFSs.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalSEFSs.setDescription('The counter associated with the number of\n       Severely Errored Framing Seconds\n       encountered in a particular 15-minute interval\n       in the past 24 hours.')
slPmIntervalUASs = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 9), PerfIntervalCount()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalUASs.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalUASs.setDescription('The counter associated with the number of\n       Unavailable Seconds encountered in a particular 15-minute interval\n       in the past 24 hours.')
slPmIntervalValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 10), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalValidData.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalValidData.setDescription('This variable indicates if the data for this interval is valid.')
slPmIntervalTcaFlag = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalTcaFlag.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalTcaFlag.setDescription('TRUE if one of the counters crossed the threshold during the 15 minutes interval.')
slPmIntervalReset = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 12), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slPmIntervalReset.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalReset.setDescription('Writing to this object reset the PM counters in this interval.')
slPmIntervalStartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 13), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmIntervalStartTime.setReference('ANSI T1.231-1997 clause 9.1.5.1.')
if mibBuilder.loadTexts: slPmIntervalStartTime.setStatus('current')
if mibBuilder.loadTexts: slPmIntervalStartTime.setDescription('This variable indicates the date and time at which this \n        interval of measurements began on this interface.')
slPmServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 1, 1, 1, 14), XpdrServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmServiceType.setStatus('current')
if mibBuilder.loadTexts: slPmServiceType.setDescription('This variable indicates the XPDR service type of the port \n         during the PM interval.')
slPmL2Table = MibTable((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1), )
if mibBuilder.loadTexts: slPmL2Table.setStatus('current')
if mibBuilder.loadTexts: slPmL2Table.setDescription('The Layer 2 PM table.')
slPmL2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "SL-PM-MIB", "slPmL2CounterType"), (0, "SL-PM-MIB", "slPmL2IntervalType"), (0, "SL-PM-MIB", "slPmL2IntervalNumber"))
if mibBuilder.loadTexts: slPmL2Entry.setStatus('current')
if mibBuilder.loadTexts: slPmL2Entry.setDescription('An entry in the Layer 2 PM table.')
slPmL2CounterType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 1), SlPmL2Type())
if mibBuilder.loadTexts: slPmL2CounterType.setStatus('current')
if mibBuilder.loadTexts: slPmL2CounterType.setDescription('The PM Layer 2 counter type')
slPmL2IntervalType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 2), SlPmIntervalType())
if mibBuilder.loadTexts: slPmL2IntervalType.setStatus('current')
if mibBuilder.loadTexts: slPmL2IntervalType.setDescription('The type of the PM interval 15min/day')
slPmL2IntervalNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 96)))
if mibBuilder.loadTexts: slPmL2IntervalNumber.setStatus('current')
if mibBuilder.loadTexts: slPmL2IntervalNumber.setDescription('A number between 1 to 96, which identifies the\n      interval for which the set of statistics is available.\n      The interval identified by 1 is the most recently\n      completed 15 minute interval,\n      and the interval identified\n      by N is the interval immediately preceding the\n      one identified\n      by N-1.')
slPmL2Count = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmL2Count.setStatus('current')
if mibBuilder.loadTexts: slPmL2Count.setDescription('The counter associated with the number of Coding\n       Violations encountered in a particular 15-minute interval\n       in the past 24 hours.')
slPmL2ValidData = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmL2ValidData.setStatus('current')
if mibBuilder.loadTexts: slPmL2ValidData.setDescription('This variable indicates if the data for this interval is valid.')
slPmL2Reset = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slPmL2Reset.setStatus('current')
if mibBuilder.loadTexts: slPmL2Reset.setDescription('Writing to this object reset the PM counters in this interval.')
slPmL2StartTime = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 7), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmL2StartTime.setReference('ANSI T1.231-1997 clause 9.1.5.1.')
if mibBuilder.loadTexts: slPmL2StartTime.setStatus('current')
if mibBuilder.loadTexts: slPmL2StartTime.setDescription('This variable indicates the date and time at which this \n        interval of measurements began on this interface.')
slPmL2ServiceType = MibTableColumn((1, 3, 6, 1, 4, 1, 4515, 1, 3, 25, 2, 1, 1, 8), XpdrServiceType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: slPmL2ServiceType.setStatus('current')
if mibBuilder.loadTexts: slPmL2ServiceType.setDescription('This variable indicates the XPDR service type of the port \n         during the PM interval.')
mibBuilder.exportSymbols("SL-PM-MIB", slPmL2StartTime=slPmL2StartTime, slPmIntervalTcaFlag=slPmIntervalTcaFlag, SlPmType=SlPmType, slPmIntervalEntry=slPmIntervalEntry, slPmType=slPmType, slPmIntervalCVs=slPmIntervalCVs, slPmIntervalUASs=slPmIntervalUASs, slPmIntervals=slPmIntervals, slPmL2IntervalNumber=slPmL2IntervalNumber, slPmIntervalValidData=slPmIntervalValidData, slPmIntervalType=slPmIntervalType, slPmIntervalSEFSs=slPmIntervalSEFSs, slPmIntervalStartTime=slPmIntervalStartTime, slPmL2Reset=slPmL2Reset, slPmL2IntervalType=slPmL2IntervalType, slPmL2ValidData=slPmL2ValidData, slPmServiceType=slPmServiceType, slPmIntervalReset=slPmIntervalReset, slPmL2Entry=slPmL2Entry, SlPmDirectionType=SlPmDirectionType, slPmIntervalTable=slPmIntervalTable, slPmL2ServiceType=slPmL2ServiceType, slPmIntervalESs=slPmIntervalESs, slPmL2Count=slPmL2Count, slPmDirectionType=slPmDirectionType, slPmMib=slPmMib, SlPmIntervalType=SlPmIntervalType, PYSNMP_MODULE_ID=slPmMib, slPmL2Table=slPmL2Table, slPmL2CounterType=slPmL2CounterType, SlPmL2Type=SlPmL2Type, slPmIntervalSESs=slPmIntervalSESs, slPmL2Intervals=slPmL2Intervals, slPmIntervalNumber=slPmIntervalNumber)
