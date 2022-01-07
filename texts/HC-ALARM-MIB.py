#
# PySNMP MIB module HC-ALARM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/HC-ALARM-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:49 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
CounterBasedGauge64, = mibBuilder.importSymbols("HCNUM-TC", "CounterBasedGauge64")
rmonEventGroup, rmon, OwnerString = mibBuilder.importSymbols("RMON-MIB", "rmonEventGroup", "rmon", "OwnerString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Counter64, Unsigned32, ModuleIdentity, Counter32, NotificationType, TimeTicks, IpAddress, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Unsigned32", "ModuleIdentity", "Counter32", "NotificationType", "TimeTicks", "IpAddress", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32")
TextualConvention, VariablePointer, RowStatus, StorageType, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "VariablePointer", "RowStatus", "StorageType", "DisplayString")
hcAlarmMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 29))
hcAlarmMIB.setRevisions(('2002-12-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: hcAlarmMIB.setRevisionsDescriptions(('Initial version of the High Capacity Alarm MIB module.\n             This version published as RFC 3434.',))
if mibBuilder.loadTexts: hcAlarmMIB.setLastUpdated('200212160000Z')
if mibBuilder.loadTexts: hcAlarmMIB.setOrganization('IETF RMONMIB Working Group')
if mibBuilder.loadTexts: hcAlarmMIB.setContactInfo('        Andy Bierman\n                     Cisco Systems, Inc.\n                Tel: +1 408 527-3711\n\n             E-mail: abierman@cisco.com\n             Postal: 170 West Tasman Drive\n                     San Jose, CA USA 95134\n\n                     Keith McCloghrie\n                     Cisco Systems, Inc.\n                Tel: +1 408 526-5260\n             E-mail: kzm@cisco.com\n             Postal: 170 West Tasman Drive\n                     San Jose, CA USA 95134\n\n             Send comments to <rmonmib@ietf.org>\n             Mailing list subscription info:\n                 http://www.ietf.org/mailman/listinfo/rmonmib ')
if mibBuilder.loadTexts: hcAlarmMIB.setDescription('This module defines Remote Monitoring MIB extensions for\n             High Capacity Alarms.\n\n             Copyright (C) The Internet Society (2002). This version\n             of this MIB module is part of RFC 3434; see the RFC\n             itself for full legal notices.')
hcAlarmObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1))
hcAlarmNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 2))
hcAlarmConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3))
hcAlarmControlObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1, 1))
hcAlarmCapabilitiesObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 1, 2))
class HcValueStatus(TextualConvention, Integer32):
    description = "This data type indicates the validity and sign of the data\n            in associated object instances which represent the absolute\n            value of a high capacity numeric quantity.  Such an object\n            may be represented with one or more object instances. An\n            object of type HcValueStatus MUST be defined within the same\n            structure as the object(s) representing the high capacity\n            absolute value.\n\n            If the associated object instance(s) representing the high\n            capacity absolute value could not be accessed during the\n            sampling interval, and is therefore invalid, then the\n            associated HcValueStatus object will contain the value\n            'valueNotAvailable(1)'.\n\n            If the associated object instance(s) representing the high\n            capacity absolute value are valid and actual value of the\n            sample is greater than or equal to zero, then the associated\n            HcValueStatus object will contain the value\n            'valuePositive(2)'.\n\n            If the associated object instance(s) representing the high\n            capacity absolute value are valid and the actual value of\n            the sample is less than zero, then the associated\n            HcValueStatus object will contain the value\n            'valueNegative(3)'.  The associated absolute value should be\n            multiplied by -1 to obtain the true sample value."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("valueNotAvailable", 1), ("valuePositive", 2), ("valueNegative", 3))

