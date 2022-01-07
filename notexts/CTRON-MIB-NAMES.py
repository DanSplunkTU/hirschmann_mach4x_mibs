#
# PySNMP MIB module CTRON-MIB-NAMES (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/enterasys/CTRON-MIB-NAMES
# Produced by pysmi-1.1.8 at Fri Jan  7 16:05:33 2022
# On host fv-az135-792 platform Linux version 5.11.0-1022-azure by user runner
# Using Python version 3.10.1 (main, Dec 14 2021, 13:12:05) [GCC 9.3.0]
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
cabletron, = mibBuilder.importSymbols("CTRON-OIDS", "cabletron")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Unsigned32, Integer32, iso, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, IpAddress, ObjectIdentity, TimeTicks, Gauge32, MibIdentifier, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Unsigned32", "Integer32", "iso", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "IpAddress", "ObjectIdentity", "TimeTicks", "Gauge32", "MibIdentifier", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4))
ctron = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1))
ctPhysical = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1))
repeaterRev4 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 1))
chassis = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 2))
ctPhysRptrMim = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 3))
ctPhysModule = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4))
ctPModuleETWMIM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 4, 1))
ctDevice = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 5))
ctDot5PhysMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 6))
ctps = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7))
ctenv = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 8))
ctChassis2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 9))
ctUPS = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 10))
ctTRStnAssign = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 11))
ctResource = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 12))
ctIFRemap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 13))
ctIFRemap2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 14))
ctOrpHSIM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 15))
ctPortMap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 16))
ctHSIMPhysMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 17))
ctCMM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 18))
ctDataLink = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2))
dot5 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 1))
ctsmtmib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 2))
ctBridge = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 3))
ctEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4))
ctCSMACD = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 1))
ctEthernetCtlParameters = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 4, 2))
ctFDDI = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5))
ctFDDIFnb = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 1))
ctFDDIStats = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 5, 2))
ctTokenRing = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6))
ctTokenRingFnb = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 6, 1))
ctronWan = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7))
ctWan = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 1))
ctRemoteAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 2))
ctWanServices = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 7, 3))
ctDLSW = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 8))
ctFastEthernet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 9))
ctATM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10))
ctATMConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 10, 1))
ctSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11))
ctsfSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1))
ctSFCS = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 1, 1))
ctFPS = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 11, 2))
ctINB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12))
ctINBinfo = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 1))
ctINBinfo2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 12, 2))
ctBroadcast = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 13))
ctPriorityExt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 14))
ctFPSServices = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 15))
ctVlanExt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16))
ctronVVD = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 18))
ctVVD = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 18, 1))
ctVoiceOverIP = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 18, 1, 1))
ctCDP = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 19))
ctSmartTrunkBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 20))
ctronVpnMonMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 21))
ctNetwork = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3))
nwDiagnostics = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 1))
ctTranslation = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 4))
ctIGMPBranch = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 5))
ctDirectory = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 6))
ctAliasMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 7))
ctApplication = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4))
ctNetManagement = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 2))
ctCATV = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 3))
ctCM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 3, 1))
ctHETS = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 3, 2))
ctWebView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 4, 4))
ctSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5))
ctPoMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 1))
ctErrLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 2))
ctBackplaneProto = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 3))
ctUPowerSupply = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 4))
ctFpRedundancy = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 5))
ctTrapTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 7))
ctDownLoad = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 8))
ctPIC = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 9))
ctFlash = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 10))
ctLFAP = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 11))
ctTxQArb = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 5, 12))
ctDcm = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 6))
ctTrapLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 44))
ctronExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2))
ctronDLM = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 1))
ctLicense = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 5))
ctX25 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 6))
ctFault = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 7))
ctGateway = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 8))
ctronHost = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 9))
ctronRunTimeDiag = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 10))
ctProfiler = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 11))
ctVLANMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 12))
ctDistMgt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 14))
ctRmonDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 15))
ctNetSim = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 17))
ctMemory = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 22))
ctEngTest = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 23))
flowPolicyPolling = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 24))
ctDemandAccess = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 27))
ctHWDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 28))
ctFWDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 29))
ctEntityStateTC = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 30))
ctEntityStateMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 31))
ctDhcpServerExpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 32))
ctFastPathProtectedPortMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 33))
ctArpAclExpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 34))
ctDhcpSnoopingExpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 35))
ctDynamicArpInspectionExpMib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 36))
ctronExtn = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3))
ctronChassis = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 1))
ctronRmon = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 2))
ctronMib2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 3))
ctActions = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 4))
ctAtmfLanEmulation = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5))
ctLeClient = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 1))
ctElan = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 2))
ctLes = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 3))
ctBus = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 3, 5, 4))
ctMidManager = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 4))
ctGateWay = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 4, 1))
ctronV2H = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 12))
v2h124_24MIB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 12, 30)).setLabel("v2h124-24MIB")
ctronAP3000 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 13))
ctronWslMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 14))
ctronTrapeze = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 15))
ctronInternal = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 100))
ctDefaults = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 100, 1))
ctEnet = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 100, 2))
mibBuilder.exportSymbols("CTRON-MIB-NAMES", ctDevice=ctDevice, ctGateway=ctGateway, ctUPowerSupply=ctUPowerSupply, ctIFRemap=ctIFRemap, ctronVpnMonMIB=ctronVpnMonMIB, ctronExtn=ctronExtn, ctIFRemap2=ctIFRemap2, ctTrapLog=ctTrapLog, ctSFCS=ctSFCS, ctFDDI=ctFDDI, ctActions=ctActions, ctEthernetCtlParameters=ctEthernetCtlParameters, ctPModuleETWMIM=ctPModuleETWMIM, ctDemandAccess=ctDemandAccess, ctUPS=ctUPS, ctCDP=ctCDP, ctronRunTimeDiag=ctronRunTimeDiag, ctVlanExt=ctVlanExt, ctronExp=ctronExp, ctTokenRingFnb=ctTokenRingFnb, ctAtmfLanEmulation=ctAtmfLanEmulation, ctLes=ctLes, flowPolicyPolling=flowPolicyPolling, ctEntityStateMib=ctEntityStateMib, ctFPSServices=ctFPSServices, ctTrapTable=ctTrapTable, ctronV2H=ctronV2H, ctBus=ctBus, ctronAP3000=ctronAP3000, ctronTrapeze=ctronTrapeze, ctDefaults=ctDefaults, ctronWan=ctronWan, ctNetManagement=ctNetManagement, ctron=ctron, ctVoiceOverIP=ctVoiceOverIP, ctps=ctps, ctDot5PhysMgmt=ctDot5PhysMgmt, ctBridge=ctBridge, ctLicense=ctLicense, ctBackplaneProto=ctBackplaneProto, ctNetwork=ctNetwork, ctPortMap=ctPortMap, ctWan=ctWan, ctATMConfig=ctATMConfig, ctDistMgt=ctDistMgt, ctVVD=ctVVD, ctLFAP=ctLFAP, ctProfiler=ctProfiler, ctFpRedundancy=ctFpRedundancy, ctronWslMIB=ctronWslMIB, ctMemory=ctMemory, ctDcm=ctDcm, ctVLANMib=ctVLANMib, ctINB=ctINB, ctDynamicArpInspectionExpMib=ctDynamicArpInspectionExpMib, ctOrpHSIM=ctOrpHSIM, ctDhcpServerExpMib=ctDhcpServerExpMib, ctResource=ctResource, ctEthernet=ctEthernet, ctElan=ctElan, ctronMib2=ctronMib2, ctHWDebug=ctHWDebug, ctenv=ctenv, ctHETS=ctHETS, ctSystem=ctSystem, ctDirectory=ctDirectory, ctronDLM=ctronDLM, ctronRmon=ctronRmon, ctRmonDebug=ctRmonDebug, ctPhysRptrMim=ctPhysRptrMim, ctFlash=ctFlash, ctTranslation=ctTranslation, ctCSMACD=ctCSMACD, ctronVVD=ctronVVD, ctX25=ctX25, ctINBinfo=ctINBinfo, ctFWDebug=ctFWDebug, ctronHost=ctronHost, ctronInternal=ctronInternal, ctApplication=ctApplication, nwDiagnostics=nwDiagnostics, ctLeClient=ctLeClient, ctNetSim=ctNetSim, ctWanServices=ctWanServices, ctSmartTrunkBranch=ctSmartTrunkBranch, ctPriorityExt=ctPriorityExt, ctIGMPBranch=ctIGMPBranch, ctTxQArb=ctTxQArb, chassis=chassis, ctTokenRing=ctTokenRing, ctDhcpSnoopingExpMib=ctDhcpSnoopingExpMib, ctPhysical=ctPhysical, ctAliasMib=ctAliasMib, ctWebView=ctWebView, ctINBinfo2=ctINBinfo2, ctFDDIStats=ctFDDIStats, ctRemoteAccess=ctRemoteAccess, ctChassis2=ctChassis2, ctEntityStateTC=ctEntityStateTC, ctFastEthernet=ctFastEthernet, ctDownLoad=ctDownLoad, ctPhysModule=ctPhysModule, ctBroadcast=ctBroadcast, ctMidManager=ctMidManager, ctCM=ctCM, ctFault=ctFault, ctPIC=ctPIC, v2h124_24MIB=v2h124_24MIB, ctTRStnAssign=ctTRStnAssign, ctGateWay=ctGateWay, ctDLSW=ctDLSW, repeaterRev4=repeaterRev4, ctronChassis=ctronChassis, ctHSIMPhysMib=ctHSIMPhysMib, dot5=dot5, mibs=mibs, ctFastPathProtectedPortMib=ctFastPathProtectedPortMib, ctPoMIB=ctPoMIB, ctCMM=ctCMM, ctFDDIFnb=ctFDDIFnb, ctsmtmib=ctsmtmib, ctDataLink=ctDataLink, ctFPS=ctFPS, ctArpAclExpMib=ctArpAclExpMib, ctErrLog=ctErrLog, ctATM=ctATM, ctCATV=ctCATV, ctEnet=ctEnet, ctsfSwitch=ctsfSwitch, ctEngTest=ctEngTest, ctSwitch=ctSwitch)
