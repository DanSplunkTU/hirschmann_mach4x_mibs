#
# PySNMP MIB module SIAE-CARRIER-AGGRL1-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-CARRIER-AGGRL1-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:31:57 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ModuleIdentity, Unsigned32, Integer32, Gauge32, IpAddress, MibIdentifier, Bits, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ModuleIdentity", "Unsigned32", "Integer32", "Gauge32", "IpAddress", "MibIdentifier", "Bits", "TimeTicks", "Counter64")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
carrierAggr = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 104))
carrierAggr.setRevisions(('2016-08-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: carrierAggr.setRevisionsDescriptions(('Initial version 01.00.00.\n            ',))
if mibBuilder.loadTexts: carrierAggr.setLastUpdated('201608230000Z')
if mibBuilder.loadTexts: carrierAggr.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: carrierAggr.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: carrierAggr.setDescription('Carrier hybrid aggregation management for SIAE equipments.\n            ')
carrierAggrMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrMibVersion.setStatus('current')
if mibBuilder.loadTexts: carrierAggrMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
carrierAggrSensorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2), )
if mibBuilder.loadTexts: carrierAggrSensorTable.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorTable.setDescription('Table with Radio(s) interface(s) that can be associated \n             to an entry of carrierAggrActuatorTable.')
carrierAggrSensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1), ).setIndexNames((0, "SIAE-CARRIER-AGGRL1-MIB", "carrierAggrSensorIndex"))
if mibBuilder.loadTexts: carrierAggrSensorEntry.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorEntry.setDescription('A row in the carrierAggrSensorTable.')
carrierAggrSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrSensorIndex.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorIndex.setDescription('This object identifies the index of carrierAggrSensorTable.')
carrierAggrSensorRowstatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorRowstatus.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorRowstatus.setDescription('The status of this sensor entry.\n\n             An entry may not exist in the active state unless all\n             objects in the entry have an appropriate value: SensorIfIndex\n             must be set to a valid ifIndex number. Otherwise, the error\n             inconsistentValue is returned on the attempt to set active this \n             row.\n\n             When this object is set to notInService changes may be made to\n             carrierAggrSensorIfIndex.\n             Other objects can be changed when carrierAggrSensorRowStatus is\n             set to active.\n\n             A sensor can not be deleted if there is any Actuator (see table\n             carrierAggrActuatorTable) associated with it.\n            ')
carrierAggrSensorAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorAdminStatus.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorAdminStatus.setDescription('Administative status of the sensor.\n             The value down(1) turns off all actuators associated with\n             this sensor.\n            ')
carrierAggrSensorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorIfIndex.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorIfIndex.setDescription('This object accepts a greater than zero value to identify an\n             interface in ifTable. Some parameters of the radio associated to\n             this interface is monitored and a notification is sent \n             to all connected actuators.\n            ')
carrierAggrSensorHitlessCapability = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 5), Bits().clone(namedValues=NamedValues(("hitlessAvailable", 0)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrSensorHitlessCapability.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorHitlessCapability.setDescription('This capability is related to \n            HITLESS Behaviour carrierAggrSensorHitlessBehaviour.')
carrierAggrSensorHitlessBehaviour = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorHitlessBehaviour.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorHitlessBehaviour.setDescription('The hitless behaviour. When enabled, data related to the current ACM zone \n            is notified to an external N.E. aggregator, so it can dynamically \n            exclude/include the data-flow without loss of frames. \n            It can be enabled only if carrierAggrSensorHitlessCapability is available')
carrierAggrSensorHitlessMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("auto", 1), ("manual", 2))).clone('auto')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorHitlessMode.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorHitlessMode.setDescription('The policy to select the hitless profile (i.e. the lowest one under \n            which a N.E. aggregator excludes the carrier from an existing aggregation).\n            auto(1): Tx Lower Profile + 1 is selected;\n            manual(2): the value set in carrierAggrSensorHitlessProfile is selected. \n           ')
carrierAggrSensorHitlessProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 8), Integer32().clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrSensorHitlessProfile.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorHitlessProfile.setDescription('The hitless profile in case of carrierHyAggrHitlessBehaviour  \n              set as enabled and carrierHyAggrHitlessMode set as manual.\n             ')
carrierAggrSensorHitlessStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("goodZone", 1), ("hitlessZone", 2), ("badZone", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrSensorHitlessStatus.setStatus('current')
if mibBuilder.loadTexts: carrierAggrSensorHitlessStatus.setDescription('The working zone of the radio link.')
carrierAggrActuatorTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3), )
if mibBuilder.loadTexts: carrierAggrActuatorTable.setStatus('current')
if mibBuilder.loadTexts: carrierAggrActuatorTable.setDescription('Table with Lan(s) interface that can be associated\n             to an entry of carrierAggrSensorTable.')
carrierAggrActuatorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1), ).setIndexNames((0, "SIAE-CARRIER-AGGRL1-MIB", "carrierAggrActuatorIndex"))
if mibBuilder.loadTexts: carrierAggrActuatorEntry.setStatus('current')
if mibBuilder.loadTexts: carrierAggrActuatorEntry.setDescription('A row in the carrierAggrActuatorTable.')
carrierAggrActuatorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrActuatorIndex.setStatus('current')
if mibBuilder.loadTexts: carrierAggrActuatorIndex.setDescription('This object identifies the carrier aggr Actuator inside the\n             Network Element.')
carrierAggrActuatorRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrActuatorRowStatus.setStatus('current')
if mibBuilder.loadTexts: carrierAggrActuatorRowStatus.setDescription('The status of this entry.\n\n             An entry may not exist in the active state unless all objects in\n             the entry have an appropriate value: carrierAggrActuatorIfIndex\n             must be set to a valid ifIndex number and carrierAggrActuatorSensorIndex\n             must be set to a valid sensor, Otherwise, the error inconsistentValue\n             is returned on the attempt to set active this row.\n\n             When set to notInService changes may be made to carrierAggrActuatorIfIndex\n             and carrierAggrActuatorSensorIndex. Other objects can be changed \n             when carrierAggrActuatorRowStatus is set to active.\n            ')
carrierAggrActuatorAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("down", 1), ("up", 2))).clone('down')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrActuatorAdminStatus.setStatus('current')
if mibBuilder.loadTexts: carrierAggrActuatorAdminStatus.setDescription('Administative status of the actuator. The value down(1) turns it off. \n             Other actuators associated with the same sensor remain active.')
carrierAggrActuatorIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 4), InterfaceIndexOrZero()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrActuatorIfIndex.setStatus('current')
if mibBuilder.loadTexts: carrierAggrActuatorIfIndex.setDescription('This object accepts a greater than zero value to identify an\n             interface in ifTable. The notify received from the connected \n             sensor is forwarded to the remote aggregator to signal some\n             anomalies on this aggregated flow.\n            ')
carrierAggrActuatorSensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: carrierAggrActuatorSensorIndex.setStatus('current')
if mibBuilder.loadTexts: carrierAggrActuatorSensorIndex.setDescription('This object connects this actuator to a sensor.\n             ')
carrierAggrActuatorConcIpAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 104, 3, 1, 6), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: carrierAggrActuatorConcIpAddr.setStatus('current')
if mibBuilder.loadTexts: carrierAggrActuatorConcIpAddr.setDescription('This object is used to contain \n               the Ip address of the equipment connected with this Lan\n               (the concatenator unit)')
mibBuilder.exportSymbols("SIAE-CARRIER-AGGRL1-MIB", carrierAggrActuatorAdminStatus=carrierAggrActuatorAdminStatus, carrierAggrActuatorIndex=carrierAggrActuatorIndex, carrierAggr=carrierAggr, carrierAggrSensorHitlessCapability=carrierAggrSensorHitlessCapability, carrierAggrMibVersion=carrierAggrMibVersion, carrierAggrActuatorConcIpAddr=carrierAggrActuatorConcIpAddr, carrierAggrSensorAdminStatus=carrierAggrSensorAdminStatus, carrierAggrActuatorTable=carrierAggrActuatorTable, carrierAggrSensorIndex=carrierAggrSensorIndex, PYSNMP_MODULE_ID=carrierAggr, carrierAggrSensorHitlessMode=carrierAggrSensorHitlessMode, carrierAggrSensorRowstatus=carrierAggrSensorRowstatus, carrierAggrSensorHitlessBehaviour=carrierAggrSensorHitlessBehaviour, carrierAggrActuatorRowStatus=carrierAggrActuatorRowStatus, carrierAggrSensorHitlessProfile=carrierAggrSensorHitlessProfile, carrierAggrSensorIfIndex=carrierAggrSensorIfIndex, carrierAggrSensorEntry=carrierAggrSensorEntry, carrierAggrActuatorSensorIndex=carrierAggrActuatorSensorIndex, carrierAggrSensorTable=carrierAggrSensorTable, carrierAggrActuatorEntry=carrierAggrActuatorEntry, carrierAggrActuatorIfIndex=carrierAggrActuatorIfIndex, carrierAggrSensorHitlessStatus=carrierAggrSensorHitlessStatus)