hcAlarmTable = MibTable((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1), )
if mibBuilder.loadTexts: hcAlarmTable.setStatus('current')
if mibBuilder.loadTexts: hcAlarmTable.setDescription('A list of entries for the configuration of high capacity\n            alarms.')
hcAlarmEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1), ).setIndexNames((0, "HC-ALARM-MIB", "hcAlarmIndex"))
if mibBuilder.loadTexts: hcAlarmEntry.setStatus('current')
if mibBuilder.loadTexts: hcAlarmEntry.setDescription('A conceptual row in the hcAlarmTable. Entries are usually\n            created in this table by management application action, but\n            may also be created by agent action as well.')
hcAlarmIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hcAlarmIndex.setStatus('current')
if mibBuilder.loadTexts: hcAlarmIndex.setDescription('An arbitrary integer index value used to uniquely identify\n            this high capacity alarm entry.')
hcAlarmInterval = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmInterval.setStatus('current')
if mibBuilder.loadTexts: hcAlarmInterval.setDescription('The interval in seconds over which the data is sampled and\n            compared with the rising and falling thresholds.  When\n            setting this variable, care should be taken in the case of\n            deltaValue sampling - the interval should be set short\n            enough that the sampled variable is very unlikely to\n            increase or decrease by more than 2^63 - 1 during a single\n            sampling interval.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).')
hcAlarmVariable = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 3), VariablePointer()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmVariable.setStatus('current')
if mibBuilder.loadTexts: hcAlarmVariable.setDescription('The object identifier of the particular variable to be\n            sampled.  Only variables that resolve to an ASN.1 primitive\n            type of INTEGER (INTEGER, Integer32, Counter32, Counter64,\n            Gauge, or TimeTicks) may be sampled.\n\n            Because SNMP access control is articulated entirely in terms\n            of the contents of MIB views, no access control mechanism\n            exists that can restrict the value of this object to\n            identify only those objects that exist in a particular MIB\n            view.  Because there is thus no acceptable means of\n            restricting the read access that could be obtained through\n            the alarm mechanism, the probe must only grant write access\n            to this object in those views that have read access to all\n            objects on the probe.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).')
hcAlarmSampleType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("absoluteValue", 1), ("deltaValue", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmSampleType.setStatus('current')
if mibBuilder.loadTexts: hcAlarmSampleType.setDescription('The method of sampling the selected variable and\n            calculating the value to be compared against the thresholds.\n            If the value of this object is absoluteValue(1), the value\n            of the selected variable will be compared directly with the\n            thresholds at the end of the sampling interval.  If the\n            value of this object is deltaValue(2), the value of the\n            selected variable at the last sample will be subtracted from\n            the current value, and the difference compared with the\n            thresholds.\n\n            If the associated hcAlarmVariable instance could not be\n            obtained at the previous sample interval, then a delta\n            sample is not possible, and the value of the associated\n            hcAlarmValueStatus object for this interval will be\n            valueNotAvailable(1).\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).')
hcAlarmAbsValue = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 5), CounterBasedGauge64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmAbsValue.setStatus('current')
if mibBuilder.loadTexts: hcAlarmAbsValue.setDescription("The absolute value (i.e., unsigned value) of the\n            hcAlarmVariable statistic during the last sampling period.\n            The value during the current sampling period is not made\n            available until the period is completed.\n\n            To obtain the true value for this sampling interval, the\n            associated instance of hcAlarmValueStatus must be checked,\n            and the value of this object adjusted as necessary.\n\n            If the MIB instance could not be accessed during the\n            sampling interval, then this object will have a value of\n            zero and the associated instance of hcAlarmValueStatus will\n            be set to 'valueNotAvailable(1)'.")
hcAlarmValueStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 6), HcValueStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmValueStatus.setStatus('current')
if mibBuilder.loadTexts: hcAlarmValueStatus.setDescription('This object indicates the validity and sign of the data for\n            the hcAlarmAbsValue object, as described in the\n            HcValueStatus textual convention.')
hcAlarmStartupAlarm = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("risingAlarm", 1), ("fallingAlarm", 2), ("risingOrFallingAlarm", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmStartupAlarm.setStatus('current')
if mibBuilder.loadTexts: hcAlarmStartupAlarm.setDescription('The alarm that may be sent when this entry is first set to\n            active.  If the first sample after this entry becomes active\n            is greater than or equal to the rising threshold and this\n            object is equal to risingAlarm(1) or\n            risingOrFallingAlarm(3), then a single rising alarm will be\n            generated.  If the first sample after this entry becomes\n            valid is less than or equal to the falling threshold and\n            this object is equal to fallingAlarm(2) or\n            risingOrFallingAlarm(3), then a single falling alarm will be\n            generated.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).')
hcAlarmRisingThreshAbsValueLo = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 8), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingThreshAbsValueLo.setStatus('current')
if mibBuilder.loadTexts: hcAlarmRisingThreshAbsValueLo.setDescription('The lower 32 bits of the absolute value for threshold for\n            the sampled statistic.  The actual threshold value is\n            determined by the associated instances of the\n            hcAlarmRisingThreshAbsValueHi and\n            hcAlarmRisingThresholdValStatus objects, as follows:\n\n               ABS(threshold) = hcAlarmRisingThreshAbsValueLo +\n                     (hcAlarmRisingThreshAbsValueHi * 2^^32)\n\n            The absolute value of the threshold is adjusted as required,\n            as described in the HcValueStatus textual convention.  These\n            three object instances are conceptually combined to\n            represent the rising threshold for this entry.\n\n            When the current sampled value is greater than or equal to\n            this threshold, and the value at the last sampling interval\n            was less than this threshold, a single event will be\n            generated.  A single event will also be generated if the\n            first sample after this entry becomes valid is greater than\n            or equal to this threshold and the associated\n            hcAlarmStartupAlarm is equal to risingAlarm(1) or\n            risingOrFallingAlarm(3).\n\n            After a rising event is generated, another such event will\n            not be generated until the sampled value falls below this\n            threshold and reaches the threshold identified by the\n            hcAlarmFallingThreshAbsValueLo,\n            hcAlarmFallingThreshAbsValueHi, and\n            hcAlarmFallingThresholdValStatus objects.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).')
hcAlarmRisingThreshAbsValueHi = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 9), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingThreshAbsValueHi.setStatus('current')
if mibBuilder.loadTexts: hcAlarmRisingThreshAbsValueHi.setDescription('The upper 32 bits of the absolute value for threshold for\n            the sampled statistic.  The actual threshold value is\n            determined by the associated instances of the\n            hcAlarmRisingThreshAbsValueLo and\n            hcAlarmRisingThresholdValStatus objects, as follows:\n\n               ABS(threshold) = hcAlarmRisingThreshAbsValueLo +\n                     (hcAlarmRisingThreshAbsValueHi * 2^^32)\n\n            The absolute value of the threshold is adjusted as required,\n            as described in the HcValueStatus textual convention.  These\n            three object instances are conceptually combined to\n            represent the rising threshold for this entry.\n\n            When the current sampled value is greater than or equal to\n            this threshold, and the value at the last sampling interval\n            was less than this threshold, a single event will be\n            generated.  A single event will also be generated if the\n            first sample after this entry becomes valid is greater than\n            or equal to this threshold and the associated\n            hcAlarmStartupAlarm is equal to risingAlarm(1) or\n            risingOrFallingAlarm(3).\n\n            After a rising event is generated, another such event will\n            not be generated until the sampled value falls below this\n            threshold and reaches the threshold identified by the\n            hcAlarmFallingThreshAbsValueLo,\n            hcAlarmFallingThreshAbsValueHi, and\n            hcAlarmFallingThresholdValStatus objects.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).')
hcAlarmRisingThresholdValStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 10), HcValueStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingThresholdValStatus.setStatus('current')
if mibBuilder.loadTexts: hcAlarmRisingThresholdValStatus.setDescription("This object indicates the sign of the data for the rising\n            threshold, as defined by the hcAlarmRisingThresAbsValueLo\n            and hcAlarmRisingThresAbsValueHi objects, as described in\n            the HcValueStatus textual convention.\n\n            The enumeration 'valueNotAvailable(1)' is not allowed, and\n            the associated hcAlarmStatus object cannot be equal to\n            'active(1)' if this object is set to this value.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).")
hcAlarmFallingThreshAbsValueLo = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 11), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingThreshAbsValueLo.setStatus('current')
if mibBuilder.loadTexts: hcAlarmFallingThreshAbsValueLo.setDescription('The lower 32 bits of the absolute value for threshold for\n            the sampled statistic.  The actual threshold value is\n            determined by the associated instances of the\n            hcAlarmFallingThreshAbsValueHi and\n            hcAlarmFallingThresholdValStatus objects, as follows:\n\n               ABS(threshold) = hcAlarmFallingThreshAbsValueLo +\n                     (hcAlarmFallingThreshAbsValueHi * 2^^32)\n\n            The absolute value of the threshold is adjusted as required,\n            as described in the HcValueStatus textual convention.  These\n            three object instances are conceptually combined to\n            represent the falling threshold for this entry.\n\n            When the current sampled value is less than or equal to this\n            threshold, and the value at the last sampling interval was\n            greater than this threshold, a single event will be\n            generated.  A single event will also be generated if the\n            first sample after this entry becomes valid is less than or\n            equal to this threshold and the associated\n            hcAlarmStartupAlarm is equal to fallingAlarm(2) or\n            risingOrFallingAlarm(3).\n\n            After a falling event is generated, another such event will\n            not be generated until the sampled value rises above this\n            threshold and reaches the threshold identified by the\n            hcAlarmRisingThreshAbsValueLo,\n            hcAlarmRisingThreshAbsValueHi, and\n            hcAlarmRisingThresholdValStatus objects.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).')
hcAlarmFallingThreshAbsValueHi = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 12), Unsigned32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingThreshAbsValueHi.setStatus('current')
if mibBuilder.loadTexts: hcAlarmFallingThreshAbsValueHi.setDescription('The upper 32 bits of the absolute value for threshold for\n            the sampled statistic.  The actual threshold value is\n            determined by the associated instances of the\n            hcAlarmFallingThreshAbsValueLo and\n            hcAlarmFallingThresholdValStatus objects, as follows:\n\n               ABS(threshold) = hcAlarmFallingThreshAbsValueLo +\n                     (hcAlarmFallingThreshAbsValueHi * 2^^32)\n\n            The absolute value of the threshold is adjusted as required,\n            as described in the HcValueStatus textual convention.  These\n            three object instances are conceptually combined to\n            represent the falling threshold for this entry.\n\n            When the current sampled value is less than or equal to this\n            threshold, and the value at the last sampling interval was\n            greater than this threshold, a single event will be\n            generated.  A single event will also be generated if the\n            first sample after this entry becomes valid is less than or\n            equal to this threshold and the associated\n            hcAlarmStartupAlarm is equal to fallingAlarm(2) or\n            risingOrFallingAlarm(3).\n\n            After a falling event is generated, another such event will\n            not be generated until the sampled value rises above this\n            threshold and reaches the threshold identified by the\n            hcAlarmRisingThreshAbsValueLo,\n            hcAlarmRisingThreshAbsValueHi, and\n            hcAlarmRisingThresholdValStatus objects.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).')
hcAlarmFallingThresholdValStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 13), HcValueStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingThresholdValStatus.setStatus('current')
if mibBuilder.loadTexts: hcAlarmFallingThresholdValStatus.setDescription("This object indicates the sign of the data for the falling\n            threshold, as defined by the hcAlarmFallingThreshAbsValueLo\n            and hcAlarmFallingThreshAbsValueHi objects, as described in\n            the HcValueStatus textual convention.\n\n            The enumeration 'valueNotAvailable(1)' is not allowed, and\n            the associated hcAlarmStatus object cannot be equal to\n            'active(1)' if this object is set to this value.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).")
hcAlarmRisingEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 14), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmRisingEventIndex.setStatus('current')
if mibBuilder.loadTexts: hcAlarmRisingEventIndex.setDescription('The index of the eventEntry that is used when a rising\n            threshold is crossed.  The eventEntry identified by a\n            particular value of this index is the same as identified by\n            the same value of the eventIndex object.  If there is no\n            corresponding entry in the eventTable, then no association\n            exists.  In particular, if this value is zero, no associated\n            event will be generated, as zero is not a valid event index.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).')
hcAlarmFallingEventIndex = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 15), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmFallingEventIndex.setStatus('current')
if mibBuilder.loadTexts: hcAlarmFallingEventIndex.setDescription('The index of the eventEntry that is used when a falling\n            threshold is crossed.  The eventEntry identified by a\n            particular value of this index is the same as identified by\n            the same value of the eventIndex object.  If there is no\n            corresponding entry in the eventTable, then no association\n            exists.  In particular, if this value is zero, no associated\n            event will be generated, as zero is not a valid event index.\n\n            This object may not be modified if the associated\n            hcAlarmStatus object is equal to active(1).')
hcAlarmValueFailedAttempts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 16), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmValueFailedAttempts.setStatus('current')
if mibBuilder.loadTexts: hcAlarmValueFailedAttempts.setDescription('The number of times the associated hcAlarmVariable instance\n            was polled on behalf of this hcAlarmEntry, (while in the\n            active state) and the value was not available.  This counter\n            may experience a discontinuity if the agent restarts,\n            indicated by the value of sysUpTime.')
hcAlarmOwner = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 17), OwnerString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmOwner.setStatus('current')
if mibBuilder.loadTexts: hcAlarmOwner.setDescription('The entity that configured this entry and is therefore\n            using the resources assigned to it.')
hcAlarmStorageType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 18), StorageType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmStorageType.setStatus('current')
if mibBuilder.loadTexts: hcAlarmStorageType.setDescription("The type of non-volatile storage configured for this entry.\n            If this object is equal to 'permanent(4)', then the\n            associated hcAlarmRisingEventIndex and\n            hcAlarmFallingEventIndex objects must be writable.")
hcAlarmStatus = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 29, 1, 1, 1, 1, 19), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hcAlarmStatus.setStatus('current')
if mibBuilder.loadTexts: hcAlarmStatus.setDescription('The status of this row.\n\n            An entry MUST NOT exist in the active state unless all\n            objects in the entry have an appropriate value, as described\n            in the description clause for each writable object.\n\n            The hcAlarmStatus object may be modified if the associated\n            instance of this object is equal to active(1),\n            notInService(2), or notReady(3).  All other writable objects\n            may be modified if the associated instance of this object is\n            equal to notInService(2) or notReady(3).')
hcAlarmCapabilities = MibScalar((1, 3, 6, 1, 2, 1, 16, 29, 1, 2, 1), Bits().clone(namedValues=NamedValues(("hcAlarmCreation", 0), ("hcAlarmNvStorage", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hcAlarmCapabilities.setStatus('current')
if mibBuilder.loadTexts: hcAlarmCapabilities.setDescription("An indication of the high capacity alarm capabilities\n            supported by this agent.\n\n            If the 'hcAlarmCreation' BIT is set, then this agent allows\n            NMS applications to create entries in the hcAlarmTable.\n\n            If the 'hcAlarmNvStorage' BIT is set, then this agent allows\n            entries in the hcAlarmTable which will be recreated after a\n            system restart, as controlled by the hcAlarmStorageType\n            object.")
hcAlarmNotifPrefix = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 2, 0))
hcRisingAlarm = NotificationType((1, 3, 6, 1, 2, 1, 16, 29, 2, 0, 1)).setObjects(("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmSampleType"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmRisingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmRisingEventIndex"))
if mibBuilder.loadTexts: hcRisingAlarm.setStatus('current')
if mibBuilder.loadTexts: hcRisingAlarm.setDescription('The SNMP notification that is generated when a high\n            capacity alarm entry crosses its rising threshold and\n            generates an event that is configured for sending SNMP\n            traps.\n\n            The hcAlarmEntry object instances identified in the OBJECTS\n            clause are from the entry that causes this notification to\n            be generated.')
hcFallingAlarm = NotificationType((1, 3, 6, 1, 2, 1, 16, 29, 2, 0, 2)).setObjects(("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmSampleType"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmFallingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmFallingEventIndex"))
if mibBuilder.loadTexts: hcFallingAlarm.setStatus('current')
if mibBuilder.loadTexts: hcFallingAlarm.setDescription('The SNMP notification that is generated when a high\n            capacity alarm entry crosses its falling threshold and\n            generates an event that is configured for sending SNMP\n            traps.\n\n            The hcAlarmEntry object instances identified in the OBJECTS\n            clause are from the entry that causes this notification to\n            be generated.')
hcAlarmCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3, 1))
hcAlarmGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 29, 3, 2))
hcAlarmCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 29, 3, 1, 1)).setObjects(("HC-ALARM-MIB", "hcAlarmControlGroup"), ("HC-ALARM-MIB", "hcAlarmCapabilitiesGroup"), ("HC-ALARM-MIB", "hcAlarmNotificationsGroup"), ("RMON-MIB", "rmonEventGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcAlarmCompliance = hcAlarmCompliance.setStatus('current')
if mibBuilder.loadTexts: hcAlarmCompliance.setDescription('Describes the requirements for conformance to the High\n            Capacity Alarm MIB.')
hcAlarmControlGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 1)).setObjects(("HC-ALARM-MIB", "hcAlarmInterval"), ("HC-ALARM-MIB", "hcAlarmVariable"), ("HC-ALARM-MIB", "hcAlarmSampleType"), ("HC-ALARM-MIB", "hcAlarmAbsValue"), ("HC-ALARM-MIB", "hcAlarmValueStatus"), ("HC-ALARM-MIB", "hcAlarmStartupAlarm"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmRisingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmRisingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueLo"), ("HC-ALARM-MIB", "hcAlarmFallingThreshAbsValueHi"), ("HC-ALARM-MIB", "hcAlarmFallingThresholdValStatus"), ("HC-ALARM-MIB", "hcAlarmRisingEventIndex"), ("HC-ALARM-MIB", "hcAlarmFallingEventIndex"), ("HC-ALARM-MIB", "hcAlarmValueFailedAttempts"), ("HC-ALARM-MIB", "hcAlarmOwner"), ("HC-ALARM-MIB", "hcAlarmStorageType"), ("HC-ALARM-MIB", "hcAlarmStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcAlarmControlGroup = hcAlarmControlGroup.setStatus('current')
if mibBuilder.loadTexts: hcAlarmControlGroup.setDescription('A collection of objects used to configure entries for high\n            capacity alarm threshold monitoring purposes.')
hcAlarmCapabilitiesGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 2)).setObjects(("HC-ALARM-MIB", "hcAlarmCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcAlarmCapabilitiesGroup = hcAlarmCapabilitiesGroup.setStatus('current')
if mibBuilder.loadTexts: hcAlarmCapabilitiesGroup.setDescription("A collection of objects used to indicate an agent's high\n            capacity alarm threshold monitoring capabilities.")
hcAlarmNotificationsGroup = NotificationGroup((1, 3, 6, 1, 2, 1, 16, 29, 3, 2, 3)).setObjects(("HC-ALARM-MIB", "hcRisingAlarm"), ("HC-ALARM-MIB", "hcFallingAlarm"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hcAlarmNotificationsGroup = hcAlarmNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: hcAlarmNotificationsGroup.setDescription('A collection of notifications to deliver information\n            related to a high capacity rising or falling threshold event\n            to a management application.')
mibBuilder.exportSymbols("HC-ALARM-MIB", hcAlarmFallingThreshAbsValueHi=hcAlarmFallingThreshAbsValueHi, hcFallingAlarm=hcFallingAlarm, PYSNMP_MODULE_ID=hcAlarmMIB, hcAlarmMIB=hcAlarmMIB, HcValueStatus=HcValueStatus, hcAlarmConformance=hcAlarmConformance, hcAlarmStatus=hcAlarmStatus, hcAlarmGroups=hcAlarmGroups, hcAlarmRisingThreshAbsValueHi=hcAlarmRisingThreshAbsValueHi, hcAlarmObjects=hcAlarmObjects, hcAlarmNotificationsGroup=hcAlarmNotificationsGroup, hcAlarmCompliances=hcAlarmCompliances, hcAlarmOwner=hcAlarmOwner, hcAlarmCapabilitiesGroup=hcAlarmCapabilitiesGroup, hcAlarmVariable=hcAlarmVariable, hcAlarmFallingEventIndex=hcAlarmFallingEventIndex, hcAlarmEntry=hcAlarmEntry, hcAlarmCapabilities=hcAlarmCapabilities, hcAlarmStartupAlarm=hcAlarmStartupAlarm, hcRisingAlarm=hcRisingAlarm, hcAlarmCompliance=hcAlarmCompliance, hcAlarmControlObjects=hcAlarmControlObjects, hcAlarmAbsValue=hcAlarmAbsValue, hcAlarmRisingThresholdValStatus=hcAlarmRisingThresholdValStatus, hcAlarmRisingThreshAbsValueLo=hcAlarmRisingThreshAbsValueLo, hcAlarmNotifPrefix=hcAlarmNotifPrefix, hcAlarmIndex=hcAlarmIndex, hcAlarmNotifications=hcAlarmNotifications, hcAlarmTable=hcAlarmTable, hcAlarmFallingThresholdValStatus=hcAlarmFallingThresholdValStatus, hcAlarmFallingThreshAbsValueLo=hcAlarmFallingThreshAbsValueLo, hcAlarmInterval=hcAlarmInterval, hcAlarmSampleType=hcAlarmSampleType, hcAlarmRisingEventIndex=hcAlarmRisingEventIndex, hcAlarmCapabilitiesObjects=hcAlarmCapabilitiesObjects, hcAlarmValueFailedAttempts=hcAlarmValueFailedAttempts, hcAlarmControlGroup=hcAlarmControlGroup, hcAlarmValueStatus=hcAlarmValueStatus, hcAlarmStorageType=hcAlarmStorageType)
