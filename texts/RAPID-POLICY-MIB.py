#
# PySNMP MIB module RAPID-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/nortel/RAPID-POLICY-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 18:14:58 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint")
rapidstream, = mibBuilder.importSymbols("RAPID-MIB", "rapidstream")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, ModuleIdentity, IpAddress, Integer32, Bits, Counter32, MibIdentifier, enterprises, Unsigned32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "ModuleIdentity", "IpAddress", "Integer32", "Bits", "Counter32", "MibIdentifier", "enterprises", "Unsigned32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "iso", "Gauge32")
DateAndTime, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TextualConvention")
rsPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4355, 4))
rsPolicyMIB.setRevisions(('2001-05-21 12:00', '2002-11-01 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rsPolicyMIB.setRevisionsDescriptions(('Initial revision.', 'Changed CONTACT-INFO.',))
if mibBuilder.loadTexts: rsPolicyMIB.setLastUpdated('0105211200Z')
if mibBuilder.loadTexts: rsPolicyMIB.setOrganization('WatchGuard Technologies, Inc.')
if mibBuilder.loadTexts: rsPolicyMIB.setContactInfo('   Ella Yu\n                      WatchGuard Technologies, Inc.\n                      1841 Zanker Road\n                      San Jose, CA 95112\n                      USA\n\n                      408-519-4888\n                      ella.yu@watchguard.com ')
if mibBuilder.loadTexts: rsPolicyMIB.setDescription('The MIB module describes various policy objects\n               of RapidStream system.')
rsPolicyToTunnel = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 4, 1))
if mibBuilder.loadTexts: rsPolicyToTunnel.setStatus('current')
if mibBuilder.loadTexts: rsPolicyToTunnel.setDescription('This is the base object identifier for all tunnels\n             information of the policies.')
rsPolicyStatistics = ObjectIdentity((1, 3, 6, 1, 4, 1, 4355, 4, 2))
if mibBuilder.loadTexts: rsPolicyStatistics.setStatus('current')
if mibBuilder.loadTexts: rsPolicyStatistics.setDescription('This is the base object identifier for all RASVPN user.')
rsPolicyToTunnelNum = MibScalar((1, 3, 6, 1, 4, 1, 4355, 4, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyToTunnelNum.setStatus('current')
if mibBuilder.loadTexts: rsPolicyToTunnelNum.setDescription('The total number of tunnels in the policytotunnel table. ')
rsPolicyToTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 4355, 4, 1, 2), )
if mibBuilder.loadTexts: rsPolicyToTunnelTable.setStatus('current')
if mibBuilder.loadTexts: rsPolicyToTunnelTable.setDescription('This is the policytotunnel table of all the policies.')
rsPolicyToTunnelEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4355, 4, 1, 2, 1), ).setIndexNames((0, "RAPID-POLICY-MIB", "rsPolicyToTunnelPolicyID"), (0, "RAPID-POLICY-MIB", "rsPolicyToTunnelTunnelID"))
if mibBuilder.loadTexts: rsPolicyToTunnelEntry.setStatus('current')
if mibBuilder.loadTexts: rsPolicyToTunnelEntry.setDescription('An entry (conceptual row) containing the tunnels\n            information.')
rsPolicyToTunnelPolicyID = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 1, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyToTunnelPolicyID.setStatus('current')
if mibBuilder.loadTexts: rsPolicyToTunnelPolicyID.setDescription('The policy identifier of this entity.')
rsPolicyToTunnelTunnelID = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 1, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyToTunnelTunnelID.setStatus('current')
if mibBuilder.loadTexts: rsPolicyToTunnelTunnelID.setDescription('The tunnel identifier of this entity.')
rsPolicyTableNum = MibScalar((1, 3, 6, 1, 4, 1, 4355, 4, 2, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyTableNum.setStatus('current')
if mibBuilder.loadTexts: rsPolicyTableNum.setDescription('The total number of policies in the policy table. ')
rsPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2), )
if mibBuilder.loadTexts: rsPolicyTable.setStatus('current')
if mibBuilder.loadTexts: rsPolicyTable.setDescription('This is the policytotunnel table of the policies.')
rsPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1), ).setIndexNames((0, "RAPID-POLICY-MIB", "rsPolicyID"))
if mibBuilder.loadTexts: rsPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: rsPolicyEntry.setDescription('An entry (conceptual row) containing the policy\n            information.')
rsPolicyID = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyID.setStatus('current')
if mibBuilder.loadTexts: rsPolicyID.setDescription('The policy identifier of this policy.')
rsPolicyName = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(32, 32)).setFixedLength(32)).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyName.setStatus('current')
if mibBuilder.loadTexts: rsPolicyName.setDescription('The policy name of this policy')
rsPolicyBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 3), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyBytes.setStatus('current')
if mibBuilder.loadTexts: rsPolicyBytes.setDescription('Total traffic in bytes since setting up this policy.')
rsPolicyPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyPackets.setStatus('current')
if mibBuilder.loadTexts: rsPolicyPackets.setDescription('Total traffic in packets since setting up this policy.')
rsPolicyIpsecDecryptErr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyIpsecDecryptErr.setStatus('current')
if mibBuilder.loadTexts: rsPolicyIpsecDecryptErr.setDescription('Total number of packets discarded due to decryption \n             errors since setting up this policy.')
rsPolicyIpsecAuthErr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 6), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyIpsecAuthErr.setStatus('current')
if mibBuilder.loadTexts: rsPolicyIpsecAuthErr.setDescription('Total number of packets discarded due to authentication  \n             errors since setting up this policy.')
rsPolicyIpsecReplayErr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 7), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyIpsecReplayErr.setStatus('current')
if mibBuilder.loadTexts: rsPolicyIpsecReplayErr.setDescription('Total number of packets discarded due to replay \n             errors since setting up this policy.')
rsPolicyIpsecPadErr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 8), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyIpsecPadErr.setStatus('current')
if mibBuilder.loadTexts: rsPolicyIpsecPadErr.setDescription('Total number of packets discarded due to pad value \n             errors since setting up this policy.')
rsPolicyIpsecPolicyErr = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 9), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyIpsecPolicyErr.setStatus('current')
if mibBuilder.loadTexts: rsPolicyIpsecPolicyErr.setDescription('Total number of packets discarded due to policy \n             errors since setting up this policy.')
rsPolicyFwDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 10), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyFwDisc.setStatus('current')
if mibBuilder.loadTexts: rsPolicyFwDisc.setDescription('Total number of packets discarded by firewall policies \n             since setting up this policy.')
rsPolicyOtherDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyOtherDisc.setStatus('current')
if mibBuilder.loadTexts: rsPolicyOtherDisc.setDescription('Total number of packets discarded due to errors \n             other than firewall errors, ipsec errors since setting up\n             this policy.')
rsPolicyActiveStreams = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 12), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyActiveStreams.setStatus('current')
if mibBuilder.loadTexts: rsPolicyActiveStreams.setDescription('Total number of the active connections since setting \n             up this policy.')
rsPolicyIpsecDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 13), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyIpsecDisc.setStatus('current')
if mibBuilder.loadTexts: rsPolicyIpsecDisc.setDescription('Total number of packets discarded by IPSEC errors \n             (decryption error, authentication error, replay error) \n             since setting up this policy.')
rsPolicyDisc = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 14), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyDisc.setStatus('current')
if mibBuilder.loadTexts: rsPolicyDisc.setDescription('Total number of packets discarded since setting up \n             this policy.')
rsPolicyNumTunl = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 15), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyNumTunl.setStatus('current')
if mibBuilder.loadTexts: rsPolicyNumTunl.setDescription('Total number of tunnels belong to this policy')
rsPolicySingleCntrNum = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 16), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicySingleCntrNum.setStatus('current')
if mibBuilder.loadTexts: rsPolicySingleCntrNum.setDescription('Total number of single counters handled by this policy.')
rsPolicyLogging = MibTableColumn((1, 3, 6, 1, 4, 1, 4355, 4, 2, 2, 1, 17), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("disabled", 0), ("enabled", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rsPolicyLogging.setStatus('current')
if mibBuilder.loadTexts: rsPolicyLogging.setDescription('Indicates whether if the logging of this policy has been enabled. ')
mibBuilder.exportSymbols("RAPID-POLICY-MIB", rsPolicyBytes=rsPolicyBytes, rsPolicyToTunnelTunnelID=rsPolicyToTunnelTunnelID, rsPolicyName=rsPolicyName, rsPolicyIpsecDisc=rsPolicyIpsecDisc, rsPolicyToTunnelPolicyID=rsPolicyToTunnelPolicyID, rsPolicyFwDisc=rsPolicyFwDisc, rsPolicyMIB=rsPolicyMIB, rsPolicyTable=rsPolicyTable, rsPolicyToTunnelTable=rsPolicyToTunnelTable, rsPolicyPackets=rsPolicyPackets, rsPolicyIpsecAuthErr=rsPolicyIpsecAuthErr, rsPolicyIpsecPadErr=rsPolicyIpsecPadErr, rsPolicyIpsecReplayErr=rsPolicyIpsecReplayErr, rsPolicyStatistics=rsPolicyStatistics, rsPolicyLogging=rsPolicyLogging, rsPolicyIpsecPolicyErr=rsPolicyIpsecPolicyErr, rsPolicyToTunnelEntry=rsPolicyToTunnelEntry, rsPolicyNumTunl=rsPolicyNumTunl, rsPolicyIpsecDecryptErr=rsPolicyIpsecDecryptErr, rsPolicyOtherDisc=rsPolicyOtherDisc, rsPolicyDisc=rsPolicyDisc, rsPolicyID=rsPolicyID, rsPolicySingleCntrNum=rsPolicySingleCntrNum, rsPolicyEntry=rsPolicyEntry, rsPolicyToTunnelNum=rsPolicyToTunnelNum, PYSNMP_MODULE_ID=rsPolicyMIB, rsPolicyTableNum=rsPolicyTableNum, rsPolicyToTunnel=rsPolicyToTunnel, rsPolicyActiveStreams=rsPolicyActiveStreams)
