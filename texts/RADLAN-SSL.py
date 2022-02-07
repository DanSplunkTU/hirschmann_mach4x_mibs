#
# PySNMP MIB module RADLAN-SSL (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/radlan/RADLAN-SSL
# Produced by pysmi-1.1.8 at Mon Feb  7 16:18:42 2022
# On host fv-az42-619 platform Linux version 5.11.0-1028-azure by user runner
# Using Python version 3.10.2 (main, Jan 16 2022, 11:55:27) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
TruthValue, RowStatus = mibBuilder.importSymbols("RADLAN-SNMPv2", "TruthValue", "RowStatus")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, Integer32, Bits, Counter64, TimeTicks, Gauge32, MibIdentifier, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "Integer32", "Bits", "Counter64", "TimeTicks", "Gauge32", "MibIdentifier", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "Unsigned32", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
DisplayString, = mibBuilder.importSymbols("SNMPv2-TC-v1", "DisplayString")
rlSsl = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 100))
rlSsl.setRevisions(('2003-09-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlSsl.setRevisionsDescriptions(('Added this MODULE-IDENTITY clause.',))
if mibBuilder.loadTexts: rlSsl.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlSsl.setOrganization('Radlan Computer Communications Ltd.')
if mibBuilder.loadTexts: rlSsl.setContactInfo('radlan.com')
if mibBuilder.loadTexts: rlSsl.setDescription('The private MIB module definition for SSL.')
rlSslCertificateGenerationTable = MibTable((1, 3, 6, 1, 4, 1, 89, 100, 1), )
if mibBuilder.loadTexts: rlSslCertificateGenerationTable.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationTable.setDescription('This table is used for :\n    1. generating keys and self signed certificate - saved in flash and RAM\n    (not in configuration file)\n    2. generating certificate requests - saved in RAM, can be read by\n    rlSslCertificateExportTable\n    3. generating self signed certificate - saved in flash and RAM (not in\n    configuraion file)\n    By setting rlSslCertificateGenerationAction to the appropriate\n    value this action takes place. The other fields of this table are used for\n    each of this actions')
rlSslCertificateGenerationEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 100, 1, 1), ).setIndexNames((0, "RADLAN-SSL", "rlSslCertificateGenerationIndex"))
if mibBuilder.loadTexts: rlSslCertificateGenerationEntry.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationEntry.setDescription(' The row definition for this table.')
rlSslCertificateGenerationIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationIndex.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationIndex.setDescription('This index is always set to 1 no matter for which certificate or\n    certificate request the action refers to.')
rlSslCertificateGenerationId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationId.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationId.setDescription('The device can hold a number of keys/certificates/certificate requests.\n    These certificates are always numbered from 1 to N (maximum number of\n    certificates in device). This field decides to which\n    keys/certificates/certificate requests the action refers.')
rlSslCertificateGenerationCountryName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationCountryName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationCountryName.setDescription('Value of country name field that will appear when a new certificate\n        request or self signed certificate is generated.')
rlSslCertificateGenerationStateOrProvinceName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationStateOrProvinceName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationStateOrProvinceName.setDescription('Value of state or province name field that will appear when a new\n        certificate or self signed certificate is generated.')
rlSslCertificateGenerationLocalityName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationLocalityName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationLocalityName.setDescription('Value of locality field that will appear when a new certificate or\n        self signed certificate is generated.')
rlSslCertificateGenerationOrganizationName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationName.setDescription('Value of organization field that will appear when a new certificate or\n        self signed certificate is generated.')
rlSslCertificateGenerationOrganizationUnitName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationUnitName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationOrganizationUnitName.setDescription('Value of organization field that will appear when a new certificate or\n        self signed certificate is generated.')
rlSslCertificateGenerationCommonName = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 8), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationCommonName.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationCommonName.setDescription('Value of common name field that will appear when a new certificate or\n        self signed certificate is generated.')
rlSslCertificateGenerationValidDays = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationValidDays.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationValidDays.setDescription("When generating self signed certificate this field sets the valid fields.\n        'Valid from' is current GMT and 'valid to' current GMT + the value of\n        this field.")
rlSslCertificateGenerationRsaKeyLength = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 10), Integer32().subtype(subtypeSpec=ValueRangeConstraint(512, 2048))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationRsaKeyLength.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationRsaKeyLength.setDescription('Setting the RSA key size that will be created when a new key is generated -\n         generateRsaKeyAndSelfSignedCertificate')
rlSslCertificateGenerationPassphrase = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 11), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationPassphrase.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationPassphrase.setDescription('When a RSA key is generated (generateRsaKeyAndSelfSignedCertificate)\n        this passphrase is saved in flash and when the time comes and the\n        certificate and the key are exported in PKCS12 format this passphrase\n        is used to encrypt it. If the passphrase is empty the key and\n        certificate can not be exported. There is no method of obtaining this\n        passphrase once a key was generated.')
rlSslCertificateGenerationAction = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 1, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("generateRsaKeyAndSelfSignedCertificate", 1), ("generateSelfSignedCertificate", 2), ("generatePkcs12", 3), ("generateCertificateRequest", 4)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateGenerationAction.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateGenerationAction.setDescription('Setting to a regenerateCertificate causes a new certificate to be\n        generated and to be used for all new sessions.')
rlSslCertificateExportTable = MibTable((1, 3, 6, 1, 4, 1, 89, 100, 2), )
if mibBuilder.loadTexts: rlSslCertificateExportTable.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportTable.setDescription('This table is used for viewing saved data from RAM and flash.')
rlSslCertificateExportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 100, 2, 1), ).setIndexNames((0, "RADLAN-SSL", "rlSslCertificateExportId"), (0, "RADLAN-SSL", "rlSslCertificateExportType"), (0, "RADLAN-SSL", "rlSslCertificateExportFragmentId"))
if mibBuilder.loadTexts: rlSslCertificateExportEntry.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportEntry.setDescription(' The row definition for this table.')
rlSslCertificateExportId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportId.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportId.setDescription('Identifies the index of this certficate / certificate request the table holds.')
rlSslCertificateExportType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("certificateRequestPemFormat", 1), ("certificatePemFormat", 2), ("certificateOpenSslFormat", 3), ("certificateAndKeyPkcs12", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportType.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportType.setDescription('Identifies the type of data the current entry shows.')
rlSslCertificateExportFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportFragmentId.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportFragmentId.setDescription('Identifies the index of this fragment in the certificate request.')
rlSslCertificateExportFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 2, 1, 4), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlSslCertificateExportFragmentText.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateExportFragmentText.setDescription('A part of the readable text entry for the certificate request.')
rlSslCertificateSave = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateSave.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateSave.setDescription('Saves data from rlSslCertificateImportTable to RAM and flash. When\n        an external certificate should be copied to the device first we copy\n        it to rlSslCertificateImportTable and then this scalar is set to the\n        certificate id that we want to save -\n        1. All entries in rlSslCertificateImportTable that have this id and\n        their format is equal to the current value of rlSslCertificateSaveFormat\n        are concatenated.\n        2. If the imported certificate format is .. - section 1 result\n        is validated against the key with the same index. If validation fails\n        for any reason - the certificate is not saved and the setting this\n        scalar fails.\n        3. If the imported certificate format is PKCS12 - section1 result is\n        decrypted using rlSslImportedPKCS12CertificatePassphrase current value.\n        If decryption fails for any reason the PKCS12 certificate and key are\n        not saved to FLASH and setting this scalar fails.')
rlSslCertificateSaveFormat = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("x509", 1), ("pkcs12", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateSaveFormat.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateSaveFormat.setDescription('.')
rlSslImportedPKCS12CertificatePassphrase = MibScalar((1, 3, 6, 1, 4, 1, 89, 100, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(8, 96))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslImportedPKCS12CertificatePassphrase.setStatus('current')
if mibBuilder.loadTexts: rlSslImportedPKCS12CertificatePassphrase.setDescription('.')
rlSslCertificateImportTable = MibTable((1, 3, 6, 1, 4, 1, 89, 100, 6), )
if mibBuilder.loadTexts: rlSslCertificateImportTable.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportTable.setDescription('This table is used for copying an external certificate to the device -\n    see rlSslCertificateSave')
rlSslCertificateImportEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 100, 6, 1), ).setIndexNames((0, "RADLAN-SSL", "rlSslCertificateImportId"), (0, "RADLAN-SSL", "rlSslCertificateImportFormat"), (0, "RADLAN-SSL", "rlSslCertificateImportFragmentId"))
if mibBuilder.loadTexts: rlSslCertificateImportEntry.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportEntry.setDescription(' The row definition for this table.')
rlSslCertificateImportId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportId.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportId.setDescription('The certificate ID.')
rlSslCertificateImportFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("x509", 1), ("pkcs12", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFormat.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportFormat.setDescription('.')
rlSslCertificateImportFragmentId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentId.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportFragmentId.setDescription('Identifies the index of this fragment in the certificate.')
rlSslCertificateImportFragmentText = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 4), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentText.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportFragmentText.setDescription('A part of the readable text entry for the certificate.')
rlSslCertificateImportFragmentStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 100, 6, 1, 5), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlSslCertificateImportFragmentStatus.setStatus('current')
if mibBuilder.loadTexts: rlSslCertificateImportFragmentStatus.setDescription('')
mibBuilder.exportSymbols("RADLAN-SSL", rlSslCertificateImportId=rlSslCertificateImportId, rlSslCertificateGenerationStateOrProvinceName=rlSslCertificateGenerationStateOrProvinceName, rlSslCertificateExportId=rlSslCertificateExportId, rlSslCertificateGenerationEntry=rlSslCertificateGenerationEntry, rlSslCertificateGenerationPassphrase=rlSslCertificateGenerationPassphrase, rlSslCertificateGenerationValidDays=rlSslCertificateGenerationValidDays, rlSslCertificateExportTable=rlSslCertificateExportTable, rlSslCertificateImportFragmentId=rlSslCertificateImportFragmentId, rlSslCertificateGenerationId=rlSslCertificateGenerationId, rlSslCertificateGenerationLocalityName=rlSslCertificateGenerationLocalityName, rlSslCertificateExportFragmentText=rlSslCertificateExportFragmentText, rlSslCertificateGenerationOrganizationName=rlSslCertificateGenerationOrganizationName, rlSslCertificateSaveFormat=rlSslCertificateSaveFormat, rlSslCertificateSave=rlSslCertificateSave, rlSslCertificateExportType=rlSslCertificateExportType, rlSslCertificateGenerationCommonName=rlSslCertificateGenerationCommonName, rlSslCertificateImportFormat=rlSslCertificateImportFormat, PYSNMP_MODULE_ID=rlSsl, rlSslCertificateGenerationCountryName=rlSslCertificateGenerationCountryName, rlSslCertificateExportEntry=rlSslCertificateExportEntry, rlSslCertificateGenerationRsaKeyLength=rlSslCertificateGenerationRsaKeyLength, rlSslCertificateGenerationOrganizationUnitName=rlSslCertificateGenerationOrganizationUnitName, rlSslCertificateExportFragmentId=rlSslCertificateExportFragmentId, rlSslCertificateImportFragmentStatus=rlSslCertificateImportFragmentStatus, rlSslCertificateGenerationTable=rlSslCertificateGenerationTable, rlSslCertificateGenerationIndex=rlSslCertificateGenerationIndex, rlSslImportedPKCS12CertificatePassphrase=rlSslImportedPKCS12CertificatePassphrase, rlSslCertificateImportTable=rlSslCertificateImportTable, rlSslCertificateImportEntry=rlSslCertificateImportEntry, rlSslCertificateImportFragmentText=rlSslCertificateImportFragmentText, rlSsl=rlSsl, rlSslCertificateGenerationAction=rlSslCertificateGenerationAction)
