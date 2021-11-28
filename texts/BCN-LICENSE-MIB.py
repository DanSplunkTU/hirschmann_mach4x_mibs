#
# PySNMP MIB module BCN-LICENSE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/bluecatnetworks/BCN-LICENSE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:22:04 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
bcnServices, = mibBuilder.importSymbols("BCN-SMI-MIB", "bcnServices")
BcnAlarmSeverity, = mibBuilder.importSymbols("BCN-TC-MIB", "BcnAlarmSeverity")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, ModuleIdentity, Counter32, iso, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Gauge32, ObjectIdentity, Integer32, IpAddress, MibIdentifier, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Counter32", "iso", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Gauge32", "ObjectIdentity", "Integer32", "IpAddress", "MibIdentifier", "Bits")
TextualConvention, TruthValue, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "DateAndTime")
bcnLicenseMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 1))
bcnLicenseMIB.setRevisions(('2010-11-30 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bcnLicenseMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: bcnLicenseMIB.setLastUpdated('201011301200Z')
if mibBuilder.loadTexts: bcnLicenseMIB.setOrganization('BlueCat Networks')
if mibBuilder.loadTexts: bcnLicenseMIB.setContactInfo('BlueCat Networks. Customer Care.\n\n        North America\n        Call: +1.866.491.2228\n        Europe\n        Call: +44.8081.011.306\n        Other\n        Call: +1.416.646.8433\n        \n        Email: support@bluecatnetworks.com')
if mibBuilder.loadTexts: bcnLicenseMIB.setDescription('This module provides information and status about features that\n         are licensed to run on the system.')
bcnLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6))
bcnLicenseObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2))
bcnLicenseNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3))
bcnLicenseConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4))
bcnLicenseInformation = ObjectIdentity((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1))
if mibBuilder.loadTexts: bcnLicenseInformation.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseInformation.setDescription('General state of the License Service.')
bcnLicenseTable = MibTable((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2), )
if mibBuilder.loadTexts: bcnLicenseTable.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseTable.setDescription('This table keeps the information about the licenses installed')
bcnLicenseEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1), ).setIndexNames((0, "BCN-LICENSE-MIB", "bcnLicenseTableIndex"))
if mibBuilder.loadTexts: bcnLicenseEntry.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseEntry.setDescription('A logical row in the bcnLicenseTable.')
bcnLicenseTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 1), Unsigned32())
if mibBuilder.loadTexts: bcnLicenseTableIndex.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseTableIndex.setDescription('A unique running value greater than 0, used as index into the\n       table. The values of this index are assigned contiguously\n       starting normally from 1.')
bcnLicenseType = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("singleServer", 1), ("multiServer", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseType.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseType.setDescription('Type of license. The possible states are:\n        singleServer(1)  The license affects a single server, normally the\n                         server in which it is installed.\n        multiServer(2)   The license affects multiple servers. This is common\n                         for licenses that limit managed units.\n        ')
bcnLicenseDescription = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseDescription.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseDescription.setDescription('A text value describing the type of license installed.')
bcnLicenseInstalled = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseInstalled.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseInstalled.setDescription('The date when the license was installedon the system.')
bcnLicenseExpiry = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 5), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseExpiry.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseExpiry.setDescription('The expiration date for the license.')
bcnLicenseGracePeriod = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseGracePeriod.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseGracePeriod.setDescription('Number of days after the license has expired the functionality\n       will continue to work. In case this is not applicable the value\n       is 0.')
bcnLicenseValid = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 7), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseValid.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseValid.setDescription('Number of days after the license has expired the functionality\n       will continue to work. In case this is not applicable the value\n       is 0.')
bcnLicenseItemsGranted = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 8), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseItemsGranted.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseItemsGranted.setDescription('Number of items granted with this license. On a multiServer license\n        this is normally the number of units allowed to be managed under\n        this license. On a singleServer license, this value is undefined.\n        If the license is of type multiServer and bcnLicenseItemsGranted\n        is zero, that indicates that the license is unlimited.')
bcnLicenseItemsUsed = MibTableColumn((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 2, 1, 2, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: bcnLicenseItemsUsed.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseItemsUsed.setDescription('Number of items consumed under this license. On a multiServer\n        license this is the number of units that have already been allocated.\n        On a singleServer license, this value is undefined.')
bcnLicenseNotificationEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 0))
bcnLicenseNotificationData = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 1))
bcnLicenseAlarmSeverity = MibScalar((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 1, 1), BcnAlarmSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: bcnLicenseAlarmSeverity.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseAlarmSeverity.setDescription('Severity classification for the alarm.')
bcnLicenseExpiryNotif = NotificationType((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 3, 0, 1)).setObjects(("BCN-LICENSE-MIB", "bcnLicenseType"), ("BCN-LICENSE-MIB", "bcnLicenseAlarmSeverity"), ("BCN-LICENSE-MIB", "bcnLicenseExpiry"), ("BCN-LICENSE-MIB", "bcnLicenseGracePeriod"), ("BCN-LICENSE-MIB", "bcnLicenseValid"))
if mibBuilder.loadTexts: bcnLicenseExpiryNotif.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseExpiryNotif.setDescription('A bcnLicenseAlarmNotif signifies that the License service has transitioned\n        state or a particular event has been detected on the service.')
bcnLicenseServiceCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 1))
bcnLicenseServiceGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2))
bcnLicenseServiceStatusGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2, 1)).setObjects(("BCN-LICENSE-MIB", "bcnLicenseType"), ("BCN-LICENSE-MIB", "bcnLicenseDescription"), ("BCN-LICENSE-MIB", "bcnLicenseInstalled"), ("BCN-LICENSE-MIB", "bcnLicenseExpiry"), ("BCN-LICENSE-MIB", "bcnLicenseGracePeriod"), ("BCN-LICENSE-MIB", "bcnLicenseValid"), ("BCN-LICENSE-MIB", "bcnLicenseItemsGranted"), ("BCN-LICENSE-MIB", "bcnLicenseItemsUsed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnLicenseServiceStatusGroup = bcnLicenseServiceStatusGroup.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseServiceStatusGroup.setDescription('Status conformance.')
bcnLicenseNotificationEventGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2, 2)).setObjects(("BCN-LICENSE-MIB", "bcnLicenseExpiryNotif"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnLicenseNotificationEventGroup = bcnLicenseNotificationEventGroup.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseNotificationEventGroup.setDescription('Server statistics conformance.')
bcnLicenseNotificationDataGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 2, 3)).setObjects(("BCN-LICENSE-MIB", "bcnLicenseAlarmSeverity"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnLicenseNotificationDataGroup = bcnLicenseNotificationDataGroup.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseNotificationDataGroup.setDescription('Server statistics conformance.')
bcnLicenseStatusCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13315, 3, 1, 6, 4, 1, 1)).setObjects(("BCN-LICENSE-MIB", "bcnLicenseServiceStatusGroup"), ("BCN-LICENSE-MIB", "bcnLicenseNotificationEventGroup"), ("BCN-LICENSE-MIB", "bcnLicenseNotificationDataGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    bcnLicenseStatusCompliance = bcnLicenseStatusCompliance.setStatus('current')
if mibBuilder.loadTexts: bcnLicenseStatusCompliance.setDescription('Basic conformance')
mibBuilder.exportSymbols("BCN-LICENSE-MIB", bcnLicenseNotificationEventGroup=bcnLicenseNotificationEventGroup, bcnLicenseNotificationDataGroup=bcnLicenseNotificationDataGroup, bcnLicenseExpiryNotif=bcnLicenseExpiryNotif, bcnLicenseDescription=bcnLicenseDescription, bcnLicenseAlarmSeverity=bcnLicenseAlarmSeverity, bcnLicenseNotificationEvents=bcnLicenseNotificationEvents, bcnLicenseNotification=bcnLicenseNotification, bcnLicenseEntry=bcnLicenseEntry, bcnLicenseInformation=bcnLicenseInformation, bcnLicenseTable=bcnLicenseTable, bcnLicenseValid=bcnLicenseValid, bcnLicenseExpiry=bcnLicenseExpiry, bcnLicenseInstalled=bcnLicenseInstalled, bcnLicenseType=bcnLicenseType, bcnLicenseGracePeriod=bcnLicenseGracePeriod, bcnLicenseObjects=bcnLicenseObjects, bcnLicenseTableIndex=bcnLicenseTableIndex, bcnLicenseServiceCompliances=bcnLicenseServiceCompliances, bcnLicense=bcnLicense, bcnLicenseServiceGroups=bcnLicenseServiceGroups, bcnLicenseServiceStatusGroup=bcnLicenseServiceStatusGroup, bcnLicenseConformance=bcnLicenseConformance, bcnLicenseItemsGranted=bcnLicenseItemsGranted, bcnLicenseMIB=bcnLicenseMIB, bcnLicenseItemsUsed=bcnLicenseItemsUsed, bcnLicenseNotificationData=bcnLicenseNotificationData, PYSNMP_MODULE_ID=bcnLicenseMIB, bcnLicenseStatusCompliance=bcnLicenseStatusCompliance)
