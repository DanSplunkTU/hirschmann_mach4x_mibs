#
# PySNMP MIB module ADTRAN-AOS-DESKTOP-AUDITING (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOS-DESKTOP-AUDITING
# Produced by pysmi-1.1.8 at Fri Jan  7 15:51:59 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
adGenAOSSwitch, adGenAOSConformance = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSSwitch", "adGenAOSConformance")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
ModuleIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter32, Counter64, NotificationType, ObjectIdentity, Unsigned32, IpAddress, Bits, Integer32, MibIdentifier, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter32", "Counter64", "NotificationType", "ObjectIdentity", "Unsigned32", "IpAddress", "Bits", "Integer32", "MibIdentifier", "TimeTicks")
TextualConvention, TruthValue, TimeStamp, DisplayString, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "TimeStamp", "DisplayString", "DateAndTime")
adGenAOSDesktopAuditingMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 4, 1))
if mibBuilder.loadTexts: adGenAOSDesktopAuditingMib.setLastUpdated('200912140000Z')
if mibBuilder.loadTexts: adGenAOSDesktopAuditingMib.setOrganization('ADTRAN, Inc.')
adGenDesktopAuditing = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2))
adGenNapClients = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0))
adGenNapClientsTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1), )
if mibBuilder.loadTexts: adGenNapClientsTable.setStatus('current')
adGenNapClientsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1), ).setIndexNames((0, "ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientMac"), (0, "ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientVlanId"))
if mibBuilder.loadTexts: adGenNapClientsEntry.setStatus('current')
adNapClientMac = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientMac.setStatus('current')
adNapClientVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientVlanId.setStatus('current')
adNapClientIp = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientIp.setStatus('current')
adNapClientHostname = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 4), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientHostname.setStatus('current')
adNapClientSrcPortIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientSrcPortIfId.setStatus('current')
adNapClientSrcPortIfType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientSrcPortIfType.setStatus('current')
adNapServerMac = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 7), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapServerMac.setStatus('current')
adNapServerIp = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapServerIp.setStatus('current')
adNapCollectionMethod = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 9), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapCollectionMethod.setStatus('current')
adNapCollectionTime = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 10), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapCollectionTime.setStatus('current')
adNapCapableClient = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 11), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapCapableClient.setStatus('current')
adNapCapableServer = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapCapableServer.setStatus('current')
adNapClientOsVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 13), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientOsVersion.setStatus('current')
adNapClientOsServicePk = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 14), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientOsServicePk.setStatus('current')
adNapClientOsProcessorArc = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 15), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientOsProcessorArc.setStatus('current')
adNapClientLastSecurityUpdate = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 16), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientLastSecurityUpdate.setStatus('current')
adNapClientSecurityUpdateServer = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 17), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientSecurityUpdateServer.setStatus('current')
adNapClientRequiresRemediation = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("unknown", 1), ("true", 2), ("false", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientRequiresRemediation.setStatus('current')
adNapClientLocalPolicyViolator = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 19), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientLocalPolicyViolator.setStatus('current')
adNapClientFirewallState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 20), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("unknown", 1), ("notInstalled", 2), ("wscServiceDown", 3), ("wscNotStarted", 4), ("notEnaNotUTD", 5), ("micsftNotEnaNotUTD", 6), ("notEnaUTD", 7), ("micsftNotEnaUTD", 8), ("enaNotUTDSn", 9), ("micsftEnaNotUTDSn", 10), ("enaNotUTDNotSn", 11), ("micsftEnaNotUTDNotSn", 12), ("enaUTDSn", 13), ("micsftEnaUTDSn", 14), ("enaUTDNotSn", 15), ("micsftEnaUTDNotSn", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientFirewallState.setStatus('current')
adNapClientFirewall = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 21), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientFirewall.setStatus('current')
adNapClientAntivirusState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 22), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("unknown", 1), ("notInstalled", 2), ("wscServiceDown", 3), ("wscNotStarted", 4), ("notEnaNotUTD", 5), ("micsftNotEnaNotUTD", 6), ("notEnaUTD", 7), ("micsftNotEnaUTD", 8), ("enaNotUTDSn", 9), ("micsftEnaNotUTDSn", 10), ("enaNotUTDNotSn", 11), ("micsftEnaNotUTDNotSn", 12), ("enaUTDSn", 13), ("micsftEnaUTDSn", 14), ("enaUTDNotSn", 15), ("micsftEnaUTDNotSn", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientAntivirusState.setStatus('current')
adNapClientAntivirus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 23), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientAntivirus.setStatus('current')
adNapClientAntispywareState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 24), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))).clone(namedValues=NamedValues(("unknown", 1), ("notInstalled", 2), ("wscServiceDown", 3), ("wscNotStarted", 4), ("notEnaNotUTD", 5), ("micsftNotEnaNotUTD", 6), ("notEnaUTD", 7), ("micsftNotEnaUTD", 8), ("enaNotUTDSn", 9), ("micsftEnaNotUTDSn", 10), ("enaNotUTDNotSn", 11), ("micsftEnaNotUTDNotSn", 12), ("enaUTDSn", 13), ("micsftEnaUTDSn", 14), ("enaUTDNotSn", 15), ("micsftEnaUTDNotSn", 16)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientAntispywareState.setStatus('current')
adNapClientAntispyware = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 25), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientAntispyware.setStatus('current')
adNapClientAutoupdateState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 26), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unknown", 1), ("notInstalled", 2), ("wscServiceDown", 3), ("wscNotStarted", 4), ("notEna", 5), ("enaCkUpdateOnly", 6), ("enaDownload", 7), ("enaDownloadInstall", 8), ("neverConfigured", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientAutoupdateState.setStatus('current')
adNapClientSecurityupdateState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 27), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("unknown", 1), ("noMissingUpdate", 2), ("missingUpdate", 3), ("noWUS", 4), ("noClientID", 5), ("wuaServiceDisabled", 6), ("wuaCommFailed", 7), ("updateInsNeedReboot", 8), ("wuaNotStarted", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientSecurityupdateState.setStatus('current')
adNapClientSecuritySeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 28), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("unknown", 1), ("unspecified", 2), ("low", 3), ("moderate", 4), ("important", 5), ("critical", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientSecuritySeverity.setStatus('current')
adNapClientConnectionState = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 4, 2, 0, 1, 1, 29), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("unknown", 1), ("notRestricted", 2), ("notResMaybeLater", 3), ("restricted", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adNapClientConnectionState.setStatus('current')
adGenAOSDesktopAuditingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10))
adGenAOSDesktopAuditingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1))
adGenAOSDesktopAuditingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 2))
adGenAOSDesktopAuditingFullCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 2, 1)).setObjects(("ADTRAN-AOS-DESKTOP-AUDITING", "adGenNapClientsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenAOSDesktopAuditingFullCompliance = adGenAOSDesktopAuditingFullCompliance.setStatus('current')
adGenNapClientsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 10, 1, 1)).setObjects(("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientMac"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientVlanId"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientIp"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientHostname"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSrcPortIfId"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSrcPortIfType"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapServerMac"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapServerIp"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCollectionMethod"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCollectionTime"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCapableClient"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapCapableServer"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientOsVersion"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientOsServicePk"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientOsProcessorArc"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientLastSecurityUpdate"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSecurityUpdateServer"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientRequiresRemediation"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientLocalPolicyViolator"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientFirewallState"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientFirewall"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntivirusState"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntivirus"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntispywareState"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAntispyware"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientAutoupdateState"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSecurityupdateState"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientSecuritySeverity"), ("ADTRAN-AOS-DESKTOP-AUDITING", "adNapClientConnectionState"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adGenNapClientsGroup = adGenNapClientsGroup.setStatus('current')
mibBuilder.exportSymbols("ADTRAN-AOS-DESKTOP-AUDITING", adNapServerIp=adNapServerIp, adGenAOSDesktopAuditingConformance=adGenAOSDesktopAuditingConformance, adGenDesktopAuditing=adGenDesktopAuditing, adNapClientOsProcessorArc=adNapClientOsProcessorArc, adNapClientAutoupdateState=adNapClientAutoupdateState, adNapCollectionMethod=adNapCollectionMethod, adNapClientAntispyware=adNapClientAntispyware, adGenNapClientsGroup=adGenNapClientsGroup, adNapClientAntivirus=adNapClientAntivirus, adNapClientLocalPolicyViolator=adNapClientLocalPolicyViolator, adGenAOSDesktopAuditingGroups=adGenAOSDesktopAuditingGroups, adNapClientSrcPortIfType=adNapClientSrcPortIfType, adGenAOSDesktopAuditingFullCompliance=adGenAOSDesktopAuditingFullCompliance, adNapClientSecuritySeverity=adNapClientSecuritySeverity, adNapCollectionTime=adNapCollectionTime, adGenNapClientsEntry=adGenNapClientsEntry, adNapClientAntispywareState=adNapClientAntispywareState, adNapClientSecurityupdateState=adNapClientSecurityupdateState, adNapCapableClient=adNapCapableClient, adGenNapClients=adGenNapClients, PYSNMP_MODULE_ID=adGenAOSDesktopAuditingMib, adNapClientOsVersion=adNapClientOsVersion, adNapServerMac=adNapServerMac, adNapClientSecurityUpdateServer=adNapClientSecurityUpdateServer, adNapClientHostname=adNapClientHostname, adGenAOSDesktopAuditingMib=adGenAOSDesktopAuditingMib, adNapClientIp=adNapClientIp, adGenAOSDesktopAuditingCompliances=adGenAOSDesktopAuditingCompliances, adNapClientOsServicePk=adNapClientOsServicePk, adNapClientLastSecurityUpdate=adNapClientLastSecurityUpdate, adNapClientRequiresRemediation=adNapClientRequiresRemediation, adNapClientFirewallState=adNapClientFirewallState, adNapClientFirewall=adNapClientFirewall, adNapClientVlanId=adNapClientVlanId, adNapClientConnectionState=adNapClientConnectionState, adNapClientSrcPortIfId=adNapClientSrcPortIfId, adGenNapClientsTable=adGenNapClientsTable, adNapCapableServer=adNapCapableServer, adNapClientAntivirusState=adNapClientAntivirusState, adNapClientMac=adNapClientMac)
