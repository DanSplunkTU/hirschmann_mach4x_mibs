#
# PySNMP MIB module COMPAT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/COMPAT-MIB
# Produced by pysmi-1.1.8 at Sat Jan 15 17:49:46 2022
# On host fv-az121-65 platform Linux version 5.11.0-1025-azure by user runner
# Using Python version 3.10.1 (main, Dec 22 2021, 10:45:09) [GCC 9.3.0]
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
enterprises, Counter64, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, IpAddress, Gauge32, Bits, NotificationType, Counter32, Unsigned32, MibIdentifier, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Counter64", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "IpAddress", "Gauge32", "Bits", "NotificationType", "Counter32", "Unsigned32", "MibIdentifier", "ModuleIdentity", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

compatible = MibIdentifier((1, 3, 6, 1, 4, 1, 255))
compatVars = MibIdentifier((1, 3, 6, 1, 4, 1, 255, 1))
compatVPN = MibIdentifier((1, 3, 6, 1, 4, 1, 255, 2))
vpnLoginTable = MibIdentifier((1, 3, 6, 1, 4, 1, 255, 2, 1))
vPNTunnelTable = MibIdentifier((1, 3, 6, 1, 4, 1, 255, 2, 2))
failedLogins = MibScalar((1, 3, 6, 1, 4, 1, 255, 2, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: failedLogins.setStatus('mandatory')
if mibBuilder.loadTexts: failedLogins.setDescription('The number of failed logins since boot time.')
failedSecurID = MibScalar((1, 3, 6, 1, 4, 1, 255, 2, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: failedSecurID.setStatus('mandatory')
if mibBuilder.loadTexts: failedSecurID.setDescription('The number of failed Secure ID logins since boot time.')
failedRadiusAuth = MibScalar((1, 3, 6, 1, 4, 1, 255, 2, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: failedRadiusAuth.setStatus('mandatory')
if mibBuilder.loadTexts: failedRadiusAuth.setDescription('The number of failed RADIUS logins since boot time.')
processorUtilizationPercentage = MibScalar((1, 3, 6, 1, 4, 1, 255, 1, 1), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: processorUtilizationPercentage.setStatus('mandatory')
if mibBuilder.loadTexts: processorUtilizationPercentage.setDescription('The percentage of time the processor is spending not idle.')
vpnTunnelTable = MibTable((1, 3, 6, 1, 4, 1, 255, 2, 2, 1), )
if mibBuilder.loadTexts: vpnTunnelTable.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTable.setDescription('This table contains information useful\n\t\t    when tracking vpn tunnels currently active for this NAS.')
vpnTunnelTableEntry = MibTableRow((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1), ).setIndexNames((0, "COMPAT-MIB", "vpnTunnelTableIndex"))
if mibBuilder.loadTexts: vpnTunnelTableEntry.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableEntry.setDescription('The tunnel active table. An entry in this table is\n            uniquely identified by the value of the\n            vpnTunnelTableIndex variable to which the entry refers.')
vpnTunnelTableIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableIndex.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableIndex.setDescription('A unique value, greater than zero, for each tunnel\n            interface.')
vpnTunnelTableUserName = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableUserName.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableUserName.setDescription('The name of the VPN user')
vpnTunnelTableGroupName = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableGroupName.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableGroupName.setDescription('The name of the VPN group')
vpnTunnelTableIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 4), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableIpAddress.setDescription("The VPN partner's IP Address.")
vpnTunnelTableAssignedIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 5), IpAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableAssignedIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableAssignedIpAddress.setDescription("The Client's dynamically assigned IP Address.")
vpnTunnelTableIpBytesRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableIpBytesRcvd.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableIpBytesRcvd.setDescription('The total number of inbound IP bytes \n            handled by this tunnel as counted by the STEP layer.')
vpnTunnelTableIpBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableIpBytesSent.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableIpBytesSent.setDescription('The total number of outbound IP bytes \n            handled by this tunnel as counted by the STEP layer.')
vpnTunnelTableIpxBytesRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableIpxBytesRcvd.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableIpxBytesRcvd.setDescription('The total number of inbound IPX bytes \n            handled by this tunnel as counted by the STEP layer.')
vpnTunnelTableIpxBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 9), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableIpxBytesSent.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableIpxBytesSent.setDescription('The total number of outbound IPX bytes \n            handled by this tunnel as counted by the STEP layer.')
vpnTunnelTableAppletalkBytesRcvd = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableAppletalkBytesRcvd.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableAppletalkBytesRcvd.setDescription('The total number of inbound Appletalk bytes \n            handled by this tunnel as counted by the STEP layer.')
vpnTunnelTableAppletalkBytesSent = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 11), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableAppletalkBytesSent.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableAppletalkBytesSent.setDescription('The total number of outbound Appletalk bytes \n            handled by this tunnel as counted by the STEP layer.')
vpnTunnelTableUptime = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 12), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableUptime.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableUptime.setDescription('The time since the tunnel was established.')
vpnTunnelTableLatency = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 13), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableLatency.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableLatency.setDescription('SLA latency metric.')
vpnTunnelTableBandwidthOut = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 14), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableBandwidthOut.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableBandwidthOut.setDescription('SLA metric for measuring outbound\n\t\t    data bandwidth through this tunnel.')
vpnTunnelTableBandwidthReturn = MibTableColumn((1, 3, 6, 1, 4, 1, 255, 2, 2, 1, 1, 15), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: vpnTunnelTableBandwidthReturn.setStatus('mandatory')
if mibBuilder.loadTexts: vpnTunnelTableBandwidthReturn.setDescription('SLA metric for measuring inbound\n\t\t    data bandwidth through this tunnel.')
mibBuilder.exportSymbols("COMPAT-MIB", vpnTunnelTableUptime=vpnTunnelTableUptime, vpnTunnelTableBandwidthOut=vpnTunnelTableBandwidthOut, vpnTunnelTableIpxBytesRcvd=vpnTunnelTableIpxBytesRcvd, vpnTunnelTableIpAddress=vpnTunnelTableIpAddress, vpnTunnelTableLatency=vpnTunnelTableLatency, failedLogins=failedLogins, vpnTunnelTableGroupName=vpnTunnelTableGroupName, vpnTunnelTableAssignedIpAddress=vpnTunnelTableAssignedIpAddress, vpnTunnelTableIpBytesRcvd=vpnTunnelTableIpBytesRcvd, vpnTunnelTableUserName=vpnTunnelTableUserName, compatVPN=compatVPN, failedSecurID=failedSecurID, failedRadiusAuth=failedRadiusAuth, vpnLoginTable=vpnLoginTable, vpnTunnelTableIpBytesSent=vpnTunnelTableIpBytesSent, compatVars=compatVars, vpnTunnelTableIpxBytesSent=vpnTunnelTableIpxBytesSent, processorUtilizationPercentage=processorUtilizationPercentage, vpnTunnelTable=vpnTunnelTable, vpnTunnelTableBandwidthReturn=vpnTunnelTableBandwidthReturn, vPNTunnelTable=vPNTunnelTable, vpnTunnelTableIndex=vpnTunnelTableIndex, vpnTunnelTableAppletalkBytesRcvd=vpnTunnelTableAppletalkBytesRcvd, DisplayString=DisplayString, compatible=compatible, vpnTunnelTableEntry=vpnTunnelTableEntry, vpnTunnelTableAppletalkBytesSent=vpnTunnelTableAppletalkBytesSent)
