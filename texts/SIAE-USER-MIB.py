#
# PySNMP MIB module SIAE-USER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/siae/SIAE-USER-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:31:57 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
siaeMib, = mibBuilder.importSymbols("SIAE-TREE-MIB", "siaeMib")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, NotificationType, ModuleIdentity, Unsigned32, Integer32, Gauge32, IpAddress, MibIdentifier, Bits, TimeTicks, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "NotificationType", "ModuleIdentity", "Unsigned32", "Integer32", "Gauge32", "IpAddress", "MibIdentifier", "Bits", "TimeTicks", "Counter64")
StorageType, RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "StorageType", "RowStatus", "DisplayString", "TextualConvention")
accessControl = ModuleIdentity((1, 3, 6, 1, 4, 1, 3373, 1103, 5))
accessControl.setRevisions(('2016-09-17 00:00', '2014-04-08 00:00', '2014-02-03 00:00', '2013-04-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: accessControl.setRevisionsDescriptions(('Added accessControlExtLoginTable.\n            ', 'Introduced accessControlGroupTelnet leaf\n             Fixed IMPORTS clause\n            ', 'Improved description of accessControlMibVersion\n            ', 'Initial version 01.00.00\n            ',))
if mibBuilder.loadTexts: accessControl.setLastUpdated('201609170000Z')
if mibBuilder.loadTexts: accessControl.setOrganization('SIAE MICROELETTRONICA spa')
if mibBuilder.loadTexts: accessControl.setContactInfo('SIAE MICROELETTONICA s.p.a.\n             Via Michelangelo Buonarroti, 21\n             20093 - Cologno Monzese\n             Milano - ITALY\n             Phone :  +39-02-27325-1\n             E-mail: tbd@siaemic.com\n            ')
if mibBuilder.loadTexts: accessControl.setDescription('User privileges and credentials for SIAE equipment access\n             control.\n            ')
accessControlMibVersion = MibScalar((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 1), Integer32().clone(1)).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlMibVersion.setStatus('current')
if mibBuilder.loadTexts: accessControlMibVersion.setDescription('Numerical version of this module.\n             The string version of this MIB have the following format:\n                XX.YY.ZZ\n             so, for example, the value 1 should be interpreted as 00.00.01\n             and the value 10001 should be interpreted as 01.00.01.')
accessControlGroupTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2), )
if mibBuilder.loadTexts: accessControlGroupTable.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupTable.setDescription('Table with Group records.')
accessControlGroupRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1), ).setIndexNames((0, "SIAE-USER-MIB", "accessControlGroupName"))
if mibBuilder.loadTexts: accessControlGroupRecord.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupRecord.setDescription('Group record. At most 10 records can be present in \n             accessControlGroupTable.')
accessControlGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupName.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupName.setDescription('ASCII string identifying the Group, used as index for the table.')
accessControlGroupProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("admin", 1), ("readwrite", 2), ("maintenance", 3), ("readonly", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupProfile.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupProfile.setDescription("This object defines the group access privileges. 'Admin' profile can \n             read and write all MIB, 'readwrite' profile can write all MIB leaves \n             but it can not manage users, 'maintenance' profile can do only manual \n             operations, while 'readonly' can only perform get operations.")
accessControlGroupHttp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupHttp.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupHttp.setDescription('This object allows or denies a given group using http protocol\n             for WebLct to access equipment.')
accessControlGroupHttps = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupHttps.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupHttps.setDescription('This object allows or denies a given group using https protocol\n            for WebLct to access equipment.')
accessControlGroupSnmp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("deny", 1), ("allowV1", 2), ("allowV2c", 3), ("allowV3", 4)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupSnmp.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupSnmp.setDescription('This object allows or denies a given group using snmp \n             protocol to access network equipment. If snmp protocol \n             is enabled, it is possible to choose between V1, V2c \n             and V3 versions of snmp.')
accessControlGroupFtp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupFtp.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupFtp.setDescription('This object allows or denies a given group using ftp \n             protocol.')
accessControlGroupSftp = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupSftp.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupSftp.setDescription('This object allows or denies a given group using sftp \n              protocol.')
accessControlGroupSsh = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupSsh.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupSsh.setDescription('This object allows or denies a given group using ssh \n              protocol.')
accessControlGroupRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlGroupRowStatus.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupRowStatus.setDescription('This object is used to manage a row in accessControlGroupTable.')
accessControlGroupCli = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 2, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("deny", 1), ("allow", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlGroupCli.setStatus('current')
if mibBuilder.loadTexts: accessControlGroupCli.setDescription("This object allows or denies a given group using both cli through \n             serial port and remote cli (telnet). Only 'admin' profile is\n             allowed to use cli and can execute all commands.")
accessControlUserTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3), )
if mibBuilder.loadTexts: accessControlUserTable.setStatus('current')
if mibBuilder.loadTexts: accessControlUserTable.setDescription('Table with User records. At most 10 records can be present in \n             accessControlUserTable.')
accessControlUserRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1), ).setIndexNames((0, "SIAE-USER-MIB", "accessControlUserName"))
if mibBuilder.loadTexts: accessControlUserRecord.setStatus('current')
if mibBuilder.loadTexts: accessControlUserRecord.setDescription('User record.')
accessControlUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserName.setStatus('current')
if mibBuilder.loadTexts: accessControlUserName.setDescription('ASCII string identifying the user.')
accessControlUserGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserGroupName.setStatus('current')
if mibBuilder.loadTexts: accessControlUserGroupName.setDescription('This object specifies which group this user belongs to.\n             It must refers to an entry of accessControlGroupTable.')
accessControlUserPwd = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserPwd.setStatus('current')
if mibBuilder.loadTexts: accessControlUserPwd.setDescription('This object specifies the login password of the specified\n             user.')
accessControlUserSnmpAuthProt = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAuth", 1), ("md5", 2), ("sha", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserSnmpAuthProt.setStatus('current')
if mibBuilder.loadTexts: accessControlUserSnmpAuthProt.setDescription('This object is used to set the user authentication protocol\n             if the related group can use snmp protocol.')
accessControlUserSnmpAuthKey = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 5), OctetString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserSnmpAuthKey.setStatus('current')
if mibBuilder.loadTexts: accessControlUserSnmpAuthKey.setDescription('This object specifies the user authentication key if\n             the related group can use snmpv3 protocol.')
accessControlUserSnmpPrivProt = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noPriv", 1), ("des", 2), ("aes", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserSnmpPrivProt.setStatus('current')
if mibBuilder.loadTexts: accessControlUserSnmpPrivProt.setDescription('This object is used to set the user cipher protocol if \n             the related group can use snmp protocol.')
accessControlUserSnmpPrivKey = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 127))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserSnmpPrivKey.setStatus('current')
if mibBuilder.loadTexts: accessControlUserSnmpPrivKey.setDescription('This object specifies the user cipher key if the related \n             group can use snmpv3 protocol.')
accessControlUserTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 3600)).clone(300)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserTimeout.setStatus('current')
if mibBuilder.loadTexts: accessControlUserTimeout.setDescription('This object defines the user timeout after login operation.\n             Zero timeout means no timeout.')
accessControlUserRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 3, 1, 9), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlUserRowStatus.setStatus('current')
if mibBuilder.loadTexts: accessControlUserRowStatus.setDescription('This object is used to manage an instance in accessControlUserTable.')
accessControlLoginTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4), )
if mibBuilder.loadTexts: accessControlLoginTable.setStatus('current')
if mibBuilder.loadTexts: accessControlLoginTable.setDescription('Table with Login records. At most 4 users via WebLct,\n             10 users via snmp and 10 users via cli can be logged \n             at the same time in the equipment.')
accessControlLoginRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1), ).setIndexNames((0, "SIAE-USER-MIB", "accessControlLoginIpAddress"), (0, "SIAE-USER-MIB", "accessControlLoginUserName"), (0, "SIAE-USER-MIB", "accessControlLoginType"))
if mibBuilder.loadTexts: accessControlLoginRecord.setStatus('current')
if mibBuilder.loadTexts: accessControlLoginRecord.setDescription('Login record. The create operation is performed by setting\n             accessControlLoginPwd object.')
accessControlLoginUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 1), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlLoginUserName.setStatus('current')
if mibBuilder.loadTexts: accessControlLoginUserName.setDescription('This object defines the name of the logged user.')
accessControlLoginIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 2), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlLoginIpAddress.setStatus('current')
if mibBuilder.loadTexts: accessControlLoginIpAddress.setDescription('This object defines the IP address of the logged user.')
accessControlLoginRequest = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("logout", 2), ("forcelogout", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accessControlLoginRequest.setStatus('current')
if mibBuilder.loadTexts: accessControlLoginRequest.setDescription("This object is used to do logout or to force logout \n             of other users. Only users with 'admin' profile can \n             force logout.")
accessControlLoginTrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accessControlLoginTrapEnable.setStatus('current')
if mibBuilder.loadTexts: accessControlLoginTrapEnable.setDescription('This object enables/disables trap receiver for a\n             given user.')
accessControlLoginType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("web", 1), ("snmp", 2), ("cli", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlLoginType.setStatus('current')
if mibBuilder.loadTexts: accessControlLoginType.setDescription('This object identifies login type.')
accessControlLoginPwd = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 6), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: accessControlLoginPwd.setStatus('current')
if mibBuilder.loadTexts: accessControlLoginPwd.setDescription('This object is used to create a row in the table. It\n             must correspond to the user password defined in \n             accessControlUserTable.')
accessControlLoginPolling = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1))).clone(namedValues=NamedValues(("polling", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlLoginPolling.setStatus('current')
if mibBuilder.loadTexts: accessControlLoginPolling.setDescription('This object is used to refresh the timeout of the related instance\n             of the table. To keep user logged in, manager must read this object \n             before the end of accessControlUserTimeout. For cli users execution \n             of cli commands refreshes timeout.')
accessControlClientTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5), )
if mibBuilder.loadTexts: accessControlClientTable.setStatus('current')
if mibBuilder.loadTexts: accessControlClientTable.setDescription('Table with records that show client credentials to \n             access FTP and SFTP services.')
accessControlClientRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1), ).setIndexNames((0, "SIAE-USER-MIB", "accessControlClientService"))
if mibBuilder.loadTexts: accessControlClientRecord.setStatus('current')
if mibBuilder.loadTexts: accessControlClientRecord.setDescription('Client credentials record for a given user.')
accessControlClientService = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ftp", 1), ("sftp", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientService.setStatus('current')
if mibBuilder.loadTexts: accessControlClientService.setDescription('This object is used to identify the service that a given user\n             can access as client.')
accessControlClientServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("disable", 1), ("enable", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientServiceStatus.setStatus('current')
if mibBuilder.loadTexts: accessControlClientServiceStatus.setDescription('This object is used to enable/disable the FTP/SFTP client\n             on the equipment. If both clients are enabled, SFTP client\n             is adopted.')
accessControlClientName = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientName.setStatus('current')
if mibBuilder.loadTexts: accessControlClientName.setDescription('ASCII string identifying the client name.')
accessControlClientPwd = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 4), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 31))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientPwd.setStatus('current')
if mibBuilder.loadTexts: accessControlClientPwd.setDescription('ASCII string identifying the client password.')
accessControlClientStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 5), StorageType().clone('nonVolatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientStorageType.setStatus('current')
if mibBuilder.loadTexts: accessControlClientStorageType.setDescription('The storage type for this conceptual row.\n                ')
accessControlClientRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 5, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: accessControlClientRowStatus.setStatus('current')
if mibBuilder.loadTexts: accessControlClientRowStatus.setDescription('The status of this conceptual row.')
accessControlExtLoginTable = MibTable((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6), )
if mibBuilder.loadTexts: accessControlExtLoginTable.setStatus('current')
if mibBuilder.loadTexts: accessControlExtLoginTable.setDescription('A table that contains additional information about\n            every user that is logged into the equipment.')
accessControlExtLoginRecord = MibTableRow((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6, 1), )
accessControlLoginRecord.registerAugmentions(("SIAE-USER-MIB", "accessControlExtLoginRecord"))
accessControlExtLoginRecord.setIndexNames(*accessControlLoginRecord.getIndexNames())
if mibBuilder.loadTexts: accessControlExtLoginRecord.setStatus('current')
if mibBuilder.loadTexts: accessControlExtLoginRecord.setDescription('Additional information record for a given logged \n            user.')
accessControlExtLoginProfile = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("admin", 1), ("readwrite", 2), ("maintenance", 3), ("readonly", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlExtLoginProfile.setStatus('current')
if mibBuilder.loadTexts: accessControlExtLoginProfile.setDescription("This object defines the access privileges associated to logged user. \n            'Admin' profile can read and write all MIB, 'readwrite' profile can \n            write all MIB leaves but it can not manage users, 'maintenance' can \n            do only manual operations, while 'readonly' can only perform get \n            operations. In case of local authentication, the user profile is found\n            in local database, while, if authentication is remote, the profile is \n            assigned by remote server.")
accessControlExtLoginAuthMode = MibTableColumn((1, 3, 6, 1, 4, 1, 3373, 1103, 5, 6, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("local", 1), ("remote", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: accessControlExtLoginAuthMode.setStatus('current')
if mibBuilder.loadTexts: accessControlExtLoginAuthMode.setDescription('This object shows if logged user has been authenticated locally or by remote \n            server (i.e RADIUS, TACACS, etc...).')
mibBuilder.exportSymbols("SIAE-USER-MIB", accessControl=accessControl, accessControlGroupSnmp=accessControlGroupSnmp, accessControlClientServiceStatus=accessControlClientServiceStatus, accessControlLoginIpAddress=accessControlLoginIpAddress, accessControlClientRowStatus=accessControlClientRowStatus, accessControlExtLoginTable=accessControlExtLoginTable, accessControlUserRowStatus=accessControlUserRowStatus, accessControlClientTable=accessControlClientTable, accessControlGroupSsh=accessControlGroupSsh, accessControlLoginTrapEnable=accessControlLoginTrapEnable, accessControlExtLoginAuthMode=accessControlExtLoginAuthMode, accessControlLoginRecord=accessControlLoginRecord, accessControlExtLoginRecord=accessControlExtLoginRecord, accessControlGroupHttps=accessControlGroupHttps, accessControlGroupRowStatus=accessControlGroupRowStatus, accessControlUserSnmpAuthProt=accessControlUserSnmpAuthProt, PYSNMP_MODULE_ID=accessControl, accessControlMibVersion=accessControlMibVersion, accessControlUserName=accessControlUserName, accessControlGroupTable=accessControlGroupTable, accessControlLoginPwd=accessControlLoginPwd, accessControlUserSnmpPrivProt=accessControlUserSnmpPrivProt, accessControlGroupFtp=accessControlGroupFtp, accessControlUserRecord=accessControlUserRecord, accessControlGroupSftp=accessControlGroupSftp, accessControlLoginPolling=accessControlLoginPolling, accessControlClientService=accessControlClientService, accessControlGroupHttp=accessControlGroupHttp, accessControlGroupCli=accessControlGroupCli, accessControlGroupName=accessControlGroupName, accessControlLoginUserName=accessControlLoginUserName, accessControlClientName=accessControlClientName, accessControlClientPwd=accessControlClientPwd, accessControlUserPwd=accessControlUserPwd, accessControlUserTimeout=accessControlUserTimeout, accessControlGroupProfile=accessControlGroupProfile, accessControlUserGroupName=accessControlUserGroupName, accessControlClientStorageType=accessControlClientStorageType, accessControlUserTable=accessControlUserTable, accessControlExtLoginProfile=accessControlExtLoginProfile, accessControlGroupRecord=accessControlGroupRecord, accessControlLoginType=accessControlLoginType, accessControlUserSnmpPrivKey=accessControlUserSnmpPrivKey, accessControlClientRecord=accessControlClientRecord, accessControlUserSnmpAuthKey=accessControlUserSnmpAuthKey, accessControlLoginTable=accessControlLoginTable, accessControlLoginRequest=accessControlLoginRequest)
