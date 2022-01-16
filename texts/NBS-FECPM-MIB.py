#
# PySNMP MIB module NBS-FECPM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mrv/NBS-FECPM-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:41:04 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
InterfaceIndex, ifAlias = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex", "ifAlias")
WritableU64, nbs = mibBuilder.importSymbols("NBS-MIB", "WritableU64", "nbs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, ModuleIdentity, ObjectIdentity, Counter32, iso, Unsigned32, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Gauge32, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "ObjectIdentity", "Counter32", "iso", "Unsigned32", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Gauge32", "Integer32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
nbsFecpmMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 629, 223))
if mibBuilder.loadTexts: nbsFecpmMib.setLastUpdated('201610190000Z')
if mibBuilder.loadTexts: nbsFecpmMib.setOrganization('NBS')
if mibBuilder.loadTexts: nbsFecpmMib.setContactInfo('For technical support, please contact your service channel')
if mibBuilder.loadTexts: nbsFecpmMib.setDescription('OTN Forward Error Correction (FEC) Performance Monitoring and\n        user-controlled statistics')
nbsFecpmThresholdsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 1))
if mibBuilder.loadTexts: nbsFecpmThresholdsGrp.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmThresholdsGrp.setDescription('Maximum considered safe by user')
nbsFecpmCurrentGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 2))
if mibBuilder.loadTexts: nbsFecpmCurrentGrp.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentGrp.setDescription('Subtotals and statistics for sample now underway')
nbsFecpmHistoricGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 3))
if mibBuilder.loadTexts: nbsFecpmHistoricGrp.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricGrp.setDescription('Totals and final statistics for a previous sample')
nbsFecpmRunningGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 4))
if mibBuilder.loadTexts: nbsFecpmRunningGrp.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningGrp.setDescription('Counter values since boot-up')
nbsFecStatsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 90))
if mibBuilder.loadTexts: nbsFecStatsGrp.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsGrp.setDescription('User-controlled statistics')
nbsFecpmEventsGrp = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 100))
if mibBuilder.loadTexts: nbsFecpmEventsGrp.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmEventsGrp.setDescription('Threshold crossing events')
nbsFecpmTraps = ObjectIdentity((1, 3, 6, 1, 4, 1, 629, 223, 100, 0))
if mibBuilder.loadTexts: nbsFecpmTraps.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmTraps.setDescription('Threshold crossing Traps or Notifications')
nbsFecpmThresholdsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 223, 1, 1), )
if mibBuilder.loadTexts: nbsFecpmThresholdsTable.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmThresholdsTable.setDescription('FEC Performance Monitoring thresholds')
nbsFecpmThresholdsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1), ).setIndexNames((0, "NBS-FECPM-MIB", "nbsFecpmThresholdsIfIndex"), (0, "NBS-FECPM-MIB", "nbsFecpmThresholdsInterval"))
if mibBuilder.loadTexts: nbsFecpmThresholdsEntry.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmThresholdsEntry.setDescription('Performance monitoring thresholds for a particular interface')
nbsFecpmThresholdsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmThresholdsIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmThresholdsIfIndex.setDescription('The mib2 ifIndex')
nbsFecpmThresholdsInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("quarterHour", 1), ("twentyfourHour", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmThresholdsInterval.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmThresholdsInterval.setDescription('Indicates the periodicity to which these thresholds apply')
nbsFecpmThresholdsBitErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 10), WritableU64()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecpmThresholdsBitErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmThresholdsBitErrCor.setDescription('Persistent.  The number of Bit Errors Corrected which, if met\n        or exceeded at the end of the nbsFecpmThresholdsInterval\n        period, should trigger the nbsFecpmTrapsBitErrCor event\n        notification.\n\n        The reserved value 0 disables notifications for this event.')
nbsFecpmThresholdsByteErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 12), WritableU64()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecpmThresholdsByteErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmThresholdsByteErrCor.setDescription('Persistent.  The number of Byte Errors Corrected\n        which, if met or exceeded at the end of the\n        nbsFecpmThresholdsInterval period, should trigger the\n        nbsFecpmTrapsByteErrCor event notification.\n\n        The reserved value 0 disables notifications for this event.')
nbsFecpmThresholdsCorBit0to1 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 14), WritableU64()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecpmThresholdsCorBit0to1.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmThresholdsCorBit0to1.setDescription("Persistent.  The number of '0' bits corrected to '1' which,\n        if met or exceeded at the end of the nbsFecpmThresholdsInterval\n        period, should trigger the nbsFecpmTrapsCorBit0to1 event\n        notification.\n\n        The reserved value 0 disables notifications for this event.")
nbsFecpmThresholdsCorBit1to0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 16), WritableU64()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecpmThresholdsCorBit1to0.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmThresholdsCorBit1to0.setDescription("Persistent.  The number of '1' bits corrected to '0' which,\n        if met or exceeded at the end of the nbsFecpmThresholdsInterval\n        period, should trigger the nbsFecpmTrapsCorBit1to0 event\n        notification.\n\n        The reserved value 0 disables notifications for this event.")
nbsFecpmThresholdsUncorWords = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 1, 1, 1, 18), WritableU64()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecpmThresholdsUncorWords.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmThresholdsUncorWords.setDescription('Persistent.  The number of Uncorrectable Words which, if met or\n        exceeded at the end of the nbsFecpmThresholdsInterval period,\n        should trigger the nbsFecpmTrapsUncorWords event notification.\n\n        The reserved value 0 disables notifications for this event.')
nbsFecpmCurrentSysDate = MibScalar((1, 3, 6, 1, 4, 1, 629, 223, 2, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentSysDate.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentSysDate.setDescription("The current (today's) UTC date, represented by an eight\n        digit decimal number: yyyymmdd")
nbsFecpmCurrentSysTime = MibScalar((1, 3, 6, 1, 4, 1, 629, 223, 2, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentSysTime.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentSysTime.setDescription("The current (now's) UTC time, represented by a six\n        digit decimal number in the format hhmmss")
nbsFecpmCurrentTable = MibTable((1, 3, 6, 1, 4, 1, 629, 223, 2, 3), )
if mibBuilder.loadTexts: nbsFecpmCurrentTable.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentTable.setDescription('All FEC Performance Monitoring statistics for the\n        nbsFecpmCurrentInterval now underway.')
nbsFecpmCurrentEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1), ).setIndexNames((0, "NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), (0, "NBS-FECPM-MIB", "nbsFecpmCurrentInterval"))
if mibBuilder.loadTexts: nbsFecpmCurrentEntry.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentEntry.setDescription('FEC Performance Monitoring statistics for a specific port/\n        interface and nbsFecpmCurrentInterval.')
nbsFecpmCurrentIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentIfIndex.setDescription('The mib2 ifIndex')
nbsFecpmCurrentInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("quarterHour", 1), ("twentyfourHour", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentInterval.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentInterval.setDescription('Indicates the periodicity of statistic')
nbsFecpmCurrentDate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentDate.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentDate.setDescription('The date (UTC) this interval began, represented by an eight\n        digit decimal number: yyyymmdd')
nbsFecpmCurrentTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentTime.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentTime.setDescription('The time (UTC) this interval began, represented by a six\n        digit decimal number: hhmmss')
nbsFecpmCurrentBitErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentBitErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentBitErrCor.setDescription('The number of Bit Errors Corrected in this interval so far;\n        it may be the sum of nbsFecpmCurrentCorBit0to1 and\n        nbsFecpmCurrentCorBit1to0.')
nbsFecpmCurrentByteErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentByteErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentByteErrCor.setDescription('The number of Byte Errors Corrected in this interval so far.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates not supported.')
nbsFecpmCurrentCorBit0to1 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentCorBit0to1.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentCorBit0to1.setDescription("The number of '0' bits corrected to '1' so far.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates there is a\n        single number for all bit corrections combined, see\n        nbsFecpmCurrentBitErrCor.")
nbsFecpmCurrentCorBit1to0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentCorBit1to0.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentCorBit1to0.setDescription("The number of '1' bits corrected to '0' so far.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates there is a\n        single number for all bit corrections combined, see\n        nbsFecpmCurrentBitErrCor.")
nbsFecpmCurrentUncorWords = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 2, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmCurrentUncorWords.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmCurrentUncorWords.setDescription('The number of Uncorrectable Words so far')
nbsFecpmHistoricTable = MibTable((1, 3, 6, 1, 4, 1, 629, 223, 3, 3), )
if mibBuilder.loadTexts: nbsFecpmHistoricTable.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricTable.setDescription('All FEC Performance Monitoring statistics for past\n        nbsFecpmHistoricInterval periods.')
nbsFecpmHistoricEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1), ).setIndexNames((0, "NBS-FECPM-MIB", "nbsFecpmHistoricIfIndex"), (0, "NBS-FECPM-MIB", "nbsFecpmHistoricInterval"), (0, "NBS-FECPM-MIB", "nbsFecpmHistoricSample"))
if mibBuilder.loadTexts: nbsFecpmHistoricEntry.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricEntry.setDescription('FEC Performance Monitoring statistics for a specific port/\n        interface and nbsFecpmHistoricInterval.')
nbsFecpmHistoricIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricIfIndex.setDescription('The mib2 ifIndex')
nbsFecpmHistoricInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("quarterHour", 1), ("twentyfourHour", 2))))
if mibBuilder.loadTexts: nbsFecpmHistoricInterval.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricInterval.setDescription('Indicates the sampling period of statistic')
nbsFecpmHistoricSample = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 4), Integer32())
if mibBuilder.loadTexts: nbsFecpmHistoricSample.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricSample.setDescription('Indicates the sample number of this statistic.  The most\n        recent sample is numbered 1, the next previous 2, and so on\n        until the oldest sample.')
nbsFecpmHistoricDate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricDate.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricDate.setDescription('The date (UTC) the interval began, represented by an eight\n        digit decimal number: yyyymmdd')
nbsFecpmHistoricTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricTime.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricTime.setDescription('The time (UTC) the interval began, represented by a six\n        digit decimal number: hhmmss')
nbsFecpmHistoricBitErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricBitErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricBitErrCor.setDescription('The final count of Bit Errors Corrected for this interval;\n        it may be the sum of nbsFecpmHistoricCorBit0to1 and\n        nbsFecpmHistoricCorBit1to0.')
nbsFecpmHistoricByteErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricByteErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricByteErrCor.setDescription('The final count of Byte Errors Corrected in this interval.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates not supported.')
nbsFecpmHistoricCorBit0to1 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricCorBit0to1.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricCorBit0to1.setDescription("The final count of '0' bits corrected to '1' in this interval.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates there is a\n        single number for all bit corrections combined, see\n        nbsFecpmHistoricBitErrCor.")
nbsFecpmHistoricCorBit1to0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricCorBit1to0.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricCorBit1to0.setDescription("The final count of '1' bits corrected to '0' in this interval.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates there is a\n        single number for all bit corrections combined, see\n        nbsFecpmHistoricBitErrCor.")
nbsFecpmHistoricUncorWords = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 3, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmHistoricUncorWords.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmHistoricUncorWords.setDescription('The final number of Uncorrectable Words in this interval')
nbsFecpmRunningTable = MibTable((1, 3, 6, 1, 4, 1, 629, 223, 4, 3), )
if mibBuilder.loadTexts: nbsFecpmRunningTable.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningTable.setDescription('All FEC Performance Monitoring statistics since boot-up.')
nbsFecpmRunningEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1), ).setIndexNames((0, "NBS-FECPM-MIB", "nbsFecpmRunningIfIndex"))
if mibBuilder.loadTexts: nbsFecpmRunningEntry.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningEntry.setDescription('FEC Performance Monitoring statistics for a specific port/\n         interface.')
nbsFecpmRunningIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningIfIndex.setDescription('The mib2 ifIndex')
nbsFecpmRunningDate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningDate.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningDate.setDescription('The date (UTC) of boot-up, represented by an eight digit\n        decimal number: yyyymmdd')
nbsFecpmRunningTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningTime.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningTime.setDescription('The time (UTC) of boot-up, represented by a six digit\n        decimal number: hhmmss')
nbsFecpmRunningBitErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningBitErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningBitErrCor.setDescription('The total count of Bit Errors Corrected since boot-up;\n        it may be the sum of nbsFecpmRunningCorBit0to1 and\n        nbsFecpmRunningCorBit1to0.')
nbsFecpmRunningByteErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningByteErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningByteErrCor.setDescription('The total count of Byte Errors Corrected since boot-up.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates not supported.')
nbsFecpmRunningCorBit0to1 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningCorBit0to1.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningCorBit0to1.setDescription("The total count of '0' bits corrected to '1' since boot-up.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates there is a\n        single number for all bit corrections combined, see\n        nbsFecpmRunningBitErrCor.")
nbsFecpmRunningCorBit1to0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningCorBit1to0.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningCorBit1to0.setDescription("The total count of '1' bits corrected to '0' since boot-up.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates there is a\n        single number for all bit corrections combined, see\n        nbsFecpmRunningBitErrCor.")
nbsFecpmRunningUncorWords = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 4, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecpmRunningUncorWords.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmRunningUncorWords.setDescription('The total number of Uncorrectable Words since boot-up')
nbsFecStatsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 223, 90, 3), )
if mibBuilder.loadTexts: nbsFecStatsTable.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsTable.setDescription("FEC statistics managed at the user's discretion. These statistics\n        may be started, stopped, and cleared whenever the user desires\n        without affecting the normal performance monitoring activity.")
nbsFecStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1), ).setIndexNames((0, "NBS-FECPM-MIB", "nbsFecStatsIfIndex"))
if mibBuilder.loadTexts: nbsFecStatsEntry.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsEntry.setDescription('User-controlled FEC statistics for a specific port/interface.')
nbsFecStatsIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 1), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsIfIndex.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsIfIndex.setDescription('The mib2 ifIndex')
nbsFecStatsDate = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsDate.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsDate.setDescription('The (UTC) date the user began statistics collection, represented\n        by an eight digit decimal number: yyyymmdd')
nbsFecStatsTime = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsTime.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsTime.setDescription('The (UTC) time the user began statistics collection, represented\n        by a six digit decimal number: hhmmss')
nbsFecStatsSpan = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsSpan.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsSpan.setDescription('The amount of time (deci-sec) statistics collection has been underway\n        since nbsFecStatsDate and nbsFecStatsTime, or if stopped, the duration\n        of the prior collection.')
nbsFecStatsState = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("notSupported", 1), ("counting", 2), ("clearing", 3), ("stopped", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbsFecStatsState.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsState.setDescription("Writing 'stopped' to this object stops (pauses) FEC statistics\n        collection.\n\n        Writing 'counting' to this object starts (resumes) FEC statistics\n        collection.\n\n        Writing 'clearing' to this object clears all statistical counters.")
nbsFecStatsBitErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsBitErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsBitErrCor.setDescription('The total count of Bit Errors Corrected since boot-up;\n        it may be the sum of nbsFecStatsCorBit0to1 and\n        nbsFecStatsCorBit1to0.')
nbsFecStatsByteErrCor = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsByteErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsByteErrCor.setDescription('The total count of Byte Errors Corrected since boot-up.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates not supported.')
nbsFecStatsCorBit0to1 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsCorBit0to1.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsCorBit0to1.setDescription("The total count of '0' bits corrected to '1' since boot-up.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates there is a\n        single number for all bit corrections combined, see\n        nbsFecStatsBitErrCor.")
nbsFecStatsCorBit1to0 = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsCorBit1to0.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsCorBit1to0.setDescription("The total count of '1' bits corrected to '0' since boot-up.\n        The reserved value 0xFFFFFFFFFFFFFFFF indicates there is a\n        single number for all bit corrections combined, see\n        nbsFecStatsBitErrCor.")
nbsFecStatsUncorWords = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 223, 90, 3, 1, 18), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbsFecStatsUncorWords.setStatus('current')
if mibBuilder.loadTexts: nbsFecStatsUncorWords.setDescription('The total number of Uncorrectable Words since boot-up')
nbsFecpmTrapsBitErrCor = NotificationType((1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 10)).setObjects(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"), ("NBS-FECPM-MIB", "nbsFecpmCurrentBitErrCor"))
if mibBuilder.loadTexts: nbsFecpmTrapsBitErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmTrapsBitErrCor.setDescription('Sent at the conclusion of an nbsFecpmThresholdsInterval if\n        nbsFecpmThresholdsBitErrCor is non-zero and less than or equal\n        to nbsFecpmCurrentBitErrCor.')
nbsFecpmTrapsByteErrCor = NotificationType((1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 12)).setObjects(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"), ("NBS-FECPM-MIB", "nbsFecpmCurrentByteErrCor"))
if mibBuilder.loadTexts: nbsFecpmTrapsByteErrCor.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmTrapsByteErrCor.setDescription('Sent at the conclusion of an nbsFecpmThresholdsInterval if\n        nbsFecpmThresholdsByteErrCor is non-zero and less than or equal\n        to nbsFecpmCurrentByteErrCor.')
nbsFecpmTrapsCorBit0to1 = NotificationType((1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 14)).setObjects(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"), ("NBS-FECPM-MIB", "nbsFecpmCurrentCorBit0to1"))
if mibBuilder.loadTexts: nbsFecpmTrapsCorBit0to1.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmTrapsCorBit0to1.setDescription('Sent at the conclusion of an nbsFecpmThresholdsInterval if\n        nbsFecpmThresholdsCorBit0to1 is non-zero and less than or equal\n        to nbsFecpmCurrentCorBit0to1.')
nbsFecpmTrapsCorBit1to0 = NotificationType((1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 16)).setObjects(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"), ("NBS-FECPM-MIB", "nbsFecpmCurrentCorBit1to0"))
if mibBuilder.loadTexts: nbsFecpmTrapsCorBit1to0.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmTrapsCorBit1to0.setDescription('Sent at the conclusion of an nbsFecpmThresholdsInterval if\n        nbsFecpmThresholdsCorBit1to0 is non-zero and less than or equal\n        to nbsFecpmCurrentCorBit1to0.')
nbsFecpmTrapsUncorWords = NotificationType((1, 3, 6, 1, 4, 1, 629, 223, 100, 0, 18)).setObjects(("NBS-FECPM-MIB", "nbsFecpmCurrentIfIndex"), ("IF-MIB", "ifAlias"), ("NBS-FECPM-MIB", "nbsFecpmCurrentInterval"), ("NBS-FECPM-MIB", "nbsFecpmCurrentUncorWords"))
if mibBuilder.loadTexts: nbsFecpmTrapsUncorWords.setStatus('current')
if mibBuilder.loadTexts: nbsFecpmTrapsUncorWords.setDescription('Sent at the conclusion of an nbsFecpmThresholdsInterval if\n        nbsFecpmThresholdsUncorWords is non-zero and less than or equal\n        to nbsFecpmCurrentUncorWords.')
mibBuilder.exportSymbols("NBS-FECPM-MIB", nbsFecStatsSpan=nbsFecStatsSpan, nbsFecpmHistoricGrp=nbsFecpmHistoricGrp, nbsFecpmRunningEntry=nbsFecpmRunningEntry, nbsFecpmHistoricCorBit1to0=nbsFecpmHistoricCorBit1to0, nbsFecpmCurrentBitErrCor=nbsFecpmCurrentBitErrCor, nbsFecpmHistoricByteErrCor=nbsFecpmHistoricByteErrCor, nbsFecStatsTime=nbsFecStatsTime, nbsFecpmHistoricInterval=nbsFecpmHistoricInterval, nbsFecpmCurrentSysDate=nbsFecpmCurrentSysDate, nbsFecpmThresholdsInterval=nbsFecpmThresholdsInterval, nbsFecpmCurrentCorBit1to0=nbsFecpmCurrentCorBit1to0, nbsFecStatsEntry=nbsFecStatsEntry, nbsFecpmHistoricCorBit0to1=nbsFecpmHistoricCorBit0to1, nbsFecpmRunningGrp=nbsFecpmRunningGrp, nbsFecpmEventsGrp=nbsFecpmEventsGrp, nbsFecpmCurrentSysTime=nbsFecpmCurrentSysTime, nbsFecStatsCorBit0to1=nbsFecStatsCorBit0to1, nbsFecpmCurrentCorBit0to1=nbsFecpmCurrentCorBit0to1, nbsFecpmThresholdsUncorWords=nbsFecpmThresholdsUncorWords, nbsFecStatsState=nbsFecStatsState, nbsFecpmHistoricBitErrCor=nbsFecpmHistoricBitErrCor, nbsFecpmThresholdsEntry=nbsFecpmThresholdsEntry, nbsFecpmTrapsBitErrCor=nbsFecpmTrapsBitErrCor, nbsFecpmRunningTable=nbsFecpmRunningTable, nbsFecStatsTable=nbsFecStatsTable, nbsFecpmMib=nbsFecpmMib, nbsFecpmCurrentGrp=nbsFecpmCurrentGrp, nbsFecpmCurrentTime=nbsFecpmCurrentTime, nbsFecpmCurrentUncorWords=nbsFecpmCurrentUncorWords, nbsFecpmThresholdsIfIndex=nbsFecpmThresholdsIfIndex, nbsFecpmThresholdsGrp=nbsFecpmThresholdsGrp, nbsFecpmRunningDate=nbsFecpmRunningDate, nbsFecStatsUncorWords=nbsFecStatsUncorWords, nbsFecpmRunningTime=nbsFecpmRunningTime, nbsFecpmThresholdsTable=nbsFecpmThresholdsTable, nbsFecStatsDate=nbsFecStatsDate, PYSNMP_MODULE_ID=nbsFecpmMib, nbsFecpmThresholdsByteErrCor=nbsFecpmThresholdsByteErrCor, nbsFecpmHistoricUncorWords=nbsFecpmHistoricUncorWords, nbsFecpmHistoricIfIndex=nbsFecpmHistoricIfIndex, nbsFecpmRunningCorBit1to0=nbsFecpmRunningCorBit1to0, nbsFecpmRunningIfIndex=nbsFecpmRunningIfIndex, nbsFecpmRunningByteErrCor=nbsFecpmRunningByteErrCor, nbsFecpmThresholdsCorBit1to0=nbsFecpmThresholdsCorBit1to0, nbsFecpmTrapsByteErrCor=nbsFecpmTrapsByteErrCor, nbsFecpmHistoricTime=nbsFecpmHistoricTime, nbsFecpmTraps=nbsFecpmTraps, nbsFecpmCurrentEntry=nbsFecpmCurrentEntry, nbsFecpmCurrentIfIndex=nbsFecpmCurrentIfIndex, nbsFecpmHistoricTable=nbsFecpmHistoricTable, nbsFecpmHistoricSample=nbsFecpmHistoricSample, nbsFecpmTrapsCorBit0to1=nbsFecpmTrapsCorBit0to1, nbsFecpmTrapsUncorWords=nbsFecpmTrapsUncorWords, nbsFecpmRunningBitErrCor=nbsFecpmRunningBitErrCor, nbsFecpmRunningCorBit0to1=nbsFecpmRunningCorBit0to1, nbsFecpmCurrentDate=nbsFecpmCurrentDate, nbsFecpmCurrentInterval=nbsFecpmCurrentInterval, nbsFecpmCurrentByteErrCor=nbsFecpmCurrentByteErrCor, nbsFecStatsBitErrCor=nbsFecStatsBitErrCor, nbsFecpmHistoricEntry=nbsFecpmHistoricEntry, nbsFecpmRunningUncorWords=nbsFecpmRunningUncorWords, nbsFecStatsCorBit1to0=nbsFecStatsCorBit1to0, nbsFecpmTrapsCorBit1to0=nbsFecpmTrapsCorBit1to0, nbsFecpmCurrentTable=nbsFecpmCurrentTable, nbsFecStatsIfIndex=nbsFecStatsIfIndex, nbsFecpmHistoricDate=nbsFecpmHistoricDate, nbsFecStatsByteErrCor=nbsFecStatsByteErrCor, nbsFecpmThresholdsCorBit0to1=nbsFecpmThresholdsCorBit0to1, nbsFecStatsGrp=nbsFecStatsGrp, nbsFecpmThresholdsBitErrCor=nbsFecpmThresholdsBitErrCor)
