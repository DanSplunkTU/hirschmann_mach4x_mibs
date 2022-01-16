#
# PySNMP MIB module MDS-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/gemds/MDS-EVENT-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:37:23 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
mdsLogging, = mibBuilder.importSymbols("MDS-ORBIT-SMI-MIB", "mdsLogging")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter64, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Counter32, IpAddress, Bits, Gauge32, MibIdentifier, NotificationType, Integer32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Counter32", "IpAddress", "Bits", "Gauge32", "MibIdentifier", "NotificationType", "Integer32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mdsEventMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1))
mdsEventMIB.setRevisions(('2018-05-16 00:00', '2013-04-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mdsEventMIB.setRevisionsDescriptions(('Updated conformance statments based on smilint.', 'Initial version.',))
if mibBuilder.loadTexts: mdsEventMIB.setLastUpdated('201805160000Z')
if mibBuilder.loadTexts: mdsEventMIB.setOrganization('GE MDS LLC\n        http://www.gemds.com')
if mibBuilder.loadTexts: mdsEventMIB.setContactInfo('T 1-800-474-0694 (Toll Free in North America)\n        T 585-242-9600\n        F 585-242-9620\n\n        175 Science Parkway\n        Rochester, New York 14620\n        USA')
if mibBuilder.loadTexts: mdsEventMIB.setDescription('Notifications for GE MDS products.')
mdsEventMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1))
mdsEventMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2))
mdsEventVariables = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1))
mdsEventName = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdsEventName.setStatus('current')
if mibBuilder.loadTexts: mdsEventName.setDescription('The name of the event.')
mdsEventInfoInCee = MibScalar((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: mdsEventInfoInCee.setStatus('current')
if mibBuilder.loadTexts: mdsEventInfoInCee.setDescription('The detailed information about the event encoded \n        in Common Event Expression (CEE) format.')
traps0 = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1))
traps = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1, 0))
mdsEvent = NotificationType((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 2, 1, 0, 1))
if mibBuilder.loadTexts: mdsEvent.setStatus('current')
if mibBuilder.loadTexts: mdsEvent.setDescription('This is the common notification sent for any events\n        generated by various subsystems in the product.')
mdsEventMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3))
mdsEventMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 1))
mdsEventMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2))
mdsEventMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 1, 2)).setObjects(("MDS-EVENT-MIB", "mdsEventNotificationsGroup"), ("MDS-EVENT-MIB", "mdsEventVariablesCeeGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdsEventMIBCompliance = mdsEventMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: mdsEventMIBCompliance.setDescription('The compliance statement for SNMP entities that\n        implement the MDS-EVENT-MIB.')
mdsEventNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2, 1)).setObjects(("MDS-EVENT-MIB", "mdsEvent"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdsEventNotificationsGroup = mdsEventNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: mdsEventNotificationsGroup.setDescription('The common notifications.')
mdsEventVariablesCeeGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 4130, 10, 4, 1, 3, 2, 2)).setObjects(("MDS-EVENT-MIB", "mdsEventName"), ("MDS-EVENT-MIB", "mdsEventInfoInCee"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mdsEventVariablesCeeGroup = mdsEventVariablesCeeGroup.setStatus('current')
if mibBuilder.loadTexts: mdsEventVariablesCeeGroup.setDescription('Information to support events that encode event \n        information in CEE format.')
mibBuilder.exportSymbols("MDS-EVENT-MIB", mdsEventNotificationsGroup=mdsEventNotificationsGroup, mdsEventVariables=mdsEventVariables, mdsEventMIBGroups=mdsEventMIBGroups, mdsEventName=mdsEventName, mdsEventMIBCompliance=mdsEventMIBCompliance, mdsEventMIB=mdsEventMIB, mdsEvent=mdsEvent, mdsEventVariablesCeeGroup=mdsEventVariablesCeeGroup, mdsEventMIBNotifications=mdsEventMIBNotifications, mdsEventMIBObjects=mdsEventMIBObjects, mdsEventMIBCompliances=mdsEventMIBCompliances, mdsEventInfoInCee=mdsEventInfoInCee, traps=traps, mdsEventMIBConformance=mdsEventMIBConformance, traps0=traps0, PYSNMP_MODULE_ID=mdsEventMIB)
