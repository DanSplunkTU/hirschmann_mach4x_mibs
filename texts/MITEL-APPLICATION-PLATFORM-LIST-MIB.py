#
# PySNMP MIB module MITEL-APPLICATION-PLATFORM-LIST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/mitel/MITEL-APPLICATION-PLATFORM-LIST-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:16:02 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mitelIdentification, = mibBuilder.importSymbols("MITEL-MIB", "mitelIdentification")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
TimeTicks, MibIdentifier, ModuleIdentity, Counter32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Integer32, Unsigned32, IpAddress, ObjectIdentity, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ModuleIdentity", "Counter32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Integer32", "Unsigned32", "IpAddress", "ObjectIdentity", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mitelIdApplicationPlatforms = ModuleIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6))
mitelIdApplicationPlatforms.setRevisions(('2014-02-11 12:00', '2006-08-10 00:00', '2005-08-24 21:34',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mitelIdApplicationPlatforms.setRevisionsDescriptions(('The MITEL Application Patform List MIB module.\n                           Platforms that provide a base for Mitel applications.\n                           These typically will be used for the sysObjectID\n                           Field.', 'Adding additional compute platforms to the list of \n                           Application Servers.', 'Created.',))
if mibBuilder.loadTexts: mitelIdApplicationPlatforms.setLastUpdated('201402111200Z')
if mibBuilder.loadTexts: mitelIdApplicationPlatforms.setOrganization('MITEL Networks Corporation')
if mibBuilder.loadTexts: mitelIdApplicationPlatforms.setContactInfo('Standards Group,\n                           Postal:    MITEL Networks Corporation\n                           350 Legget Drive, PO Box 13089\n                           Kanata, Ontario\n                           Canada  K2K 2W7\n                           Tel: +1 613 592 2122\n                           Fax: +1 613 592 4784\n                           URL: www.mitel.com')
if mibBuilder.loadTexts: mitelIdApplicationPlatforms.setDescription('Replaced E-Mail: std@mitel.com with URL: www.mitel.com.')
mitelIdAppPlatManagementApplicationServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 1))
if mibBuilder.loadTexts: mitelIdAppPlatManagementApplicationServer.setStatus('current')
if mibBuilder.loadTexts: mitelIdAppPlatManagementApplicationServer.setDescription('The Mitel Networks MAS application server platform.')
mitelIdAppPlatLXTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 2))
if mibBuilder.loadTexts: mitelIdAppPlatLXTelephonyServer.setStatus('current')
if mibBuilder.loadTexts: mitelIdAppPlatLXTelephonyServer.setDescription('The Mitel Networks LX Telephony server platform.')
mitelIdAppPlatMXTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 3))
if mibBuilder.loadTexts: mitelIdAppPlatMXTelephonyServer.setStatus('current')
if mibBuilder.loadTexts: mitelIdAppPlatMXTelephonyServer.setDescription('The Mitel Networks MX Telephony server platform.')
mitelIdAppPlatCXTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 4))
if mibBuilder.loadTexts: mitelIdAppPlatCXTelephonyServer.setStatus('current')
if mibBuilder.loadTexts: mitelIdAppPlatCXTelephonyServer.setDescription('The Mitel Networks CX Telephony server platform.')
mitelIdAppPlatCXiTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 5))
if mibBuilder.loadTexts: mitelIdAppPlatCXiTelephonyServer.setStatus('current')
if mibBuilder.loadTexts: mitelIdAppPlatCXiTelephonyServer.setDescription('The Mitel Networks CXi Telephony server platform.')
mitelIdAppPlatLiteTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 6))
if mibBuilder.loadTexts: mitelIdAppPlatLiteTelephonyServer.setStatus('current')
if mibBuilder.loadTexts: mitelIdAppPlatLiteTelephonyServer.setDescription('The Mitel Networks Lite Telephony server platform.')
mitelIdAppPlatMXeTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 7))
if mibBuilder.loadTexts: mitelIdAppPlatMXeTelephonyServer.setStatus('current')
if mibBuilder.loadTexts: mitelIdAppPlatMXeTelephonyServer.setDescription('The Mitel Networks MXe Telephony server platform.')
mitelIdAppPlatAXTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 8))
if mibBuilder.loadTexts: mitelIdAppPlatAXTelephonyServer.setStatus('current')
if mibBuilder.loadTexts: mitelIdAppPlatAXTelephonyServer.setDescription('The Mitel Networks AX Telephony server platform.')
mitelIdAppPlatMXTTelephonyServer = ObjectIdentity((1, 3, 6, 1, 4, 1, 1027, 1, 6, 9))
if mibBuilder.loadTexts: mitelIdAppPlatMXTTelephonyServer.setStatus('current')
if mibBuilder.loadTexts: mitelIdAppPlatMXTTelephonyServer.setDescription('The Mitel Networks MXT Telephony server platform.')
mibBuilder.exportSymbols("MITEL-APPLICATION-PLATFORM-LIST-MIB", mitelIdApplicationPlatforms=mitelIdApplicationPlatforms, mitelIdAppPlatManagementApplicationServer=mitelIdAppPlatManagementApplicationServer, mitelIdAppPlatAXTelephonyServer=mitelIdAppPlatAXTelephonyServer, mitelIdAppPlatMXTTelephonyServer=mitelIdAppPlatMXTTelephonyServer, mitelIdAppPlatCXTelephonyServer=mitelIdAppPlatCXTelephonyServer, mitelIdAppPlatMXTelephonyServer=mitelIdAppPlatMXTelephonyServer, PYSNMP_MODULE_ID=mitelIdApplicationPlatforms, mitelIdAppPlatCXiTelephonyServer=mitelIdAppPlatCXiTelephonyServer, mitelIdAppPlatLXTelephonyServer=mitelIdAppPlatLXTelephonyServer, mitelIdAppPlatLiteTelephonyServer=mitelIdAppPlatLiteTelephonyServer, mitelIdAppPlatMXeTelephonyServer=mitelIdAppPlatMXeTelephonyServer)
