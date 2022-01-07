#
# PySNMP MIB module MIMOSA-NETWORKS-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-NETWORKS-BASE-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:30:20 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter64, MibIdentifier, enterprises, Integer32, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, IpAddress, ObjectIdentity, TimeTicks, NotificationType, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "MibIdentifier", "enterprises", "Integer32", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "IpAddress", "ObjectIdentity", "TimeTicks", "NotificationType", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mimosa = ModuleIdentity((1, 3, 6, 1, 4, 1, 43356))
mimosa.setRevisions(('2015-06-03 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mimosa.setRevisionsDescriptions(('First draft',))
if mibBuilder.loadTexts: mimosa.setLastUpdated('201506030000Z')
if mibBuilder.loadTexts: mimosa.setOrganization('Mimosa Networks\n    \t\t\t  www.mimosa.co')
if mibBuilder.loadTexts: mimosa.setContactInfo('postal:\n    \tMimosa Networks, Inc.\n\t\t300 Orchard City Dr.\n\t\tCampbell, CA 95008\n        email: support@mimosa.co')
if mibBuilder.loadTexts: mimosa.setDescription('Mimosa device MIB definitions')
mimosaProduct = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1))
mimosaMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2))
mimosaHardware = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1))
mimosaSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 2))
mimosaB5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 1))
mimosaB5Lite = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 2))
mimosaA5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 3))
mimosaC5 = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 1, 1, 4))
mimosaTrap = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 0))
mimosaMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1))
mimosaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 3))
mimosaConformanceGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 4))
mimosaTrapMib = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1))
mimosaWireless = MibIdentifier((1, 3, 6, 1, 4, 1, 43356, 2, 1, 2))
mimosaTrapMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 43356, 2, 3, 1)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaOldSpeed"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaNewSpeed"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaTrapMIBGroup = mimosaTrapMIBGroup.setStatus('current')
if mibBuilder.loadTexts: mimosaTrapMIBGroup.setDescription('A collection of objects providing basic Trap function.')
mimosaTrapMessage = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTrapMessage.setStatus('current')
if mibBuilder.loadTexts: mimosaTrapMessage.setDescription('General Octet String object to contain message sent with traps.')
mimosaOldSpeed = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaOldSpeed.setStatus('current')
if mibBuilder.loadTexts: mimosaOldSpeed.setDescription('The speed of the Ethernet link before the change within Ethernet\n         Speed Change Notifications.')
mimosaNewSpeed = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaNewSpeed.setStatus('current')
if mibBuilder.loadTexts: mimosaNewSpeed.setDescription('The speed of the Ethernet link after the change within Ethernet\n         Speed Change Notifications.')
mimosaGenericNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 43356, 2, 3, 2)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaCriticalFault"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTempWarning"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTempNormal"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaEthernetSpeedChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaGenericNotificationsGroup = mimosaGenericNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: mimosaGenericNotificationsGroup.setDescription('The basic Trap notifications for all Mimosa products.')
mimosaCriticalFault = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 1)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaCriticalFault.setStatus('current')
if mibBuilder.loadTexts: mimosaCriticalFault.setDescription('The mimosaCriticalFault notification is sent when the log manager\n         in the Mimosa product determines that a fault with a critical\n         severity has been detected. The mimosaCriticalFaultLog contains\n         the description of the general error.')
mimosaTempWarning = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 2)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaTempWarning.setStatus('current')
if mibBuilder.loadTexts: mimosaTempWarning.setDescription('The mimosaTempWarning notification is sent when the log manager in\n         the Mimosa product receives an indication that the temperature is\n         outside the safe range.')
mimosaTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 3)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaTempNormal.setStatus('current')
if mibBuilder.loadTexts: mimosaTempNormal.setDescription('The mimosaTempNormal notification is sent when the log manager in the\n         Mimosa product receives an indication that the temperature is with\n         in the safe range.')
mimosaEthernetSpeedChange = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaOldSpeed"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaNewSpeed"))
if mibBuilder.loadTexts: mimosaEthernetSpeedChange.setStatus('current')
if mibBuilder.loadTexts: mimosaEthernetSpeedChange.setDescription('The mimosaEthernetSpeedChange notification is sent when the log manager\n         in the Mimosa product determines that a speed change on the Ethernet\n         port was detected. The mimosaOldSpeed and mimosaNewSpeed indicates the\n         speed in bits per second of the change. ifIndex is used per the ifTable\n         in the IF-MIB.')
mibBuilder.exportSymbols("MIMOSA-NETWORKS-BASE-MIB", mimosaMgmt=mimosaMgmt, mimosaConformanceGroup=mimosaConformanceGroup, mimosaNewSpeed=mimosaNewSpeed, mimosaHardware=mimosaHardware, mimosaMib=mimosaMib, mimosaWireless=mimosaWireless, mimosaCriticalFault=mimosaCriticalFault, mimosaB5=mimosaB5, mimosaEthernetSpeedChange=mimosaEthernetSpeedChange, mimosaGenericNotificationsGroup=mimosaGenericNotificationsGroup, mimosaTempWarning=mimosaTempWarning, mimosaTrapMIBGroup=mimosaTrapMIBGroup, PYSNMP_MODULE_ID=mimosa, mimosaMIBGroups=mimosaMIBGroups, mimosaOldSpeed=mimosaOldSpeed, mimosa=mimosa, mimosaTrapMib=mimosaTrapMib, mimosaC5=mimosaC5, mimosaSoftware=mimosaSoftware, mimosaProduct=mimosaProduct, mimosaTrap=mimosaTrap, mimosaA5=mimosaA5, mimosaB5Lite=mimosaB5Lite, mimosaTrapMessage=mimosaTrapMessage, mimosaTempNormal=mimosaTempNormal)
