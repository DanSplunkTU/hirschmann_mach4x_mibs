#
# PySNMP MIB module MDS-SERVICE-GPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-SERVICE-GPS-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:12:52 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
mdsServices, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsServices")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Counter32, Integer32, Gauge32, NotificationType, Unsigned32, ObjectIdentity, ModuleIdentity, Counter64, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Counter32", "Integer32", "Gauge32", "NotificationType", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Counter64", "TimeTicks")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
mdsGpsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12))
mdsGpsMIB.setRevisions(('2018-05-16 00:00', '2016-06-06 00:00', '2015-01-29 00:00',))
if mibBuilder.loadTexts: mdsGpsMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsGpsMIB.setOrganization('GE MDS LLC http://www.gemds.com')
mGpsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1))
mGpsConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 1))
mGpsStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2))
mGpsStatusFixMode = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("nofix", 0), ("a2dfix", 1), ("a3dfix", 2))).clone('nofix')).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusFixMode.setStatus('current')
mGpsStatusTime = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusTime.setStatus('current')
mGpsStatusLatitude = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusLatitude.setStatus('current')
mGpsStatusLongitude = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusLongitude.setStatus('current')
mGpsStatusAltitude = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 5), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusAltitude.setStatus('current')
mGpsStatusSpeed = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 6), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusSpeed.setStatus('current')
mGpsStatusHeading = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 7), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusHeading.setStatus('current')
mGpsStatusSatellitesVisible = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusSatellitesVisible.setStatus('current')
mGpsStatusSatellitesUsed = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsStatusSatellitesUsed.setStatus('current')
mGpsSatellitesTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10), )
if mibBuilder.loadTexts: mGpsSatellitesTable.setStatus('current')
mGpsSatellitesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1), ).setIndexNames((0, "MDS-SERVICE-GPS-MIB", "mGpsSatellitesPrn"))
if mibBuilder.loadTexts: mGpsSatellitesEntry.setStatus('current')
mGpsSatellitesPrn = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: mGpsSatellitesPrn.setStatus('current')
mGpsSatellitesUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsSatellitesUsed.setStatus('current')
mGpsSatellitesElevation = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 3), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsSatellitesElevation.setStatus('current')
mGpsSatellitesAzimuth = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsSatellitesAzimuth.setStatus('current')
mGpsSatellitesSnr = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 2, 10, 1, 5), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsSatellitesSnr.setStatus('current')
mGpsSourcesTable = MibTable((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3), )
if mibBuilder.loadTexts: mGpsSourcesTable.setStatus('current')
mGpsSourcesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3, 1), ).setIndexNames((0, "MDS-SERVICE-GPS-MIB", "mGpsSourceName"))
if mibBuilder.loadTexts: mGpsSourcesEntry.setStatus('current')
mGpsSourceName = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3, 1, 1), DisplayString())
if mibBuilder.loadTexts: mGpsSourceName.setStatus('current')
mGpsSourceDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 1, 3, 1, 2), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mGpsSourceDevice.setStatus('current')
mdsGpsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3))
mdsGpsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 1))
mdsGpsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 2))
mGpsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 1, 1)).setObjects(("MDS-SERVICE-GPS-MIB", "mGpsStatusGroup"), ("MDS-SERVICE-GPS-MIB", "mGpsSourcesGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mGpsCompliance = mGpsCompliance.setStatus('current')
mGpsStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 2, 1)).setObjects(("MDS-SERVICE-GPS-MIB", "mGpsStatusFixMode"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusTime"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusLatitude"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusLongitude"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusAltitude"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusSpeed"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusHeading"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusSatellitesVisible"), ("MDS-SERVICE-GPS-MIB", "mGpsStatusSatellitesUsed"), ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesUsed"), ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesElevation"), ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesAzimuth"), ("MDS-SERVICE-GPS-MIB", "mGpsSatellitesSnr"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mGpsStatusGroup = mGpsStatusGroup.setStatus('current')
mGpsSourcesGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 3, 12, 3, 2, 2)).setObjects(("MDS-SERVICE-GPS-MIB", "mGpsSourceDevice"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mGpsSourcesGroup = mGpsSourcesGroup.setStatus('current')
mibBuilder.exportSymbols("MDS-SERVICE-GPS-MIB", mGpsStatus=mGpsStatus, mdsGpsMIB=mdsGpsMIB, mGpsSatellitesUsed=mGpsSatellitesUsed, mGpsStatusSatellitesVisible=mGpsStatusSatellitesVisible, mGpsSatellitesTable=mGpsSatellitesTable, PYSNMP_MODULE_ID=mdsGpsMIB, mGpsSatellitesSnr=mGpsSatellitesSnr, mGpsMIBObjects=mGpsMIBObjects, mGpsSourcesEntry=mGpsSourcesEntry, mGpsStatusLatitude=mGpsStatusLatitude, mGpsConfig=mGpsConfig, mGpsStatusHeading=mGpsStatusHeading, mGpsStatusTime=mGpsStatusTime, mGpsSourceDevice=mGpsSourceDevice, mdsGpsMIBGroups=mdsGpsMIBGroups, mdsGpsMIBCompliances=mdsGpsMIBCompliances, mGpsSatellitesElevation=mGpsSatellitesElevation, mGpsSourcesTable=mGpsSourcesTable, mGpsStatusGroup=mGpsStatusGroup, mdsGpsMIBConformance=mdsGpsMIBConformance, mGpsStatusLongitude=mGpsStatusLongitude, mGpsSourceName=mGpsSourceName, mGpsStatusFixMode=mGpsStatusFixMode, mGpsSatellitesEntry=mGpsSatellitesEntry, mGpsSatellitesPrn=mGpsSatellitesPrn, mGpsStatusSpeed=mGpsStatusSpeed, mGpsSatellitesAzimuth=mGpsSatellitesAzimuth, mGpsStatusSatellitesUsed=mGpsStatusSatellitesUsed, mGpsSourcesGroup=mGpsSourcesGroup, mGpsStatusAltitude=mGpsStatusAltitude, mGpsCompliance=mGpsCompliance)
