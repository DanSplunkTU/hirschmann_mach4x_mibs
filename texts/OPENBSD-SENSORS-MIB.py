#
# PySNMP MIB module OPENBSD-SENSORS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/openbsd/OPENBSD-SENSORS-MIB
# Produced by pysmi-1.1.3 at Sun Nov 21 00:49:21 2021
# On host fv-az39-63 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint")
openBSD, = mibBuilder.importSymbols("OPENBSD-BASE-MIB", "openBSD")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Bits, Integer32, enterprises, ObjectIdentity, Counter32, MibIdentifier, Counter64, IpAddress, Gauge32, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, iso, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Bits", "Integer32", "enterprises", "ObjectIdentity", "Counter32", "MibIdentifier", "Counter64", "IpAddress", "Gauge32", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "iso", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sensorsMIBObjects = ModuleIdentity((1, 3, 6, 1, 4, 1, 30155, 2))
sensorsMIBObjects.setRevisions(('2012-09-20 00:00', '2012-01-31 00:00', '2008-12-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sensorsMIBObjects.setRevisionsDescriptions(('Add new sensor types.', 'Update email address.', 'Updated for MIB for the OpenBSD snmpd(8) implementation.',))
if mibBuilder.loadTexts: sensorsMIBObjects.setLastUpdated('201209200000Z')
if mibBuilder.loadTexts: sensorsMIBObjects.setOrganization('OpenBSD')
if mibBuilder.loadTexts: sensorsMIBObjects.setContactInfo('Editor:    Reyk Floeter\n\t    EMail:      reyk@openbsd.org\n\t    WWW:        http://www.openbsd.org/\n\n\t    Editor:     Joel Knight\n\t    EMail:      knight.joel@gmail.com\n\t    WWW:        http://www.packetmischief.ca/openbsd-snmp-mibs/')
if mibBuilder.loadTexts: sensorsMIBObjects.setDescription("The MIB module for gathering information from\n\t    OpenBSD's kernel sensor framework.")
sensors = MibIdentifier((1, 3, 6, 1, 4, 1, 30155, 2, 1))
sensorNumber = MibScalar((1, 3, 6, 1, 4, 1, 30155, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorNumber.setStatus('current')
if mibBuilder.loadTexts: sensorNumber.setDescription('The number of sensors present on this system.')
sensorTable = MibTable((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2), )
if mibBuilder.loadTexts: sensorTable.setStatus('current')
if mibBuilder.loadTexts: sensorTable.setDescription('A list of individual sensors. The number of entries is\n\t    given by the value of sensorNumber.')
sensorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1), ).setIndexNames((0, "OPENBSD-SENSORS-MIB", "sensorIndex"))
if mibBuilder.loadTexts: sensorEntry.setStatus('current')
if mibBuilder.loadTexts: sensorEntry.setDescription('An entry containing management information applicable to a\n\t    particular sensor.')
sensorIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorIndex.setStatus('current')
if mibBuilder.loadTexts: sensorIndex.setDescription('A unique value, greater than zero, for each sensor.')
sensorDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorDescr.setStatus('current')
if mibBuilder.loadTexts: sensorDescr.setDescription('A description of the sensor indicating what information the\n\t    sensor is monitoring.')
sensorType = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))).clone(namedValues=NamedValues(("temperature", 0), ("fan", 1), ("voltsdc", 2), ("voltsac", 3), ("resistance", 4), ("power", 5), ("current", 6), ("watthour", 7), ("amphour", 8), ("indicator", 9), ("raw", 10), ("percent", 11), ("illuminance", 12), ("drive", 13), ("timedelta", 14), ("humidity", 15), ("freq", 16), ("angle", 17), ("distance", 18), ("pressure", 19), ("accel", 20)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorType.setStatus('current')
if mibBuilder.loadTexts: sensorType.setDescription('Indicates the type of sensor.')
sensorDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorDevice.setStatus('current')
if mibBuilder.loadTexts: sensorDevice.setDescription('The name of the sensor driver that provides the sensor.')
sensorValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorValue.setStatus('current')
if mibBuilder.loadTexts: sensorValue.setDescription('The value the sensor is currently reporting.')
sensorUnits = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorUnits.setStatus('current')
if mibBuilder.loadTexts: sensorUnits.setDescription('The units that the sensor reports in.')
sensorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 30155, 2, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("unspecified", 0), ("ok", 1), ("warn", 2), ("critical", 3), ("unknown", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: sensorStatus.setStatus('current')
if mibBuilder.loadTexts: sensorStatus.setDescription('Indicates whether the sensor value is within an acceptable\n\t    range.')
mibBuilder.exportSymbols("OPENBSD-SENSORS-MIB", sensorEntry=sensorEntry, sensorDescr=sensorDescr, sensors=sensors, sensorDevice=sensorDevice, sensorValue=sensorValue, sensorUnits=sensorUnits, sensorTable=sensorTable, sensorNumber=sensorNumber, sensorType=sensorType, sensorStatus=sensorStatus, PYSNMP_MODULE_ID=sensorsMIBObjects, sensorIndex=sensorIndex, sensorsMIBObjects=sensorsMIBObjects)
