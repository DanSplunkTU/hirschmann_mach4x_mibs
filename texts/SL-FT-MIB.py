#
# PySNMP MIB module SL-FT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/packetlight/SL-FT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:15:40 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
IANAifType, = mibBuilder.importSymbols("IANAifType-MIB", "IANAifType")
ifIndex, ifAlias = mibBuilder.importSymbols("IF-MIB", "ifIndex", "ifAlias")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
PerfCurrentCount, PerfIntervalCount, PerfTotalCount = mibBuilder.importSymbols("PerfHist-TC-MIB", "PerfCurrentCount", "PerfIntervalCount", "PerfTotalCount")
slMain, = mibBuilder.importSymbols("SL-MAIN-MIB", "slMain")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, ModuleIdentity, IpAddress, Integer32, Counter64, ObjectIdentity, Unsigned32, MibIdentifier, Bits, NotificationType, enterprises, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "ModuleIdentity", "IpAddress", "Integer32", "Counter64", "ObjectIdentity", "Unsigned32", "MibIdentifier", "Bits", "NotificationType", "enterprises", "Gauge32", "Counter32")
TimeStamp, DisplayString, RowStatus, RowPointer, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "TimeStamp", "DisplayString", "RowStatus", "RowPointer", "TruthValue", "TextualConvention")
class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

slFt = ModuleIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30))
if mibBuilder.loadTexts: slFt.setLastUpdated('200007240000Z')
if mibBuilder.loadTexts: slFt.setOrganization('PacketLight Networks Ltd.')
if mibBuilder.loadTexts: slFt.setContactInfo('Omri_Viner@PacketLight.com')
if mibBuilder.loadTexts: slFt.setDescription('This MIB module describes the file transfer operations')
slFtGen = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1))
slFtSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 1))
slFtAgnt = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2))
slFtFileTransfer = MibIdentifier((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12))
class SftpUserLogin(DisplayString):
    description = 'The SFTP User Login Type.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

class SftpUserPassword(DisplayString):
    description = 'The SFTP User Password Type.'
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(1, 20)

