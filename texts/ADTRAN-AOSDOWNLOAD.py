#
# PySNMP MIB module ADTRAN-AOSDOWNLOAD (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/adtran/ADTRAN-AOSDOWNLOAD
# Produced by pysmi-1.1.8 at Fri Jan  7 16:08:26 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
adGenAOSConformance, adGenAOSCommon = mibBuilder.importSymbols("ADTRAN-AOS", "adGenAOSConformance", "adGenAOSCommon")
adIdentity, = mibBuilder.importSymbols("ADTRAN-MIB", "adIdentity")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, ObjectIdentity, Integer32, iso, ModuleIdentity, Bits, Counter32, NotificationType, IpAddress, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "Integer32", "iso", "ModuleIdentity", "Bits", "Counter32", "NotificationType", "IpAddress", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "MibIdentifier")
DisplayString, TDomain, TextualConvention, TAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TDomain", "TextualConvention", "TAddress", "RowStatus")
adAOSDownloadMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 664, 6, 10000, 53, 1, 3))
adAOSDownloadMib.setRevisions(('2004-09-21 22:16',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: adAOSDownloadMib.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: adAOSDownloadMib.setLastUpdated('200409212216Z')
if mibBuilder.loadTexts: adAOSDownloadMib.setOrganization('ADTRAN, Inc.')
if mibBuilder.loadTexts: adAOSDownloadMib.setContactInfo('        Technical Support Dept.\n                \tPostal: ADTRAN, Inc.\n                        901 Explorer Blvd.\n                        Huntsville, AL 35806\n\n                   Tel: +1 800 726-8663\n                   Fax: +1 256 963 6217\n                E-mail: support@adtran.com')
if mibBuilder.loadTexts: adAOSDownloadMib.setDescription('This MIB defines how the method for commanding an ADTRAN\n\t\t\tOS device to initiate a download or upload of configuration\n\t\t\tor firmware from a TFTP server ')
adAOSDownload = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3))
adAOSDownloadTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1), )
if mibBuilder.loadTexts: adAOSDownloadTable.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadTable.setDescription('A table of firmware downloads to this device.\n                   There will at any time be either 0 or 1 rows in\n                   this table, and the only valid index for this\n                   table is 1.  It is only a table so that we may\n                   take advantage of the RowStatus textual convention\n                   for configuring the download parameters.')
adAOSDownloadEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1), ).setIndexNames((0, "ADTRAN-AOSDOWNLOAD", "adAOSDownloadIndex"))
if mibBuilder.loadTexts: adAOSDownloadEntry.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadEntry.setDescription('The row in the adAOSDownloadTable containing the\n                   download parameters.')
adAOSDownloadIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("dlInstance", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadIndex.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadIndex.setDescription('The index which uniquely identifies this row.\n                   The only legal value for this object is 1.')
adAOSDownloadOwnerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 2), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadOwnerAddress.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadOwnerAddress.setDescription('The transport address of the management station\n                   that initiated this download attempt, formatted\n                   according to the value of the associated instance\n                   of adAOSDownloadOwnerDomain.')
adAOSDownloadOwnerDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 3), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadOwnerDomain.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadOwnerDomain.setDescription('The kind of transport service used by the\n                   management station that initiated this download\n                   attempt.')
adAOSDownloadTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 4), TAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadTAddress.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadTAddress.setDescription("The transport address of the node to download\n                   firmware from, formatted according to the value of\n                   the associated instance of adAOSDownloadTDomain.\n\n                   An attempt to modify this value will fail if the\n                   associated adAOSDownloadStatus object would be\n                   equal to 'active' both before and after the\n                   modification attempt.")
adAOSDownloadTDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 5), TDomain()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadTDomain.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadTDomain.setDescription("The kind of transport service to be used for the\n                   download.  Currently supports snmpUDPDomain and\n                   snmpIPXDomain.\n\n                   An attempt to modify this value will fail if the\n                   associated adAOSDownloadStatus object would be\n                   equal to 'active' both before and after the\n                   modification attempt.")
adAOSDownloadFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadFilename.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadFilename.setDescription("Filename and path of file to download (maximum\n                   length of 63 characters + NULL).\n\n                   An attempt to modify this value will fail if the\n                   associated adAOSDownloadStatus object would be\n                   equal to 'active' both before and after the\n                   modification attempt.")
adAOSDownloadResetType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noReset", 1), ("warmReset", 2), ("factoryReset", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadResetType.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadResetType.setDescription('The type of reset to perform after completion of\n                   the firmware download.  Note that not all agents\n                   will support all possible values, and there may\n                   be other agent-specific values for this object.')
adAOSDownloadErrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))).clone(namedValues=NamedValues(("fileNotFound", 1), ("accessViolation", 2), ("diskFull", 3), ("illegalOperation", 4), ("unknownTID", 5), ("fileExists", 6), ("noSuchUser", 7), ("notDefined", 8), ("corruptFile", 9), ("noServer", 10), ("tftpTimeout", 11), ("hardwareError", 12), ("success", 13), ("aborted", 14), ("inProgress", 15), ("idle", 16), ("erasingEeprom", 17), ("incompleteFirmware", 18), ("requirePowerCycle", 19), ("cannotUpgrade", 20), ("cannotDowngrade", 21)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadErrorStatus.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadErrorStatus.setDescription("Status of download.  The first seven codes are\n                   equal to the codes defined by the TFTP protocol.\n                   'notDefined' is the same as TFTP protocol error 0.\n                   The following are the other possible values for this\n                   object:\n\n                     corruptFile        - the agent detected a problem\n                                          with the download file format.\n                     noServer           - the TFTP server at\n                                          adAOSDownloadTAddress did not\n                                          respond to the TFTP request.\n                     tftpTimeout        - the download was aborted due\n                                          to excessive timeouts.\n                     hardwareError      - there was a hardware problem\n                                          on the agent that forced an\n                                          abort of the download (see\n                                          adAOSDownloadErrorText for\n                                          more detailed information).\n                     success            - the download has completed\n                                          successfully.\n                     aborted            - the download was aborted by\n                                          setting the\n                                          adAOSDownloadStatus to\n                                          'notInService' or 'delete'.\n                     inProgress         - the TFTP transfer is currently\n                                          active.\n                     idle               - means that the download has\n                                          not yet started (i.e. the\n                                          value of adAOSDownloadStatus\n                                          has not yet been set to\n                                          'active').\n                     erasingEeprom      - the agent is currently erasing\n                                          the EEPROM device.\n                     incompleteFirmware - the agent is running an\n                                          incomplete version of firmware\n                                          and requires a download.\n                     requirePowerCycle  - the agent must be power cycled\n                                          to run the newly downloaded\n                                          firmware.\n                     cannotUpgrade      - the agent's current firmware\n                                          revision cannot be upgraded to\n                                          the revision in the download\n                                          file.\n                     cannotDowngrade    - the agent's current firmware\n                                          revision cannot be downgraded\n                                          to the revision in the\n                                          download file.")
adAOSDownloadErrorText = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadErrorText.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadErrorText.setDescription('A textual description of the current error status\n                   of the firmware download.')
adAOSDownloadStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadStatus.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadStatus.setDescription("The status of this download entry.  This object\n                   may not be set to 'active' unless the following\n                   columnar objects exist in this row:\n                   adAOSDownloadTAddress, adAOSDownloadTDomain,\n                   adAOSDownloadFilename, and\n                   adAOSDownloadResetType.")
adAOSDownloadPassesLeft = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadPassesLeft.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadPassesLeft.setDescription("The number of passes remaining in the current\n                   download attempt.  Some agents require multiple\n                   passes through the download file in order to\n                   download a firmware image.  This object indicates\n                   the number of passes remaining, including the\n                   current pass.  The object is initialized by the\n                   agent to the number of passes required to complete\n                   the download when the corresponding instance of\n                   adAOSDownloadStatus is set to 'active'.  It is\n                   decremented by one each time a pass completes.")
adAOSDownloadOctetCount = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 12), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadOctetCount.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadOctetCount.setDescription("The number of octets that have been transferred\n                   during the current pass.  This object is initialized\n                   to zero by the agent when the corresponding instance\n                   of adAOSDownloadStatus is set to 'active', and\n                   reinitialized to zero at the beginning of each pass.")
adAOSDownloadDestination = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 13), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63)).clone('/os/primary')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadDestination.setStatus('deprecated')
if mibBuilder.loadTexts: adAOSDownloadDestination.setDescription("The destination of the download file.\n                   The allowable destination names depend on the type\n                   of agent being downloaded.  In all cases, a\n                   destination of '/os/primary' or '/os/secondary'\n\t\t   indicates that this is a download of the agent's\n                   firmware image.  The agent will use '/os/primary'\n\t\t   as the default value for this object when the row\n                   is created.\n\n                   ICF router agents also allow a download of a config\n                   file.  Currently, the name of the config file on the\n                   agent is '/config'.\n\n                   An agent should reject an attempt to set this object\n                   to a destination name that does not make sense for\n                   this type of agent.")
adAOSDownloadDestinationType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 1, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("primary", 1), ("secondary", 2), ("config", 3), ("remote", 4), ("other", 5))).clone(1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: adAOSDownloadDestinationType.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadDestinationType.setDescription("The destination of the download file.\n                   The allowable destination names depend on the type\n                   of agent being downloaded.  In all cases, a\n                   destination of  'primary(1)' or 'secondary(2)'\n                   indicates that this is a download of the agent's\n                   firmware image.  The agent will use 'primary(1)'\n                   as the default value for this object when the row\n                   is created.\n\n                   ICF router agents also allow a download of a config\n                   file.  Currently, the name of the config file on the\n                   agent is 'config(3)'.\n\n                   ICF router agents also allow a download of a\n                   file to a remote server. A destination of 'remote(4)'\n                   indicates that this is a download to a remote server.\n\n                    An agent should reject an attempt to set this object\n                   to a destination name that does not make sense for\n                   this type of agent.")
adAOSDownloadLogMaxSize = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadLogMaxSize.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadLogMaxSize.setDescription('The maximum number of the download log entries\n                   supported by this agent.  Note that 0 is a\n                   legal value for this variable.')
adAOSDownloadLogSize = MibScalar((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 3), Gauge32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDownloadLogSize.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadLogSize.setDescription('The number of download log entries currently in\n                   the adAOSDownloadLogTable.')
adAOSDownloadLogTable = MibTable((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4), )
if mibBuilder.loadTexts: adAOSDownloadLogTable.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadLogTable.setDescription('A log of the adAOSDownloadSize most recent\n                   download attempts to this device.  The first entry\n                   in the table is the oldest.')
adAOSDownloadLogEntry = MibTableRow((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1), ).setIndexNames((0, "ADTRAN-AOSDOWNLOAD", "adAOSDlLogIndex"))
if mibBuilder.loadTexts: adAOSDownloadLogEntry.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadLogEntry.setDescription('An entry in the adAOSDownloadLogTable containing\n                   information about a single download attempt.')
adAOSDlLogIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogIndex.setStatus('current')
if mibBuilder.loadTexts: adAOSDlLogIndex.setDescription('The index of this entry in the download log\n                   table.  Index 1 will always contain the oldest\n                   entry.  If the table is full when a download\n                   attempt is made, the new entry becomes the last\n                   entry (adAOSDownloadLogMaxSize), and all earlier\n                   entries are shifted down by one entry, removing\n                   the old index 1.')
adAOSDlLogOwnerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 2), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogOwnerAddress.setStatus('current')
if mibBuilder.loadTexts: adAOSDlLogOwnerAddress.setDescription('The transport address of the management station\n                   that attempted to initiate a download of this\n                   device, formatted according to the value of\n                   adAOSDlLastOwnerDomain.')
adAOSDlLogOwnerDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 3), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogOwnerDomain.setStatus('current')
if mibBuilder.loadTexts: adAOSDlLogOwnerDomain.setDescription('The kind of transport service used by the\n                   management station that attempted to initiate a\n                   download of this device.')
adAOSDlLogTAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 4), TAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogTAddress.setStatus('current')
if mibBuilder.loadTexts: adAOSDlLogTAddress.setDescription('The transport address of the node from which this\n                   device attempted to download firmware, formatted\n                   according to the value of adAOSDlLastTDomain.')
adAOSDlLogTDomain = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 5), TDomain()).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogTDomain.setStatus('current')
if mibBuilder.loadTexts: adAOSDlLogTDomain.setDescription('The kind of transport service which was used for\n                   the attempt to download firmware to this device.')
adAOSDlLogFilename = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 63))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogFilename.setStatus('current')
if mibBuilder.loadTexts: adAOSDlLogFilename.setDescription('The filename from which this device attempted to\n                   download firmware.')
adAOSDlLogResetType = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noReset", 1), ("warmReset", 2), ("factoryReset", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogResetType.setStatus('current')
if mibBuilder.loadTexts: adAOSDlLogResetType.setDescription('The type of reset requested to be  performed\n                   after completion of the firmware download\n                   attempt.')
adAOSDlLogErrorStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14))).clone(namedValues=NamedValues(("fileNotFound", 1), ("accessViolation", 2), ("diskFull", 3), ("illegalOperation", 4), ("unknownTID", 5), ("fileExists", 6), ("noSuchUser", 7), ("notDefined", 8), ("corruptFile", 9), ("noServer", 10), ("tftpTimeout", 11), ("hardwareError", 12), ("success", 13), ("aborted", 14)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogErrorStatus.setStatus('current')
if mibBuilder.loadTexts: adAOSDlLogErrorStatus.setDescription('The result of the attempt to download firmware to\n                   this device.  The values are the same as the\n                   corresponding values of adAOSDownloadErrorStatus.')
adAOSDlLogErrorText = MibTableColumn((1, 3, 6, 1, 4, 1, 664, 5, 53, 1, 3, 4, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: adAOSDlLogErrorText.setStatus('current')
if mibBuilder.loadTexts: adAOSDlLogErrorText.setDescription('A textual description of the final error status\n                   of the attempt to download firmware to this\n                   device.')
adAOSDownloadConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3))
adAOSDownloadCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 1))
adAOSDownloadGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 2))
adAOSDownloadConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 1, 1)).setObjects(("ADTRAN-AOSDOWNLOAD", "adAOSDownloadConfigGroup"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadLogGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSDownloadConfigCompliance = adAOSDownloadConfigCompliance.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadConfigCompliance.setDescription('New version of the compliance statement for\n                   network downloadable devices that allows\n                   for monitoring in-progress downloads and for\n                   directing a download to different destinations\n                   on the device.')
adAOSDownloadLogGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 2, 1)).setObjects(("ADTRAN-AOSDOWNLOAD", "adAOSDlLogIndex"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogOwnerAddress"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogOwnerDomain"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogTAddress"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogTDomain"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogFilename"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogResetType"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogErrorStatus"), ("ADTRAN-AOSDOWNLOAD", "adAOSDlLogErrorText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSDownloadLogGroup = adAOSDownloadLogGroup.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadLogGroup.setDescription('A collection of objects for maintaining a log of\n                   network download attempts to ICF devices.')
adAOSDownloadConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 664, 5, 53, 99, 3, 2, 2)).setObjects(("ADTRAN-AOSDOWNLOAD", "adAOSDownloadIndex"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadOwnerAddress"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadOwnerDomain"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadTAddress"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadTDomain"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadFilename"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadResetType"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadErrorStatus"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadErrorText"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadStatus"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadPassesLeft"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadOctetCount"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadDestination"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadLogMaxSize"), ("ADTRAN-AOSDOWNLOAD", "adAOSDownloadLogSize"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    adAOSDownloadConfigGroup = adAOSDownloadConfigGroup.setStatus('current')
if mibBuilder.loadTexts: adAOSDownloadConfigGroup.setDescription('A collection of objects for controlling and\n                   monitoring network download of device firmware to\n                   ICF devices.')
mibBuilder.exportSymbols("ADTRAN-AOSDOWNLOAD", adAOSDownloadMib=adAOSDownloadMib, adAOSDownloadLogTable=adAOSDownloadLogTable, adAOSDownloadOwnerAddress=adAOSDownloadOwnerAddress, adAOSDownloadLogEntry=adAOSDownloadLogEntry, adAOSDownloadIndex=adAOSDownloadIndex, adAOSDownloadOwnerDomain=adAOSDownloadOwnerDomain, adAOSDownloadPassesLeft=adAOSDownloadPassesLeft, adAOSDownloadCompliances=adAOSDownloadCompliances, adAOSDownloadTable=adAOSDownloadTable, adAOSDownloadOctetCount=adAOSDownloadOctetCount, PYSNMP_MODULE_ID=adAOSDownloadMib, adAOSDownloadLogGroup=adAOSDownloadLogGroup, adAOSDownloadDestinationType=adAOSDownloadDestinationType, adAOSDownloadConfigCompliance=adAOSDownloadConfigCompliance, adAOSDlLogFilename=adAOSDlLogFilename, adAOSDownloadErrorStatus=adAOSDownloadErrorStatus, adAOSDownloadTAddress=adAOSDownloadTAddress, adAOSDownloadLogSize=adAOSDownloadLogSize, adAOSDownloadLogMaxSize=adAOSDownloadLogMaxSize, adAOSDlLogErrorStatus=adAOSDlLogErrorStatus, adAOSDownloadConformance=adAOSDownloadConformance, adAOSDownloadTDomain=adAOSDownloadTDomain, adAOSDlLogTDomain=adAOSDlLogTDomain, adAOSDownloadFilename=adAOSDownloadFilename, adAOSDlLogErrorText=adAOSDlLogErrorText, adAOSDownloadErrorText=adAOSDownloadErrorText, adAOSDownloadStatus=adAOSDownloadStatus, adAOSDownload=adAOSDownload, adAOSDownloadGroups=adAOSDownloadGroups, adAOSDlLogTAddress=adAOSDlLogTAddress, adAOSDownloadResetType=adAOSDownloadResetType, adAOSDlLogResetType=adAOSDlLogResetType, adAOSDownloadDestination=adAOSDownloadDestination, adAOSDlLogOwnerAddress=adAOSDlLogOwnerAddress, adAOSDownloadEntry=adAOSDownloadEntry, adAOSDlLogOwnerDomain=adAOSDlLogOwnerDomain, adAOSDownloadConfigGroup=adAOSDownloadConfigGroup, adAOSDlLogIndex=adAOSDlLogIndex)
