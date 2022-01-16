#
# PySNMP MIB module VMWARE-VC-EVENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/vmware/VMWARE-VC-EVENT-MIB
# Produced by pysmi-1.1.8 at Sun Jan 16 00:45:13 2022
# On host fv-az42-839 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
ModuleIdentity, Counter32, ObjectIdentity, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, MibIdentifier, Gauge32, Counter64, IpAddress, Integer32, NotificationType, iso = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter32", "ObjectIdentity", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "MibIdentifier", "Gauge32", "Counter64", "IpAddress", "Integer32", "NotificationType", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vmwVC, = mibBuilder.importSymbols("VMWARE-PRODUCTS-MIB", "vmwVC")
VmwLongSnmpAdminString, = mibBuilder.importSymbols("VMWARE-TC-MIB", "VmwLongSnmpAdminString")
vmwVCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1))
vmwVCMIB.setRevisions(('2009-12-15 00:00', '2009-09-08 00:00', '2009-05-27 00:00', '2009-04-06 00:00', '2009-03-17 00:00', '2008-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vmwVCMIB.setRevisionsDescriptions(('Notification vpxdAlarm is now obsolete and is replaced with vpxdAlarmInfo,\n     new object group vmwVCAlarmGroup is created making the vmwVCAlarmInfoGroup\n     obsolete, new notification group vmwVCAlarmNotificationGroup is created\n     making vmwVCNotificationGroup obsolete,new varbinds vmwVpxdTargetObj and\n     vmwVpxdTargetObjType are added, var binds vmwVpxdHostName, vmwVpxdVMName\n     and vmwVpxdTrapType have become obsolete.', 'VC SNMP Agent has always used UTF-8 in notifications,\n      update this MIB module to reflect that.', 'Updated comments on the alarm trap and parameters with more detail.', 'Swap vmwVpxdNewStatus and vmwVpxdOldStatus to match code implementation.', 'Changed vmwVpxdObjValue be of type vmwLongDisplayString', 'This is the first revision in SMIv2 format. Prior version was published as SMIv1.\n     Notifications were formerly in the VMWARE-TRAPS-MIB module.',))
if mibBuilder.loadTexts: vmwVCMIB.setLastUpdated('200912150000Z')
if mibBuilder.loadTexts: vmwVCMIB.setOrganization('VMware, Inc')
if mibBuilder.loadTexts: vmwVCMIB.setContactInfo('VMware, Inc\n    3401 Hillview Ave\n    Palo Alto, CA 94304\n    Tel: 1-877-486-9273 or 650-427-5000\n    Fax: 650-427-5001\n    Web: http://communities.vmware.com/community/developer/forums/managementapi\n    ')
if mibBuilder.loadTexts: vmwVCMIB.setDescription('This MIB module identifies vCenter Trap notifications (traps or inform).')
vmwVCNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0))
vpxdAlarm = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 201)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTrapType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdHostName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdVMName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"))
if mibBuilder.loadTexts: vpxdAlarm.setStatus('obsolete')
if mibBuilder.loadTexts: vpxdAlarm.setDescription('This notification is sent on entity alarm state change, by the vCenter Server SNMP agent.\n         This information is also available through the vSphere client, through the Alarms screen,\n         or through the Managed Object Browser(MOB) interface for alarms at\n         https://<vCenter Server machine address>/mob/?moid=AlarmManager.\n         Listing individual objects of a specific type or ID can be done through the PropertyCollector SDK API.\n         See http://www.vmware.com/support/developer/vc-sdk/visdk2xpubs/ReferenceGuide/vmodl.query.PropertyCollector.html\n         for details.')
vpxdDiagnostic = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 202))
if mibBuilder.loadTexts: vpxdDiagnostic.setStatus('current')
if mibBuilder.loadTexts: vpxdDiagnostic.setDescription('This notification is sent on starting or restarting vCenter Server,\n         on requesting a test notification explicitly, and can also be\n         configured to be sent periodically at a specified time interval via\n         vCenter Server configuration by the vCenter Server SNMP agent.')
vpxdAlarmInfo = NotificationType((1, 3, 6, 1, 4, 1, 6876, 4, 3, 0, 203)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObjType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObj"))
if mibBuilder.loadTexts: vpxdAlarmInfo.setStatus('current')
if mibBuilder.loadTexts: vpxdAlarmInfo.setDescription('This notification is sent on entity alarm state change, by the vCenter Server SNMP agent.\n         This information is also available through the vSphere client, through the Alarms screen,\n         or through the Managed Object Browser(MOB) interface for alarms at\n         https://<vCenter Server machine address>/mob/?moid=AlarmManager.\n         Listing individual objects of a specific type or ID can be done through the PropertyCollector SDK API.\n         See http://www.vmware.com/support/developer/vc-sdk/visdk2xpubs/ReferenceGuide/vmodl.query.PropertyCollector.html\n         for details.')
vmwVpxdTrapType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 301), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdTrapType.setStatus('obsolete')
if mibBuilder.loadTexts: vmwVpxdTrapType.setDescription('This is the alarm notification type.')
vmwVpxdHostName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 302), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdHostName.setStatus('obsolete')
if mibBuilder.loadTexts: vmwVpxdHostName.setDescription('This is the name of the vSphere host in the notification.')
vmwVpxdVMName = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 303), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdVMName.setStatus('obsolete')
if mibBuilder.loadTexts: vmwVpxdVMName.setDescription('This is the name of the VM in the notification.')
vmwVpxdOldStatus = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 304), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdOldStatus.setStatus('current')
if mibBuilder.loadTexts: vmwVpxdOldStatus.setDescription('This is the old status in the notification.')
vmwVpxdNewStatus = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 305), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdNewStatus.setStatus('current')
if mibBuilder.loadTexts: vmwVpxdNewStatus.setDescription('This is the new status in the notification.')
vmwVpxdObjValue = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 306), VmwLongSnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdObjValue.setStatus('current')
if mibBuilder.loadTexts: vmwVpxdObjValue.setDescription('This is the current object value in the notification.')
vmwVpxdTargetObj = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 307), SnmpAdminString()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdTargetObj.setStatus('current')
if mibBuilder.loadTexts: vmwVpxdTargetObj.setDescription('This is the current object in the notification. This may be\n\tone of esx host name, vm name, or other. This value must not be empty.')
vmwVpxdTargetObjType = MibScalar((1, 3, 6, 1, 4, 1, 6876, 4, 3, 308), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("host", 2), ("vm", 3), ("other", 4)))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: vmwVpxdTargetObjType.setStatus('current')
if mibBuilder.loadTexts: vmwVpxdTargetObjType.setDescription('This is the alarm target object type.')
vmwVCMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2))
vmwVCMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1))
vmwVCMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2))
vmwVCMIBBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1, 2)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVCAlarmInfoGroup"), ("VMWARE-VC-EVENT-MIB", "vmwVCNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCMIBBasicCompliance = vmwVCMIBBasicCompliance.setStatus('obsolete')
if mibBuilder.loadTexts: vmwVCMIBBasicCompliance.setDescription('The compliance statement for entities which implement VMWARE-VC-EVENT-MIB.')
vmwVCMIBBasicComplianceRev2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 1, 3)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVCAlarmGroup"), ("VMWARE-VC-EVENT-MIB", "vmwVCAlarmNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCMIBBasicComplianceRev2 = vmwVCMIBBasicComplianceRev2.setStatus('current')
if mibBuilder.loadTexts: vmwVCMIBBasicComplianceRev2.setDescription('The compliance statement for entities which implement VMWARE-VC-EVENT-MIB.')
vmwVCAlarmInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 1)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTrapType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdHostName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdVMName"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCAlarmInfoGroup = vmwVCAlarmInfoGroup.setStatus('obsolete')
if mibBuilder.loadTexts: vmwVCAlarmInfoGroup.setDescription('These objects provide alarm notification details.')
vmwVCNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 2)).setObjects(("VMWARE-VC-EVENT-MIB", "vpxdAlarm"), ("VMWARE-VC-EVENT-MIB", "vpxdDiagnostic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCNotificationGroup = vmwVCNotificationGroup.setStatus('obsolete')
if mibBuilder.loadTexts: vmwVCNotificationGroup.setDescription('Group of objects describing notifications (traps).')
vmwVCAlarmGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 3)).setObjects(("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObjType"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdOldStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdNewStatus"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdObjValue"), ("VMWARE-VC-EVENT-MIB", "vmwVpxdTargetObj"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCAlarmGroup = vmwVCAlarmGroup.setStatus('current')
if mibBuilder.loadTexts: vmwVCAlarmGroup.setDescription('These objects provide alarm notification details.')
vmwVCAlarmNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 6876, 4, 3, 1, 2, 2, 4)).setObjects(("VMWARE-VC-EVENT-MIB", "vpxdAlarmInfo"), ("VMWARE-VC-EVENT-MIB", "vpxdDiagnostic"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    vmwVCAlarmNotificationGroup = vmwVCAlarmNotificationGroup.setStatus('current')
if mibBuilder.loadTexts: vmwVCAlarmNotificationGroup.setDescription('Group of objects describing notifications (traps).')
mibBuilder.exportSymbols("VMWARE-VC-EVENT-MIB", vmwVpxdObjValue=vmwVpxdObjValue, vmwVCMIBCompliances=vmwVCMIBCompliances, vpxdAlarmInfo=vpxdAlarmInfo, vmwVCAlarmInfoGroup=vmwVCAlarmInfoGroup, vmwVpxdOldStatus=vmwVpxdOldStatus, vmwVCAlarmGroup=vmwVCAlarmGroup, vmwVCMIBBasicCompliance=vmwVCMIBBasicCompliance, vmwVCAlarmNotificationGroup=vmwVCAlarmNotificationGroup, vmwVCMIBConformance=vmwVCMIBConformance, vmwVCNotifications=vmwVCNotifications, vmwVpxdNewStatus=vmwVpxdNewStatus, vmwVpxdVMName=vmwVpxdVMName, vmwVCMIBBasicComplianceRev2=vmwVCMIBBasicComplianceRev2, vmwVpxdTargetObj=vmwVpxdTargetObj, vpxdDiagnostic=vpxdDiagnostic, vpxdAlarm=vpxdAlarm, vmwVCMIB=vmwVCMIB, vmwVCMIBGroups=vmwVCMIBGroups, vmwVpxdTrapType=vmwVpxdTrapType, vmwVpxdHostName=vmwVpxdHostName, vmwVpxdTargetObjType=vmwVpxdTargetObjType, PYSNMP_MODULE_ID=vmwVCMIB, vmwVCNotificationGroup=vmwVCNotificationGroup)
