#
# PySNMP MIB module PRVT-LOAD-BALANCE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/telco-systems/binox/PRVT-LOAD-BALANCE-MIB
# Produced by pysmi-1.1.3 at Sun Nov 28 20:26:47 2021
# On host fv-az77-612 platform Linux version 5.11.0-1021-azure by user runner
# Using Python version 3.10.0 (default, Oct 18 2021, 13:54:29) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
ipSwitch, = mibBuilder.importSymbols("PRVT-SWITCH-MIB", "ipSwitch")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Counter64, TimeTicks, Unsigned32, Bits, Counter32, Gauge32, Integer32, ObjectIdentity, MibIdentifier, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Counter64", "TimeTicks", "Unsigned32", "Bits", "Counter32", "Gauge32", "Integer32", "ObjectIdentity", "MibIdentifier", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "NotificationType")
TextualConvention, TimeStamp, DisplayString, MacAddress, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "DisplayString", "MacAddress", "RowStatus")
prvtLoadBalMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 738, 10, 6, 7))
prvtLoadBalMIB.setRevisions(('2010-12-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: prvtLoadBalMIB.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: prvtLoadBalMIB.setLastUpdated('201012200000Z')
if mibBuilder.loadTexts: prvtLoadBalMIB.setOrganization('BATM Advanced Communication')
if mibBuilder.loadTexts: prvtLoadBalMIB.setContactInfo('BATM/Telco Systems Support team\n         Email:\n         For North America: techsupport@telco.com\n         For North Europe: support@batm.de, info@batm.de\n         For the rest of the world: techsupport@telco.com')
if mibBuilder.loadTexts: prvtLoadBalMIB.setDescription('The private MIB module for management of load balancing functionality.')
class PrvtLoadBalMtxIndexTC(TextualConvention, Unsigned32):
    description = 'A valid matrix group (load balancing application) index.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 8)

prvtLoadBalObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1))
prvtLoadBalDistributionMode = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("disabled", 1), ("general", 2), ("perPortUserNetwork", 3), ("globalNetwork", 4), ("globalUser", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalDistributionMode.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalDistributionMode.setDescription('The global distribution mode to use.')
prvtLoadBalIpV6DistributionMode = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalIpV6DistributionMode.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIpV6DistributionMode.setDescription('Specifies whether IPv6 distribution mode should be enabled/disabled.')
prvtLoadBalSpiDistributionMode = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalSpiDistributionMode.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalSpiDistributionMode.setDescription('Specifies whether SPI distribution mode should be enabled/disabled.')
prvtLoadBalMaxAvailSize = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 5), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLoadBalMaxAvailSize.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalMaxAvailSize.setDescription('The maximum number of elements available in the matrix according to the\n         configured global distribution mode and included protocols.')
prvtLoadBalMtxTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 6), )
if mibBuilder.loadTexts: prvtLoadBalMtxTable.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalMtxTable.setDescription('The matrix table.')
prvtLoadBalMtxEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 6, 1), ).setIndexNames((0, "PRVT-LOAD-BALANCE-MIB", "prvtLoadBalMtxIndex"))
if mibBuilder.loadTexts: prvtLoadBalMtxEntry.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalMtxEntry.setDescription('An entry belonging to prvtLoadBalMtxTable.')
prvtLoadBalMtxIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 6, 1, 1), PrvtLoadBalMtxIndexTC())
if mibBuilder.loadTexts: prvtLoadBalMtxIndex.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalMtxIndex.setDescription('Uniquely identifies a matrix (load-balancing application) entry.')
prvtLoadBalMtxBuckets = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 6, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 1024))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLoadBalMtxBuckets.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalMtxBuckets.setDescription('Specifies the buckets of the load-balancing matrix.\n         Each nibble specifies the CPU blade (1-12) that should handle\n         traffic belonging to the corresponding ACL rule. The high nibbles\n         corresponds to even ACL rules, the lower nibbles to odd ACL rules.\n         The number of valid nibbles is equal to prvtLoadBalMaxAvailSize.')
prvtLoadBalMtxSignature = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 6, 1, 3), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLoadBalMtxSignature.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalMtxSignature.setDescription('The MD5 signature of prvtLoadBalMtxBuckets.')
prvtLoadBalIfTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 7), )
if mibBuilder.loadTexts: prvtLoadBalIfTable.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfTable.setDescription('This table contains port specific configuration.')
prvtLoadBalIfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 7, 1), ).setIndexNames((0, "PRVT-LOAD-BALANCE-MIB", "prvtLoadBalIfId"))
if mibBuilder.loadTexts: prvtLoadBalIfEntry.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfEntry.setDescription('An entry belonging to prvtLoadBalIfTable.')
prvtLoadBalIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 7, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: prvtLoadBalIfId.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfId.setDescription('The port number to which this row applies.')
prvtLoadBalIfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 7, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLoadBalIfRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfRowStatus.setDescription('Row status of this table.')
prvtLoadBalIfMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 7, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("network", 1), ("user", 2), ("sync", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLoadBalIfMode.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfMode.setDescription('The mode in which this interface should function.')
prvtLoadBalIfMatrixIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 7, 1, 4), PrvtLoadBalMtxIndexTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLoadBalIfMatrixIndex.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfMatrixIndex.setDescription('The matrix index (prvtLoadBalMtxIndex) assigned to this interface.')
prvtLoadBalUserNtwkSrcIpv4Mask = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 8), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalUserNtwkSrcIpv4Mask.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalUserNtwkSrcIpv4Mask.setDescription('The user/network source IPv4 mask.')
prvtLoadBalUserNtwkDstIpv4Mask = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 9), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalUserNtwkDstIpv4Mask.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalUserNtwkDstIpv4Mask.setDescription('The user/network destination IPv4 mask.')
prvtLoadBalUserNtwkSrcIpv6Mask = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 10), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalUserNtwkSrcIpv6Mask.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalUserNtwkSrcIpv6Mask.setDescription('The user/network source IPv6 mask.')
prvtLoadBalUserNtwkDstIpv6Mask = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 11), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalUserNtwkDstIpv6Mask.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalUserNtwkDstIpv6Mask.setDescription('The user/network destination IPv6 mask.')
prvtLoadBalSpiMask = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 12), Unsigned32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalSpiMask.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalSpiMask.setDescription('The SPI mask.')
prvtLoadBalGeneralSrcIpv4Mask = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 13), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalGeneralSrcIpv4Mask.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalGeneralSrcIpv4Mask.setDescription('The general source IPv4 mask.')
prvtLoadBalGeneralDstIpv4Mask = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 14), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalGeneralDstIpv4Mask.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalGeneralDstIpv4Mask.setDescription('The general destination IPv4 mask.')
prvtLoadBalGeneralSrcIpv6Mask = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 15), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalGeneralSrcIpv6Mask.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalGeneralSrcIpv6Mask.setDescription('The general source IPv6 mask.')
prvtLoadBalGeneralDstIpv6Mask = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 16), Ipv6Address()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalGeneralDstIpv6Mask.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalGeneralDstIpv6Mask.setDescription('The general destination IPv6 mask.')
prvtLoadBalLastUpdateTime = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 17), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: prvtLoadBalLastUpdateTime.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalLastUpdateTime.setDescription('The value of sysUpTime when the configuration was last updated.')
prvtLoadBalApplyConfiguration = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("noAction", 0), ("apply", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalApplyConfiguration.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalApplyConfiguration.setDescription("Setting this object to the value 'apply' results in the configuration being\n         applied to the device.\n         Reads from the object always return 'noAction'.")
prvtLoadBalBladeTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 19), )
if mibBuilder.loadTexts: prvtLoadBalBladeTable.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalBladeTable.setDescription('This table contains blade specific configuration.')
prvtLoadBalBladeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 19, 1), ).setIndexNames((0, "PRVT-LOAD-BALANCE-MIB", "prvtLoadBalBladeIndex"))
if mibBuilder.loadTexts: prvtLoadBalBladeEntry.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalBladeEntry.setDescription('An entry belonging to prvtLoadBalBladeTable.')
prvtLoadBalBladeIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 19, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 12)))
if mibBuilder.loadTexts: prvtLoadBalBladeIndex.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalBladeIndex.setDescription('The index of the blade to which this row applies.')
prvtLoadBalBladeMacAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 19, 1, 3), MacAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLoadBalBladeMacAddr.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalBladeMacAddr.setDescription('The MAC address for this blade.')
prvtLoadBalBaseIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 20), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalBaseIpAddr.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalBaseIpAddr.setDescription('The base IP address.')
prvtLoadBalBaseIpAddrMask = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 21), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalBaseIpAddrMask.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalBaseIpAddrMask.setDescription('The mask associated with prvtCpMatrixBaseIpAddr.')
prvtLoadBalAdminPass = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 22), OctetString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalAdminPass.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalAdminPass.setDescription('Admin user password.')
prvtLoadBalQsfpPortsMode = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 23), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mode4x10g", 1), ("mode40g", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalQsfpPortsMode.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalQsfpPortsMode.setDescription("Gets to this object return the mode of the front panel QSFP ports.\n         Sets to this object will configure the mode of these ports.\n         Note that changing the mode requires the device to be reloaded to\n         manufacturing defaults.  Thus, sets to this object that change the\n         object's value will result in the device reloading to the default\n         configuration.")
prvtLoadBalIfVlanTable = MibTable((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 24), )
if mibBuilder.loadTexts: prvtLoadBalIfVlanTable.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfVlanTable.setDescription('This table contains port specific configuration.')
prvtLoadBalIfVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 24, 1), ).setIndexNames((0, "PRVT-LOAD-BALANCE-MIB", "prvtLoadBalIfId"), (0, "PRVT-LOAD-BALANCE-MIB", "prvtLoadBalVlanId"))
if mibBuilder.loadTexts: prvtLoadBalIfVlanEntry.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfVlanEntry.setDescription('An entry belonging to prvtLoadBalIfVlanTable.')
prvtLoadBalVlanId = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 24, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)))
if mibBuilder.loadTexts: prvtLoadBalVlanId.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalVlanId.setDescription('The port number and vlan to which this row applies.')
prvtLoadBalIfVlanRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 24, 1, 2), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLoadBalIfVlanRowStatus.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfVlanRowStatus.setDescription('Row status of this table.')
prvtLoadBalIfVlanMode = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 24, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("network", 1), ("user", 2)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLoadBalIfVlanMode.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfVlanMode.setDescription('The mode in which this interface and vlan should function.')
prvtLoadBalIfVlanMatrixIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 24, 1, 4), PrvtLoadBalMtxIndexTC()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: prvtLoadBalIfVlanMatrixIndex.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalIfVlanMatrixIndex.setDescription('The matrix index (prvtLoadBalMtxIndex) assigned to this interface and vlan.')
prvtLoadBalLoseLessMode = MibScalar((1, 3, 6, 1, 4, 1, 738, 10, 6, 7, 1, 25), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("mode1to64", 0), ("mode1to32", 1), ("mode1to16", 2), ("mode1to8", 3), ("mode1to4", 4), ("mode1to2", 5), ("mode1", 6), ("mode2", 7), ("mode4", 8), ("mode8", 9)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: prvtLoadBalLoseLessMode.setStatus('current')
if mibBuilder.loadTexts: prvtLoadBalLoseLessMode.setDescription('The lose-less mode to use.')
mibBuilder.exportSymbols("PRVT-LOAD-BALANCE-MIB", prvtLoadBalBladeTable=prvtLoadBalBladeTable, prvtLoadBalGeneralSrcIpv6Mask=prvtLoadBalGeneralSrcIpv6Mask, PrvtLoadBalMtxIndexTC=PrvtLoadBalMtxIndexTC, PYSNMP_MODULE_ID=prvtLoadBalMIB, prvtLoadBalUserNtwkSrcIpv6Mask=prvtLoadBalUserNtwkSrcIpv6Mask, prvtLoadBalIfVlanTable=prvtLoadBalIfVlanTable, prvtLoadBalIfTable=prvtLoadBalIfTable, prvtLoadBalMIB=prvtLoadBalMIB, prvtLoadBalDistributionMode=prvtLoadBalDistributionMode, prvtLoadBalUserNtwkDstIpv6Mask=prvtLoadBalUserNtwkDstIpv6Mask, prvtLoadBalBaseIpAddr=prvtLoadBalBaseIpAddr, prvtLoadBalLoseLessMode=prvtLoadBalLoseLessMode, prvtLoadBalMtxEntry=prvtLoadBalMtxEntry, prvtLoadBalVlanId=prvtLoadBalVlanId, prvtLoadBalIfMatrixIndex=prvtLoadBalIfMatrixIndex, prvtLoadBalObjects=prvtLoadBalObjects, prvtLoadBalMaxAvailSize=prvtLoadBalMaxAvailSize, prvtLoadBalIfVlanMode=prvtLoadBalIfVlanMode, prvtLoadBalBladeMacAddr=prvtLoadBalBladeMacAddr, prvtLoadBalSpiMask=prvtLoadBalSpiMask, prvtLoadBalApplyConfiguration=prvtLoadBalApplyConfiguration, prvtLoadBalIfVlanMatrixIndex=prvtLoadBalIfVlanMatrixIndex, prvtLoadBalIfMode=prvtLoadBalIfMode, prvtLoadBalBaseIpAddrMask=prvtLoadBalBaseIpAddrMask, prvtLoadBalIfVlanRowStatus=prvtLoadBalIfVlanRowStatus, prvtLoadBalGeneralDstIpv6Mask=prvtLoadBalGeneralDstIpv6Mask, prvtLoadBalIfId=prvtLoadBalIfId, prvtLoadBalLastUpdateTime=prvtLoadBalLastUpdateTime, prvtLoadBalMtxTable=prvtLoadBalMtxTable, prvtLoadBalBladeIndex=prvtLoadBalBladeIndex, prvtLoadBalMtxBuckets=prvtLoadBalMtxBuckets, prvtLoadBalGeneralSrcIpv4Mask=prvtLoadBalGeneralSrcIpv4Mask, prvtLoadBalMtxSignature=prvtLoadBalMtxSignature, prvtLoadBalAdminPass=prvtLoadBalAdminPass, prvtLoadBalMtxIndex=prvtLoadBalMtxIndex, prvtLoadBalIfRowStatus=prvtLoadBalIfRowStatus, prvtLoadBalIfEntry=prvtLoadBalIfEntry, prvtLoadBalGeneralDstIpv4Mask=prvtLoadBalGeneralDstIpv4Mask, prvtLoadBalQsfpPortsMode=prvtLoadBalQsfpPortsMode, prvtLoadBalSpiDistributionMode=prvtLoadBalSpiDistributionMode, prvtLoadBalUserNtwkSrcIpv4Mask=prvtLoadBalUserNtwkSrcIpv4Mask, prvtLoadBalIpV6DistributionMode=prvtLoadBalIpV6DistributionMode, prvtLoadBalIfVlanEntry=prvtLoadBalIfVlanEntry, prvtLoadBalUserNtwkDstIpv4Mask=prvtLoadBalUserNtwkDstIpv4Mask, prvtLoadBalBladeEntry=prvtLoadBalBladeEntry)
