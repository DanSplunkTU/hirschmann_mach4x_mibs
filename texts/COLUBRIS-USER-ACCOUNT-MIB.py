#
# PySNMP MIB module COLUBRIS-USER-ACCOUNT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/hpmsm/COLUBRIS-USER-ACCOUNT-MIB.my
# Produced by pysmi-1.1.8 at Sat Jan 15 18:07:40 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
colubrisMgmtV2, = mibBuilder.importSymbols("COLUBRIS-SMI", "colubrisMgmtV2")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Integer32, MibIdentifier, ModuleIdentity, IpAddress, TimeTicks, Counter32, Unsigned32, Gauge32, Bits, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibIdentifier", "ModuleIdentity", "IpAddress", "TimeTicks", "Counter32", "Unsigned32", "Gauge32", "Bits", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
colubrisUserAccountMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 8744, 5, 35))
if mibBuilder.loadTexts: colubrisUserAccountMIB.setLastUpdated('200704180000Z')
if mibBuilder.loadTexts: colubrisUserAccountMIB.setOrganization('Colubris Networks, Inc.')
if mibBuilder.loadTexts: colubrisUserAccountMIB.setContactInfo('Colubris Networks\n                     Postal: 200 West Street Ste 300\n                             Waltham, Massachusetts 02451-1121\n                             UNITED STATES\n                     Phone:  +1 781 684 0001\n                     Fax:    +1 781 684 0009\n\n                     E-mail: cn-snmp@colubris.com')
if mibBuilder.loadTexts: colubrisUserAccountMIB.setDescription('Colubris User Account MIB.')
colubrisUserAccountMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1))
coUserAccountStatusGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1))
coUserAccountStatusTable = MibTable((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1), )
if mibBuilder.loadTexts: coUserAccountStatusTable.setStatus('current')
if mibBuilder.loadTexts: coUserAccountStatusTable.setDescription('User account attributes.')
coUserAccountStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1), ).setIndexNames((0, "COLUBRIS-USER-ACCOUNT-MIB", "coUserAccIndex"))
if mibBuilder.loadTexts: coUserAccountStatusEntry.setStatus('current')
if mibBuilder.loadTexts: coUserAccountStatusEntry.setDescription('An entry in the coUserAccountStatusTable.\n                 coUserAccIndex - Uniquely identifies a user account on\n                                  the MultiService Controller.')
coUserAccIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: coUserAccIndex.setStatus('current')
if mibBuilder.loadTexts: coUserAccIndex.setDescription('Specifies the index of the user account.')
coUserAccUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccUserName.setStatus('current')
if mibBuilder.loadTexts: coUserAccUserName.setDescription('User name corresponding to the user account.')
coUserAccPlanName = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccPlanName.setStatus('current')
if mibBuilder.loadTexts: coUserAccPlanName.setDescription('The name of the subscription plan name associated to\n                 this account.')
coUserAccRemainingOnlineTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 4), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccRemainingOnlineTime.setStatus('current')
if mibBuilder.loadTexts: coUserAccRemainingOnlineTime.setDescription('The online remaining time for this account.')
coUserAccFirstLoginTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccFirstLoginTime.setStatus('current')
if mibBuilder.loadTexts: coUserAccFirstLoginTime.setDescription('First login time recorded for this account.')
coUserAccRemainingSessionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 6), Integer32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccRemainingSessionTime.setStatus('current')
if mibBuilder.loadTexts: coUserAccRemainingSessionTime.setDescription('Time before next logout.')
coUserAccStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("valid", 1), ("invalid", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccStatus.setStatus('current')
if mibBuilder.loadTexts: coUserAccStatus.setDescription('Current Status of the user account based on the rules\n                 defined in the subscription plan.')
coUserAccExpirationTime = MibTableColumn((1, 3, 6, 1, 4, 1, 8744, 5, 35, 1, 1, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: coUserAccExpirationTime.setStatus('current')
if mibBuilder.loadTexts: coUserAccExpirationTime.setDescription('This field include the Date and time of the account\n                 expiration based on the subscription plan.')
colubrisUserAccountMIBNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 2))
colubrisUserAccountMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 2, 0))
colubrisUserAccountMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 3))
colubrisUserAccountMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 1))
colubrisUserAccountMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 2))
colubrisUserAccountMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 1, 1)).setObjects(("COLUBRIS-USER-ACCOUNT-MIB", "colubrisUserAccountStatusMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisUserAccountMIBCompliance = colubrisUserAccountMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: colubrisUserAccountMIBCompliance.setDescription('The compliance statement for the User Account MIB.')
colubrisUserAccountStatusMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 8744, 5, 35, 3, 2, 1)).setObjects(("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccUserName"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccPlanName"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccRemainingOnlineTime"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccFirstLoginTime"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccRemainingSessionTime"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccStatus"), ("COLUBRIS-USER-ACCOUNT-MIB", "coUserAccExpirationTime"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    colubrisUserAccountStatusMIBGroup = colubrisUserAccountStatusMIBGroup.setStatus('current')
if mibBuilder.loadTexts: colubrisUserAccountStatusMIBGroup.setDescription('A collection of objects for User Account status.')
mibBuilder.exportSymbols("COLUBRIS-USER-ACCOUNT-MIB", colubrisUserAccountMIBCompliance=colubrisUserAccountMIBCompliance, coUserAccountStatusGroup=coUserAccountStatusGroup, colubrisUserAccountMIBConformance=colubrisUserAccountMIBConformance, coUserAccountStatusTable=coUserAccountStatusTable, colubrisUserAccountMIBObjects=colubrisUserAccountMIBObjects, colubrisUserAccountMIBNotifications=colubrisUserAccountMIBNotifications, coUserAccRemainingSessionTime=coUserAccRemainingSessionTime, coUserAccExpirationTime=coUserAccExpirationTime, coUserAccUserName=coUserAccUserName, colubrisUserAccountStatusMIBGroup=colubrisUserAccountStatusMIBGroup, coUserAccRemainingOnlineTime=coUserAccRemainingOnlineTime, colubrisUserAccountMIB=colubrisUserAccountMIB, coUserAccStatus=coUserAccStatus, coUserAccPlanName=coUserAccPlanName, PYSNMP_MODULE_ID=colubrisUserAccountMIB, coUserAccIndex=coUserAccIndex, colubrisUserAccountMIBCompliances=colubrisUserAccountMIBCompliances, coUserAccountStatusEntry=coUserAccountStatusEntry, coUserAccFirstLoginTime=coUserAccFirstLoginTime, colubrisUserAccountMIBGroups=colubrisUserAccountMIBGroups, colubrisUserAccountMIBNotificationPrefix=colubrisUserAccountMIBNotificationPrefix)
