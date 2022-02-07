#
# PySNMP MIB module ATKK-WLAN-ACCESS (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/allied/ATKK-WLAN-ACCESS-MIB
# Produced by pysmi-1.1.8 at Mon Feb  7 16:07:18 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
wirelesslan, wirelessLanmMIB = mibBuilder.importSymbols("AT-SMI-MIB", "wirelesslan", "wirelessLanmMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, Counter64, Gauge32, MibIdentifier, ModuleIdentity, Unsigned32, IpAddress, ObjectIdentity, NotificationType, enterprises, TimeTicks, Bits, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Gauge32", "MibIdentifier", "ModuleIdentity", "Unsigned32", "IpAddress", "ObjectIdentity", "NotificationType", "enterprises", "TimeTicks", "Bits", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
atkkWlanAccess = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 6))
atkkWlanAccess.setRevisions(('2016-05-25 00:00', '2016-03-23 00:00', '2015-06-17 00:00', '2015-05-11 00:00', '2014-09-30 00:00', '2013-11-22 00:00', '2012-08-13 00:00', '2012-07-09 00:00', '2012-06-06 00:00', '2012-01-11 00:00', '2011-04-08 00:00', '2010-08-20 00:00', '2009-07-28 00:00',))
if mibBuilder.loadTexts: atkkWlanAccess.setLastUpdated('201605250000Z')
if mibBuilder.loadTexts: atkkWlanAccess.setOrganization('Allied Telesis K.K.')
tq2403 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 13))
tq2450 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 19))
tq2403ex = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 20))
tq3600 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 22))
tq3200 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 24))
tq3400 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 25))
tq4400 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 26))
tq4600 = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 27))
tq4400e = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 1, 13, 34))
class SsidString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class UserIdString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class TrapHostString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 256)

class CommunityString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 256)

class TrapString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 256)

class ChannelString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

