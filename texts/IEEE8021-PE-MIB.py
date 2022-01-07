#
# PySNMP MIB module IEEE8021-PE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/standard/IEEE8021-PE-MIB
# Produced by pysmi-1.1.8 at Fri Jan  7 16:07:49 2022
# On host fv-az36-988 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
IEEE8021BridgePortNumberOrZero, IEEE8021PbbComponentIdentifier, ieee802dot1mibs, IEEE8021BridgePortNumber = mibBuilder.importSymbols("IEEE8021-TC-MIB", "IEEE8021BridgePortNumberOrZero", "IEEE8021PbbComponentIdentifier", "ieee802dot1mibs", "IEEE8021BridgePortNumber")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Bits, Counter64, Unsigned32, ModuleIdentity, TimeTicks, Counter32, NotificationType, IpAddress, Integer32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter64", "Unsigned32", "ModuleIdentity", "TimeTicks", "Counter32", "NotificationType", "IpAddress", "Integer32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "Gauge32")
TextualConvention, MacAddress, TruthValue, TimeStamp, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "TruthValue", "TimeStamp", "DisplayString")
ieee8021BridgePEMib = ModuleIdentity((1, 3, 111, 2, 802, 1, 1, 25))
ieee8021BridgePEMib.setRevisions(('2012-01-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ieee8021BridgePEMib.setRevisionsDescriptions(('Initial version published as part of IEEE Std. 802.1BR-2012',))
if mibBuilder.loadTexts: ieee8021BridgePEMib.setLastUpdated('201201220000Z')
if mibBuilder.loadTexts: ieee8021BridgePEMib.setOrganization('IEEE 802.1 Working Group')
if mibBuilder.loadTexts: ieee8021BridgePEMib.setContactInfo('WG-URL: http:////www.ieee802.org/1/\n            WG-EMail: stds-802-1-L@IEEE.ORG\n\n             Contact: Tony Jeffree\n              Postal: C/O IEEE 802.1 Working Group\n                      IEEE Standards Association\n                      445 Hoes Lane\n                      Piscataway\n                      NJ 08854\n                      USA\n              E-mail: stds-802-1-L@IEEE.ORG')
if mibBuilder.loadTexts: ieee8021BridgePEMib.setDescription('The PE MIB module for managing devices that support\n        Bridge Port Extension.\n\n        Unless otherwise indicated, the references in this MIB\n        module are to IEEE Std 802.1BR-2012.\n\n        Copyright (C) IEEE.\n        This version of this MIB module is part of \n        IEEE 802.1BR-2012; see the specification itself\n        for full legal notices.')
ieee8021BridgePENotifications = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 25, 1))
ieee8021BridgePEObjects = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 25, 2))
ieee8021BridgePEConformance = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 25, 3))
class IEEE802BridgePEEChannelIDTC(TextualConvention, Unsigned32):
    description = 'Textual convention of an E-Channel Identifier.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4194302)

class IEEE802BridgePETrafficClassValueTC(TextualConvention, Unsigned32):
    description = 'Indicates a traffic class. Values 0-7 correspond to\n        traffic classes.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 7)

class IEEE802BridgePETrafficSelectionAlgorithmTC(TextualConvention, Integer32):
    description = 'Indicates the Traffic Selection Algorithm\n        0: Strict Priority\n        1: Credit-based shaper\n        2: Enhanced transmission selection\n        3-254: Reserved for furture standardization\n        255: Vendor specific'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 255))
    namedValues = NamedValues(("tsaStrictPriority", 0), ("tsaCreditBasedShaper", 1), ("tsaEnhancedTransmission", 2), ("tsaVendorSpecific", 255))

class IEEE802BridgePETrafficClassBandwidthValue(TextualConvention, Unsigned32):
    description = 'Indicates the bandwidth in percent assigned to a\n        traffic class.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 100)

