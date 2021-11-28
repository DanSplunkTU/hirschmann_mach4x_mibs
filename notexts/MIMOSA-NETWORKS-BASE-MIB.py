#
# PySNMP MIB module MIMOSA-NETWORKS-BASE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mimosa/MIMOSA-NETWORKS-BASE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:16:16 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, Counter32, Gauge32, ObjectIdentity, Counter64, NotificationType, MibIdentifier, ModuleIdentity, enterprises, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "Counter32", "Gauge32", "ObjectIdentity", "Counter64", "NotificationType", "MibIdentifier", "ModuleIdentity", "enterprises", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mimosa = ModuleIdentity((1, 3, 6, 1, 4, 1, 43356))
mimosa.setRevisions(('2015-06-03 00:00',))
if mibBuilder.loadTexts: mimosa.setLastUpdated('201506030000Z')
if mibBuilder.loadTexts: mimosa.setOrganization('Mimosa Networks www.mimosa.co')
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
mimosaTrapMessage = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaTrapMessage.setStatus('current')
mimosaOldSpeed = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaOldSpeed.setStatus('current')
mimosaNewSpeed = MibScalar((1, 3, 6, 1, 4, 1, 43356, 2, 1, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: mimosaNewSpeed.setStatus('current')
mimosaGenericNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 43356, 2, 3, 2)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaCriticalFault"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTempWarning"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaTempNormal"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaEthernetSpeedChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    mimosaGenericNotificationsGroup = mimosaGenericNotificationsGroup.setStatus('current')
mimosaCriticalFault = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 1)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaCriticalFault.setStatus('current')
mimosaTempWarning = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 2)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaTempWarning.setStatus('current')
mimosaTempNormal = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 3)).setObjects(("MIMOSA-NETWORKS-BASE-MIB", "mimosaTrapMessage"))
if mibBuilder.loadTexts: mimosaTempNormal.setStatus('current')
mimosaEthernetSpeedChange = NotificationType((1, 3, 6, 1, 4, 1, 43356, 2, 0, 4)).setObjects(("IF-MIB", "ifIndex"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaOldSpeed"), ("MIMOSA-NETWORKS-BASE-MIB", "mimosaNewSpeed"))
if mibBuilder.loadTexts: mimosaEthernetSpeedChange.setStatus('current')
mibBuilder.exportSymbols("MIMOSA-NETWORKS-BASE-MIB", mimosaTrapMib=mimosaTrapMib, mimosaProduct=mimosaProduct, mimosaCriticalFault=mimosaCriticalFault, mimosaTrapMessage=mimosaTrapMessage, mimosaMib=mimosaMib, mimosaTrap=mimosaTrap, mimosaA5=mimosaA5, mimosaMIBGroups=mimosaMIBGroups, mimosaNewSpeed=mimosaNewSpeed, mimosaEthernetSpeedChange=mimosaEthernetSpeedChange, mimosaGenericNotificationsGroup=mimosaGenericNotificationsGroup, mimosaSoftware=mimosaSoftware, PYSNMP_MODULE_ID=mimosa, mimosaC5=mimosaC5, mimosaMgmt=mimosaMgmt, mimosaConformanceGroup=mimosaConformanceGroup, mimosaOldSpeed=mimosaOldSpeed, mimosaB5Lite=mimosaB5Lite, mimosaB5=mimosaB5, mimosa=mimosa, mimosaTempWarning=mimosaTempWarning, mimosaTrapMIBGroup=mimosaTrapMIBGroup, mimosaHardware=mimosaHardware, mimosaWireless=mimosaWireless, mimosaTempNormal=mimosaTempNormal)
