#
# PySNMP MIB module MITEL-APPLIST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mitel/MITEL-APPLIST-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:12:49 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
mitelIdentification, = mibBuilder.importSymbols("MITEL-MIB", "mitelIdentification")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, Integer32, iso, Gauge32, Unsigned32, Bits, Counter32, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, IpAddress, TimeTicks, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "iso", "Gauge32", "Unsigned32", "Bits", "Counter32", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "IpAddress", "TimeTicks", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitelIdApplications = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7))
mitelIdApplications.setRevisions(('2014-02-11 12:00', '2008-11-25 00:00', '2008-10-02 00:00', '2008-08-13 00:00', '2007-06-07 00:00', '2007-04-09 00:00', '2007-02-12 00:00', '2006-08-10 00:00', '2005-02-23 21:34',))
if mibBuilder.loadTexts: mitelIdApplications.setLastUpdated('201402111200Z')
if mibBuilder.loadTexts: mitelIdApplications.setOrganization('MITEL Networks Corporation')
mitelIdAppMasTeleworker = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 1))
if mibBuilder.loadTexts: mitelIdAppMasTeleworker.setStatus('current')
mitelIdAppMasOfficeServerSuite = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 2))
if mibBuilder.loadTexts: mitelIdAppMasOfficeServerSuite.setStatus('current')
mitelIdAppMasManagedVpn = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 3))
if mibBuilder.loadTexts: mitelIdAppMasManagedVpn.setStatus('current')
mitelIdAppMasMobileExtention = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 4))
if mibBuilder.loadTexts: mitelIdAppMasMobileExtention.setStatus('current')
mitelIdAppCallServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 5))
if mibBuilder.loadTexts: mitelIdAppCallServer.setStatus('current')
mitelIdAppQuickConference = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 6))
if mibBuilder.loadTexts: mitelIdAppQuickConference.setStatus('current')
mitelIdAppSecureCallRecConn = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 7))
if mibBuilder.loadTexts: mitelIdAppSecureCallRecConn.setStatus('current')
mitelIdAppSuiteAppService = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 8))
if mibBuilder.loadTexts: mitelIdAppSuiteAppService.setStatus('current')
mitelIdAppAudioWebConferencing = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 9))
if mibBuilder.loadTexts: mitelIdAppAudioWebConferencing.setStatus('current')
mitelIdAppCustomerServiceManager = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 10))
if mibBuilder.loadTexts: mitelIdAppCustomerServiceManager.setStatus('current')
mitelIdAppNupointUnifiedMessenger = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 11))
if mibBuilder.loadTexts: mitelIdAppNupointUnifiedMessenger.setStatus('current')
mitelIdAppUnifiedCommunicationsServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 12))
if mibBuilder.loadTexts: mitelIdAppUnifiedCommunicationsServer.setStatus('current')
mitelIdAppUnifiedIPClient = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 13))
if mibBuilder.loadTexts: mitelIdAppUnifiedIPClient.setStatus('current')
mitelIdAppMediaServiceManager = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 14))
if mibBuilder.loadTexts: mitelIdAppMediaServiceManager.setStatus('current')
mitelIdAppMitelCommunicationDirectorManager = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 7, 15))
if mibBuilder.loadTexts: mitelIdAppMitelCommunicationDirectorManager.setStatus('current')
mibBuilder.exportSymbols("MITEL-APPLIST-MIB", PYSNMP_MODULE_ID=mitelIdApplications, mitelIdAppMediaServiceManager=mitelIdAppMediaServiceManager, mitelIdAppMasMobileExtention=mitelIdAppMasMobileExtention, mitelIdAppCustomerServiceManager=mitelIdAppCustomerServiceManager, mitelIdAppMasManagedVpn=mitelIdAppMasManagedVpn, mitelIdAppNupointUnifiedMessenger=mitelIdAppNupointUnifiedMessenger, mitelIdAppQuickConference=mitelIdAppQuickConference, mitelIdAppCallServer=mitelIdAppCallServer, mitelIdAppSuiteAppService=mitelIdAppSuiteAppService, mitelIdAppAudioWebConferencing=mitelIdAppAudioWebConferencing, mitelIdAppSecureCallRecConn=mitelIdAppSecureCallRecConn, mitelIdAppMasTeleworker=mitelIdAppMasTeleworker, mitelIdApplications=mitelIdApplications, mitelIdAppMasOfficeServerSuite=mitelIdAppMasOfficeServerSuite, mitelIdAppUnifiedCommunicationsServer=mitelIdAppUnifiedCommunicationsServer, mitelIdAppMitelCommunicationDirectorManager=mitelIdAppMitelCommunicationDirectorManager, mitelIdAppUnifiedIPClient=mitelIdAppUnifiedIPClient)