ieee8021BridgePEPortTable = MibTable((1, 3, 111, 2, 802, 1, 1, 25, 2, 1), )
if mibBuilder.loadTexts: ieee8021BridgePEPortTable.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPortTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortTable.setDescription('A table that contains per port information\n        related to Port Extension.  A row is created in this\n        table for any port on a Controlling Bridge that is\n        extended using Port Extension, including those ports\n        that provide communication to the Port Extenders\n        themselves.')
ieee8021BridgePEPortEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1), ).setIndexNames((0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortComponentId"), (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPort"), (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortType"))
if mibBuilder.loadTexts: ieee8021BridgePEPortEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortEntry.setDescription('A list of per port Port Extension objects.')
ieee8021BridgePEPortComponentId = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 1), IEEE8021PbbComponentIdentifier())
if mibBuilder.loadTexts: ieee8021BridgePEPortComponentId.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortComponentId.setDescription('The component identifier is used to distinguish between the\n        multiple virtual bridge instances within a PBB. In simple\n        situations where there is only a single component the default\n        value is 1.')
ieee8021BridgePEPort = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 2), IEEE8021BridgePortNumber())
if mibBuilder.loadTexts: ieee8021BridgePEPort.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPort.setDescription('The port number of the port for which this entry\n        contains bridge management information.')
ieee8021BridgePEPortType = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("pepCascade", 1), ("pepUpstream", 2), ("pepExtended", 3))))
if mibBuilder.loadTexts: ieee8021BridgePEPortType.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPortType.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortType.setDescription('The operational mode of a port participating in\n        Port Exension.  The enumerated values are:\n        pepCascade - the port is operating as a Cascade port\n        pepUpstream - the port is operating as an Upstream port\n        pepExtended - the port is operating as an Extended port')
ieee8021BridgePEPortUpstreamCSPAddress = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 4), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortUpstreamCSPAddress.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPortUpstreamCSPAddress.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortUpstreamCSPAddress.setDescription('The MAC address used for communication of the PE CSP\n        protocol of the device connected to the upstream port\n        of the Port Extender (which may be the Controlling \n        Bridge or an upstream Port Extender).  This provides\n        the hierarchal relationship in a cascade of Port\n        Extenders')
ieee8021BridgePEPortEcid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 5), IEEE802BridgePEEChannelIDTC()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortEcid.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPortEcid.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortEcid.setDescription('The default ECID assigend to this port and the port\n        on the Port Extender to which this port corresponds.')
ieee8021BridgePEPortNumber = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 6), IEEE8021BridgePortNumberOrZero()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortNumber.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPortNumber.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortNumber.setDescription('The Port number on the of the Port on the Port Extender,\n        or zero for the Upstream Port.')
ieee8021BridgePECounterDiscontinuityTime = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 7), TimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePECounterDiscontinuityTime.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePECounterDiscontinuityTime.setDescription('The value of sysUpTime on the most recent occasion at which\n        any one or more of the counters in this conceptaul row\n        suffered a discontinuity.  The relevant counters are the\n        specific instances associated with this conceptual row of \n        any Counter32 or Counter64 object. If no such discontinuities\n        have occurred since the last re-initialization of the local \n        management subsystem, then this object contains a zero value.')
ieee8021BridgePEPortRxrqErrorsBridge = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 8), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrqErrorsBridge.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrqErrorsBridge.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrqErrorsBridge.setDescription('The number of PE CSP flow control overflow errors\n        that have occured for requests on the Bridge.')
ieee8021BridgePEPortRxrspErrorsBridge = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 9), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrspErrorsBridge.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrspErrorsBridge.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrspErrorsBridge.setDescription('The number of PE CSP flow control overflow errors\n        that have occured for responses on the Bridge.')
ieee8021BridgePEPortRxrqErrorsPE = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 10), Counter64()).setUnits('frames').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrqErrorsPE.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrqErrorsPE.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrqErrorsPE.setDescription('The number of PE CSP flow control overflow errors\n        that have occured for requests on the Port Extender.')
ieee8021BridgePEPortRxrspErrorsPE = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 11), Counter64()).setUnits('octets').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrspErrorsPE.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrspErrorsPE.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPortRxrspErrorsPE.setDescription('The number of PE CSP flow control overflow errors\n        that have occured for responses on the Port Extender.')
ieee8021BridgePEPCP = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 12), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPCP.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPCP.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPCP.setDescription('Indicates whether the Port Exender supports\n        modification of the priority code point\n        table (true) or not (false).')
ieee8021BridgePEROW = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 13), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEROW.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEROW.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEROW.setDescription('Indicates whether the Port Extender supports\n        rows in the PCP table in addition to the 8P0D\n        row (true)or not (false).')
ieee8021BridgePEDEI = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 14), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEDEI.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEDEI.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEDEI.setDescription('Indicates whether the Port Extender supports\n        encoding of the Drop Eligible Indicatior (true)\n        or not (false).')
ieee8021BridgePECN = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 15), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePECN.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePECN.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePECN.setDescription('Indicates whether the Port Extender supports\n        Congestion Notification (true) or not (false).')
ieee8021BridgePEPFC = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 16), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEPFC.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEPFC.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEPFC.setDescription('Indicates whether the Port Extender supports\n        Priority-based flow control(true) or\n        not (false).')
ieee8021BridgePEExtPortEChannelsSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 17), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 1048575))).setUnits('E-channels').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEExtPortEChannelsSupported.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEExtPortEChannelsSupported.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEExtPortEChannelsSupported.setDescription('Indicates the number of Extended Port\n        E-channels supported by the Port Extender.')
ieee8021BridgePERemoteRepEChannelsSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 18), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 3145727))).setUnits('E-channels').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePERemoteRepEChannelsSupported.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePERemoteRepEChannelsSupported.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePERemoteRepEChannelsSupported.setDescription('Indicates the number of Remote Replication\n        E-channels supported by the Port Extender.')
ieee8021BridgePETCsSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 19), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setUnits('traffic classes').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePETCsSupported.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePETCsSupported.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePETCsSupported.setDescription('Indicates the number of traffic clasees\n        supported by the Port Extender.')
ieee8021BridgePEUtVLANsSupported = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 1, 1, 20), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 4094))).setUnits('VLANs').setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePEUtVLANsSupported.setReference('10.2.1')
if mibBuilder.loadTexts: ieee8021BridgePEUtVLANsSupported.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEUtVLANsSupported.setDescription('Indicates the number of untagged VLANs\n        supported by the Port Extender.')
ieee8021BridgePERemoteReplicationTable = MibTable((1, 3, 111, 2, 802, 1, 1, 25, 2, 2), )
if mibBuilder.loadTexts: ieee8021BridgePERemoteReplicationTable.setReference('10.3.1')
if mibBuilder.loadTexts: ieee8021BridgePERemoteReplicationTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePERemoteReplicationTable.setDescription('A table that contains one row for each Remote Replication\n        entry in the filtering database.')
ieee8021BridgePERemoteReplicationEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 25, 2, 2, 1), ).setIndexNames((0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortComponentId"), (0, "IEEE8021-PE-MIB", "ieee8021BridgePERREcid"))
if mibBuilder.loadTexts: ieee8021BridgePERemoteReplicationEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePERemoteReplicationEntry.setDescription('A list of Remote Replication objects.')
ieee8021BridgePERREcid = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 2, 1, 1), IEEE802BridgePEEChannelIDTC())
if mibBuilder.loadTexts: ieee8021BridgePERREcid.setReference('10.3.1')
if mibBuilder.loadTexts: ieee8021BridgePERREcid.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePERREcid.setDescription('The ECID assigend to this Remote Replication\n        filtering entry.')
ieee8021BridgePERRPortMap = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 2, 1, 2), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ieee8021BridgePERRPortMap.setReference('10.3.1')
if mibBuilder.loadTexts: ieee8021BridgePERRPortMap.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePERRPortMap.setDescription('The list of ports to which a frame is to be\n        replicated.')
ieee8021BridgePEETSTable = MibTable((1, 3, 111, 2, 802, 1, 1, 25, 2, 3), )
if mibBuilder.loadTexts: ieee8021BridgePEETSTable.setReference('10.2.2')
if mibBuilder.loadTexts: ieee8021BridgePEETSTable.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEETSTable.setDescription('A table that contains per port information\n        related to Enhanced Transmission Selection.\n        A row is created in this table for any port on a\n        Controlling Bridge that corresponds to a Cascade\n        Port. These objects refer to the ETS configuration \n        of the attached Upstream Port')
ieee8021BridgePEETSEntry = MibTableRow((1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1), ).setIndexNames((0, "IEEE8021-PE-MIB", "ieee8021BridgePEPortComponentId"), (0, "IEEE8021-PE-MIB", "ieee8021BridgePEPort"), (0, "IEEE8021-PE-MIB", "ieee8021BridgePEETSTrafficClass"))
if mibBuilder.loadTexts: ieee8021BridgePEETSEntry.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEETSEntry.setDescription('A list of per Cascade Port ETS objects.')
ieee8021BridgePEETSTrafficClass = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1, 1), IEEE802BridgePETrafficClassValueTC())
if mibBuilder.loadTexts: ieee8021BridgePEETSTrafficClass.setReference('10.2.3')
if mibBuilder.loadTexts: ieee8021BridgePEETSTrafficClass.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEETSTrafficClass.setDescription('Indicates the traffic class to\n        which this bandwidth applies')
ieee8021BridgePEETSTrafficSelectionAlgorthm = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1, 2), IEEE802BridgePETrafficSelectionAlgorithmTC()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021BridgePEETSTrafficSelectionAlgorthm.setReference('10.2.3')
if mibBuilder.loadTexts: ieee8021BridgePEETSTrafficSelectionAlgorthm.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEETSTrafficSelectionAlgorthm.setDescription('Inticates the Traffic Selection Algorthm \n        assigned to this traffic class')
ieee8021BridgePEETSBandwidth = MibTableColumn((1, 3, 111, 2, 802, 1, 1, 25, 2, 3, 1, 3), IEEE802BridgePETrafficClassBandwidthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ieee8021BridgePEETSBandwidth.setReference('10.2.3')
if mibBuilder.loadTexts: ieee8021BridgePEETSBandwidth.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEETSBandwidth.setDescription('Indicates the bandwidth assigned to this traffic class.')
ieee8021BridgePEGroups = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 25, 3, 1))
ieee8021BridgePECompliances = MibIdentifier((1, 3, 111, 2, 802, 1, 1, 25, 3, 2))
ieee8021BridgePEGroup = ObjectGroup((1, 3, 111, 2, 802, 1, 1, 25, 3, 1, 1)).setObjects(("IEEE8021-PE-MIB", "ieee8021BridgePEPortUpstreamCSPAddress"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortEcid"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortNumber"), ("IEEE8021-PE-MIB", "ieee8021BridgePECounterDiscontinuityTime"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrqErrorsBridge"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrspErrorsBridge"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrqErrorsPE"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPortRxrspErrorsPE"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPCP"), ("IEEE8021-PE-MIB", "ieee8021BridgePEROW"), ("IEEE8021-PE-MIB", "ieee8021BridgePEDEI"), ("IEEE8021-PE-MIB", "ieee8021BridgePECN"), ("IEEE8021-PE-MIB", "ieee8021BridgePEPFC"), ("IEEE8021-PE-MIB", "ieee8021BridgePEExtPortEChannelsSupported"), ("IEEE8021-PE-MIB", "ieee8021BridgePERemoteRepEChannelsSupported"), ("IEEE8021-PE-MIB", "ieee8021BridgePETCsSupported"), ("IEEE8021-PE-MIB", "ieee8021BridgePEUtVLANsSupported"), ("IEEE8021-PE-MIB", "ieee8021BridgePERRPortMap"), ("IEEE8021-PE-MIB", "ieee8021BridgePEETSTrafficSelectionAlgorthm"), ("IEEE8021-PE-MIB", "ieee8021BridgePEETSBandwidth"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021BridgePEGroup = ieee8021BridgePEGroup.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePEGroup.setDescription('The collection of objects used to represent\n        Port Extension management objects.')
ieee8021BridgePECompliance = ModuleCompliance((1, 3, 111, 2, 802, 1, 1, 25, 3, 2, 1)).setObjects(("IEEE8021-PE-MIB", "ieee8021BridgePEGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ieee8021BridgePECompliance = ieee8021BridgePECompliance.setStatus('current')
if mibBuilder.loadTexts: ieee8021BridgePECompliance.setDescription('The compliance statement for devices supporting PE\n        as defined in IEEE 802.1BR.')
mibBuilder.exportSymbols("IEEE8021-PE-MIB", ieee8021BridgePEPortUpstreamCSPAddress=ieee8021BridgePEPortUpstreamCSPAddress, ieee8021BridgePEETSBandwidth=ieee8021BridgePEETSBandwidth, ieee8021BridgePEGroup=ieee8021BridgePEGroup, ieee8021BridgePEObjects=ieee8021BridgePEObjects, ieee8021BridgePEPortRxrspErrorsBridge=ieee8021BridgePEPortRxrspErrorsBridge, ieee8021BridgePEDEI=ieee8021BridgePEDEI, ieee8021BridgePERemoteReplicationTable=ieee8021BridgePERemoteReplicationTable, ieee8021BridgePENotifications=ieee8021BridgePENotifications, ieee8021BridgePEExtPortEChannelsSupported=ieee8021BridgePEExtPortEChannelsSupported, ieee8021BridgePEUtVLANsSupported=ieee8021BridgePEUtVLANsSupported, ieee8021BridgePEROW=ieee8021BridgePEROW, ieee8021BridgePEMib=ieee8021BridgePEMib, ieee8021BridgePEPortNumber=ieee8021BridgePEPortNumber, ieee8021BridgePETCsSupported=ieee8021BridgePETCsSupported, ieee8021BridgePECompliances=ieee8021BridgePECompliances, ieee8021BridgePERemoteReplicationEntry=ieee8021BridgePERemoteReplicationEntry, ieee8021BridgePEPortType=ieee8021BridgePEPortType, IEEE802BridgePETrafficSelectionAlgorithmTC=IEEE802BridgePETrafficSelectionAlgorithmTC, ieee8021BridgePEETSTrafficClass=ieee8021BridgePEETSTrafficClass, IEEE802BridgePEEChannelIDTC=IEEE802BridgePEEChannelIDTC, ieee8021BridgePECN=ieee8021BridgePECN, ieee8021BridgePEPort=ieee8021BridgePEPort, ieee8021BridgePEPortRxrqErrorsPE=ieee8021BridgePEPortRxrqErrorsPE, ieee8021BridgePECounterDiscontinuityTime=ieee8021BridgePECounterDiscontinuityTime, ieee8021BridgePEPortRxrspErrorsPE=ieee8021BridgePEPortRxrspErrorsPE, ieee8021BridgePEPortTable=ieee8021BridgePEPortTable, ieee8021BridgePEPCP=ieee8021BridgePEPCP, ieee8021BridgePERRPortMap=ieee8021BridgePERRPortMap, ieee8021BridgePEETSEntry=ieee8021BridgePEETSEntry, ieee8021BridgePEPFC=ieee8021BridgePEPFC, ieee8021BridgePERREcid=ieee8021BridgePERREcid, ieee8021BridgePEETSTrafficSelectionAlgorthm=ieee8021BridgePEETSTrafficSelectionAlgorthm, ieee8021BridgePEETSTable=ieee8021BridgePEETSTable, PYSNMP_MODULE_ID=ieee8021BridgePEMib, ieee8021BridgePEConformance=ieee8021BridgePEConformance, ieee8021BridgePEPortRxrqErrorsBridge=ieee8021BridgePEPortRxrqErrorsBridge, ieee8021BridgePEPortEcid=ieee8021BridgePEPortEcid, ieee8021BridgePEGroups=ieee8021BridgePEGroups, ieee8021BridgePECompliance=ieee8021BridgePECompliance, ieee8021BridgePEPortComponentId=ieee8021BridgePEPortComponentId, ieee8021BridgePERemoteRepEChannelsSupported=ieee8021BridgePERemoteRepEChannelsSupported, ieee8021BridgePEPortEntry=ieee8021BridgePEPortEntry, IEEE802BridgePETrafficClassBandwidthValue=IEEE802BridgePETrafficClassBandwidthValue, IEEE802BridgePETrafficClassValueTC=IEEE802BridgePETrafficClassValueTC)