atkkWiAcVersion = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcVersion.setStatus('current')
atkkWiAcApInfo = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6))
if mibBuilder.loadTexts: atkkWiAcApInfo.setStatus('current')
atkkWiAcApInfoTrapTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1), )
if mibBuilder.loadTexts: atkkWiAcApInfoTrapTable.setStatus('current')
atkkWiAcApInfoTrapEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1), ).setIndexNames((0, "ATKK-WLAN-ACCESS", "atkkWiAcApTrapHost"))
if mibBuilder.loadTexts: atkkWiAcApInfoTrapEntry.setStatus('current')
atkkWiAcApTrapHost = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 1), TrapHostString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapHost.setStatus('current')
atkkWiAcApTrapCommunity = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 2), CommunityString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapCommunity.setStatus('current')
atkkWiAcApTrapColdStartConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapColdStartConfig.setStatus('current')
atkkWiAcApTrapLinkConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapLinkConfig.setStatus('current')
atkkWiAcApTrapAuthenticationConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapAuthenticationConfig.setStatus('current')
atkkWiAcApTrapAssociationConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapAssociationConfig.setStatus('current')
atkkWiAcApTrapUnknownApConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapUnknownApConfig.setStatus('current')
atkkWiAcApTrapFilteredStaConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapFilteredStaConfig.setStatus('current')
atkkWiAcApTrapRadiusAuthSuccessConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapRadiusAuthSuccessConfig.setStatus('current')
atkkWiAcApTrapRadiusAuthFailConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapRadiusAuthFailConfig.setStatus('current')
atkkWiAcApTrapDfsDetectedConfig = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 6, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcApTrapDfsDetectedConfig.setStatus('current')
atkkWiAcClients = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2))
if mibBuilder.loadTexts: atkkWiAcClients.setStatus('current')
atkkWiAcClientTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1), )
if mibBuilder.loadTexts: atkkWiAcClientTable.setStatus('current')
atkkWiAcClientEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1), ).setIndexNames((0, "ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"))
if mibBuilder.loadTexts: atkkWiAcClientEntry.setStatus('current')
atkkWiAcClientAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClientAddress.setStatus('current')
atkkWiAcClientSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 2), SsidString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClientSSID.setStatus('current')
atkkWiAcClient80211Spec = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("dot11b", 2), ("dot11g", 3), ("dot11a", 4), ("dot11ng", 5), ("dot11na", 6), ("dot11ac", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClient80211Spec.setStatus('current')
atkkWiAcClientChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClientChannel.setStatus('current')
atkkWiAcClientAge = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClientAge.setStatus('current')
atkkWiAcClientUserID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 2, 1, 1, 6), UserIdString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcClientUserID.setStatus('current')
atkkWiAcAPs = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3))
if mibBuilder.loadTexts: atkkWiAcAPs.setStatus('current')
atkkWiAcAPTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1), )
if mibBuilder.loadTexts: atkkWiAcAPTable.setStatus('current')
atkkWiAcAPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1), ).setIndexNames((0, "ATKK-WLAN-ACCESS", "atkkWiAcAPAddress"))
if mibBuilder.loadTexts: atkkWiAcAPEntry.setStatus('current')
atkkWiAcAPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPAddress.setStatus('current')
atkkWiAcAPSSID = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 2), SsidString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPSSID.setStatus('current')
atkkWiAcAP80211Spec = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 1), ("dot11b", 2), ("dot11g", 3), ("dot11a", 4), ("dot11ng", 5), ("dot11na", 6), ("dot11ac", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAP80211Spec.setStatus('current')
atkkWiAcAPChannel = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPChannel.setStatus('current')
atkkWiAcAPRSSI = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPRSSI.setStatus('current')
atkkWiAcAPRadarDetected = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 6), TrapString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPRadarDetected.setStatus('current')
atkkWiAcAPChannels = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 1, 1, 7), ChannelString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcAPChannels.setStatus('current')
atkkWiAcAPDetectConfig = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atkkWiAcAPDetectConfig.setStatus('current')
atkkWiAcAPDetectConfig2 = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 3, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atkkWiAcAPDetectConfig2.setStatus('current')
atkkWiAcMacACL = ObjectIdentity((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4))
if mibBuilder.loadTexts: atkkWiAcMacACL.setStatus('current')
atkkWiAcMacACLTable = MibTable((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 1), )
if mibBuilder.loadTexts: atkkWiAcMacACLTable.setStatus('current')
atkkWiAcMacACLEntry = MibTableRow((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 1, 1), ).setIndexNames((0, "ATKK-WLAN-ACCESS", "atkkWiAcMacACLAddress"))
if mibBuilder.loadTexts: atkkWiAcMacACLEntry.setStatus('current')
atkkWiAcMacACLAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 1, 1, 1), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: atkkWiAcMacACLAddress.setStatus('current')
atkkWiAcMacACLModeConfig = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 4, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("accept", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: atkkWiAcMacACLModeConfig.setStatus('current')
atkkWiAcNotification = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5))
atkkWiAcNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0))
atkkWiAcAssociated = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 1)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcClient80211Spec"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientChannel"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientAge"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
if mibBuilder.loadTexts: atkkWiAcAssociated.setStatus('current')
atkkWiAcDisassociated = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 2)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcClient80211Spec"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientChannel"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientAge"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
if mibBuilder.loadTexts: atkkWiAcDisassociated.setStatus('current')
atkkWiAcUnknownAP = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 3)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcAPAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcAPSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcAP80211Spec"), ("ATKK-WLAN-ACCESS", "atkkWiAcAPChannel"), ("ATKK-WLAN-ACCESS", "atkkWiAcAPRSSI"))
if mibBuilder.loadTexts: atkkWiAcUnknownAP.setStatus('current')
atkkWiAcFiltered = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 4)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcClient80211Spec"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientChannel"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientAge"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
if mibBuilder.loadTexts: atkkWiAcFiltered.setStatus('current')
atkkWiAcRadiusAuthSucceeded = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 5)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
if mibBuilder.loadTexts: atkkWiAcRadiusAuthSucceeded.setStatus('current')
atkkWiAcRadiusAuthFailed = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 6)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcClientAddress"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientSSID"), ("ATKK-WLAN-ACCESS", "atkkWiAcClientUserID"))
if mibBuilder.loadTexts: atkkWiAcRadiusAuthFailed.setStatus('current')
atkkWiAcRadarDetected = NotificationType((1, 3, 6, 1, 4, 1, 207, 8, 42, 6, 5, 0, 7)).setObjects(("ATKK-WLAN-ACCESS", "atkkWiAcAPRadarDetected"), ("ATKK-WLAN-ACCESS", "atkkWiAcAPChannels"))
if mibBuilder.loadTexts: atkkWiAcRadarDetected.setStatus('current')
mibBuilder.exportSymbols("ATKK-WLAN-ACCESS", tq3400=tq3400, ChannelString=ChannelString, tq4400=tq4400, atkkWiAcApInfoTrapEntry=atkkWiAcApInfoTrapEntry, atkkWiAcApTrapCommunity=atkkWiAcApTrapCommunity, atkkWiAcMacACLAddress=atkkWiAcMacACLAddress, SsidString=SsidString, tq2450=tq2450, atkkWiAcClientChannel=atkkWiAcClientChannel, atkkWiAcClientSSID=atkkWiAcClientSSID, atkkWiAcClientEntry=atkkWiAcClientEntry, atkkWiAcFiltered=atkkWiAcFiltered, atkkWiAcAPEntry=atkkWiAcAPEntry, atkkWiAcNotificationObjects=atkkWiAcNotificationObjects, atkkWiAcAPAddress=atkkWiAcAPAddress, atkkWiAcMacACLModeConfig=atkkWiAcMacACLModeConfig, atkkWiAcAPChannel=atkkWiAcAPChannel, atkkWiAcRadiusAuthFailed=atkkWiAcRadiusAuthFailed, atkkWiAcApTrapAssociationConfig=atkkWiAcApTrapAssociationConfig, atkkWiAcClient80211Spec=atkkWiAcClient80211Spec, atkkWiAcAPRSSI=atkkWiAcAPRSSI, atkkWiAcAPDetectConfig=atkkWiAcAPDetectConfig, tq2403ex=tq2403ex, atkkWiAcApTrapColdStartConfig=atkkWiAcApTrapColdStartConfig, atkkWiAcUnknownAP=atkkWiAcUnknownAP, atkkWiAcAPSSID=atkkWiAcAPSSID, atkkWiAcAPChannels=atkkWiAcAPChannels, atkkWiAcApTrapFilteredStaConfig=atkkWiAcApTrapFilteredStaConfig, tq2403=tq2403, PYSNMP_MODULE_ID=atkkWlanAccess, tq4400e=tq4400e, atkkWiAcApTrapRadiusAuthFailConfig=atkkWiAcApTrapRadiusAuthFailConfig, atkkWlanAccess=atkkWlanAccess, atkkWiAcApInfoTrapTable=atkkWiAcApInfoTrapTable, atkkWiAcClientUserID=atkkWiAcClientUserID, tq3200=tq3200, atkkWiAcVersion=atkkWiAcVersion, atkkWiAcAPTable=atkkWiAcAPTable, atkkWiAcApTrapAuthenticationConfig=atkkWiAcApTrapAuthenticationConfig, atkkWiAcClientAddress=atkkWiAcClientAddress, atkkWiAcMacACLTable=atkkWiAcMacACLTable, TrapHostString=TrapHostString, atkkWiAcApTrapHost=atkkWiAcApTrapHost, atkkWiAcApTrapRadiusAuthSuccessConfig=atkkWiAcApTrapRadiusAuthSuccessConfig, atkkWiAcClientAge=atkkWiAcClientAge, atkkWiAcNotification=atkkWiAcNotification, atkkWiAcAssociated=atkkWiAcAssociated, atkkWiAcAPRadarDetected=atkkWiAcAPRadarDetected, atkkWiAcApTrapDfsDetectedConfig=atkkWiAcApTrapDfsDetectedConfig, atkkWiAcRadiusAuthSucceeded=atkkWiAcRadiusAuthSucceeded, UserIdString=UserIdString, atkkWiAcClientTable=atkkWiAcClientTable, atkkWiAcAP80211Spec=atkkWiAcAP80211Spec, atkkWiAcDisassociated=atkkWiAcDisassociated, atkkWiAcAPs=atkkWiAcAPs, TrapString=TrapString, atkkWiAcMacACL=atkkWiAcMacACL, atkkWiAcApInfo=atkkWiAcApInfo, atkkWiAcMacACLEntry=atkkWiAcMacACLEntry, CommunityString=CommunityString, tq4600=tq4600, atkkWiAcApTrapUnknownApConfig=atkkWiAcApTrapUnknownApConfig, atkkWiAcRadarDetected=atkkWiAcRadarDetected, atkkWiAcAPDetectConfig2=atkkWiAcAPDetectConfig2, atkkWiAcClients=atkkWiAcClients, tq3600=tq3600, atkkWiAcApTrapLinkConfig=atkkWiAcApTrapLinkConfig)
