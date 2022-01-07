#
# PySNMP MIB module SIAE-FEATUREKEYS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-FEATUREKEYS-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:26:21 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Unsigned32, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, iso, Counter32, IpAddress, ModuleIdentity, Counter64, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "iso", "Counter32", "IpAddress", "ModuleIdentity", "Counter64", "MibIdentifier", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
featureKeys = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 101))
featureKeys.setRevisions(('2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: featureKeys.setRevisionsDescriptions(('Improved description of featureKeysMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: featureKeys.setLastUpdated('201402030000Z')
if mibBuilder.loadTexts: featureKeys.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: featureKeys.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: featureKeys.setDescription("Protection by key of the SIAE's equipment features.\n            ")
featureKeysMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 101, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: featureKeysMibVersion.setStatus('current')
if mibBuilder.loadTexts: featureKeysMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
featureKeysRadioMap = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 101, 2), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: featureKeysRadioMap.setStatus('current')
if mibBuilder.loadTexts: featureKeysRadioMap.setDescription('This object is the map of the radio feature keys (16 bits). The Get\n             operation returns a map of 2 bytes. The value of the Set operation\n             must be composed by the map of the 2 bytes and a 16 bytes signature\n             from MD5 (the first 8 bytes as primary and the last 8 bytes as\n             secondary).')
featureKeysLineMap = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 101, 3), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: featureKeysLineMap.setStatus('current')
if mibBuilder.loadTexts: featureKeysLineMap.setDescription('This object is the map of the line feature keys (16 bits). The Get\n             operation returns a map of 2 bytes. The value of the Set operation\n             must be composed by the map of the 2 bytes and a 16 bytes signature\n             from MD5 (the first 8 bytes as primary and the last 8 bytes as\n             secondary).')
featureKeysActionRequest = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 101, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("noAction", 1), ("upload", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: featureKeysActionRequest.setStatus('current')
if mibBuilder.loadTexts: featureKeysActionRequest.setDescription('This objects is used to perform the action modifying feature key.')
featureKeysCertificateName = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 101, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: featureKeysCertificateName.setStatus('current')
if mibBuilder.loadTexts: featureKeysCertificateName.setDescription('This objects is the path filename of the certificate used to set the\n             radio or line feature keys. The file is sent through FTP/SFTP.')
featureKeysCertificateRemoteIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 101, 6), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: featureKeysCertificateRemoteIpAddress.setStatus('current')
if mibBuilder.loadTexts: featureKeysCertificateRemoteIpAddress.setDescription('This objects is the IP address of the FTP/SFTP server from which\n             the certificate has to be downloaded to the equipment.')
featureKeysLastOperationState = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 101, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("initial", 1), ("downloadCompleted", 2), ("downloadTransferring", 3), ("downloadVerifying", 4), ("downloadInterrupted", 5), ("setSuccess", 6), ("setFailure", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: featureKeysLastOperationState.setStatus('current')
if mibBuilder.loadTexts: featureKeysLastOperationState.setDescription('This objects is the state of the last operation (a SNMP set on radio/line\n             map or a certificate transfer). The values mean:\n             initial -> default state after a start-up\n             downloadCompleted -> a certificate has been downloaded successfully\n             downloadTransferring -> a download is running\n             downloadVerifying -> the certificate has been checking\n             downloadInterrupted -> the download of a certificate had a bad result\n             setSuccess -> a success of a SMNP set on radio/line map\n             setFailure -> a failure of a SMNP set on radio/line map.')
featureKeysLastOperationFailure = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 101, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("noFailure", 1), ("transfer", 2), ("serialNo", 3), ("verifySign", 4), ("primaryDigest", 5), ("secondaryDigest", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: featureKeysLastOperationFailure.setStatus('current')
if mibBuilder.loadTexts: featureKeysLastOperationFailure.setDescription('This objects is the failure code of the last operation (a SNMP set on\n             radio/line map or a certificate transfer).')
mibBuilder.exportSymbols("SIAE-FEATUREKEYS-MIB", PYSNMP_MODULE_ID=featureKeys, featureKeysLineMap=featureKeysLineMap, featureKeysRadioMap=featureKeysRadioMap, featureKeysCertificateName=featureKeysCertificateName, featureKeysCertificateRemoteIpAddress=featureKeysCertificateRemoteIpAddress, featureKeysLastOperationState=featureKeysLastOperationState, featureKeys=featureKeys, featureKeysMibVersion=featureKeysMibVersion, featureKeysLastOperationFailure=featureKeysLastOperationFailure, featureKeysActionRequest=featureKeysActionRequest)
