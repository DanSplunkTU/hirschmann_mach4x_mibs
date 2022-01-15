#
# PySNMP MIB module LIEBERT-GP-FLEXIBLE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/liebert/LIEBERT-GP-FLEXIBLE-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:12:11 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
lgpFlexible, liebertFlexibleModuleReg = mibBuilder.importSymbols("LIEBERT-GP-REGISTRATION-MIB", "lgpFlexible", "liebertFlexibleModuleReg")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, TimeTicks, IpAddress, Gauge32, MibIdentifier, Counter32, iso, NotificationType, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ModuleIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "TimeTicks", "IpAddress", "Gauge32", "MibIdentifier", "Counter32", "iso", "NotificationType", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ModuleIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
liebertGlobalProductsFlexibleModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 476, 1, 42, 1, 10, 1))
liebertGlobalProductsFlexibleModule.setRevisions(('2013-05-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: liebertGlobalProductsFlexibleModule.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: liebertGlobalProductsFlexibleModule.setLastUpdated('201305140000Z')
if mibBuilder.loadTexts: liebertGlobalProductsFlexibleModule.setOrganization('Liebert Corporation')
if mibBuilder.loadTexts: liebertGlobalProductsFlexibleModule.setContactInfo('Contact:   Technical Support\n\n      Postal:\n      Liebert Corporation\n      1050 Dearborn Drive\n      P.O. Box 29186\n      Columbus OH, 43229\n      US\n\n      Tel: +1 (800) 222-5877\n\n      E-mail: liebert.monitoring@vertivco.com\n      Web:    www.vertivco.com\n\n      Author:  Phil Ulrich')
if mibBuilder.loadTexts: liebertGlobalProductsFlexibleModule.setDescription("The MIB module used to register Liebert Flexible related SNMP OIDs.\n\n      Copyright 2013 Liebert Corporation. All rights reserved.\n      Reproduction of this document is authorized on the condition\n      that the forgoing copyright notice is included.\n\n      This Specification is supplied 'AS IS' and Liebert Corporation\n      makes no warranty, either express or implied, as to the use,\n      operation, condition, or performance of the Specification.")
lgpFlexibleTableCount = MibScalar((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 10), Unsigned32()).setUnits('Count').setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpFlexibleTableCount.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleTableCount.setDescription('This is the number of entries in the lgpFlexibleBasicTable.')
lgpFlexibleBasicTable = MibTable((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20), )
if mibBuilder.loadTexts: lgpFlexibleBasicTable.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleBasicTable.setDescription('This table contains data points supported by the managed device. The \n         data in this table is formatted in string form. This data is also \n         available in numerical form in the augmented \n         lgpFlexibleExtendedTable.\n\n         In this table, the row indexing is not necessarily sequential and \n         leads to a sparsely populated table.')
lgpFlexibleBasicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1), ).setIndexNames((1, "LIEBERT-GP-FLEXIBLE-MIB", "lgpFlexibleEntryIndex"))
if mibBuilder.loadTexts: lgpFlexibleBasicEntry.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleBasicEntry.setDescription("This entry defines the columns to be populated in the\n             'lgpFlexibleBasicTable'.")
lgpFlexibleEntryIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: lgpFlexibleEntryIndex.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryIndex.setDescription('This is the index which defines a specific row in the \n             lgpFlexibleBasicTable.  Each row index is associated with a unique\n             data point ID which fixes the data point to its permanent location\n             in the table.')
lgpFlexibleEntryDataLabel = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpFlexibleEntryDataLabel.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryDataLabel.setDescription('A short description of the data reported in this row.')
lgpFlexibleEntryValue = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 20), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpFlexibleEntryValue.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryValue.setDescription('A string representation of any data available.  This is the\n             preferred method of data access, since this will give fully\n             scaled data for both integer and floating point data, in addition\n             to textual data.  If this string column cannot be used, then \n             columns in the lgpFlexibleExtendedTable must be used in order \n             to get a fully scaled version of integer data.')
lgpFlexibleEntryUnitsOfMeasure = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 20, 1, 30), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpFlexibleEntryUnitsOfMeasure.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryUnitsOfMeasure.setDescription('The unit of measure that the value will be presented in.  This is\n             not populated when the data does not have a unit of measure\n             associated with it.')
lgpFlexibleExtendedTable = MibTable((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30), )
if mibBuilder.loadTexts: lgpFlexibleExtendedTable.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleExtendedTable.setDescription('This table contains data points supported by the managed device.  This\n         table augments the lgpFlexibleBasicTable, providing additional\n         information that may be relevant to advanced users.  Values presented \n         in string format in the lgpFlexibleBasicTable table are also available in \n         numeric form in this table.\n\n         Since the lgpFlexibleBasicTable and this table are both indexed by \n         lgpFlexibleEntryIndex, data applicable to a specific data point can be \n         found in both tables at the same index.')
lgpFlexibleExtendedEntry = MibTableRow((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1), )
lgpFlexibleBasicEntry.registerAugmentions(("LIEBERT-GP-FLEXIBLE-MIB", "lgpFlexibleExtendedEntry"))
lgpFlexibleExtendedEntry.setIndexNames(*lgpFlexibleBasicEntry.getIndexNames())
if mibBuilder.loadTexts: lgpFlexibleExtendedEntry.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleExtendedEntry.setDescription("This entry defines the columns to be populated in the\n             'lgpFlexibleExtendedTable'.")
lgpFlexibleEntryIntegerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 10), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpFlexibleEntryIntegerValue.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryIntegerValue.setDescription('This is the data point value formatted as a signed integer. This \n             column is populated only for numerical data points whose type \n             requires a signed value.\n\n             To convert this value to the units indicated in the units of \n             measure columns (lgpFlexibleEntryUnitsOfMeasure or \n             lgpFlexibleEntryUnitsOfMeasureEnum), divide this value \n             by 10^n, where n is the value from the \n             lgpFlexibleEntryDecimalPosition column.\n\n             For data points that are writable (as designated by the\n             lgpFlexibleEntryAccessibility column), the inverse\n             calculation must done.  The desired value must be multiplied by\n             10^n before it is written to this column, where n is the value \n             from the lgpFlexibleEntryDecimalPosition column.')
lgpFlexibleEntryUnsignedIntegerValue = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 20), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: lgpFlexibleEntryUnsignedIntegerValue.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryUnsignedIntegerValue.setDescription('This is the data point value formatted as an unsigned integer. This \n             column is populated only for numerical data points whose type \n             does not require a signed value.\n\n             To convert this value to the units indicated in the units of \n             measure columns (lgpFlexibleEntryUnitsOfMeasure or \n             lgpFlexibleEntryUnitsOfMeasureEnum), divide this value \n             by 10^n, where n is the value from the \n             lgpFlexibleEntryDecimalPosition column.\n\n             For data points that are writable (as designated by the\n             lgpFlexibleEntryAccessibility column), the inverse\n             calculation must done.  The desired value must be multiplied by\n             10^n before it is written to this column, where n is the value \n             from the lgpFlexibleEntryDecimalPosition column.')
lgpFlexibleEntryDecimalPosition = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 30), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpFlexibleEntryDecimalPosition.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryDecimalPosition.setDescription('This is a power of ten divider needed to convert values from the \n             signed and unsigned integer columns \n             (lgpFlexibleEntryIntegerValue or \n             lgpFlexibleEntryUnsignedIntegerValue) to floating \n             point values. This essentially tells how many positions to move \n             the decimal point to the left.\n\n             To convert the integer values to the units indicated in the units \n             of measure columns (lgpFlexibleEntryUnitsOfMeasure or \n             lgpFlexibleEntryUnitsOfMeasureEnum), divide the \n             integer value by 10^n, where n is the value from this column.\n\n             For data points that are writable (as designated by the\n             lgpFlexibleEntryAccessibility column), the inverse\n             calculation must done. The desired value must be multiplied by\n             10^n before it is written to the signed or unsigned integer \n             columns.')
lgpFlexibleEntryDataType = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 40), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("not-specified", 0), ("int16", 1), ("uint16", 2), ("int32", 3), ("uint32", 4), ("text", 5), ("enum", 6), ("event16", 7), ("event32", 8), ("ipv4", 9), ("time32", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpFlexibleEntryDataType.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryDataType.setDescription('The format that the data will appear as.  This can be used to\n             determine which field the numerical data will appear in.  Data of \n             type int16 and int32 will appear in the column\n             lgpFlexibleEntryIntegerValue.  Data of type uint16, \n             uint32, and enum, will appear in the column\n             lgpFlexibleEntryUnsignedIntegerValue.')
lgpFlexibleEntryAccessibility = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 50), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("not-specified", 0), ("readonly", 1), ("writeonly", 2), ("readwrite", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpFlexibleEntryAccessibility.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryAccessibility.setDescription('This describes the read/write access that is available for the \n             data in the row.')
lgpFlexibleEntryUnitsOfMeasureEnum = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 60), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 4096, 4097, 4098, 4099, 4100, 4101, 4102, 4103, 4104, 4105, 4106, 4107, 4108, 4109, 4110, 4111, 4112, 4113, 4114, 4115, 4116, 4117, 4118, 4119, 4120, 4121, 4122, 4123, 4124, 4125, 4126, 4127, 4128, 4129, 4130, 4131, 4132, 4133, 4134, 4135, 4136, 4137, 4138, 4139, 4140, 4141, 4142, 4143, 4144, 4145, 4146, 4147, 4148, 4149, 4150, 4151, 4152, 4153, 4154, 4155, 4156, 4157, 4158, 4159, 4160, 4161, 4162, 4163, 4164, 4165, 4166, 4167, 4168, 4169, 4170, 4171, 4172, 4173, 4174, 4175, 4176, 4177, 4178))).clone(namedValues=NamedValues(("not-specified", 0), ("milliSeconds", 4096), ("seconds", 4097), ("minutes", 4098), ("hours", 4099), ("voltsAcRms", 4100), ("milliVoltsAcRms", 4101), ("voltsDc", 4102), ("milliVoltsDc", 4103), ("voltsPeak", 4104), ("voltsPeakToPeak", 4105), ("ampsAcRms", 4106), ("milliAmpsAcRms", 4107), ("ampsDc", 4108), ("milliAmpsDc", 4109), ("voltAmps", 4110), ("kiloVoltAmps", 4111), ("voltAmpsReactive", 4112), ("kVAReactive", 4113), ("watts", 4114), ("kiloWatts", 4115), ("wattHours", 4116), ("kiloWattHour", 4117), ("ampDcHours", 4118), ("hertz", 4119), ("milliHertz", 4120), ("kiloHertz", 4121), ("megaHertz", 4122), ("gigaHertz", 4123), ("percent", 4124), ("degC", 4125), ("degCDelta", 4126), ("degF", 4127), ("degFDelta", 4128), ("psi", 4129), ("pascal", 4130), ("psia", 4131), ("relativeHumidity", 4132), ("thd", 4133), ("days", 4134), ("phase", 4135), ("microOhms", 4136), ("milliOhms", 4137), ("ohms", 4138), ("kiloOhms", 4139), ("megaOhms", 4140), ("bars", 4141), ("rpm", 4142), ("bytes", 4143), ("kilobytes", 4144), ("megabytes", 4145), ("gigabytes", 4146), ("terabytes", 4147), ("voltAmpHours", 4148), ("kiloVoltAmpHours", 4149), ("vaReactiveHours", 4150), ("kVAReactiveHours", 4151), ("meter", 4152), ("feet", 4153), ("cms", 4154), ("cmh", 4155), ("cfs", 4156), ("cfm", 4157), ("lpm", 4158), ("gpmUk", 4159), ("gpmUs", 4160), ("absoluteHumidity", 4161), ("kilograms", 4162), ("cubicMeters", 4163), ("btu", 4164), ("torrs", 4165), ("millitorrs", 4166), ("pounds", 4167), ("mps", 4168), ("fpm", 4169), ("liter", 4170), ("gallonUs", 4171), ("gallonUk", 4172), ("lps", 4173), ("mho", 4174), ("siemensCm", 4175), ("weeks", 4176), ("inWC", 4177), ("btuHours", 4178)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpFlexibleEntryUnitsOfMeasureEnum.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryUnitsOfMeasureEnum.setDescription('The unit of measurement that the value will be in.')
lgpFlexibleEntryDataDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 476, 1, 42, 3, 9, 30, 1, 70), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: lgpFlexibleEntryDataDescription.setStatus('current')
if mibBuilder.loadTexts: lgpFlexibleEntryDataDescription.setDescription('A description of the data reported in this row.  This is generally \n             longer and more thorough than the simple label described by \n             lgpFlexibleEntryDataLabel.')
mibBuilder.exportSymbols("LIEBERT-GP-FLEXIBLE-MIB", lgpFlexibleExtendedTable=lgpFlexibleExtendedTable, lgpFlexibleEntryIntegerValue=lgpFlexibleEntryIntegerValue, lgpFlexibleEntryDataDescription=lgpFlexibleEntryDataDescription, lgpFlexibleEntryDataLabel=lgpFlexibleEntryDataLabel, liebertGlobalProductsFlexibleModule=liebertGlobalProductsFlexibleModule, lgpFlexibleExtendedEntry=lgpFlexibleExtendedEntry, lgpFlexibleBasicEntry=lgpFlexibleBasicEntry, lgpFlexibleBasicTable=lgpFlexibleBasicTable, lgpFlexibleEntryUnitsOfMeasure=lgpFlexibleEntryUnitsOfMeasure, lgpFlexibleEntryDecimalPosition=lgpFlexibleEntryDecimalPosition, lgpFlexibleEntryIndex=lgpFlexibleEntryIndex, lgpFlexibleEntryUnsignedIntegerValue=lgpFlexibleEntryUnsignedIntegerValue, lgpFlexibleEntryAccessibility=lgpFlexibleEntryAccessibility, lgpFlexibleEntryUnitsOfMeasureEnum=lgpFlexibleEntryUnitsOfMeasureEnum, lgpFlexibleTableCount=lgpFlexibleTableCount, lgpFlexibleEntryDataType=lgpFlexibleEntryDataType, PYSNMP_MODULE_ID=liebertGlobalProductsFlexibleModule, lgpFlexibleEntryValue=lgpFlexibleEntryValue)