slFtFileServerIP = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 1), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileServerIP.setStatus('current')
if mibBuilder.loadTexts: slFtFileServerIP.setDescription('The IP address of the server from which the file is loaded ')
slFtFileName = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileName.setStatus('current')
if mibBuilder.loadTexts: slFtFileName.setDescription('The name of the file to be loaded. For protection, read returns\n\t NULL. ')
slFtFileTransCmd = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 255))).clone(namedValues=NamedValues(("swDwnLoad", 1), ("configDwnLoad", 2), ("configUpLoad", 3), ("coProcDwnLoad", 4), ("stateUpLoad", 5), ("dwnLoadUserFile", 6), ("upLoadUserFile", 7), ("swDwnLoadAndReset", 8), ("swUpLoad", 9), ("swDwnLoad2BkupStorage", 10), ("bootDwnLoad", 11), ("bootUpLoad", 12), ("swUpLoadFromBkupStorage", 13), ("licenseDwnLoad", 14), ("configDwnLoadToDefaultFile", 15), ("noOp", 255)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileTransCmd.setStatus('current')
if mibBuilder.loadTexts: slFtFileTransCmd.setDescription('The command to be executed on fileName at fileServerIP.')
slFtTftpRetryTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtTftpRetryTimeOut.setStatus('current')
if mibBuilder.loadTexts: slFtTftpRetryTimeOut.setDescription(' General Retransmission time-out value (seconds) ')
slFtTftpTotalTimeOut = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtTftpTotalTimeOut.setStatus('current')
if mibBuilder.loadTexts: slFtTftpTotalTimeOut.setDescription(' Total Retransmission time-out value (seconds) ')
slFtTftpStatus = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("noOp", 2), ("connecting", 3), ("transferringData", 4), ("endedTimeOut", 5), ("endedOk", 6), ("error", 7))).clone('noOp')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtTftpStatus.setStatus('current')
if mibBuilder.loadTexts: slFtTftpStatus.setDescription("Status of tftp session. When a session ended with success,\n    the tftpStatus should be endedOk(6). Before restarting a\n    tftp session, the NMS should set the tftpStatus to noOp(2).\n    That's the reason of MAX-ACCESS read-write to this field.")
slFtTftpError = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 7), OctetString().subtype(subtypeSpec=ValueSizeConstraint(2, 2)).setFixedLength(2).clone(hexValue="0000")).setMaxAccess("readonly")
if mibBuilder.loadTexts: slFtTftpError.setStatus('current')
if mibBuilder.loadTexts: slFtTftpError.setDescription(' The MSB represents the standard error code.\n    The LSB represents the private error code.\n\t0x0000 is No Error\n\t0x0100 is File Not Found\n\t0x0200 is Access violation\n\t0x0300 is Disk full or allocation exceeded\n\t0x0400 is Illegal TFTP operation\n\t0x0500 is Unknown transfer ID\n\t0x0600 is File already exists\n\t0x0700 is No such user\n\t0x0001 is Server Overflow\n\t0x0002 is No empty UDP port\n\t0x0003 is No empty connection\n\t0x0004 is Illegal File Mode\n\t0x0007 is Illegal PDU size\n\t0x0008 is TFTP Server does not exist \n\t0x0009 is Incorrect File\n\t0x000A is Wrong License format\n\t0x000B is License ID already used ')
slFtFileTransferToSubSystems = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 8), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1)).setFixedLength(1)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileTransferToSubSystems.setStatus('current')
if mibBuilder.loadTexts: slFtFileTransferToSubSystems.setDescription(" This object represents the sub-systems the fileTransCmd \n      refers to. It should be used when a system is divided \n      to sub-systems and each sub-system (or part of them) can \n\t  have a different SW/Configuration.\n\n\t  Each bit of this object will represent one of the sub-systems.\n\t  Bit='1' - APPLY to respective sub-system\n\t  Bit='0' - DO NOT APPLY to respective sub-system\n\n\t  For the meaning of each bit, see product's specification.\n\t  User will select the sub-systems envolved by filling-in the bits\n      that represent these sub-systems.\n      In this case, the file represented by 'fileName' will \n\t  include several parts, each representing one of the sub-systems.\n\t  The agent will refer only to the part/s indicated by this object.\n\n      0 Octet Strings = not applicable  \n      DEFVAL = 0h\tfor  the products that support this object.")
slFtFileNameWithinProduct = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 9), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileNameWithinProduct.setStatus('current')
if mibBuilder.loadTexts: slFtFileNameWithinProduct.setDescription('The file name used by the product within the product file system.')
slFtFileTransferServerPort = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 14), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileTransferServerPort.setStatus('current')
if mibBuilder.loadTexts: slFtFileTransferServerPort.setDescription('Server Port number used for File Transfer. \n     Applicable for SFTP.\n     Valid values: 0..65535.')
slFtFileTransferProtocol = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("tftp", 1), ("sftp", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtFileTransferProtocol.setStatus('current')
if mibBuilder.loadTexts: slFtFileTransferProtocol.setDescription('File Transfer protocol used.')
slFtSftpUserLogin = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 16), SftpUserLogin()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtSftpUserLogin.setStatus('current')
if mibBuilder.loadTexts: slFtSftpUserLogin.setDescription('The SFTP User Login.')
slFtSftpPasswordLogin = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 12, 17), SftpUserPassword()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtSftpPasswordLogin.setStatus('current')
if mibBuilder.loadTexts: slFtSftpPasswordLogin.setDescription('The SFTP User Password.')
slFtSystemReset = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("off", 2), ("on", 3), ("resetConfig", 4), ("resetMapping", 5), ("resetStandby", 6)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtSystemReset.setStatus('current')
if mibBuilder.loadTexts: slFtSystemReset.setDescription('Reset action to be performed on the system.\n\t - resetStandby(6) - can be used only by devices with redundancy on MAIN/CL.')
slFtAgnSwVersionSwapCmd = MibScalar((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 2, 51), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(2, 3))).clone(namedValues=NamedValues(("off", 2), ("mainAndBackup", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: slFtAgnSwVersionSwapCmd.setStatus('current')
if mibBuilder.loadTexts: slFtAgnSwVersionSwapCmd.setDescription('SW switch command.\n\t mainAndBackup (3) = Swap between Main SW and the backup one.\n\t Agent will perform the required command and change automatically \n\t the value of this object to off(2).')
slFtSystemsEvents = ObjectIdentity((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 1, 0))
if mibBuilder.loadTexts: slFtSystemsEvents.setStatus('current')
if mibBuilder.loadTexts: slFtSystemsEvents.setDescription('The system events for products.')
slFtTftpStatusChangeTrap = NotificationType((1, 3, 6, 1, 4, 1, 4515, 1, 3, 30, 1, 1, 0, 1)).setObjects(("SL-FT-MIB", "slFtTftpStatus"))
if mibBuilder.loadTexts: slFtTftpStatusChangeTrap.setStatus('current')
if mibBuilder.loadTexts: slFtTftpStatusChangeTrap.setDescription('This trap is sent whenever the status of tftp changed.')
mibBuilder.exportSymbols("SL-FT-MIB", slFtSftpUserLogin=slFtSftpUserLogin, slFtTftpStatus=slFtTftpStatus, SftpUserLogin=SftpUserLogin, slFtFileTransferProtocol=slFtFileTransferProtocol, slFtTftpStatusChangeTrap=slFtTftpStatusChangeTrap, slFtFileName=slFtFileName, slFtFileTransCmd=slFtFileTransCmd, slFtSystemsEvents=slFtSystemsEvents, slFtFileNameWithinProduct=slFtFileNameWithinProduct, slFtFileTransferServerPort=slFtFileTransferServerPort, slFt=slFt, SftpUserPassword=SftpUserPassword, slFtFileTransferToSubSystems=slFtFileTransferToSubSystems, slFtSftpPasswordLogin=slFtSftpPasswordLogin, slFtFileServerIP=slFtFileServerIP, slFtGen=slFtGen, slFtTftpError=slFtTftpError, slFtTftpTotalTimeOut=slFtTftpTotalTimeOut, slFtSystemReset=slFtSystemReset, slFtFileTransfer=slFtFileTransfer, PYSNMP_MODULE_ID=slFt, slFtAgnt=slFtAgnt, slFtAgnSwVersionSwapCmd=slFtAgnSwVersionSwapCmd, MacAddress=MacAddress, slFtSystems=slFtSystems, slFtTftpRetryTimeOut=slFtTftpRetryTimeOut)
